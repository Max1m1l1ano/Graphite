"""
Partie XV : la grille décalée, où la chèvre retrouve son simplexe. Tous les paramètres ensemble.

    python3 scripts/grille_decalee.py        # ≈ 30 s

Écrit resultats/grille_decalee.md et figures/o1_grille_decalee.png.

1. La grille décalée d'une demi-maille (le réseau A_n) : la grille cubique de dimension n+1 coupée en diagonale. Sa maille
   est le simplexe régulier de la partie VI, d'arête s(n) = √(2n/(n+1)) à hauteur 1.
2. La corde de la chèvre et la maille : le ménisque, et la meilleure distance offerte par chaque grille.
3. La chèvre comptée sur la grille : à partir de combien de points la grille voit le ménisque.
4. Les dimensions d'or de la grille décalée (√5, 2φ, φ³), et la carte de toutes les dimensions particulières.
5. L'aiguille sur la grille décalée : les entiers d'Eisenstein, le demi-cercle et l'hexagone ; l'échantillonnage.
"""

import itertools
import logging
import math
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Polygon
from scipy.optimize import brentq, minimize_scalar
from scipy.special import betainc

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
PHI = (1 + 5 ** 0.5) / 2
ROUGE = "#d0342c"
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


def part(n, r):
    """Part de la boule unité de dimension réelle n broutée avec la corde r (bêta incomplète régularisée)."""
    c1 = 1 - r * r / 2
    I1 = betainc((n + 1) / 2, 0.5, 1 - c1 * c1)
    return (I1 + r ** n * betainc((n + 1) / 2, 0.5, 1 - r * r / 4)) / 2


def corde(n):
    return brentq(lambda r: part(n, r) - 0.5, 1.0, 2 ** 0.5, xtol=1e-15)


arete = lambda n: math.sqrt(2 * n / (n + 1))  # maille de la grille décalée, rangées (couches) espacées de 1

# ---------------------------------------------------------------------------
# 1. La grille décalée : la grille cubique coupée en diagonale
# ---------------------------------------------------------------------------
ligne("## 1. La grille décalée d'une demi-maille\n")
ligne("En 2D : des rangées espacées de 1 (la distance du piquet P au centre O), une rangée sur deux décalée d'une demi-maille."
      " Si les triangles sont équilatéraux, la maille vaut 2/√3 = 1,154701 : c'est la grille hexagonale, et son triangle est"
      " celui de la chèvre (partie VI : sommet P, base par O).")
ligne("En dimension n : le réseau A_n, la grille cubique de dimension n+1 coupée par le plan x₁ + … + x_{n+1} = 0. Le"
      " simplexe e₁, …, e_{n+1} a l'arête √2 (la diagonale d'une face du cube) et la hauteur √((n+1)/n).\n")
ligne("| n | hauteur du simplexe e₁…e_{n+1} | √((n+1)/n) | arête ramenée à la hauteur 1 | s(n) = √(2n/(n+1)) |")
ligne("|---:|---|---|---|---|")
for n in range(1, 7):
    E = np.eye(n + 1)
    h = np.linalg.norm(E[0] - E[1:].mean(0))
    ligne(f"| {n} | {fr(h, '{:.6f}')} | {fr(math.sqrt((n + 1) / n), '{:.6f}')} | {fr(math.sqrt(2) / h, '{:.6f}')} |"
          f" {fr(arete(n), '{:.6f}')} |")


def theta(points, normes=(2, 4, 6, 8)):
    c = {k: 0 for k in normes}
    for v in points:
        k = sum(x * x for x in v)
        if k in c:
            c[k] += 1
    return c


TA3 = theta(v for v in itertools.product(range(-3, 4), repeat=4) if sum(v) == 0)
TD3 = theta(v for v in itertools.product(range(-3, 4), repeat=3) if sum(v) % 2 == 0)
ligne(f"\nEn 3D, A₃ (dans Z⁴, somme nulle) et la grille cubique à faces centrées (dans Z³, somme paire) ont les mêmes nombres"
      f" de points aux distances² 2, 4, 6, 8 : {list(TA3.values())} et {list(TD3.values())}. C'est l'empilement des couches"
      " hexagonales décalées, le plus dense de l'espace (Kepler).")
