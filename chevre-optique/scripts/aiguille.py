"""
Partie V : l'aiguille de Kakeya, l'arbre de Perron et la chèvre. Calculs et figure.

    python3 scripts/aiguille.py

Écrit resultats/aiguille.md et figures/e1_aiguille_kakeya.png.

Conventions : l'aiguille a la longueur 1. L'arbre de Perron part du triangle
équilatéral de hauteur 1 (base [0, 2/√3] sur l'axe x, sommet (1/√3, 1)),
coupé en 2^k triangles fins qu'on fait glisser le long de la base
(construction de Perron 1928, dans la version de Schoenberg 1962) : à chaque
étage, deux blocs voisins sont recollés puis rapprochés, de sorte que leur
triangle principal se réduit d'un rapport α_j.
"""

import os
import sys
import time

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from matplotlib.patches import Polygon

sys.path.insert(0, os.path.dirname(__file__))
import archimede as A  # noqa: E402
import chevre as ch  # noqa: E402
import figures as F  # noqa: E402  (style et palette des parties I à IV)

mp.mp.dps = 30
ICI = os.path.dirname(os.path.abspath(__file__))
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, d=10):
    return mp.nstr(x, d).replace(".", ",")


def shoelace(x, y):
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))


# ---------------------------------------------------------------------------
# 1. Les ensembles où l'on retourne une aiguille de longueur 1
# ---------------------------------------------------------------------------
t = np.linspace(0, 2 * np.pi, 200001)[:-1]
a = 0.25  # deltoïde : cercle roulant de rayon 1/4 dans un cercle de rayon 3/4
deltoide = (2 * a * np.cos(t) + a * np.cos(2 * t), 2 * a * np.sin(t) - a * np.sin(2 * t))


def reuleaux(n=4000):
    """Triangle de Reuleaux de largeur 1 : trois arcs de rayon 1 centrés aux sommets."""
    S = [np.array([np.cos(np.pi / 2 + 2 * np.pi * i / 3), np.sin(np.pi / 2 + 2 * np.pi * i / 3)]) / np.sqrt(3)
         for i in range(3)]
    xs, ys = [], []
    for i in range(3):
        c, p, q = S[i], S[(i + 1) % 3], S[(i + 2) % 3]
        a0, a1 = np.arctan2(*(p - c)[::-1]), np.arctan2(*(q - c)[::-1])
        if a1 < a0:
            a1 += 2 * np.pi
        th = np.linspace(a0, a1, n, endpoint=False)
        xs.append(c[0] + np.cos(th))
        ys.append(c[1] + np.sin(th))
    return np.concatenate(xs), np.concatenate(ys), S


rx, ry, _ = reuleaux()
ENSEMBLES = [  # nom, aire exacte (formule), aire exacte (valeur), contrôle numérique
    ("disque de diamètre 1", "π/4", mp.pi / 4, np.pi / 4),
    ("triangle de Reuleaux de largeur 1", "(π − √3)/2", (mp.pi - mp.sqrt(3)) / 2, shoelace(rx, ry)),
    ("triangle équilatéral de hauteur 1 (Pál)", "1/√3", 1 / mp.sqrt(3), 1 / np.sqrt(3)),
    ("deltoïde (Kakeya)", "π/8", mp.pi / 8, shoelace(*deltoide)),
]
ligne("## 1. Où retourner une aiguille de longueur 1\n")
ligne("| ensemble | aire | valeur | contrôle numérique | part du disque |")
ligne("|---|---|---|---|---|")
for nom, formule, v, num in ENSEMBLES:
    ligne(f"| {nom} | {formule} | {fr(v, 8)} | {num:.8f} | {fr(v / (mp.pi / 4), 6)} |".replace(".", ","))
