"""
Partie VIII : le foyer, le diaphragme, les ménisques, les géodésiques et Fibonacci.

    python3 scripts/foyer_fibonacci.py        # ≈ 1 min

Écrit resultats/foyer_fibonacci.md, figures/h1_foyer_menisques.png et figures/h2_fibonacci.png.

1. Retourner l'aiguille : par un foyer, en pivotant, dans le deltoïde de Kakeya.
2. Le ménisque de phase et les zones de Fresnel.
3. Les deux ménisques de la FTM, et la FTO défocalisée (Hopkins 1955) : la transformée de Fourier
   de la lentille de la chèvre.
4. Une facette géodésique est un ménisque de phase.
5. Les géodésiques sont les rayons de l'œil de poisson de Maxwell, qui retourne l'image.
6. La réciprocité de la partie VII est le théorème de la boîte à chapeau d'Archimède.
7. La lentille de Fibonacci (Monsoriu et al. 2013) : deux foyers dans le rapport φ.
8. Les sphères géodésiques aux fréquences de Fibonacci, et la grille de Fibonacci.
"""

import logging
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle, FancyArrowPatch, Polygon
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq, minimize_scalar
from scipy.signal import find_peaks
from scipy.spatial import ConvexHull

sys.path.insert(0, os.path.dirname(__file__))
import archimede as A  # noqa: E402
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)  # ajustements d'échelle des schémas, sans importance
ICI = os.path.dirname(os.path.abspath(__file__))
PHI = (1 + 5 ** 0.5) / 2
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.6f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


# ---------------------------------------------------------------------------
# 1. Retourner l'aiguille
# ---------------------------------------------------------------------------
def deltoide(t):
    """Deltoïde 2e^{it} + e^{−2it}, réduit d'un facteur 4 pour que l'aiguille mesure 1."""
    return (2 * np.cos(t) + np.cos(2 * t)) / 4, (2 * np.sin(t) - np.sin(2 * t)) / 4


def aiguille_deltoide(t):
    """Extrémités de la tangente en D(t), coupée par le deltoïde."""
    x0, y0 = deltoide(t)
    ux, uy = np.cos(-t / 2), np.sin(-t / 2)  # D'(t) est parallèle à e^{−it/2}
    g = lambda s: (deltoide(s)[0] - x0) * uy - (deltoide(s)[1] - y0) * ux
    ss = np.linspace(t + 1e-3, t + 2 * np.pi - 1e-3, 4001)
    vals = g(ss)
    racines = [brentq(g, ss[i], ss[i + 1]) for i in range(len(ss) - 1) if vals[i] * vals[i + 1] < 0]
    pts = [np.array(deltoide(s)) for s in racines]
    return pts[0], pts[-1]


ligne("## 1. Retourner une aiguille de longueur 1\n")
xd, yd = deltoide(np.linspace(0, 2 * np.pi, 20001))
aire_d = 0.5 * abs(np.sum(xd[:-1] * yd[1:] - xd[1:] * yd[:-1]))
longs = [np.linalg.norm(np.subtract(*aiguille_deltoide(t))) for t in np.linspace(0.1, 2 * np.pi - 0.1, 9)]
ligne("| façon de retourner | aire balayée | la longueur reste 1 ? |")
ligne("|---|---|---|")
ligne("| par un foyer, dans le plan de l'image (x ↦ λx, λ de 1 à −1) | 0 : l'aiguille reste sur sa droite | non : elle passe par 0 au foyer |")
ligne("| par un foyer, le long de l'axe (objet et image à la distance d) | d : deux triangles opposés par le sommet | non |")
ligne(f"| en pivotant autour du point à la distance t du milieu | π/4 + πt², minimum π/4 = {fr(np.pi / 4, '{:.4f}')} pour t = 0 | oui |")
ligne(f"| deltoïde de Kakeya | π/8 = {fr(np.pi / 8, '{:.4f}')} (calculé : {fr(aire_d, '{:.6f}')}) | oui : corde tangente de longueur "
      f"{fr(min(longs), '{:.6f}')} à {fr(max(longs), '{:.6f}')} |")
ligne("| Besicovitch–Perron (partie V) | aussi petite qu'on veut, mais ≥ c/log N avec N directions | oui |")
ligne("\nPivoter de 180° autour du milieu, c'est appliquer x ↦ −x : la même application que le foyer, sans passer par la longueur 0.")

# ---------------------------------------------------------------------------
# 2. Le ménisque de phase et les zones de Fresnel
# ---------------------------------------------------------------------------
ligne("\n## 2. Le ménisque qui déphase : zones de Fresnel\n")
lam, f = 550e-9, 0.05
ligne("Épaisseur du ménisque entre le plan du diaphragme et la sphère centrée au foyer, et retard du chemin optique :")
ligne("| r (mm) | flèche f − √(f² − r²) (nm) | retard √(f² + r²) − f (nm) | r²/2f (nm) | nombre de demi-longueurs d'onde |")
ligne("|---:|---:|---:|---:|---:|")
for r in (0.1e-3, 0.5e-3, 1e-3, 2e-3):
    fl, re, ap = f - np.sqrt(f * f - r * r), np.hypot(f, r) - f, r * r / (2 * f)
    ligne(f"| {fr(r * 1e3, '{:.1f}')} | {fr(fl * 1e9, '{:.2f}')} | {fr(re * 1e9, '{:.2f}')} | {fr(ap * 1e9, '{:.2f}')} | {fr(re / (lam / 2), '{:.2f}')} |")
