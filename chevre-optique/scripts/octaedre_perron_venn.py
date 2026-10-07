"""
Partie XXVIII : l'hexagone rejoint l'octaèdre, le théorème de Perron développé, et le Venn à 17.

    python3 scripts/octaedre_perron_venn.py        # ≈ 1 min

Écrit resultats/octaedre_perron_venn.md, figures/ac1_octaedre.png, figures/ac2_perron.png et figures/ac3_venn17.png.

1. L'octaèdre : dual du cube par la sphère médiane, même ombre hexagonale, ombre max(‖u‖₁, 2‖u‖∞), égale à celle du
   cube sur 35,1 % des directions ; les deux cercles arctiques (dominos, losanges) comme ombres de la sphère médiane ;
   la récurrence de l'octaèdre (Dodgson, Kuo) qui compte les deux pavages ; son cône de lumière, de rayon t/√2.
2. Perron : une fusion (3α² − 4α + 2), la borne « cœur + oreilles » pour tous les rapports, les oreilles égales
   (d'où les rapports télescopiques), le plateau 1/(k + 2) démontré par l'ombre du cube, et la fenêtre de Kakeya
   au grain δ entièrement démontrée (avec N éventails : le polygone circonscrit à 2N côtés).
3. Le Venn à 17 : Henderson (n premier), Fermat par les orbites, les comptes d'Euler, un Venn à 5 ellipses vérifié,
   le diaphragme à 17 lames (97,7 % de la lumière, 34 aigrettes), Gauss, 4 ≡ i (mod 17), la période de 1/17 et son
   miroir, le diaphragme de Perron à 17 lames, et les coupes de l'arbre de Perron comme Venn à une dimension.
"""

import itertools
import logging
import math
import os
import sys
import textwrap
import time
from fractions import Fraction as Fr

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, to_rgb
from matplotlib.patches import Circle, Polygon
from scipy import ndimage
from scipy.spatial import ConvexHull

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
ROUGE, VIOLET, VERT = "#d0342c", "#7d4fc4", "#1baf7a"
R2, R3 = math.sqrt(2), math.sqrt(3)
GAM = float(mp.euler)
T0 = time.time()
mp.mp.dps = 40
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


def sup(n):
    return str(n).translate(str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))


def sci(x, c=2):
    e = math.floor(math.log10(abs(x)))
    return f"{fr(x / 10 ** e, '{:.' + str(c) + 'f}')}·10{sup(e)}"


def ent(n):
    return f"{n:,}".replace(",", " ")


def petit(x, c=0):
    """Un petit nombre écrit m·10⁻ⁿ (0 s'il est nul)."""
    if x == 0:
        return "0"
    e = math.floor(math.log10(abs(x)))
    m = round(x / 10 ** e, c)
    if abs(m) >= 10:
        m, e = m / 10, e + 1
    return f"{fr(m, '{:.' + str(c) + 'f}')}·10{sup(e)}"


ligne("# Partie XXVIII : l'hexagone rejoint l'octaèdre, le théorème de Perron développé, le Venn à 17\n")
ligne("Tableaux complets, recalculés par `scripts/octaedre_perron_venn.py`.\n")

# ===========================================================================
# 1. L'octaèdre
# ===========================================================================
ligne("## 1. L'hexagone rejoint l'octaèdre\n")
CUBE = np.array(list(itertools.product([-0.5, 0.5], repeat=3)))
OCT = np.vstack([np.eye(3), -np.eye(3)])
SIG = np.array(list(itertools.product([-1, 1], repeat=3)), float)


def ombre_cube(u):
    return np.abs(u).sum(-1)


def ombre_oct_faces(u):
    """Ombre de |x| + |y| + |z| ≤ 1 par ses 8 faces : ½ Σ aire·|n·u| = ¼ Σ_σ |σ·u|."""
    return 0.25 * np.abs(u @ SIG.T).sum(-1)


def ombre_oct(u):
    return np.maximum(np.abs(u).sum(-1), 2 * np.abs(u).max(-1))


def repere(u):
    a = np.cross(u, [1.0, 0, 0]) if abs(u[0]) < 0.9 else np.cross(u, [0, 1.0, 0])
    a /= np.linalg.norm(a)
    return a, np.cross(u, a)


def aire_projetee(P, u):
    a, b = repere(u)
    return ConvexHull(np.c_[P @ a, P @ b]).volume


def aretes(P, L):
    return [(i, j) for i, j in itertools.combinations(range(len(P)), 2) if abs(np.linalg.norm(P[i] - P[j]) - L) < 1e-9]


def silhouette(P, E, u):
    """Arêtes dont la projection est un côté du contour."""
    a, b = repere(u)
    h = ConvexHull(np.c_[P @ a, P @ b])
    cyc = list(h.vertices)
    out = []
    for i, j in E:
        if i in cyc and j in cyc and (cyc.index(i) - cyc.index(j)) % len(cyc) in (1, len(cyc) - 1):
            out.append((i, j))
    return out


rng = np.random.default_rng(28)
U = rng.normal(size=(200000, 3))
U /= np.linalg.norm(U, axis=1)[:, None]
ERR_FACES = float(np.abs(ombre_oct_faces(U) - ombre_oct(U)).max())
ERR_PROJ = max(max(abs(aire_projetee(CUBE, u) - ombre_cube(u)), abs(aire_projetee(OCT, u) - ombre_oct(u)))
               for u in U[:2000])
n_fib = 2_000_000
i_ = np.arange(n_fib) + 0.5
zf = 1 - 2 * i_ / n_fib
rf = np.sqrt(1 - zf * zf)
phf = i_ * math.pi * (3 - math.sqrt(5))
VF = np.c_[rf * np.cos(phf), rf * np.sin(phf), zf]
MOY_OCT, MOY_CUBE = float(ombre_oct(VF).mean()), float(ombre_cube(VF).mean())
FRAC_EGAL = float((np.abs(ombre_oct(VF) - ombre_cube(VF)) < 1e-12).mean())
FRAC_TH = 6 * math.acos(1 / 3) / math.pi - 2
N3, N4, N2 = np.ones(3) / R3, np.array([0, 0, 1.0]), np.array([1.0, 1, 0]) / R2
proj_c = CUBE - np.outer(CUBE @ N3, N3)
proj_o = OCT - np.outer(OCT @ N3, N3)
ECART_HEX = max(float(np.min(np.linalg.norm(proj_c - p, axis=1))) for p in proj_o)
E_CUBE, E_OCT = aretes(CUBE, 1.0), aretes(OCT, R2)
MIL_C = sorted({tuple(np.round((CUBE[i] + CUBE[j]) / 2, 9)) for i, j in E_CUBE})
MIL_O = sorted({tuple(np.round((OCT[i] + OCT[j]) / 2, 9)) for i, j in E_OCT})
ligne("### 1.1 Le cube [−½, ½]³ et l'octaèdre |x| + |y| + |z| ≤ 1\n")
ligne("- Polaire du cube par la sphère de rayon √2/2 : {y : x·y ≤ ½ pour tout x du cube} = {½‖y‖₁ ≤ ½} = l'octaèdre."
      " L'ombre du cube ‖u‖₁ (partie XXVI) est la jauge de l'octaèdre.")
ligne(f"- Les 12 milieux d'arêtes coïncident : {'oui' if MIL_C == MIL_O else 'non'} ; à distance"
      f" {fr(float(np.linalg.norm(MIL_C[0])), '{:.6f}')} = √2/2 (la sphère médiane des deux solides).")
ligne(f"- Le long de (1, 1, 1), chaque sommet de l'octaèdre se projette sur un sommet du cube (écart"
      f" {petit(ECART_HEX, 1)}) : les deux ombres sont le même hexagone.")


def coupe_centrale(P, E, n):
    """Points où le plan n·x = 0 coupe les arêtes."""
    pts = []
    for i, j in E:
        a, b = P[i] @ n, P[j] @ n
        if a * b < 0:
            t = a / (a - b)
            pts.append(tuple(np.round(P[i] + t * (P[j] - P[i]), 9)))
    return sorted(set(pts))


COUPE_C, COUPE_O = coupe_centrale(CUBE, E_CUBE, N3), coupe_centrale(OCT, E_OCT, N3)
ligne(f"- Le plan x + y + z = 0 coupe le cube et l'octaèdre selon le même hexagone ({len(COUPE_C)} sommets,"
      f" {'identiques' if COUPE_C == COUPE_O else 'différents'}) : ses sommets sont 6 des 12 milieux communs, à"
      f" {fr(float(np.linalg.norm(COUPE_C[0])), '{:.6f}')} du centre (le cercle inscrit dans l'ombre passe par eux).\n")
ligne("| axe | arêtes du contour (cube) | leurs milieux · axe | arêtes du contour (octaèdre) | leurs milieux · axe |")
ligne("|---|---:|---|---:|---|")
SIL = {}
for nom, ax_ in (("ordre 3 : (1, 1, 1)", N3), ("ordre 4 : (0, 0, 1)", N4)):
    sc, so = silhouette(CUBE, E_CUBE, ax_), silhouette(OCT, E_OCT, ax_)
    mc = max(abs(float(((CUBE[i] + CUBE[j]) / 2) @ ax_)) for i, j in sc)
    mo = max(abs(float(((OCT[i] + OCT[j]) / 2) @ ax_)) for i, j in so)
    SIL[nom] = (mc, mo)
    ligne(f"| {nom} | {len(sc)} | max {fr(mc, '{:.3f}')} | {len(so)} | max {fr(mo, '{:.3f}')} |")
ligne("\nQuand les milieux des arêtes du contour sont dans le plan équatorial (produit scalaire nul), la sphère médiane"
      " touche le contour en ces points : son ombre est le cercle inscrit dans l'ombre du solide.\n")

ligne("### 1.2 L'ombre de l'octaèdre\n")
ligne(f"- Par ses faces : ¼ Σ_σ |σ·u| ; c'est max(‖u‖₁, 2‖u‖∞) à {petit(ERR_FACES)} près sur 200 000 directions ;"
      f" projection directe des sommets : écart {petit(ERR_PROJ)} (cube et octaèdre).")
ligne(f"- Égale à l'ombre du cube sur une part {fr(FRAC_EGAL, '{:.6f}')} des directions (grille de Fibonacci,"
      f" 2·10⁶ points) ; théorie 6·arccos(1/3)/π − 2 = {fr(FRAC_TH, '{:.6f}')}.")
