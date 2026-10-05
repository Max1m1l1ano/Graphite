"""
Partie IX : le moiré du diaphragme de Fibonacci, l'équation d'optique et les racines de l'unité.

    python3 scripts/moire_fibonacci.py        # ≈ 1 min

Écrit resultats/moire_fibonacci.md, figures/i1_moire_fibonacci.png et figures/i2_optique_racines.png.

1. Le moiré : un diaphragme échantillonné sur la grille des pixels montre de nouveaux centres en
   (m, n)·R²/(2u) pixels pour chaque composante u de ses anneaux (R : rayon du disque en pixels).
2. Deux familles de centres pour le diaphragme de Fibonacci, dans le rapport φ ; une seule pour Fresnel.
3. Mesure : spectre local le long de l'axe, et filtre adapté qui localise les centres.
4. L'équation d'optique : les deux foyers de Fibonacci sont conjugués, 1/φ + 1/φ² = 1, Fermat pour n ≥ 3.
5. Les racines dixièmes de l'unité, le pentagone, et la chèvre entre le triangle et le pentagone.
6. Hurwitz : φ est le nombre que les fractions approchent le plus mal.
"""

import logging
import os
import sys
from fractions import Fraction

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon
from scipy.ndimage import gaussian_filter
from scipy.optimize import brentq, minimize_scalar
from scipy.signal import find_peaks

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
PHI = (1 + 5 ** 0.5) / 2
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


# ---------------------------------------------------------------------------
# Les diaphragmes (mêmes conventions que la partie VIII)
# ---------------------------------------------------------------------------
def mot_fibonacci(j):
    """S₀ = B, S₁ = A, S_(j+1) = S_j S_(j−1) ; A = anneau transparent, B = opaque."""
    S = ["B", "A"]
    for _ in range(2, j + 1):
        S.append(S[-1] + S[-2])
    return S[j]


def intensite_axe(q, u):
    """Intensité sur l'axe (Fresnel) d'un diaphragme de N zones égales en ζ = (r/a)², u = a²/(2λz)."""
    N = len(q)
    z = np.exp(-2j * np.pi * np.asarray(u, float) / N)
    Q = np.zeros_like(z)
    for t in q[::-1]:
        Q = Q * z + t
    return 4 * np.sin(np.pi * np.asarray(u, float) / N) ** 2 * np.abs(Q) ** 2


def deux_foyers(q):
    N = len(q)
    u = np.linspace(0.3, N - 0.3, 60 * N)
    I = intensite_axe(q, u)
    pics, _ = find_peaks(I)
    deux = sorted(pics[np.argsort(I[pics])[-2:]])
    return [minimize_scalar(lambda x: -intensite_axe(q, x), bounds=(u[k - 1], u[k + 1]), method="bounded",
                            options={"xatol": 1e-11}).x for k in deux]


def plaque(q, R, n):
    """Le diaphragme de rayon R pixels, échantillonné au centre des pixels (n impair : un pixel au centre)."""
    c = (n - 1) / 2
    y, x = np.mgrid[0:n, 0:n] - c
    k = np.floor(len(q) * (x * x + y * y) / R ** 2).astype(int)
    out = np.zeros((n, n))
    dedans = k < len(q)
    out[dedans] = np.asarray(q, float)[k[dedans]]
    return out


def taille(R):
    n = int(2 * R + 41)
    return n + (n % 2 == 0)


Q55 = np.array([c == "A" for c in mot_fibonacci(9)], float)
Q144 = np.array([c == "A" for c in mot_fibonacci(11)], float)
QF55 = np.array([k % 2 == 0 for k in range(55)], float)  # lame de Fresnel ordinaire, 55 zones
U = {55: deux_foyers(Q55), 144: deux_foyers(Q144)}

