"""
Partie XXV : les ouverts de la partie XXIV, la tranche 10⁻⁴⁹ – 10⁻⁵⁵ et les tournants d'aiguilles.

    python3 scripts/tranche_aiguilles.py        # ≈ 1 min

Écrit resultats/tranche_aiguilles.md, figures/z1_ouverts.png et figures/z2_tranche_aiguilles.png.

1. La divergence : l'équation de la chèvre s'écrit exactement comme une intégrale de Laplace ; d'où les grands ordres
   r²_m ≈ (−1)^m e^(−1/2) √(ln 2/π) Γ(m − 1/2) (2/ln 2)^m (vérifiés sur 40 coefficients), la meilleure précision
   e^(−1/2) √(2/ln 2) 2^(−n/2)/n, et la resommation de Borel–Padé, qui redonne la chèvre plane depuis l'infini.
2. Les bornes explicites des ordres 2 à 8 : |r_n² − S_J(n)| < C_J/n^(J+1) pour n ≥ 100 (polynômes entiers exacts).
3. c₂ = 4/405 et c₃ = 1/96 exacts, par l'aire et le volume exacts de la lentille.
4. L'unité du grain : le tournant de l'aiguille, cos α_n = x₀, et le miroir des lectures.
5. La tranche 49 – 55 : sommes de carrés, miroir autour de 52, plans, taux de change, blocs de chiffres, crans.
6. Les tournants d'aiguilles : aiguilles du plan et angles pythagoriciens, demi-tours, 45°, dimensions minimales,
   i modulo k, stations du retournement, r₂₄ et le τ de Ramanujan, le croisement des chèvres.
"""

import logging
import math
import os
import sys
import time
from fractions import Fraction as Fr
from math import comb, factorial, gcd, isqrt

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
import sympy as sp
from matplotlib.patches import Rectangle
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import betainc, erfinv

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


def sci_mp(x, chiffres=3):
    """Comme sci, pour un mpf éventuellement minuscule."""
    x = mp.mpf(x)
    if x == 0:
        return "0"
    e = int(mp.floor(mp.log10(abs(x))))
    m = float(x / mp.mpf(10) ** e)
    m = round(m, chiffres - 1)
    if abs(m) >= 10:
        m, e = m / 10, e + 1
    return f"{fr(m, '{:.' + str(chiffres - 1) + 'f}')}·10{sup(e)}"


# ===========================================================================
# La corde exacte (mêmes outils que la partie XXIV)
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
    """P(|X − P|² ≤ k²), piquet à distance d, k² = d² + (n − 1)/(n + 1) + μ (intégrale radiale, E = −n ln ρ)."""
    c = (n - 1) / (n + 1) + mu

    def f(s):
        r = math.exp(-s / n)
        tau = (math.expm1(-2 * s / n) + 2 / (n + 1) - mu) / (2 * d * r)
        return math.exp(-s) * part_calotte(tau, n)
    k = math.sqrt(d * d + c)
    pts = sorted(p for p in (-n * math.log(x) for x in (k - d, d - k, d + k) if 0 < x < 1) if 0 < p < 60)
    return quad(f, 0, 60, points=pts or None, limit=400, epsabs=1e-16, epsrel=1e-13)[0] + math.exp(-60)


def mu_chevre(n, d=1.0):
    return brentq(lambda m: broute_mu(n, d, m) - 0.5, -0.2 / n, 2.0 / n, xtol=1e-18, rtol=1e-13)


def W(n, th):
    """∫₀^θ sinⁿ par la récurrence de la partie IV."""
    s, c = mp.sin(th), mp.cos(th)
    w, m0 = (th, 0) if n % 2 == 0 else (1 - c, 1)
    p, s2 = s ** (m0 + 1), s * s
    for m in range(m0 + 2, n + 1, 2):
        w = -p * c / m + mp.mpf(m - 1) / m * w
        p *= s2
    return w


def W_petit(n, th):
    s = mp.sin(th)
    return s ** (n + 1) / (n + 1) * mp.hyp2f1(mp.mpf(1) / 2, mp.mpf(n + 1) / 2, mp.mpf(n + 3) / 2, s * s)


def corde2_hp(n, r2_depart, dps=60):
    """r_n² à dps chiffres : W_n(2α) − (2cos α)ⁿ W_n(α) = ½W_n(π), méthode de Newton."""
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


def developpement(J, zero, un, cst):
    """Coefficients de r_n² en puissances de 1/n (méthode de la partie XXIV)."""
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
        for i in range(j):
            poly = mul(poly, [un, cst(-(3 + 2 * i))] + [zero] * (L - 2))
        poly = [zero] * (J - j) + poly[: L - J + j]
        coef = cst((-1) ** j) / cst(2 ** j * factorial(j) * (2 * j + 1) * 2 ** p)
        for s in range(p + 1):
            geo = [cst((p - 2 * s) ** t * (-1) ** t) for t in range(L)]
            terme = mul(poly, geo)
            for t in range(L):
                B[s][t] += coef * cst(comb(p, s)) * terme[t]
    w = [cst(-1)] + [cst(2 * (-1) ** (t + 1)) for t in range(1, L)]
    for i in range(2, J + 1):
        acc = [zero] * L
        for s in range(2 * J - 1, -1, -1):
            acc = mul(acc, w)
            for t in range(L):
                acc[t] += B[s][t]
        w[i] -= 2 * acc[J + i]
    return [1 - w[0]] + [-x for x in w[1: J + 1]]


R2N = developpement(14, Fr(0), Fr(1), Fr)  # exact
MU_C = {i: R2N[i] - 2 * (-1) ** i for i in range(2, len(R2N))}
assert MU_C[2] == Fr(2, 3) and MU_C[3] == Fr(-98, 15)
mp.mp.dps = 200
C40 = developpement(40, mp.mpf(0), mp.mpf(1), mp.mpf)
mp.mp.dps = 60
T_COEF = time.time() - T0


def serie(n, J):
    x = mp.mpf(1) / n
    return sum(C40[i] * x ** i for i in range(J + 1))


ligne("# Partie XXV : les ouverts, la tranche 10⁻⁴⁹ – 10⁻⁵⁵ et les tournants d'aiguilles")
ligne()
ligne("Résultats calculés par `scripts/tranche_aiguilles.py`.")
ligne()

# ===========================================================================
# 1. La divergence
# ===========================================================================
ligne("## 1. La divergence de la série, constante comprise")
ligne()
L0 = mp.log(2) / 2
KGO = mp.exp(-mp.mpf(1) / 2) * mp.sqrt(mp.log(2) / mp.pi)
RATIO = {m: C40[m] / ((-1) ** m * KGO * mp.gamma(m - mp.mpf(1) / 2) / L0 ** m) for m in range(4, 41)}


def richardson(ordre):
    pts = [(m, RATIO[m]) for m in range(41 - ordre - 1, 41)]
    A = mp.matrix([[mp.mpf(1) / mp.mpf(m) ** j for j in range(ordre + 1)] for m, _ in pts])
    return mp.lu_solve(A, mp.matrix([r for _, r in pts]))


RICH = {o: richardson(o) for o in (4, 6, 8)}
assert all(abs(RICH[o][0] - 1) < 2e-5 for o in RICH)
ligne("**La forme de Laplace de l'équation de la chèvre.** Avec 2α = π/2 + β (r² = 2 − 2 sin β), l'équation "
      "W_n(2α) − (2cos α)ⁿ W_n(α) = ½W_n(π) s'écrit exactement")
ligne()
ligne("∫₀^β (cos ψ/cos β)ⁿ dψ = ∫₀^∞ e^(−nu) tan φ(u) du,  avec sin φ = sin α·e^(−u).")
ligne()
ligne("Le membre de droite est une intégrale de Laplace. Son intégrande, tan φ(u) = s·e^(−u)/√(1 − s²e^(−2u)) "
      "(s = sin α), a sa singularité la plus proche en u = ln s → ln sin 45° = −ln √2 : une racine carrée.")
ligne()


def forme_laplace(n):
    """Résout la forme de Laplace pour β, renvoie r² = 2 − 2 sin β."""
    def F_(beta):
        g = mp.quad(lambda p: (mp.cos(p) / mp.cos(beta)) ** n, [0, beta])
        s = mp.sin(mp.pi / 4 + beta / 2)
        d_ = mp.quad(lambda u: mp.exp(-n * u) * s * mp.exp(-u) / mp.sqrt(1 - s * s * mp.exp(-2 * u)), [0, 1, 10, mp.inf])
        return g - d_
    beta = mp.findroot(F_, mp.mpf(1) / n)
    return 2 - 2 * mp.sin(beta)


