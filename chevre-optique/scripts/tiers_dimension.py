"""
Partie XXIV : un tiers de dimension. Le terme 2/(3n²) de la partie I démontré en entier, tous les termes suivants,
et le facteur 2 entre les deux lectures du grain (le plan et l'aire).

    python3 scripts/tiers_dimension.py        # ≈ 40 s

Écrit resultats/tiers_dimension.md et figures/y1_tiers_dimension.png.

1. La démonstration : X = ρU, E = −n ln ρ exactement exponentielle, la série de l'équateur, les moments exacts de la
   coquille, la zone centrale (√m − 1)ⁿ, l'inversion. Ordre 1 : le simplexe. Ordre 2 : 2/(3n²). Reste borné par
   1 800/n³ pour n ≥ 100 (vérification exacte par polynômes).
2. Tous les termes : coefficients rationnels exacts, contrôle en haute précision (60 chiffres), divergence au rythme
   1/ln √2, troncature optimale ≈ 2^(−n/2)/n, les décimales en blocs en dimensions 10⁴ et 10⁵⁰.
3. Un tiers de dimension : r_n² = arête² du simplexe de dimension N, N − n croît de 0 à 1/3 ; 1/x₀ = n + 4/3 − ….
4. Le piquet n'importe où : k² = d² + (n − 1)/(n + 1) + 2/(3n²d²) + …, le c_n de la partie XVI, μ ≈ 2δ.
5. Le facteur 2 : Euclide (r² = 2R·(R − x₀)), la bande de largeur x₀ et de hauteur 2R, un cran, les lectures du grain.
"""

import logging
import math
import os
import sys
import time
from fractions import Fraction as Fr
from math import comb, factorial

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import betainc

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
ROUGE, VIOLET, VERT = "#d0342c", "#7d4fc4", "#1baf7a"
R2 = math.sqrt(2)
T0 = time.time()
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def sup(n):
    return str(n).translate(SUP)


def sci(x, chiffres=3):
    """3,52·10⁻⁷ : écriture scientifique à la française."""
    x = float(x)
    if x == 0:
        return "0"
    e = math.floor(math.log10(abs(x)))
    m = round(x / 10 ** e, chiffres - 1)
    if abs(m) >= 10:
        m, e = m / 10, e + 1
    return f"{fr(m, '{:.' + str(chiffres - 1) + 'f}')}·10{sup(e)}"


def frac(q):
    return str(q).replace("-", "−")


def terme(q, i, premier=False):
    """q/n^i écrit 8/(3n²), 2/n ou 2, avec son signe."""
    p, d = abs(q.numerator), q.denominator
    pn = "" if i == 0 else ("n" if i == 1 else f"n{sup(i)}")
    corps = str(p) if i == 0 else (f"{p}/{pn}" if d == 1 else f"{p}/({d}{pn})")
    if i == 0 and d > 1:
        corps = f"{p}/{d}"
    signe = ("−" if q < 0 else "") if premier else ("− " if q < 0 else "+ ")
    return signe + corps


def somme(coefs, i0=0):
    morceaux = [terme(q, i, premier=(k == 0)) for k, (i, q) in enumerate((i, q) for i, q in enumerate(coefs) if i >= i0 and q != 0)]
    return " ".join(morceaux)


def sci_log(l10):
    """Écrit 10^l10 sans passer par un flottant (pour les très petits nombres)."""
    e = math.floor(l10)
    return f"{fr(10 ** (l10 - e), '{:.2f}')}·10{sup(e)}"


# ===========================================================================
# La corde exacte, deux méthodes indépendantes
# ===========================================================================
def part_calotte(c, n):
    """P(U₁ ≥ c) pour U uniforme sur la sphère de dimension n − 1 (n réel permis)."""
    if c >= 1:
        return 0.0
    if c <= -1:
        return 1.0
    v = betainc(0.5, (n - 1) / 2, c * c)
    return 0.5 * (1 - v) if c >= 0 else 0.5 * (1 + v)


def broute_mu(n, d, mu):
    """P(|X − P|² ≤ k²), piquet à distance d, k² = d² + (n − 1)/(n + 1) + μ. Intégrale radiale avec E = −n ln ρ."""
    c = (n - 1) / (n + 1) + mu

    def f(s):
        r = math.exp(-s / n)
        tau = (math.expm1(-2 * s / n) + 2 / (n + 1) - mu) / (2 * d * r)  # (ρ² − c)/(2dρ), sans soustraction
        return math.exp(-s) * part_calotte(tau, n)
    k = math.sqrt(d * d + c)
    pts = sorted(p for p in (-n * math.log(x) for x in (k - d, d - k, d + k) if 0 < x < 1) if 0 < p < 60)
    return quad(f, 0, 60, points=pts or None, limit=400, epsabs=1e-16, epsrel=1e-13)[0] + math.exp(-60)


def mu_chevre(n, d=1.0):
    """Le ménisque généralisé μ = k² − d² − (n − 1)/(n + 1) de la chèvre (n réel ≥ 1,05)."""
    hi = 2.0 / n
    return brentq(lambda m: broute_mu(n, d, m) - 0.5, -0.2 / n, hi, xtol=1e-18, rtol=1e-13)


def W(n, th):
    """∫₀^θ sinⁿ par la récurrence de la partie IV (stable quand la valeur n'est pas exponentiellement petite)."""
    s, c = mp.sin(th), mp.cos(th)
    w, m0 = (th, 0) if n % 2 == 0 else (1 - c, 1)
    p, s2 = s ** (m0 + 1), s * s
    for m in range(m0 + 2, n + 1, 2):
        w = -p * c / m + mp.mpf(m - 1) / m * w
        p *= s2
    return w


def W_petit(n, th):
    """∫₀^θ sinⁿ pour θ ≤ π/2, en précision relative (série hypergéométrique)."""
    s = mp.sin(th)
    return s ** (n + 1) / (n + 1) * mp.hyp2f1(mp.mpf(1) / 2, mp.mpf(n + 1) / 2, mp.mpf(n + 3) / 2, s * s)


def corde2_hp(n, r2_depart, dps=60):
    """r_n² à dps chiffres : équation de la chèvre W_n(2α) − (2cos α)ⁿ W_n(α) = ½W_n(π) (partie I § 5.1), Newton."""
    with mp.workdps(dps + 20):
        demi = mp.sqrt(mp.pi) * mp.gamma(mp.mpf(n + 1) / 2) / mp.gamma(mp.mpf(n) / 2 + 1) / 2
        a = mp.acos(mp.sqrt(mp.mpf(r2_depart)) / 2)
        for _ in range(60):
            wa, c2 = W_petit(n, a), (2 * mp.cos(a)) ** n
            f = W(n, 2 * a) - c2 * wa - demi
            fp = mp.sin(2 * a) ** n + 2 * n * mp.sin(a) * c2 / (2 * mp.cos(a)) * wa
            a -= f / fp
            if abs(f / fp) < mp.mpf(10) ** (-dps - 8):
                break
        return +4 * mp.cos(a) ** 2