# longueur des segments tangents au deltoïde : 4a = 1 pour tout paramètre
L = []
for s in np.linspace(0.1, 2.0, 7):
    # la tangente au point de paramètre s recoupe le deltoïde aux paramètres −s/2 et π − s/2
    p1 = np.array([2 * a * np.cos(-s / 2) + a * np.cos(-s), 2 * a * np.sin(-s / 2) - a * np.sin(-s)])
    p2 = np.array([2 * a * np.cos(np.pi - s / 2) + a * np.cos(2 * np.pi - s), 2 * a * np.sin(np.pi - s / 2) - a * np.sin(2 * np.pi - s)])
    p0 = np.array([2 * a * np.cos(s) + a * np.cos(2 * s), 2 * a * np.sin(s) - a * np.sin(2 * s)])
    v = np.array([-2 * a * np.sin(s) - 2 * a * np.sin(2 * s), 2 * a * np.cos(s) - 2 * a * np.cos(2 * s)])  # tangente
    croix = lambda u, w: u[0] * w[1] - u[1] * w[0]
    assert abs(croix(v, p1 - p0)) < 1e-12 and abs(croix(v, p2 - p0)) < 1e-12
    L.append(np.linalg.norm(p2 - p1))
ligne(f"\nDeltoïde : longueur des segments tangents (7 positions) = {min(L):.12f} … {max(L):.12f} (aiguille de longueur 1)")
ligne(f"Étoilés : aire ≥ π/108 = {fr(mp.pi / 108, 5)} (Cunningham 1971), amélioré en π/98 = {fr(mp.pi / 98, 5)} (2025)")

# ---------------------------------------------------------------------------
# 2. La chèvre et le triangle équilatéral
# ---------------------------------------------------------------------------
r_chevre = ch.corde_moitie_mp(2)
cote = 2 / mp.sqrt(3)
ligne("\n## 2. La chèvre et le triangle équilatéral de hauteur R\n")
ligne(f"- corde de la chèvre : {fr(r_chevre, 12)} R ; côté du triangle équilatéral de hauteur R : 2/√3 = {fr(cote, 12)} R")
ligne(f"- écart : {fr(r_chevre - cote, 4)} R ({fr(100 * (r_chevre - cote) / r_chevre, 3)} %)")
ligne(f"- herbe broutée avec la corde 2/√3 : {A.lentille(1, float(cote), 1) / np.pi * 100:.4f} % (au lieu de 50 %)".replace(".", ","))
ligne(f"- angle au centre : chèvre β = {fr(2 * mp.acos(r_chevre / 2), 10)} ; triangle 2·arccos(1/√3) = {fr(2 * mp.acos(1 / mp.sqrt(3)), 10)}")
ligne(f"- triangle de Reuleaux = trois chèvres de corde = côté : chaque paire de disques se recouvre de "
      f"{A.lentille(1, 1, 1) / np.pi * 100:.2f} % (vesica piscis, (2π/3 − √3/2)/π)".replace(".", ","))

# ---------------------------------------------------------------------------
# 3. L'arbre de Perron
# ---------------------------------------------------------------------------
BASE, AX = 2 / np.sqrt(3), 1 / np.sqrt(3)


def arbre(k, alphas, base=BASE, ax0=AX):
    """Arbre de Perron à 2^k branches : renvoie (l, r, ax), bases [l, r] et abscisse des sommets (hauteur 1).

    alphas[j] est le rapport de réduction à l'étage j (du plus fin au plus grossier)."""
    n = 2 ** k
    xs = [base * i / n for i in range(n + 1)]
    l, r, ax = list(xs[:-1]), list(xs[1:]), [ax0] * n
    blocs = [(i, i + 1, l[i], r[i]) for i in range(n)]
    for alpha in alphas:
        nouveaux = []
        for j in range(0, len(blocs), 2):
            (s1, _, u1, v1), (s2, e2, u2, v2) = blocs[j], blocs[j + 1]
            largeur = (v1 - u1) + (v2 - u2)
            dx = (v1 - u2) - (1 - alpha) * largeur  # recoller les deux blocs, puis les rapprocher
            for i in range(s2, e2):
                l[i] += dx
                r[i] += dx
                ax[i] += dx
            nouveaux.append((s1, e2, u1, u1 + alpha * largeur))
        blocs = nouveaux
    return l, r, ax


def longueur_union(l, r, ax, y):
    iv = sorted((l[i] + (ax[i] - l[i]) * y, r[i] + (ax[i] - r[i]) * y) for i in range(len(l)))
    tot, m = 0 * y, None
    for g, d in iv:
        debut = g if m is None else max(g, m)
        if d > debut:
            tot += d - debut
        m = d if m is None else max(m, d)
    return tot