with mp.workdps(30):
    HP2 = corde2_hp(2, 1.3426, 40)
    LAP = {n: forme_laplace(n) for n in (2, 10)}
    assert abs(LAP[2] - HP2) < mp.mpf(10) ** -25
    assert abs(LAP[10] - corde2_hp(10, 1.8212, 40)) < mp.mpf(10) ** -25
ligne(f"Contrôle : la forme de Laplace redonne la corde plane, r₂² = {mp.nstr(LAP[2], 22).replace('.', ',')} "
      "(Ullisch), et celle de la dimension 10, à 10⁻²⁵ près.")
ligne()
ligne("**Les grands ordres.** La singularité en racine carrée (Darboux), la dérivée de la corde par rapport à β (−2) "
      "et le déplacement de α avec la dimension (facteur e^(−1/2), signe alterné) donnent :")
ligne()
ligne("r²_m ≈ (−1)^m · e^(−1/2)·√(ln 2/π) · Γ(m − 1/2) · (2/ln 2)^m")
ligne()
ligne("| m | 10 | 20 | 30 | 40 | limite (Richardson, ordres 4, 6, 8) |")
ligne("|---|---|---|---|---|---|")
ligne("| coefficient / prédiction | " + " | ".join(mp.nstr(RATIO[m], 6).replace(".", ",") for m in (10, 20, 30, 40))
      + " | " + " ; ".join(mp.nstr(RICH[o][0], 7).replace(".", ",") for o in (4, 6, 8)) + " |")
ligne()
ligne(f"Le rapport tend vers 1 comme 1 + c/m, avec c ≈ {fr(float(RICH[6][1]), '{:.2f}')}.")
ligne()

# Troncature optimale
PRED_ERR = mp.exp(-mp.mpf(1) / 2) * mp.sqrt(2 / mp.log(2))
NS_OPT = list(range(10, 111, 4))
OPT = {}
for n in NS_OPT:
    ex = corde2_hp(n, float(serie(n, 4)) if n > 20 else 2 * n / (n + 1) + 2 / (3 * n * n))
    errs = [abs(ex - serie(n, J)) for J in range(41)]
    jb = min(range(2, 41), key=lambda J: errs[J])
    termes = [abs(C40[m]) / mp.mpf(n) ** m for m in range(2, 41)]
    plus_petit = min(termes)
    OPT[n] = (jb, errs[jb], plus_petit, ex)
ligne(f"**La meilleure précision.** On coupe au plus petit terme (j* ≈ n·ln √2). Prédiction : erreur ≈ moitié du plus "
      f"petit terme ≈ e^(−1/2)·√(2/ln 2)·2^(−n/2)/n = {fr(float(PRED_ERR), '{:.4f}')}·2^(−n/2)/n.")
ligne()
ligne("| n | j* | erreur optimale | erreur × n·2^(n/2) | erreur / plus petit terme |")
ligne("|---:|---:|---|---|---|")
for n in (10, 30, 50, 70, 90, 110):
    jb, e, pp, _ = OPT[n]
    ligne(f"| {n} | {jb} | {sci_mp(e)} | {fr(float(e * n * mp.mpf(2) ** (mp.mpf(n) / 2)), '{:.3f}')} | "
          f"{fr(float(e / pp), '{:.3f}')} |")
ligne()

# Borel–Padé
mp.mp.dps = 80
BCOEF = [C40[m] / mp.gamma(m) for m in range(1, 41)]
PP, QQ = mp.pade(BCOEF[:39], 19, 19)
POLES = mp.polyroots(QQ[::-1], maxsteps=400, extraprec=400)
ZEROS = mp.polyroots(PP[::-1], maxsteps=400, extraprec=400)
assert not any(abs(mp.im(z)) < 1e-8 and mp.re(z) > 0 for z in POLES)
# doublets de Froissart : un pôle collé à un zéro (résidu nul), artefact de l'approximant
DOUBLETS = [z for z in POLES if min(abs(z - w) for w in ZEROS) < 1e-8]
VRAIS = [z for z in POLES if z not in DOUBLETS]


def borel_pade(n):
    def B(t):
        return mp.polyval(PP[::-1], t) / mp.polyval(QQ[::-1], t)
    return C40[0] + mp.quad(lambda t: mp.exp(-n * t) * B(t), [0, 1, 5, 20, mp.inf])


NS_BP = [1, 2, 3, 4, 5, 8, 10, 16, 24]
BP = {}
for n in NS_BP:
    ex = mp.mpf(1) if n == 1 else corde2_hp(n, 2 * n / (n + 1) + 2 / (3 * n * n), 60)
    val = borel_pade(n)
    errs = [abs(ex - serie(n, J)) for J in range(1, 41)]
    BP[n] = (val, ex, abs(val - ex), min(errs))
mp.mp.dps = 60
assert BP[2][2] < 1e-8 and BP[24][2] < 1e-24
REELS = sorted(float(mp.re(z)) for z in VRAIS if abs(mp.im(z)) < 1e-6)
PROCHE_PI = min(VRAIS, key=lambda z: abs(z - (-L0 + 1j * mp.pi)) if mp.im(z) > 0 else mp.inf)
assert max(REELS) < -float(L0) and abs(max(REELS) + float(L0)) < 0.002
assert abs(PROCHE_PI - (-L0 + 1j * mp.pi)) < 0.2
ligne("**La resommation de Borel–Padé** (39 coefficients, approximant [19/19] de la transformée de Borel, intégrale de "
      "Laplace) :")
ligne()
ligne("| n | 1 | 2 (Ullisch) | 3 | 5 | 10 | 24 |")
ligne("|---|---|---|---|---|---|---|")
ligne("| erreur de Borel–Padé | " + " | ".join(sci_mp(BP[n][2]) for n in (1, 2, 3, 5, 10, 24)) + " |")
ligne("| troncature optimale | " + " | ".join(sci_mp(BP[n][3]) for n in (1, 2, 3, 5, 10, 24)) + " |")
ligne()
ligne(f"- En 2D, r² resommé = {mp.nstr(BP[2][0], 13).replace('.', ',')} pour {mp.nstr(BP[2][1], 13).replace('.', ',')} : "
      "la chèvre plane retrouvée depuis la dimension infinie.")
ligne(f"- Les pôles réels de l'approximant s'alignent de {fr(max(REELS), '{:.4f}')} vers −∞, en alternance avec ses "
      f"zéros : c'est la coupure, qui commence en −ln √2 = −{fr(float(L0), '{:.4f}')}. "
      f"({len(DOUBLETS)} pôle parasite, en {fr(float(mp.re(DOUBLETS[0])), '{:.3f}')}, est collé à un zéro : un "
      "doublet de Froissart, sans effet.)")
ligne(f"- Les pôles complexes les plus proches de −ln √2 ± iπ (la singularité suivante prédite, −0,347 ± 3,142i) "
      f"sont en {fr(float(mp.re(PROCHE_PI)), '{:.3f}')} ± {fr(float(mp.im(PROCHE_PI)), '{:.3f}')}i.")
ligne()

# ===========================================================================
# 2. Les bornes explicites
# ===========================================================================
ligne("## 2. Les bornes explicites, ordres 2 à 8")
ligne()