# ---------------------------------------------------------------------------
# 1. La loi des centres fantômes
# ---------------------------------------------------------------------------
ligne("## 1. Où apparaissent les nouveaux centres\n")
ligne("Une composante cos(2πu·r²/R²) des anneaux, échantillonnée sur la grille des pixels, prend aux pixels exactement les"
      " mêmes valeurs qu'un motif identique centré en (m, n)·R²/(2u) pixels : u·(x² − (x − x_m)²)/R² diffère d'un entier"
      " quand x est entier. En unités du rayon a du disque : x_m/a = m·R/(2u).")
i = np.arange(-400, 401)
pire = 0
for u_, R_ in ((33.916, 36), (21.084, 50), (88.968, 120)):
    xm = R_ * R_ / (2 * u_)
    a1 = np.cos(2 * np.pi * u_ * i ** 2 / R_ ** 2)
    a2 = np.cos(2 * np.pi * u_ * (i - xm) ** 2 / R_ ** 2 - 2 * np.pi * u_ * xm ** 2 / R_ ** 2)
    pire = max(pire, np.max(np.abs(a1 - a2)))
ligne(f"Contrôle de l'identité sur 801 pixels : écart maximal {pire:.1e}.\n")
u1, u2 = U[55]
ligne(f"Diaphragme de Fibonacci à 55 anneaux : composantes principales u₁ = {fr(u1)} et u₂ = {fr(u2)} (ses deux foyers,"
      f" partie VIII), rapport {fr(u2 / u1, '{:.6f}')}. Lame de Fresnel ordinaire à 55 zones : u = 27,5.\n")
ligne("| rayon R (pixels) | famille u₂ (axes) | famille u₁ (axes) | u₂, diagonales | u₁, diagonales | Fresnel (axes) |")
ligne("|---:|---|---|---|---|---|")
for R in (30, 36, 45, 60, 80, 100):
    cases = []
    for v in (R / (2 * u2), R / (2 * u1), 2 ** 0.5 * R / (2 * u2), 2 ** 0.5 * R / (2 * u1), R / 55):
        cases.append(f"{fr(v, '{:.3f}')} a" + ("" if v < 1 else " (dehors)"))
    ligne(f"| {R} | " + " | ".join(cases) + " |")
ligne(f"\nUne famille sort du disque quand R dépasse 2u (axes) ou √2·u (diagonales) : u₂ sort à R = {fr(2 * u2, '{:.1f}')} px,"
      f" u₁ à R = {fr(2 * u1, '{:.1f}')} px. Le rapport des deux seuils vaut u₂/u₁ → φ.")
ligne("Les deux familles vérifient l'équation des lentilles : 1/x₁ + 1/x₂ = 2(u₁ + u₂)/R = 2N/R = 2/x_F, où x_F = R/N"
      " est la famille de la lame de Fresnel ordinaire.")


# ---------------------------------------------------------------------------
# 2. La mesure : un filtre adapté qui cherche les centres d'anneaux
# ---------------------------------------------------------------------------
def score_axe(R, q, u, sig=1.0, fac=0.06):
    """Ressemblance locale de l'image (adoucie comme par l'œil ou l'écran) avec des anneaux de loi u centrés en x0."""
    n = taille(R)
    S = plaque(q, R, n)
    c = (n - 1) / 2
    L = gaussian_filter(S - S.mean(), sig)
    sw = max(2.5, fac * R * R / u)
    W = int(3 * sw) + 1
    k = np.arange(-W, W + 1)
    Y, Xo = np.meshgrid(k, k, indexing="ij")
    xs = np.arange(3, R, 0.1)
    out = []
    for x0 in xs:
        j0 = int(round(x0))
        X = Xo + j0 - x0
        G = np.exp(-(X ** 2 + Y ** 2) / (2 * sw ** 2))
        I_, J_ = (c + Y).astype(int), (c + Xo + j0).astype(int)
        blk = L[np.clip(I_, 0, n - 1), np.clip(J_, 0, n - 1)] * (J_ < n)
        num = np.abs(np.sum(G * blk * np.exp(2j * np.pi * u * (X ** 2 + Y ** 2) / R ** 2)))
        out.append(num / (np.sqrt(np.sum(G * blk ** 2) * np.sum(G)) + 1e-12))
    return xs, np.array(out)