def aire_exacte(k, alphas):
    """Aire exacte (mpmath) : la longueur de la coupe est affine entre deux croisements d'arêtes."""
    l, r, ax = arbre(k, [mp.mpf(v) for v in alphas], mp.mpf(2) / mp.sqrt(3), 1 / mp.sqrt(3))
    aretes = [(l[i], ax[i] - l[i]) for i in range(len(l))] + [(r[i], ax[i] - r[i]) for i in range(len(l))]
    ys = {mp.mpf(0), mp.mpf(1)}
    for i in range(len(aretes)):
        for j in range(i + 1, len(aretes)):
            (p, q), (s, u) = aretes[i], aretes[j]
            if q != u and 0 < (s - p) / (q - u) < 1:
                ys.add((s - p) / (q - u))
    ys = sorted(ys)
    aire = sum((y1 - y0) * longueur_union(l, r, ax, (y0 + y1) / 2) for y0, y1 in zip(ys[:-1], ys[1:]))
    return aire / (1 / mp.sqrt(3))  # part du triangle de départ


def aire_tranches(k, alphas, niveaux=3000):
    """Aire approchée (numpy) par tranches horizontales, pour les grands arbres."""
    l, r, ax = (np.array(v) for v in arbre(k, alphas))
    tot = 0.0
    for y in (np.arange(niveaux) + 0.5) / niveaux:
        g, d = l + (ax - l) * y, r + (ax - r) * y
        o = np.argsort(g)
        g, d = g[o], d[o]
        prec = np.concatenate(([-np.inf], np.maximum.accumulate(d)[:-1]))
        tot += np.sum(np.maximum(0.0, d - np.maximum(g, prec)))
    return tot / niveaux / (1 / np.sqrt(3))


def telescope(k):
    """Rapports (k+1)/(k+2), k/(k+1), …, 3/4, 2/3, du plus fin au plus grossier."""
    return [mp.mpf(k + 2 - j) / (k + 3 - j) for j in range(1, k + 1)]


ligne("\n## 3. L'arbre de Perron (triangle équilatéral de hauteur 1, 2^k branches)\n")
ligne(f"- 2 branches, α = 2/3 : aire = {fr(aire_exacte(1, [mp.mpf(2) / 3]), 20)} (minimum de α² + 2(1 − α)²)")
demi = aire_exacte(2, [1 / mp.sqrt(2)] * 2)
ligne(f"- 4 branches, α = 1/√2 aux deux étages : aire = {fr(demi, 25)} ; près de l'optimum, aire = 1 − 2α² + 2α⁴ = ½ + 2(α² − ½)²")
ligne(f"- 4 branches, α = 3/4 puis 2/3 : aire = {fr(aire_exacte(2, [mp.mpf(3) / 4, mp.mpf(2) / 3]), 25)}")
ligne("\n| branches N = 2^k | rapports α (du plus fin au plus grossier) | aire exacte | 2/(k+2) |")
ligne("|---:|---|---|---|")
t0 = time.time()
for k in range(1, 7):
    ligne(f"| {2 ** k} | {', '.join(f'{k + 2 - j}/{k + 3 - j}' for j in range(1, k + 1))} | {fr(aire_exacte(k, telescope(k)), 20)} |"
          f" {fr(mp.mpf(2) / (k + 2), 20)} |")
ligne(f"\n(calcul exact : {time.time() - t0:.0f} s)")
ligne("\nGrands arbres (tranches, 3000 niveaux) :")
grands = {}
for k in range(7, 15):
    grands[k] = aire_tranches(k, [float(v) for v in telescope(k)], 3000 if k < 13 else 1500)
    ligne(f"- k = {k} ({2 ** k} branches) : {grands[k]:.5f} ; 2/(k+2) = {2 / (k + 2):.5f}".replace(".", ","))
ligne("\nRapports irréguliers trouvés par optimisation (Nelder–Mead, départs aléatoires), aire exacte :")
for k, al in ((3, ("0.7778", "0.5953", "0.8602")), (5, ("0.8396", "0.7207", "0.9287", "0.598", "0.8449"))):
    v = aire_exacte(k, [mp.mpf(x) for x in al])
    ligne(f"- k = {k} : α = ({', '.join(al)}) → {fr(v, 8)} contre 2/(k+2) = {fr(mp.mpf(2) / (k + 2), 8)}"
          f" (gain {fr(100 * (1 - v / (mp.mpf(2) / (k + 2))), 2)} %)")

