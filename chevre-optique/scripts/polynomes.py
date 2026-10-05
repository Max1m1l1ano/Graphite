"""
Partie VII : les nombres des polynômes de la chèvre (dimensions impaires) et
des équations des dimensions paires 6, 12, 24. Calculs et figure.

    python3 scripts/polynomes.py

Écrit resultats/polynomes.md et figures/g1_polynomes_retenues.png.

L'équation de la chèvre (pré de rayon 1, piquet au bord, corde r = 2 cos α)
s'écrit dans toutes les dimensions
    rⁿ · [Q_n(1) − Q_n(r/2)] = Q_n(1 − r²/2),   Q_n(c) = ∫₀^c (1 − u²)^((n−1)/2) du,
où Q_n est l'intégrale des tranches d'une calotte. En dimension impaire, Q_n
est un polynôme ; en dimension paire n = 2m, Q_n(c) = κ_n arcsin c + √(1 − c²) p_n(c),
avec κ_n = C(2m, m)/4^m.
"""

import os
import sys
import warnings

import matplotlib.pyplot as plt
import mpmath as mp
import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
import chevre as ch  # noqa: E402
import figures as F  # noqa: E402  (style et palette des parties précédentes)

warnings.filterwarnings("ignore", category=DeprecationWarning)  # sympy : comparaisons d'entiers modulaires
mp.mp.dps = 30
ICI = os.path.dirname(os.path.abspath(__file__))
r, u, x = sp.symbols("r u x")
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def v2(k):
    k, e = abs(int(k)), 0
    while k and k % 2 == 0:
        k //= 2
        e += 1
    return e


uns = lambda m: bin(m).count("1")
EXP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
IND = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")  # nombre de 1 en binaire = retenues de m + m en base 2 (Kummer)


def polynome_impair(n):
    """Polynôme entier (contenu 1, coefficient dominant > 0) de la corde en dimension impaire n."""
    m = (n - 1) // 2
    Q = lambda c: sp.integrate((1 - u ** 2) ** m, (u, 0, c))
    num = sp.fraction(sp.together(sp.expand(r ** n * (Q(1) - Q(r / 2)) - Q(1 - r ** 2 / 2))))[0]
    P = sp.Poly(num, r)
    P = sp.Poly(P.as_expr() / sp.gcd_list(P.coeffs()), r)
    return -P if P.LC() < 0 else P


def h(n):
    """Rapport hémisphère / cylindre de la partie IV : Q_n(1) = W_n(π)/2."""
    m = (n - 1) / sp.Integer(2)
    return sp.sqrt(sp.pi) * sp.gamma(m + 1) / (2 * sp.gamma(m + sp.Rational(3, 2)))


def kappa_p(m):
    """∫₀^x (1 − u²)^(m − 1/2) du = κ·arcsin x + √(1 − x²)·p(x), par la formule de réduction."""
    k, p = sp.Integer(1), sp.Integer(0)
    for j in range(1, m + 1):
        p = sp.expand(x * (1 - x ** 2) ** (j - 1) / (2 * j) + sp.Rational(2 * j - 1, 2 * j) * p)
        k = sp.Rational(2 * j - 1, 2 * j) * k
    return k, p


def ecrire(P):
    termes = [(P.degree() - i, c) for i, c in enumerate(P.all_coeffs()) if c != 0]
    t = " ".join(f"{'+' if c > 0 else '−'} {abs(c)}" + (f" r^{k}" if k > 1 else (" r" if k == 1 else "")) for k, c in termes)
    return t.lstrip("+ ")