# ===========================================================================
# Le développement exact en 1/n (méthode de la démonstration, § 1)
# ===========================================================================
def developpement(J, zero, un, cst):
    """Coefficients de r_n² en puissances de ε = 1/n, indices 0 … J.

    Condition de médiane : Σ_j (−1)^j C(k, j)/(2j + 1) · E[τ^(2j+1)] = 0, k = (n − 3)/2,
    τ = (ρ² + 1 − m)/(2ρ), E[ρ^a] = n/(n + a). On l'écrit F(w) = Σ_s w^s B_s avec w = 1 − m (Horner)."""
    L = 2 * J + 2

    def mul(a, b):
        out = [zero] * L
        for i, x in enumerate(a):
            if x != 0:
                for j in range(L - i):
                    out[i + j] += x * b[j]
        return out
    B = [[zero] * L for _ in range(2 * J)]
    for j in range(J):
        p = 2 * j + 1
        poly = [un] + [zero] * (L - 1)
        for i in range(j):  # C(k, j)·ε^j, polynôme en ε
            poly = mul(poly, [un, cst(-(3 + 2 * i))] + [zero] * (L - 2))
        poly = [zero] * (J - j) + poly[: L - J + j]  # on travaille sur ε^J·F
        coef = cst((-1) ** j) / cst(2 ** j * factorial(j) * (2 * j + 1) * 2 ** p)
        for s in range(p + 1):
            geo = [cst((p - 2 * s) ** t * (-1) ** t) for t in range(L)]  # E[ρ^(2i−p)] = 1/(1 + (2i − p)ε), i = p − s
            terme = mul(poly, geo)
            for t in range(L):
                B[s][t] += coef * cst(comb(p, s)) * terme[t]
    w = [cst(-1)] + [cst(2 * (-1) ** (t + 1)) for t in range(1, L)]  # w = 1 − 2n/(n + 1)
    for i in range(2, J + 1):
        acc = [zero] * L
        for s in range(2 * J - 1, -1, -1):
            acc = mul(acc, w)
            for t in range(L):
                acc[t] += B[s][t]
        w[i] -= 2 * acc[J + i]  # F ≈ −μ/2 : on corrige l'ordre i
    return [1 - w[0]] + [-x for x in w[1: J + 1]]


R2N = developpement(14, Fr(0), Fr(1), Fr)  # r² = Σ R2N[i]/n^i, exact
MU_C = {i: R2N[i] - 2 * (-1) ** i for i in range(2, len(R2N))}  # μ = r² − 2n/(n + 1) = Σ MU_C[i]/n^i
assert MU_C[2] == Fr(2, 3) and MU_C[3] == Fr(-98, 15) and MU_C[4] == Fr(5966, 105)
mp.mp.dps = 170
R2N_MP = developpement(30, mp.mpf(0), mp.mpf(1), mp.mpf)  # 30 termes en flottants à 170 chiffres
mp.mp.dps = 60
assert all(abs(R2N_MP[i] - mp.mpf(R2N[i].numerator) / R2N[i].denominator) < mp.mpf(10) ** -40 * abs(R2N_MP[i])
           for i in range(1, 15))
T_SERIE = time.time() - T0


def serie(n, J, coefs=None):
    """Somme partielle Σ_{i ≤ J} c_i/n^i de r² (en haute précision)."""
    coefs = R2N_MP if coefs is None else coefs
    x = mp.mpf(1) / n
    return sum(coefs[i] * x ** i for i in range(J + 1))


ligne("# Partie XXIV : un tiers de dimension")
ligne()
ligne("Résultats calculés par `scripts/tiers_dimension.py`.")
ligne()

# ===========================================================================
# 1. La démonstration
# ===========================================================================
ligne("## 1. La démonstration du terme 2/(3n²)")
ligne()
ligne("**L'écriture exacte.** X = ρU, U uniforme sur la sphère, ρⁿ uniforme sur [0, 1]. Donc E = −n ln ρ suit "
      "*exactement* la loi exponentielle : P(E > t) = P(ρⁿ < e^(−t)) = e^(−t). (La partie I utilisait n(1 − ρ), "
      "seulement asymptotiquement exponentielle.)")
ligne("La condition |X − P|² ≤ m s'écrit U₁ ≥ τ(ρ) = (ρ² + 1 − m)/(2ρ), et sur la coquille extérieure (ρ = 1), "
      "τ = 1 − m/2 = x₀ : τ est le plan de la lentille vu depuis chaque coquille.")
ligne()

nn, mm = sp.symbols("n m", positive=True)


def Mp_sym(p, m):
    return sp.Rational(1, 2 ** p) * sum(comb(p, i) * (1 - m) ** (p - i) * nn / (nn + 2 * i - p) for i in range(p + 1))


ordre1 = sp.solve(sp.Eq(Mp_sym(1, mm), 0), mm)[0]
assert sp.simplify(ordre1 - 2 * nn / (nn + 1)) == 0
g2_moments = sp.simplify((nn / (nn + 1)) / (nn / (nn - 1)))
assert sp.simplify(g2_moments - (nn - 1) / (nn + 1)) == 0
Eexp = sp.Symbol("E", positive=True)
skew = sp.integrate((1 - Eexp) ** 3 * sp.exp(-Eexp), (Eexp, 0, sp.oo))
assert skew == -2
ligne("**Ordre 1 : le simplexe.** E[τ] = ½(E[ρ] + (1 − m)E[ρ⁻¹]) = 0 donne exactement m = "
      "2n/(n + 1), l'arête² du simplexe (partie VI).")
ligne("Autrement dit, k² − d² = E[ρ]/E[ρ⁻¹] = (n − 1)/(n + 1) : la projection g² de la partie XVI, par un troisième "
      "calcul (après Archimède et Parseval).")
ligne()
ligne(f"**Ordre 2.** E[τ] = (k/3)·E[τ³], avec k = (n − 3)/2 ≈ n/2 (courbure de l'équateur) et "
      f"E[τ³] ≈ E[(1 − E)³]/n³ = {fr(int(skew), '{}')}/n³ (asymétrie de la coquille). Comme E[τ] = −(μ/2)·n/(n − 1) :")
ligne("μ/2 ≈ (n/6)·(2/n³), donc μ ≈ 2/(3n²). Le calcul exact (§ 2) donne bien μ = 2/(3n²) − 98/(15n³) + ….")
ligne()

# Vérification assistée de la borne explicite
nn2, tt = sp.symbols("n t", positive=True)


def Mp_n(p, m):
    return sp.Rational(1, 2 ** p) * sum(comb(p, i) * (1 - m) ** (p - i) * nn2 / (nn2 + 2 * i - p) for i in range(p + 1))


F2 = lambda m: Mp_n(1, m) - (nn2 - 3) / 6 * Mp_n(3, m)  # noqa: E731
EE5 = sum(comb(5, i) * sp.Rational(11, 10) ** (5 - i) * factorial(i) for i in range(6))
C_RESTE = sp.Rational(1, 40) * sp.Rational(5, 2) ** 5 * EE5  # (n²/8)·(1/5)·(2,5/n)⁵·E[(E + 1,1)⁵]
C_BORNE, N0 = 1800, 100
M_APP = 2 * nn2 / (nn2 + 1) + sp.Rational(2, 3) / nn2 ** 2
PREUVE = True
for signe in (1, -1):
    expr = F2(M_APP + signe * sp.Integer(C_BORNE) / nn2 ** 3) + signe * (C_RESTE / nn2 ** 3 + 1 / nn2 ** 4)
    num, den = sp.fraction(sp.together(sp.expand(expr)))
    pn = sp.Poly(sp.expand(-signe * num.subs(nn2, N0 + tt)), tt).all_coeffs()
    pd = sp.Poly(sp.expand(den.subs(nn2, N0 + tt)), tt).all_coeffs()
    PREUVE &= all(c >= 0 for c in pn) and pn[-1] > 0 and all(c >= 0 for c in pd)