# ---------------------------------------------------------------------------
# 4. Deux façons de subdiviser vers l'infini
# ---------------------------------------------------------------------------
ligne("\n## 4. Ménisques d'Archimède contre arbre de Perron\n")
ligne("| N | ménisques : 1 − (N/2π)·sin(2π/N) | arbre de Perron : 2/(log₂N + 2) |")
ligne("|---:|---|---|")
for k in (2, 4, 6, 8, 10, 12, 14):
    N = 2 ** k
    ligne(f"| {N} | {1 - N / (2 * np.pi) * np.sin(2 * np.pi / N):.3e} | {2 / (k + 2):.4f} |".replace(".", ","))
ligne("\nPour que l'arbre de Perron descende à 1 % du triangle, il faudrait 2^198 ≈ 4·10⁵⁹ branches"
      " (2/(k+2) = 0,01 ⇒ k = 198) ; les ménisques d'Archimède passent sous 1 % dès N = 26.")

with open(os.path.join(ICI, "..", "resultats", "aiguille.md"), "w") as fh:
    fh.write("# Résultats de la partie V (générés par scripts/aiguille.py)\n\n" + "\n".join(md) + "\n")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig = plt.figure(figsize=(15.5, 9.6))
gs = fig.add_gridspec(2, 2, width_ratios=[1.35, 1], height_ratios=[1, 1.1], wspace=0.2, hspace=0.22)

# a) l'échelle des aires
ax = fig.add_subplot(gs[0, 0])
ax.set_aspect("equal")
ax.axis("off")
aiguille = dict(color=F.INK, lw=3.2, solid_capstyle="butt", zorder=5)
xc = [0.0, 1.55, 3.15, 4.75]
th = np.linspace(0, 2 * np.pi, 400)
ax.fill(xc[0] + 0.5 * np.cos(th), 0.5 * np.sin(th), color=F.BLEU, alpha=0.18, lw=0)
ax.plot(xc[0] + 0.5 * np.cos(th), 0.5 * np.sin(th), color=F.BLEU, lw=1.6)
ax.plot([xc[0], xc[0]], [-0.5, 0.5], **aiguille)
cy = 0.5 - 1 / np.sqrt(3)  # Reuleaux : sommet en haut à y = 0.5
ax.fill(xc[1] + rx, ry + cy, color=F.AQUA, alpha=0.18, lw=0)
ax.plot(np.append(xc[1] + rx, xc[1] + rx[0]), np.append(ry + cy, ry[0] + cy), color=F.AQUA, lw=1.6)
ax.plot([xc[1], xc[1]], [0.5, -0.5], **aiguille)
tri = np.array([[xc[2] - 1 / np.sqrt(3), -0.5], [xc[2] + 1 / np.sqrt(3), -0.5], [xc[2], 0.5]])
ax.add_patch(Polygon(tri, closed=True, fc=F.ORANGE, alpha=0.18, lw=0))
ax.add_patch(Polygon(tri, closed=True, fill=False, ec=F.ORANGE, lw=1.6))
ax.plot([xc[2], xc[2]], [-0.5, 0.5], **aiguille)
dx_, dy_ = deltoide[0][::100], deltoide[1][::100]
ax.fill(xc[3] + dx_ + 0.06, dy_, color=F.JAUNE, alpha=0.22, lw=0)
ax.plot(np.append(xc[3] + dx_ + 0.06, xc[3] + dx_[0] + 0.06), np.append(dy_, dy_[0]), color=F.JAUNE, lw=1.6)
ax.plot([xc[3] - a + 0.06] * 2, [-2 * a, 2 * a], **aiguille)
for s_ in (np.pi - 0.75, np.pi + 0.75):  # deux autres positions de l'aiguille qui tourne dans le deltoïde
    q1 = (2 * a * np.cos(-s_ / 2) + a * np.cos(-s_), 2 * a * np.sin(-s_ / 2) - a * np.sin(-s_))
    q2 = (2 * a * np.cos(np.pi - s_ / 2) + a * np.cos(2 * np.pi - s_), 2 * a * np.sin(np.pi - s_ / 2) - a * np.sin(2 * np.pi - s_))
    ax.plot([xc[3] + 0.06 + q1[0], xc[3] + 0.06 + q2[0]], [q1[1], q2[1]], color=F.INK2, lw=1.6, alpha=0.55, zorder=4)