def centres_mesures(R, q, us):
    trouves = []
    for u in us:
        xs, sc = score_axe(R, q, u)
        pk, _ = find_peaks(sc, prominence=0.05)
        trouves += [xs[p] for p in pk]
    return np.array(sorted(trouves))


ligne("\n## 2. Mesure des centres sur les images échantillonnées\n")
ligne("Filtre adapté le long de l'axe (image adoucie par un flou gaussien d'un pixel) ; on garde le centre détecté le plus"
      " proche de chaque prédiction, à 1,5 pixel près.\n")
ligne("| anneaux | R (px) | famille | centre prédit (px) | centre mesuré (px) | écart (px) |")
ligne("|---:|---:|---|---:|---:|---:|")
MESURES = {55: [], 144: []}
for N_, q_, Rs in ((55, Q55, (30, 36, 40, 44, 50, 56, 60, 64)), (144, Q144, (90, 100, 110, 120, 130))):
    for R in Rs:
        trouves = centres_mesures(R, q_, U[N_])
        for nom, u in (("u₂", U[N_][1]), ("u₁", U[N_][0])):
            xp = R * R / (2 * u)
            if xp > 0.95 * R:
                continue
            d = np.abs(trouves - xp) if len(trouves) else np.array([np.inf])
            ok = d.min() <= 1.5
            if ok:
                MESURES[N_].append((R, nom, xp, trouves[d.argmin()]))
            ligne(f"| {N_} | {R} | {nom} | {fr(xp, '{:.1f}')} | {fr(trouves[d.argmin()], '{:.1f}') if ok else 'non trouvé'} |"
                  f" {fr(trouves[d.argmin()] - xp, '{:+.1f}') if ok else ''} |")
ecarts = [abs(m - p) for v in MESURES.values() for _, _, p, m in v]
ligne(f"\n{len(ecarts)} centres retrouvés ; écart moyen {fr(np.mean(ecarts), '{:.2f}')} px, écart maximal {fr(max(ecarts), '{:.2f}')} px.")


# ---------------------------------------------------------------------------
# 3. L'équation d'optique
# ---------------------------------------------------------------------------
ligne("\n## 3. L'équation d'optique, φ et Fermat\n")
ligne("Distances focales de la lentille de Fibonacci, en unités de z_N = a²/(2λN), la moitié du foyer de la lame de Fresnel"
      " ordinaire :\n")
ligne("| anneaux N | z₁ (foyer lointain) | z₂ (foyer proche) | 1/z₁ + 1/z₂ | grandissement −z₁/z₂ |")
ligne("|---:|---|---|---|---|")
for j in (9, 10, 11, 12, 13, 14):
    q = np.array([c == "A" for c in mot_fibonacci(j)], float)
    a_, b_ = deux_foyers(q)
    N = len(q)
    ligne(f"| {N} | {fr(N / a_, '{:.6f}')} | {fr(N / b_, '{:.6f}')} | {fr(a_ / N + b_ / N, '{:.6f}')} | {fr(-b_ / a_, '{:.6f}')} |")
ligne(f"\nLimites : φ² = {fr(PHI ** 2, '{:.6f}')} et φ = {fr(PHI, '{:.6f}')} ; 1/φ² + 1/φ = {fr(1 / PHI ** 2 + 1 / PHI, '{:.12f}')}.")
ligne("Une lentille de focale 1 forme l'image d'un objet placé à φ à la distance φ², retournée et agrandie φ fois.")
ligne("\nSolutions entières de 1/aⁿ + 1/bⁿ = 1/cⁿ (a ≤ b ≤ 300) :")
for n in (1, 2, 3):
    sols = []
    for a in range(1, 301):
        for b in range(a, 301):
            c = Fraction(1, a ** n) + Fraction(1, b ** n)
            if c.numerator == 1:
                r = round(c.denominator ** (1 / n))
                if r ** n == c.denominator:
                    sols.append((a, b, r))
    prim = [s for s in sols if np.gcd.reduce(s) == 1]
    ligne(f"- n = {n} : {len(sols)} solutions, dont {len(prim)} primitives ; premières : {prim[:5]}")