ligne(f"\nZones de Fresnel pour f = 50 mm et λ = 550 nm : r_k = √(kλf), soit r₁ = {fr(np.sqrt(lam * f) * 1e3, '{:.4f}')} mm ;"
      f" chaque zone a la même aire πλf = {fr(np.pi * lam * f * 1e6, '{:.4f}')} mm², comme les anneaux de Newton (partie I).")
uu = np.linspace(0.05, 6, 500)
ouvert = np.abs(1 - np.exp(-2j * np.pi * uu)) ** 2
ligne(f"Diaphragme ouvert, intensité sur l'axe (u = a²/2λz) : écart maximal à 4 sin²(πu) = {np.max(np.abs(ouvert - 4 * np.sin(np.pi * uu) ** 2)):.1e} ;"
      " noir pour u entier (nombre pair de zones), 4 fois l'intensité incidente pour u demi-entier.")


# ---------------------------------------------------------------------------
# 3. Les deux ménisques de la FTM, et la FTM défocalisée
# ---------------------------------------------------------------------------
def lentille(s):
    """Aire commune à deux disques de rayon 1 dont les centres sont à la distance s."""
    return 2 * np.arccos(s / 2) - (s / 2) * np.sqrt(4 - s * s)


def ftm(nu, w):
    """FTO défocalisée (Hopkins 1955), c'est-à-dire la FTM avec son signe ; nu = fréquence/coupure, w = défocalisation W₂₀ en longueurs d'onde.
    Le déphasage entre les deux pupilles décalées de s = 2nu est 4πw·s·x : linéaire sur la lentille commune."""
    s = 2 * nu
    if s >= 2:
        return 0.0
    g = lambda x: np.sqrt(max(0.0, 1 - (x + s / 2) ** 2)) * np.cos(4 * np.pi * w * s * x)
    return 4 / np.pi * quad(g, 0, 1 - s / 2, limit=400)[0]


def ftm_min(w):
    g = np.linspace(0.01, 0.99, 300)
    o = [ftm(n, w) for n in g]
    k = int(np.argmin(o))
    r = minimize_scalar(lambda n: ftm(n, w), bounds=(g[max(k - 1, 0)], g[min(k + 1, len(g) - 1)]), method="bounded",
                        options={"xatol": 1e-12})
    return r.fun, r.x


ligne("\n## 3. Les deux ménisques de la FTM, et la défocalisation\n")
s50 = brentq(lambda s: lentille(s) - np.pi / 2, 0.1, 1.9)
ligne(f"Lentille = ménisque = π/2 (la condition de la chèvre pour deux disques égaux) : s = {fr(s50)}, soit ν/ν_c = {fr(s50 / 2, '{:.4f}')} (FTM50 de la partie I).")
ligne("Les deux ménisques (disque 1 privé du disque 2, et l'inverse) s'échangent par x ↦ −x autour du centre de la lentille : rotation de 180°.")
ligne(f"Contrôle : FTM sans défocalisation contre formule fermée, écart maximal "
      f"{max(abs(ftm(n, 0) - lentille(2 * n) / np.pi) for n in np.linspace(0, 0.99, 40)):.1e}")
w_seuil = brentq(lambda w: ftm_min(w)[0], 0.62, 0.66, xtol=1e-7)
ligne(f"La FTO (la FTM avec son signe) devient négative (contraste inversé) au-delà de W₂₀ = {fr(w_seuil, '{:.4f}')} λ, d'abord vers ν/ν_c = {fr(ftm_min(w_seuil)[1], '{:.3f}')}.")
ligne("\n| défocalisation W₂₀ | premier zéro de la FTO (ν/ν_c) | minimum (contraste inversé) | approximation géométrique 2J₁(v)/v, premier zéro |")
ligne("|---|---|---|---|")
OTF_TAB = {}
for w in (0.5, 0.75, 1.0, 2.0):
    mn, xn = ftm_min(w)
    g = np.linspace(0.002, 0.998, 500)
    o = np.array([ftm(n, w) for n in g])
    neg = np.where(o < 0)[0]
    z = brentq(lambda n: ftm(n, w), g[neg[0] - 1], g[neg[0]]) if len(neg) else None
    OTF_TAB[w] = (z, mn, xn)
    ligne(f"| {fr(w, '{:.2f}')} λ | {'aucun' if z is None else fr(z, '{:.4f}')} | {fr(mn, '{:.4f}')} en {fr(xn, '{:.3f}')} |"
          f" {fr(3.8317 / (8 * np.pi * w), '{:.4f}')} |")

# ---------------------------------------------------------------------------
# 4. Une facette géodésique est un ménisque de phase
# ---------------------------------------------------------------------------
ligne("\n## 4. Une facette géodésique est un ménisque de phase\n")
ligne("Sur une onde qui converge vers le centre O de la sphère (le foyer), une facette plane retarde la lumière de l'épaisseur"
      " du ménisque qui la sépare de la sphère. Épaisseur maximale par facette, pour une sphère de rayon R :")
ligne("| fréquence ν | facettes | ménisque le plus épais (R) | × ν² | zones de Fresnel par facette (R = 1 m, λ = 550 nm) |")
ligne("|---:|---:|---|---|---:|")
MEN = {}
for nu in (1, 2, 3, 5, 8, 13, 21, 34):
    V = A.polyedre(f"geo{nu}")
    hull = ConvexHull(V)
    d = np.abs(hull.equations[:, 3])  # distance de O au plan de chaque facette
    e = 1 - d.min()
    MEN[nu] = e
    ligne(f"| {nu} | {len(hull.simplices)} | {fr(e, '{:.4e}')} | {fr(e * nu * nu, '{:.4f}')} | {fr(2 * e / 550e-9, '{:,.0f}').replace(',', ' ')} |")