legendes = [("disque\nπ/4 = 0,785", "100 %"), ("Reuleaux (3 chèvres)\n(π − √3)/2 = 0,705", "89,7 %"),
            ("triangle de Pál\n1/√3 = 0,577", "73,5 % : le plus\npetit convexe"), ("deltoïde de Kakeya\nπ/8 = 0,393", "50 % : la moitié\nexactement")]
for x, (nom, part) in zip(xc, legendes):
    ax.text(x, -0.76, f"{nom}\n{part}", ha="center", va="top", fontsize=9.5, color=F.INK, linespacing=1.25)
ax.annotate("", xy=(5.92, -0.1), xytext=(5.92, 0.42), arrowprops=dict(arrowstyle="-|>", color=F.MUTED, lw=1.2))
ax.text(6.0, 0.16, "Besicovitch\n(1928) :\naussi petit\nqu'on veut", fontsize=9, color=F.INK2, va="center")
ax.set_xlim(-0.7, 6.95)
ax.set_ylim(-1.55, 0.72)
ax.set_title("a)  Où retourner une aiguille de longueur 1 (en noir)")

# b) la chèvre et le triangle équilatéral
ax = fig.add_subplot(gs[0, 1])
ax.set_aspect("equal")
F.remplir_intersection(ax, float(r_chevre), (F.BLEU, F.SURF), 0.2)
F.cercle(ax, (0, 0), 1, color=F.INK, lw=1.6)
F.cercle(ax, (1, 0), float(r_chevre), color=F.BLEU, lw=1.6)
F.cercle(ax, (1, 0), float(cote), color=F.ORANGE, lw=1.3, ls=(0, (4, 3)))
tri = np.array([[1, 0], [0, 1 / np.sqrt(3)], [0, -1 / np.sqrt(3)]])
ax.add_patch(Polygon(tri, closed=True, fill=False, ec=F.ORANGE, lw=1.8))
ax.plot([0, 1], [0, 0], color=F.ORANGE, lw=1, ls=":")
F.point(ax, 1, 0, F.INK, 8)
F.point(ax, 0, 0, F.INK, 6)
for s in (1, -1):
    F.point(ax, 0, s / np.sqrt(3), F.ORANGE, 7)
ax.text(1.06, 0.07, "P", fontsize=11, color=F.INK)
ax.text(-0.13, 0.05, "O", fontsize=11, color=F.INK)
ax.text(0.5, -0.1, "hauteur R", fontsize=9, color=F.ORANGE, ha="center", va="top")
ax.text(-1.15, 1.45, "corde de la chèvre : 1,1587 R → 50 %", fontsize=9.5, color=F.BLEU)
ax.text(-1.15, 1.29, "côté du triangle : 2/√3 = 1,1547 R → 49,72 %", fontsize=9.5, color=F.ORANGE)
ax.text(-1.15, -1.45, "écart 0,35 % : une quasi-coïncidence, pas une égalité", fontsize=9, color=F.INK2)
ax.set_xlim(-1.2, 3.3)
ax.set_ylim(-1.55, 1.58)
ax.set_xticks([])
ax.set_yticks([])
for sp in ax.spines.values():
    sp.set_visible(False)
ax.grid(False)
ax.set_title("b)  La chèvre et le triangle équilatéral de hauteur R")
zoom = ax.inset_axes([0.75, 0.34, 0.24, 0.32])
zoom.set_aspect("equal")
for rr, coul, st in ((float(r_chevre), F.BLEU, "-"), (float(cote), F.ORANGE, (0, (4, 3)))):
    tt = np.linspace(2.5, 2.75, 300)
    zoom.plot(1 + rr * np.cos(tt), rr * np.sin(tt), color=coul, lw=1.4, ls=st)
