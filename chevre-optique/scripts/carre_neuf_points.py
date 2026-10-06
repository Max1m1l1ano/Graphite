"""
Partie XXII : le carré de neuf points. √2 là où les pas de 10 se précipitent, les chèvres de 1 à √2, et 24 pour la
sphère 24D.

    python3 scripts/carre_neuf_points.py        # ≈ 15 s

Écrit resultats/carre_neuf_points.md et figures/w1_carre_neuf_points.png.

1. Les pas de 10 se précipitent vers √2 : la corde ρ_n de la chèvre de dimension n, calculée jusqu'à n = 10⁸ par une
   intégrale radiale exacte. Chaque facteur 10 sur la dimension ajoute un 9 à ρ² ; 2 − ρ² ≈ 2/n ; le doublement de
   l'aire (ρ² = 2) n'arrive qu'à l'infini, et 10⁻⁵⁰ y correspond à la dimension 2·10⁵⁰.
2. Le carré de neuf points (sommets, milieux, centre) : les distances 1 et √2, que les cordes de toutes les dimensions
   remplissent ; les 3ⁿ points du cube ; 3ⁿ modulo 10.
3. Les faisceaux : 2n chèvres aux milieux (±e_i) recouvrent la clôture S^(n−1), et leur nerf est le bord du polytope
   croisé, en toute dimension finie ; à l'infini, le recouvrement cesse d'être bon.
4. 24 pour la sphère 24D : la chèvre 24D et ses 48 piquets, le réseau de Leech (rayon 1, trou √2), et le rapport √2
   des meilleurs empilements en 3, 8 et 24.
"""

import itertools
import logging
import math
import os
import sys
from math import comb

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.patches import Polygon
from numpy.random import default_rng
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import betainc

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
ROUGE, VIOLET = "#d0342c", "#7d4fc4"
R2 = math.sqrt(2)
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def sup(n):
    return str(n).translate(SUP)


# ---------------------------------------------------------------------------
# 1. La corde de la chèvre, de la dimension 1 à 10⁸
# ---------------------------------------------------------------------------
def part_calotte(c, n):
    """P(U₁ ≥ c) pour U uniforme sur la sphère S^(n−1) (U₁² suit une loi bêta(½, (n − 1)/2))."""
    if c >= 1:
        return 0.0
    if c <= -1:
        return 1.0
    v = betainc(0.5, (n - 1) / 2, c * c)
    return 0.5 * (1 - v) if c >= 0 else 0.5 * (1 + v)


def broute(n, rho2):
    """Part de la boule unité de dimension n à distance ≤ ρ du piquet e₁ (|X| = r, avec rⁿ = e^(−s))."""
    def f(s):
        r = math.exp(-s / n)
        return math.exp(-s) * part_calotte((r * r + 1 - rho2) / (2 * r), n)
    pts = [-n / 2 * math.log(rho2 - 1)] if rho2 > 1 else []
    pts = [p for p in pts if 0 < p < 60]
    return quad(f, 0, 60, points=pts or None, limit=400, epsabs=1e-15, epsrel=1e-13)[0] + math.exp(-60)


def t_n(n):
    """t_n = n·(2 − ρ_n²)/2 : la corde vérifie ρ_n² = 2 − 2·t_n/n."""
    return brentq(lambda t: broute(n, 2 - 2 * t / n) - 0.5, 0.05, min(5.0, 0.4995 * n), xtol=1e-14)


def corde(n):
    return 1.0 if n == 1 else math.sqrt(2 - 2 * t_n(n) / n)


CERTIF = {2: 1.15872847301812151782, 3: 1.22854486373522090345, 4: 1.26807925667341823348,
          8: 1.33486242915790962010, 24: 1.38593157500109279341}
RHO = {n: corde(n) for n in list(range(1, 31)) + [100]}
for n, v in CERTIF.items():
    assert abs(RHO[n] - v) < 1e-13, (n, RHO[n], v)
DEC = {k: t_n(10 ** k) for k in range(1, 9)}
RHO2_DEC = {k: 2 - 2 * DEC[k] / 10 ** k for k in DEC}
FIT = {k: 10 ** k * (DEC[k] - 1) for k in (4, 5, 6)}
assert all(abs(v + 4 / 3) < 2e-3 for v in FIT.values())
ALPHA = {n: math.degrees(2 * math.asin(RHO[n] / 2)) for n in RHO}

ligne("## 1. Les pas de 10 se précipitent vers √2\n")
ligne("La corde ρ_n est calculée pour toute dimension par une intégrale exacte sur le rayon : un point X de la boule"
      " s'écrit X = r·U, avec rⁿ uniforme et U uniforme sur la sphère, et la chèvre broute X quand"
      " U₁ ≥ (r² + 1 − ρ²)/(2r). Contrôle : on retrouve les cordes certifiées de la partie XX (dimensions 2, 3, 4, 8"
      " et 24) à 10⁻¹³ près.\n")
ligne("| n | ρ_n | ρ_n² (aire du disque de la corde / aire du pré) | 2 − ρ_n² | n·(2 − ρ_n²) | α_n |")
ligne("|---:|---|---|---|---|---|")
for n in (1, 2, 3, 4, 8, 10, 24, 100):
    r = RHO.get(n) or math.sqrt(RHO2_DEC[1])
    ligne(f"| {n} | {fr(r, '{:.10f}')} | {fr(r * r, '{:.10f}')} | {fr(2 - r * r, '{:.3e}')} |"
          f" {fr(n * (2 - r * r), '{:.6f}')} | {fr(math.degrees(2 * math.asin(r / 2)), '{:.4f}')}° |")