# ---------------------------------------------------------------------------
# 4. Les racines de l'unité, le pentagone et la chèvre
# ---------------------------------------------------------------------------
ligne("\n## 4. Les racines de l'unité, le pentagone et la chèvre\n")
z = np.exp(1j * np.pi / 5)
forme = (1 + 5 ** 0.5) / 4 + 1j * np.sqrt(5 / 8 - 5 ** 0.5 / 8)
ligne(f"(−1)^(1/5) = e^(iπ/5) = (1 + √5)/4 + i·√(5/8 − √5/8) : écart {abs(z - forme):.1e}.")
ligne("Racines dixièmes de l'unité autres que ±1 (huit) : parties réelles ±φ/2 = ±0,8090 et ±1/(2φ) = ±0,3090.")


def lentille(r):
    """Aire broutée (pré de rayon 1, piquet sur le bord, corde r)."""
    return r * r * np.arccos(r / 2) + np.arccos(1 - r * r / 2) - (r / 2) * np.sqrt(4 - r * r)


r_chevre = brentq(lambda r: lentille(r) - np.pi / 2, 1, 1.4, xtol=1e-15)
CAS = [("triangle (simplexe)", 2 / 3 ** 0.5), ("chèvre", r_chevre), ("pentagone", 2 * np.sin(np.pi / 5))]
ligne("\n| corde | r | α = arccos(r/2) | β = 2α | part broutée |")
ligne("|---|---|---|---|---|")
for nom, r in CAS:
    al = np.degrees(np.arccos(r / 2))
    ligne(f"| {nom} | {fr(r, '{:.6f}')} | {fr(al, '{:.4f}')}° | {fr(2 * al, '{:.4f}')}° | {fr(100 * lentille(r) / np.pi, '{:.3f}')} % |")
ligne(f"\nPentagone : r² = 4 sin²36° = 3 − φ = {fr(3 - PHI, '{:.6f}')} ; part broutée exacte (13 − 3φ)/10 − sin 72°/π ="
      f" {fr(100 * ((13 - 3 * PHI) / 10 - np.sin(2 * np.pi / 5) / np.pi), '{:.3f}')} %.")

# ---------------------------------------------------------------------------
# 5. Hurwitz
# ---------------------------------------------------------------------------
ligne("\n## 5. φ, le nombre le plus mal approché par des fractions (Hurwitz)\n")
ligne("| fraction p/q | q²·|x − p/q| |")
ligne("|---|---|")
fib = [1, 1]
while len(fib) < 16:
    fib.append(fib[-1] + fib[-2])
for k in (4, 7, 10, 14):
    p, q = fib[k + 1], fib[k]
    ligne(f"| φ ≈ {p}/{q} | {fr(q * q * abs(PHI - p / q), '{:.6f}')} |")
for p, q in ((22, 7), (333, 106), (355, 113)):
    ligne(f"| π ≈ {p}/{q} | {fr(q * q * abs(np.pi - p / q), '{:.6f}')} |")
ligne(f"\nPour φ, la valeur tend vers 1/√5 = {fr(1 / 5 ** 0.5, '{:.6f}')} : aucune fraction ne fait mieux à long terme"
      " (théorème de Hurwitz, 1891).")

with open(os.path.join(ICI, "..", "resultats", "moire_fibonacci.md"), "w") as fh:
    fh.write("# Résultats de la partie IX (générés par scripts/moire_fibonacci.py)\n\n" + "\n".join(md) + "\n")