ligne("Variante « brique » (grille carrée, une rangée sur deux décalée d'une demi-maille, rangées espacées de 1) : la"
      f" diagonale vaut √5/2 = {fr(5 ** 0.5 / 2, '{:.6f}')} = φ − 1/2, et l'angle au sommet du triangle vaut"
      f" 2·arctan(1/2) = {fr(math.degrees(2 * math.atan(0.5)), '{:.4f}')}°, l'angle du 3-4-5 (partie XIV).")

# ---------------------------------------------------------------------------
# 2. La corde de la chèvre et la maille : le ménisque
# ---------------------------------------------------------------------------
ligne("\n## 2. La corde de la chèvre et la maille décalée : le ménisque\n")
ligne("| n | corde r(n) | maille s(n) | écart r − s | écart relatif |")
ligne("|---:|---|---|---|---|")
TAB = {}
for n in (1.5, 2, 2.5, 3, 4, 6, 10, 20, 50, 100, 400):
    r = corde(n)
    TAB[n] = r
    ligne(f"| {fr(n, '{:g}')} | {fr(r, '{:.6f}')} | {fr(arete(n), '{:.6f}')} | {fr(r - arete(n), '{:.6f}')} |"
          f" {fr(100 * (r - arete(n)) / arete(n), '{:.4f}')} % |")
MREL = minimize_scalar(lambda n: -(corde(n) - arete(n)) / arete(n), bounds=(1.2, 6), method="bounded", options={"xatol": 1e-9})
MABS = minimize_scalar(lambda n: -(corde(n) - arete(n)), bounds=(1.2, 6), method="bounded", options={"xatol": 1e-9})
ligne(f"\nLe ménisque relatif est maximal en n = {fr(MREL.x, '{:.4f}')} ({fr(-100 * MREL.fun, '{:.4f}')} %), l'écart absolu en"
      f" n = {fr(MABS.x, '{:.4f}')} ({fr(-MABS.fun, '{:.6f}')}, partie VI) : entre 2D et 3D. Ensuite les deux décroissent vers 0,"
      " et r comme s tendent vers √2, la diagonale du carré de la grille.\n")
R2, R3 = corde(2), corde(3)
PREC = {"2D : grille carrée, côté 1": (1.0, R2), "2D : grille carrée, diagonale √2": (2 ** 0.5, R2),
        "2D : brique, diagonale √5/2": (5 ** 0.5 / 2, R2), "2D : grille décalée, maille 2/√3": (2 / 3 ** 0.5, R2),
        "3D : grille cubique, côté 1": (1.0, R3), "3D : couches décalées, maille √(3/2)": (1.5 ** 0.5, R3)}
ligne("Meilleures distances offertes par chaque grille (rangées ou couches espacées de 1), comparées à la corde :\n")
ligne("| grille | distance | écart à la corde |")
ligne("|---|---|---|")
for nom, (d, r) in PREC.items():
    ligne(f"| {nom} | {fr(d, '{:.6f}')} | {fr(100 * (d - r) / r, '{:+.3f}')} % |")


# ---------------------------------------------------------------------------
# 3. La chèvre comptée sur la grille : quand la grille voit le ménisque
# ---------------------------------------------------------------------------
def chevre_comptee(pts, N, P):
    """Pré = points à distance ≤ N du centre ; corde = distance au piquet P du point de rang médian, ramenée à N."""
    pre = pts[np.einsum("ij,ij->i", pts, pts) <= N * N + 1e-9]
    k = (len(pre) + 1) // 2
    return np.partition(np.sqrt(((pre - P) ** 2).sum(1)), k - 1)[k - 1] / N, len(pre)


def g_carree(N):
    x = np.arange(-N, N + 1)
    X, Y = np.meshgrid(x, x)
    return np.c_[X.ravel(), Y.ravel()].astype(float)


def g_hex(N):
    J, I = np.meshgrid(np.arange(-int(N / 0.866) - 2, int(N / 0.866) + 3), np.arange(-N - 2, N + 3), indexing="ij")
    return np.c_[(I + 0.5 * (J % 2)).ravel(), (J * math.sqrt(3) / 2).ravel()]


def g_cub(N):
    x = np.arange(-N, N + 1)
    return np.stack(np.meshgrid(x, x, x, indexing="ij"), -1).reshape(-1, 3).astype(float)