# ---------------------------------------------------------------------------
# 1. Dimensions impaires
# ---------------------------------------------------------------------------
ligne("## 1. Dimensions impaires : des polynômes entiers\n")
ligne("| n | degré | polynôme (normalisé) | h_n | terme constant | racine | corde (partie I) |")
ligne("|---:|---:|---|---|---|---|---|")
IMPAIRS = {}
for n in (3, 5, 7, 9, 13):
    P = polynome_impair(n)
    IMPAIRS[n] = P
    racine = next(z for z in P.nroots(n=25) if z.is_real and 1 < z < 1.5)
    c0 = P.all_coeffs()[-1]
    texte = ecrire(P) if n <= 9 else f"273 r^24 − 7280 r^22 + … + 2^22 r^13 − 2^22 (degré {P.degree()})"
    ligne(f"| {n} | {P.degree()} | {texte} | {sp.nsimplify(h(n))} | {'−' if c0 < 0 else '+'}2^{v2(c0)} |"
          f" {mp.nstr(mp.mpf(str(racine)), 15)} | {mp.nstr(ch.corde_moitie_mp(n), 15)} |".replace(".", ","))
ligne("\nForme d'Archimède : h_n·(rⁿ − 1) = G_n(r²), polynôme pair en r. Exemples :")
for n in (3, 5, 7):
    P = IMPAIRS[n]
    cn = P.coeff_monomial(r ** n)
    G = sp.expand(-(P.as_expr() - cn * (r ** n - 1)) / cn * sp.nsimplify(h(n)))
    ligne(f"- n = {n} : ({sp.nsimplify(h(n))})·(r^{n} − 1) = " + str(G).replace("**", "^").replace("*", "·"))

# Groupe de Galois du polynôme de degré 24 (dimension 13) : Frobenius + théorème de Jordan
P13 = IMPAIRS[13]
fl = sp.factor_list(P13.as_expr())[1]
cycle_q, impaire = None, None
for p in sp.primerange(3, 600):
    if int(P13.LC()) % p == 0:
        continue
    flp = sp.factor_list(P13.as_expr(), modulus=p)[1]
    if any(e > 1 for _, e in flp):
        continue
    degs = sorted(sp.Poly(f, r).degree() for f, _ in flp)
    for q in (13, 17, 19):
        if cycle_q is None and degs.count(q) == 1 and all(d % q for d in degs if d != q):
            cycle_q = (p, q, degs)
    if impaire is None and sum(d - 1 for d in degs) % 2:
        impaire = (p, degs)
    if cycle_q and impaire:
        break
ligne(f"\nDimension 13 (degré 24) : irréductible sur Q = {len(fl) == 1 and fl[0][1] == 1} ;"
      f" modulo {cycle_q[0]}, facteurs de degrés {cycle_q[2]} → un {cycle_q[1]}-cycle (Jordan : le groupe contient A₂₄) ;"
      f" modulo {impaire[0]}, degrés {impaire[1]} → permutation impaire ; groupe de Galois = S₂₄")

# ---------------------------------------------------------------------------
# 2. Dimensions paires 2, 6, 12, 24
# ---------------------------------------------------------------------------
ligne("\n## 2. Dimensions paires : κ_n·[π/2 − (2 − rⁿ)·α] = √(4 − r²)·Π_n(r), α = arccos(r/2)\n")
ligne("| n | κ_n = C(2m, m)/4^m | Π_n (degré) | résidu à la corde de la partie I |")
ligne("|---:|---|---|---|")
PAIRS = {}
for n in (2, 6, 12, 24):
    m = n // 2
    kap, pn = kappa_p(m)
    Pi = sp.expand(r ** n / 2 * pn.subs(x, r / 2) + r / 2 * pn.subs(x, 1 - r ** 2 / 2))
    rn = ch.corde_moitie_mp(n)
    residu = mp.mpf(kap.p) / kap.q * (mp.pi / 2 - (2 - rn ** n) * mp.acos(rn / 2)) - mp.sqrt(4 - rn ** 2) * sp.lambdify(r, Pi, "mpmath")(rn)
    PAIRS[n] = (kap, Pi)
    texte_pi = str(Pi).replace("**", "^").replace("*", "·") if n <= 6 else f"degré {sp.Poly(Pi, r).degree()}"
    ligne(f"| {n} | {kap} | {texte_pi} | {mp.nstr(residu, 2)} |")

