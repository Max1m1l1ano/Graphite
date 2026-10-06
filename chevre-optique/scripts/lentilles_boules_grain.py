"""
Partie XXIII : relecture. Les lentilles, les boules et le grain grossier des parties précédentes, appliqués aux pas de
10 et à √2.

    python3 scripts/lentilles_boules_grain.py        # ≈ 10 s

Écrit resultats/lentilles_boules_grain.md et figures/x1_lentilles_boules_grain.png.

1. Ce que la partie XXII avait oublié : le développement r_n² = 2n/(n+1) + 2/(3n²) (partie I), l'arête du simplexe
   (parties V, VI, XV) et le plan de la lentille à R/(n+1) (parties I et VI).
2. Le plan de la lentille : une décade de dimension est une décade de longueur.
3. Les décimales en deux couches : r² = 1 + (n − 1)/(n + 1) + μ (partie XVI). La projection répète (10ᵏ − 1)², le
   ménisque commence au chiffre 2k + 1 et y fait une retenue.
4. Les boules et le grain grossier : coquille, équateur, plan et ménisque, quatre taux de change entre le grain et la
   dimension (partie I § 5.2, parties X, XV et XVIII).
5. Le carré de neuf points relu : un seul cran de diaphragme pour toutes les dimensions, la grille décalée A_n.
6. 24D relu : √(48/25) = 4√3/5 et le plan à R/25.
"""

import logging
import math
import os
import sys
from fractions import Fraction

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import betainc, erfinv

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
ROUGE, VIOLET, VERT = "#d0342c", "#7d4fc4", "#1baf7a"
R2 = math.sqrt(2)
md = []


def sci(x):
    """4,55·10⁵ pour les grands nombres, sinon l'écriture courte."""
    if x < 1e4:
        return fr(x, "{:.4g}")
    m = float(f"{x:.3g}")
    e = math.floor(math.log10(m))
    return f"{fr(m / 10 ** e, '{:.3g}')}·10{sup(e)}"


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def sup(n):
    return str(n).translate(SUP)


# ---------------------------------------------------------------------------
# La corde de la chèvre en dimension n (même intégrale radiale que la partie XXII, n réel permis)
# ---------------------------------------------------------------------------
def part_calotte(c, n):
    if c >= 1:
        return 0.0
    if c <= -1:
        return 1.0
    v = betainc(0.5, (n - 1) / 2, c * c)
    return 0.5 * (1 - v) if c >= 0 else 0.5 * (1 + v)


def broute(n, rho2):
    def f(s):
        r = math.exp(-s / n)
        return math.exp(-s) * part_calotte((r * r + 1 - rho2) / (2 * r), n)
    pts = [p for p in ([-n / 2 * math.log(rho2 - 1)] if rho2 > 1 else []) if 0 < p < 60]
    return quad(f, 0, 60, points=pts or None, limit=400, epsabs=1e-15, epsrel=1e-13)[0] + math.exp(-60)


def rho2(n):
    if n == 1:
        return 1.0
    t = brentq(lambda t: broute(n, 2 - 2 * t / n) - 0.5, 0.05, min(5.0, 0.4995 * n), xtol=1e-14)
    return 2 - 2 * t / n


CERTIF = {2: 1.15872847301812151782, 3: 1.22854486373522090345, 24: 1.38593157500109279341}
for n, v in CERTIF.items():
    assert abs(math.sqrt(rho2(n)) - v) < 1e-13
DIMS = [1, 2, 3, 4, 8, 10, 24, 100] + [10 ** k for k in range(3, 8)]
RHO2 = {n: rho2(n) for n in DIMS}
MU = {n: RHO2[n] - 2 * n / (n + 1) for n in DIMS}
X0 = {n: 1 - RHO2[n] / 2 for n in DIMS}
assert all(abs(n * n * MU[n] - 2 / 3) < 0.01 for n in (10 ** 4, 10 ** 5, 10 ** 6))

# ---------------------------------------------------------------------------
# 1. Ce que la partie XXII avait oublié
# ---------------------------------------------------------------------------
ligne("## 1. Ce que la partie XXII avait oublié\n")
ligne("Trois phrases de la partie XXII contredisaient des acquis des parties précédentes :\n")
ligne("| partie XXII | ce qu'on avait posé | où |")
ligne("|---|---|---|")
ligne("| « le terme 8/(3n) est mesuré, pas démontré » | r_n² = 2n/(n + 1) + 2/(3n²) + …, dérivé (esquisse) et vérifié"
      " jusqu'à n = 10 000 : il donne exactement n·(2 − r²) = 2 − 8/(3n) + … | partie I, § 5.4 |")