def padd(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def pscal(c, a):
    return [c * x for x in a]


def ppow(a, k):
    out = [1]
    for _ in range(k):
        out = pmul(out, a)
    return out


def pshift(a, n0):
    out = [0]
    for x in reversed(a):
        out = padd(pmul(out, [n0, 1]), [x])
    return out


def C_reste(J):
    """(n/2)^J/J!·(1/(2J+1))·(2,5/n)^(2J+1)·E[(E + 1,1)^(2J+1)] = C_reste/n^(J+1)."""
    EE = sum(comb(2 * J + 1, i) * Fr(11, 10) ** (2 * J + 1 - i) * factorial(i) for i in range(2 * J + 2))
    return Fr(1, 2 ** J * factorial(J) * (2 * J + 1)) * Fr(5, 2) ** (2 * J + 1) * EE


def borne_prouvee(J, C, n0):
    """Vrai si la condition de médiane change de signe entre S_J ∓ C/n^(J+1) pour tout n ≥ n0 (exact)."""
    Q = pmul([1, 1], [0] * (J + 1) + [1])
    qs = list(range(-(2 * J - 1), 2 * J, 2))
    D = ppow(Q, 2 * J - 1)
    for q in qs:
        D = pmul(D, [q, 1])
    ok = all(x >= 0 for x in pshift(D, n0))
    for signe in (1, -1):
        P = [0] * (J + 3)
        P[J + 2] += 2
        for i in range(2, J + 1):
            P = padd(P, pscal(MU_C[i], pmul([1, 1], [0] * (J + 1 - i) + [1])))
        P = padd(P, pscal(signe * C, [1, 1]))
        Wp = padd(Q, pscal(-1, P))
        num = [0]
        for j in range(J):
            p = 2 * j + 1
            bj = [1]
            for i in range(j):
                bj = pmul(bj, [-(3 + 2 * i), 1])
            cst = Fr((-1) ** j, 2 ** j * factorial(j) * (2 * j + 1) * 2 ** p)
            for i in range(p + 1):
                terme = pmul(pmul(ppow(Wp, p - i), ppow(Q, i + (2 * J - 1 - p))), [0, 1])
                for q in qs:
                    if q != 2 * i - p:
                        terme = pmul(terme, [q, 1])
                num = padd(num, pscal(cst * comb(p, i), pmul(terme, bj)))
        assert all(x == 0 for x in D[: J + 2])
        reste = pmul(padd([1], [0, C_reste(J)]), D[J + 2:])
        pol = pshift(pscal(-signe, padd(num, pscal(signe, reste))), n0)
        ok &= all(x >= 0 for x in pol) and pol[0] > 0
    return ok


# la zone centrale : borne numérique de son poids à n = 100 (elle décroît ensuite)
def zone_centrale(n, J):
    rho0 = math.sqrt(2) - 1
    tot = rho0 ** n
    for j in range(J):
        tot += (n / 2) ** j / (factorial(j) * (2 * j + 1)) * 2.0 ** (-(2 * j + 1)) * n * rho0 ** (n - 2 * j - 1) / (n - 2 * j - 1)
    return tot


BORNES = {}
for J in range(2, 9):
    cr = C_reste(J)
    C = int(2.05 * cr) + 1
    assert zone_centrale(100, J) < 100.0 ** -(J + 2)
    assert borne_prouvee(J, C, 100)
    BORNES[J] = (float(cr), C)
ligne("Même méthode que la partie XXIV, poussée à J termes de la série de l'équateur. Pour chaque J, on vérifie "
      "exactement (polynômes à coefficients entiers positifs en t = n − 100) que la condition de médiane change de "
      "signe entre S_J(n) ∓ C_J/n^(J+1), où S_J est la série coupée à 1/n^J. La zone centrale pèse moins que 1/n^(J+2).")
ligne()
ligne("| J | constante du reste | borne démontrée C_J (n ≥ 100) | vrai coefficient suivant |μ_(J+1)| |")
ligne("|---:|---|---|---|")
for J, (cr, C) in BORNES.items():
    ligne(f"| {J} | {sci(cr, 4)} | {sci(C, 4)} | {sci(abs(float(MU_C[J + 1])), 4)} |")
ligne()
ligne("Les constantes démontrées croissent comme les coefficients eux-mêmes (des factorielles) : la série est "
      "asymptotique, et chaque ordre est démontré.")
ligne()

# ===========================================================================
# 3. c₂ et c₃ exacts
# ===========================================================================
ligne("## 3. Le c_n de la partie XVI en dimensions 2 et 3, exactement")
ligne()
x_ = sp.symbols("x", positive=True)
cc_, ee_ = sp.symbols("c e")
dd_ = 1 / x_
rr2 = dd_ ** 2 + sp.Rational(1, 2) + cc_ * x_ ** 2 + ee_ * x_ ** 4
rr = sp.sqrt(rr2)
VOL = sp.pi * (1 + rr - dd_) ** 2 * (dd_ ** 2 + 2 * dd_ * rr - 3 * rr ** 2 + 2 * dd_ + 6 * rr - 3) / (12 * dd_)
ser3 = sp.expand(sp.series(VOL - sp.Rational(2, 3) * sp.pi, x_, 0, 6).removeO())
C3 = sp.solve(ser3.coeff(x_, 3), cc_)[0]
E3 = sp.solve(ser3.coeff(x_, 5).subs(cc_, C3), ee_)[0]
a1, a3, a5 = sp.symbols("a1 a3 a5")
psi = a1 * x_ + a3 * x_ ** 3 + a5 * x_ ** 5
O_ = 6
sps = sp.series(sp.sin(psi), x_, 0, O_).removeO()
cps = sp.series(sp.cos(psi), x_, 0, O_).removeO()
qq = sp.expand(1 - 2 * x_ * sps + x_ ** 2)
s_th = sp.series(sp.expand(cps * x_ * sp.series(1 / sp.sqrt(qq), x_, 0, O_).removeO()), x_, 0, O_ + 2).removeO()
th_ = sp.series(sp.asin(s_th), x_, 0, O_ + 2).removeO()
c_th = sp.series(sp.sqrt(1 - s_th ** 2), x_, 0, O_ + 2).removeO()
f2 = sp.expand(sp.series(sp.expand(qq / x_ ** 2 * (th_ - s_th * c_th)) - psi - sps * cps, x_, 0, O_).removeO())
SOL = {}
for k_, a_ in ((1, a1), (3, a3), (5, a5)):
    SOL[a_] = sp.solve(f2.coeff(x_, k_).subs(SOL), a_)[0]
cser2 = sp.expand(sp.series((1 - 2 * sps / x_).subs(SOL), x_, 0, 6).removeO())
C2, E2 = cser2.coeff(x_, 2), cser2.coeff(x_, 4)
assert cser2.coeff(x_, 0) == sp.Rational(1, 3)
c_n_formule = lambda n: sp.Rational(2 * n * (n - 1), 3 * (n + 1) ** 3 * (n + 3))  # noqa: E731
assert C2 == c_n_formule(2) == sp.Rational(4, 405) and C3 == c_n_formule(3) == sp.Rational(1, 96)
def terme_d(q, i, var="d"):
    q = sp.Rational(q)
    p_, d_ = abs(q.p), q.q
    pv = var if i == 1 else f"{var}{sup(i)}"
    corps = f"{p_}/{pv}" if d_ == 1 else f"{p_}/({d_}{pv})"
    return ("− " if q < 0 else "+ ") + corps


ligne("- **2D, par l'aire exacte de la lentille.** On paramètre par l'angle ψ = arcsin x₀ (le plan de la lentille) : "
      "r²(θ − sin θ cos θ) = ψ + sin ψ cos ψ, avec r² = d² − 2d sin ψ + 1. Le développement exact donne "
      f"k² − d² = 1/3 {terme_d(C2, 2)} {terme_d(E2, 4)} + …")
ligne(f"- **3D, par le volume exact de la lentille** (deux boules) : k² − d² = 1/2 {terme_d(C3, 2)} {terme_d(E3, 4)} + …")
ligne("- Ce sont exactement c₂ = 2·2·1/(3·3³·5) = 4/405 et c₃ = 2·3·2/(3·4³·6) = 1/96 : la formule "
      "c_n = 2n(n − 1)/(3(n + 1)³(n + 3)) de la partie XVI est démontrée en dimensions 2 et 3, où la méthode des "
      "moments ne s'appliquait pas.")
ligne(f"- Au passage, en 2D, le plan de la lentille est en sin ψ = x₀ avec ψ = "
      f"{terme_d(SOL[a1], 1).lstrip('+ ')} {terme_d(SOL[a3], 3)} {terme_d(SOL[a5], 5)} + …")
ligne()
NUM_C = {}
for n in (2, 3):
    for d in (10.0, 30.0):
        mu = mu_chevre(n, d)
        NUM_C[(n, d)] = mu * d * d
pred2 = lambda d: float(C2) + float(E2) / d ** 2  # noqa: E731
pred3 = lambda d: float(C3) + float(E3) / d ** 2  # noqa: E731
assert abs(NUM_C[(2, 30.0)] - pred2(30.0)) < 1e-7 and abs(NUM_C[(3, 30.0)] - pred3(30.0)) < 1e-7
ligne(f"Contrôle par l'intégrale radiale : en d = 30, (k² − d² − g²)·d² = {fr(NUM_C[(2, 30.0)], '{:.8f}')} (2D, "
      f"prédit {fr(pred2(30.0), '{:.8f}')}) et {fr(NUM_C[(3, 30.0)], '{:.8f}')} (3D, prédit {fr(pred3(30.0), '{:.8f}')}).")
ligne()

# ===========================================================================
# 4. L'unité du grain : le tournant de l'aiguille
# ===========================================================================
ligne("## 4. L'unité du grain : l'angle de l'aiguille")
ligne()
ALPHA = {}
for n in (2, 3, 4, 8, 24, 100):
    r2v = corde2_hp(n, 2 * n / (n + 1) + 2 / (3 * n * n), 40)
    x0 = 1 - r2v / 2
    ALPHA[n] = (float(mp.degrees(mp.acos(x0))), float(x0), float(mp.asin(x0)))
assert abs(ALPHA[2][0] - 70.81) < 0.01 and abs(ALPHA[24][0] - 87.73) < 0.01
ligne("Le piquet en e₃ sur la sphère, l'aiguille tourne de e₃ vers e₂ (partie XXI). Elle passe le bord de la chèvre "
      "de dimension n à l'angle α_n tel que 2 − 2cos α_n = r_n², donc **cos α_n = x₀ exactement** : l'écart au "
      "croisement vaut 90° − α_n = arcsin x₀.")
ligne()
ligne("| n | 2 | 3 | 4 | 8 | 24 | 100 |")
ligne("|---|---|---|---|---|---|---|")
ligne("| α_n | " + " | ".join(fr(ALPHA[n][0], "{:.2f}") + "°" for n in ALPHA) + " |")
ligne("| x₀ = cos α_n | " + " | ".join(fr(ALPHA[n][1], "{:.4f}") for n in ALPHA) + " |")
ligne("| écart arcsin x₀ (radian) | " + " | ".join(fr(ALPHA[n][2], "{:.4f}") for n in ALPHA) + " |")
ligne()
LECTURES = [("corde relative (√2 − r)/√2", Fr(1, 2)), ("corde √2 − r", "1/√2"), ("coquille (partie XXIII)", "ln 2"),
            ("plan x₀ = cos α_n", Fr(1)), ("crans log₂(2/r²)", "1/ln 2"), ("diamètre 2(√2 − r)", "√2"),
            ("aire 2 − r²", Fr(2))]
ligne("**Le miroir des lectures.** Chaque lecture lit n ≈ κ/ε. Les κ vont par paires de produit 1 autour du plan : "
      "(1/2, 2) la corde relative et l'aire, (1/√2, √2) la corde et le diamètre, (ln 2, 1/ln 2) la coquille et les "
      "crans. Le plan est leur moyenne géométrique : le miroir x·x′ = f² avec f = 1.")
ligne()
ligne("| lecture | " + " | ".join(nom for nom, _ in LECTURES) + " |")
ligne("|---|" + "---|" * len(LECTURES))
ligne("| κ | " + " | ".join(str(kv) for _, kv in LECTURES) + " |")
ligne()

# ===========================================================================
# 5. La tranche 49 – 55
# ===========================================================================
ligne("## 5. La tranche 10⁻⁴⁹ – 10⁻⁵⁵")
ligne()
TR = list(range(49, 56))
NMAX = 56
THETA = [0] * (NMAX + 1)
for a in range(-isqrt(NMAX), isqrt(NMAX) + 1):
    THETA[a * a] += 1
RD = {0: [1] + [0] * NMAX}
for d in range(1, 25):
    prev, new = RD[d - 1], [0] * (NMAX + 1)
    for i, x in enumerate(prev):
        if x:
            for j in range(NMAX + 1 - i):
                if THETA[j]:
                    new[i + j] += x * THETA[j]
    RD[d] = new


def reps(k, d):
    out = []

    def rec(rest, maxv, pref):
        if len(pref) == d:
            if rest == 0:
                out.append(tuple(pref))
            return
        for a in range(min(maxv, isqrt(rest)), -1, -1):
            rec(rest - a * a, a, pref + [a])
    rec(k, isqrt(k), [])
    return out


MINC = {k: next(d for d in range(1, 5) if RD[d][k]) for k in TR}
assert [MINC[k] for k in TR] == [1, 2, 3, 2, 2, 3, 4]
IMOD = {k: [x for x in range(k) if (x * x + 1) % k == 0] for k in TR}
assert [k for k in TR if IMOD[k]] == [50, 53]
DECOMP = {k: [r for r in reps(k, MINC[k]) if min(r) > 0] for k in TR}
ligne("| k | facteurs | k mod 8 | carrés min. | aiguilles (sans zéro) | r₂ | r₃ | r₄ | i modulo k |")
ligne("|---:|---|---:|---:|---|---:|---:|---:|---|")
for k in TR:
    fac = " · ".join(f"{p}{sup(e) if e > 1 else ''}" for p, e in sp.factorint(k).items())
    aig = " ; ".join("(" + ", ".join(map(str, r)) + ")" for r in DECOMP[k][:3])
    ligne(f"| {k} | {fac} | {k % 8} | {MINC[k]} | {aig} | {RD[2][k]} | {RD[3][k]} | {RD[4][k]} | "
          f"{', '.join(map(str, IMOD[k])) or '—'} |")
ligne()
ligne("- **Une dimension par cran** (partie XXI) : l'aiguille (7, 1, …, 1) à j uns a pour carré 49 + j. La tranche "
      "est cette aiguille vue de la dimension 1 à la dimension 7.")
ligne("- **Le miroir de la tranche** : 49 + 55 = 50 + 54 = 51 + 53 = 2·52, donc 10⁻⁴⁹·10⁻⁵⁵ = 10⁻⁵⁰·10⁻⁵⁴ = "
      "10⁻⁵¹·10⁻⁵³ = (10⁻⁵²)². Sept niveaux, centre 52, quatre en bas et quatre en haut.")
ligne("- **La tranche parcourt les restes 1 à 7 modulo 8** : 49 ≡ 1 … 55 ≡ 7. Elle finit sur la colonne interdite "
      "de Legendre (partie XXI) : comme 7, 55 exige quatre carrés.")
ligne()
C_EQ = 2 * erfinv(0.5) ** 2
ligne("| k | plan (n = 10ᵏ − 4/3) | aire (2·10ᵏ − 4/3) | coquille ≈ ln 2·10ᵏ | équateur ≈ 0,455·10²ᵏ | ménisque ≈ 0,577·10^(k/2) |")
ligne("|---:|---|---|---|---|---|")
for k in TR:
    men = 1 / math.sqrt(3) * 10 ** (k / 2 - math.floor(k / 2))
    ligne(f"| {k} | 10{sup(k)} | 2·10{sup(k)} | {fr(math.log(2), '{:.3f}')}·10{sup(k)} | "
          f"{fr(C_EQ, '{:.3f}')}·10{sup(2 * k)} | {fr(men, '{:.3f}')}·10{sup(math.floor(k / 2))} |")
ligne()
ligne("- Aux exposants impairs (49, 51, 53, 55), le ménisque fait apparaître √10 : 0,577·10^24,5 = 1,826·10²⁴.")
ligne()
# blocs de chiffres en dimension 10^k
MOTIF_OK = True
for k in TR:
    r2k = sum(q / Fr(10 ** k) ** i for i, q in enumerate(R2N))
    ent = r2k.numerator // r2k.denominator
    dec = str(((r2k - ent) * 10 ** (4 * k)).numerator // ((r2k - ent) * 10 ** (4 * k)).denominator).zfill(4 * k)
    blocs = [dec[i * k:(i + 1) * k] for i in range(4)]
    attendu = ["9" * (k - 1) + "8", "0" * (k - 1) + "2", "6" * (k - 2) + "58", "1" + "3" * (k - 3) + "92"]
    MOTIF_OK &= (ent == 1 and blocs == attendu)
assert MOTIF_OK
ligne("**Les chiffres de la corde.** Pour chaque k de 49 à 55, en dimension 10ᵏ, les quatre premiers blocs de k "
      "chiffres sont les mêmes, à la longueur près : 99…98 | 00…02 | 66…6658 | 133…3392 (vérifié exactement). "
      "La tranche est autosimilaire : une décade de plus allonge chaque bloc d'un chiffre.")
ligne()
ligne(f"**Décades et crans.** La tranche couvre 6 décades, soit 6·log₂ 10 = {fr(6 * math.log2(10), '{:.2f}')} crans. "
      "2²⁰ = 1 048 576 dépasse 10⁶ de 4,86 % : vingt crans de diaphragme couvrent la tranche, à la virgule « kibi » "
      "près (partie XIX).")
ligne()

# ===========================================================================
# 6. Les tournants d'aiguilles
# ===========================================================================
ligne("## 6. Les tournants d'aiguilles")
ligne()
PLAN = {}
for k in TR:
    pts = sorted([(a, b) for a in range(-8, 9) for b in range(-8, 9) if a * a + b * b == k],
                 key=lambda p: math.atan2(p[1], p[0]))
    if not pts:
        continue
    q1 = [p for p in pts if p[0] > 0 and p[1] >= 0]
    rots = []
    for v in q1:
        w = pts[(pts.index(v) + 1) % len(pts)]
        re_, im_ = v[0] * w[0] + v[1] * w[1], v[0] * w[1] - v[1] * w[0]
        g = gcd(gcd(abs(re_), abs(im_)), k)
        rots.append((v, w, re_ // g, im_ // g, k // g, math.degrees(math.atan2(im_, re_))))
    th0 = math.atan2(q1[0][1], q1[0][0])
    rel = lambda p, th0=th0: (math.atan2(p[1], p[0]) - th0) % (2 * math.pi)  # noqa: E731
    tour = sorted([p for p in pts if rel(p) <= math.pi + 1e-9], key=rel)
    aire = sum(abs(a[0] * b[1] - a[1] * b[0]) for a, b in zip(tour, tour[1:])) / 2
    PLAN[k] = (pts, q1, rots, tour, aire)
assert sorted(PLAN) == [49, 50, 52, 53] and PLAN[50][4] == 74 and PLAN[49][4] == 49
ligne("**Dans le plan** (parties XIV et XXI), seules 49, 50, 52 et 53 ont des aiguilles. Elles tournent par des "
      "angles pythagoriciens (rotation (a + bi)/c de la grille) :")
ligne()
ligne("| k | aiguilles du premier quadrant | rotations | demi-tour autour d'un bout : cases balayées | demi-disque πk/2 |")
ligne("|---:|---|---|---|---|")
for k, (pts, q1, rots, tour, aire) in PLAN.items():
    rtxt = " ; ".join(f"{fr(a_, '{:.2f}')}° = ({re_} + {im_}i)/{c_}" for _, _, re_, im_, c_, a_ in rots)
    ligne(f"| {k} | {', '.join(str(p) for p in q1)} | {rtxt} | {aire:.0f} ({len(tour)} positions) | "
          f"{fr(math.pi * k / 2, '{:.1f}')} |")
ligne()
VERS45 = []
for (a, b) in ((7, 0), (7, 1), (6, 4), (7, 2)):
    c_, d_ = a + b, a - b
    g = gcd(c_, d_)
    c_, d_ = c_ // g, d_ // g
    VERS45.append((a, b, c_, d_, a * c_ - b * d_))
    assert a * c_ - b * d_ == a * d_ + b * c_
ligne("**Vers 45°, la diagonale 1x, 1y** (la chèvre de dimension infinie) : chaque aiguille du plan y arrive avec "
      "une aiguille complémentaire.")
ligne()
for a, b, c_, d_, s_ in VERS45:
    ligne(f"- ({a} + {b}i)({c_} + {d_}i) = {s_}(1 + i) : arctan({b}/{a}) + arctan({d_}/{c_}) = 45°")
ligne("- Pour 50, le complément est 4 + 3i, l'aiguille 3-4-5 : c'est la formule de Hermann de la partie XXI.")
ligne()
ligne("**Combien de dimensions pour que l'aiguille existe et tourne.** Nombre r_d(k) de points du réseau ℤᵈ à "
      "distance √k de l'origine :")
ligne()
ligne("| d | " + " | ".join(str(k) for k in TR) + " |")
ligne("|---:|" + "---|" * len(TR))
for d in (1, 2, 3, 4, 5, 8):
    ligne(f"| {d} | " + " | ".join(str(RD[d][k]) for k in TR) + " |")
ligne()
# Ramanujan pour r24
NT = 56
DEL = [1] + [0] * NT
for m in range(1, NT + 1):
    for _ in range(24):
        for i in range(NT, m - 1, -1):
            DEL[i] -= DEL[i - m]
TAU = {k: DEL[k - 1] for k in range(1, NT + 1)}
assert [TAU[k] for k in range(1, 8)] == [1, -24, 252, -1472, 4830, -6048, -16744]


def sig11s(n):
    return sum((-1) ** (n + d) * d ** 11 for d in range(1, n + 1) if n % d == 0)


for k in TR:
    t2 = TAU[k // 2] if k % 2 == 0 else 0
    assert Fr(16, 691) * sig11s(k) + Fr(128, 691) * ((-1) ** (k - 1) * 259 * TAU[k] - 512 * t2) == RD[24][k]
ligne("- **En 24D**, r₂₄(k) = (16/691)·σ*₁₁(k) + (128/691)·((−1)^(k−1)·259·τ(k) − 512·τ(k/2)) (Ramanujan), vérifié "
      "pour k = 49 … 55. Le τ de la partie XXI (Δ = η²⁴) compte les aiguilles de la tranche en dimension 24 : "
      f"τ(49) = {fr(TAU[49], '{}')}, τ(50) = {TAU[50]}, r₂₄(49) = {sci(RD[24][49], 4)}.")
ligne()


def stations(j, d):
    """Aiguilles w de ℤᵈ de même longueur que v = (7, 1^j), perpendiculaires à v : les arrêts du quart de tour."""
    k = 49 + j
    cnt = 0
    R = isqrt(k)

    def rec(pos, pref, s, dot):
        nonlocal cnt
        if pos == j + 1:
            if dot == 0:
                cnt += RD[d - j - 1][k - s] if d - j - 1 >= 0 else 0
            return
        poids = 7 if pos == 0 else 1
        for a in range(-R, R + 1):
            if s + a * a <= k:
                rec(pos + 1, pref, s + a * a, dot + poids * a)
    rec(0, [], 0, 0)
    return cnt


STATIONS = {j: {d: stations(j, d) for d in range(max(2, j + 1), 9)} for j in range(4)}
assert STATIONS[0][2] == 2 and STATIONS[1][3] == 2 and STATIONS[2][3] == 0 and STATIONS[2][4] == 24
ligne("**Le retournement i·i = −1 sur le réseau** (partie XX : une sphère S^(d−2) de chemins en dimension d). Les "
      "arrêts possibles du quart de tour sont les aiguilles du réseau de même longueur, perpendiculaires :")
ligne()
ligne("| aiguille | 2D | 3D | 4D | 5D | 6D | 8D |")
ligne("|---|---|---|---|---|---|---|")
for j in range(4):
    v = "(7" + ", 1" * j + ")"
    ligne(f"| {v} (carré {49 + j}) | " + " | ".join(str(STATIONS[j].get(d, "—")) for d in (2, 3, 4, 5, 6, 8)) + " |")
ligne()
ligne("- (7, 1, 1) n'a **aucun** arrêt perpendiculaire en 3D : sur le réseau, elle ne peut pas s'y retourner par deux "
      "quarts de tour. Il faut une quatrième dimension (24 arrêts).")
ligne()
GAP = {k: (10.0 ** -k, math.degrees(10.0 ** -k)) for k in TR}
ligne("**Le croisement, dans la tranche.** En tournant de e₃ vers e₂, l'aiguille passe la chèvre de dimension n à "
      "arcsin x₀ ≈ 1/(n + 4/3) radian du croisement. Les chèvres de dimension 10⁴⁹ à 10⁵⁵ sont donc passées dans "
      "les derniers 10⁻⁴⁹ radian (5,7·10⁻⁴⁸ degré) du quart de tour, une décade d'angle par décade de dimension.")
ligne()

# ===========================================================================
# 7. Les liens
# ===========================================================================
ligne("## 7. Les liens avec les autres parties")
ligne()
LIENS = [
    ("XXIV", "la divergence au rythme 1/ln √2, mesurée", "dérivée, constante e^(−1/2)√(ln 2/π) ; Borel–Padé"),
    ("XXIV", "bornes explicites : ordre 2 seulement", "ordres 2 à 8 démontrés pour n ≥ 100"),
    ("XVI, XXIV", "c_n vérifié en 2D et 3D", "démontré par l'aire et le volume exacts de la lentille"),
    ("XX", "deux chèvres au même endroit", "la série de l'infini, resommée, redonne la chèvre plane"),
    ("XXI", "49-50-51, une dimension par cran", "la tranche 49 – 55 : l'aiguille (7, 1, …, 1) en 1 à 7 dimensions"),
    ("XXI", "√7 et Legendre", "55 ≡ 7 (mod 8) exige quatre carrés"),
    ("XXI", "le croisement, α_n", "cos α_n = x₀ : le grain comme angle"),
    ("XIV", "aiguilles de la grille, 3-4-5, demi-case", "rotations 3-4-5, 7-24-25, 5-12-13, 28-45-53 ; demi-tours"),
    ("XIX", "i modulo une base, aiguille primitive", "i n'existe que modulo 50 et 53 dans la tranche"),
    ("XX", "retournement : S^(d−2) chemins", "arrêts du réseau ; aucun pour (7, 1, 1) en 3D"),
    ("XXI", "τ de Ramanujan, Δ = η²⁴", "r₂₄(k) de la tranche par τ(k)"),
    ("XIX", "kilo contre kibi", "20 crans ≈ 6 décades"),
]
ligne("| partie | ce qu'on avait | ce que la partie XXV ajoute |")
ligne("|---|---|---|")
for a, b, c in LIENS:
    ligne(f"| {a} | {b} | {c} |")
ligne()

with open(os.path.join(ICI, "..", "resultats", "tranche_aiguilles.md"), "w") as fh:
    fh.write("\n".join(md) + "\n")
print(f"calculs : {time.time() - T0:.1f} s (coefficients : {T_COEF:.1f} s)")

# ===========================================================================
# Figures z1 et z2
# ===========================================================================
T1 = time.time()


def legende(ax, texte, y=-0.13):
    ax.text(0.5, y, texte, transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)


def schema(ax, xlim, ylim, egal=True):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if egal:
        ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for sp_ in ax.spines.values():
        sp_.set_visible(False)


# --------------------------- z1 : les ouverts ---------------------------
fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.22, hspace=0.38)

# a) les grands ordres
ax = fig.add_subplot(gs[0, 0])
ms_ = np.array(sorted(RATIO))
ax.plot(1 / ms_, [float(RATIO[m]) for m in ms_], "o", color=F.BLEU, ms=5, label="r²_m ÷ prédiction (m = 4 … 40)")
xx = np.linspace(0, 0.045, 100)
coef6 = [float(c) for c in RICH[6]]
ax.plot(xx, sum(c * xx ** j for j, c in enumerate(coef6)), color=F.ORANGE, lw=1.4, label="ajustement de Richardson")
ax.axhline(1, color=ROUGE, lw=1.4, ls="--")
ax.plot([0], [float(RICH[6][0])], "*", color=ROUGE, ms=15, zorder=6, label=f"limite : {fr(float(RICH[6][0]), '{:.6f}')}")
ax.set_xlim(-0.005, 0.26)
ax.set_ylim(0.88, 1.012)
ax.set_xlabel("1/m")
ax.set_ylabel("coefficient exact ÷ formule des grands ordres")
ax.legend(loc="lower left", fontsize=8.5, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.text(0.97, 0.97, "r²_m ≈ (−1)^m · e^(−1/2)·√(ln 2/π)\n· Γ(m − ½) · (2/ln 2)^m", transform=ax.transAxes, ha="right",
        va="top", fontsize=9.6, color=F.INK, bbox=dict(boxstyle="round,pad=0.4", fc=F.SURF, ec=F.BASE))
ax.set_title("a)  La divergence, constante comprise")
legende(ax, "Les 40 coefficients exacts divisés par la formule dérivée de la forme de Laplace : le rapport\n"
        "tend vers 1 (à 10⁻⁵ près). La divergence vient du bord de la calotte à 45°, qui « sent » le\n"
        "sommet du sinus à 90° : la singularité est en −ln √2 = −ln sin 45°.")

# b) la meilleure précision
ax = fig.add_subplot(gs[0, 1])
nb = np.array(NS_OPT)
ax.plot(nb, [float(OPT[n][1] * n * mp.mpf(2) ** (mp.mpf(n) / 2)) for n in NS_OPT], "o-", color=F.BLEU, ms=4.5,
        lw=1.4, label="erreur optimale × n·2^(n/2)")
ax.plot(nb, [float(OPT[n][2] * n * mp.mpf(2) ** (mp.mpf(n) / 2) / 2) for n in NS_OPT], "s--", color=F.ORANGE, ms=4,
        lw=1.1, label="moitié du plus petit terme × n·2^(n/2)")
ax.axhline(float(PRED_ERR), color=ROUGE, lw=1.5, ls="--", label=f"prédit : e^(−1/2)·√(2/ln 2) = {fr(float(PRED_ERR), '{:.4f}')}")
ax.set_xlabel("dimension n")
ax.set_ylabel("erreur × n·2^(n/2)")
ax.set_ylim(0.85, 1.08)
ax.legend(loc="lower right", fontsize=8.5, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("b)  La meilleure précision : 1,03·2^(−n/2)/n")
legende(ax, "On coupe la série à son plus petit terme (vers j ≈ n·ln √2). L'erreur restante vaut la moitié de\n"
        "ce terme, comme pour la série de Stirling, et tend vers la constante prédite : 0,15 chiffre par\n"
        "dimension, plus log₁₀ n. C'est la limite de la série seule, pas de la chèvre.")

# c) Borel–Padé
ax = fig.add_subplot(gs[0, 2])
nbp = np.array(NS_BP, dtype=float)
ax.semilogy(nbp, [float(BP[n][2]) for n in NS_BP], "o-", color=F.BLEU, ms=6, lw=1.6, label="Borel–Padé [19/19]")
ax.semilogy(nbp, [float(BP[n][3]) for n in NS_BP], "s-", color=F.ORANGE, ms=5, lw=1.3, label="troncature optimale")
ax.annotate("la chèvre plane\n(Ullisch) : 6·10⁻¹⁰", (2, float(BP[2][2])), (6.0, 1e-8), fontsize=9, color=F.BLEU,
            fontweight="bold", arrowprops=dict(arrowstyle="-", color=F.BLEU, lw=0.8))
ax.annotate("dimension 1 :\nr = 1 à 10⁻⁶", (1, float(BP[1][2])), (3.2, 1e-4), fontsize=8.8, color=F.BLEU,
            arrowprops=dict(arrowstyle="-", color=F.BLEU, lw=0.8))
ax.set_xlabel("dimension n")
ax.set_ylabel("écart à la corde exacte |Δr²|")
ax.set_ylim(1e-28, 3)
ax.legend(loc="upper right", fontsize=8.6, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("c)  Resommée, la série redonne la chèvre plane")
legende(ax, "La série en 1/n, développée autour de la dimension infinie, diverge. Resommée par Borel–Padé\n"
        "(39 coefficients), elle redonne pourtant la corde exacte : la chèvre plane à 10 chiffres, celle de\n"
        "la 3D à 12. Les deux chèvres de la partie XX sont reliées par un calcul exact.")

# d) les pôles de Borel–Padé
ax = fig.add_subplot(gs[1, 0])
ax.axhline(0, color=F.BASE, lw=0.8)
ax.axvline(0, color=F.BASE, lw=0.8)
ax.plot([-float(L0), -2.2], [0, 0], color=ROUGE, lw=3, alpha=0.35, solid_capstyle="butt", label="coupure prédite")
for sgn in (1, -1):
    ax.plot([-float(L0), -2.2], [sgn * math.pi, sgn * math.pi], color=ROUGE, lw=3, alpha=0.2, solid_capstyle="butt")
zr = [z for z in ZEROS if -2.2 < float(mp.re(z)) < 0.6 and abs(float(mp.im(z))) < 6.4]
ax.plot([float(mp.re(z)) for z in zr], [float(mp.im(z)) for z in zr], "o", mfc="none", mec=F.MUTED, ms=6,
        label="zéros de l'approximant")
pv = [z for z in VRAIS if -2.2 < float(mp.re(z)) < 0.6 and abs(float(mp.im(z))) < 6.4]
ax.plot([float(mp.re(z)) for z in pv], [float(mp.im(z)) for z in pv], "o", color=F.BLEU, ms=6,
        label="pôles de l'approximant")
ax.plot([float(mp.re(z)) for z in DOUBLETS], [float(mp.im(z)) for z in DOUBLETS], "x", color=F.INK2, ms=9, mew=2,
        label="doublet de Froissart")
for yb in (0, math.pi, -math.pi):
    ax.plot([-float(L0)], [yb], "*", color=ROUGE, ms=16, zorder=6)
ax.text(-float(L0) + 0.06, 0.35, "−ln √2", color=ROUGE, fontsize=10, fontweight="bold")
ax.text(-float(L0) + 0.08, math.pi + 0.3, "−ln √2 + iπ", color=ROUGE, fontsize=9.5)
ax.text(-float(L0) + 0.08, -math.pi - 0.6, "−ln √2 − iπ", color=ROUGE, fontsize=9.5)
ax.set_xlim(-2.2, 0.6)
ax.set_ylim(-6.5, 9.2)
ax.set_xlabel("partie réelle de t")
ax.set_ylabel("partie imaginaire de t")
ax.legend(loc="upper right", fontsize=8.2, frameon=True, facecolor=F.SURF, edgecolor="none", ncol=2)
ax.set_title("d)  Les singularités de Borel, là où la théorie les met")
legende(ax, "Dans le plan de Borel, les pôles de l'approximant s'alignent sur la coupure qui part de −ln √2,\n"
        "en alternance avec ses zéros, et la paire suivante se place près de −ln √2 ± iπ (étoiles). C'est la\n"
        "racine carrée de tan φ(u), là où sin φ = 1 : le sommet du sinus, à 90°.")

# e) les bornes démontrées
ax = fig.add_subplot(gs[1, 1])
NS_B = [100, 150, 200, 300, 500, 700, 1000, 2000, 3000, 5000, 10000]
HPB = {n: corde2_hp(n, float(serie(n, 6))) for n in NS_B}
cols_b = {2: F.RAMPE[1], 4: F.RAMPE[2], 6: F.RAMPE[3], 8: F.RAMPE[4]}
for J, col in cols_b.items():
    S_J = {n: 2 * mp.mpf(n) / (n + 1) + sum(mp.mpf(MU_C[i].numerator) / MU_C[i].denominator / mp.mpf(n) ** i
                                             for i in range(2, J + 1)) for n in NS_B}
    vrai = [float(abs(HPB[n] - S_J[n])) for n in NS_B]
    borne = [BORNES[J][1] / n ** (J + 1) for n in NS_B]
    ax.loglog(NS_B, vrai, "o-", color=col, ms=4, lw=1.6, label=f"J = {J} : écart réel")
    ax.loglog(NS_B, borne, "--", color=col, lw=1.2)
    ax.text(NS_B[-1] * 1.1, borne[-1], f"J = {J}", color=col, fontsize=8.5, va="center")
ax.plot([], [], "--", color=F.INK2, lw=1.2, label="borne démontrée C_J/n^(J+1)")
ax.set_xlim(90, 2.2e4)
ax.set_xlabel("dimension n")
ax.set_ylabel("|r_n² − S_J(n)|")
ax.legend(loc="lower left", fontsize=8.4, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("e)  Les ordres 2 à 8, démontrés pour n ≥ 100")
legende(ax, "Pour chaque ordre J, une borne explicite C_J/n^(J+1) (tirets), vérifiée exactement par des\n"
        "polynômes à coefficients entiers positifs, encadre l'écart réel (points). Les constantes sont\n"
        "grossières, mais chaque ordre est démontré, pas seulement mesuré.")

# f) c₂ et c₃ exacts
ax = fig.add_subplot(gs[1, 2])
DD = np.logspace(np.log10(1.5), 2, 16)
for n, col, cv, ev in ((2, F.BLEU, C2, E2), (3, F.ORANGE, C3, E3)):
    yv = [mu_chevre(n, float(d)) * d * d for d in DD]
    ax.semilogx(DD, yv, "o", color=col, ms=5, label=f"{n}D : intégrale radiale")
    dd2 = np.logspace(np.log10(1.5), 2, 200)
    ax.semilogx(dd2, float(cv) + float(ev) / dd2 ** 2, "-", color=col, lw=1.4,
                label=f"{n}D : {cv} {terme_d(ev, 2)} (exact)")
    ax.axhline(float(cv), color=col, lw=0.8, ls=":")
ax.set_xlabel("distance d du piquet au centre")
ax.set_ylabel("(k² − d² − g²) · d²")
ax.set_ylim(0.0085, 0.0108)
ax.legend(loc="lower right", fontsize=8.6, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("f)  Le c_n de la partie XVI, exact en 2D et 3D")
legende(ax, "Loin du pré, k² − d² − g² ≈ c_n/d². En 2D, l'aire exacte de la lentille donne 4/405, et en 3D\n"
        "son volume exact donne 1/96 : la formule 2n(n − 1)/(3(n + 1)³(n + 3)) de la partie XVI, que la\n"
        "méthode des moments ne couvrait pas en dimensions 2 et 3.")
F.sauver(fig, "z1_ouverts.png")

# --------------------------- z2 : la tranche et les aiguilles ---------------------------
fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.22, hspace=0.38)

# a) la colonne des sept niveaux
ax = fig.add_subplot(gs[0, 0])
schema(ax, (-3.3, 6.6), (-0.6, 7.9))
COUL_C = {1: F.SEQ[3], 2: F.SEQ[6], 3: F.SEQ[9], 4: F.SEQ[12]}
for i, k in enumerate(TR):
    y0 = i
    ax.add_patch(Rectangle((0, y0), 1, 1, fc=COUL_C[MINC[k]], ec=F.SURF, lw=2))
    ax.text(0.5, y0 + 0.5, str(k), ha="center", va="center", fontsize=12, fontweight="bold",
            color=F.SURF if MINC[k] >= 2 else F.INK)
    dec = DECOMP[k][0]
    aig = "(" + ", ".join(map(str, dec)) + ")"
    ax.text(1.25, y0 + 0.62, f"10⁻{str(k).translate(SUP)} R : n = 10{sup(k)} − 4/3", fontsize=8.9, color=F.INK)
    ax.text(1.25, y0 + 0.22, f"aiguille {aig} · {MINC[k]} carré{'s' if MINC[k] > 1 else ''}"
            + (f" · i ≡ {IMOD[k][0]}" if IMOD[k] else ""), fontsize=8.6, color=F.INK2)
for (a, b), col in (((49, 55), ROUGE), ((50, 54), F.ORANGE), ((51, 53), F.JAUNE)):
    ya, yb = a - 49 + 0.5, b - 49 + 0.5
    rayon = (yb - ya) / 2
    t_ = np.linspace(np.pi / 2, 3 * np.pi / 2, 100)
    ax.plot(-0.1 + rayon * 0.55 * np.cos(t_), (ya + yb) / 2 + rayon * np.sin(t_), color=col, lw=1.6)
ax.text(-1.95, 3.5, "miroir\nautour\nde 52", ha="center", va="center", fontsize=9, color=ROUGE)
ax.plot([-0.25, -0.25], [0.02, 3.98], color=F.INK2, lw=0)
for (y_a, y_b, nom) in ((0, 4, "4 en bas"), (3, 7, "4 en haut")):
    xb = 6.35 if nom == "4 en haut" else 6.05
    ax.plot([xb, xb], [y_a + 0.05, y_b - 0.05], color=F.MUTED, lw=1.2)
    ax.text(xb + 0.08, (y_a + y_b) / 2, nom, rotation=90, va="center", fontsize=8.6, color=F.MUTED)
for m_, lab in ((1, "1 carré"), (2, "2 carrés"), (3, "3 carrés"), (4, "4 carrés (Legendre)")):
    pass
ax.text(0, 7.25, "7 niveaux, centre 52 : 10⁻⁴⁹·10⁻⁵⁵ = (10⁻⁵²)²", fontsize=9.4, color=F.INK, fontweight="bold")
ax.set_title("a)  La tranche 10⁻⁴⁹ – 10⁻⁵⁵")
legende(ax, "Chaque niveau k : un plan de lentille à 10⁻ᵏ R et une aiguille de carré k.\n"
        "Couleur : nombre minimal de carrés (1 à 4). L'aiguille (7, 1, …, 1) gagne\n"
        "une dimension par niveau ; 55 ≡ 7 (mod 8) exige quatre carrés, comme 7\n"
        "(partie XXI). i n'existe que modulo 50 et 53.", y=-0.02)

# b) les aiguilles du plan
ax = fig.add_subplot(gs[0, 1])
schema(ax, (-0.5, 12.6), (-0.6, 8.3))
COUL_K = {49: F.INK2, 50: F.BLEU, 52: F.ORANGE, 53: VIOLET}
tt = np.linspace(0, np.pi / 2, 200)
from matplotlib.lines import Line2D  # noqa: E402
for k, col in COUL_K.items():
    rk = math.sqrt(k)
    ax.plot(rk * np.cos(tt), rk * np.sin(tt), color=col, lw=0.8, alpha=0.5)
    for (a, b) in PLAN[k][1] + ([(0, 7)] if k == 49 else []):
        ax.annotate("", (a, b), (0, 0), arrowprops=dict(arrowstyle="-|>", color=col, lw=1.6, mutation_scale=11))
ax.plot([0, 7.6], [0, 7.6], color=ROUGE, lw=1.0, ls="--")
ARCS = {50: ((7, 1), (5, 5), 2.4), 52: ((6, 4), (4, 6), 1.5), 53: ((7, 2), (2, 7), 3.4)}
for k, (v, w, r_arc) in ARCS.items():
    a0, a1_ = math.atan2(v[1], v[0]), math.atan2(w[1], w[0])
    ta = np.linspace(a0, a1_, 60)
    ax.plot(r_arc * np.cos(ta), r_arc * np.sin(ta), color=COUL_K[k], lw=1.5)
ETIQ = [((7, 0), 49, "(7, 0) : quarts de tour, 90°", (7.6, -0.25)),
        ((7, 1), 50, "(7, 1) → (5, 5) : 36,87° (3-4-5)", (7.6, 0.75)),
        ((7, 2), 53, "(7, 2) → (2, 7) : 58,11° (28-45-53)", (7.6, 1.75)),
        ((6, 4), 52, "(6, 4) → (4, 6) : 22,62° (5-12-13)", (7.6, 3.6)),
        ((5, 5), 50, "(5, 5) → (1, 7) : 36,87° ; (1, 7) → (−1, 7) : 16,26° (7-24-25)", None)]
for (a, b), k, txt, pos in ETIQ:
    if pos is None:
        continue
    ax.annotate(txt, (a, b), pos, fontsize=8.6, color=COUL_K[k], fontweight="bold", va="center",
                arrowprops=dict(arrowstyle="-", color=COUL_K[k], lw=0.6, alpha=0.7))
ax.text(7.6, 5.0, "50 continue : (5, 5) → (1, 7) : 36,87°\npuis (1, 7) → (−1, 7) : 16,26° (7-24-25)", fontsize=8.4,
        color=COUL_K[50], va="center")
ax.legend(handles=[Line2D([], [], color=COUL_K[k], lw=2, label=f"carré {k}") for k in COUL_K]
          + [Line2D([], [], color=ROUGE, lw=1, ls="--", label="45° : la diagonale 1x, 1y")],
          loc="upper right", fontsize=8.4, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("b)  Les aiguilles du plan et leurs tournants")
legende(ax, "Sur la grille, une aiguille de carré k ne tourne que vers les points du cercle\n"
        "de rayon √k, par des angles pythagoriciens ; par quarts de tour pour 49.\n"
        "51, 54 et 55 n'ont aucune aiguille dans le plan (Fermat).", y=-0.02)

# c) combien de dimensions
ax = fig.add_subplot(gs[0, 2])
DS_ = [1, 2, 3, 4, 5, 6, 8]
M = np.array([[RD[d][k] for k in TR] for d in DS_], dtype=float)
im_ = ax.imshow(np.where(M > 0, np.log10(np.maximum(M, 1)), np.nan), cmap="Blues", aspect="auto", origin="lower",
                vmin=0, vmax=7)
for i, d in enumerate(DS_):
    for j, k in enumerate(TR):
        v = int(M[i, j])
        txt = "0" if v == 0 else (str(v) if v < 1e5 else sci(v, 2))
        ax.text(j, i, txt, ha="center", va="center", fontsize=7.8,
                color=ROUGE if v == 0 else (F.SURF if v > 3000 else F.INK), fontweight="bold" if v == 0 else None)
    for j, k in enumerate(TR):
        if MINC[k] == d:
            ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, ec=ROUGE, lw=2))
ax.set_xticks(range(len(TR)))
ax.set_xticklabels([str(k) for k in TR])
ax.set_yticks(range(len(DS_)))
ax.set_yticklabels([f"{d}D" for d in DS_])
ax.grid(False)
ax.set_xlabel("carré k de l'aiguille")
ax.set_title("c)  Combien de dimensions pour que l'aiguille existe")
legende(ax, "Nombre d'aiguilles du réseau ℤᵈ de carré k (cadres rouges : la première dimension où il y en a).\n"
        "Fermat ferme le plan à 51, 54 et 55 ; Legendre ferme l'espace à 55 ; Lagrange ouvre tout en 4D.\n"
        "En 24D, ces nombres sont donnés par le τ de Ramanujan (partie XXI), vérifié pour k = 49 … 55.")

# d) le retournement sur le réseau
ax = fig.add_subplot(gs[1, 0])
cols_s = [F.RAMPE[1], F.RAMPE[2], F.RAMPE[3], F.RAMPE[4]]
for j in range(4):
    dd = sorted(STATIONS[j])
    vals = [STATIONS[j][d] for d in dd]
    v_plot = [v if v > 0 else 0.5 for v in vals]
    ax.semilogy(dd, v_plot, "o-", color=cols_s[j], ms=6, lw=1.6, label="(7" + ", 1" * j + f") : carré {49 + j}")
    for d, v in zip(dd, vals):
        if v == 0:
            ax.plot([d], [0.5], "X", color=ROUGE, ms=13, zorder=6)
            ax.annotate("aucun arrêt :\n(7, 1, 1) ne se retourne\npas sur le réseau 3D", (d, 0.5), (3.6, 0.09),
                        fontsize=8.8, color=ROUGE, arrowprops=dict(arrowstyle="-", color=ROUGE, lw=0.8))
ax.set_ylim(0.05, 1e6)
ax.set_xlim(1.7, 8.4)
ax.set_xlabel("dimension d")
ax.set_ylabel("arrêts du quart de tour (aiguilles perpendiculaires)")
ax.legend(loc="upper left", fontsize=8.6, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("d)  Le retournement i·i = −1 sur le réseau")
legende(ax, "Retourner l'aiguille, c'est deux quarts de tour par une aiguille\n"
        "perpendiculaire de même longueur (partie XX : une sphère S^(d−2) de chemins).\n"
        "Sur le réseau, ces arrêts se comptent : 2 dans le plan, puis de plus en plus\n"
        "avec la dimension, avec des trous arithmétiques.", y=-0.13)

# e) le croisement et les chèvres
ax = fig.add_subplot(gs[1, 1])
NSC_ = np.logspace(0, 4, 18)
gap_num = []
for n in NSC_:
    if n == 1:
        gap_num.append(math.asin(0.5))
    else:
        mu = mu_chevre(float(n))
        gap_num.append(math.asin(1 / (n + 1) - mu / 2))
ax.loglog(NSC_, gap_num, "o", color=F.BLEU, ms=5, label="écart 90° − α_n (calculé)")
NL = np.logspace(0.2, 60, 300)
ax.loglog(NL, 1 / (NL + 4 / 3), "-", color=F.BLEU, lw=1.4, label="≈ 1/(n + 4/3) : la lecture du plan")
ax.loglog(NL, 2 / (NL + 4 / 3), "--", color=VIOLET, lw=1.2, label="2/(n + 4/3) : la lecture de l'aire")
ax.axvspan(1e49, 1e55, color=F.ORANGE, alpha=0.18)
ax.axhspan(1e-55, 1e-49, color=F.ORANGE, alpha=0.12)
ax.text(10 ** 52, 10 ** -20, "la tranche\n10⁴⁹ – 10⁵⁵", ha="center", fontsize=9.4, color=F.ORANGE, fontweight="bold")
for n, (a_deg, x0v, gap), pos in ((2, ALPHA[2], (1e9, 1e-2)), (24, ALPHA[24], (1e13, 1e-7))):
    ax.annotate(f"{n}D : α = {fr(a_deg, '{:.2f}')}°", (n, gap), pos, fontsize=8.8, color=F.BLEU,
                arrowprops=dict(arrowstyle="-", color=F.BLEU, lw=0.7))
ax.set_xlim(1, 1e60)
ax.set_ylim(1e-60, 3)
ax.set_xlabel("dimension n de la chèvre")
ax.set_ylabel("angle restant avant le croisement (radian)")
ax.legend(loc="lower left", fontsize=8.6, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("e)  L'aiguille passe les chèvres : cos α_n = x₀")
legende(ax, "En tournant de e₃ vers e₂ (partie XXI), l'aiguille passe le bord de la chèvre\n"
        "de dimension n à arcsin x₀ ≈ 1/(n + 4/3) radian du croisement. Le grain angulaire\n"
        "est la lecture du plan ; l'aire est un cran au-dessus, invisible sur 60 décades.\n"
        "Toute la tranche tient dans les derniers 10⁻⁴⁹ radian.", y=-0.13)

# f) décades et crans
ax = fig.add_subplot(gs[1, 2])
schema(ax, (-49.35, -55.9), (-1.6, 3.0), egal=False)
ax.plot([-49, -55], [1.6, 1.6], color=F.INK, lw=1.4)
for k in TR:
    ax.plot([-k, -k], [1.45, 1.75], color=F.INK, lw=1.6)
    ax.text(-k, 1.92, f"10⁻{str(k).translate(SUP)}", ha="center", fontsize=9.6, color=F.INK)
ax.plot([-49, -49 - 20 * math.log10(2)], [0.4, 0.4], color=F.ORANGE, lw=1.4)
for j in range(21):
    x = -49 - j * math.log10(2)
    ax.plot([x, x], [0.28, 0.52], color=F.ORANGE, lw=1.2 if j % 5 else 2)
    if j % 5 == 0:
        ax.text(x, 0.0, f"2⁻{str(j).translate(SUP)}" if j else "1", ha="center", fontsize=9, color=F.ORANGE)
xk = -49 - 20 * math.log10(2)
ax.annotate("", (xk, 0.75), (-55, 1.35), arrowprops=dict(arrowstyle="<->", color=ROUGE, lw=1.2))
ax.text((xk - 55) / 2 - 0.05, 1.05, "virgule kibi :\n2²⁰/10⁶ = 1,0486", ha="right", fontsize=8.8, color=ROUGE)
ax.text(-49.05, 2.55, "décades : un pas de ton échelle", fontsize=9.4, color=F.INK, fontweight="bold")
ax.text(-49.05, -0.65, "crans : 20 doublements (×2 en aire, √2 en longueur)", fontsize=9.4, color=F.ORANGE,
        fontweight="bold")
ax.text(-49.05, -1.15, "1 décade = log₂ 10 = 3,32 crans ; 6 décades = 19,93 crans", fontsize=9, color=F.INK2)
ax.set_title("f)  Six décades, vingt crans")
legende(ax, "La tranche couvre 6 décades, soit 19,93 crans de diaphragme : les deux échelles (base 10 et\n"
        "base 2) se ratent de 4,86 % au bout, la virgule entre kilo et kibi (partie XIX). Le facteur 2\n"
        "entre le plan et l'aire (partie XXIV) est un seul de ces crans.", y=-0.02)
F.sauver(fig, "z2_tranche_aiguilles.png")
print(f"figures : {time.time() - T1:.1f} s ; total : {time.time() - T0:.1f} s")