ligne("\nLe ménisque d'une facette suit 1/ν², comme les zones de Fresnel suivent r² : passer d'une fréquence de Fibonacci à la"
      " suivante le divise par (F_(k+1)/F_k)², qui tend vers φ².")


# ---------------------------------------------------------------------------
# 5. L'œil de poisson de Maxwell
# ---------------------------------------------------------------------------
def rayon_maxwell(P, ang, L):
    """Rayon dans l'indice n = 2/(1 + r²), paramétré par la longueur d'arc."""
    def g(s, y):
        x, d = y[:2], y[2:]
        gr = -2 * x / (1 + x @ x)  # gradient de ln n
        return np.r_[d, gr - (gr @ d) * d]
    return solve_ivp(g, (0, L), np.r_[P, np.cos(ang), np.sin(ang)], rtol=1e-12, atol=1e-13, dense_output=True)


ligne("\n## 5. Les géodésiques sont des rayons : l'œil de poisson de Maxwell\n")
P = np.array([0.45, 0.25])
Pp = -P / (P @ P)
RAYONS, pire = [], 0.0
for ang in np.radians(np.arange(0, 360, 15)):
    dvec = np.array([np.cos(ang), np.sin(ang)])
    nvec = np.array([-dvec[1], dvec[0]])
    rc = abs((P - Pp) @ (P - Pp) / (2 * nvec @ (P - Pp)))  # rayon du cercle passant par P et P'
    if rc > 3:
        continue
    L = 2 * np.pi * rc * 1.02
    sol = rayon_maxwell(P, ang, L)
    ss = np.linspace(0, L, 3000)
    X = sol.sol(ss)[:2].T
    k = int(np.argmin(np.linalg.norm(X - Pp, axis=1)))
    r = minimize_scalar(lambda t: np.linalg.norm(sol.sol(t)[:2] - Pp), bounds=(ss[max(k - 1, 0)], ss[min(k + 1, len(ss) - 1)]),
                        method="bounded", options={"xatol": 1e-12})
    pire = max(pire, r.fun)
    RAYONS.append(sol.sol(np.linspace(0, r.x, 600))[:2])
ligne(f"Point source P = (0,45 ; 0,25), image attendue P' = −P/|P|² = ({fr(Pp[0], '{:.4f}')} ; {fr(Pp[1], '{:.4f}')}).")
ligne(f"{len(RAYONS)} rayons tracés numériquement : tous repassent par P' à {pire:.1e} près. |OP|·|OP'| = {fr(np.linalg.norm(P) * np.linalg.norm(Pp), '{:.6f}')} = R².")
ligne("Sur le cercle |x| = R, l'image de x est −x : la rotation de 180°, l'aiguille retournée.")

# ---------------------------------------------------------------------------
# 6. La réciprocité de la partie VII est la boîte à chapeau d'Archimède
# ---------------------------------------------------------------------------
ligne("\n## 6. La réciprocité κ₂ₘ·h₂ₘ₊₁ = 1/(2m + 1) et la boîte à chapeau d'Archimède\n")
boule = lambda n: sp.pi ** sp.Rational(n, 2) / sp.gamma(sp.Rational(n, 2) + 1)      # volume de B^n
sphere = lambda n: 2 * sp.pi ** sp.Rational(n + 1, 2) / sp.gamma(sp.Rational(n + 1, 2))  # aire de S^n (dans R^(n+1))
ok = []
for m in range(1, 13):
    h = sp.nsimplify(boule(2 * m + 1) / (2 * boule(2 * m)))
    kappa = sp.binomial(2 * m, m) / sp.Integer(4) ** m
    ok.append((sp.simplify(kappa * h - sp.Rational(1, 2 * m + 1)) == 0, sp.simplify(sphere(2 * m) - 2 * sp.pi * boule(2 * m - 1)) == 0))
ligne(f"m = 1 à 12 : κ₂ₘ·h₂ₘ₊₁ = 1/(2m + 1) {'vérifié' if all(a for a, _ in ok) else 'FAUX'} ;"
      f" aire(S^2m) = 2π·volume(B^(2m−1)) {'vérifié' if all(b for _, b in ok) else 'FAUX'} (calcul exact).")
ligne("Pour m = 1 : κ₂·h₃ = ½ · ⅔ = ⅓, et aire(S²) = 4π = 2π × 2 : la sphère a l'aire du cylindre qui l'entoure (Archimède).")


# ---------------------------------------------------------------------------
# 7. La lentille de Fibonacci
# ---------------------------------------------------------------------------
def mot_fibonacci(j):
    """S₀ = B, S₁ = A, S_(j+1) = S_j S_(j−1) ; A = anneau transparent, B = opaque."""
    S = ["B", "A"]
    for _ in range(2, j + 1):
        S.append(S[-1] + S[-2])
    return S[j]


def intensite_axe(q, u):
    """Intensité sur l'axe d'un diaphragme de N zones égales en ζ = (r/a)², de transmissions q (Fresnel) :
    I(u) = 4 sin²(πu/N) |Σ q_k e^(−2iπuk/N)|², avec u = a²/(2λz)."""
    N = len(q)
    z = np.exp(-2j * np.pi * np.asarray(u, float) / N)
    Q = np.zeros_like(z)
    for t in q[::-1]:  # schéma de Horner
        Q = Q * z + t
    return 4 * np.sin(np.pi * np.asarray(u, float) / N) ** 2 * np.abs(Q) ** 2