def g_cfc(N):
    m = int(N * math.sqrt(2)) + 2
    x = np.arange(-m, m + 1)
    G = np.stack(np.meshgrid(x, x, x, indexing="ij"), -1).reshape(-1, 3)
    return G[G.sum(1) % 2 == 0].astype(float) / math.sqrt(2)


ligne("\n## 3. La chèvre comptée sur la grille : quand la grille voit le ménisque\n")
ligne("Pré de rayon N (en mailles), piquet sur un point de la grille à la distance N : la corde comptée est la distance au"
      " piquet du point de rang médian. La grille « voit » le ménisque quand cette corde est plus près de la chèvre r(n)"
      " que du simplexe s(n).\n")
COMPTE = {}
CAS = {"2D, grille carrée": (g_carree, range(3, 301), lambda N: np.array([N, 0.0]), R2, arete(2)),
       "2D, grille décalée": (g_hex, range(3, 301), lambda N: np.array([N, 0.0]), R2, arete(2)),
       "3D, grille cubique": (g_cub, range(2, 61), lambda N: np.array([N, 0.0, 0.0]), R3, arete(3)),
       "3D, couches décalées": (g_cfc, range(2, 61), lambda N: np.array([N, N, 0.0]) / math.sqrt(2), R3, arete(3))}
ligne("| grille | voit le ménisque | toujours à partir de N | points du pré à ce N | corde comptée = arête du simplexe exactement |")
ligne("|---|---|---|---|---|")
for nom, (gen, Ns, P, r, s) in CAS.items():
    res = [(N,) + chevre_comptee(gen(N), N, P(N)) for N in Ns]
    voit = [abs(c - r) < abs(c - s) for _, c, _ in res]
    dernier = max([N for (N, _, _), v in zip(res, voit) if not v], default=Ns[0] - 1)
    M_seuil = next(M for N, _, M in res if N == dernier + 1)
    exacts = [N for N, c, _ in res if abs(c - s) < 1e-12]
    COMPTE[nom] = (res, voit, dernier + 1, M_seuil, r)
    ligne(f"| {nom} | {fr(100 * np.mean(voit), '{:.0f}')} % des tailles | {dernier + 1} | {M_seuil} |"
          f" {', '.join(f'N = {N}' for N in exacts) if exacts else 'jamais'} |")
ligne("\nLa grille cubique contient la grille à couches décalées (les points de somme paire) : tant qu'elle est grossière, elle"
      " retombe pile sur l'arête du tétraèdre √(3/2), sans voir le ménisque.")

# ---------------------------------------------------------------------------
# 4. Les dimensions d'or de la grille décalée, et la carte de toutes les dimensions
# ---------------------------------------------------------------------------
ligne("\n## 4. Les dimensions d'or de la grille décalée\n")
ligne("s(n)² = 2n/(n+1) : la maille atteint la valeur v en n = v²/(2 − v²), une dimension algébrique. La chèvre atteint la"
      " même valeur un peu plus tôt : le ménisque la décale.\n")
ligne("| valeur de la maille | dimension exacte de la grille décalée | dimension où la chèvre l'atteint | décalage |")
ligne("|---|---|---|---|")
OR = [("2/√3 (grille hexagonale)", 2 / 3 ** 0.5, "2"), ("2 sin 36° (côté du pentagone, √(3 − φ))", 2 * math.sin(math.pi / 5), "√5"),
      ("6/5 (triangle 3-4-5)", 1.2, "18/7"), ("√(3/2) (couches décalées)", 1.5 ** 0.5, "3"), ("2/φ", 2 / PHI, "2φ"),
      ("√φ", PHI ** 0.5, "φ³")]
DOR = []
for nom, v, exact in OR:
    n_s = v * v / (2 - v * v)
    n_r = brentq(lambda n: corde(n) - v, 1.01, 50)
    DOR.append((nom, v, exact, n_s, n_r))
    ligne(f"| {nom} = {fr(v, '{:.6f}')} | {exact} = {fr(n_s, '{:.6f}')} | {fr(n_r, '{:.6f}')} | {fr(n_s - n_r, '{:.4f}')} |")