# ---------------------------------------------------------------------------
# 3. Réciprocité et retenues de la base 2
# ---------------------------------------------------------------------------
ligne("\n## 3. Réciprocité : κ_(2m)·h_(2m+1) = 1/(2m+1)\n")
ligne("| paire ↔ impaire | κ_(2m) | h_(2m+1) | produit |")
ligne("|---|---|---|---|")
for m in (1, 2, 3, 6, 12):
    k = kappa_p(m)[0]
    hh = sp.nsimplify(h(2 * m + 1))
    ligne(f"| {2 * m} ↔ {2 * m + 1} | {k} | {hh} | {k * hh} |")

ligne("\n## 4. Les facteurs 2 comptent les retenues de la base 2 (Kummer)\n")
ligne("| n pair | m = n/2 en binaire | retenues (nombre de 1) | dénominateur de κ_n |")
ligne("|---:|---|---:|---|")
for m in range(1, 17):
    k = kappa_p(m)[0]
    ligne(f"| {2 * m} | {bin(m)[2:]} | {uns(m)} | 2^{v2(k.q)} = 2^({2 * m} − {uns(m)}) |")
ligne("\n| n impair | degré 2(n−1) | (n−1)/2 en binaire | terme constant | dénominateur de κ en dimension 2(n−1) |")
ligne("|---:|---:|---|---|---|")
CONSTANTES = {}
for n in range(3, 32, 2):
    P = polynome_impair(n)
    c0 = P.all_coeffs()[-1]
    impair_part = abs(c0) // 2 ** v2(c0)
    kd = kappa_p(n - 1)[0].q
    CONSTANTES[n] = v2(c0)
    ligne(f"| {n} | {P.degree()} | {bin((n - 1) // 2)[2:]} | {'−' if c0 < 0 else '+'}2^{v2(c0)}"
          f"{'' if impair_part == 1 else f' × {impair_part}'} | 2^{v2(kd)} {'= le même' if abs(c0) == kd else '≠'} |")

# ---------------------------------------------------------------------------
# 5. La preuve : la virgule binaire
# ---------------------------------------------------------------------------
from fractions import Fraction  # noqa: E402
from math import comb, factorial  # noqa: E402


def B(m, k):
    """Coefficient de r^(2(m+1+k)) dans F/h, au signe et à la puissance de 2 près."""
    return Fraction(factorial(2 * m + 1), factorial(m) * factorial(k) * factorial(m - 1 - k) * (2 * k + 1) * (m + k + 1))


def F_sur_h(n):
    m = (n - 1) // 2
    return (r ** n - 1) - sum(sp.Integer(-1) ** k * sp.Rational(B(m, k).numerator, B(m, k).denominator) * r ** (2 * (m + 1 + k))
                              / sp.Integer(2) ** (2 * m + 2 * k + 1) for k in range(m))


def h_frac(n):
    m = (n - 1) // 2
    return Fraction(4 ** m * factorial(m) ** 2, factorial(2 * m + 1))


def periode2(q):
    d = q.denominator
    while d % 2 == 0:
        d //= 2
    if d == 1:
        return 0
    k, x = 1, 2 % d
    while x != 1:
        x, k = x * 2 % d, k + 1
    return k


ligne("\n## 5. La preuve : F/h n'a que des fractions binaires finies\n")
formule_ok = all(sp.expand(sp.expand(F_sur_h(n)) - sp.expand(polynome_impair(n).as_expr() / polynome_impair(n).coeff_monomial(r ** n))) == 0
                 for n in range(3, 32, 2))
ligne(f"- formule fermée F/h = (rⁿ − 1) − Σ (−1)^k B(m,k) r^(2(m+1+k)) / 2^(2m+2k+1) identique au polynôme exact, n = 3 à 31 : {formule_ok}")
cas_ok = all((2 * a + 2 * b + 3) // q - (a + b + 1) // q >= (2 * a + 1 == q) + ((2 * a + b + 2) % q == 0)
             for q in range(3, 302, 2) for a in range(q) for b in range(q))