ligne(f"- Moyennes sur la sphère : octaèdre {fr(MOY_OCT, '{:.9f}')} (√3 = {fr(R3, '{:.9f}')}, Cauchy : surface 4√3 / 4) ;"
      f" cube {fr(MOY_CUBE, '{:.9f}')} (3/2).\n")
ligne("| direction | ombre du cube | ombre de l'octaèdre | forme (cube / octaèdre) |")
ligne("|---|---|---|---|")
for nom, u_, fo in (("axe d'ordre 4", N4, "carré d'aire 1 / losange (diamant) d'aire 2"),
                    ("axe d'ordre 3", N3, "le même hexagone"),
                    ("axe d'ordre 2", N2, "rectangle 1 × √2 / losange de diagonales 2 et √2")):
    ligne(f"| {nom} | {fr(float(ombre_cube(u_)), '{:.6f}')} | {fr(float(ombre_oct(u_)), '{:.6f}')} | {fo} |")
ZONO = np.array([sum(s * g for s, g in zip(sg, SIG[[7, 6, 5, 3]] / 2)) for sg in itertools.product([-1, 1], repeat=4)])
hz = ConvexHull(ZONO)
NORM_Z = {tuple(np.round(eq[:3], 6)) for eq in hz.equations}
ERR_ZONO = max(abs(float(np.max(ZONO @ u) - ombre_oct(u))) for u in U[:3000])
ligne(f"\n- Le zonoèdre engendré par les 4 grandes diagonales [−σ/2, σ/2] a {len(hz.vertices)} sommets et"
      f" {len(NORM_Z)} faces : le dodécaèdre rhombique (les losanges de la partie II). Sa fonction d'appui est l'ombre"
      f" de l'octaèdre (écart {petit(ERR_ZONO)}).")
ligne("- arccos(1/3) = 70,53° : l'angle des 8 triangles sphériques (côtés 60°, sommets aux axes d'ordre 2) où les"
      " deux ombres sont égales.\n")


# --- la conique inscrite ---
def hexagone(a, b, c):
    P = [0j]
    for long_, k in zip([a, b, c, a, b, c], range(6)):
        P.append(P[-1] + long_ * np.exp(1j * math.pi * k / 3))
    P = np.array(P[:-1])
    return P - P.mean()


def droites(P):
    out = []
    for i in range(len(P)):
        p, q = P[i], P[(i + 1) % len(P)]
        a, b = (q - p).imag, -(q - p).real
        out.append(np.array([a, b, -(a * p.real + b * p.imag)]) / math.hypot(a, b))
    return out


def conique_cinq(L):
    """La conique tangente à 5 droites : l^T C* l = 0 (C* = conique duale, 6 inconnues), noyau de dimension 1."""
    M = np.array([[a * a, 2 * a * b, b * b, 2 * a * c, 2 * b * c, c * c] for a, b, c in L])
    v = np.linalg.svd(M)[2][-1]
    A, B, C, D, E, F_ = v
    return np.array([[A, B, D], [B, C, E], [D, E, F_]])


ligne("### 1.3 La conique inscrite (l'argument du cercle arctique)\n")
ligne("Kenyon et Okounkov : la frontière gelée d'un pavage en losanges d'un polygone à 3d côtés est une courbe de classe"
      " d inscrite (tangente à tous les côtés) ; pour l'hexagone, une conique. Cinq tangentes fixent une conique :\n")
ligne("| hexagone (côtés a, b, c, a, b, c) | conique tangente aux 5 premiers côtés : résidu sur le 6ᵉ | la conique |")
ligne("|---|---|---|")
CONIQUES = {}
for abc in ((1, 1, 1), (2, 3, 4), (1, 2, 5)):
    L_ = droites(hexagone(*abc))
    Cs = conique_cinq(L_[:5])
    res = float(L_[5] @ Cs @ L_[5])
    C_ = np.linalg.inv(Cs)
    C_ /= -C_[2, 2]
    CONIQUES[abc] = (res, C_)
    if abc == (1, 1, 1):
        r_in = abs(L_[0][2])
        desc = f"x² + y² = {fr(1 / C_[0, 0], '{:.6f}')} = r² du cercle inscrit ({fr(r_in ** 2, '{:.6f}')})"
    else:
        desc = f"ellipse {fr(C_[0, 0], '{:.4f}')}x² + {fr(2 * C_[0, 1], '{:.4f}')}xy + {fr(C_[1, 1], '{:.4f}')}y² = 1"
    ligne(f"| {abc} | {petit(abs(res))} | {desc} |")
ligne("\nPour l'hexagone régulier, la conique est le cercle inscrit, c'est-à-dire l'ombre de la sphère médiane"
      " (§ 1.1) ; pour a × b × c, l'ellipse inscrite de Cohn, Larsen et Propp. Le 6ᵉ côté est tangent parce que les"
      " grandes diagonales d'un hexagone centré se coupent au centre (Brianchon).\n")


# --- la récurrence de l'octaèdre ---
def H(n):
    p = 1
    for k in range(n):
        p *= math.factorial(k)
    return p


def macmahon(a, b, c):
    num, den = H(a) * H(b) * H(c) * H(a + b + c), H(a + b) * H(b + c) * H(c + a)
    assert num % den == 0
    return num // den