N_RNPHI = brentq(lambda n: corde(n) ** n - PHI, 2.0, 3.5, xtol=1e-13)
N_PENT = [d for d in DOR if d[2] == "√5"][0][4]
SPECIALES = [  # (n, ce qui s'y passe, partie, nature : grille = dimension exacte de la grille décalée, chevre, autre)
    (2.0, "chèvre 2D sur la grille hexagonale (ménisque 0,35 %)", "VI, XV", "grille"),
    (MREL.x, "ménisque relatif maximal", "XV", "chevre"),
    (N_PENT, "corde = côté du pentagone (φ)", "XII", "chevre"),
    (5 ** 0.5, "maille décalée = côté du pentagone (n = √5)", "XV", "grille"),
    (MABS.x, "ménisque absolu maximal", "VI", "chevre"),
    (2.42216, "déplacement δ maximal", "VI", "chevre"),
    (2.5, "borne 5/2 de Wolff (Kakeya en 3D)", "XIII", "autre"),
    (brentq(lambda n: corde(n) - 1.2, 2.4, 2.6), "corde = 6/5 (triangle 3-4-5)", "XIII", "chevre"),
    (N_RNPHI, "rⁿ = φ (limite de la ligne de Fibonacci)", "XIII", "chevre"),
    (3.0, "chèvre 3D sur les couches décalées (0,31 %)", "VI, XV", "grille"),
    (3.0000853, "δ repasse au niveau de la 2D", "VI", "chevre"),
    (brentq(lambda n: corde(n) - 2 / PHI, 3.0, 3.3), "corde = 2/φ", "XIII", "chevre"),
    (3.19953, "part manquante maximale", "VI", "chevre"),
    (2 * PHI, "maille décalée = 2/φ (n = 2φ)", "XV", "grille"),
    (brentq(lambda n: corde(n) - PHI ** 0.5, 4.0, 4.3), "corde = √φ (r² = φ)", "XIII", "chevre"),
    (PHI ** 3, "maille décalée = √φ (n = φ³)", "XV", "grille"),
    (7.0, "corde ≈ nombre plastique (à 4·10⁻⁵ près)", "III", "autre"),
]
SPECIALES.sort()
ligne("\n### La carte des dimensions particulières (parties III à XV)\n")
ligne("| dimension n | ce qui s'y passe | partie |")
ligne("|---:|---|---|")
for n, quoi, ou, _ in SPECIALES:
    ligne(f"| {fr(n, '{:.4f}')} | {quoi} | {ou} |")


# ---------------------------------------------------------------------------
# 5. L'aiguille sur la grille décalée : les entiers d'Eisenstein
# ---------------------------------------------------------------------------
def points_hex(L):
    """Points de la grille hexagonale (maille 1) sur le cercle de rayon L : a + b·e^{iπ/3}, de norme a² + ab + b²."""
    return [(a + b / 2, b * math.sqrt(3) / 2) for a in range(-2 * L, 2 * L + 1) for b in range(-2 * L, 2 * L + 1)
            if a * a + a * b + b * b == L * L]


def r_hex(N):
    """6·Σ χ(d) sur les diviseurs d de N, χ(d) = 0, 1, −1 selon d ≡ 0, 1, 2 (mod 3)."""
    return 6 * sum((0, 1, -1)[d % 3] for d in range(1, N + 1) if N % d == 0)


def mod60(a):
    v = a % 60
    return 0.0 if abs(v - 60) < 1e-6 else round(v, 6)


ligne("\n## 5. L'aiguille sur la grille décalée\n")
ligne("| L | points de la grille décalée sur le cercle (comptés) | formule d'Eisenstein | points de la grille carrée (partie XIV) |")
ligne("|---:|---:|---:|---:|")
for L in (1, 2, 3, 5, 7, 13, 19, 49, 91):
    sq = sum(1 for a in range(-L, L + 1) for b in range(-L, L + 1) if a * a + b * b == L * L)
    ligne(f"| {L} | {len(points_hex(L))} | {r_hex(L * L)} | {sq} |")
TH7 = math.degrees(math.acos(11 / 14))
ligne(f"\nSur la grille décalée, ce sont les nombres premiers de la forme 3k + 1 (7, 13, 19…) qui ouvrent des directions ;"
      f" 5 n'en ouvre plus. L'angle du triangle 5-7-8 (ou 3-5-7) vaut arccos(11/14) = {fr(TH7, '{:.4f}')}° :\n")