ligne("| « 2/√3 et ρ₂ : une coïncidence, sans plus » | 2/√3 est l'arête du triangle de hauteur R, le simplexe de la"
      " dimension 2 ; l'arête √(2n/(n + 1)) du simplexe est le terme principal de la corde dans toutes les dimensions,"
      " et l'écart (0,35 % en 2D) est le ménisque. C'est aussi la maille de la grille décalée. En 2D, le rapport"
      " trou/rayon de l'hexagonal tombe sur le même 2/√3 (côté/hauteur du triangle équilatéral) ; en 3D, les deux se"
      " séparent (√2 pour le trou du cubique à faces centrées, √(3/2) pour le simplexe). | parties V, VI, XV |")
ligne("| « l'accord se fait dans les dimensions, pas dans les longueurs » | le plan de la lentille (où se coupent le pré"
      " et la sphère de la corde) est à x₀ ≈ R/(n + 1) du centre : ½, ⅓, ¼… Avec la corde du simplexe, il passe"
      " exactement par son centre de gravité. Une décade de dimension est une décade de longueur. | parties I (§ 5.4)"
      " et VI |")
ligne("\n**Contrôle du développement de la partie I** (n²·μ_n doit tendre vers 2/3, avec μ_n = r_n² − 2n/(n + 1)) :\n")
ligne("| n | " + " | ".join(str(n) if n < 1000 else f"10{sup(round(math.log10(n)))}" for n in DIMS[1:]) + " |")
ligne("|---|" + "---|" * (len(DIMS) - 1))
ligne("| n²·μ_n | " + " | ".join(fr(n * n * MU[n], "{:.4f}") for n in DIMS[1:]) + " |")
ligne("\n(En 10⁷, la double précision ne suffit plus pour μ ; jusqu'à 10⁶ la limite 2/3 est atteinte à 10⁻⁴ près.)")

# ---------------------------------------------------------------------------
# 2. Le plan de la lentille
# ---------------------------------------------------------------------------
ligne("\n## 2. Le plan de la lentille : une décade de dimension, une décade de longueur\n")
ligne("La zone broutée est une lentille (partie I, § 2.1 et § 6.2). Le pré et la sphère de la corde se coupent dans un"
      " plan, à la distance x₀ = R − r²/(2R) du centre. Avec r² = 1 + (n − 1)/(n + 1) + μ (partie XVI), on a exactement"
      " x₀ = 1/(n + 1) − μ/2 (pour R = 1).\n")
ligne("| n | x₀ (plan de la lentille) | 1/(n + 1) (centre de gravité du simplexe) | μ/2 |")
ligne("|---:|---|---|---|")
for n in DIMS:
    nom = str(n) if n < 1000 else f"10{sup(round(math.log10(n)))}"
    ligne(f"| {nom} | {fr(X0[n], '{:.6e}')} | {fr(1 / (n + 1), '{:.6e}')} |"
          f" {fr(MU[n] / 2, '{:.3e}') if n > 1 else '0'} |")
for n in DIMS:
    assert abs(X0[n] - (1 / (n + 1) - MU[n] / 2)) < 1e-12
ligne("\n- **Une décade de dimension est une décade de longueur.** En dimension n = 10ᵏ − 1, le plan de la lentille"
      " est à 10⁻ᵏ R du centre, à μ/2 ≈ 1/(3n²) près. La partie XXII l'avait écrit en aire (2 − r² ≈ 2/n) ; c'est la"
      " même chose en longueur, puisque 2 − r² = 2x₀.")
ligne("- **Le miroir 49-50-51 de la partie XXI est un miroir de plans.** En dimensions 10⁴⁹ − 1, 10⁵⁰ − 1 et 10⁵¹ − 1,"
      " le plan est à 10⁻⁴⁹, 10⁻⁵⁰ et 10⁻⁵¹ R, et x₀·x₀′ = (10⁻⁵⁰)² : la forme de Newton, sur des longueurs.")
ligne("- **√2 arrive exactement quand le plan atteint le centre.** Le plan coupe alors le pré en deux moitiés : c'est"
      " le partage d'aire. C'est la phrase de la partie I (« ce plan glisse vers le centre, et quand il l'atteint, la"
      " corde vaut √2 R »), et c'est la tienne : √2 arrive là où les pas de 10 se précipitent vers la dimension"
      " infinie.")

# ---------------------------------------------------------------------------
# 3. Les décimales en deux couches
# ---------------------------------------------------------------------------
ligne("\n## 3. Les décimales en deux couches\n")
ligne("En dimension n = 10ᵏ, la projection vaut (10ᵏ − 1)/(10ᵏ + 1). Son écriture décimale répète exactement le carré"
      " (10ᵏ − 1)², sur 2k chiffres :\n")