ligne(f"- étude de cas de Legendre (q impair ≤ 301, toutes les valeurs de α et β) : contribution ≥ 0 partout : {cas_ok}")
entiers = all(B(m, k).denominator == 1 for m in range(1, 401) for k in range(m))
ligne(f"- B(m, k) entier pour m ≤ 400 : {entiers}")
expo_ok = all(-min(0, min(v2(B(m, k).numerator) - (2 * m + 2 * k + 1) for k in range(m))) == 4 * m - uns(m) for m in range(1, 401))
cat_ok = all(B(m, m - 1) == (2 * m + 1) * comb(2 * m - 2, m - 1) // m for m in range(1, 200))
ligne(f"- exposant du terme constant = 4m − (nombre de 1 de m), m ≤ 400 (n ≤ 801) : {expo_ok} ; B(m, m−1) = (2m+1)·Catalan(m−1) : {cat_ok}")
ligne("\n| n | h_n | période binaire de h_n | périodes des coefficients de F | toutes divisent celle de h_n |")
ligne("|---:|---|---:|---|---|")
for n in (3, 5, 7, 9, 13):
    m = (n - 1) // 2
    hn = h_frac(n)
    pers = [periode2(hn)] + [periode2(hn * B(m, k) / 2 ** (2 * m + 2 * k + 1)) for k in range(m)]
    ligne(f"| {n} | {hn} | {periode2(hn)} | {pers} | {all(periode2(hn) % q == 0 for q in pers if q)} |")
SEUIL = next(n for n in range(2, 40) if (ch.corde_moitie_mp(n) - mp.sqrt(mp.mpf(2 * n) / (n + 1))) / ch.corde_moitie_mp(n) < mp.mpf("0.001"))
ligne(f"\n« Cercle de confusion » de 0,1 % : l'écart relatif chèvre / simplexe passe sous 0,1 % dès la dimension {SEUIL}")

with open(os.path.join(ICI, "..", "resultats", "polynomes.md"), "w") as fh:
    fh.write("# Résultats de la partie VII (générés par scripts/polynomes.py)\n\n" + "\n".join(md) + "\n")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, axs = plt.subplots(1, 2, figsize=(15.5, 5.6), gridspec_kw={"wspace": 0.22})
ax = axs[0]
ns = list(range(2, 33, 2))
expo = [v2(kappa_p(n // 2)[0].q) for n in ns]
ax.plot([1, 33], [1, 33], color=F.BASE, lw=1.2)
ax.text(30.5, 31.6, "2ⁿ", fontsize=10, color=F.INK2, ha="right")
ax.vlines(ns, expo, ns, color=F.ORANGE, lw=2.2, alpha=0.8)
ax.plot(ns, expo, "o", color=F.BLEU, ms=6, mec=F.SURF, zorder=5, label="exposant de 2 au dénominateur de κ_n")
for n in (6, 12, 24):
    F.point(ax, n, v2(kappa_p(n // 2)[0].q), F.INK, 9)
    pos = {6: (0.8, 15), 12: (13.2, 2.5), 24: (25.2, 14.5)}[n]
    ax.annotate(f"n = {n} : m = {bin(n // 2)[2:]}\n2 retenues → 2" + str(n - 2).translate(EXP), xy=(n, n - 2), xytext=pos, fontsize=9.5,
                color=F.INK, arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.plot([], [], color=F.ORANGE, lw=2.2, label="écart à n = nombre de retenues de m + m en base 2")
ax.set_xlabel("dimension paire n = 2m")
ax.set_ylabel("exposant de 2")
ax.set_xlim(0, 34)
ax.set_ylim(0, 34)
ax.set_title("a)  Dimensions paires : les facteurs 2 comptent les retenues")
ax.legend(fontsize=9, loc="upper left")
ax = axs[1]
ni = sorted(CONSTANTES)
ax.plot([2, 32], [2 * 2 - 2, 2 * 32 - 2], color=F.BASE, lw=1.2)
ax.text(31, 2 * 31 - 2 + 1.5, "2^(degré)", fontsize=10, color=F.INK2, ha="right")
ax.vlines(ni, [CONSTANTES[n] for n in ni], [2 * n - 2 for n in ni], color=F.ORANGE, lw=2.2, alpha=0.8)
ax.plot(ni, [CONSTANTES[n] for n in ni], "o", color=F.BLEU, ms=6, mec=F.SURF, zorder=5,
        label="exposant de 2 du terme constant du polynôme")
for n, d in ((7, 12), (13, 24)):
    F.point(ax, n, CONSTANTES[n], F.INK, 9)
    pos = {7: (1.5, 31), 13: (14.5, 8)}[n]
    ax.annotate(f"dimension {n} (degré {d}) :\n2" + str(CONSTANTES[n]).translate(EXP) + " = dénominateur de κ" + str(d).translate(IND),
                xy=(n, CONSTANTES[n]), xytext=pos, fontsize=9.5, color=F.INK, arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.plot([], [], color=F.ORANGE, lw=2.2, label="écart au degré = retenues de (n−1)/2 doublé")
ax.set_xlabel("dimension impaire n")
ax.set_ylabel("exposant de 2")
ax.set_title("b)  Dimensions impaires : la même signature binaire")
ax.legend(fontsize=9, loc="upper left")
F.sauver(fig, "g1_polynomes_retenues.png")


# Figure 2 : la virgule binaire comme foyer (dimension 7)
def chiffres(q, n):
    q, out = abs(q) - int(abs(q)), []
    for _ in range(n):
        q *= 2
        out.append(int(q))
        q -= int(q)
    return out


m7, NCH = 3, 26
sup = lambda e: str(e).translate(EXP)
avant = [("h₇ = 16/35 (r⁷ et constante)", h_frac(7))] + [
    (f"coefficient de r{sup(2 * (m7 + 1 + k))}", h_frac(7) * B(m7, k) / 2 ** (2 * m7 + 2 * k + 1)) for k in range(m7)]
apres = [("r⁷ et constante : 1", Fraction(1))] + [
    (f"r{sup(2 * (m7 + 1 + k))} : {B(m7, k)}/2{sup(2 * m7 + 2 * k + 1)}", B(m7, k) / 2 ** (2 * m7 + 2 * k + 1)) for k in range(m7)]
fig, axs = plt.subplots(1, 2, figsize=(15.5, 4.8), gridspec_kw={"wspace": 0.12})
for ax, lignes, titre, couleur in ((axs[0], avant, "a)  L'équation telle quelle : des périodes binaires", F.ORANGE),
                                    (axs[1], apres, "b)  Divisée par h₇ : tout s'arrête avant 10 chiffres", F.BLEU)):
    for i, (nom, q) in enumerate(lignes):
        y = len(lignes) - 1 - i
        if q == 1:
            ds = [0] * NCH
            ax.add_patch(plt.Rectangle((-1, y - 0.38), 0.92, 0.76, fc=couleur, ec=F.SURF))
        else:
            ds = chiffres(q, NCH)
        fin = max([j for j, d_ in enumerate(ds) if d_] or [-1])
        for j, d_ in enumerate(ds):
            fini = periode2(q) == 0 and j > fin
            ax.add_patch(plt.Rectangle((j, y - 0.38), 0.92, 0.76, fc=couleur if d_ else (F.SURF if fini else F.GRID),
                                       ec=F.SURF, lw=0.5, alpha=1 if d_ else 0.9))
        per = periode2(q)
        ax.text(-1.4, y, nom, ha="right", va="center", fontsize=9, color=F.INK)
        ax.text(NCH + 0.4, y, f"période {per}" if per else "finie", va="center", fontsize=9, color=F.INK2)
    ax.axvline(-0.04, color=F.INK, lw=2.2)
    ax.text(-0.04, len(lignes) - 0.05, "virgule", ha="center", va="bottom", fontsize=9.5, color=F.INK, fontweight="bold")
    ax.set_xlim(-9.5, NCH + 4.5)
    ax.set_ylim(-1.3, len(lignes) + 0.35)
    ax.axis("off")
    ax.set_title(titre)
axs[1].axvspan(-0.04, 9.96, color=F.BLEU, alpha=0.07, lw=0)
axs[1].text(11, -0.95, "virgule déplacée de 10 rangs (× 2¹⁰ = 1024) : tout devient entier,\net le terme constant devient 2¹⁰",
            ha="left", va="center", fontsize=9.5, color=F.INK2)
F.sauver(fig, "g2_virgule_binaire.png")