ligne("| L | directions par sixième de tour | longueurs des trous |")
ligne("|---:|---:|---|")
for k in (1, 2, 3):
    a = sorted({mod60(math.degrees(math.atan2(y, x))) for x, y in points_hex(7 ** k)})
    assert np.allclose(a, sorted({mod60(m * TH7) for m in range(-k, k + 1)}))
    g = np.diff(a + [a[0] + 60])
    ligne(f"| 7^{k} = {7 ** k} | {len(a)} | {' ; '.join(fr(v, '{:.3f}') for v in sorted({round(x, 4) for x in g}))} |")
ligne("\nS'inverser avec la grille décalée (maille 1) :")
ligne(f"- un bout fixe : 4 positions (0°, 60°, 120°, 180°), trois triangles équilatéraux d'aire totale 3√3/4 ="
      f" {fr(3 * 3 ** 0.5 / 4, '{:.4f}')}, contre π/2 = {fr(math.pi / 2, '{:.4f}')} pour le demi-disque"
      " (grille carrée : 3 positions seulement) ;")
ligne(f"- le milieu fixe (aiguille de longueur 2) : 3 positions, l'hexagone d'aire 3√3/2 = {fr(3 * 3 ** 0.5 / 2, '{:.4f}')},"
      f" contre π = {fr(math.pi, '{:.4f}')} pour le disque ;")
ligne(f"- chaque pas de rotation coûte au moins un triangle de la grille, √3/4 = {fr(3 ** 0.5 / 4, '{:.4f}')} : la demi-maille.")
ligne(f"\nÉchantillonnage (Petersen et Middleton, 1962) : à nombre de points égal, la grille décalée laisse passer des"
      f" fréquences {fr(100 * (math.sqrt(2 / 3 ** 0.5) - 1), '{:.1f}')} % plus fines dans toutes les directions ; pour la même"
      f" finesse, il lui faut {fr(100 * (1 - 3 ** 0.5 / 2), '{:.1f}')} % de points en moins.")