assert PREUVE
ligne("**Le reste et l'inversion (borne explicite).**")
ligne("- Série de l'équateur : ∫₀^τ (1 − u²)^k du = τ − kτ³/3 + R, |R| ≤ C(k, 2)|τ|⁵/5 (Lagrange, k ≥ 2).")
ligne("- Pour ρ ≥ ρ₀ = √m − 1 ≥ 0,4 : |τ| ≤ (E + a)/(nρ₀), avec m = 2 − 2a/n, a ≤ 1,1. Donc "
      f"|R| ≤ (n²/8)(1/5)(2,5/n)⁵·E[(E + 1,1)⁵] = {fr(float(C_RESTE), '{:.1f}')}/n³ "
      f"(E[(E + 1,1)⁵] = {fr(float(EE5), '{:.2f}')}).")
ligne("- Zone centrale ρ < ρ₀ (toujours broutée) : poids ρ₀ⁿ ≈ (√2 − 1)ⁿ, borné ici par 1/n⁴.")
ligne(f"- Inversion : la fraction broutée croît avec m. On vérifie exactement (polynômes en t = n − {N0} à coefficients "
      f"positifs) que la condition change de signe entre m± = 2n/(n + 1) + 2/(3n²) ± {C_BORNE}/n³. "
      f"**Résultat : |r_n² − 2n/(n + 1) − 2/(3n²)| < {C_BORNE}/n³ pour tout n ≥ {N0}.** Vérification : "
      f"{'faite' if PREUVE else 'ÉCHEC'}.")
MARGE = min((C_BORNE / n ** 3) / abs(mu_chevre(n) - 2 / (3 * n * n)) for n in range(2, N0))
assert MARGE > 100
ligne("- La constante est grossière : la vraie limite de n³·|μ − 2/(3n²)| est 98/15 = 6,53. Pour n < 100, la borne "
      f"reste vraie sur les cordes calculées, avec une marge d'au moins {MARGE:.0f}.")
ligne()
ZONE = {n: n * math.log10(math.sqrt(2 * n / (n + 1) + 2 / (3 * n * n)) - 1) for n in (10, 24, 100, 1000)}
ligne("| n | zone centrale (√m − 1)ⁿ | (1/√2)ⁿ |")
ligne("|---:|---|---|")
for n, z in ZONE.items():
    ligne(f"| {n} | {sci_log(z)} | {sci_log(-n * math.log10(R2))} |")
ligne()

# ===========================================================================
# 2. Tous les termes
# ===========================================================================
ligne("## 2. Tous les termes")
ligne()
ligne(f"Coefficients exacts (fractions, 14 termes) et 30 termes à 170 chiffres, calculés en {fr(T_SERIE, '{:.1f}')} s.")
ligne()
ligne("| j | μ_j dans μ = Σ μ_j/n^j | valeur | μ_(j+1)/μ_j |")
ligne("|---:|---|---|---|")
for j in range(2, 13):
    q = MU_C[j]
    val = fr(float(q), '{:.6g}') if abs(q) < 1e5 else sci(q, 6)
    ligne(f"| {j} | {frac(q)} | {val} | {fr(float(MU_C[j + 1] / q), '{:.3f}')} |")
ligne()
ligne("En puissances de 1/n :")
ligne()
ligne("- r² = " + somme(R2N[:7]) + " + …")
X0N = [1 - R2N[0] / 2] + [-q / 2 for q in R2N[1:]]
ligne("- x₀ = 1 − r²/2 = " + somme(X0N[:7], 1) + " + …")
NX = [Fr(0)] * 8  # n(2 − r²)
for i in range(1, 8):
    NX[i - 1] = -R2N[i]
ligne("- n(2 − r²) = " + somme(NX[:6]) + " + … (partie XXII : 2 − 8/(3n))")
ligne()

# 1/x₀ = n + 4/3 − 112/(45n) + … (inversion exacte de la série de x₀)
inv = [Fr(0)] * 8  # 1/x₀ = n·(1/(x₀·n)) ; x₀·n = Σ X0N[i+1]/n^i
u = [X0N[i + 1] for i in range(8)]
inv[0] = 1 / u[0]
for i in range(1, 8):
    inv[i] = -sum(u[j] * inv[i - j] for j in range(1, i + 1)) / u[0]
assert inv[0] == 1 and inv[1] == Fr(4, 3) and inv[2] == Fr(-112, 45)
INV_X0 = inv
ligne(f"- 1/x₀ = n + {somme(inv[1:5])} + … : **le ménisque vaut un tiers de dimension** (§ 3).")
ligne()

# Contrôles en haute précision
CERT50 = {4: "1.26807925667341823348355415211571793356474343402219",
          8: "1.33486242915790962010461237019787330529447771629681",
          24: "1.38593157500109279341163629468441198854737501013798"}
for n, v in CERT50.items():
    r2 = corde2_hp(n, float(v) ** 2)
    assert abs(mp.sqrt(r2) - mp.mpf(v)) < mp.mpf(10) ** -48