ligne("\n**Les décades de dimension.**\n")
ligne("| n | ρ_n² | 2 − ρ_n² | n·(2 − ρ_n²) |")
ligne("|---:|---|---|---|")
for k, r2_ in [(k, v) for k, v in RHO2_DEC.items() if k <= 7]:
    ligne(f"| 10{sup(k)} | {fr(r2_, '{:.15f}')} | {fr(2 - r2_, '{:.4e}')} | {fr(2 * DEC[k], '{:.10f}')} |")
ligne("\n(En 10⁸, ρ² = 1,99999998 ; le terme suivant n'est plus lisible en double précision.)\n")
ligne("- Chaque facteur 10 sur la dimension ajoute un 9 (et un 0) à ρ² : 1,82…, 1,980…, 1,998 0…, 1,999 800 0…,"
      " 1,999 980 000 3… Les décades de dimension sont les décimales de l'approche de 2.")
ligne(f"- n·(2 − ρ_n²) → 2 (partie XX), et le calcul donne n·(2 − ρ_n²) = 2 − 8/(3n) + … (n·(t_n − 1) vaut"
      f" {fr(FIT[4], '{:.5f}')}, {fr(FIT[5], '{:.5f}')}, {fr(FIT[6], '{:.5f}')} en 10⁴, 10⁵, 10⁶ ; −4/3 = −1,33333)."
      " Donc 2 − ρ_n² ≈ 2/n.")
ligne("- ρ² est le rapport entre l'aire du disque de la corde et celle du pré (dans le plan méridien, la projection"
      " de la partie XX). Le doublement de l'aire, ρ² = 2, n'arrive qu'en dimension infinie.")
ligne("- Les trois cercles de rayons 1/√2 (la moitié du pré), 1 (le pré) et √2 (la corde infinie) ont des aires ½, 1"
      " et 2 : trois diaphragmes de suite.")
ligne("- **Ton 10⁻⁵⁰ y a une place précise.** 2 − ρ_n² = 10⁻⁵⁰ en n ≈ 2·10⁵⁰ ; de même 10⁻⁴⁹ en 2·10⁴⁹ et 10⁻⁵¹ en"
      " 2·10⁵¹ (correction relative 4/(3n), négligeable). Le miroir 49-50-51 de la partie XXI est une échelle de"
      " dimensions : chaque cran de 10 sur la précision est un cran de 10 sur la dimension.")
ligne("- Ce qui reste vrai : sur une longueur physique (10⁻⁵⁰ m → 10⁻⁵¹ m), un cran de 10 multiplie l'aire par 100."
      " L'accord entre le pas de 10 et le pas de √2 se fait dans les dimensions et dans les chiffres, pas dans les"
      " longueurs.")

# ---------------------------------------------------------------------------
# 2. Le carré de neuf points
# ---------------------------------------------------------------------------
NEUF = [(x, y) for y in (1, 0, -1) for x in (-1, 0, 1)]
PIQUET = (1, 0)
DIST = {}
for p in NEUF:
    if p != PIQUET:
        DIST.setdefault(round(math.dist(p, PIQUET) ** 2), []).append(p)
assert sorted(DIST) == [1, 2, 4, 5] and len(DIST[1]) == 3 and len(DIST[2]) == 2
ligne("\n## 2. Le carré de neuf points\n")
ligne("Le carré [−1, 1]² : quatre sommets (±1, ±1), quatre milieux d'arêtes (±1, 0), (0, ±1), et le centre. Vu du"
      " centre : 0, 1 (les milieux) et √2 (les sommets). Le pré est le cercle inscrit, de rayon 1 ; le piquet est le"
      " milieu (1, 0).\n")
ligne("| distance au piquet (1, 0) | points |")
ligne("|---|---|")
for d2, pts in sorted(DIST.items()):
    nom = {1: "1", 2: "√2", 4: "2", 5: "√5"}[d2]
    ligne(f"| {nom} | {', '.join(f'({x}, {y})' for x, y in pts)} |".replace("-", "−"))
ligne("\n**Les chèvres remplissent l'écart entre 1 et √2.** Le carré ne donne que deux distances autour du piquet, 1 et"
      " √2. Les cordes de toutes les dimensions remplissent l'intervalle entre les deux :")
ligne("- n = 1 : ρ₁ = 1 exactement. La chèvre de la droite (le pré est le diamètre [−1, 1]) broute la moitié en"
      " allant jusqu'au centre ; son cercle passe par le centre et par les deux coins (1, ±1).")
ligne(f"- n = 2 : ρ₂ = {fr(RHO[2], '{:.10f}')}…, la division d'intégrales complexes d'Ullisch ;"
      f" n = 3 : {fr(RHO[3], '{:.10f}')}… ;"
      f" n = 24 : {fr(RHO[24], '{:.10f}')}…")
ligne("- n → ∞ : ρ → √2. La corde atteint les deux milieux voisins (0, ±1) : le croisement.")
ligne("- Les cordes croissent avec la dimension (vérifié de 1 à 30, puis 100 et les décades jusqu'à 10⁸).")
assert all(RHO[a] < RHO[a + 1] for a in range(1, 30)) and RHO[30] < RHO[100] < R2
FACES = {n: [comb(n, k) * 2 ** k for k in range(n + 1)] for n in range(1, 9)}
assert all(sum(v) == 3 ** n for n, v in FACES.items())
ligne("\n**Les 3ⁿ points du cube.** En dimension n, les points à coordonnées dans {−1, 0, 1} sont les centres des faces"
      " du cube (le cube lui-même compris) : 3ⁿ points, dont C(n, k)·2ᵏ à la distance √k du centre.\n")
ligne("| n | distances 0, 1, √2, √3… | total 3ⁿ | 3ⁿ modulo 10 |")
ligne("|---:|---|---:|---|")
TOUR = {3: "3 = i", 9: "9 = −1", 7: "7 = −i", 1: "1"}
for n, v in FACES.items():
    ligne(f"| {n} | {', '.join(map(str, v))} | {3 ** n} | {TOUR[pow(3, n, 10)]} |")