def deux_foyers(j):
    q = np.array([c == "A" for c in mot_fibonacci(j)], float)
    N = len(q)
    u = np.linspace(0.3, N - 0.3, 60 * N)
    I = intensite_axe(q, u)
    pics, _ = find_peaks(I)
    deux = sorted(pics[np.argsort(I[pics])[-2:]])
    fins = []
    for k in deux:
        r = minimize_scalar(lambda x: -intensite_axe(q, x), bounds=(u[k - 1], u[k + 1]), method="bounded", options={"xatol": 1e-11})
        fins.append((r.x, -r.fun))
    return N, q, fins


ligne("\n## 7. La lentille de Fibonacci : deux foyers dans le rapport φ\n")
ligne("| anneaux N = F_j | foyer 1 (u) | foyer 2 (u) | u₁ + u₂ | F_(j−2), F_(j−1) | rapport des distances focales z₁/z₂ = u₂/u₁ | écart des intensités |")
ligne("|---:|---|---|---|---|---|---|")
FOYERS = {}
for j in range(7, 15):
    N, q, ((u1, I1), (u2, I2)) = deux_foyers(j)
    FOYERS[j] = (N, u1, u2)
    ligne(f"| {N} | {fr(u1, '{:.4f}')} | {fr(u2, '{:.4f}')} | {fr(u1 + u2, '{:.6f}')} | {len(mot_fibonacci(j - 2))}, {len(mot_fibonacci(j - 1))} |"
          f" {fr(u2 / u1)} | {abs(I1 / I2 - 1):.0e} |")
ligne(f"\nφ = {fr(PHI)}. La somme u₁ + u₂ vaut N : pour tout diaphragme à N zones égales, I(N − u) = I(u) exactement."
      " Les deux foyers sont donc symétriques (en 1/z) autour du foyer unique u = N/2 de la lame de Fresnel périodique.")
qp = np.array([k % 2 == 0 for k in range(144)], float)
up = np.linspace(0.3, 143.7, 60 * 144)
Ip = intensite_axe(qp, up)
ligne(f"Lame de Fresnel périodique (144 zones) : un seul foyer principal, en u = {fr(up[np.argmax(Ip)], '{:.2f}')} = 144/2.")


# ---------------------------------------------------------------------------
# 8. Sphères géodésiques aux fréquences de Fibonacci, grille de Fibonacci
# ---------------------------------------------------------------------------
def grille_fibonacci(N):
    i = np.arange(N)
    z = 1 - (2 * i + 1) / N
    t = 2 * np.pi * i / PHI ** 2  # angle d'or
    rho = np.sqrt(1 - z ** 2)
    return np.c_[rho * np.cos(t), rho * np.sin(t), z]


ligne("\n## 8. Sphères géodésiques aux fréquences de Fibonacci\n")
ligne("| fréquence ν | points | volume manquant 4π/3 − V | rapport au précédent | grille de Fibonacci, même N | grille / géodésique |")
ligne("|---:|---:|---|---|---|---|")
GEO, prec = {}, None
for nu in (1, 2, 3, 5, 8, 13, 21, 34, 55):
    V = A.polyedre(f"geo{nu}")
    dg = 4 * np.pi / 3 - ConvexHull(V).volume
    dfib = 4 * np.pi / 3 - ConvexHull(grille_fibonacci(len(V))).volume
    GEO[nu] = (len(V), dg, dfib)
    ligne(f"| {nu} | {len(V)} | {fr(dg, '{:.4e}')} | {'' if prec is None else fr(prec / dg, '{:.4f}')} | {fr(dfib, '{:.4e}')} | {fr(dfib / dg, '{:.3f}')} |")
    prec = dg
ligne(f"\nφ² = {fr(PHI ** 2, '{:.4f}')}. Avec les fréquences doublées de la partie II (2, 4, 8…), le même rapport tend vers 4 = 2² :")
DOUBLE, prec = {}, None
for nu in (1, 2, 4, 8, 16, 32):
    V = A.polyedre(f"geo{nu}")
    DOUBLE[nu] = 4 * np.pi / 3 - ConvexHull(V).volume
    if prec is not None:
        ligne(f"- ν = {nu // 2} → {nu} : rapport {fr(prec / DOUBLE[nu], '{:.4f}')}")
    prec = DOUBLE[nu]