NS_HP = [8, 10, 12, 16, 20, 24, 32, 40, 50, 70, 100, 150, 200, 300, 500, 700, 1000, 2000, 3000, 5000, 10000]
HP = {}
for n in NS_HP:
    HP[n] = corde2_hp(n, float(serie(n, min(6, n // 5))) if n > 30 else 2 * n / (n + 1) + 2 / (3 * n * n))
assert abs(HP[10000] - serie(10000, 20)) < mp.mpf(10) ** -50
ligne("**Contrôles.** Cordes certifiées de la partie XX retrouvées à 48 chiffres (n = 4, 8, 24). Cordes à 60 chiffres "
      "par l'équation de la chèvre (partie I § 5.1, Newton), écart à la série tronquée à l'ordre J :")
ligne()
ligne("| n | r_n² (40 chiffres) | J = 2 | J = 4 | J = 8 | J = 12 |")
ligne("|---:|---|---|---|---|---|")
for n in (24, 100, 1000, 10000):
    e = [abs(HP[n] - serie(n, J)) for J in (2, 4, 8, 12)]
    ligne(f"| {n} | {mp.nstr(HP[n], 40).replace('.', ',')} | " + " | ".join(sci(x) for x in e) + " |")
ligne()
ligne("Chaque ordre gagne un facteur ≈ n : les coefficients sont justes (à 10⁻⁵⁰ près en dimension 10 000 avec "
      "20 termes).")
ligne()

# La série diverge au rythme 1/ln √2
mu_mp = [R2N_MP[i] - 2 * (-1) ** i for i in range(len(R2N_MP))]
RAP = [mu_mp[j + 1] / mu_mp[j] for j in range(2, len(mu_mp) - 1)]
INC = [RAP[i] - RAP[i + 1] for i in range(len(RAP) - 1)]  # ≈ A
A_TH = 2 / math.log(2)
ligne(f"**La série diverge.** μ_(j+1)/μ_j ≈ −A·j, et l'écart entre deux rapports successifs tend vers "
      f"A = 1/ln √2 = 2/ln 2 = {fr(A_TH, '{:.5f}')} :")
ligne()
ligne("| j | 5 | 10 | 15 | 20 | 25 | 28 |")
ligne("|---|---|---|---|---|---|---|")
ligne("| écart des rapports | " + " | ".join(fr(float(INC[j - 3]), "{:.4f}") for j in (5, 10, 15, 20, 25, 28)) + " |")
ligne()
ligne("Lecture (argument de col, pas une preuve) : le bord de la calotte de la corde est à α → 45°, et le "
      "développement de W_n(α) = ∫₀^α sinⁿ « sent » le sommet du sinus à 90°, à la distance "
      "ln(sin 90°/sin 45°) = ln √2.")
ligne()
OPT = []
for n in (10, 16, 24, 32, 50, 70):
    ex = HP[n] if n in HP else corde2_hp(n, 2 * n / (n + 1))
    errs = [abs(ex - serie(n, J)) for J in range(len(R2N_MP))]
    jb = min(range(2, len(errs)), key=lambda J: errs[J])
    OPT.append((n, jb, errs[jb]))
ligne("**Troncature optimale.** On s'arrête au plus petit terme, vers j* ≈ n·ln √2. L'erreur vaut alors ≈ 2^(−n/2)/n :")
ligne()
ligne("| n | j* | n·ln √2 | erreur optimale | 2^(−n/2)/n | rapport |")
ligne("|---:|---:|---:|---|---|---|")
for n, jb, e in OPT:
    ref = 2 ** (-n / 2) / n
    ligne(f"| {n} | {jb} | {fr(n * math.log(R2), '{:.1f}')} | {sci(e)} | {sci(ref)} | {fr(float(e) / ref, '{:.2f}')} |")
ligne()
CHIF = {n: n * math.log10(R2) + math.log10(n) for n in (24, 100)}
ligne(f"Soit −log₁₀(2^(−n/2)/n) = {fr(math.log10(R2), '{:.4f}')}·n + log₁₀ n chiffres au mieux : "
      f"{fr(CHIF[24], '{:.1f}')} en 24D, {fr(CHIF[100], '{:.1f}')} en 100D, 1,5·10⁴⁹ en dimension 10⁵⁰.")
ligne()


# Les décimales en blocs
def decimales(q, nb):
    ent = q.numerator // q.denominator
    reste = q - ent
    return str(ent), str((reste * 10 ** nb).numerator // (reste * 10 ** nb).denominator).zfill(nb)


ligne("**Les décimales en blocs.** En dimension 10ᵏ, chaque terme de la série occupe un bloc de k chiffres.")
ligne()
e4, d4 = decimales(Fr(int(mp.floor(HP[10000] * mp.mpf(10) ** 44))) / 10 ** 44, 44)
ligne("En dimension 10⁴ (60 chiffres exacts, blocs de 4) :")
ligne()
ligne("```")
ligne(f"r² = {e4}," + " ".join(d4[i:i + 4] for i in range(0, 44, 4)))
ligne("```")
ligne()
N50 = 10 ** 50
r2_50 = sum(q / Fr(N50) ** i for i, q in enumerate(R2N))  # reste < 10⁻⁷⁰⁰
e50, d50 = decimales(r2_50, 300)
ligne("En dimension 10⁵⁰ (série à 14 termes, reste < 10⁻⁷⁰⁰ ; blocs de 50 chiffres) :")
ligne()
ligne("```")
ligne(f"r² = {e50},")
for i in range(0, 300, 50):
    ligne(f"     {d50[i:i + 50]}")
ligne("```")
ligne()
ligne("Bloc 1 : 2 − 2/n. Bloc 2 : le 2 de 8/3 = 2 + 2/3 (le 2/n² du simplexe 2n/(n + 1)). Bloc 3 : le 2/3 du "
      "ménisque (0,666…), moins le 8 de 128/15 = 8,53… (66 − 8 = 58). Bloc 4 : 0,1333… = 2/15, plus le 58 de "
      "6176/105 = 58,8… Chaque bloc porte la partie décimale d'un coefficient ; les retenues les recousent "
      "(parties XIX et XXIII).")
ligne()

# ===========================================================================
# 3. Un tiers de dimension
# ===========================================================================
ligne("## 3. Un tiers de dimension")
ligne()
ligne("On cherche le simplexe qui a la même corde : 2N/(N + 1) = r_n², soit N = r²/(2 − r²) = 1/x₀ − 1.")
ligne()


def decalage(n):
    """N − n, avec N la dimension du simplexe de même corde (calcul sans soustraction)."""
    if n == 1:
        return 0.0
    mu = mu_chevre(n)
    return 2 / (2 / (n + 1) - mu) - 1 - n


NS_TIERS = [1, 2, 3, 4, 5, 8, 10, 24, 100, 1000, 10 ** 4, 10 ** 5, 10 ** 6]
TIERS = {n: decalage(n) for n in NS_TIERS}
for n in (24, 100, 1000, 10000):
    exact = 1 / (1 - HP[n] / 2) - 1 - n
    assert abs(TIERS[n] - float(exact)) < 1e-6
ligne("| n | 1 | 2 | 3 | 4 | 5 | 8 | 10 | 24 | 100 | 10³ | 10⁴ | 10⁵ | 10⁶ |")
ligne("|---|" + "---|" * len(NS_TIERS))
ligne("| N − n | " + " | ".join(fr(TIERS[n], "{:.4f}") for n in NS_TIERS) + " |")
ligne()
SH_INT = [decalage(n) for n in range(2, 61)]
assert all(b > a for a, b in zip(SH_INT, SH_INT[1:]))
ligne("- N − n croît de 0 (dimension 1) vers 1/3 (vérifié pour n = 2 … 60 et aux décades), avec "
      "N − n = 1/3 − 112/(45n) + ….")
ligne("- Donc r_n² = 2N/(N + 1) avec N = n + 1/3 − …, et le plan de la lentille est en x₀ = 1/(N + 1) = 1/(n + 4/3 − …).")
ligne()

# ===========================================================================
# 4. Le piquet n'importe où
# ===========================================================================
ligne("## 4. Le piquet n'importe où")
ligne()
Dd = sp.Symbol("D", positive=True)  # D = 1/d²


def developpement_d(J):
    """μ(n, d) = Σ μ_i(D)/n^i, D = 1/d² ; même méthode, τ = (ρ² − c)/(2dρ)."""
    L = 2 * J
    Z = sp.Integer(0)

    def mul(a, b):
        out = [Z] * L
        for i, x in enumerate(a):
            if x != 0:
                for j in range(L - i):
                    out[i + j] += x * b[j]
        return [sp.expand(x) for x in out]

    def momt(p, c):  # E[(ρ² − c)^p/ρ^p]
        pw = [[sp.Integer(1)] + [Z] * (L - 1)]
        for _ in range(p):
            pw.append(mul(pw[-1], [-x for x in c]))
        out = [Z] * L
        for i in range(p + 1):
            g = mul(pw[p - i], [sp.Integer((p - 2 * i) ** t) for t in range(L)])  # E[ρ^(2i−p)] = 1/(1 + (2i − p)ε)
            out = [sp.expand(o + comb(p, i) * x) for o, x in zip(out, g)]
        return out
    c = [sp.Integer(1)] + [sp.Integer(2 * (-1) ** t) for t in range(1, L)]  # (n − 1)/(n + 1)
    mus = {}
    for i in range(2, J + 1):
        tot = [Z] * L
        for j in range(J):
            poly = [sp.Integer(1)] + [Z] * (L - 1)
            for q in range(j):
                poly = mul(poly, [sp.Integer(1), sp.Integer(-(3 + 2 * q))] + [Z] * (L - 2))
            t_ = mul(poly, momt(2 * j + 1, c))[j:] + [Z] * j
            fac = sp.Rational((-1) ** j, 2 ** j * factorial(j) * (2 * j + 1) * 4 ** j) * Dd ** j
            tot = [sp.expand(a + fac * b) for a, b in zip(tot, t_)]
        mus[i] = sp.factor(tot[i])
        c[i] = sp.expand(c[i] + tot[i])
    return mus


MU_D = developpement_d(4)
assert all(sp.simplify(MU_D[i].subs(Dd, 1) - MU_C[i]) == 0 for i in (2, 3, 4))
c_n = 2 * nn * (nn - 1) / (3 * (nn + 1) ** 3 * (nn + 3))  # partie XVI § 6
eps = sp.Symbol("e", positive=True)
cn_serie = sp.series(c_n.subs(nn, 1 / eps), eps, 0, 5).removeO()
for i in (2, 3, 4):
    assert sp.simplify(sp.diff(MU_D[i], Dd).subs(Dd, 0) - cn_serie.coeff(eps, i)) == 0
# le c_n exact à partir des moments (grand d, n fixé)
tt3 = sp.Rational(1, 8) * (nn / (nn + 3) - 3 * (nn - 1) / (nn + 1) * nn / (nn + 1)
                          + 3 * ((nn - 1) / (nn + 1)) ** 2 * nn / (nn - 1) - ((nn - 1) / (nn + 1)) ** 3 * nn / (nn - 3))
cn_moments = sp.simplify(-((nn - 3) / 3) * tt3 / (nn / (nn - 1)))
assert sp.simplify(cn_moments - c_n) == 0
ligne("Même démonstration avec τ = (ρ² − c)/(2dρ), c = k² − d², D = 1/d² :")
ligne()
ligne("k² = d² + (n − 1)/(n + 1) + μ(n, d), avec")
ligne()
def joli(e):
    t = str(e).replace("**2", "²").replace("**3", "³").replace("*", "").replace("-", "−")
    return t


for i, e in MU_D.items():
    ligne(f"- ordre 1/n{sup(i)} : {joli(e)}")
ligne()
ligne("- C'est la loi k² ≈ δ² + (n − 1)/(n + 1) de la partie I (§ 5.4), désormais démontrée, avec sa correction "
      "2/(3n²d²). Le paramètre est 1/(nd²) : valable tant que d ≫ 1/√n, comme annoncé.")
ligne("- La partie en D (piquet lointain) redonne exactement le c_n/ρ² de la partie XVI (§ 6) : "
      "c_n = 2n(n − 1)/(3(n + 1)³(n + 3)), retrouvé ici par les moments, et n²c_n → 2/3.")
ligne("- Les deux « à faire relire » (partie I § 5.4, partie XVI § 6) sont le même terme : le τ³ de l'équateur.")
ligne()
CHK_D = []
for n, d in ((100, 0.5), (100, 1.0), (100, 3.0), (1000, 0.2), (1000, 1.0)):
    mu = mu_chevre(n, d)
    pred = sum(float(MU_D[i].subs(Dd, 1 / d ** 2)) / n ** i for i in MU_D)
    CHK_D.append((n, d, mu, pred))
    assert abs(mu - pred) / mu < 0.02
ligne("| n | d | μ calculé | μ prédit (ordres 2 à 4) |")
ligne("|---:|---:|---|---|")
for n, d, mu, pred in CHK_D:
    ligne(f"| {n} | {fr(d, '{:.1f}')} | {sci(mu, 5)} | {sci(pred, 5)} |")
ligne()

# μ ≈ 2δ (parties VI et XVI)
DELTA = {}
for n in (2, 3, 5, 10, 20, 50, 100):
    a2 = 2 * n / (n + 1)
    g2 = (n - 1) / (n + 1)

    def manque(dl, n=n, a2=a2, g2=g2):
        d = 1 - dl
        return broute_mu(n, d, a2 - d * d - g2) - 0.5
    dl = brentq(manque, 1e-9, 0.02, xtol=1e-16)
    DELTA[n] = (dl, mu_chevre(n))
assert abs(DELTA[2][0] - 0.0047121107) < 2e-9 and abs(DELTA[3][0] - 0.0047121571) < 2e-9
ligne("**μ ≈ 2δ (parties VI et XVI).** On garde la corde du simplexe et on rapproche le piquet du centre de δ :")
ligne()
ligne("| n | δ | μ | 2δ/μ | 1 + 5μ/4 |")
ligne("|---:|---|---|---|---|")
for n, (dl, mu) in DELTA.items():
    ligne(f"| {n} | {fr(dl, '{:.10f}')} | {sci(mu, 5)} | {fr(2 * dl / mu, '{:.6f}')} | {fr(1 + 1.25 * mu, '{:.6f}')} |")
ligne()
ligne("2δ − δ² = μ(n, 1 − δ) ≈ μ(1 + 2δ) donne 2δ/μ ≈ 1 + 5μ/4, juste quand n grandit.")
ligne()

# ===========================================================================
# 5. Le facteur 2
# ===========================================================================
ligne("## 5. Le facteur 2 entre le plan et l'aire")
ligne()
for n in (2, 3, 24, 100):
    r2 = float(HP[n]) if n in HP else (float(corde2_hp(n, 2 * n / (n + 1))))
    x0 = 1 - r2 / 2
    assert abs(r2 - 2 * 1 * (1 - x0)) < 1e-15
ligne("**Euclide (Éléments VI.8) et Thalès (III.31).** Le triangle P Q P′ (P′ l'antipode du piquet, Q sur le bord de "
      "la lentille) est rectangle en Q. Le côté PQ = r est moyen proportionnel entre le diamètre PP′ = 2R et sa "
      "projection PH = R − x₀ : **r² = 2R·(R − x₀)**, exactement, en toute dimension.")
ligne("- Donc 2R² − r² = 2R·x₀ : le défaut d'aire est l'aire de la bande de largeur x₀ et de hauteur 2R (le diamètre).")
ligne("- Le facteur 2 est le diamètre mesuré en rayons. En dimension infinie, x₀ = 0 et Q est le coin du demi-carré "
      "(partie I, § 5.3).")
ligne("- En unités : x₀ = (2R² − r²)/(2R²) (défaut relatif au disque limite, rayon √2, le cercle des coins) et "
      "2 − r² = (2R² − r²)/R² (relatif au pré, le cercle des côtés). Les deux unités sont à un cran (partie I, § 6.4).")
ligne()
LECT = [("corde relative (√2 − r)/√2", lambda r2: (R2 - math.sqrt(r2)) / R2, 0.5),
        ("corde √2 − r", lambda r2: R2 - math.sqrt(r2), 1 / R2),
        ("plan x₀", lambda r2: 1 - r2 / 2, 1.0),
        ("cran log₂(2/r²)", lambda r2: math.log2(2 / r2), 1 / math.log(2)),
        ("aire 2 − r² (unité : le pré)", lambda r2: 2 - r2, 2.0),
        ("aire en unité du disque central (½)", lambda r2: 2 * (2 - r2), 4.0)]
ligne("**Les lectures du grain.** (n + 4/3)·défaut tend vers une constante pour chaque lecture :")
ligne()
ligne("| lecture | n = 100 | n = 10³ | n = 10⁴ | limite | n au grain 10⁻⁵⁰ |")
ligne("|---|---|---|---|---|---|")
LECT_VAL = {}
for nom, f, lim in LECT:
    vals = []
    for n in (100, 1000, 10000):
        x = 2 / (n + 1) - mu_chevre(n) if "aire" in nom or "plan" in nom else None
        r2 = float(HP[n])
        if nom.startswith("plan"):
            v = x / 2
        elif nom.startswith("aire 2"):
            v = x
        elif nom.startswith("aire en"):
            v = 2 * x
        else:
            v = f(r2)
        vals.append((n + 4 / 3) * v)
    LECT_VAL[nom] = vals
    ligne(f"| {nom} | " + " | ".join(fr(v, "{:.5f}") for v in vals) + f" | {fr(lim, '{:.5f}')} | "
          f"≈ {fr(lim, '{:.3g}')}·10⁵⁰ |")
ligne()
ligne("- Le plan et l'aire : n = 10⁵⁰ − 4/3 et n = 2·10⁵⁰ − 4/3 (à 10⁻⁵⁰ près). Le facteur 2 multiplie, le 4/3 "
      "décale : 1 pour le simplexe (centre de gravité), 1/3 pour le ménisque, le même dans les deux lectures.")
ligne(f"- Un facteur 2, c'est exactement 1 cran (base 2), {fr(math.log10(2), '{:.5f}')} décade (base 10) et "
      f"{fr(10 * math.log10(2), '{:.4f}')} dB.")
ligne()

# ===========================================================================
# 6. Les liens
# ===========================================================================
ligne("## 6. Les liens avec les autres parties")
ligne()
LIENS = [
    ("I § 5.4", "esquisse de 2/(3n²)", "démonstration complète, borne 1 800/n³, tous les ordres"),
    ("I § 4.3 et § 5.4", "k² ≈ δ² + (n − 1)/(n + 1)", "démontrée, + 2/(3n²δ²), validité δ ≫ 1/√n"),
    ("I § 5.2–5.3", "coquille et équateur", "2/3 = 2 (double produit 2ρU₁) × 1/6 (équateur) × 2 (coquille)"),
    ("I § 5.5", "paires transcendantes, impaires algébriques", "même série rationnelle ; écart sous (1/√2)ⁿ"),
    ("I § 6.4, XXI", "un cran, le doublement de l'aire", "le facteur 2 entre plan et aire"),
    ("IV, VII, XX", "Wallis, W_n, cordes certifiées", "c_n se simplifie ; contrôles à 48 chiffres"),
    ("VI", "simplexe, n²(r² − a²) = 0,037 … 0,65", "E[τ] = 0 : la chèvre linéarisée ; 2/3 démontré"),
    ("VI § 3 bis", "dimensions non entières", "la chèvre de dimension n = le simplexe de dimension n + 1/3"),
    ("XVI", "g² deux fois ; c_n/ρ² ; μ ≈ 2δ", "g² = E[ρ]/E[ρ⁻¹] ; c_n retrouvé ; 2δ/μ ≈ 1 + 5μ/4"),
    ("XVII, XVIII", "√2 − 1, tan 22,5°", "zone centrale (√2 − 1)ⁿ"),
    ("XVIII, XXII, XXIII", "un chiffre par décade, 2 − 8/(3n), deux couches", "les blocs de k chiffres en 10ᵏ"),
]
ligne("| partie | ce qu'on avait | ce que la partie XXIV ajoute |")
ligne("|---|---|---|")
for a, b, c in LIENS:
    ligne(f"| {a} | {b} | {c} |")
ligne()

with open(os.path.join(ICI, "..", "resultats", "tiers_dimension.md"), "w") as fh:
    fh.write("\n".join(md) + "\n")
print(f"calculs : {time.time() - T0:.1f} s")

# ===========================================================================
# Figure y1
# ===========================================================================
T1 = time.time()


def schema(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for sp_ in ax.spines.values():
        sp_.set_visible(False)


def legende(ax, texte, y=-0.12):
    ax.text(0.5, y, texte, transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)


GRILLE = np.unique(np.concatenate([np.logspace(np.log10(1.05), 6, 44), [2, 3, 4, 8, 10, 24, 100, 1000]]))
MU_G = np.array([mu_chevre(float(x)) for x in GRILLE])
TIERS_G = 2 / (2 / (GRILLE + 1) - MU_G) - 1 - GRILLE

fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.2, hspace=0.36)

# a) n²μ → 2/3
ax = fig.add_subplot(gs[0, 0])
ax.semilogx(GRILLE, GRILLE ** 2 * MU_G, color=F.BLEU, lw=2.2, label="n²·μ_n exact (intégrale radiale)", zorder=4)
nn_ = np.logspace(np.log10(1.5), 6.2, 400)
for J, col in ((3, F.ORANGE), (4, F.JAUNE), (6, VERT), (10, VIOLET)):
    y = sum(float(MU_C[i]) * nn_ ** (2 - i) for i in range(2, J + 1))
    ax.semilogx(nn_, y, color=col, lw=1.1, alpha=0.9, label=f"série jusqu'à 1/n{sup(J)}")
ax.axhline(2 / 3, color=ROUGE, lw=1.5, ls="--", label="2/3 (démontré)")
PVI = [(2, 0.037), (20, 0.44), (100, 0.61), (400, 0.65)]
ax.plot(*zip(*PVI), "s", mfc="none", mec=F.INK, ms=8, mew=1.3, label="partie VI (mesuré)", zorder=5)
ax.set_ylim(0, 0.78)
ax.set_xlim(1.5, 2e6)
ax.set_xlabel("dimension n")
ax.set_ylabel("n²·(r_n² − 2n/(n + 1))")
ax.legend(loc="lower right", fontsize=8.3, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.text(0.47, 0.6, "2/3 = 2 × 1/6 × 2\n2 : le double produit 2ρU₁\n1/6 : la courbure de l'équateur\n"
        "2 : l'asymétrie de la coquille", transform=ax.transAxes, va="top", fontsize=8.8, color=F.INK,
        bbox=dict(boxstyle="round,pad=0.4", fc=F.SURF, ec=F.BASE))
ax.set_title("a)  n²·μ_n → 2/3, terme par terme")
legende(ax, "Le ménisque μ_n = r_n² − 2n/(n + 1), multiplié par n². La série exacte (couleurs)"
        "\ncolle aux valeurs exactes d'autant plus tôt qu'on garde de termes, puis décroche"
        "\naux petites dimensions : elle diverge. Les carrés sont les mesures de la partie VI,"
        "\nmaintenant expliquées.")

# b) l'erreur ordre par ordre
ax = fig.add_subplot(gs[0, 1])
NSb = np.array(NS_HP, dtype=float)
cols = F.SEQ[4:]
for k_, J in enumerate((2, 3, 4, 6, 8, 12, 20, 30)):
    err = np.array([float(abs(HP[n] - serie(n, J))) for n in NS_HP])
    ok = err > 1e-58
    col = cols[min(k_ + 1, len(cols) - 1)]
    ax.loglog(NSb[ok], err[ok], "o-", ms=3.2, lw=1.2, color=col)
    ax.text(NSb[ok][-1] * 1.15, err[ok][-1], f"J = {J}", fontsize=8, color=col, va="center")
env_n = np.linspace(8, 420, 300)
ax.loglog(env_n, 2.0 ** (-env_n / 2) / env_n, color=ROUGE, lw=1.8, ls="--",
          label="2^(−n/2)/n : la meilleure précision")
ax.set_ylim(1e-60, 1)
ax.set_xlim(7, 3e4)
ax.set_xlabel("dimension n")
ax.set_ylabel("|r_n² − série jusqu'à 1/n^J|")
ax.legend(loc="lower left", fontsize=8.4, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.text(0.97, 0.97, "pente −(J + 1) :\nchaque coefficient\nest juste", transform=ax.transAxes, ha="right", va="top",
        fontsize=9, color=F.INK2)
ax.set_title("b)  L'erreur, ordre par ordre (cordes à 60 chiffres)")
legende(ax, "Écart entre la corde exacte (60 chiffres) et la série coupée à 1/n^J : chaque terme"
        "\ngagne un facteur n. Mais les coefficients croissent comme j!·(1/ln √2)^j : au mieux,"
        "\nla série donne r² à 2^(−n/2)/n près (tirets), en coupant vers j ≈ n·ln √2."
        "\nC'est encore √2.")

# c) un tiers de dimension
ax = fig.add_subplot(gs[0, 2])
ax.semilogx(GRILLE, TIERS_G, color=F.BLEU, lw=2.2, label="N − n (simplexe de même corde)")
nn2_ = np.logspace(np.log10(15), 6.2, 200)
ax.semilogx(nn2_, 1 / 3 - 112 / (45 * nn2_), color=F.ORANGE, lw=1.3, ls=":", label="1/3 − 112/(45n)")
ax.axhline(1 / 3, color=ROUGE, lw=1.5, ls="--", label="1/3")
for n, xt, yt in ((2, 6, 0.012), (3, 9, 0.05), (24, 70, 0.215), (100, 300, 0.275)):
    v = TIERS[n]
    ax.plot([n], [v], "o", color=F.BLEU, ms=6.5, mec=F.SURF, mew=1.4, zorder=5)
    ax.annotate(f"{n}D : {fr(v, '{:.3f}')}", (n, v), (xt, yt), fontsize=8.8, color=F.BLEU,
                fontweight="bold", arrowprops=dict(arrowstyle="-", color=F.BLEU, lw=0.7))
ax.set_ylim(0, 0.37)
ax.set_xlim(1, 2e6)
ax.set_xlabel("dimension n (réelle)")
ax.set_ylabel("N − n")
ax.legend(loc="center right", fontsize=8.6, frameon=True, facecolor=F.SURF, edgecolor="none",
          bbox_to_anchor=(1, 0.42))
ax.text(0.03, 0.97, "r_n² = 2N/(N + 1)\nx₀ = 1/(N + 1)", transform=ax.transAxes, va="top", fontsize=9.5,
        color=F.INK, bbox=dict(boxstyle="round,pad=0.4", fc=F.SURF, ec=F.BASE))
ax.set_title("c)  Le ménisque vaut un tiers de dimension")
legende(ax, "Le simplexe (partie VI) qui a exactement la corde de la chèvre est de dimension N :"
        "\nN dépasse n de 0 (en 1D) à 1/3 (à l'infini). Le terme 2/(3n²) n'est rien d'autre"
        "\nque ce tiers de dimension : 2n/(n + 1) + 2/(3n²) = 2N/(N + 1) avec N = n + 1/3,"
        "\nà 1/n³ près.")

# d) le piquet n'importe où
ax = fig.add_subplot(gs[1, 0])
DS = np.logspace(np.log10(0.03), np.log10(30), 23)
for n, col in ((10, F.RAMPE[1]), (100, F.RAMPE[3]), (1000, F.RAMPE[4])):
    y = np.array([n * n * d * d * mu_chevre(n, float(d)) for d in DS])
    cn_v = float(c_n.subs(nn, n)) * n * n
    ax.semilogx(DS, y, "o-", color=col, ms=3.5, lw=1.6, label=f"n = {n} ; n²c_n = {fr(cn_v, '{:.3f}')}")
    ax.axhline(cn_v, color=col, lw=1.0, ls=":")
    ax.plot([1], [n * n * float(mu_chevre(n))], "D", color=ROUGE, ms=6, zorder=6)
    ax.axvline(1 / math.sqrt(n), color=col, lw=0.8, ls="--", alpha=0.6)
ax.axhline(2 / 3, color=ROUGE, lw=1.5, ls="--")
ax.text(25, 2 / 3 + 0.02, "2/3", color=ROUGE, fontsize=9.5, ha="right")
ax.text(0.98, 0.05, "tirets verticaux : d = 1/√n\nlosanges rouges : la chèvre (d = 1)", transform=ax.transAxes,
        ha="right", fontsize=8.5, color=F.INK2)
ax.set_ylim(0, 0.8)
ax.set_xlim(0.03, 32)
ax.set_xlabel("distance d du piquet au centre (R = 1)")
ax.set_ylabel("n²·d²·μ(n, d)")
ax.legend(loc="center right", fontsize=8.6, frameon=True, facecolor=F.SURF, edgecolor="none",
          bbox_to_anchor=(1, 0.6))
ax.set_title("d)  Le piquet n'importe où : parties I et XVI réunies")
legende(ax, "k² = d² + (n − 1)/(n + 1) + μ, avec μ ≈ 2/(3n²d²) dès que d ≫ 1/√n (partie I,"
        "\ndémontré ici). Loin du pré, la même démonstration redonne exactement le c_n/ρ²"
        "\nde la partie XVI (pointillés). Les deux calculs « à faire relire » sont le même"
        "\nterme : le τ³ de l'équateur.")

# e) le facteur 2 : Thalès, Euclide et la bande
ax = fig.add_subplot(gs[1, 1])
schema(ax, (-1.15, 2.3), (-1.85, 1.3))
t_ = np.linspace(0, 2 * np.pi, 400)
r2D = math.sqrt(4 / 3 + mu_chevre(2))
x0 = 1 - r2D ** 2 / 2
yq = math.sqrt(1 - x0 * x0)
ax.fill_between([0, x0], [-1, -1], [1, 1], color=VIOLET, alpha=0.16, lw=0)
ax.plot([0, x0, x0, 0, 0], [-1, -1, 1, 1, -1], color=VIOLET, lw=1.2)
ax.plot(np.cos(t_), np.sin(t_), color=F.INK, lw=1.8)
ang = np.linspace(-math.pi, math.pi, 900)
for rr, col, ls, lw in ((r2D, F.ORANGE, "-", 2.2), (R2, ROUGE, "--", 1.4)):
    cx, cy = 1 + rr * np.cos(ang), rr * np.sin(ang)
    ax.plot(np.where(cx ** 2 + cy ** 2 <= 1.0001, cx, np.nan), cy, color=col, lw=lw, ls=ls)
ax.plot([x0, x0], [-1.12, 1.12], color=F.ORANGE, lw=1.0, ls="--")
ax.plot([0, 0], [-1.12, 1.12], color=ROUGE, lw=1.0, ls="--")
ax.plot([1, x0, -1], [0, yq, 0], color=F.INK2, lw=1.4)
ax.plot([-1.05, 1.05], [0, 0], color=F.BASE, lw=0.8)
u1 = np.array([1 - x0, -yq]) / math.hypot(1 - x0, yq)
u2 = np.array([-1 - x0, -yq]) / math.hypot(1 + x0, yq)
q = np.array([x0, yq])
s_ = 0.08
ax.plot(*zip(q + s_ * u1, q + s_ * (u1 + u2), q + s_ * u2), color=F.INK2, lw=1.0)
for (x, y), nom, dx, dy, col in (((1, 0), "P", 0.04, 0.05, F.INK), ((-1, 0), "P′", -0.15, 0.05, F.INK),
                                 ((x0, yq), "Q", 0.04, 0.05, F.INK), ((x0, 0), "H", 0.03, -0.12, F.INK),
                                 ((0, 0), "O", -0.1, -0.12, F.INK), ((0, 1), "Q∞", -0.24, 0.05, ROUGE)):
    F.point(ax, x, y, col, 6)
    ax.text(x + dx, y + dy, nom, fontsize=10.5, fontweight="bold", color=col)
ax.annotate("", (1, -0.2), (x0, -0.2), arrowprops=dict(arrowstyle="<->", color=F.ORANGE, lw=1.1))
ax.text(0.63, -0.27, "PH = r²/(2R)", ha="center", va="top", fontsize=8.6, color=F.ORANGE)
ax.annotate("", (0, -1.1), (x0, -1.1), arrowprops=dict(arrowstyle="<->", color=VIOLET, lw=1.1))
ax.text(x0 + 0.06, -1.1, "x₀", va="center", fontsize=10, color=VIOLET, fontweight="bold")
ax.text(1.13, 1.25, "Thalès : Q est un angle droit\nEuclide VI.8 :\n  PQ² = PP′·PH\n  r² = 2R·(R − x₀)\n"
        "  2R² − r² = 2R·x₀", fontsize=9.2, color=F.INK, va="top",
        bbox=dict(boxstyle="round,pad=0.4", fc=F.SURF, ec=F.BASE))
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
ax.legend(handles=[Line2D([], [], color=F.ORANGE, lw=2.2, label=f"bord de la lentille, chèvre 2D (r = {fr(r2D, '{:.4f}')})"),
                   Line2D([], [], color=ROUGE, lw=1.4, ls="--", label="dimension infinie : r = √2, plan en O"),
                   Patch(fc=VIOLET, alpha=0.3, ec=VIOLET, label="bande : largeur x₀, hauteur 2R, aire 2R² − r²")],
          loc="lower center", bbox_to_anchor=(0.5, 0.0), fontsize=8.6, frameon=True, facecolor=F.SURF,
          edgecolor="none")
ax.set_title("e)  Le facteur 2 : Thalès, Euclide et la bande")
legende(ax, "Q est sur le bord de la lentille : le triangle PQP′ est rectangle (Thalès). Euclide"
        "\ndonne r² = 2R·PH, donc le défaut d'aire 2R² − r² est la bande violette : largeur x₀"
        "\n(le plan), hauteur 2R (le diamètre). Le facteur 2 est le diamètre compté en rayons."
        "\nÀ l'infini, Q monte en Q∞, le coin du demi-carré (partie I, § 5.3).", y=-0.02)

# f) les lectures du grain
ax = fig.add_subplot(gs[1, 2])
sel = GRILLE >= 10
ng, mug = GRILLE[sel], MU_G[sel]
dx = 2 / (ng + 1) - mug  # 2 − r², sans soustraction
r_g = np.sqrt(2 - dx)
LECT_F = [("corde relative (√2 − r)/√2", (R2 - r_g) / R2, 0.5, F.RAMPE[0]),
          ("corde √2 − r", R2 - r_g, 1 / R2, F.RAMPE[2]),
          ("plan x₀", dx / 2, 1.0, F.ORANGE),
          ("crans log₂(2/r²)", -np.log2(1 - dx / 2), 1 / math.log(2), F.JAUNE),
          ("aire 2 − r² (unité : le pré)", dx, 2.0, VIOLET),
          ("aire, unité : le disque central", 2 * dx, 4.0, F.RAMPE[4])]
for nom, v, lim, col in LECT_F:
    ax.semilogx(ng, (ng + 4 / 3) * v, color=col, lw=2)
    ax.axhline(lim, color=col, lw=0.8, ls=":")
    ax.text(1.4e6, lim * 1.035, nom, fontsize=8.4, color=col, ha="right", va="bottom", fontweight="bold")
ax.set_yscale("log", base=2)
ax.set_yticks([0.5, 1 / R2, 1, 1 / math.log(2), 2, 4])
ax.set_yticklabels(["1/2", "1/√2", "1", "1/ln 2", "2", "4"])
ax.set_ylim(0.42, 5.2)
ax.set_xlim(10, 1.6e6)
ax.set_xlabel("dimension n")
ax.set_ylabel("(n + 4/3) × défaut  (échelle en crans)")
ax.text(0.03, 0.765, "plan → aire : × 2 = 1 cran = 0,301 décade = 3,01 dB\nau grain 10⁻⁵⁰ : n = 10⁵⁰ − 4/3 (plan),"
        " 2·10⁵⁰ − 4/3 (aire)", transform=ax.transAxes, va="center", fontsize=8.6, color=F.INK,
        bbox=dict(boxstyle="round,pad=0.4", fc=F.SURF, ec=F.BASE))
ax.set_title("f)  Les lectures du grain : un cran entre le plan et l'aire")
legende(ax, "Chaque lecture du grain (la corde, le plan, les crans, l'aire) mesure le même défaut"
        "\navec une autre unité : (n + 4/3) × défaut tend vers une constante. Entre le plan et"
        "\nl'aire, exactement 2 : le diamètre (panneau e), ou le cran entre le cercle des côtés"
        "\net celui des coins (partie I, § 6.4).")

F.sauver(fig, "y1_tiers_dimension.png")
print(f"figure : {time.time() - T1:.1f} s ; total : {time.time() - T0:.1f} s")