assert [pow(3, n, 10) for n in range(1, 9)] == [3, 9, 7, 1] * 2
ligne("\n- Le carré de neuf points est la ligne n = 2 : 1 centre, 4 milieux, 4 sommets.")
ligne("- 3 est i modulo 10 (partie XIX) : 3² = 9 ≡ −1. Chaque dimension multiplie le nombre de points par 3, donc les"
      " fait tourner d'un quart de tour modulo 10 : 3, 9, 7, 1.")
ligne("- Comme empilement : des sphères de rayon 1 centrées aux sommets se touchent aux milieux des arêtes, et le"
      " centre est le trou le plus profond, à √2. Le rapport entre le trou et le rayon vaut √2 (§ 4).")
ligne("- Les quatre petits carrés ont leurs centres (±½, ±½) sur le cercle de rayon 1/√2, celui de la moitié du pré.")

# ---------------------------------------------------------------------------
# 3. Les faisceaux
# ---------------------------------------------------------------------------
P_MOD = 1_000_003


def rang_mod(M):
    M = [row[:] for row in M]
    r = 0
    for c in range(len(M[0]) if M else 0):
        piv = next((i for i in range(r, len(M)) if M[i][c] % P_MOD), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], P_MOD - 2, P_MOD)
        M[r] = [(x * inv) % P_MOD for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % P_MOD:
                f_ = M[i][c]
                M[i] = [(a - f_ * b) % P_MOD for a, b in zip(M[i], M[r])]
        r += 1
    return r


def betti(faces, maxd):
    idx = {d: {f_: i for i, f_ in enumerate(faces.get(d, []))} for d in range(maxd + 2)}
    rg = {}
    for d in range(1, maxd + 1):
        lignes_, cols = faces.get(d - 1, []), faces.get(d, [])
        M = [[0] * len(cols) for _ in lignes_]
        for j, f_ in enumerate(cols):
            for k in range(len(f_)):
                M[idx[d - 1][f_[:k] + f_[k + 1:]]][j] = (-1) ** k % P_MOD
        rg[d] = rang_mod(M) if lignes_ and cols else 0
    return [len(faces.get(d, [])) - rg.get(d, 0) - rg.get(d + 1, 0) for d in range(maxd + 1)]


def nerf_croise(n):
    axe = [i for i in range(n) for _ in (1, -1)]
    faces = {}
    for k in range(1, n + 1):
        for S in itertools.combinations(range(2 * n), k):
            if len({axe[v] for v in S}) == k:
                faces.setdefault(k - 1, []).append(S)
    return faces


NERFS = {n: nerf_croise(n) for n in range(2, 6)}
BETTI = {n: betti(f_, n - 1) for n, f_ in NERFS.items()}
for n, b in BETTI.items():
    assert b == [1] + [0] * (n - 2) + [1] and [len(NERFS[n][d]) for d in range(n)] == [comb(n, k + 1) * 2 ** (k + 1)
                                                                                         for k in range(n)]
ARCS = {"E": (-90, 90), "N": (0, 180), "O": (90, 270), "S": (180, 360)}


def sur_arc(a, arc):
    return any(arc[0] <= a + k * 360 <= arc[1] for k in (-1, 0, 1))


GRILLE = [x / 4 for x in range(360 * 4)]
NOMS = list(ARCS)
NERF_INF = {}
for k in range(1, 5):
    for S in itertools.combinations(range(4), k):
        if any(all(sur_arc(a, ARCS[NOMS[i]]) for i in S) for a in GRILLE):
            NERF_INF.setdefault(k - 1, []).append(S)
BETTI_INF = betti(NERF_INF, 3)
EO = [a for a in GRILLE if sur_arc(a, ARCS["E"]) and sur_arc(a, ARCS["O"])]
assert BETTI_INF == [1, 0, 1, 0] and EO == [90.0, 270.0]
SEUIL = {n: math.degrees(math.acos(1 / math.sqrt(n))) for n in RHO if n >= 2}
assert all(SEUIL[n] < ALPHA[n] < 90 for n in SEUIL)
ALPHA_DEC = {k: math.degrees(2 * math.asin(math.sqrt(RHO2_DEC[k]) / 2)) for k in RHO2_DEC}
assert all(math.degrees(math.acos(1 / math.sqrt(10 ** k))) < a < 90 for k, a in ALPHA_DEC.items())
rng = default_rng(22)
MULT = {}
for n in (2, 3, 4, 8, 24, 100):
    X = rng.standard_normal((200000, n))
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    m = (np.abs(X) >= math.cos(math.radians(ALPHA[n]))).sum(axis=1)
    assert m.min() >= 1 and m.max() <= n
    MULT[n] = (int(m.min()), int(m.max()), float(m.mean()))

ligne("\n## 3. Les faisceaux\n")
ligne("**En 2D.** Quatre chèvres, une à chaque milieu. Chacune broute sur la clôture un arc de ±α₂ = ±70,81° autour de"
      " son piquet. Comme 70,81° > 45°, les quatre arcs couvrent le cercle. Les arcs voisins se recouvrent autour des"
      " directions des sommets ; les arcs opposés ne se touchent jamais. Le nerf (qui recouvre qui) est un carré, un"
      " cycle de 4 : il calcule la cohomologie du cercle (H⁰ = H¹ = ℤ).\n")
ligne("**En dimension n.** 2n chèvres aux ±e_i, les sommets du polytope croisé (les milieux des faces du cube). C'est un"
      " bon recouvrement de la clôture S^(n−1) dès que arccos(1/√n) < α_n < 90° :")
ligne("- si α_n > arccos(1/√n), un groupe de chèvres sans paire opposée a toujours un point commun, au besoin dans la"
      " direction d'un sommet du cube ;")
ligne("- si α_n < 90°, deux chèvres opposées ne se touchent pas ;")
ligne("- les calottes de moins de 90° sont convexes, donc leurs intersections sont contractiles.\n")
ligne("| n | α_n | seuil arccos(1/√n) | chèvres | nerf : sommets, arêtes, triangles… | nombres de Betti |")
ligne("|---:|---|---|---:|---|---|")
for n in (2, 3, 4, 5):
    fv = ", ".join(str(len(NERFS[n][d])) for d in range(n))
    ligne(f"| {n} | {fr(ALPHA[n], '{:.2f}')}° | {fr(SEUIL[n], '{:.2f}')}° | {2 * n} | {fv} |"
          f" {', '.join(map(str, BETTI[n]))} |")
for n in (8, 24, 100):
    ligne(f"| {n} | {fr(ALPHA[n], '{:.2f}')}° | {fr(SEUIL[n], '{:.2f}')}° | {2 * n} | C(n, k)·2ᵏ | sphère"
          f" S{sup(n - 1)} |")
ligne("\n- Le nerf est le bord du polytope croisé, une sphère S^(n−1) : la condition est vérifiée pour toutes les"
      " dimensions calculées (2 à 30, 100, et les décades jusqu'à 10⁸), car 90° − α_n ≈ 1/(n + 1) radian alors que"
      " 90° − arccos(1/√n) ≈ 1/√n.")
ligne("- Les nombres de Betti sont vérifiés de 2 à 5 (rang des bords modulo un nombre premier) : 1, 0, …, 0, 1, ceux"
      " de la sphère.")
ligne("- **Les sommets du cube sont les endroits où n chèvres se recouvrent** : dans la direction (±1, …, ±1)/√n, les n"
      " chèvres d'un même signe broutent ensemble. Sur un piquet, une seule.\n")
ligne("| n | chèvres | au moins (sur un piquet) | au plus (vers un sommet du cube) | en moyenne (2·10⁵ points"
      " au hasard) | le moins brouté des points tirés |")
ligne("|---:|---:|---:|---:|---|---:|")
for n, (mn, mx, moy) in MULT.items():
    ligne(f"| {n} | {2 * n} | 1 | {n} | {fr(moy, '{:.2f}')} | {mn} |")
ligne("\n- En grande dimension, un point au hasard est loin des piquets : en 24D, aucun des 200 000 points tirés n'est"
      " brouté par moins de 12 chèvres.")
ligne("\n**À l'infini, le recouvrement cesse d'être bon.** En α = 90°, les arcs sont des demi-cercles fermés et les"
      f" chèvres opposées se touchent : en 2D, Est et Ouest se rencontrent en {fr(EO[0], '{:g}')}° et"
      f" {fr(EO[1], '{:g}')}°, deux points séparés. Le nerf devient le bord d'un tétraèdre, de nombres de Betti"
      f" {', '.join(map(str, BETTI_INF))} : une sphère S² au lieu du cercle. Le croisement est exactement l'endroit où"
      " le calcul des faisceaux casse.")

# ---------------------------------------------------------------------------
# 4. 24 pour la sphère 24D
# ---------------------------------------------------------------------------
def dec_D(x):
    f_ = np.round(x)
    impair = f_.sum(axis=-1) % 2 != 0
    if np.any(impair):
        xb, fb = x[impair], f_[impair].copy()
        err = xb - fb
        k = np.argmax(np.abs(err), axis=1)
        lig = np.arange(len(xb))
        fb[lig, k] += np.where(err[lig, k] > 0, 1, -1)
        f_[impair] = fb
    return f_


def dec_E8(x):
    a_, b_ = dec_D(x), dec_D(x - 0.5) + 0.5
    return np.where((((x - a_) ** 2).sum(axis=1) <= ((x - b_) ** 2).sum(axis=1))[:, None], a_, b_)


def distance(x, dec):
    return np.sqrt(((x - dec(x)) ** 2).sum(axis=1))


def recouvrement(n, dec):
    """Le plus grand écart au réseau trouvé par tirage puis montée locale (une borne inférieure)."""
    X = rng.uniform(-2, 2, size=(200000, n))
    meilleurs = X[np.argsort(-distance(X, dec))[:150]]
    for it in range(300):
        Y = meilleurs + rng.normal(scale=0.02 * 0.99 ** it, size=meilleurs.shape)
        meilleurs = np.where((distance(Y, dec) > distance(meilleurs, dec))[:, None], Y, meilleurs)
    return float(distance(meilleurs, dec).max())


RESEAUX = []
for nom, n, dec, emp, trou in (("ℤ² (le carré de neuf points)", 2, np.round, 0.5, [0.5, 0.5]),
                                ("D₃ = cubique à faces centrées (record en 3D)", 3, dec_D, R2 / 2, [1, 0, 0]),
                                ("D₄", 4, dec_D, R2 / 2, [1, 0, 0, 0]),
                                ("E₈ (record en 8D)", 8, dec_E8, R2 / 2, [1] + [0] * 7)):
    rt = float(distance(np.array([trou], float), dec)[0])
    mc = recouvrement(n, dec)
    assert abs(rt / emp - R2) < 1e-12 and mc <= rt + 1e-9 and mc > rt - 2e-3
    RESEAUX.append((nom, n, emp, rt, mc))
HEX = np.array([i * np.array([1, 0]) + j * np.array([0.5, math.sqrt(3) / 2]) for i in range(-3, 4) for j in range(-3, 4)])
R_HEX = float(np.min(np.linalg.norm(HEX - np.array([0.5, math.sqrt(3) / 6]), axis=1)))
assert abs(R_HEX - 1 / math.sqrt(3)) < 1e-12
F24 = [comb(24, k) * 2 ** k for k in range(1, 25)]
assert sum((-1) ** i * v for i, v in enumerate(F24)) == 0 and F24[0] == 48 and F24[-1] == 2 ** 24
F24_TXT = f"{F24[-1]:,}".replace(",", " ")

ligne("\n## 4. 24 pour la sphère 24D\n")
ligne(f"**La chèvre 24D.** ρ₂₄ = {fr(RHO[24], '{:.12f}')}… (certifiée à 50 chiffres dans la partie XX), α₂₄ ="
      f" {fr(ALPHA[24], '{:.3f}')}°. Ses 48 piquets ±e_i couvrent la clôture S²³ (seuil arccos(1/√24) ="
      f" {fr(SEUIL[24], '{:.2f}')}°). Le nerf est le bord du polytope croisé de dimension 24 : {F24[0]} sommets,"
      f" {F24[1]} arêtes, …, 2²⁴ = {F24_TXT} facettes, de caractéristique d'Euler 0, celle de S²³. Un point au hasard"
      f" de la clôture est brouté par {fr(MULT[24][2], '{:.1f}')} chèvres en moyenne.")
ligne("- Les 48 piquets sont aussi les 48 points où une sphère de ℤ²⁴ touche ses voisines (les centres des faces du"
      " cube).\n")
ligne("**Le réseau de Leech garde le √2 du carré.** Ses sphères ont un rayon de 1 (vecteurs minimaux de norme 4), et le"
      " point de l'espace le plus éloigné du réseau est à √2 : le rayon de recouvrement vaut √2 (Conway, Parker et"
      " Sloane, 1982). Les trous les plus profonds forment 23 familles, une par réseau de Niemeier. C'est exactement le"
      " rapport du carré de neuf points : milieux (contacts) à 1, centre (trou) à √2.\n")
ligne("| réseau | dimension | rayon des sphères | trou le plus profond | rapport | contrôle |")
ligne("|---|---:|---|---|---|---|")
ligne("| ℤ (la droite) | 1 | ½ | ½ | 1 | exact |")
EXACT = {2: ("½", "√2/2", "(½, ½)"), 3: ("√2/2", "1", "(1, 0, 0)"), 4: ("√2/2", "1", "(1, 0, 0, 0) et (½, ½, ½, ½)"),
         8: ("√2/2", "1", "(1, 0, …, 0)")}
for nom, n, emp, rt, mc in RESEAUX:
    e_, t_, h_ = EXACT[n]
    ligne(f"| {nom} | {n} | {e_} | {t_} | √2 | trou en {h_} ; le plus loin trouvé par tirage : {fr(mc, '{:.5f}')} |")
ligne(f"| A₂ = hexagonal (record en 2D) | 2 | ½ | 1/√3 = {fr(R_HEX)} | 2/√3 = {fr(2 / math.sqrt(3))} | exact |")
ligne("| Λ₂₄ = Leech (record en 24D) | 24 | 1 | √2 | √2 | Conway, Parker et Sloane (1982) |")
ligne(f"| ℤ²⁴ | 24 | ½ | √24/2 | √24 = {fr(math.sqrt(24))} | exact |")
ligne("\n- **En 3, 8 et 24**, trois des cinq dimensions où l'empilement record est démontré (1, 2, 3, 8, 24), le trou le"
      " plus profond est à √2 fois le rayon des sphères : le rapport du carré de neuf points. En 2D, le record"
      " (hexagonal) a 2/√3 ; le carré, lui, a √2.")
ligne("- **Dans ℤ²⁴**, le centre du cube est à √24 fois le rayon. Leech ramène ce rapport au √2 du carré, comme E₈ le"
      " fait en 8D en remplissant les trous de D₈ (partie XX).")
ligne("- **Les contacts.** Une sphère de ℤ²⁴ en touche 48 (les piquets des chèvres), une sphère de Leech 196 560"
      " (partie XXI).")
ligne(f"- Une coïncidence à signaler, sans plus : 2/√3 = {fr(2 / math.sqrt(3), '{:.5f}')} (l'hexagonal) et ρ₂ ="
      f" {fr(RHO[2], '{:.5f}')} (la chèvre plane) diffèrent de {fr(100 * (RHO[2] * math.sqrt(3) / 2 - 1), '{:.2f}')} %."
      " Je ne connais pas de procédé commun.")

with open(os.path.join(ICI, "..", "resultats", "carre_neuf_points.md"), "w") as fh:
    fh.write("# Résultats de la partie XXII (générés par scripts/carre_neuf_points.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure w1
# ===========================================================================
COUL = {1: F.SEQ[3], 2: F.ORANGE, 3: F.JAUNE, 8: F.AQUA, 24: F.SEQ[10], 100: F.SEQ[13]}


def cercle(ax, r, cx=0.0, cy=0.0, t0=0.0, t1=2 * np.pi, **kw):
    t = np.linspace(t0, t1, 400)
    ax.plot(cx + r * np.cos(t), cy + r * np.sin(t), **kw)


def schema(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)


def legende(ax, texte, y=-0.02):
    ax.text(0.5, y, texte, transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)


fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.18, hspace=0.3)

# a) le carré de neuf points et les cordes
ax = fig.add_subplot(gs[0, 0])
ax.add_patch(plt.Circle((0, 0), 1, fc=F.SEQ[1], ec=F.INK, lw=1.3, alpha=0.8))
ax.add_patch(Polygon([(-1, -1), (1, -1), (1, 1), (-1, 1)], closed=True, fill=False, ec=F.BLEU, lw=1.4))
ax.add_patch(Polygon([(1, 0), (0, 1), (-1, 0), (0, -1)], closed=True, fill=False, ec=F.BASE, lw=1.0, ls="--"))
cercle(ax, 1 / R2, color=VIOLET, lw=1.0, ls=":")
for n, c, lw in [(n, COUL[n], 1.6 if n in (1, 2) else 1.2) for n in (1, 2, 3, 8, 24, 100)] + [(None, ROUGE, 2.4)]:
    rr = R2 if n is None else RHO[n]
    t = np.linspace(math.radians(95), math.radians(265), 500)
    xa, ya = 1 + rr * np.cos(t), rr * np.sin(t)
    ax.plot(xa, ya, color=c, lw=0.9, alpha=0.35)
    pre = xa ** 2 + ya ** 2 <= 1 + 1e-9
    ax.plot(np.where(pre, xa, np.nan), np.where(pre, ya, np.nan), color=c, lw=lw + 0.6)
for (x_, y_) in NEUF:
    c = VIOLET if (x_, y_) == (0, 0) else (ROUGE if x_ * y_ == 0 else F.BLEU)
    ax.plot([x_], [y_], "o", ms=13 if (x_, y_) == PIQUET else 10, color=c, mec=F.SURF, mew=1.8, zorder=6)
for sx in (1, -1):
    for sy in (1, -1):
        ax.plot([sx / 2], [sy / 2], "o", ms=4, color=VIOLET, zorder=5)
ax.annotate("", (0.03, 0.0), (0.97, 0.0), arrowprops=dict(arrowstyle="<->", color=F.INK, lw=1.2))
ax.text(0.5, -0.12, "1", ha="center", va="top", fontsize=11, fontweight="bold")
ax.annotate("", (0.03, 0.97), (0.97, 0.03), arrowprops=dict(arrowstyle="<->", color=ROUGE, lw=1.2))
ax.text(0.56, 0.56, "√2", color=ROUGE, fontsize=11, fontweight="bold")
ax.text(1.12, 0.06, "piquet", color=ROUGE, fontsize=9.4, fontweight="bold")
for i, n in enumerate((1, 2, 3, 8, 24, 100)):
    ax.text(1.55, 1.15 - 0.17 * i, f"n = {n} : ρ = {fr(RHO[n], '{:.4f}')}", color=COUL[n], fontsize=9.0,
            fontweight="bold")
ax.text(1.55, 1.15 - 0.17 * 6, "n = ∞ : ρ = √2 = 1,4142", color=ROUGE, fontsize=9.0, fontweight="bold")
ax.text(1.55, -0.3, "bleu : sommets (le réseau)\nrouge : milieux (contacts,\n    piquets)\nviolet : centre (le trou)\n"
        "pointillés : rayon 1/√2", fontsize=8.6, color=F.INK2, va="top", linespacing=1.35)
schema(ax, (-1.55, 3.15), (-1.55, 1.55))
ax.set_title("a)  Le carré de neuf points et les cordes de 1 à √2")
legende(ax, "Piquet au milieu (1, 0) d'un côté. Le centre et les deux coins voisins sont à 1, les deux milieux voisins à"
        "\n√2. Les cordes de toutes les dimensions remplissent la bande entre les deux (en trait plein, la partie dans"
        "\nle pré) : la chèvre de la droite atteint le centre, celle de dimension infinie les milieux voisins.")

# b) les décades de dimension jusqu'à 10⁵¹
ax = fig.add_subplot(gs[0, 1])
NS_CALC = [2, 3, 4, 8, 24, 100]
xs = NS_CALC + [10 ** k for k in DEC]
ys = [2 - RHO[n] ** 2 for n in NS_CALC] + [2 - RHO2_DEC[k] for k in DEC]
nn = np.logspace(0, 52, 300)
ax.loglog(nn, 2 / nn, color=F.MUTED, lw=1.2, ls="--")
ax.loglog(xs, ys, "o", ms=7, color=F.BLEU, mec=F.SURF, zorder=5)
for k in (49, 50, 51):
    ax.loglog([2 * 10.0 ** k], [10.0 ** -k], "o", ms=10, color=ROUGE, mec=F.SURF, zorder=6)
ax.annotate("le miroir de la partie XXI :\n10⁻⁴⁹, 10⁻⁵⁰, 10⁻⁵¹ en\nn = 2·10⁴⁹, 2·10⁵⁰, 2·10⁵¹", (2e49, 1e-49), (1e4, 1e-40),
            fontsize=9, color=ROUGE, va="center", fontweight="bold", arrowprops=dict(arrowstyle="->", color=ROUGE))
ax.text(1e24, 3e-20, "2 − ρ² ≈ 2/n", color=F.MUTED, fontsize=9.4, rotation=-33)
ax.text(1e11, 1e-2, "\n".join(f"n = 10{sup(k)} : ρ² = {fr(RHO2_DEC[k], '{:.' + str(min(2 * k + 2, 15)) + 'f}')}"
                              for k in range(1, 7)), fontsize=8.8, va="top", color=F.INK, family="DejaVu Sans Mono",
        bbox=dict(fc=F.SURF, ec=F.BASE, pad=4))
ax.set_xlim(1, 1e53)
ax.set_ylim(1e-53, 3)
ax.set_xticks([1, 1e10, 1e20, 1e30, 1e40, 1e50])
ax.set_yticks([1, 1e-10, 1e-20, 1e-30, 1e-40, 1e-50])
ax.set_xlabel("dimension n")
ax.set_ylabel("2 − ρ_n² : ce qui manque au doublement de l'aire")
ax.set_title("b)  Les pas de 10 se précipitent vers √2")
legende(ax, "Points bleus : la corde calculée (dimensions 2 à 10⁸). Chaque facteur 10"
        "\nsur la dimension ajoute un 9 à ρ² (encadré). ρ² est l'aire du disque de la corde"
        "\nrapportée au pré : elle ne double qu'à l'infini. Sur la droite 2/n, la précision"
        "\n10⁻⁵⁰ tombe en dimension 2·10⁵⁰.", y=-0.13)

# c) les 3ⁿ points du cube
ax = fig.add_subplot(gs[0, 2])
NMAX = 8
MAT = np.full((NMAX, NMAX + 1), np.nan)
for n, v in FACES.items():
    MAT[n - 1, :n + 1] = v
ax.imshow(np.log10(MAT), cmap=ListedColormap(F.SEQ[1:11]), aspect="auto", vmin=0, vmax=3.2)
for n, v in FACES.items():
    for k, x_ in enumerate(v):
        ax.text(k, n - 1, str(x_), ha="center", va="center", fontsize=9.2,
                color=F.SURF if x_ >= 200 else F.INK, fontweight="bold" if n == 2 else "normal")
    ax.text(NMAX + 1.75, n - 1, f"{3 ** n}", ha="right", va="center", fontsize=9.2, color=F.INK)
    ax.text(NMAX + 2.05, n - 1, TOUR[pow(3, n, 10)], ha="left", va="center", fontsize=9.2,
            color=[F.BLEU, ROUGE, F.AQUA, F.INK][(n - 1) % 4], fontweight="bold")
ax.add_patch(plt.Rectangle((-0.5, 0.5), 3, 1, fill=False, ec=ROUGE, lw=2.2))
ax.set_xticks(range(NMAX + 1))
ax.set_xticklabels(["0", "1", "√2", "√3", "2", "√5", "√6", "√7", "2√2"])
ax.set_yticks(range(NMAX))
ax.set_yticklabels([f"n = {n}" for n in range(1, NMAX + 1)])
ax.set_xlim(-0.5, NMAX + 4.1)
ax.set_ylim(NMAX - 0.5, -1.25)
ax.text(NMAX + 1.75, -0.85, "3ⁿ", ha="right", va="center", fontsize=9.4, fontweight="bold")
ax.text(NMAX + 2.05, -0.85, "mod 10", ha="left", va="center", fontsize=9.4, fontweight="bold")
ax.text((NMAX) / 2, -0.85, "nombre de points à chaque distance", ha="center", va="center", fontsize=9.0,
        color=F.INK2)
ax.set_xlabel("distance au centre")
ax.grid(False)
ax.set_title("c)  Les 3ⁿ points du cube, et la base 10 qui tourne")
legende(ax, "Les centres des faces du cube de dimension n, rangés par distance au centre :"
        "\nC(n, k)·2ᵏ points à √k. Le carré de neuf points est la ligne n = 2 (cadre rouge)."
        "\nLe total 3ⁿ tourne d'un quart de tour modulo 10 à chaque dimension"
        "\n(3 est i modulo 10, partie XIX) : 3, 9, 7, 1.", y=-0.13)

# d) les faisceaux en 2D : dimension finie et dimension infinie
ax = fig.add_subplot(gs[1, 0])
for cx, alpha_, titre in ((0, ALPHA[2], "n = 2 : α = 70,81°"), (3.1, 90.0, "n = ∞ : α = 90°")):
    cercle(ax, 1, cx, 0, color=F.BASE, lw=1.2)
    for i, (ang, c) in enumerate(((0, F.ORANGE), (90, F.AQUA), (180, F.BLEU), (270, VIOLET))):
        rr = 1.08 + 0.07 * i
        cercle(ax, rr, cx, 0, t0=math.radians(ang - alpha_), t1=math.radians(ang + alpha_), color=c, lw=3.2,
               solid_capstyle="butt")
        px, py = cx + math.cos(math.radians(ang)), math.sin(math.radians(ang))
        ax.plot([px], [py], "o", ms=9, color=c, mec=F.SURF, zorder=6)
    som = [(cx + 0.62 * math.cos(math.radians(a)), 0.62 * math.sin(math.radians(a))) for a in (0, 90, 180, 270)]
    if alpha_ < 90:
        ax.add_patch(Polygon(som, closed=True, fill=False, ec=F.INK, lw=1.6))
    else:
        for tri in itertools.combinations(range(4), 3):
            ax.add_patch(Polygon([som[t] for t in tri], closed=True, fc=ROUGE, alpha=0.07, ec="none"))
        for a_, b_ in itertools.combinations(range(4), 2):
            ax.plot([som[a_][0], som[b_][0]], [som[a_][1], som[b_][1]], color=ROUGE, lw=1.4)
    for p in som:
        ax.plot([p[0]], [p[1]], "o", ms=6, color=F.INK, zorder=7)
    ax.text(cx, 1.62, titre, ha="center", fontsize=10, fontweight="bold")
ax.text(0, -1.62, "nerf : un carré (cycle de 4)\n= le cercle, H¹ = ℤ", ha="center", va="top", fontsize=9, color=F.INK)
ax.text(3.1, -1.62, "nerf : le bord d'un tétraèdre\n= S², faux : Est et Ouest\nse touchent en deux points",
        ha="center", va="top", fontsize=9, color=ROUGE)
for a in (45, 135, 225, 315):
    ax.text(1.5 * math.cos(math.radians(a)), 1.5 * math.sin(math.radians(a)), "2", ha="center", va="center",
            fontsize=9, color=F.INK2, fontweight="bold")
schema(ax, (-1.75, 4.85), (-2.45, 1.85))
ax.set_title("d)  Les faisceaux : quatre chèvres aux quatre milieux")
legende(ax, "Chaque chèvre broute un arc de la clôture (couleurs décalées pour les voir). À gauche, les arcs voisins se"
        "\nrecouvrent deux à deux autour des sommets (les « 2 »), jamais les opposés : le nerf calcule le cercle. À"
        "\ndroite, la limite infinie : les opposés se touchent, le recouvrement n'est plus bon et le nerf se trompe.")

# e) en 3D : six chèvres sur la sphère
ax = fig.add_subplot(gs[1, 1])
az, el = math.radians(35), math.radians(25)
droite = np.array([-math.sin(az), math.cos(az), 0.0])
haut = np.array([-math.sin(el) * math.cos(az), -math.sin(el) * math.sin(az), math.cos(el)])
oeil = np.array([math.cos(el) * math.cos(az), math.cos(el) * math.sin(az), math.sin(el)])
N_PIX = 520
u_ = np.linspace(-1, 1, N_PIX)
U_, V_ = np.meshgrid(u_, u_)
W2 = 1 - U_ ** 2 - V_ ** 2
dedans = W2 >= 0
P3 = U_[..., None] * droite + V_[..., None] * haut + np.sqrt(np.clip(W2, 0, None))[..., None] * oeil
MULT3 = (np.abs(P3) >= math.cos(math.radians(ALPHA[3]))).sum(axis=2).astype(float)
MULT3[~dedans] = np.nan
ax.imshow(MULT3, origin="lower", extent=(-1, 1, -1, 1), cmap=ListedColormap([F.SEQ[2], F.SEQ[6], F.SEQ[11]]),
          vmin=0.5, vmax=3.5, interpolation="nearest")
cercle(ax, 1, color=F.INK, lw=1.2)
for v in [s * np.eye(3)[i] for i in range(3) for s in (1, -1)]:
    if v @ oeil > 0:
        p_ = (v @ droite, v @ haut)
        ax.plot([p_[0]], [p_[1]], "o", ms=9, color=ROUGE, mec=F.SURF, zorder=6)
for v in itertools.product((1, -1), repeat=3):
    w = np.array(v) / math.sqrt(3)
    if w @ oeil > 0:
        ax.plot([w @ droite], [w @ haut], "s", ms=8, color=F.JAUNE, mec=F.INK, mew=0.8, zorder=6)
for val, nom, c in ((1, "1 chèvre (autour des piquets)", F.SEQ[2]), (2, "2 chèvres (autour des arêtes)", F.SEQ[6]),
                    (3, "3 chèvres (autour des sommets du cube)", F.SEQ[11])):
    ax.plot([], [], "s", ms=10, color=c, label=nom)
ax.plot([], [], "o", ms=8, color=ROUGE, label="piquets ±e_i (sommets de l'octaèdre)")
ax.plot([], [], "s", ms=8, color=F.JAUNE, mec=F.INK, label="directions des sommets du cube")
ax.legend(loc="lower center", ncol=2, fontsize=8.2, frameon=True, facecolor=F.SURF, edgecolor="none",
          columnspacing=1.0, handletextpad=0.4)
schema(ax, (-1.45, 1.45), (-1.62, 1.06))
ax.set_title("e)  En 3D : six chèvres sur la sphère, nerf = octaèdre")
legende(ax, "La clôture S² vue de face, coloriée par le nombre de chèvres (α₃ = 75,80°) qui broutent chaque point. Le"
        "\nnerf est l'octaèdre : 6 sommets, 12 arêtes, 8 triangles, un par sommet du cube, là où trois chèvres se"
        "\nrecouvrent. Jamais deux opposées : le nerf calcule bien la sphère S².")

# f) le rapport trou / rayon, et la corde
ax = fig.add_subplot(gs[1, 2])
dims = np.arange(1, 27)
ax.plot(dims, np.sqrt(dims), color=F.MUTED, lw=1.4, ls="--")
ax.text(20.5, math.sqrt(20.5) + 0.12, "ℤⁿ : √n (le centre du cube)", color=F.MUTED, fontsize=8.8, ha="right",
        rotation=8)
ax.plot(range(1, 27), [RHO[n] for n in range(1, 27)], "-o", color=F.ORANGE, ms=4, lw=1.6,
        label="corde de la chèvre ρ_n (de 1 à √2)")
ax.axhline(R2, color=ROUGE, lw=1.2)
ax.text(15, R2 + 0.04, "√2", color=ROUGE, fontsize=11, fontweight="bold", ha="center", va="bottom")
for x_, y_, nom, c, at in ((1, 1.0, "ℤ : 1", F.INK, (1.6, 0.86)),
                           (2, 2 / math.sqrt(3), "A₂ hexagonal : 2/√3", F.BLEU, (4.6, 1.02)),
                           (2, R2, "ℤ² (le carré)", ROUGE, (1.2, 2.05)), (3, R2, "D₃ (cfc)", ROUGE, (3.6, 2.3)),
                           (4, R2, "D₄", ROUGE, (5.6, 1.7)), (8, R2, "E₈", ROUGE, (8, 1.68)),
                           (24, R2, "Λ₂₄ (Leech)", ROUGE, (22.4, 1.68)), (24, math.sqrt(24), "ℤ²⁴ : √24", F.MUTED,
                                                                         (24, 5.15))):
    ax.plot([x_], [y_], "s" if c == ROUGE else "o", ms=10, color=c, mec=F.SURF, mew=1.5, zorder=6)
    fleche = math.dist(at, (x_, y_)) > 0.3
    ax.annotate(nom, (x_, y_), at, ha="center", va="center", fontsize=8.8, color=c, fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=c, lw=0.8, shrinkA=2, shrinkB=6) if fleche else None, zorder=7)
ax.set_xticks([1, 2, 3, 4, 8, 12, 16, 20, 24])
ax.set_xlim(0.3, 26.5)
ax.set_ylim(0.75, 5.4)
ax.set_xlabel("dimension")
ax.set_ylabel("trou le plus profond / rayon des sphères")
ax.legend(loc="upper left", fontsize=8.6, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("f)  3, 8, 24 : le trou le plus profond à √2")
legende(ax, "Carrés rouges : les réseaux dont le trou le plus profond est à √2 fois le rayon, comme le carré de neuf"
        "\npoints. En 3, 8 et 24, ce sont les empilements records ; Leech (24D) a ses sphères de rayon 1 et son trou à"
        "\n√2 (Conway, Parker, Sloane). La corde de la chèvre (orange) monte de 1 vers le même √2.", y=-0.13)
F.sauver(fig, "w1_carre_neuf_points.png")