# ===========================================================================
# Figure i1 : le moiré du diaphragme de Fibonacci
# ===========================================================================
def montrer(ax, q, R, vue=1.3):
    n = taille(R)
    S = plaque(q, R, n)
    c = (n - 1) / 2
    ext = (-(c + 0.5) / R, (c + 0.5) / R, -(c + 0.5) / R, (c + 0.5) / R)
    ax.imshow(1 - S, cmap="gray", vmin=0, vmax=1, interpolation="nearest", extent=ext, origin="lower")
    ax.set_xlim(-vue, vue)
    ax.set_ylim(-vue, vue)
    ax.set_aspect("equal")
    ax.axis("off")


def marquer(ax, R, u, couleur, diag=True, taille_=0.07, lw=1.6):
    x0 = R / (2 * u)
    pts = [(x0, 0), (-x0, 0), (0, x0), (0, -x0)]
    if diag:
        pts += [(x0, x0), (-x0, x0), (x0, -x0), (-x0, -x0)]
    for p in pts:
        ax.add_patch(Circle(p, taille_, fill=False, ec=couleur, lw=lw, zorder=5))


fig = plt.figure(figsize=(20, 12.6))
gs = fig.add_gridspec(2, 3, wspace=0.14, hspace=0.22)

# a) R = 36
ax = fig.add_subplot(gs[0, 0])
montrer(ax, Q55, 36, vue=1.12)
marquer(ax, 36, u2, F.BLEU)
marquer(ax, 36, u1, F.ORANGE, diag=False)
F.cercle(ax, (0, 0), 1, color=F.MUTED, lw=1, ls=(0, (4, 3)))
ax.text(-1.1, -1.18, "cercles bleus : famille u₂ (foyer proche) ; orange : famille u₁ (foyer lointain)", fontsize=9,
        color=F.INK2, va="top")
ax.set_title("a)  Fibonacci à 36 pixels de rayon (ta 1ʳᵉ capture)", pad=10)