with open(os.path.join(ICI, "..", "resultats", "grille_decalee.md"), "w") as fh:
    fh.write("# Résultats de la partie XV (générés par scripts/grille_decalee.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure
# ===========================================================================
fig = plt.figure(figsize=(20, 13.6))
gs = fig.add_gridspec(2, 3, wspace=0.2, hspace=0.27)
FOND = dict(fc=F.SURF, ec="none", alpha=0.92, pad=2.5)


def schema(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")


# a) la chèvre sur la grille décalée
ax = fig.add_subplot(gs[0, 0])
s2 = arete(2)
for j in range(-2, 3):  # la rangée de P (y = 1) n'est pas décalée, celle de A et B (y = 0) l'est d'une demi-maille
    xs_ = (np.arange(-3, 4) + (0.5 if j % 2 == 0 else 0.0)) * s2
    ax.plot([xs_[0] - s2, xs_[-1] + s2], [j, j], color=F.GRID, lw=0.8, zorder=0)
    for x0 in xs_:
        for dx in (-0.5, 0.5):  # arêtes des triangles vers la rangée du dessus
            ax.plot([x0, x0 + dx * s2], [j, j + 1], color=F.GRID, lw=0.8, zorder=0)
    ax.plot(xs_, np.full_like(xs_, float(j)), "o", color=F.MUTED, ms=3.5, zorder=1)
O_, P_ = np.array([0.0, 0.0]), np.array([0.0, 1.0])
A_, B_ = np.array([-s2 / 2, 0.0]), np.array([s2 / 2, 0.0])
t = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(t), np.sin(t), color=F.INK, lw=1.4)
ax.plot(R2 * np.cos(t), 1 + R2 * np.sin(t), color=F.ORANGE, lw=1.4)
ax.add_patch(Polygon([P_, A_, B_], closed=True, fc=F.BLEU, alpha=0.18, ec=F.BLEU, lw=1.4))
for p, lab, dx, dy in ((O_, "O", 0.06, -0.12), (P_, "P", 0.07, 0.05), (A_, "A", -0.16, -0.12), (B_, "B", 0.06, -0.12)):
    F.point(ax, *p, F.INK if lab in "OP" else F.BLEU, 6)
    ax.text(p[0] + dx, p[1] + dy, lab, fontsize=11, fontweight="bold")
ax.annotate("", xy=(0, 1.0), xytext=(0, 0.0), arrowprops=dict(arrowstyle="<->", color=F.INK2, lw=0.9))
ax.text(0.04, 0.45, "1", fontsize=10, color=F.INK2)
ax.text(-2.55, 2.35, "rangées espacées de 1, une sur deux décalée d'une demi-maille :\nla maille vaut 2/√3, le côté du triangle PAB de la chèvre",
        fontsize=9, color=F.INK2, va="top", bbox=FOND)
ax.text(1.12, -0.85, "noir : le pré ;\norange : la corde, r = 1,15873.\nElle passe juste au-delà des\nsix voisins de P (à 1,15470) :\n"
        "le ménisque.", fontsize=9, color=F.INK2, va="top", bbox=FOND)
axi = ax.inset_axes([0.0, 0.0, 0.34, 0.3])
zoom = 0.012
axi.plot(R2 * np.cos(t), 1 + R2 * np.sin(t), color=F.ORANGE, lw=1.6)
axi.plot(s2 * np.cos(t), 1 + s2 * np.sin(t), color=F.BLEU, lw=1.2, ls="--")
axi.plot(*A_, "o", color=F.BLEU, ms=5)
axi.set_xlim(A_[0] - zoom, A_[0] + zoom)
axi.set_ylim(A_[1] - zoom, A_[1] + zoom)
axi.set_aspect("equal")
axi.set_xticks([])
axi.set_yticks([])
axi.set_title("près de A : le ménisque\n(0,35 % de la corde)", fontsize=7.5, fontweight="normal", loc="center")
schema(ax, (-2.6, 2.7), (-1.6, 2.45))
ax.set_title("a)  Ta grille décalée : la chèvre retrouve son triangle")

# b) la corde et la maille de dimension en dimension
ax = fig.add_subplot(gs[0, 1])
nn = np.exp(np.linspace(np.log(1.02), np.log(200), 260))
rr = np.array([corde(n) for n in nn])
ss = np.array([arete(n) for n in nn])
ax.semilogx(nn, rr, color=F.ORANGE, lw=2, label="corde de la chèvre r(n)")
ax.semilogx(nn, ss, color=F.BLEU, lw=1.4, ls="--", label="maille décalée s(n) = √(2n/(n+1))")
ax.axhline(1, color=F.MUTED, lw=0.9, ls=":")
ax.axhline(2 ** 0.5, color=F.MUTED, lw=0.9, ls=":")
ax.text(1.6, 1.006, "grille carrée : côté 1", ha="left", fontsize=8.5, color=F.INK2)
ax.text(150, 2 ** 0.5 - 0.016, "grille carrée : diagonale √2", ha="right", fontsize=8.5, color=F.INK2)
ax.set_xlabel("dimension n")
ax.set_ylabel("longueur (rayon du pré = 1)")
ax.set_ylim(0.97, 1.45)
ax.legend(fontsize=8.5, loc="upper left", frameon=True, facecolor=F.SURF, edgecolor="none")
axt = ax.inset_axes([0.45, 0.12, 0.52, 0.33])
gap = 100 * (rr - ss) / ss
axt.semilogx(nn, gap, color=ROUGE, lw=1.5)
axt.axvline(MREL.x, color=ROUGE, lw=0.8, ls=":")
axt.axvline(MABS.x, color=F.INK2, lw=0.8, ls=":")
axt.text(MREL.x * 1.05, 0.04, f"max {MREL.x:.2f}".replace(".", ","), fontsize=7, color=ROUGE)
axt.text(MABS.x * 1.15, 0.2, f"écart absolu\nmax {MABS.x:.2f}".replace(".", ","), fontsize=7, color=F.INK2)
axt.set_title("le ménisque (r − s)/s, en %", fontsize=7.5, fontweight="normal", loc="center")
axt.tick_params(labelsize=7)
axt.set_ylim(0, 0.4)
axt.set_facecolor(F.SURF)
ax.set_title("b)  De 1 à √2 : la chèvre suit la maille décalée")

# c) quand la grille voit le ménisque
ax = fig.add_subplot(gs[0, 2])
couls = {"2D, grille carrée": F.MUTED, "2D, grille décalée": F.BLEU, "3D, grille cubique": F.JAUNE, "3D, couches décalées": F.ORANGE}
for nom, (res, voit, seuil, Ms, r) in COMPTE.items():
    Ms_ = np.array([M for _, _, M in res])
    err = np.array([abs(c - r) / r for _, c, _ in res]) * 100
    ax.loglog(Ms_, np.maximum(err, 1e-5), "o", ms=2.6, color=couls[nom], alpha=0.75, label=f"{nom} (seuil : {Ms} points)")
ax.axhline(100 * (R2 - arete(2)) / R2, color=F.BLEU, lw=1, ls="--")
ax.axhline(100 * (R3 - arete(3)) / R3, color=F.ORANGE, lw=1, ls="--")
ax.text(30, 0.42, "ménisques 2D (0,35 %) et 3D (0,31 %)", fontsize=8.5, color=F.INK2)
ax.set_ylim(1e-5, 30)
ax.set_xlabel("points dans le pré")
ax.set_ylabel("écart de la corde comptée à la vraie corde (%)")
ax.legend(fontsize=8, loc="lower left", frameon=True, facecolor=F.SURF, edgecolor="none", markerscale=2)
ax.text(0.97, 0.97, "Sous les tirets, la grille sépare la chèvre\nde son simplexe : elle voit le ménisque.",
        transform=ax.transAxes, ha="right", va="top", fontsize=9, color=F.INK2)
ax.set_title("c)  La chèvre comptée : quand la grille voit le ménisque")

# d) la carte des dimensions
sub = gs[1, 0:2].subgridspec(1, 2, width_ratios=[1.45, 1], wspace=0.02)
ax = fig.add_subplot(sub[0, 0])
nd = np.linspace(1.6, 4.45, 400)
gd = np.array([corde(n) - arete(n) for n in nd])
ax.plot(nd, 1000 * gd, color=ROUGE, lw=1.8)
ax.fill_between(nd, 0, 1000 * gd, color=ROUGE, alpha=0.08)
COUL_NAT = {"grille": F.BLEU, "chevre": F.ORANGE, "autre": F.INK2}
DECAL = [0.45, 0.95, 1.45, 1.95, 2.45]
for i, (n, quoi, ou, nat) in enumerate(SPECIALES, 1):
    if n > 4.45:
        continue
    y = 1000 * (corde(n) - arete(n))
    ax.plot([n, n], [0, y], color=COUL_NAT[nat], lw=0.8, ls="-" if nat == "grille" else ":")
    ax.plot(n, y, "o", color=COUL_NAT[nat], ms=5.5, mec=F.SURF, zorder=5)
    yt = y + DECAL[(i - 1) % len(DECAL)]
    ax.plot([n, n], [y, yt - 0.12], color=F.BASE, lw=0.5)
    ax.text(n, yt, str(i), ha="center", va="bottom", fontsize=8.5, color=COUL_NAT[nat], fontweight="bold")
ax.set_xlim(1.6, 4.45)
ax.set_ylim(0, 7.0)
ax.set_xlabel("dimension n")
ax.set_ylabel("ménisque r(n) − s(n) (millièmes du rayon)")
ax.set_title("d)  Tous les paramètres sur une seule carte : le ménisque et les dimensions particulières")
axl = fig.add_subplot(sub[0, 1])
axl.axis("off")
for i, (n, quoi, ou, nat) in enumerate(SPECIALES, 1):
    axl.text(0.0, 1 - (i - 0.5) / len(SPECIALES), f"{i:>2}", fontsize=8.5, color=COUL_NAT[nat], fontweight="bold",
             va="center", transform=axl.transAxes)
    axl.text(0.06, 1 - (i - 0.5) / len(SPECIALES), f"n = {fr(n, '{:.4f}')} : {quoi} ({ou})", fontsize=8.3, va="center",
             transform=axl.transAxes, color=F.INK)
axl.text(0.0, -0.06, "bleu : dimension exacte de la grille décalée (algébrique) ; orange : la chèvre ; gris : autre",
         fontsize=8, color=F.INK2, transform=axl.transAxes)

# e) la carte des liens : un anneau fermé, et quatre nœuds intérieurs
ax = fig.add_subplot(gs[1, 2])
ANNEAU = ["chevre", "simplexe", "grille", "carree", "345", "or", "foyers", "menisque"]
NOMS = {"chevre": "corde de la\nchèvre r(n)", "simplexe": "simplexe s(n)", "grille": "grille décalée\n(cube coupé)",
        "carree": "grille carrée", "345": "3-4-5\n53,13°", "or": "angle d'or\n137,5°", "foyers": "foyers de\nFibonacci",
        "menisque": "ménisque\n0,35 %", "phi": "φ", "aiguille": "aiguille\nde Kakeya", "moire": "moiré,\ncentres fantômes",
        "ptolemee": "Ptolémée,\nplan hyperbolique"}
POS = {k: (2.55 * math.cos(math.radians(135 - 45 * i)), 0.45 + 2.2 * math.sin(math.radians(135 - 45 * i)))
       for i, k in enumerate(ANNEAU)}
POS.update({"phi": (-0.95, 0.55), "ptolemee": (1.2, 1.2), "aiguille": (0.4, 0.3), "moire": (0.1, -0.85)})
ARETES = [("chevre", "simplexe", "0,35 % (VI)", False, 0.5), ("simplexe", "grille", "maille (XV)", True, 0.5),
          ("grille", "carree", "coupe diagonale (XV)", True, 0.25), ("carree", "345", "2·arctan ½ (XIV)", False, 0.5),
          ("345", "or", "trois distances (XI, XIV)", False, 0.5), ("or", "foyers", "même partage (XI)", False, 0.5),
          ("foyers", "menisque", "FTM50 (VIII)", False, 0.35), ("menisque", "chevre", "(VI)", False, 0.5),
          ("simplexe", "phi", "pentagone en √5 (XV)", True, 0.45), ("chevre", "phi", "rⁿ = φ (XIII)", False, 0.5),
          ("phi", "foyers", "1/φ² + 1/φ = 1 (IX)", False, 0.5), ("phi", "ptolemee", "pentagone (X)", False, 0.5),
          ("ptolemee", "carree", "λ = aire (XIV)", False, 0.5), ("carree", "aiguille", "directions (XIV)", False, 0.5),
          ("aiguille", "simplexe", "triangle 2/√3 (V)", False, 0.5), ("aiguille", "moire", "Perron tourné (XIII)", False, 0.5),
          ("moire", "foyers", "nœuds (XIII)", False, 0.62), ("moire", "carree", "réseau réciproque (X)", False, 0.62)]
for a_, b_, lab, nouveau, tt in ARETES:
    (xa, ya), (xb, yb) = POS[a_], POS[b_]
    ax.plot([xa, xb], [ya, yb], color=ROUGE if nouveau else F.BASE, lw=1.6 if nouveau else 1.0, zorder=1)
    ax.text(xa + tt * (xb - xa), ya + tt * (yb - ya), lab, fontsize=6.9, color=ROUGE if nouveau else F.INK2, ha="center",
            va="center", zorder=3, bbox=dict(fc=F.SURF, ec="none", alpha=0.9, pad=0.6))
for k, (x, y) in POS.items():
    lb = {"ptolemee": 1.3, "moire": 1.25}.get(k, 1.0)
    ax.add_patch(FancyBboxPatch((x - lb / 2, y - 0.24), lb, 0.48, boxstyle="round,pad=0.04", fc=F.SURF,
                                ec=ROUGE if k == "grille" else F.BLEU, lw=1.4, zorder=4))
    ax.text(x, y, NOMS[k], ha="center", va="center", fontsize=7.8, zorder=5, color=F.INK)
ax.text(-3.15, -2.25, "L'anneau extérieur se referme : chèvre → simplexe → grille décalée → grille carrée\n"
        "→ 3-4-5 → angle d'or → foyers → ménisque → chèvre. En rouge : les liens de la partie XV.",
        fontsize=8, color=F.INK2, va="top")
schema(ax, (-3.25, 3.25), (-2.6, 2.95))
ax.set_title("e)  La carte des liens entre tous les paramètres")
F.sauver(fig, "o1_grille_decalee.png")