ligne("| k | n | projection (n − 1)/(n + 1) | se répète | ménisque μ | premier chiffre du ménisque |")
ligne("|---:|---:|---|---|---|---:|")
REPET = {}
for k in range(1, 9):
    n = 10 ** k
    rep = str((n - 1) ** 2).zfill(2 * k)
    q = Fraction(n - 1, n + 1)
    chiffres = str(q.numerator * 10 ** (6 * k) // q.denominator).zfill(6 * k)
    assert chiffres == rep * 3
    REPET[k] = rep
    mu_txt = fr(MU[n], "{:.3e}") if n in MU else "≈ 2/(3n²)"
    premier = 2 * k + 1
    if n in MU:
        assert int(-math.floor(math.log10(MU[n]))) == premier
    ligne(f"| {k} | 10{sup(k)} | 0,{rep}{rep}… | {rep} = {'9' * k}² | {mu_txt} | {premier} |")
ligne("\n- **La projection est la couche 1** (partie XIX) : un nombre rationnel, la grille décalée (l'arête du simplexe)."
      " Ses décimales sont les carrés de 9, 99, 999… : 9/11 = 0,(81), 99/101 = 0,(9801), 999/1001 = 0,(998001).")
ligne("- **Le ménisque est la couche 2** : la division d'intégrales complexes (transcendante en dimension paire,"
      " partie I § 5.5). Il vaut ≈ 2/(3n²) et commence exactement au chiffre 2k + 1, juste après le premier carré.")
ligne("- **Il entre par une retenue.** En 100D : 1,9801 9801 98… + 0,0000 6064 85… = 1,9802 5866 83… : le 1 devient 2. En"
      " 1000D : 1,998001 998… + 0,000000 660… = 1,998002 658… Les retenues de la partie XIX sont la frontière exacte"
      " entre les deux couches.")
ADD = {}
for k in (1, 2, 3, 4):
    n = 10 ** k
    proj = 1 + (n - 1) / (n + 1)
    ADD[k] = (proj, MU[n], RHO2[n])
    assert abs(proj + MU[n] - RHO2[n]) < 1e-15

# ---------------------------------------------------------------------------
# 4. Les boules et le grain grossier
# ---------------------------------------------------------------------------
def n_coquille(eps):
    """Dimension où la coquille d'épaisseur eps contient la moitié du volume : 1 − (1 − eps)ⁿ = ½."""
    return math.log(2) / -math.log1p(-eps)


def n_equateur(eps):
    """Dimension où la tranche |x₁| < eps contient la moitié du volume (x₁² suit une loi bêta(½, (n + 1)/2))."""
    return brentq(lambda n: betainc(0.5, (n + 1) / 2, eps * eps) - 0.5, 0.01, 1e12)


def n_menisque(eps):
    """Dimension (réelle) où le ménisque ne déplace plus le plan que de eps : μ_n/2 = eps."""
    return brentq(lambda n: (rho2(n) - 2 * n / (n + 1)) / 2 - eps, 2.0, 2e4)


C_EQ = 2 * erfinv(0.5) ** 2
VERIF = []
for eps in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
    ne = n_equateur(eps)
    nm = n_menisque(eps) if eps <= 1e-3 else float("nan")
    VERIF.append((eps, ne, n_coquille(eps), 1 / eps - 1, nm))
assert abs(betainc(0.5, 5.5, 0.01) - 0.2549) < 1e-3 and abs(betainc(0.5, 50.5, 0.01) - 0.685) < 1e-3
assert abs(1 - 0.9 ** 10 - 0.651) < 1e-3
ligne("\n## 4. Les boules et le grain grossier\n")
ligne("**Ce qu'on avait posé.**")
ligne("- **Partie I, § 5.2.** La coquille d'épaisseur 0,1 R contient 1 − 0,9ⁿ du volume (65 % en 10D) ; la tranche"
      " |x₁| < 0,1 R autour d'un équateur en contient 25 % en 10D, 69 % en 100D et 99,8 % en 1000D (recalculé :"
      f" {fr(100 * betainc(0.5, 5.5, 0.01), '{:.1f}')} %, {fr(100 * betainc(0.5, 50.5, 0.01), '{:.1f}')} %,"
      f" {fr(100 * betainc(0.5, 500.5, 0.01), '{:.1f}')} %).")
ligne("- **Partie I, § 5.3.** La corde est la distance médiane ; |X − P|² ≈ 2 parce que |X| ≈ 1 (la coquille) et"
      " X·P ≈ 0 (l'équateur). La fraction broutée par √2 converge en 1/√n (l'équateur), la corde en 1/n (la"
      " coquille).")
ligne("- **Partie XV.** Comptée sur une grille grossière, la chèvre se confond avec son simplexe ; il faut quelques"
      " milliers de points en 2D pour voir le ménisque.")
ligne("- **Partie XVIII.** Le grain grossier honnête : chaque niveau décimal du grain donne un chiffre certain de la"
      " corde. L'aire converge sous le grain, la longueur jamais (« π = 4 »).")
ligne("- **Partie X.** Sous le flou, un point, un disque et un carré se confondent ; l'écart décroît comme la taille²,"
      " puis taille⁴ quand le carré a le bon côté (√3 fois le rayon).\n")
ligne("**Quatre taux de change entre le grain ε (une longueur, R = 1) et la dimension.** Ce sont les dimensions à partir"
      " desquelles le grain ne distingue plus :\n")
ligne("| grain ε | la sphère de son équateur (tranche \\|x₁\\| < ε : la moitié) | la boule de sa coquille (épaisseur ε :"
      " la moitié) | le plan de la lentille du centre (x₀ < ε) | la chèvre de son simplexe (μ/2 < ε) |")
ligne("|---|---|---|---|---|")
for eps, ne, nc, npl, nm in VERIF:
    ligne(f"| 10⁻{sup(round(-math.log10(eps)))} | {sci(ne)} | {sci(nc)} | 10{sup(round(-math.log10(eps)))} − 1 |"
          f" {fr(nm, '{:.4g}') if not math.isnan(nm) else '—'} |")
ligne(f"| loi | ≈ {fr(C_EQ, '{:.3f}')}/ε² | ≈ ln 2/ε = 0,693/ε | 1/ε − 1 | ≈ 1/√(3ε) = 0,577/√ε |")
ligne(f"| **10⁻⁵⁰** | **≈ {fr(C_EQ, '{:.2f}')}·10¹⁰⁰** | **≈ 0,69·10⁵⁰** | **10⁵⁰** | **≈ 0,58·10²⁵** |")
ligne("\n- **Les puissances et leurs racines.** À un même grain, l'équateur demande ε⁻², la coquille et le plan ε⁻¹, le"
      " ménisque ε^(−1/2). Pour ton 10⁻⁵⁰ : 10¹⁰⁰, 10⁵⁰ et 10²⁵, le carré, le nombre et la racine.")
ligne("- **Ce qu'on voit de la chèvre à un grain donné** (figure, panneau d) : au-dessous de n ≈ 0,58/√ε, le ménisque"
      " (la chèvre diffère de son simplexe) ; entre les deux, le simplexe seul, le plan encore hors du centre ; au-delà"
      " de n ≈ 1/ε, le plan est au centre à un grain près, et la chèvre est la chèvre infinie, √2.")
ligne("- La chèvre suit la coquille, pas l'équateur : sa corde converge en 1/n parce que la médiane ne voit que le"
      " décalage moyen de la coquille (1/n), pas les fluctuations symétriques de l'équateur (1/√n) — l'esquisse de la"
      " partie I.")

# ---------------------------------------------------------------------------
# 5. Le carré de neuf points relu
# ---------------------------------------------------------------------------
CRAN = {n: math.log2(RHO2[n]) for n in DIMS}
ARETE = {n: math.sqrt(2 * n / (n + 1)) for n in DIMS}
ligne("\n## 5. Le carré de neuf points relu\n")
ligne("**Il était déjà là, trois fois.**")
ligne("- **Partie I, § 6.4 : un cran.** « Un cran sépare le cercle tangent aux côtés et le cercle qui passe par les"
      " coins » : les cercles inscrit et circonscrit d'un carré ont des aires dans le rapport 2. Les distances 1 et √2"
      " du carré de neuf points sont un cran de diaphragme.")
ligne("- **Partie X : les centres fantômes.** Des pixels carrés replient les anneaux et font apparaître 8 nouveaux"
      " centres : 4 aux points cardinaux, 4 sur les diagonales. Avec le vrai centre, ce sont les neuf points, créés par"
      " le grain grossier lui-même. Des pixels hexagonaux en donnent 6, sur un hexagone.")
ligne("- **Partie XV : la grille carrée et la grille décalée.** La grille carrée n'offre que 1 et √2 autour du piquet"
      " (14 % et 22 % de la corde) ; la grille décalée d'une demi-maille offre l'arête du simplexe, 2/√3 en 2D, √(3/2) en"
      " 3D (le cubique à faces centrées), √(2n/(n + 1)) en dimension n. C'est le réseau A_n : la grille carrée d'une"
      " dimension de plus, coupée en diagonale.\n")
ligne("**Toutes les dimensions tiennent dans un seul cran.** De la dimension 1 (corde 1) à l'infini (corde √2), l'aire"
      " du disque de la corde passe de 1 à 2 fois celle du pré : exactement un cran. Chaque dimension en parcourt une"
      " part, log₂ r_n² :\n")
ligne("| n | arête du simplexe √(2n/(n + 1)) | corde r_n | ménisque μ_n | part du cran log₂ r_n² |")
ligne("|---:|---|---|---|---|")
for n in DIMS[:8] + [1000, 10 ** 6]:
    nom = str(n) if n < 1000 else f"10{sup(round(math.log10(n)))}"
    ligne(f"| {nom} | {fr(ARETE[n], '{:.6f}')} | {fr(math.sqrt(RHO2[n]), '{:.6f}')} |"
          f" {fr(MU[n], '{:.2e}') if n > 1 else '0'} |"
          f" {fr(CRAN[n], '{:.6f}')} |")
ligne("| ∞ | √2 | √2 | 0 | 1 |")
ligne("\n- La part qui manque au cran vaut ≈ 1/((n + 1)·ln 2) = 1,44/(n + 1) : une décade de dimension divise par 10 ce qui manque au"
      " cran.")
ligne("- Le complément des neuf points se fait donc en deux couches : la grille décalée (l'arête du simplexe, couche 1),"
      " puis le ménisque (la division d'intégrales, couche 2).")

# ---------------------------------------------------------------------------
# 6. 24D relu
# ---------------------------------------------------------------------------
MU24 = CERTIF[24] ** 2 - Fraction(48, 25)
ligne("\n## 6. 24D relu\n")
ligne("- **Le terme principal a le 5² des boulets pour dénominateur** : 2n/(n + 1) = 48/25, donc l'arête du simplexe"
      f" vaut √48/5 = 4√3/5 = {fr(4 * math.sqrt(3) / 5, '{:.10f}')} (partie XXI : 24 + 1 = 5²).")
ligne(f"- La corde certifiée vaut {fr(CERTIF[24], '{:.10f}')} : le ménisque est μ₂₄ = {fr(float(MU24), '{:.3e}')}"
      f" (n²·μ = {fr(576 * float(MU24), '{:.3f}')}, en route vers 2/3).")
ligne(f"- La projection vaut 23/25 ; le plan de la lentille est à 1/25 − μ/2 = {fr(1 / 25 - float(MU24) / 2, '{:.5f}')} R"
      " du centre ; et κ₂₄·h₂₅ = 1/25 aussi (parties VII et XXI). Le même 1/(n + 1) : le centre de gravité du simplexe"
      " d'un côté, la réciprocité de Wallis de l'autre.")
ligne(f"- La 24D a parcouru {fr(CRAN[24], '{:.4f}')} du cran.")

with open(os.path.join(ICI, "..", "resultats", "lentilles_boules_grain.md"), "w") as fh:
    fh.write("# Résultats de la partie XXIII (générés par scripts/lentilles_boules_grain.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure x1
# ===========================================================================
def schema(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)


def legende(ax, texte, y=-0.02):
    ax.text(0.5, y, texte, transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)


fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.2, hspace=0.32)

# a) la relecture
ax = fig.add_subplot(gs[0, 0])
LIGNES = [
    ("✗", ROUGE, "« pas dans les longueurs »", "plan de la lentille à R/(n+1)", "I § 5.4 ; VI"),
    ("✗", ROUGE, "« 2/√3 et ρ₂ : coïncidence »", "simplexe + ménisque", "V ; VI ; XV"),
    ("✗", ROUGE, "« le terme 8/(3n) : mesuré »", "2n/(n+1) + 2/(3n²), dérivé", "I § 5.4"),
    ("✓", VERT, "un 9 par décade de dimension", "r² = 1 + (n−1)/(n+1) + μ", "XVI"),
    ("✓", VERT, "le carré de neuf points", "un cran ; 8 fantômes", "I § 6.4 ; X ; XV"),
    ("✓", VERT, "10⁻⁵⁰ ↔ 2·10⁵⁰", "1 chiffre par décade de grain", "XVIII"),
    ("✓", VERT, "les faisceaux des 2n chèvres", "n + 1 chèvres, un simplexe", "XX"),
    ("+", F.BLEU, "coquille et équateur", "les boules : 1/n et 1/√n", "I § 5.2–5.3"),
]
ax.text(0.02, 0.97, "partie XXII", fontsize=9.6, fontweight="bold", color=F.INK, transform=ax.transAxes)
ax.text(0.45, 0.97, "ce qu'on avait posé", fontsize=9.6, fontweight="bold", color=F.INK, transform=ax.transAxes)
ax.text(0.84, 0.97, "où (partie)", fontsize=9.6, fontweight="bold", color=F.INK, transform=ax.transAxes)
for i, (sym, c, gauche, droite, ou) in enumerate(LIGNES):
    y = 0.88 - 0.112 * i
    ax.add_patch(plt.Rectangle((0.0, y - 0.045), 1.0, 0.09, transform=ax.transAxes, fc=c, alpha=0.07, ec="none"))
    ax.text(0.005, y, sym, fontsize=13, color=c, fontweight="bold", va="center", transform=ax.transAxes)
    ax.text(0.05, y, gauche, fontsize=8.7, color=F.INK, va="center", transform=ax.transAxes)
    ax.text(0.45, y, droite, fontsize=8.7, color=F.INK2, va="center", transform=ax.transAxes)
    ax.text(0.84, y, ou, fontsize=8.4, color=c, va="center", fontweight="bold", transform=ax.transAxes)
schema(ax, (0, 1), (0, 1))
ax.set_title("a)  La relecture : trois corrections, et ce qui tient")
legende(ax, "Rouge : trois phrases de la partie XXII qui contredisaient des acquis. Vert : ce qui tient, avec la partie"
        "\noù c'était déjà posé. Bleu : l'acquis des boules (partie I) qui donne les taux de change du panneau e.")

# b) le plan de la lentille
ax = fig.add_subplot(gs[0, 1])
NS = [n for n in DIMS if n < 10 ** 7]
nn = np.logspace(0, 52, 400)
ax.loglog(nn, 1 / (nn + 1), color=F.MUTED, lw=1.3, ls="--")
ax.loglog(NS, [X0[n] for n in NS], "o", ms=7, color=F.BLEU, mec=F.SURF, zorder=5)
for k in (49, 50, 51):
    ax.loglog([10.0 ** k], [10.0 ** -k], "o", ms=10, color=ROUGE, mec=F.SURF, zorder=6)
ax.annotate("le miroir 49-50-51 :\nplans à 10⁻⁴⁹, 10⁻⁵⁰, 10⁻⁵¹ R\nen dimensions 10⁴⁹, 10⁵⁰, 10⁵¹", (1e49, 1e-49), (1e31, 1e-8),
            fontsize=9, color=ROUGE, fontweight="bold", va="center", arrowprops=dict(arrowstyle="->", color=ROUGE))
ax.text(1e24, 1e-30, "x₀ ≈ 1/(n + 1)", color=F.MUTED, fontsize=9.4, rotation=-34, ha="center", va="center")
ins = ax.inset_axes([0.03, 0.04, 0.42, 0.42])
t = np.linspace(0, 2 * np.pi, 300)
ins.plot(np.cos(t), np.sin(t), color=F.INK, lw=1.0)
r3 = math.sqrt(RHO2[3])
ins.plot(1 + r3 * np.cos(t), r3 * np.sin(t), color=F.ORANGE, lw=1.0)
x0 = X0[3]
yy = math.sqrt(1 - x0 ** 2)
ins.plot([x0, x0], [-yy, yy], color=ROUGE, lw=1.6)
ins.add_patch(Polygon([(1, 0), (0, R2 / math.sqrt(3) * math.sqrt(1.5)), (0, -R2 / math.sqrt(3) * math.sqrt(1.5))],
                      closed=True, fill=False, ec=F.BLEU, lw=1.0, ls=":"))
ins.plot([0], [0], "o", ms=3, color=F.INK)
ins.plot([1], [0], "o", ms=4, color=ROUGE)
ins.text(x0 + 0.05, -0.95, "plan x₀", color=ROUGE, fontsize=7.5)
ins.text(-0.95, 0.85, "3D : x₀ = 0,245\n(1/4 pour le simplexe)", fontsize=7.2, color=F.INK2, va="top")
ins.set_xlim(-1.1, 2.0)
ins.set_ylim(-1.1, 1.1)
ins.set_aspect("equal")
ins.set_xticks([])
ins.set_yticks([])
ins.patch.set_alpha(0.9)
ax.set_xlim(1, 1e53)
ax.set_ylim(1e-53, 2)
ax.set_xticks([1, 1e10, 1e20, 1e30, 1e40, 1e50])
ax.set_xlabel("dimension n")
ax.set_ylabel("x₀ : distance du plan de la lentille au centre (R = 1)")
ax.set_title("b)  Le plan de la lentille suit la dimension")
legende(ax, "Points bleus : le plan calculé, de 1D à 10⁶D. Il suit le centre de gravité du simplexe,"
        "\n1/(n + 1) (parties I et VI). En dimension 10ᵏ, il est à 10⁻ᵏ R du centre : le miroir"
        "\n49-50-51 de la partie XXI est un miroir de plans, et √2 arrive quand le plan atteint"
        "\nle centre et coupe le pré en deux moitiés. Encart : la coupe 3D.", y=-0.13)

# c) les deux couches des décimales
ax = fig.add_subplot(gs[0, 2])
y = 0.95
for k in (1, 2, 3, 4):
    proj, mu, r2_ = ADD[k]
    nd = 2 * k + 5
    q = Fraction(10 ** k - 1, 10 ** k + 1)
    p_int = (q.numerator * 10 ** nd) // q.denominator
    r_int = int(r2_ * 10 ** nd) - 10 ** nd
    m_int = r_int - p_int
    assert abs(m_int - int(mu * 10 ** nd)) <= 1
    ps = "1," + str(p_int).zfill(nd)
    ms_ = "0," + str(m_int).zfill(nd)
    rs = "1," + str(r_int).zfill(nd)
    ax.text(0.0, y, f"n = 10{sup(k)}", fontsize=10, fontweight="bold", transform=ax.transAxes, va="center")
    y -= 0.052
    x_ = 0.3
    for etiquette, s_, c in (("projection", ps, F.BLEU), ("+ ménisque", ms_, F.ORANGE), ("= r²", rs, F.INK)):
        ax.text(x_ - 0.03, y, etiquette, fontsize=8.6, color=c, ha="right", transform=ax.transAxes, va="center")
        for j, ch in enumerate(s_):
            cc = c
            if etiquette == "= r²" and j >= 2:
                pos = j - 1
                cc = ROUGE if pos == 2 * k else (F.BLEU if pos < 2 * k else F.ORANGE)
            ax.text(x_ + 0.04 * j, y, ch, fontsize=10.5, family="DejaVu Sans Mono", color=cc, transform=ax.transAxes,
                    va="center", fontweight="bold" if etiquette == "= r²" else "normal")
        y -= 0.05
    ax.plot([0.3, 0.3 + 0.04 * (nd + 2)], [y + 0.075, y + 0.075], transform=ax.transAxes, color=F.BASE, lw=0.8)
    y -= 0.025
ax.text(0.0, 0.0, "rouge : la retenue du ménisque, au chiffre 2k (9801 → 9802, 998001 → 998002)", fontsize=8.6,
        color=ROUGE, transform=ax.transAxes)
schema(ax, (0, 1), (0, 1))
ax.set_title("c)  Les décimales en deux couches")
legende(ax, "r² = 1 + (n − 1)/(n + 1) + μ (partie XVI). En dimension 10ᵏ, la projection répète le"
        "\ncarré (10ᵏ − 1)² : 0,(81), 0,(9801), 0,(998001)… C'est la couche 1, la grille décalée."
        "\nLe ménisque, la division d'intégrales, commence au chiffre 2k + 1 et entre par une"
        "\nretenue (partie XIX) : c'est la couche 2.")

# d) ce qu'on voit de la chèvre à un grain donné
ax = fig.add_subplot(gs[1, 0])
n_ = np.logspace(0.3, 30, 400)
plan = 1 / (n_ + 1)
N_DENSE = np.unique(np.round(np.logspace(np.log10(2), 3, 40), 3))
MU_DENSE = np.array([(rho2(float(m)) - 2 * m / (m + 1)) / 2 for m in N_DENSE])
men = np.where(n_ > 1e3, 1 / (3 * n_ ** 2), np.exp(np.interp(np.log(n_), np.log(N_DENSE), np.log(MU_DENSE))))
ax.fill_between(n_, 1e-62, men, color=F.ORANGE, alpha=0.18, lw=0)
ax.fill_between(n_, men, plan, color=F.BLEU, alpha=0.12, lw=0)
ax.fill_between(n_, plan, 1, color=VIOLET, alpha=0.10, lw=0)
ax.loglog(n_, plan, color=F.BLEU, lw=2.0)
ax.loglog(n_, men, color=F.ORANGE, lw=2.0)
ax.axhline(1e-50, color=ROUGE, lw=1.4, ls="--")
ax.plot([0.577e25], [1e-50], "o", ms=9, color=F.ORANGE, mec=F.SURF, zorder=6)
ax.text(1.2, 1e-50 * 3, "grain 10⁻⁵⁰", color=ROUGE, fontsize=9, fontweight="bold", va="bottom")
ax.text(3, 1e-28, "le grain voit le ménisque :\nla chèvre ≠ son simplexe", color=F.ORANGE, fontsize=9.2, fontweight="bold")
ax.text(3e10, 1e-15, "le grain voit le plan,\npas le ménisque :\nla chèvre = son simplexe", color=F.BLEU, fontsize=9.2,
        fontweight="bold")
ax.text(1e18, 1e-5, "le plan est au centre à un grain\nprès : la chèvre infinie, √2", color=VIOLET, fontsize=9.2,
        fontweight="bold")
ax.annotate("n ≈ 0,58·10²⁵", (0.577e25, 1e-50), (1e22, 1e-56), fontsize=8.8, color=F.ORANGE, ha="center",
            arrowprops=dict(arrowstyle="-", color=F.ORANGE, lw=0.8))
ax.text(1e28, 3e-50, "→ 10⁵⁰", color=F.BLEU, fontsize=8.8, ha="center", va="bottom")
ax.set_xlim(2, 1e30)
ax.set_ylim(1e-60, 1)
ax.set_xlabel("dimension n")
ax.set_ylabel("grain ε (une longueur, R = 1)")
ax.set_title("d)  Le grain grossier : ce qu'on voit de la chèvre")
legende(ax, "Bleu : le plan de la lentille, x₀ ≈ 1/(n + 1). Orange : son déplacement dû au"
        "\nménisque, μ/2 ≈ 1/(3n²). Un grain plus gros que le ménisque confond la chèvre avec"
        "\nson simplexe (partie XV) ; plus gros que x₀, avec la chèvre infinie. Au grain 10⁻⁵⁰ :"
        "\nle ménisque disparaît dès 0,58·10²⁵, le plan dès 10⁵⁰.", y=-0.13)

# e) quatre taux de change
ax = fig.add_subplot(gs[1, 1])
kk = np.linspace(1, 60, 200)
for pente, cste, c, nom in ((2, C_EQ, VIOLET, "la sphère = son équateur : ≈ 0,455/ε²"),
                            (1, math.log(2), F.AQUA, "la boule = sa coquille : ≈ 0,693/ε"),
                            (1, 1.0, F.BLEU, "le plan au centre : 1/ε"),
                            (0.5, 1 / math.sqrt(3), F.ORANGE, "la chèvre = son simplexe : ≈ 0,577/√ε")):
    ax.plot(kk, pente * kk + math.log10(cste), color=c, lw=2.2 if c != F.AQUA else 1.6,
            ls="-" if c != F.AQUA else "--", label=nom)
for eps, ne, nc, npl, nm in VERIF:
    k = -math.log10(eps)
    ax.plot([k], [math.log10(ne)], "o", ms=6, color=VIOLET, mec=F.SURF, zorder=6)
    ax.plot([k], [math.log10(nc)], "o", ms=6, color=F.AQUA, mec=F.SURF, zorder=6)
    if not math.isnan(nm):
        ax.plot([k], [math.log10(nm)], "o", ms=6, color=F.ORANGE, mec=F.SURF, zorder=6)
ax.axvline(50, color=ROUGE, lw=1.2, ls="--")
for v, c in ((100 + math.log10(C_EQ), VIOLET), (50, F.BLEU), (25 + math.log10(1 / math.sqrt(3)), F.ORANGE)):
    ax.plot([50], [v], "s", ms=9, color=c, mec=F.SURF, zorder=7)
ax.text(51, 100, "10¹⁰⁰", color=VIOLET, fontsize=10, fontweight="bold", va="center")
ax.text(51, 52, "10⁵⁰", color=F.BLEU, fontsize=10, fontweight="bold", va="center")
ax.text(51, 26, "10²⁵", color=F.ORANGE, fontsize=10, fontweight="bold", va="center")
ax.text(49, 112, "grain 10⁻⁵⁰", color=ROUGE, fontsize=9, ha="right", fontweight="bold")
ax.set_xlim(0, 62)
ax.set_ylim(-2, 122)
ax.set_xlabel("grain ε = 10⁻ᵏ : k")
ax.set_ylabel("log₁₀ de la dimension où le grain ne distingue plus")
ax.legend(loc="upper left", fontsize=8.5, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("e)  Les boules : quatre taux de change")
legende(ax, "Pentes 2, 1 et ½ : le carré, le nombre et la racine. Points : les valeurs exactes"
        "\nde 10⁻¹ à 10⁻⁶ (loi bêta pour l'équateur, 1 − (1 − ε)ⁿ pour la coquille, la corde"
        "\ncalculée pour le ménisque). La chèvre suit la coquille (1/n), pas l'équateur (1/√n) :"
        "\nsa médiane ne voit que le décalage moyen (partie I).", y=-0.13)

# f) un seul cran pour toutes les dimensions
ax = fig.add_subplot(gs[1, 2])
nc_ = np.logspace(0, 7, 300)
ax.semilogx(nc_, np.log2(2 * nc_ / (nc_ + 1)), color=F.BLEU, lw=1.6, ls="--", label="arête du simplexe² : 2n/(n + 1)"
            " (couche 1)")
NSC = [n for n in DIMS if n < 10 ** 7]
ax.semilogx(NSC, [CRAN[n] for n in NSC], "o-", color=F.ORANGE, ms=6, lw=1.4,
            label="corde² r_n² = simplexe + ménisque (couche 2)")
ax.axhline(1, color=ROUGE, lw=1.4)
ax.axhline(0, color=F.INK2, lw=1.0)
ax.text(1.1, 1.02, "√2 : un cran entier (les coins du carré)", color=ROUGE, fontsize=9, va="bottom")
ax.text(1.1, -0.03, "1 : les milieux du carré (dimension 1)", color=F.INK2, fontsize=9, va="top")
for n, nom in ((2, "2D : 0,425"), (3, "3D : 0,594"), (24, "24D : 0,942"), (100, "100D : 0,986")):
    ax.annotate(nom, (n, CRAN[n]), (n * 2.2, CRAN[n] - 0.1), fontsize=8.8, color=F.ORANGE, fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=F.ORANGE, lw=0.7))
ax.set_ylim(-0.12, 1.12)
ax.set_xlim(0.8, 2e7)
ax.set_xlabel("dimension n")
ax.set_ylabel("part du cran parcourue : log₂ r_n²")
ax.legend(loc="center right", fontsize=8.4, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("f)  Un seul cran pour toutes les dimensions")
legende(ax, "De la dimension 1 à l'infini, l'aire du disque de la corde double exactement : un"
        "\ncran (partie I, § 6.4 : le cran sépare les cercles inscrit et circonscrit d'un carré)."
        "\nLa grille décalée (tirets) en fait presque tout ; le ménisque comble le reste. Ce qui"
        "\nmanque au cran est divisé par 10 à chaque décade de dimension.", y=-0.13)
F.sauver(fig, "x1_lentilles_boules_grain.png")