# b) quatre tailles
sub = gs[0, 1].subgridspec(2, 2, wspace=0.05, hspace=0.18)
for k, R in enumerate((30, 45, 60, 80)):
    ax = fig.add_subplot(sub[k // 2, k % 2])
    montrer(ax, Q55, R, vue=1.32)
    for u, coul in ((u2, F.BLEU), (u1, F.ORANGE)):
        marquer(ax, R, u, coul, diag=(u == u2), taille_=0.09, lw=1.3)
    F.cercle(ax, (0, 0), 1, color=F.MUTED, lw=0.8, ls=(0, (4, 3)))
    ax.set_title(f"R = {R} px" + (" (ta 2ᵉ capture)" if R == 80 else ""), fontsize=10, fontweight="normal", loc="center")
    if k == 0:
        ax.text(-1.32, 1.62, "b)  Quand on agrandit, les centres s'en vont", fontsize=11.5, fontweight="bold", color=F.INK)

# c) spectre local le long de l'axe
ax = fig.add_subplot(gs[0, 2])
R = 60
ii = np.arange(-R, R + 1)
k_ = np.floor(55 * ii * ii / R ** 2).astype(int)
row = np.where(k_ < 55, Q55[np.minimum(k_, 54)], 0.0)
Lw, nfft = 16, 512
w = np.hanning(Lw)
spec = []
for c0 in range(len(row)):
    seg = np.array([row[j] if 0 <= j < len(row) else 0.0 for j in range(c0 - Lw // 2, c0 - Lw // 2 + Lw)])
    seg = (seg - np.sum(seg * w) / np.sum(w)) * w
    spec.append(np.abs(np.fft.rfft(seg, nfft)))
spec = np.array(spec)
ax.imshow(spec.T, origin="lower", aspect="auto", extent=(-1, 1, 0, 0.5), cmap="Greys", vmax=np.percentile(spec, 99.5))
xx = np.linspace(-1, 1, 801)
for u, coul in ((u1, F.ORANGE), (u2, F.BLEU)):
    fl = 2 * u * np.abs(xx) / R  # fréquence locale, en cycles par pixel : 2u·x/R² avec x = (x/a)·R pixels
    ax.plot(xx, np.abs(fl - np.round(fl)), color=coul, lw=1.4)
    for m in (1, -1):
        ax.axvline(m * R / (2 * u), color=coul, lw=1, ls=":")
ax.set_xlim(-1, 1)
ax.set_ylim(0, 0.5)
ax.grid(False)
ax.set_xlabel("position sur l'axe (x/a), R = 60 px")
ax.set_ylabel("fréquence des franges vues (cycles par pixel)")
ax.text(0.02, 0.47, "gris : spectre mesuré sur l'image ;\ntraits : repliement prévu des deux composantes", fontsize=9,
        color=F.INK2, va="top", ha="center", bbox=dict(fc=F.SURF, ec="none", alpha=0.85))
ax.set_title("c)  La mesure : les franges suivent le repliement prévu")

# d) positions en fonction de la taille
ax = fig.add_subplot(gs[1, 0])
Rr = np.linspace(10, 110, 300)
ax.axhspan(1, 1.6, color=F.GRID, alpha=0.6, lw=0)
ax.text(12, 1.55, "hors du disque", fontsize=9, color=F.INK2, va="top")
ax.plot(Rr, Rr / (2 * u2), color=F.BLEU, lw=1.8, label="famille u₂, axes")
ax.plot(Rr, Rr / (2 * u1), color=F.ORANGE, lw=1.8, label="famille u₁, axes")
ax.plot(Rr, 2 ** 0.5 * Rr / (2 * u2), color=F.BLEU, lw=1.2, ls="--", label="famille u₂, diagonales")
ax.plot(Rr, Rr / 55, color=F.MUTED, lw=1.2, ls=":", label="lame de Fresnel ordinaire")
for R_, nom, xp, xm in MESURES[55]:
    F.point(ax, R_, xm / R_, F.BLEU if nom == "u₂" else F.ORANGE, 6)
ax.plot([], [], "o", color=F.INK2, ms=5, mec=F.SURF, label="centres mesurés (filtre adapté)")
for R_, lab in ((36, "1ʳᵉ capture"), (80, "2ᵉ capture")):
    ax.axvline(R_, color=F.INK2, lw=0.9, ls=(0, (2, 2)))
    ax.text(R_ + 1, 0.05, lab, fontsize=9, color=F.INK2, rotation=90, va="bottom")
ax.set_xlim(10, 110)
ax.set_ylim(0, 1.6)
ax.set_xlabel("rayon du disque à l'écran, R (pixels)")
ax.set_ylabel("position du centre fantôme, x/a")
ax.legend(fontsize=9, loc="center right", bbox_to_anchor=(1, 0.43), frameon=True, facecolor=F.SURF, edgecolor="none",
          framealpha=1, title=f"rapport des pentes u₂/u₁ = {u2 / u1:.4f} → φ".replace(".", ","), title_fontsize=9)
ax.set_title("d)  La loi : x/a = R/(2u), deux pentes")

# e) la lame de Fresnel ordinaire
ax = fig.add_subplot(gs[1, 1])
montrer(ax, QF55, 36, vue=1.12)
marquer(ax, 36, 27.5, F.AQUA)
F.cercle(ax, (0, 0), 1, color=F.MUTED, lw=1, ls=(0, (4, 3)))
ax.text(-1.1, -1.18, "une seule famille de centres (verts), en R/N = 0,655 a :\nla lame ordinaire n'a qu'un foyer",
        fontsize=9, color=F.INK2, va="top")
ax.set_title("e)  Pour comparer : la lame de Fresnel ordinaire, 36 px", pad=10)

# f) le prisme invisible
ax = fig.add_subplot(gs[1, 2])
R, u = 36, u2
xm = R * R / (2 * u)
xc = np.linspace(0, 36, 3000)
xi = np.arange(0, 37)
ax.plot(xc, (u * xc ** 2 / R ** 2) % 1, color=F.BASE, lw=0.8, label="anneaux centrés en 0")
ax.plot(xc, (u * (xc - xm) ** 2 / R ** 2 - u * xm ** 2 / R ** 2) % 1, color=F.BLEU, lw=0.9, alpha=0.8,
        label=f"anneaux centrés en {xm:.1f} px".replace(".", ","))
ax.plot(xi, (u * xi ** 2 / R ** 2) % 1, "o", color=F.INK, ms=4.5, mec=F.SURF, mew=0.8, label="les pixels : mêmes valeurs", zorder=5)
ax.axvline(xm, color=F.BLEU, lw=1, ls=":")
ax.set_xlim(8, 31)
ax.set_ylim(-0.02, 1.3)
ax.set_yticks([0, 0.5, 1])
ax.set_xlabel("pixel le long de l'axe (R = 36 px, composante u₂)")
ax.set_ylabel("phase des anneaux (en tours, modulo 1)")
ax.legend(fontsize=9, loc="upper left", ncol=1)
ax.text(30.7, 1.27, "La différence des deux phases\nvaut un nombre entier de tours\nà chaque pixel : un « prisme »\n"
        "que la grille ne voit pas.", fontsize=9, color=F.INK2, ha="right", va="top")
ax.set_title("f)  Pourquoi : un prisme invisible d'un tour par pixel")
F.sauver(fig, "i1_moire_fibonacci.png")

# ===========================================================================
# Figure i2 : l'équation d'optique, les racines de l'unité, la chèvre entre triangle et pentagone
# ===========================================================================
fig, axs = plt.subplots(1, 3, figsize=(20, 6.6), gridspec_kw={"wspace": 0.18})

# a) les échelles croisées
ax = axs[0]
z1, z2, d = PHI ** 2, PHI, 2.2
ax.plot([0, 0], [0, z1], color=F.ORANGE, lw=4, solid_capstyle="butt")
ax.plot([d, d], [0, z2], color=F.BLEU, lw=4, solid_capstyle="butt")
ax.plot([0, d], [z1, 0], color=F.INK2, lw=1.2)
ax.plot([0, d], [0, z2], color=F.INK2, lw=1.2)
xc_ = d * z1 / (z1 + z2)
F.point(ax, xc_, 1, F.INK, 7)
ax.plot([xc_, xc_], [0, 1], color=F.INK, lw=1, ls=":")
ax.axhline(0, color=F.BASE, lw=1)
ax.text(-0.1, z1, "z₁ = φ²\n(foyer lointain)", ha="right", va="center", fontsize=9.5)
ax.text(d + 0.1, z2, "z₂ = φ\n(foyer proche)", ha="left", va="center", fontsize=9.5)
ax.text(xc_ + 0.08, 1.05, "hauteur 1 = z_N", fontsize=9.5)
ax.text(-0.9, -0.35, "Les deux échelles se croisent à la hauteur c telle que 1/c = 1/z₁ + 1/z₂ :\n"
        "l'équation des lentilles. Avec φ² et φ, c = 1, car 1/φ² + 1/φ = 1 : c'est la\n"
        "définition même du nombre d'or. Une lentille de focale 1 envoie φ sur φ²,\n"
        "image renversée et agrandie φ fois. Les deux foyers de la lentille de Fibonacci\n"
        "sont ce couple d'objet et d'image (z_N : la moitié du foyer de Fresnel).", fontsize=9, color=F.INK2, va="top")
ax.set_xlim(-1.0, 3.2)
ax.set_ylim(-1.75, 2.85)
ax.set_aspect("equal", adjustable="datalim")
ax.axis("off")
ax.set_title("a)  Les foyers de Fibonacci sont conjugués")

# b) les racines dixièmes de l'unité
ax = axs[1]
F.cercle(ax, (0, 0), 1, color=F.MUTED, lw=1)
racines = np.exp(2j * np.pi * np.arange(10) / 10)
ax.add_patch(Polygon(np.c_[racines.real, racines.imag], closed=True, fill=False, ec=F.BASE, lw=1))
penta = racines[::2]
ax.add_patch(Polygon(np.c_[penta.real, penta.imag], closed=True, fill=False, ec=F.AQUA, lw=1.3))
for k, zr in enumerate(racines):
    reel = k in (0, 5)
    F.point(ax, zr.real, zr.imag, F.MUTED if reel else (F.ORANGE if k == 1 else F.BLEU), 7.5)
ax.plot([0, 1], [0, 0], color=F.BASE, lw=0.8)
ax.plot([np.cos(np.pi / 5)] * 2, [0, np.sin(np.pi / 5)], color=F.ORANGE, lw=1, ls=":")
ax.text(np.cos(np.pi / 5) + 0.06, np.sin(np.pi / 5) + 0.06, "e^(iπ/5) = (−1)^(1/5)", fontsize=9.5, color=F.ORANGE)
ax.text(0.45, -0.1, "φ/2", fontsize=9.5, ha="center", va="top")
ax.text(-1.45, -1.25, "Les huit racines dixièmes de l'unité autres que ±1 (bleu, orange)\n"
        "s'écrivent toutes avec √5 : parties réelles ±φ/2 et ±1/(2φ).\n"
        "e^(iπ/5) = (1 + √5)/4 + i·√(5/8 − √5/8) ; en vert, le pentagone.\n"
        "sin²36° = (5 − √5)/8 est la raison de la suite des trois solides\nissue du pentagone (partie IV).",
        fontsize=9, color=F.INK2, va="top")
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2.15, 1.35)
ax.set_aspect("equal", adjustable="datalim")
ax.axis("off")
ax.set_title("b)  Les racines de l'unité et le nombre d'or")

# c) la chèvre entre le triangle et le pentagone
ax = axs[2]
ang = {nom: np.degrees(np.arccos(r / 2)) for nom, r in CAS}
part = {nom: 100 * lentille(r) / np.pi for nom, r in CAS}
ax.axhline(0, color=F.BASE, lw=1.2)
for nom, coul, dy in (("pentagone", F.AQUA, 1), ("chèvre", F.INK, -1), ("triangle (simplexe)", F.ORANGE, 1)):
    F.point(ax, ang[nom], 0, coul, 9)
    lab = {"pentagone": f"pentagone : α = 54°\ncorde 2 sin 36° (φ)\n{part[nom]:.2f} % du pré",
           "chèvre": f"chèvre : α = {ang[nom]:.3f}°\ncorde {CAS[1][1]:.4f}\n50 % du pré",
           "triangle (simplexe)": f"triangle de l'aiguille :\nα = {ang[nom]:.3f}°, corde 2/√3\n{part[nom]:.2f} % du pré"}[nom]
    ax.annotate(lab.replace(".", ","), xy=(ang[nom], 0), xytext=(ang[nom], 0.55 * dy), ha="center",
                va="bottom" if dy > 0 else "top", fontsize=9, arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.set_xlim(53.75, 55.0)
ax.set_ylim(-1.35, 1.6)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.grid(False)
ax.set_xlabel("demi-angle α de la corde, r = 2 cos α (degrés)")
ax.text(53.78, -1.05, "La chèvre est 4 fois plus près du triangle (0,14°) que du pentagone (0,59°).\n"
        "En angle au centre β = 2α : 108° (pentagone), 109,19° (chèvre, la racine\n"
        "de la division d'Ullisch), 109,47° (l'angle du tétraèdre).", fontsize=9, color=F.INK2, va="top")
ax.set_title("c)  φ est voisin de la chèvre, pas dedans")
F.sauver(fig, "i2_optique_racines.png")