ligne("### 1.4 La récurrence de l'octaèdre compte les deux pavages\n")
AD = [2 ** (n * (n + 1) // 2) for n in range(0, 61)]
OK_AD = all(AD[n] * AD[n - 2] == 2 * AD[n - 1] ** 2 for n in range(2, 61))
OK_KUO, N_KUO = True, 0
for a, b, c in itertools.product(range(1, 13), repeat=3):
    g = macmahon(a, b, c) * macmahon(a, b - 1, c - 1)
    d = macmahon(a + 1, b - 1, c - 1) * macmahon(a - 1, b, c) + macmahon(a, b - 1, c) * macmahon(a, b, c - 1)
    OK_KUO &= g == d
    N_KUO += 1
PTS_KUO = [(0, 0, 0), (0, -1, -1), (1, -1, -1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
MILIEUX_KUO = {tuple((np.array(PTS_KUO[2 * i]) + np.array(PTS_KUO[2 * i + 1])) / 2) for i in range(3)}
ligne(f"- Diamant aztèque : AD(n) = 2^(n(n+1)/2) vérifie AD(n)·AD(n − 2) = 2·AD(n − 1)² (Dodgson) : "
      f"{'vrai' if OK_AD else 'faux'} pour n ≤ 60.")
ligne(f"- Hexagone : T(a, b, c)·T(a, b − 1, c − 1) = T(a + 1, b − 1, c − 1)·T(a − 1, b, c) + T(a, b − 1, c)·T(a, b, c − 1)"
      f" (Kuo, 2004), avec la formule de MacMahon : {'vrai' if OK_KUO else 'faux'} pour les {ent(N_KUO)} triplets a, b, c ≤ 12.")
ligne(f"- Les six hexagones de l'identité de Kuo forment trois paires de même milieu"
      f" ({'un seul milieu' if len(MILIEUX_KUO) == 1 else 'plusieurs milieux'} : (a, b − ½, c − ½)) : les sommets"
      " opposés d'un octaèdre, comme les six voisins de f(x, y, t) dans f(t + 1)f(t − 1) = f(x ± 1)… + f(y ± 1)….\n")

# --- le cône de lumière ---
ligne("### 1.5 Le cône de lumière de la récurrence linéarisée\n")
kk = np.linspace(-math.pi, math.pi, 1201)
K1, K2 = np.meshgrid(kk, kk)
c1_, c2_ = np.cos(K1), np.cos(K2)
s2_ = 1 - ((c1_ + c2_) / 2) ** 2
masque = s2_ > 1e-6
V2 = np.full(K1.shape, np.nan)
V2[masque] = (np.sin(K1[masque]) ** 2 + np.sin(K2[masque]) ** 2) / (4 * s2_[masque])
IDENT = 0.5 - (c1_ - c2_) ** 2 / (2 * (4 - (c1_ + c2_) ** 2))
ERR_IDENT = float(np.nanmax(np.abs(V2[masque] - IDENT[masque])))
ligne("- Ondes planes de h(t + 1) + h(t − 1) = ½[h(x ± 1) + h(y ± 1)] : cos ω = (cos k₁ + cos k₂)/2.")
ligne(f"- Vitesse de groupe : |∇ω|² = ½ − (cos k₁ − cos k₂)² / (2[4 − (cos k₁ + cos k₂)²]) (écart numérique"
      f" {petit(ERR_IDENT)}) ; maximum sur la grille {fr(float(np.nanmax(V2)), '{:.12f}')} = ½, donc |v| ≤ 1/√2.")
T_ONDE = 240
N_ONDE = 2 * T_ONDE + 5
c0 = N_ONDE // 2
h_prec, h_cour = np.zeros((N_ONDE, N_ONDE)), np.zeros((N_ONDE, N_ONDE))
h_cour[c0, c0] = 1.0
for _ in range(T_ONDE):
    h_suiv = 0.5 * (np.roll(h_cour, 1, 0) + np.roll(h_cour, -1, 0) + np.roll(h_cour, 1, 1) + np.roll(h_cour, -1, 1)) - h_prec
    h_prec, h_cour = h_cour, h_suiv
HX = h_cour
XX, YY = np.meshgrid(np.arange(N_ONDE) - c0, np.arange(N_ONDE) - c0)
RR, L1 = np.hypot(XX, YY), np.abs(XX) + np.abs(YY)
ENER = HX ** 2
SUPPORT = int(L1[np.abs(HX) > 0].max())
ligne(f"- Source ponctuelle, t = {T_ONDE} : le support exact est le losange |x| + |y| ≤ {SUPPORT} (un pas par tour).\n")
ligne("| rayon ÷ t | part de l'énergie Σh² en dedans | plus grand |h| au-delà |")
ligne("|---|---|---|")
PARTS = {}
for rr in (0.6, 0.7, 1 / R2, 0.72, 0.75, 0.8, 0.9):
    PARTS[rr] = (float(ENER[RR < rr * T_ONDE].sum() / ENER.sum()), float(np.abs(HX[RR >= rr * T_ONDE]).max()))
    nom = "1/√2 = 0,7071" if abs(rr - 1 / R2) < 1e-9 else fr(rr, "{:.2f}")
    ligne(f"| {nom} | {fr(PARTS[rr][0], '{:.6f}')} | {petit(PARTS[rr][1], 1)} |")
COIN = abs(float(HX[c0, c0 + T_ONDE]))
ligne(f"\n- Au coin (t, 0) du losange : |h| = {sci(COIN, 3)} = 2^(−{T_ONDE}) = {sci(2.0 ** -T_ONDE, 3)}.")
ligne("- Le losange est le cône exact, le cercle inscrit de rayon t/√2 le cône des vitesses de groupe : celui du cercle"
      " arctique des dominos (Jockusch, Propp, Shor). Le polynôme 1 − (x + 1/x + y + 1/y)z/2 + z² est un facteur du"
      " dénominateur de la fonction génératrice des probabilités de placement des dominos (Cohn, Elkies, Propp).\n")

# ===========================================================================
# 2. Perron
# ===========================================================================
ligne("## 2. Le théorème de Perron, développé\n")


def decalages(alphas):
    """Coordonnées de la partie : triangle de base [0, 1] à la profondeur u = 1, sommets à u = 0 ; la branche i a pour
    coupe [s_i + u·i/N, s_i + u·(i + 1)/N]. À l'étape j, le bloc de droite glisse de 2^j/N·((2α_j − 1)P_j − 1)."""
    k = len(alphas)
    N = 2 ** k
    zero = Fr(0) if isinstance(alphas[0], Fr) else 0.0
    P = [zero + 1]
    for a in alphas:
        P.append(P[-1] * a)
    D = [(zero + 2 ** j) / N * ((2 * alphas[j] - 1) * P[j] - 1) for j in range(k)]
    return [sum((D[j] for j in range(k) if (i >> j) & 1), zero) for i in range(N)], P


def longueur_coupe(s, u, N):
    iv = sorted((s[i] + u * i / N, s[i] + u * (i + 1) / N) for i in range(N))
    tot, (gl, gr) = 0, iv[0]
    for lo, hi in iv[1:]:
        if lo > gr:
            tot += gr - gl
            gl, gr = lo, hi
        else:
            gr = max(gr, hi)
    return tot + gr - gl


def aire_exacte(alphas):
    """Aire exacte (rapport au triangle) : la coupe est affine entre les points où deux bords se croisent."""
    s, P = decalages(alphas)
    N = len(s)
    zero = s[0]
    ruptures = {zero, zero + 1}
    for i, j in itertools.permutations(range(N), 2):
        for ei, ej in itertools.product((0, 1), repeat=2):
            den = (zero + j + ej - i - ei) / N
            if den != 0:
                u = (s[i] - s[j]) / den
                if 0 < u < 1:
                    ruptures.add(u)
    ruptures = sorted(ruptures)
    Ls = [longueur_coupe(s, u, N) for u in ruptures]
    A = sum((ruptures[t + 1] - ruptures[t]) * (Ls[t] + Ls[t + 1]) / 2 for t in range(len(ruptures) - 1))
    return 2 * A, P


def borne_F(P):
    return P[-1] ** 2 + 2 * sum((P[j] - P[j + 1]) ** 2 for j in range(len(P) - 1))


def telescope(k, exact=True):
    return [Fr(k + 2 - j, k + 3 - j) if exact else (k + 2 - j) / (k + 3 - j) for j in range(1, k + 1)]


ligne("### 2.1 Une fusion\n")
ligne("| α | aire exacte (rapport au triangle) | 3α² − 4α + 2 |")
ligne("|---|---|---|")
UNE = []
for a in (Fr(1, 2), Fr(3, 5), Fr(2, 3), Fr(3, 4), Fr(4, 5), Fr(19, 20)):
    A_, _ = aire_exacte([a])
    UNE.append(A_ == 3 * a * a - 4 * a + 2)
    ligne(f"| {a} | {A_} | {3 * a * a - 4 * a + 2} |")
ligne(f"\nToutes égales : {'oui' if all(UNE) else 'non'}. Le minimum est 2/3, en α = 2/3 : un cœur α² = 4/9 et deux"
      " oreilles (1 − α)² = 1/9.\n")

ligne("### 2.2 La borne cœur + oreilles, pour tous les rapports\n")
rng_p = np.random.default_rng(5)
NUAGE, EGAUX, PIRE, UN_SEUL = [], 0, Fr(-1), 0
for _ in range(80):
    k = int(rng_p.integers(1, 6))
    al = [Fr(int(x), 64) for x in rng_p.integers(32, 65, size=k)]
    A_, P_ = aire_exacte(al)
    B_ = borne_F(P_)
    NUAGE.append((float(B_), float(A_), k))
    EGAUX += A_ == B_
    UN_SEUL += k == 1
    PIRE = max(PIRE, A_ - B_)
ligne(f"- 80 arbres au hasard (k = 1 à 5, rapports α = m/64 entre ½ et 1), aires exactes en fractions :"
      f" max(aire − F) = {PIRE} ; égalité dans {EGAUX} cas, dont les {UN_SEUL} arbres à une seule fusion.")
TEL = {}
for k in range(1, 6):
    A_, P_ = aire_exacte(telescope(k))
    TEL[k] = (A_, borne_F(P_))
ligne("- Rapports télescopiques (k + 1)/(k + 2), …, 3/4, 2/3 : aire exacte = F = 2/(k + 2) :"
      f" {', '.join(f'k = {k} : {TEL[k][0]}' for k in TEL)}.\n")

ligne("### 2.3 Le plateau, en entiers\n")
ligne("Aux rapports télescopiques, en unités v = u(k + 2) et largeur × N(k + 2), la coupe est l'union des 2^k intervalles"
      " [c_i, c_i + v], c_i = Σ_j b_j(i)·2^j·(v − j − 2). Le lemme : sa longueur vaut 2^k·v, puis 2^k (plateau), puis"
      " 2^k·(v − k). Vérification exacte (en entiers) sur la grille v = p/48 :\n")


def plateau_ecarts(k, q=48):
    N = 2 ** k
    idx = np.arange(N)
    bits = ((idx[:, None] >> np.arange(k)[None, :]) & 1).astype(np.int64)
    w = (2 ** np.arange(k)).astype(np.int64)
    mauvais = 0
    for p in range(0, (k + 2) * q + 1):
        c = bits @ (w * (p - (np.arange(k) + 2) * q))
        lo = np.sort(c)
        tot = p + int(np.sum(np.minimum(np.diff(lo), p)))
        v = Fr(p, q)
        g = v if v <= 1 else (Fr(1) if v <= k + 1 else v - k)
        mauvais += Fr(tot, q) != N * g
    return mauvais, (k + 2) * q + 1


ligne("| k | branches | points de la grille | écarts au lemme |")
ligne("|---:|---:|---:|---:|")
PLAT = {}
for k in (1, 2, 3, 4, 6, 8, 10, 12, 14, 16):
    PLAT[k] = plateau_ecarts(k)
    ligne(f"| {k} | {ent(2 ** k)} | {PLAT[k][1]} | {PLAT[k][0]} |")


def fentes(k, v):
    """Composantes de la coupe à la profondeur v (unités du lemme), avec les bits hauts de leurs branches."""
    N = 2 ** k
    idx = np.arange(N)
    bits = (idx[:, None] >> np.arange(k)[None, :]) & 1
    c = bits @ (2.0 ** np.arange(k) * (v - np.arange(k) - 2))
    o = np.argsort(c)
    lo = c[o]
    comps, cl, cr, lab = [], lo[0], lo[0] + v, {int(idx[o[0]]) >> int(v)}
    for t in range(1, N):
        if lo[t] > cr + 1e-9:
            comps.append((cl, cr, lab))
            cl, cr, lab = lo[t], lo[t] + v, set()
        cr = max(cr, lo[t] + v)
        lab.add(int(idx[o[t]]) >> int(v))
    comps.append((cl, cr, lab))
    return comps


ligne("\nLes fentes (k = 4) : à la profondeur v entre j et j + 1, combien de morceaux, de quelle largeur, et quels bits"
      " hauts (b_j … b_(k−1)) chacun porte :\n")
ligne("| v | morceaux | largeurs | bits hauts, de gauche à droite |")
ligne("|---|---:|---|---|")
for v in (0.5, 1.5, 2.5, 3.5, 4.5, 5.5):
    cps = fentes(4, v)
    larg = sorted({round(float(c[1] - c[0]), 6) for c in cps})
    labs = [sorted(c[2]) for c in cps]
    ligne(f"| {fr(v, '{:.1f}')} | {len(cps)} | {', '.join(fr(x_, '{:g}') for x_ in larg)} |"
          f" {', '.join(str(lb[0]) if len(lb) == 1 else str(lb) for lb in labs)} |")
ligne("\nChaque combinaison des bits hauts apparaît une fois et une seule, dans l'ordre binaire décroissant : chaque coupe"
      " est un diagramme de Venn à une dimension.\n")

ligne("### 2.4 Kakeya au grain δ : la fenêtre démontrée\n")
ligne("Avec N éventails d'ouverture π/N (hauteur 1, aire tan(π/2N) chacun), des arbres télescopiques à 2^k branches et un"
      " tube 1 × δ par direction (Partie XXVI) : aire ≤ N·[tan(π/2N)·2/(k + 2) + 2^k·δ/cos(π/2N)]. En bas, la borne de"
      " Córdoba π/(1 + 2γ + 2 ln(2/δ)).\n")


def borne_haut(N, k, ld):
    x = k * math.log(2) - ld
    return math.inf if x > 50 else N * (math.tan(math.pi / (2 * N)) * 2 / (k + 2)
                                          + math.exp(x) / math.cos(math.pi / (2 * N)))


def meilleur_k(N, ld):
    k0 = max(0, int((ld - math.log(N)) / math.log(2) - 2 * math.log2(max(ld, 2))))
    return min((borne_haut(N, k, ld), k) for k in range(max(0, k0 - 60), k0 + 60))


def meilleur(ld, Ns=range(2, 400)):
    return min((*meilleur_k(N, ld), N) for N in Ns)


def bas(ld):
    return math.pi / (1 + 2 * GAM + 2 * (math.log(2) + ld))


CONS26 = {1: 1.179, 2: 0.643, 3: 0.430, 4: 0.318, 5: 0.250}  # partie XXVI : unions calculées (3 éventails)
ligne("| grain δ | borne du bas (Córdoba) | haut, 3 éventails (hexagone) | haut, 17 éventails | meilleur N | haut ÷ bas |"
      " partie XXVI (calculé) |")
ligne("|---|---|---|---|---|---|---|")
FEN = {}
for e in (1, 2, 3, 4, 5, 10, 20, 49, 50, 51, 52, 53, 54, 55, 100):
    ld = e * math.log(10)
    b3, b17, bb = meilleur_k(3, ld), meilleur_k(17, ld), meilleur(ld)
    FEN[e] = (bas(ld), b3, b17, bb)
    ligne(f"| 10⁻{sup(e)} | {fr(bas(ld), '{:.5f}')} | {fr(b3[0], '{:.5f}')} (k = {b3[1]}) | {fr(b17[0], '{:.5f}')}"
          f" (k = {b17[1]}) | {fr(bb[0], '{:.5f}')} (N = {bb[2]}, k = {bb[1]}) | {fr(bb[0] / bas(ld), '{:.3f}')} |"
          f" {fr(CONS26[e], '{:.3f}') if e in CONS26 else '—'} |")
ligne(f"\n- Constantes (aire × ln(1/δ) quand δ → 0) : en bas π/2 = {fr(math.pi / 2, '{:.4f}')} ; en haut π·ln 2 ="
      f" {fr(math.pi * math.log(2), '{:.4f}')} avec assez d'éventails, 2√3·ln 2 = {fr(2 * R3 * math.log(2), '{:.4f}')}"
      f" avec 3. Rapport limite 2 ln 2 = {fr(2 * math.log(2), '{:.4f}')}.")
ligne("- Le coefficient 2N·tan(π/2N) est l'aire du polygone régulier à 2N côtés circonscrit au cercle unité :\n")
ligne("| N éventails | polygone circonscrit | 2N·tan(π/2N) | écart à π | π²/(12N²) |")
ligne("|---:|---|---|---|---|")
for N, nom in ((2, "carré"), (3, "hexagone"), (4, "octogone"), (6, "dodécagone"), (12, "24 côtés"), (17, "34 côtés"),
               (100, "200 côtés")):
    a_ = 2 * N * math.tan(math.pi / (2 * N))
    ligne(f"| {N} | {nom} | {fr(a_, '{:.6f}')} | {fr((a_ - math.pi) / math.pi * 100, '{:.4f}')} % |"
          f" {fr(math.pi ** 2 / (12 * N * N) * 100, '{:.4f}')} % |")
ligne("")

# ===========================================================================
# 3. Le Venn à 17
# ===========================================================================
ligne("## 3. Le Venn à 17\n")
ligne("### 3.1 Henderson : n doit être premier\n")


def premier(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


HEND = all((all(math.comb(n, k) % n == 0 for k in range(1, n)) == premier(n)) for n in range(2, 201))
ligne(f"- n divise C(n, k) pour tout 0 < k < n ⟺ n premier : {'vrai' if HEND else 'faux'} pour n ≤ 200.")
ORB = [math.comb(17, k) // 17 for k in range(1, 17)]
ligne(f"- 2¹⁷ − 2 = {ent(2 ** 17 - 2)} = 17 × {ent((2 ** 17 - 2) // 17)} (Fermat) ; régions dans exactement k ensembles,"
      " par orbites de 17 :\n")
ligne("| k | C(17, k) | orbites |")
ligne("|---:|---:|---:|")
for k in range(1, 17):
    ligne(f"| {k} | {ent(math.comb(17, k))} | {ent(ORB[k - 1])} |")
ligne(f"\n- Total : {ent(sum(ORB))} orbites ; colliers binaires de 17 perles : {ent(sum(ORB) + 2)}.")
V17 = 2 ** 17 - 2
ligne(f"- Venn simple à n courbes (Euler, V − E + F = 2 avec E = 2V et F = 2ⁿ) : V = 2ⁿ − 2 croisements. Pour 17 :"
      f" {ent(V17)} croisements = 17 × {ent(V17 // 17)}, {ent(2 * V17)} arcs, {ent(2 * V17 // 17)} croisements sur"
      " chaque courbe.\n")

ligne("### 3.2 Un Venn symétrique à 5 ellipses, vérifié\n")
ELL = (1.06, 0.50, 0.36, 2.95)  # demi-axes, distance du centre, inclinaison du grand axe (trouvés par recherche)


def codes_venn(A, B, d, th, n=5, M=900):
    Lm = d + A + 0.15
    x = np.linspace(-Lm, Lm, M)
    X, Y = np.meshgrid(x, x)
    C = np.zeros(X.shape, int)
    for j in range(n):
        p = 2 * math.pi * j / n
        u = (X - d * math.cos(p)) * math.cos(p + th) + (Y - d * math.sin(p)) * math.sin(p + th)
        w = -(X - d * math.cos(p)) * math.sin(p + th) + (Y - d * math.sin(p)) * math.cos(p + th)
        C |= ((u / A) ** 2 + (w / B) ** 2 < 1).astype(int) << j
    return C, x


def croisements_ellipses(A, B, d, th, n=5, M=200000):
    """Compte les points où deux bords se croisent (changements de signe le long de chaque ellipse), par paire."""
    t = np.linspace(0, 2 * math.pi, M, endpoint=False)
    par_paire = {}
    for j in range(n):
        p = 2 * math.pi * j / n
        xs = d * math.cos(p) + A * np.cos(t) * math.cos(p + th) - B * np.sin(t) * math.sin(p + th)
        ys = d * math.sin(p) + A * np.cos(t) * math.sin(p + th) + B * np.sin(t) * math.cos(p + th)
        for i in range(n):
            if i == j:
                continue
            q = 2 * math.pi * i / n
            u = (xs - d * math.cos(q)) * math.cos(q + th) + (ys - d * math.sin(q)) * math.sin(q + th)
            w = -(xs - d * math.cos(q)) * math.sin(q + th) + (ys - d * math.sin(q)) * math.cos(q + th)
            f_ = (u / A) ** 2 + (w / B) ** 2 - 1
            cle = tuple(sorted((i, j)))
            par_paire[cle] = par_paire.get(cle, 0) + int(np.sum(np.sign(f_) != np.sign(np.roll(f_, 1))))
    return {c: v // 2 for c, v in par_paire.items()}


CV, XV = codes_venn(*ELL)
REG = {}
for code in range(32):
    lab_, nb = ndimage.label(CV == code)
    tailles = ndimage.sum(np.ones_like(CV), lab_, range(1, nb + 1))
    REG[code] = int(np.sum(tailles > 3))  # un pixel isolé près d'un croisement n'est pas une région
OK_VENN = len(np.unique(CV)) == 32 and all(nb == 1 for nb in REG.values())
CROIX = croisements_ellipses(*ELL)
NCROIX = sum(CROIX.values())
VOIS = sorted({v for (i, j), v in CROIX.items() if (j - i) % 5 in (1, 4)})
LOIN = sorted({v for (i, j), v in CROIX.items() if (j - i) % 5 in (2, 3)})
ligne(f"- Ellipses de demi-axes {fr(ELL[0], '{:g}')} et {fr(ELL[1], '{:g}')}, centres à {fr(ELL[2], '{:g}')} du centre,"
      f" inclinées de {fr(ELL[3], '{:g}')} rad, tournées de 72° : {len(np.unique(CV))} régions sur 32, chacune d'un seul"
      f" morceau : {'oui' if OK_VENN else 'non'} (grille 900 × 900).")
ligne(f"- Croisements : {NCROIX} = 2⁵ − 2, en {NCROIX // 5} orbites de 5 ({'/'.join(map(str, VOIS))} par paire de voisines,"
      f" {'/'.join(map(str, LOIN))} par paire éloignée). Le contour est connexe, donc Euler donne 2·30 − 30 + 2 = 32 faces : avec les 32 codes présents,"
      " chaque combinaison est une seule région (le Venn est simple).")
ligne("- Régions hors centre et dehors : 30 = 5 × 6 (C(5, k)/5 = 1, 2, 2, 1).\n")

ligne("### 3.3 Le diaphragme à 17 lames\n")


def polygone(N, R=1.0, phase=math.pi / 2):
    t = phase + 2 * math.pi * np.arange(N) / N
    return np.c_[R * np.cos(t), R * np.sin(t)]


def tf_polygone(P, KX, KY):
    """Transformée de Fourier exacte de l'indicatrice d'un polygone (théorème de la divergence) :
    F(k) = (i/|k|²) Σ_côtés (k·n) ℓ e^(−ik·m) sinc(k·t ℓ/2)."""
    Fk = np.zeros(KX.shape, complex)
    for j in range(len(P)):
        a, b = P[j], P[(j + 1) % len(P)]
        e = b - a
        lg = math.hypot(*e)
        t = e / lg
        n = np.array([t[1], -t[0]])
        m = (a + b) / 2
        Fk += (KX * n[0] + KY * n[1]) * lg * np.exp(-1j * (KX * m[0] + KY * m[1])) * np.sinc((KX * t[0] + KY * t[1]) * lg
                                                                                               / (2 * math.pi))
    return 1j * Fk / (KX ** 2 + KY ** 2)


def aigrettes(N, K=400.0, nth=36000):
    P = polygone(N)
    th = np.linspace(0, 2 * math.pi, nth, endpoint=False)
    rs = np.linspace(0.8 * K, 1.2 * K, 41)
    Th, Rs = np.meshgrid(th, rs)
    prof = (np.abs(tf_polygone(P, Rs * np.cos(Th), Rs * np.sin(Th))) ** 2 * Rs ** 2).mean(0)
    loc = (prof > np.roll(prof, 1)) & (prof >= np.roll(prof, -1)) & (prof > 0.2 * prof.max())
    return int(loc.sum()), th[loc], th, prof


P17 = polygone(17)
AIRE17 = 0.5 * abs(float(np.sum(P17[:, 0] * np.roll(P17[:, 1], -1) - P17[:, 1] * np.roll(P17[:, 0], -1))))
F0 = float(tf_polygone(P17, np.array([[1e-4]]), np.array([[0.0]])).real[0, 0])
LUM17 = 17 / (2 * math.pi) * math.sin(2 * math.pi / 17)
ligne(f"- Lumière : (N/2π)·sin(2π/N) = {fr(LUM17, '{:.6f}')} du cercle (partie II) ; il manque {fr((1 - LUM17) * 100, '{:.3f}')} %"
      f" (2π²/(3N²) = {fr(200 * math.pi ** 2 / (3 * 17 ** 2), '{:.3f}')} %, les ménisques de la partie V), soit"
      f" {fr(math.log2(1 / LUM17), '{:.4f}')} cran.")
ligne(f"- Contrôle de la transformée exacte : F(0) = {fr(F0, '{:.6f}')}, aire du 17-gone {fr(AIRE17, '{:.6f}')}.\n")
ligne("| lames N | aigrettes comptées | attendu (N pair : N ; impair : 2N) |")
ligne("|---:|---:|---:|")
PICS = {}
for N in (5, 6, 7, 8, 16, 17, 18):
    PICS[N] = aigrettes(N)
    ligne(f"| {N} | {PICS[N][0]} | {N if N % 2 == 0 else 2 * N} |")
ang17 = PICS[17][1]
ECARTS17 = np.degrees(np.diff(np.r_[ang17, ang17[0] + 2 * math.pi]))
ligne(f"\n- Les 34 aigrettes du 17-gone sont espacées de {fr(ECARTS17.min(), '{:.3f}')}° à {fr(ECARTS17.max(), '{:.3f}')}°"
      f" (180/17 = {fr(180 / 17, '{:.3f}')}°).")
ligne("- Même parité pour le diaphragme de Perron : N éventails posés comme N lames (angles 2πj/N) couvrent chaque"
      " direction modulo π une fois si N est impair ; pour N pair, la moitié des directions deux fois et l'autre jamais.")
for N in (16, 17):
    dirs = sorted({(2 * j) % N for j in range(N)})
    ligne(f"  - N = {N} : {len(dirs)} directions distinctes sur {N}.")
ligne("")

ligne("### 3.4 Gauss, i et la période de 1/17\n")
c17 = (-1 + math.sqrt(17) + math.sqrt(34 - 2 * math.sqrt(17))
       + 2 * math.sqrt(17 + 3 * math.sqrt(17) - math.sqrt(34 - 2 * math.sqrt(17)) - 2 * math.sqrt(34 + 2 * math.sqrt(17)))) / 16
ligne(f"- cos(2π/17) = {fr(math.cos(2 * math.pi / 17), '{:.15f}')} ; formule de Gauss : {fr(c17, '{:.15f}')}.")
ORD = {b: next(e for e in range(1, 17) if pow(b, e, 17) == 1) for b in (2, 3, 4, 10)}
ligne(f"- Ordres modulo 17 : 2 → {ORD[2]}, 3 → {ORD[3]} (racine primitive), 4 → {ORD[4]}, 10 → {ORD[10]}.")
ligne(f"- 4² = 16 ≡ −1 : 4 ≡ i (mod 17), car 17 = 4² + 1 (comme 101 = 10² + 1 à la partie XIX) ; 2⁴ ≡ −1 ;"
      f" 10⁴ ≡ {pow(10, 4, 17)} ≡ i ; 10⁸ ≡ {fr(pow(10, 8, 17) - 17, '{:d}')} (mod 17).")
per = str(10 ** 16 // 17).zfill(16)
moit = int(per[:8]) + int(per[8:])
quarts = sum(int(per[4 * q:4 * q + 4]) for q in range(4))
ligne(f"- 1/17 = 0,({per}) : période 16 ; {per[:8]} + {per[8:]} = {moit} (Midy, car 10⁸ ≡ −1) ; par quarts :"
      f" {' + '.join(per[4 * q:4 * q + 4] for q in range(4))} = {ent(quarts)} = 2 × 9 999.")
GEN = [pow(3, j, 17) for j in range(16)]
z17 = np.exp(2j * math.pi * np.arange(17) / 17)
ligne("- Périodes de Gauss (racine primitive 3) : on coupe les 16 racines en 2, 4, 8 classes ; chaque étape est une"
      " racine carrée.")
for niv in (2, 4, 8):
    eta = [sum(z17[GEN[j]] for j in range(c, 16, niv)).real for c in range(niv)]
    ligne(f"  - {niv} classes de {16 // niv} : " + ", ".join(fr(x_, "{:.6f}") for x_ in eta))
ligne(f"  - niveau 2 : (−1 ± √17)/2 = {fr((-1 + math.sqrt(17)) / 2, '{:.6f}')}, {fr((-1 - math.sqrt(17)) / 2, '{:.6f}')}.\n")

DUREE_CALC = time.time() - T0
ligne(f"(calculs : {fr(DUREE_CALC, '{:.0f}')} s)")
with open(os.path.join(ICI, "..", "resultats", "octaedre_perron_venn.md"), "w") as fh:
    fh.write("\n".join(md) + "\n")
print(f"calculs : {DUREE_CALC:.1f} s")
T1 = time.time()


# ===========================================================================
# Figures
# ===========================================================================
def legende(ax, texte, y=-0.13, largeur=86):
    """Légende sous le panneau, recoupée en lignes de longueur fixe (pour ne pas déborder sur le voisin)."""
    texte = textwrap.fill(" ".join(texte.split("\n")), largeur)
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


BOITE = dict(boxstyle="round,pad=0.35", fc=F.SURF, ec=F.BASE)


def dessin_solide(ax, P, E, u, col, lw=1.6, cach=True):
    """Arêtes d'un solide convexe vu le long de u (les arêtes cachées en pointillés)."""
    a, b = repere(u)
    Q = np.c_[P @ a, P @ b]
    prof = P @ u
    hv = ConvexHull(Q)
    for i, j in E:
        m = (P[i] + P[j]) / 2
        # caché si le milieu est derrière le centre et pas sur le contour
        cyc = list(hv.vertices)
        contour = i in cyc and j in cyc and (cyc.index(i) - cyc.index(j)) % len(cyc) in (1, len(cyc) - 1)
        devant = (m @ u) > -1e-9 or contour
        if not devant and not cach:
            continue
        ax.plot(Q[[i, j], 0], Q[[i, j], 1], color=col, lw=lw if devant else 0.9, ls="-" if devant else (0, (3, 3)),
                alpha=1 if devant else 0.55, zorder=4 if devant else 2)
    return Q, prof


# --------------------------- ac1 : l'octaèdre ---------------------------
fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.16, hspace=0.34)

# a) même hexagone
ax = fig.add_subplot(gs[0, 0])
schema(ax, (-1.05, 1.05), (-1.0, 1.05))
Qc, _ = dessin_solide(ax, CUBE, E_CUBE, N3, F.BLEU)
Qo, _ = dessin_solide(ax, OCT, E_OCT, N3, F.ORANGE, lw=1.4)
F.cercle(ax, (0, 0), R2 / 2, color=VERT, lw=2.2, zorder=5)
for q in Qo:
    F.point(ax, q[0], q[1], F.INK, 5.5)
ax.text(0, -0.96, "même contour : l'hexagone ; cercle inscrit = ombre de la sphère médiane (rayon √2/2)",
        ha="center", fontsize=8.6, color=F.INK2)
ax.text(-1.0, 0.95, "cube", color=F.BLEU, fontsize=10, fontweight="bold")
ax.text(-1.0, 0.86, "octaèdre", color=F.ORANGE, fontsize=10, fontweight="bold")
ax.set_title("a)  Le cube et l'octaèdre, vus le long de (1, 1, 1)")
legende(ax, "L'octaèdre |x| + |y| + |z| ≤ 1 est le polaire du cube [−½, ½]³ par la sphère médiane : leurs 12 milieux"
        " d'arêtes sont les mêmes points, et leurs arêtes s'y croisent à angle droit. Le long d'une grande diagonale, chaque"
        " sommet de l'octaèdre tombe sur un sommet du cube : les deux ombres sont le même hexagone.", y=-0.03)

# b) le long de l'axe d'ordre 4 : le diamant aztèque
ax = fig.add_subplot(gs[0, 1])
schema(ax, (-1.12, 1.12), (-1.12, 1.12))
ax.add_patch(Polygon([(1, 0), (0, 1), (-1, 0), (0, -1)], closed=True, fc=(*to_rgb(F.ORANGE), 0.12), ec=F.ORANGE,
                     lw=2))
ax.add_patch(Polygon([(0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5), (0.5, -0.5)], closed=True, fc=(*to_rgb(F.BLEU), 0.12),
                     ec=F.BLEU, lw=2))
F.cercle(ax, (0, 0), R2 / 2, color=VERT, lw=2.4, zorder=5)
for sx, sy in itertools.product((-0.5, 0.5), repeat=2):
    F.point(ax, sx, sy, VERT, 7)
ax.annotate("(½, ½) : milieu commun d'une arête\ndu cube et d'une arête de l'octaèdre", (0.5, 0.5), (1.1, 1.08),
            fontsize=8.4, color=F.INK2, ha="right", va="top",
            arrowprops=dict(arrowstyle="->", color=F.INK2, lw=0.9, shrinkB=5))
ax.text(0, -0.08, "ombre du cube\n(aire 1)", ha="center", va="top", fontsize=9, color=F.BLEU)
ax.text(0.0, -1.08, "ombre de l'octaèdre : le diamant aztèque (aire 2)", ha="center", fontsize=9, color=F.ORANGE)
ax.text(-1.11, 1.11, "cercle arctique des dominos\n= ombre de la sphère médiane", fontsize=8.8, color=VERT, va="top")
ax.set_title("b)  Le long d'un axe d'ordre 4 : le losange")
legende(ax, "Vu d'en haut, l'octaèdre est le losange |x| + |y| ≤ 1 des dominos (partie XXVII) et le cube un carré d'aire 1."
        " La sphère médiane se projette sur le cercle de rayon 1/√2, inscrit dans le losange et circonscrit au carré :"
        " c'est le cercle arctique de Jockusch, Propp et Shor. Les deux carrés sont à un cran l'un de l'autre (aires 1 et"
        " 2).", y=-0.03)

# c) carte du rapport des ombres
ax = fig.add_subplot(gs[0, 2])
lon = np.linspace(-math.pi, math.pi, 721)
zz = np.linspace(-1, 1, 361)
LON, ZZ = np.meshgrid(lon, zz)
Rr = np.sqrt(1 - ZZ ** 2)
UU = np.stack([Rr * np.cos(LON), Rr * np.sin(LON), ZZ], -1)
RAP = ombre_oct(UU) / ombre_cube(UU)
cmap = LinearSegmentedColormap.from_list("rap", [F.SURF, "#cde2fb", F.BLEU, "#104281"])
im = ax.pcolormesh(np.degrees(LON), ZZ, RAP, cmap=cmap, vmin=1, vmax=2, shading="auto", rasterized=True)
ax.contour(np.degrees(LON), ZZ, RAP, levels=[1 + 1e-9], colors=[F.ORANGE], linewidths=1.6)
for v_, nom, col in ((N3, "3", F.INK), (N2, "2", VERT), (N4, "4", ROUGE)):
    for s in itertools.product((-1, 1), repeat=3):
        w = v_ * np.array(s)
        for perm in set(itertools.permutations(range(3))):
            ww = w[list(perm)]
            ax.plot(math.degrees(math.atan2(ww[1], ww[0])), ww[2], "o", color=col, ms=4.5, mec=F.SURF, mew=0.8)
cb = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02)
cb.set_label("ombre de l'octaèdre ÷ ombre du cube", color=F.INK2)
ax.set_xlabel("longitude (degrés)")
ax.set_ylabel("z = cos(colatitude)  (carte à aires égales)")
ax.set_xlim(-180, 180)
ax.set_title("c)  Où les deux ombres sont égales")
legende(ax, f"Points noirs : axes d'ordre 3 (les hexagones) ; verts : ordre 2 ; rouges : ordre 4. Blanc (rapport 1), cerné d'orange : les 8 triangles sphériques autour des hexagones, d'angles arccos(1/3) ="
        f" 70,53°, où l'ombre de l'octaèdre max(‖u‖₁, 2‖u‖∞) égale celle du cube ‖u‖₁. Ils couvrent"
        f" 6·arccos(1/3)/π − 2 = {fr(FRAC_TH * 100, '{:.2f}')} % des directions (compté : {fr(FRAC_EGAL * 100, '{:.2f}')} %)."
        " Ailleurs l'octaèdre fait plus d'ombre, jusqu'au double.", y=-0.13)

# d) le cône de lumière
ax = fig.add_subplot(gs[1, 0])
HABS = ndimage.maximum_filter(np.abs(HX), size=3)  # enveloppe locale : efface la parité et les nœuds isolés
LGp = np.log10(HABS + 1e-300)
cmap2 = LinearSegmentedColormap.from_list("onde", ["#0d366b", F.BLEU, "#cde2fb", F.SURF])
im = ax.imshow(np.clip(LGp, -24, -1), origin="lower", extent=(-c0, c0, -c0, c0), cmap=cmap2.reversed(), vmin=-24,
               vmax=-1, interpolation="nearest")
ax.plot([T_ONDE, 0, -T_ONDE, 0, T_ONDE], [0, T_ONDE, 0, -T_ONDE, 0], color=F.ORANGE, lw=1.8)
F.cercle(ax, (0, 0), T_ONDE / R2, color=VERT, lw=2.0)
schema(ax, (-c0, c0), (-c0, c0))
cax = ax.inset_axes([0.9, 0.05, 0.025, 0.3])
cb = fig.colorbar(im, cax=cax)
cax.yaxis.set_ticks_position("left")
cax.set_title("log₁₀|h|", fontsize=8.4, color=F.INK2)
ax.text(-c0 + 8, c0 - 12, f"t = {T_ONDE}\norange : |x| + |y| = t (cône exact)\nvert : rayon t/√2 (vitesse de groupe)",
        fontsize=8.6, va="top", color=F.INK2, bbox=BOITE)
ax.set_title("d)  L'onde de la récurrence de l'octaèdre")
legende(ax, "La récurrence de l'octaèdre linéarisée, h(t + 1) + h(t − 1) = ½[h(x ± 1) + h(y ± 1)], partie d'un point. Elle"
        " remplit le losange un pas par tour, mais elle s'éteint hors du cercle inscrit : les quatre coins entre le cercle"
        " et le losange sont les quatre coins gelés du diamant aztèque.", y=-0.03)

# e) la coupe
ax = fig.add_subplot(gs[1, 1])
xs_ = np.arange(0, T_ONDE + 1)
ax_h = np.abs(HX[c0, c0:c0 + T_ONDE + 1])
env = np.array([np.abs(HX[c0, c0 + max(0, x - 1):c0 + x + 2]).max() for x in xs_])
dg = np.array([np.abs(HX[c0 + d - 1:c0 + d + 2, c0 + d - 1:c0 + d + 2]).max() for d in range(1, T_ONDE // 2 + 1)])
ax.semilogy(xs_ / T_ONDE, np.maximum(env, 1e-80), color=F.BLEU, lw=1.6, label="le long d'un axe (vers un coin)")
ax.semilogy(np.arange(1, T_ONDE // 2 + 1) * R2 / T_ONDE, np.maximum(dg, 1e-80), color=F.ORANGE, lw=1.4,
            label="le long d'une diagonale (vers un côté)")
ax.axvline(1 / R2, color=VERT, lw=1.8, ls="--")
ax.text(1 / R2 - 0.01, 1e-30, "1/√2", color=VERT, fontsize=10, ha="right")
ax.semilogy([1.0], [COIN], "o", color=ROUGE, ms=6)
ax.text(0.97, COIN * 1e5, f"coin : 2⁻²⁴⁰\n= {sci(COIN)}", color=ROUGE, fontsize=8.6, ha="right")
ax.set_ylim(1e-80, 1)
ax.set_xlabel("distance au centre ÷ t")
ax.set_ylabel("|h| (enveloppe)")
ax.legend(loc="lower left", fontsize=8.6)
ax.set_title("e)  La coupe : un mur à t/√2")
legende(ax, f"Dans le cercle, l'onde décroît doucement ; au-delà de t/√2, elle chute en exponentielle. À t = {T_ONDE},"
        f" {fr(PARTS[0.72][0] * 100, '{:.2f}')} % de l'énergie est à moins de 0,72·t, et rien ne dépasse"
        f" {petit(PARTS[0.8][1])} au-delà de 0,8·t. Le long d'une diagonale, le cercle touche le losange : l'onde va jusqu'au"
        " bord.", y=-0.13)

# f) la vitesse de groupe
ax = fig.add_subplot(gs[1, 2])
im = ax.pcolormesh(K1 / math.pi, K2 / math.pi, np.sqrt(V2), cmap=LinearSegmentedColormap.from_list(
    "v", [F.SURF, "#cde2fb", F.BLEU, "#104281"]), vmin=0, vmax=1 / R2, shading="auto", rasterized=True)
ax.plot([-1, 1], [-1, 1], color=F.ORANGE, lw=1.6)
ax.plot([-1, 1], [1, -1], color=F.ORANGE, lw=1.6)
ax.set_aspect("equal")
cb = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02)
cb.set_label("|vitesse de groupe| (max 1/√2)", color=F.INK2)
ax.set_xlabel("k₁ / π")
ax.set_ylabel("k₂ / π")
ax.set_title("f)  La vitesse de groupe ne dépasse jamais 1/√2")
legende(ax, "|∇ω|² = ½ − (cos k₁ − cos k₂)²/(2[4 − (cos k₁ + cos k₂)²]) ≤ ½ : égalité sur les diagonales k₂ = ±k₁"
        " (orange) et près de k = 0 dans toutes les directions. D'où le cercle de rayon t/√2. Le même polynôme,"
        " 1 − (x + 1/x + y + 1/y)z/2 + z², est au dénominateur de la fonction génératrice des dominos.", y=-0.13)
F.sauver(fig, "ac1_octaedre.png")

# --------------------------- ac2 : Perron ---------------------------
fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.18, hspace=0.36)

# a) une fusion
ax = fig.add_subplot(gs[0, 0])
schema(ax, (-0.62, 1.05), (-0.08, 1.12))
al_ = 2 / 3
d_ = 1 - al_
T1g = [(0, 1), (0, 0), (0.5, 0)]
T2g = [(-d_, 1), (0.5 - d_, 0), (1 - d_, 0)]
ax.add_patch(Polygon(T1g, closed=True, fc=F.BLEU, alpha=0.18, ec=F.BLEU, lw=1.6))
ax.add_patch(Polygon(T2g, closed=True, fc=F.ORANGE, alpha=0.18, ec=F.ORANGE, lw=1.6))
ax.add_patch(Polygon([(0, 1 - d_), (0, 0), (1 - d_, 0)], closed=True, fc="none", ec=F.INK, lw=2.2, ls="-"))
ax.add_patch(Polygon([(-d_, 1), (0, 1 - d_), (0, 1 - 2 * d_)], closed=True, fc=ROUGE, alpha=0.35, ec=ROUGE, lw=1.4))
ax.add_patch(Polygon([(0, 1), (0, 1 - d_), (d_, 1 - 2 * d_)], closed=True, fc=ROUGE, alpha=0.35, ec=ROUGE, lw=1.4))
ax.text(0.06, 0.1, "cœur : α² = 4/9", fontsize=10, color=F.INK, fontweight="bold")
ax.text(0.2, 0.84, "oreille\n(1 − α)²", fontsize=9, color=ROUGE)
ax.text(-0.6, 0.55, "oreille\n(1 − α)²", fontsize=9, color=ROUGE)
ax.annotate("", (-d_, 1.04), (0, 1.04), arrowprops=dict(arrowstyle="<->", color=F.INK2))
ax.text(-d_ / 2, 1.06, "glissement 1 − α", ha="center", fontsize=8.6, color=F.INK2)
ax.set_title("a)  Une fusion : un cœur et deux oreilles")
legende(ax, "Deux moitiés de triangle ; on glisse la droite vers la gauche. Leur union est un triangle semblable, rétréci"
        " de α (le cœur), plus deux petites oreilles. Aire exacte : α² + 2(1 − α)² = 3α² − 4α + 2, minimale en α = 2/3,"
        " où elle vaut 2/3 (2 branches de la partie V).", y=-0.02)

# b) l'arbre à 16 branches
ax = fig.add_subplot(gs[0, 1])
KB = 4
sB, PB = decalages(telescope(KB, exact=False))
NB = 2 ** KB
for i in range(NB):
    sq = sB[i]
    ax.add_patch(Polygon([(sq, 1), (sq + i / NB, 0), (sq + (i + 1) / NB, 0)], closed=True, fc=F.BLEU, alpha=0.10,
                         ec=F.BLEU, lw=0.6))
for v in range(1, KB + 2):
    u = v / (KB + 2)
    ax.axhline(1 - u, color=F.GRID, lw=0.8, zorder=0)
    ax.text(0.86, 1 - u + 0.008, f"v = {v}", fontsize=7.8, color=F.MUTED)
for v, col in ((0.5, ROUGE), (1.5, F.ORANGE), (2.5, VERT), (3.5, VIOLET), (4.5, F.INK)):
    u = v / (KB + 2)
    for cl, cr, _ in fentes(KB, v):
        ax.plot([cl / (NB * (KB + 2)), cr / (NB * (KB + 2))], [1 - u, 1 - u], color=col, lw=3.2, solid_capstyle="butt")
ax.set_xlim(-0.5, 1.0)
ax.set_ylim(-0.03, 1.04)
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
for sp_ in ax.spines.values():
    sp_.set_visible(False)
ax.set_title("b)  L'arbre à 16 branches et ses coupes")
legende(ax, "Rapports 5/6, 4/5, 3/4, 2/3. Les traits de couleur sont la coupe à cinq profondeurs (v = u·(k + 2) = 0,5 ;"
        " 1,5 ; 2,5 ; 3,5 ; 4,5) : 16 fentes, puis 8, 4, 2, 1. Les fentes fusionnent deux par deux à chaque niveau entier,"
        " et la longueur totale ne bouge pas.", y=-0.02)

# c) le plateau
ax = fig.add_subplot(gs[0, 2])
for k, col in ((2, F.RAMPE[0]), (4, F.RAMPE[1]), (8, F.RAMPE[2]), (16, F.RAMPE[4])):
    vs = np.linspace(0, k + 2, 400)
    Lv = []
    for v in vs:
        cps = fentes(k, max(v, 1e-9))
        Lv.append(sum(c[1] - c[0] for c in cps) / 2 ** k)
    ax.plot(vs / (k + 2), np.array(Lv) / (k + 2), color=col, lw=2, label=f"k = {k} ({2 ** k} branches)")
    ax.plot([1 / (k + 2), (k + 1) / (k + 2)], [1 / (k + 2), 1 / (k + 2)], color=col, lw=0.8, ls=":")
ax.set_xlabel("profondeur u sous les sommets (0 : sommets, 1 : base)")
ax.set_ylabel("longueur de la coupe (base du triangle = 1)")
ax.legend(loc="upper left", fontsize=8.6)
ax.set_title("c)  La coupe est un plateau à 1/(k + 2)")
legende(ax, "Théorème (démontré au § 2.3 du texte) : la coupe vaut u jusqu'à 1/(k + 2), reste exactement à 1/(k + 2)"
        " jusqu'à (k + 1)/(k + 2), puis suit le cœur. L'aire est donc 1/(k + 2) du carré unité, soit 2/(k + 2) du"
        " triangle : la formule de la partie V, pour tout k.", y=-0.13)

# d) borne et aire
ax = fig.add_subplot(gs[1, 0])
cols_k = {1: F.RAMPE[0], 2: F.RAMPE[1], 3: F.RAMPE[2], 4: F.RAMPE[3], 5: F.RAMPE[4]}
for k in range(1, 6):
    pts_ = [(b_, a_) for b_, a_, kk_ in NUAGE if kk_ == k]
    if pts_:
        ax.plot(*zip(*pts_), "o", color=cols_k[k], ms=5, alpha=0.8, label=f"k = {k}")
for k in TEL:
    ax.plot([float(TEL[k][1])], [float(TEL[k][0])], "*", color=F.ORANGE, ms=13, mec=F.INK, mew=0.6)
ax.plot([0.3, 1.0], [0.3, 1.0], color=F.INK2, lw=1, ls="--")
ax.text(0.84, 0.88, "aire = F", rotation=40, color=F.INK2, fontsize=9)
ax.text(0.3, 0.97, "étoiles : rapports télescopiques\n(aire = F = 2/(k + 2))", color=F.ORANGE, fontsize=9, va="top")
ax.set_xlabel("borne F = P_k² + 2 Σ (P_j − P_(j+1))²")
ax.set_ylabel("aire exacte de l'arbre")
ax.legend(loc="lower right", fontsize=8.6, title="branches 2^k", title_fontsize=8.6)
ax.set_title("d)  La borne cœur + oreilles, pour tous les rapports")
legende(ax, f"80 arbres au hasard, aires calculées exactement en fractions : tous sous la diagonale (max(aire − F) ="
        f" {PIRE}). La borne ne compte jamais trop peu ; elle compte trop quand les oreilles se recouvrent. Son minimum,"
        " 2/(k + 2), est atteint aux seuls rapports télescopiques, où l'arbre l'atteint aussi.", y=-0.13)

# e) les fentes, Venn à une dimension
ax = fig.add_subplot(gs[1, 1])
schema(ax, (-0.02, 1.02), (-0.6, 5.6), egal=False)
for row, v in enumerate((0.5, 1.5, 2.5, 3.5, 4.5)):
    cps = fentes(KB, v)
    lo_, hi_ = min(c[0] for c in cps), max(c[1] for c in cps)
    j = int(v)
    for cl, cr, lab in cps:
        x0, x1 = (cl - lo_) / (hi_ - lo_), (cr - lo_) / (hi_ - lo_)
        ax.add_patch(Polygon([(x0, 4.6 - row), (x1, 4.6 - row), (x1, 5.0 - row), (x0, 5.0 - row)], closed=True,
                             fc=F.RAMPE[min(4, row)], ec=F.SURF, lw=0.8))
        code = format(sorted(lab)[0], f"0{KB - j}b") if KB - j > 0 else "—"
        if KB - j <= 3 or row == 0:
            ax.text((x0 + x1) / 2, 4.55 - row, code, ha="center", va="top", fontsize=7.2 if row == 0 else 8.4,
                    color=F.INK2, rotation=90 if row == 0 else 0)
    ax.text(-0.01, 4.8 - row, f"v = {fr(v, '{:.1f}')}", ha="right", va="center", fontsize=8.6, color=F.INK2)
ax.text(0.5, -0.45, "chaque combinaison des bits hauts une fois, toutes de même largeur, dans l'ordre binaire",
        ha="center", fontsize=8.6, color=F.INK2)
ax.set_title("e)  Chaque coupe est un Venn à une dimension")
legende(ax, "Les fentes de l'arbre à 16 branches, étirées à la même longueur. À la profondeur v entre j et j + 1, il y a"
        " 2^(4 − j) fentes : une par combinaison des bits b_j … b₃ des branches qu'elles contiennent. C'est la propriété"
        " de Venn (chaque combinaison une fois et une seule) sur une droite.", y=-0.02)

# f) la fenêtre de Kakeya
ax = fig.add_subplot(gs[1, 2])
ks = np.arange(1, 61)
lb = np.array([bas(k * math.log(10)) * k * math.log(10) for k in ks])
u3 = np.array([meilleur_k(3, k * math.log(10))[0] * k * math.log(10) for k in ks])
ub = np.array([meilleur(k * math.log(10), Ns=range(2, 120))[0] * k * math.log(10) for k in ks])
ax.plot(ks, lb, color=F.BLEU, lw=2.2, label="borne du bas (Córdoba) : démontrée")
ax.plot(ks, u3, color=F.ORANGE, lw=1.6, ls="--", label="arbres télescopiques, 3 éventails : démontré")
ax.plot(ks, ub, color=F.ORANGE, lw=2.2, label="meilleur nombre d'éventails : démontré")
ax.plot(list(CONS26), [CONS26[k] * k * math.log(10) for k in CONS26], "o", color=F.INK, ms=6,
        label="unions calculées (partie XXVI)")
for yv, txt, col in ((math.pi / 2, "π/2", F.BLEU), (math.pi * math.log(2), "π ln 2", F.ORANGE),
                     (2 * R3 * math.log(2), "2√3 ln 2", F.ORANGE)):
    ax.axhline(yv, color=col, lw=0.8, ls=":")
    ax.text(61.5, yv, txt, color=col, fontsize=8.6, va="center")
ax.axvline(50, color=F.MUTED, lw=1, ls=":")
b50 = FEN[50]
ax.text(49, 3.55, f"10⁻⁵⁰ : aire entre {fr(b50[0], '{:.5f}')}\net {fr(b50[3][0], '{:.5f}')} ({b50[3][2]} éventails)",
        ha="right", fontsize=8.6, color=F.INK2, bbox=BOITE)
ax.set_ylim(1.2, 4.6)
ax.set_xlim(0, 70)
ax.set_xlabel("chiffres du grain : k, avec δ = 10⁻ᵏ")
ax.set_ylabel("aire × ln(1/δ)")
ax.legend(loc="upper right", fontsize=8.2)
ax.set_title("f)  Kakeya au grain δ : la fenêtre démontrée")
legende(ax, "L'aire minimale de N tubes 1 × δ (un par direction) est entre les deux courbes pleines, toutes deux"
        " démontrées. La constante du haut tend vers π·ln 2 = 2,18 quand on multiplie les éventails (le polygone"
        " circonscrit tend vers le cercle), celle du bas vers π/2 = 1,57.", y=-0.13)
F.sauver(fig, "ac2_perron.png")

# --------------------------- ac3 : le Venn à 17 ---------------------------
fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.16, hspace=0.34)

# a) le Venn à 5 ellipses
ax = fig.add_subplot(gs[0, 0])
rang = np.vectorize(lambda c: bin(c).count("1"))(CV)
cmap_r = LinearSegmentedColormap.from_list("rang", [F.SURF, "#cde2fb", F.BLEU, "#104281"], N=6)
ax.imshow(rang, origin="lower", extent=(XV[0], XV[-1], XV[0], XV[-1]), cmap=cmap_r, vmin=0, vmax=5,
          interpolation="nearest")
tt = np.linspace(0, 2 * math.pi, 400)
for j in range(5):
    p = 2 * math.pi * j / 5
    ex = ELL[2] * math.cos(p) + ELL[0] * np.cos(tt) * math.cos(p + ELL[3]) - ELL[1] * np.sin(tt) * math.sin(p + ELL[3])
    ey = ELL[2] * math.sin(p) + ELL[0] * np.cos(tt) * math.sin(p + ELL[3]) + ELL[1] * np.sin(tt) * math.cos(p + ELL[3])
    ax.plot(ex, ey, color=[F.ORANGE, ROUGE, VIOLET, VERT, F.JAUNE][j], lw=1.6)
schema(ax, (XV[0], XV[-1]), (XV[0], XV[-1]))
ax.text(XV[0] + 0.05, XV[-1] - 0.05, "teinte : nombre d'ensembles\n(blanc 0, bleu nuit 5 = le centre)", fontsize=8.6,
        va="top", color=F.INK2, bbox=BOITE)
ax.set_title("a)  Un Venn symétrique à 5 courbes (vérifié)")
legende(ax, f"Cinq ellipses tournées de 72°. Le script vérifie les 32 régions, chacune d'un seul morceau, et compte"
        f" {NCROIX} croisements = 2⁵ − 2 (Euler). Hors du centre et du dehors, 30 = 5 × 6 régions en 6 orbites : c'est"
        " Fermat (2⁵ ≡ 2 mod 5) dessiné. Ton Venn à 17 fait la même chose avec 131 072 régions.", y=-0.02)

# b) les orbites du Venn à 17
ax = fig.add_subplot(gs[0, 1])
ax.bar(range(1, 17), ORB, color=F.BLEU, width=0.75)
for k in range(1, 17):
    ax.text(k, ORB[k - 1] + 25, ent(ORB[k - 1]), ha="center", va="bottom", fontsize=7.6, color=F.INK2, rotation=90)
ax.set_xticks(range(1, 17))
ax.set_xlabel("k : nombre d'ensembles qui contiennent la région")
ax.set_ylabel("formes de régions (orbites de 17)")
ax.set_ylim(0, 2050)
ax.text(0.6, 2010, f"2¹⁷ − 2 = {ent(V17)} = 17 × {ent(V17 // 17)}\n+ le centre (17 ensembles) et le dehors (0)",
        fontsize=9, color=F.INK2, bbox=BOITE, va="top")
ax.set_title("b)  Les 7 710 formes du Venn à 17")
legende(ax, "La rotation de 2π/17 ne laisse fixes que le centre et le dehors : les autres régions vont par 17. Il y a"
        " C(17, k)/17 formes de régions à k ensembles, et 7 710 en tout. Si 17 n'était pas premier, une de ces divisions"
        f" tomberait mal (Henderson, 1963). Un Venn simple à 17 courbes a aussi {ent(V17)} croisements.", y=-0.13)

# c) le diaphragme à 17 lames
ax = fig.add_subplot(gs[0, 2])
schema(ax, (-1.25, 1.25), (-1.25, 1.25))
R_EXT = 1.2
ax.add_patch(Circle((0, 0), R_EXT, fc="#d9d8d2", ec=F.INK2, lw=1.0))
ax.add_patch(Polygon(P17, closed=True, fc=F.SURF, ec="none"))
for j in range(17):
    p1, p2 = P17[j], P17[(j + 1) % 17]
    e = (p2 - p1) / np.linalg.norm(p2 - p1)
    # le bord d'une lame prolonge un côté jusqu'au cercle extérieur
    b_ = float(p2 @ e)
    t_ = -b_ + math.sqrt(b_ * b_ - (float(p2 @ p2) - R_EXT ** 2))
    ax.plot([p1[0], p2[0] + t_ * e[0]], [p1[1], p2[1] + t_ * e[1]], color=F.INK2, lw=0.9)
ax.add_patch(Polygon(P17, closed=True, fc=F.JAUNE, alpha=0.35, ec=F.INK, lw=1.4))
F.cercle(ax, (0, 0), 1.0, color=F.MUTED, lw=1.2, ls="--")
ax.text(0, 0, f"17-gone :\n{fr(LUM17 * 100, '{:.2f}')} % de la\nlumière du cercle", ha="center", va="center",
        fontsize=10, color=F.INK)
ax.set_title("c)  Le diaphragme à 17 lames")
legende(ax, f"Le centre de ton Venn est fixé par la rotation, comme l'ouverture d'un diaphragme à 17 lames. Droites, les"
        f" lames dessinent un 17-gone qui laisse passer {fr(LUM17 * 100, '{:.2f}')} % de la lumière du cercle (partie II) :"
        f" il manque les 17 ménisques de la partie V, {fr((1 - LUM17) * 100, '{:.2f}')} % ≈ 2π²/(3·17²).", y=-0.02)

# d) les aigrettes : image polaire, rayon en échelle log, intensité × |k|² (maximum par anneau, pour ne pas
#    échantillonner les anneaux d'Airy au hasard)
ax = fig.add_subplot(gs[1, 0], projection="polar")
TH_D = np.linspace(0, 2 * math.pi, 1441)
KB_D = np.geomspace(30, 2400, 171)
IMG_D = np.zeros((len(KB_D) - 1, len(TH_D) - 1))
thc = (TH_D[:-1] + TH_D[1:]) / 2
for b in range(len(KB_D) - 1):
    ks_ = np.linspace(KB_D[b], KB_D[b + 1], 10)
    Th_, Ks_ = np.meshgrid(thc, ks_)
    IMG_D[b] = (np.abs(tf_polygone(P17, Ks_ * np.cos(Th_), Ks_ * np.sin(Th_))) ** 2 * Ks_ ** 2).max(0)
LIMG = np.log10(IMG_D / IMG_D.max())
im = ax.pcolormesh(TH_D, np.log10(KB_D), LIMG, cmap=LinearSegmentedColormap.from_list(
    "d", ["#0b0b0b", "#104281", F.BLEU, "#cde2fb", F.SURF]), vmin=float(np.percentile(LIMG, 2)), vmax=0,
    shading="flat", rasterized=True)
ax.set_rorigin(math.log10(KB_D[0]) - 0.15)
ax.set_ylim(math.log10(KB_D[0]), math.log10(KB_D[-1]))
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
ax.spines["polar"].set_visible(False)
ax.set_title("d)  Ses aigrettes : 34, pas 17", pad=12)
legende(ax, "La figure de diffraction du 17-gone, calculée exactement (somme sur les côtés), vue de loin : rayon en échelle"
        " logarithmique (de 30 à 2 400 fois l'inverse du rayon d'ouverture), intensité × |k|². Près du centre, les anneaux"
        " du cercle ; plus loin, les aigrettes. Chaque côté en envoie une de part et d'autre ; 17 est impair, donc aucun"
        " côté n'est parallèle à un autre : 34 aigrettes, espacées de 180°/17.", y=-0.04)

# e) le profil angulaire
ax = fig.add_subplot(gs[1, 1])
for N, col, dec in ((16, F.ORANGE, 0.0), (17, F.BLEU, 1.2)):
    _, _, th_, prof_ = PICS[N]
    ax.plot(np.degrees(th_), prof_ / prof_.max() + dec, color=col, lw=1.2)
    ax.text(362, dec + 0.5, f"N = {N} :\n{PICS[N][0]} aigrettes", color=col, fontsize=9.5, va="center")
ax.set_xlim(0, 360)
ax.set_xticks(range(0, 361, 45))
ax.set_yticks([])
ax.set_xlabel("angle autour du centre de la figure (degrés)")
ax.set_title("e)  Pair ou impair : N ou 2N aigrettes")
legende(ax, "Intensité à grande distance, tour complet. Avec 16 lames, les côtés opposés sont parallèles et leurs"
        " aigrettes se superposent : 16. Avec 17, elles se croisent : 34. Le script trouve aussi 10 pour 5, 6 pour 6,"
        " 14 pour 7, 8 pour 8 et 18 pour 18 (la règle de la partie II).", y=-0.13)

# f) le diaphragme de Perron
ax = fig.add_subplot(gs[1, 2])
schema(ax, (-1.42, 1.42), (-1.42, 1.42))
KP = 3
NP = 2 ** KP
demi = math.tan(math.pi / 34)
sP, _ = decalages(telescope(KP, exact=False))
r0 = 0.32
for j in range(17):
    ang = math.pi / 2 + 2 * math.pi * j / 17
    ca, sa = math.cos(ang), math.sin(ang)
    for i in range(NP):
        # branche i dans le repère local : sommet (x, 0) près du centre, base à la hauteur 1 (vers l'extérieur)
        hs_l = np.array([0.0, 1.0, 1.0])
        # triangle rectangle de base [0, 1] → éventail isocèle de demi-ouverture π/34 : x ↦ 2·demi·x − demi·u
        xs_l = np.array([sP[i], sP[i] + i / NP, sP[i] + (i + 1) / NP]) * 2 * demi - demi * hs_l
        pts = [(r0 * ca + h_ * ca - x_ * sa, r0 * sa + h_ * sa + x_ * ca) for x_, h_ in zip(xs_l, hs_l)]
        ax.add_patch(Polygon(pts, closed=True, fc=F.BLEU if j % 2 == 0 else F.ORANGE, alpha=0.16, ec="none"))
F.cercle(ax, (0, 0), r0, color=F.MUTED, lw=0.8, ls=":")
ax.text(0, -1.41, f"17 arbres de Perron à {NP} branches, ouverture π/17, posés comme les 17 lames (angles 2πj/17)",
        fontsize=8.4, color=F.INK2, ha="center", va="top")
ax.set_title("f)  Le diaphragme de Perron à 17 lames")
legende(ax, f"Chaque arbre contient une aiguille dans chaque direction de son éventail de π/17. Posés aux angles 2πj/17,"
        f" les 17 éventails couvrent chaque direction une fois, parce que 17 est impair (la même parité que les"
        f" aigrettes). Avec des arbres plus fins, c'est la meilleure construction démontrée à 10⁻⁵⁰ :"
        f" {fr(FEN[50][2][0], '{:.4f}')} avec 17 éventails.", y=-0.02)
F.sauver(fig, "ac3_venn17.png")
print(f"figures : {time.time() - T1:.1f} s ; total : {time.time() - T0:.1f} s")