F.point(zoom, 0, 1 / np.sqrt(3), F.ORANGE, 5)
zoom.set_xlim(-0.03, 0.03)
zoom.set_ylim(0.55, 0.61)
zoom.set_xticks([])
zoom.set_yticks([])
zoom.set_title("zoom sur le coin", fontsize=8.5, color=F.INK2, fontweight="normal")
for sp in zoom.spines.values():
    sp.set_visible(True)
    sp.set_color(F.MUTED)
ax.add_patch(plt.Rectangle((-0.06, 0.52), 0.12, 0.12, fill=False, ec=F.MUTED, lw=1))
ax.annotate("", xy=(2.2, 0.75), xytext=(0.07, 0.6), arrowprops=dict(arrowstyle="-|>", color=F.MUTED, lw=0.9))

# c) deux arbres de Perron
ax = fig.add_subplot(gs[1, 0])
ax.set_aspect("equal")
ax.axis("off")
for decal, k, alphas, coul, texte in ((0.0, 2, [1 / np.sqrt(2)] * 2, F.AQUA, "4 branches, α = 1/√2\naire = ½ du triangle, exactement"),
                                      (1.75, 6, [float(v) for v in telescope(6)], F.BLEU,
                                       "64 branches, α = 7/8, 6/7, …, 3/4, 2/3\naire = ¼ du triangle, exactement")):
    l, r, axx = arbre(k, alphas)
    ax.add_patch(Polygon([[decal, 0], [decal + BASE, 0], [decal + AX, 1]], closed=True, fill=False, ec=F.BASE, lw=1.2,
                         ls=(0, (4, 3))))
    for i in range(len(l)):
        ax.add_patch(Polygon([[decal + l[i], 0], [decal + r[i], 0], [decal + axx[i], 1]], closed=True, fc=coul,
                             alpha=0.28, ec=coul, lw=0.5))
    ax.text(decal + AX, -0.07, texte, ha="center", va="top", fontsize=9.5, color=F.INK)
ax.text(3.05, 0.55, "même triangle de départ\n(pointillés), hauteur 1 :\nune aiguille dans\nchaque direction\nsur 60°", fontsize=9,
        color=F.INK2, va="center")
ax.set_xlim(-0.08, 4.0)
ax.set_ylim(-0.32, 1.05)
ax.set_title("c)  L'arbre de Perron : glisser les branches pour gagner de l'aire")

# d) deux façons de subdiviser vers l'infini
ax = fig.add_subplot(gs[1, 1])
ks = np.arange(1, 41)
Ns = 2.0 ** ks
xm = 2 * np.pi / Ns  # 1 − sin(x)/x, en série quand x est petit (sinon la soustraction perd tous ses chiffres)
men = np.where(xm > 0.05, 1 - np.sin(xm) / xm, xm ** 2 / 6 - xm ** 4 / 120 + xm ** 6 / 5040)
ax.loglog(Ns[1:], men[1:], color=F.AQUA, lw=2.2, label="ménisques d'Archimède (N segments) : en 1/N²")
ax.loglog(Ns, 2 / (ks + 2), color=F.BLEU, lw=2.2, label="arbre de Perron : 2/(log₂N + 2)")
kk = np.array(sorted(grands))
ax.loglog(2.0 ** kk, [grands[k] for k in kk], "o", color=F.BLEU, ms=5, mec=F.SURF, label="arbres calculés (k = 7 à 14)")
ax.axhline(0.01, color=F.MUTED, lw=1, ls=(0, (4, 3)))
ax.text(1.25, 0.0075, "1 %", fontsize=9, color=F.INK2, va="top")
ax.annotate("1 % dès N = 26", xy=(26, 0.01), xytext=(80, 1e-4), fontsize=9, color=F.INK2,
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.text(3e4, 30, "avec cette construction, il faudrait\n2¹⁹⁸ branches pour descendre à 1 %", fontsize=9, color=F.INK2,
        va="top")
ax.set_xlabel("nombre de morceaux N")
ax.set_ylabel("aire restante (part du disque / du triangle)")
ax.set_ylim(1e-22, 300)
ax.set_title("d)  Deux façons de subdiviser vers l'infini")
ax.legend(fontsize=9, loc="lower left")
F.sauver(fig, "e1_aiguille_kakeya.png")