with open(os.path.join(ICI, "..", "resultats", "foyer_fibonacci.md"), "w") as fh:
    fh.write("# Résultats de la partie VIII (générés par scripts/foyer_fibonacci.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure h1 : le foyer, les ménisques, les géodésiques
# ===========================================================================
fig, axs = plt.subplots(2, 3, figsize=(20, 12.6), gridspec_kw={"wspace": 0.14, "hspace": 0.2})
FOND = dict(fc=F.SURF, ec="none", alpha=0.88, pad=2)


def schema(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")


def aiguille(ax, p, q_, couleur, lw=3.0, z=5):
    ax.plot([p[0], q_[0]], [p[1], q_[1]], color=couleur, lw=lw, solid_capstyle="butt", zorder=z)
    F.point(ax, q_[0], q_[1], couleur, 6.5, z + 1)  # le point marque le « haut » de l'aiguille


# a) retourner l'aiguille
ax = axs[0, 0]
fx = 2.0
ax.plot([0.1, 3.9], [0, 0], color=F.BASE, lw=0.9, zorder=0)
ax.add_patch(Polygon([[0.3, -0.5], [0.3, 0.5], [fx, 0]], fc=F.ORANGE, alpha=0.18, ec="none"))
ax.add_patch(Polygon([[3.7, -0.5], [3.7, 0.5], [fx, 0]], fc=F.ORANGE, alpha=0.18, ec="none"))
for x in (0.72, 1.15, 1.58, 2.42, 2.85, 3.28):
    h = 0.5 * abs(x - fx) / 1.7
    ax.plot([x, x], [-h, h], color=F.ORANGE, lw=1.4, alpha=0.9)
aiguille(ax, (0.3, -0.5), (0.3, 0.5), F.INK)
aiguille(ax, (3.7, 0.5), (3.7, -0.5), F.INK)
F.point(ax, fx, 0, F.ORANGE, 7)
ax.text(fx, 0.13, "foyer", ha="center", fontsize=9)
ax.text(fx, -0.62, "par un foyer : la longueur passe par 0", ha="center", va="top", fontsize=9.5)
cy = -1.75
ax.add_patch(Circle((0.9, cy), 0.5, fc=F.BLEU, alpha=0.12, ec=F.BLEU, lw=1))
for a_ in np.radians(np.arange(15, 180, 15)):
    ax.plot([0.9 - 0.5 * np.sin(a_), 0.9 + 0.5 * np.sin(a_)], [cy + 0.5 * np.cos(a_), cy - 0.5 * np.cos(a_)], color=F.BLEU, lw=0.9,
            alpha=0.6)
aiguille(ax, (0.9, cy - 0.5), (0.9, cy + 0.5), F.INK)
F.point(ax, 0.9, cy - 0.5, F.BLEU, 6.5, 7)
F.point(ax, 0.9, cy, F.ORANGE, 6, 8)
cd = 3.0
ax.fill(cd + xd, cy + yd, fc=F.AQUA, alpha=0.15, ec=F.AQUA, lw=1.2)
for t in np.linspace(0.25, 2 * np.pi - 0.25, 11):
    p1, p2 = aiguille_deltoide(t)
    ax.plot([cd + p1[0], cd + p2[0]], [cy + p1[1], cy + p2[1]], color=F.AQUA, lw=0.9, alpha=0.75)
ax.text(0.9, -2.5, "en pivotant au milieu\nπ/4 = 0,785", ha="center", va="top", fontsize=9.5)
ax.text(cd + 0.1, -2.5, "Kakeya : le deltoïde\nπ/8 = 0,393", ha="center", va="top", fontsize=9.5)
ax.text(0.0, -3.08, "Au bout du compte, les trois font x ↦ −x : l'image retournée.\n"
        "Le foyer y arrive en écrasant l'aiguille jusqu'à zéro ;\n"
        "pivoter ou suivre le deltoïde garde sa longueur.\n"
        "Le bord du deltoïde enveloppe toutes les positions de\n"
        "l'aiguille : une caustique, si on les lit comme des rayons.", fontsize=9, color=F.INK2, va="top")
schema(ax, (-0.3, 4.3), (-4.0, 0.75))
ax.set_title("a)  Trois façons de retourner l'aiguille")

# b) le ménisque de phase
ax = axs[0, 1]
a_, f_ = 1.2, 1.5
dl = (f_ - np.sqrt(f_ ** 2 - a_ ** 2)) / 5  # λ/2, très exagéré
yy = np.linspace(-a_, a_, 400)
fl = f_ - np.sqrt(f_ ** 2 - yy ** 2)
ax.fill_betweenx(yy, 0, fl, color=F.BLEU, alpha=0.2, lw=0)
ax.plot(fl, yy, color=F.BLEU, lw=1.6)
ax.fill_betweenx(yy, -fl, 0, color=F.BLEU, alpha=0.07, lw=0)
ax.plot(-fl, yy, color=F.BLEU, lw=1.2, ls=(0, (4, 3)))
bords = [0.0]
for k in range(1, 6):  # tranches de λ/2 dans le ménisque, et les bords des zones qu'elles découpent
    yk = np.sqrt(f_ ** 2 - (f_ - k * dl) ** 2)
    bords.append(yk)
    if k < 5:
        ax.plot([k * dl, k * dl], [-yk, yk], color=F.BLEU, lw=0.7, alpha=0.7)
for k in range(5):
    for sgn in (1, -1):
        ax.plot([0, 0], [sgn * bords[k], sgn * bords[k + 1]], color=F.INK if k % 2 == 0 else F.BASE, lw=5, solid_capstyle="butt")
for sgn in (1, -1):
    ax.plot([0, 0], [sgn * a_, sgn * 1.5], color=F.INK, lw=8, solid_capstyle="butt")
for y0 in (1.12, 0.3, -0.3, -1.12):
    ax.plot([0, f_], [y0, 0], color=F.ORANGE, lw=0.9, alpha=0.85)
    ax.plot([0, -f_], [y0, 0], color=F.ORANGE, lw=0.8, alpha=0.6, ls=(0, (3, 3)))
ax.plot([-2.0, 2.0], [0, 0], color=F.BASE, lw=0.9, zorder=0)
F.point(ax, f_, 0, F.ORANGE, 7)
F.point(ax, -f_, 0, F.ORANGE, 7)
ax.text(f_ + 0.12, 0.06, "F : foyer réel\nimage renversée", ha="left", va="bottom", fontsize=9)
ax.text(-f_ - 0.12, 0.06, "F' : foyer virtuel\nimage droite", ha="right", va="bottom", fontsize=9)
ax.annotate("ménisque : son épaisseur est\nle retard de la lumière (≈ r²/2f)", xy=(0.2, 0.95), xytext=(0.45, 1.6), fontsize=9,
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.annotate("diaphragme", xy=(-0.05, 1.4), xytext=(-1.45, 1.7), fontsize=9, color=F.INK2,
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.text(-2.75, -1.68, "Tous les λ/2 d'épaisseur, la phase s'inverse : les tranches\n"
        "du ménisque tombent sur le diaphragme en r_k ≈ √(kλf) :\n"
        "les zones de Fresnel, la loi des anneaux de Newton.\n"
        "Le ménisque conjugué (tirets) sert au foyer virtuel F' :\n"
        "une lame de zones a les deux foyers, +f et −f.  (λ exagéré)", fontsize=9, color=F.INK2, va="top")
schema(ax, (-2.9, 2.9), (-2.85, 2.0))
ax.set_title("b)  Le ménisque où le diaphragme déphase la lumière")

# c) les deux ménisques de la FTM
ax = axs[0, 2]
s = s50
ext = (-1.6, 1.6, -1.1, 1.1)
X, Y = np.meshgrid(np.linspace(-1.6, 1.6, 900), np.linspace(-1.1, 1.1, 620))
in1 = (X + s / 2) ** 2 + Y ** 2 < 1
in2 = (X - s / 2) ** 2 + Y ** 2 < 1
ax.imshow(np.where(in1 & in2, np.cos(4 * np.pi * 1.0 * s * X), np.nan), extent=ext, origin="lower",
          cmap=LinearSegmentedColormap.from_list("ph", [F.SURF, F.BLEU]), alpha=0.55, vmin=-1, vmax=1, zorder=1)
ax.imshow(np.where(in1 & ~in2, 1.0, np.nan), extent=ext, origin="lower",
          cmap=LinearSegmentedColormap.from_list("o", [F.ORANGE, F.ORANGE]), alpha=0.32, zorder=1)
ax.imshow(np.where(in2 & ~in1, 1.0, np.nan), extent=ext, origin="lower",
          cmap=LinearSegmentedColormap.from_list("o2", [F.JAUNE, F.JAUNE]), alpha=0.32, zorder=1)
F.cercle(ax, (-s / 2, 0), 1, color=F.INK2, lw=1.2)
F.cercle(ax, (s / 2, 0), 1, color=F.INK2, lw=1.2)
F.point(ax, 0, 0, F.INK, 6.5, 7)
ax.text(0.06, -0.1, "C", fontsize=9.5, va="top")
th = np.radians(np.linspace(160, -14, 200))
ax.plot(1.12 * np.cos(th), 1.12 * np.sin(th), color=F.INK2, lw=1.1, zorder=6)
ax.annotate("", xy=(1.12 * np.cos(np.radians(-20)), 1.12 * np.sin(np.radians(-20))),
            xytext=(1.12 * np.cos(np.radians(-12)), 1.12 * np.sin(np.radians(-12))),
            arrowprops=dict(arrowstyle="-|>", color=F.INK2, lw=1.1, mutation_scale=13), zorder=6)
ax.text(-1.0, -0.22, "ménisque 1", ha="center", fontsize=9.5)
ax.text(1.0, 0.14, "ménisque 2", ha="center", fontsize=9.5)
ax.text(0, 1.2, "rotation de 180° autour de C : x ↦ −x", ha="center", fontsize=9.5, color=F.INK)
ax.text(-1.62, -1.15, f"Une pupille et la même, décalée de s = {s:.3f} :\n".replace(".", ",")
        + "leur partie commune est la lentille de la chèvre.\n"
        "À ce décalage, lentille = ménisque = π/2 : la FTM50.\n"
        "Rayures : le déphasage de défocalisation, linéaire\n"
        "sur la lentille (formule de Hopkins).", fontsize=9, color=F.INK2, va="top")
schema(ax, (-1.75, 1.75), (-1.95, 1.35))
ax.set_title("c)  Les deux ménisques conjugués de la FTM")

# d) la FTO défocalisée (la FTM avec son signe)
ax = axs[1, 0]
nus = np.linspace(0, 1, 401)
for w, coul in ((0.0, F.INK), (0.5, F.RAMPE[0]), (0.75, F.RAMPE[2]), (1.0, F.RAMPE[3]), (2.0, F.RAMPE[4])):
    o = np.array([ftm(n, w) for n in nus])
    ax.plot(nus, o, color=coul, lw=1.7, label=f"W₂₀ = {w:g} λ".replace(".", ","))
    ax.fill_between(nus, 0, o, where=o < 0, color=F.ORANGE, alpha=0.3, lw=0)
ax.axhline(0, color=F.MUTED, lw=0.9)
F.point(ax, s50 / 2, 0.5, F.INK, 6.5)
ax.annotate("FTM50 : lentille = ménisque\n(la condition de la chèvre)", xy=(s50 / 2, 0.5), xytext=(0.5, 0.62), fontsize=9,
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.text(0.3, -0.13, f"au-delà de W₂₀ = {w_seuil:.2f} λ, la FTO passe sous 0 :\n".replace(".", ",")
        + "contraste inversé, le noir d'une mire devient blanc", fontsize=9, color=F.ORANGE, va="center")
ax.set_xlim(0, 1)
ax.set_ylim(-0.2, 1.03)
ax.set_xlabel("fréquence / fréquence de coupure  (ν/ν_c = s/2)")
ax.set_ylabel("FTO (FTM avec son signe) = TF de la lentille")
ax.set_title("d)  La FTO défocalisée : sous zéro, l'image s'inverse")
ax.legend(fontsize=9, loc="upper right")

# e) une facette géodésique est un ménisque de phase
ax = axs[1, 1]
t = np.linspace(np.radians(8), np.radians(172), 400)
ax.plot(np.cos(t), np.sin(t), color=F.BLEU, lw=1.6)
angs = np.radians([15, 65, 115, 165])
for a1, a2 in zip(angs[:-1], angs[1:]):
    tt = np.linspace(a1, a2, 80)
    ax.add_patch(Polygon(np.c_[np.cos(tt), np.sin(tt)], closed=True, fc=F.BLEU, alpha=0.22, ec="none"))
    ax.plot([np.cos(a1), np.cos(a2)], [np.sin(a1), np.sin(a2)], color=F.INK, lw=1.8)
    m, d0 = (a1 + a2) / 2, np.cos((a2 - a1) / 2)
    for k in (1, 2):  # tranches de λ/2 (exagérées) dans chaque ménisque
        dk = d0 + k * (1 - d0) / 3
        hw = np.sqrt(1 - dk ** 2)
        ax.plot([dk * np.cos(m) - hw * np.sin(m), dk * np.cos(m) + hw * np.sin(m)],
                [dk * np.sin(m) + hw * np.cos(m), dk * np.sin(m) - hw * np.cos(m)], color=F.BLEU, lw=0.7, alpha=0.75)
    for c_ in (0.12, 0.5, 0.88):
        p_ = (1 - c_) * np.array([np.cos(a1), np.sin(a1)]) + c_ * np.array([np.cos(a2), np.sin(a2)])
        ax.plot([0, p_[0]], [0, p_[1]], color=F.ORANGE, lw=0.8, alpha=0.7)
F.point(ax, 0, 0, F.ORANGE, 7)
ax.text(0.07, -0.04, "O : centre de la sphère = foyer", fontsize=9, va="top")
ax.annotate("facette plane", xy=(0.12, 0.905), xytext=(0.32, 1.13), fontsize=9, arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.annotate("onde sphérique qui converge vers O", xy=(np.cos(np.radians(150)), np.sin(np.radians(150))), xytext=(-1.18, 1.13),
            fontsize=9, arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.text(-1.18, -0.2, "Sur une onde qui converge vers O, chaque facette retarde la\n"
        "lumière de l'épaisseur de son ménisque : c'est le ménisque du\n"
        "panneau b, découpé en triangles au lieu d'anneaux.\n"
        f"Le plus épais vaut ≈ {MEN[34] * 34 ** 2:.2f} R/ν² ; de ν = F_k à F_(k+1),\n".replace(".", ",")
        + "il est divisé par (F_(k+1)/F_k)², qui tend vers φ².\n"
        "(schéma : trois facettes très agrandies)", fontsize=9, color=F.INK2, va="top")
schema(ax, (-1.22, 1.22), (-0.95, 1.22))
ax.set_title("e)  Une facette géodésique est un ménisque de phase")

# f) l'œil de poisson de Maxwell
ax = axs[1, 2]
V3 = A.polyedre("geo3")
aretes = set()
for simp in ConvexHull(V3).simplices:
    for i, j in ((0, 1), (1, 2), (0, 2)):
        aretes.add(tuple(sorted((simp[i], simp[j]))))
for i, j in aretes:
    a, b = V3[i], V3[j]
    om = np.arccos(np.clip(a @ b, -1, 1))
    tt = np.linspace(0, 1, 30)[:, None]
    arc = (np.sin((1 - tt) * om) * a + np.sin(tt * om) * b) / np.sin(om)
    if arc[:, 2].max() > 0.75:
        continue
    pr = arc[:, :2] / (1 - arc[:, 2:3])  # projection stéréographique depuis le pôle nord
    ax.plot(pr[:, 0], pr[:, 1], color=F.BASE, lw=0.7, zorder=1)
F.cercle(ax, (0, 0), 1, color=F.INK2, lw=1.2, ls=(0, (5, 3)))
for R_ in RAYONS:
    ax.plot(R_[0], R_[1], color=F.BLEU, lw=1.1, alpha=0.85, zorder=3)
F.point(ax, *P, F.INK, 7, 6)
F.point(ax, *Pp, F.ORANGE, 8, 6)
ax.text(P[0] + 0.08, P[1] + 0.06, "P", fontsize=10.5, fontweight="bold", bbox=FOND, zorder=7)
ax.text(Pp[0] - 0.12, Pp[1] - 0.13, "P' = −P/|P|²", fontsize=10, ha="right", va="top", bbox=FOND, zorder=7)
ax.text(-2.75, 2.35, "Indice n = 2/(1 + r²) : tous les rayons partis de P\nse retrouvent en P', de l'autre côté du centre.\n"
        "En gris : les arêtes de la sphère géodésique ν = 3,\nprojetées : ce sont des morceaux de rayons.",
        fontsize=9, color=F.INK2, va="top", bbox=FOND, zorder=7)
ax.text(0.62, -1.05, "sur le cercle |x| = R :\nP' = −P, la rotation de 180°", fontsize=9, color=F.INK2, va="top", bbox=FOND, zorder=7)
schema(ax, (-2.8, 2.45), (-2.5, 2.4))
ax.set_title("f)  Les géodésiques sont des rayons : l'œil de poisson de Maxwell")
F.sauver(fig, "h1_foyer_menisques.png")

# ===========================================================================
# Figure h2 : Fibonacci
# ===========================================================================
fig, axs = plt.subplots(2, 2, figsize=(15.5, 11.4), gridspec_kw={"wspace": 0.2, "hspace": 0.3})

# a) le diaphragme de Fibonacci
ax = axs[0, 0]
w55 = mot_fibonacci(9)
for k in range(len(w55) - 1, -1, -1):
    ax.add_patch(Circle((0, 0), np.sqrt((k + 1) / len(w55)), fc=F.INK if w55[k] == "A" else F.SURF, ec="none"))
ax.add_patch(Circle((0, 0), 1, fill=False, ec=F.MUTED, lw=1))
ax.text(1.15, 0.55, "anneaux transparents (noirs) et opaques\nselon le mot de Fibonacci :\nA B A A B A B A A B …", fontsize=9.5,
        color=F.INK2, va="center")
ax.text(1.15, -0.4, "rayons en √k, comme les zones de Fresnel\net les anneaux de Newton :\nseul l'ordre des anneaux change",
        fontsize=9.5, color=F.INK2, va="center")
ax.set_xlim(-1.1, 3.3)
ax.set_ylim(-1.54, 1.54)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("a)  Un diaphragme de Fibonacci (55 anneaux)")

# b) deux foyers
ax = axs[0, 1]
q144 = np.array([c == "A" for c in mot_fibonacci(11)], float)
uu = np.linspace(0.3, 143.7, 60 * 144)
I144 = intensite_axe(q144, uu)
ax.plot(up, Ip / Ip.max(), color=F.MUTED, lw=1.2, label="lame périodique (Fresnel) : un foyer, en N/2")
ax.plot(uu, I144 / I144.max(), color=F.BLEU, lw=1.6, label="lame de Fibonacci : deux foyers égaux")
_, u1, u2 = FOYERS[11]
for x_, lab in ((u1, "55"), (u2, "89")):
    ax.text(x_, 1.03, lab, ha="center", fontsize=9.5)
ax.annotate("", xy=(u1, 1.13), xytext=(72, 1.13), arrowprops=dict(arrowstyle="<->", color=F.INK2, lw=0.9))
ax.annotate("", xy=(u2, 1.13), xytext=(72, 1.13), arrowprops=dict(arrowstyle="<->", color=F.INK2, lw=0.9))
ax.text(72, 1.17, "symétriques autour de N/2 = 72", ha="center", fontsize=9, color=F.INK2)
ax.text(118, 0.55, f"89/55 → φ\nrapport mesuré {u2 / u1:.4f}".replace(".", ","), ha="center", fontsize=9.5)
ax.set_xlim(0, 144)
ax.set_ylim(0, 1.55)
ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_xlabel("u = a² / (2λz)   (proportionnel à 1/distance)")
ax.set_ylabel("intensité sur l'axe (normalisée)")
ax.set_title("b)  Le second foyer : 144 anneaux, deux foyers dans le rapport φ")
ax.legend(fontsize=9, loc="upper left")

# c) géodésiques
ax = axs[1, 0]
nf = sorted(GEO)
nd = sorted(DOUBLE)
ax.loglog(nf, [GEO[n][1] for n in nf], "-o", color=F.BLEU, ms=6, mec=F.SURF, label="géodésique, ν de Fibonacci (1, 2, 3, 5, 8…)")
ax.loglog(nd, [DOUBLE[n] for n in nd], "--D", color=F.INK2, ms=4.5, mec=F.SURF, label="géodésique, ν doublé (partie II : 2, 4, 8…)")
ax.loglog(nf, [GEO[n][2] for n in nf], ":s", color=F.AQUA, ms=5, mec=F.SURF, label="grille de Fibonacci (angle d'or), même N")
ax.set_xticks(nf)
ax.set_xticklabels([str(n) for n in nf])
ax.minorticks_off()
ax.text(1.1, 1.3e-3, "pente −2 : le volume manquant suit 1/ν².\nFibonacci : ÷ φ² = 2,618 par pas.\nDoublement : ÷ 4 par pas.\n"
        "La grille de Fibonacci manque\nenviron 6 % de plus.", fontsize=9.3, color=F.INK, va="bottom")
ax.set_xlabel("fréquence de subdivision ν")
ax.set_ylabel("volume manquant (sphère unité)")
ax.set_title("c)  La découpe géodésique au rythme de Fibonacci")
ax.legend(fontsize=9, loc="upper right")

# d) convergences vers φ et φ²
ax = axs[1, 1]
js = sorted(FOYERS)
ax.loglog([FOYERS[j][0] for j in js], [abs(FOYERS[j][2] / FOYERS[j][1] - PHI) for j in js], "-o", color=F.BLEU, ms=6, mec=F.SURF,
          label="lentille à N anneaux : |u₂/u₁ − φ|")
kk = list(zip(nf[2:-1], nf[3:]))
ax.loglog([b_ for _, b_ in kk], [abs(GEO[a_][1] / GEO[b_][1] - PHI ** 2) for a_, b_ in kk], "-s", color=F.AQUA, ms=5.5, mec=F.SURF,
          label="géodésique : |rapport des volumes manquants − φ²|")
fib = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
ax.loglog(fib[1:], [abs(b_ / a_ - PHI) for a_, b_ in zip(fib[:-1], fib[1:])], ":", color=F.MUTED, lw=1.4,
          label="|F_(k+1)/F_k − φ|, pour comparer")
ax.set_xticks(fib[1:])
ax.set_xticklabels([str(v) for v in fib[1:]], fontsize=8.5)
ax.minorticks_off()
ax.set_xlabel("nombre de Fibonacci atteint (N anneaux, ou fréquence ν)")
ax.set_ylabel("écart à la limite")
ax.set_title("d)  Deux suites qui convergent vers φ et φ²")
ax.legend(fontsize=9, loc="lower left")
F.sauver(fig, "h2_fibonacci.png")
