"""
Partie X : le trou du rayon droit, le point et le carré, Ptolémée et le plan hyperbolique.

    python3 scripts/carre_ptolemee.py        # ≈ 30 s

Écrit resultats/carre_ptolemee.md et figures/j1_carre_ptolemee.png.

1. Le « trou » des rayons de l'œil de poisson (partie VIII) : les rayons presque droits, autour du diamètre O–P–P'.
2. Un point, un disque et un carré rapetissés sous le flou : à quelle vitesse ils se confondent.
3. Le carré des centres fantômes (partie IX) est le réseau réciproque de la grille des pixels : hexagone sur une grille
   hexagonale.
4. Le repliement et l'arbre de Perron : couper, translater.
5. Ptolémée : le carré donne √2, le pentagone donne φ ; la corde de la chèvre dans sa table.
6. Le plan hyperbolique : l'indice 2/(1 − r²), jumeau de l'œil de poisson ; la récurrence du pentagone.
"""

import logging
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle, Polygon
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.spatial import cKDTree
from scipy.special import j1

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
# 1. Le trou des rayons
# ---------------------------------------------------------------------------
P = np.array([0.45, 0.25])  # le point source de la partie VIII
Pp = -P / (P @ P)
dPP = np.linalg.norm(P - Pp)
dirP = np.degrees(np.arctan2(P[1], P[0]))


def rayon_cercle(psi):
    """Rayon du cercle-rayon de l'œil de poisson lancé de P dans la direction psi (degrés) : |PP'|/(2|sin θ|)."""
    d = np.array([np.cos(np.radians(psi)), np.sin(np.radians(psi))])
    n = np.array([-d[1], d[0]])
    return abs((P - Pp) @ (P - Pp) / (2 * n @ (P - Pp)))


ligne("## 1. Le trou des rayons de l'œil de poisson\n")
demi = np.degrees(np.arcsin(dPP / (2 * 3)))
ligne(f"P = (0,45 ; 0,25), direction {fr(dirP, '{:.2f}')}° ; P' = −P/|P|² ; |PP'| = {fr(dPP)}.")
ligne("Le rayon lancé à l'angle θ de la droite PP' est un cercle de rayon |PP'|/(2|sin θ|). Pour θ = 0, c'est la droite"
      " P–O–P', le seul rayon droit.")
ligne(f"Avec mon seuil « cercle de rayon > 3 », les rayons sautés forment deux secteurs de ±{fr(demi, '{:.2f}')}° autour de"
      f" {fr(dirP, '{:.2f}')}° et {fr(dirP + 180, '{:.2f}')}° : de {fr(dirP - demi, '{:.2f}')}° à {fr(dirP + demi, '{:.2f}')}°,"
      f" et de {fr(dirP + 180 - demi, '{:.2f}')}° à {fr(dirP + 180 + demi, '{:.2f}')}°.")
ligne(f"Rayon du cercle à 137,5° : {fr(rayon_cercle(137.5), '{:.3f}')} (tracé) ; à 222,5° : {fr(rayon_cercle(222.5), '{:.3f}')}"
      " (sauté, car il est dans le second secteur).")
Q = np.array([-0.3, 0.4])
ligne(f"Pour un autre point, Q = (−0,3 ; 0,4), le trou serait centré sur {fr(np.degrees(np.arctan2(Q[1], Q[0])), '{:.2f}')}° et"
      f" {fr(np.degrees(np.arctan2(Q[1], Q[0])) + 180, '{:.2f}')}° : il suit le point, pas un angle fixe.")

# ---------------------------------------------------------------------------
# 2. Un point, un disque et un carré rapetissés sous le flou
# ---------------------------------------------------------------------------
N_, L_ = 256, 16.0  # grille de Fourier, en unités du flou σ
k = np.fft.fftfreq(N_, d=L_ / N_)
KX, KY = np.meshgrid(k, k)
K = np.hypot(KX, KY)
TACHE = np.exp(-2 * np.pi ** 2 * K ** 2)  # flou gaussien de largeur σ = 1


def tf_disque(rho):
    x = 2 * np.pi * rho * K
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(x > 1e-12, 2 * j1(x) / x, 1.0)


def tf_carre(s):
    return np.sinc(s * KX) * np.sinc(s * KY)


def image(tf):
    return np.real(np.fft.ifft2(tf * TACHE))


ligne("\n## 2. Un point, un disque et un carré rapetissés sous le flou\n")
ligne("Images floues (tache gaussienne de largeur σ), à lumière totale égale ; écart maximal rapporté au maximum de l'image du disque.\n")
ligne("| rayon du disque ρ/σ | point contre disque | carré de même aire (côté √π·ρ) | carré de côté √3·ρ |")
ligne("|---:|---|---|---|")
RHO = np.geomspace(0.04, 2.0, 28)
ECARTS = {"point": [], "aire": [], "moment": []}
for rho in RHO:
    Id = image(tf_disque(rho))
    m = Id.max()
    ECARTS["point"].append(np.abs(image(np.ones_like(K)) - Id).max() / m)
    ECARTS["aire"].append(np.abs(image(tf_carre(np.sqrt(np.pi) * rho)) - Id).max() / m)
    ECARTS["moment"].append(np.abs(image(tf_carre(np.sqrt(3) * rho)) - Id).max() / m)
for rho in (0.05, 0.1, 0.2, 0.4, 0.8, 1.6):
    Id = image(tf_disque(rho))
    m = Id.max()
    e = [np.abs(image(t) - Id).max() / m for t in (np.ones_like(K), tf_carre(np.sqrt(np.pi) * rho), tf_carre(np.sqrt(3) * rho))]
    ligne(f"| {fr(rho, '{:.2f}')} | {fr(e[0], '{:.2e}')} | {fr(e[1], '{:.2e}')} | {fr(e[2], '{:.2e}')} |")
pentes = {c: np.polyfit(np.log(RHO[:10]), np.log(np.array(v[:10])), 1)[0] for c, v in ECARTS.items()}
ligne(f"\nPentes aux petites tailles (log-log) : point/disque {fr(pentes['point'], '{:.2f}')}, carré de même aire"
      f" {fr(pentes['aire'], '{:.2f}')}, carré de côté √3·ρ {fr(pentes['moment'], '{:.2f}')}.")
ligne("Moments d'ordre 2 par axe : disque ρ²/4, carré s²/12. À aire égale (s² = πρ²), le carré est π/3 = 1,0472 fois plus"
      " étalé ; à étalement égal (s = √3·ρ), son aire vaut 3/π = 0,9549 fois celle du disque.")
ligne("La première différence de forme est d'ordre 4 : pour le carré, ⟨x⁴⟩ − 3⟨x²y²⟩ = s⁴(1/80 − 1/48) = −s⁴/120 (le disque"
      " donne 0).")


# ---------------------------------------------------------------------------
# 3. Le réseau réciproque : carré ou hexagone
# ---------------------------------------------------------------------------
def zones(x, y, R, N=55):
    k_ = np.floor(N * (x * x + y * y) / R ** 2).astype(int)
    return np.where(k_ < N, (k_ % 2 == 0).astype(float), 0.0)  # lame de Fresnel ordinaire


ligne("\n## 3. Le carré des centres fantômes est le réseau réciproque de la grille\n")
R3, u3 = 36, 27.5
x0 = R3 * R3 / (2 * u3)
B1, B2 = np.array([1, -1 / np.sqrt(3)]), np.array([0, 2 / np.sqrt(3)])  # réseau réciproque de la grille hexagonale
A1, A2 = np.array([1.0, 0.0]), np.array([0.5, np.sqrt(3) / 2])
I_, J_ = np.meshgrid(np.arange(-80, 81), np.arange(-80, 81))
HEX = (I_[..., None] * A1 + J_[..., None] * A2).reshape(-1, 2)
HEX = HEX[np.hypot(*HEX.T) < 1.3 * R3]
pire = 0
for g in (B1, B2, B1 + B2):
    xg = g * R3 * R3 / (2 * u3)
    ph0 = u3 * (HEX ** 2).sum(1) / R3 ** 2
    ph1 = u3 * ((HEX - xg) ** 2).sum(1) / R3 ** 2 - u3 * (xg @ xg) / R3 ** 2
    dd = ph0 - ph1
    pire = max(pire, np.max(np.abs(dd - np.round(dd))))
ligne(f"Grille hexagonale (pas 1 pixel) : u·|x|²/R² et u·|x − x_g|²/R² − u·|x_g|²/R² diffèrent d'un entier en chaque point du réseau"
      f" quand g est un vecteur du réseau réciproque ; écart maximal à un entier : {pire:.1e}.")
ligne(f"Lame de Fresnel à 55 zones, R = 36 px : grille carrée → 8 centres sur le carré de demi-côté {fr(x0 / R3, '{:.3f}')} a"
      f" (4 aux milieux des côtés, 4 aux coins, à √2 près) ; grille hexagonale → 6 centres sur l'hexagone de rayon"
      f" {fr(2 / np.sqrt(3) * x0 / R3, '{:.3f}')} a, soit 2/√3 = {fr(2 / np.sqrt(3), '{:.4f}')} fois plus loin.")

# ---------------------------------------------------------------------------
# 4. Ptolémée
# ---------------------------------------------------------------------------
ligne("\n## 4. Ptolémée : les polygones dans le cercle\n")
ligne("Théorème de Ptolémée (quadrilatère inscrit) : AC·BD = AB·CD + AD·BC.")
ligne(f"- carré de côté 1 : d² = 1 + 1, d = √2 = {fr(2 ** 0.5, '{:.6f}')}, la diagonale du carré, limite de la chèvre en"
      " dimension infinie ;")
ligne(f"- pentagone régulier de côté 1 (quatre sommets consécutifs) : d² = 1 + d, d = φ = {fr(PHI, '{:.6f}')}.")
rng = np.random.default_rng(1)
pire = 0
for _ in range(1000):
    t = np.sort(rng.uniform(0, 2 * np.pi, 4))
    pts = np.c_[np.cos(t), np.sin(t)]
    dist = lambda i, j: np.linalg.norm(pts[i] - pts[j])
    pire = max(pire, abs(dist(0, 2) * dist(1, 3) - dist(0, 1) * dist(2, 3) - dist(0, 3) * dist(1, 2)))
ligne(f"Contrôle sur 1000 quadrilatères inscrits tirés au hasard : écart maximal {pire:.1e}.")


def lentille(r):
    return r * r * np.arccos(r / 2) + np.arccos(1 - r * r / 2) - (r / 2) * np.sqrt(4 - r * r)


r_ch = brentq(lambda r: lentille(r) - np.pi / 2, 1, 1.4, xtol=1e-15)
theta = np.degrees(2 * np.arcsin(r_ch / 2))
crd = 60 * r_ch  # corde de Ptolémée, cercle de rayon 60
sexa = (int(crd), int((crd % 1) * 60), (crd * 3600) % 60)
ligne(f"\nLa corde de la chèvre est la corde de l'arc {fr(theta, '{:.4f}')}° = 180° − β (β = {fr(180 - theta, '{:.4f}')}°)."
      f" Dans la table de Ptolémée (rayon 60), elle vaut {sexa[0]};{sexa[1]:02d},{sexa[2]:02.0f}, entre les cordes de 70°30′"
      f" ({fr(120 * np.sin(np.radians(35.25)), '{:.4f}')}) et de 71° ({fr(120 * np.sin(np.radians(35.5)), '{:.4f}')}),"
      " calculées ici avec les valeurs modernes.")


# ---------------------------------------------------------------------------
# 5. Le plan hyperbolique
# ---------------------------------------------------------------------------
def rayon_milieu(P0, ang, signe, smax=12):
    """Rayon dans l'indice n = 2/(1 + signe·r²) : signe = +1 œil de poisson (sphère), −1 disque de Poincaré (plan hyperbolique)."""
    def g(s, y):
        x, d = y[:2], y[2:]
        gr = -2 * signe * x / (1 + signe * (x @ x))  # gradient de ln n
        return np.r_[d, gr - (gr @ d) * d]

    bord = lambda s, y: 0.997 - np.hypot(y[0], y[1])
    bord.terminal = True
    ev = [bord] if signe < 0 else None
    return solve_ivp(g, (0, smax), np.r_[P0, np.cos(ang), np.sin(ang)], rtol=1e-10, atol=1e-12, max_step=0.01, events=ev)


ligne("\n## 5. Le plan hyperbolique, jumeau de l'œil de poisson\n")
P5 = np.array([0.3, 0.2])
HYP = []
for a_ in np.radians(np.arange(0, 360, 15)):
    s = rayon_milieu(P5, a_, -1)
    HYP.append(s.y[:2])
fins = np.array([h[:, -1] for h in HYP])
angles_bord = []
for h in HYP:
    d = h[:, -1] - h[:, -2]
    d /= np.linalg.norm(d)
    angles_bord.append(np.degrees(np.arccos(abs(d @ (h[:, -1] / np.linalg.norm(h[:, -1]))))))
min_sep = np.inf
for i in range(len(HYP)):
    for j in range(i + 1, len(HYP)):
        a, b = HYP[i][:, 20:], HYP[j][:, 20:]
        dmin = np.min(np.hypot(a[0][:, None] - b[0][None, :], a[1][:, None] - b[1][None, :]))
        min_sep = min(min_sep, dmin)
ligne("Indice n = 2/(1 − r²) dans le disque unité : c'est le disque de Poincaré, le plan hyperbolique.")
ligne(f"{len(HYP)} rayons partis de P = (0,3 ; 0,2) : tous atteignent le bord (|x| > 0,997) ; angle avec le rayon du disque à"
      f" l'arrivée ≤ {fr(max(angles_bord), '{:.1f}')}° (perpendiculaires au bord, à la discrétisation près) ; deux rayons ne se"
      f" recroisent jamais (distance minimale hors du départ : {fr(min_sep, '{:.3f}')}).")
ligne("Avec l'indice 2/(1 + r²) (partie VIII), tous se recroisent en −P/|P|². Sphère : les rayons se refocalisent ;"
      " plan : droites ; plan hyperbolique : ils s'écartent sans retour.")
x = [1.0, 2.0]
for _ in range(12):
    x.append((1 + x[-1]) / x[-2])
ligne(f"\nRécurrence du pentagone x_(n+1) = (1 + x_n)/x_(n−1), départ (1 ; 2) : {', '.join(fr(v, '{:.4f}') for v in x[:11])} …"
      " période 5.")
pire = 0
for _ in range(200):
    a, b = rng.uniform(0.1, 10, 2)
    y = [a, b]
    for _ in range(5):
        y.append((1 + y[-1]) / y[-2])
    pire = max(pire, abs(y[5] - a) / a, abs(y[6] - b) / b)
ligne(f"Contrôle sur 200 départs au hasard : retour au départ après 5 pas, écart relatif maximal {pire:.1e}. Point fixe :"
      f" x² = 1 + x, soit φ = {fr(PHI, '{:.6f}')} (la relation de Ptolémée du pentagone).")

with open(os.path.join(ICI, "..", "resultats", "carre_ptolemee.md"), "w") as fh:
    fh.write("# Résultats de la partie X (générés par scripts/carre_ptolemee.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure j1
# ===========================================================================
fig = plt.figure(figsize=(20, 13.2))
gs = fig.add_gridspec(2, 3, wspace=0.15, hspace=0.24)
FOND = dict(fc=F.SURF, ec="none", alpha=0.88, pad=2)


def schema(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")


# a) le trou
ax = fig.add_subplot(gs[0, 0])
F.cercle(ax, (0, 0), 1, color=F.INK2, lw=1, ls=(0, (5, 3)))
for psi in np.arange(0, 360, 5):
    rc = rayon_cercle(psi)
    saute = rc > 3
    d = np.array([np.cos(np.radians(psi)), np.sin(np.radians(psi))])
    n = np.array([-d[1], d[0]])
    if rc > 400:
        continue
    cote = np.sign(n @ (Pp - P))
    C = P + cote * rc * n
    t = np.linspace(0, 2 * np.pi, 1500)
    ax.plot(C[0] + rc * np.cos(t), C[1] + rc * np.sin(t), color=F.ORANGE if saute else F.BLEU, lw=0.8 if saute else 0.9,
            alpha=0.75)
u = (P - Pp) / dPP
ax.plot([Pp[0] - 3 * u[0], P[0] + 6 * u[0]], [Pp[1] - 3 * u[1], P[1] + 6 * u[1]], color=F.INK, lw=2)
for c_, d_ in ((dirP, 1), (dirP + 180, 1)):
    w = np.radians(np.linspace(c_ - demi, c_ + demi, 50))
    ax.add_patch(Polygon(np.r_[[P], np.c_[P[0] + 0.55 * np.cos(w), P[1] + 0.55 * np.sin(w)]], closed=True, fc=F.ORANGE, alpha=0.25,
                         ec="none", zorder=4))
F.point(ax, *P, F.INK, 7, 6)
F.point(ax, *Pp, F.ORANGE, 8, 6)
F.point(ax, 0, 0, F.INK2, 5, 6)
ax.text(P[0] + 0.06, P[1] + 0.08, "P", fontsize=10.5, fontweight="bold", bbox=FOND, zorder=7)
ax.text(Pp[0] - 0.1, Pp[1] + 0.1, "P'", fontsize=10.5, fontweight="bold", ha="right", bbox=FOND, zorder=7)
ax.text(-2.75, 2.42, "Bleu : rayons tracés. Orange : ceux que j'avais sautés\n(cercles de rayon > 3), autour du seul rayon droit,\n"
        f"le diamètre P–O–P' (noir). Le trou fait ±{fr(demi, '{:.1f}')}° autour de\n"
        f"{fr(dirP, '{:.1f}')}° et {fr(dirP + 180, '{:.1f}')}° : il suit P, pas un angle fixe.",
        fontsize=9, color=F.INK2, va="top", bbox=FOND, zorder=7)
schema(ax, (-2.8, 2.5), (-2.6, 2.5))
ax.set_title("a)  Le « trou » : les rayons presque droits")

# b) point, disque, carré
ax = fig.add_subplot(gs[0, 1])
for cle, coul, lab in (("point", F.INK, "point contre disque"), ("aire", F.ORANGE, "carré de même aire contre disque"),
                       ("moment", F.BLEU, "carré de côté √3·ρ contre disque")):
    ax.loglog(RHO, ECARTS[cle], "-", color=coul, lw=1.8, label=lab + f" (pente {pentes[cle]:.2f})".replace(".", ","))
ax.set_xlabel("taille de l'objet (rayon du disque ρ, en largeurs de flou σ)")
ax.set_ylabel("écart maximal entre les deux images floues")
ax.set_xlim(0.04, 2)
ax.set_ylim(1e-10, 1e3)
ax.legend(fontsize=9, loc="lower right")
ins = ax.inset_axes([0.02, 0.76, 0.2, 0.23])
ins.set_aspect("equal")
ins.axis("off")
ins.add_patch(Circle((0, 0), 1, fc=F.INK, alpha=0.18, ec=F.INK, lw=1))
ins.add_patch(plt.Rectangle((-np.sqrt(3) / 2, -np.sqrt(3) / 2), np.sqrt(3), np.sqrt(3), fill=False, ec=F.BLEU, lw=1.6))
ins.add_patch(plt.Rectangle((-np.sqrt(np.pi) / 2, -np.sqrt(np.pi) / 2), np.sqrt(np.pi), np.sqrt(np.pi), fill=False, ec=F.ORANGE,
                            lw=1.2, ls=(0, (3, 2))))
F.point(ins, 0, 0, F.INK, 4)
ins.set_xlim(-1.1, 1.1)
ins.set_ylim(-1.1, 1.1)
ax.text(0.25, 0.98, "Sous le flou, les trois se confondent.\nLe disque et le carré de côté √3·ρ\n(même étalement, aire 3/π de celle\n"
        "du disque) se confondent deux fois\nplus vite : seuls leurs coins diffèrent.", transform=ax.transAxes, fontsize=9,
        color=F.INK2, va="top")
ax.set_yticks([1e-10, 1e-8, 1e-6, 1e-4, 1e-2, 1])
ax.set_title("b)  Sous le flou, point, disque et carré se confondent")

# c) réseau réciproque
sub = gs[0, 2].subgridspec(1, 2, wspace=0.04)
cm = LinearSegmentedColormap.from_list("nb", [F.SURF, F.INK])
n3 = int(2 * R3 + 41) | 1
c3 = (n3 - 1) / 2
yy, xx = np.mgrid[0:n3, 0:n3] - c3
axc = fig.add_subplot(sub[0, 0])
ext = (-(c3 + 0.5) / R3, (c3 + 0.5) / R3, -(c3 + 0.5) / R3, (c3 + 0.5) / R3)
axc.imshow(zones(xx, yy, R3), cmap=cm, vmin=0, vmax=1, interpolation="nearest", extent=ext, origin="lower")
v = x0 / R3
car = [(v, 0), (v, v), (0, v), (-v, v), (-v, 0), (-v, -v), (0, -v), (v, -v)]
for p in car:
    axc.add_patch(Circle(p, 0.07, fill=False, ec=F.AQUA, lw=1.5, zorder=5))
axc.add_patch(Polygon([(v, v), (-v, v), (-v, -v), (v, -v)], closed=True, fill=False, ec="#7d3c98", lw=1.6, zorder=4))
axc.set_xlim(-1.08, 1.08)
axc.set_ylim(-1.08, 1.08)
axc.set_aspect("equal")
axc.axis("off")
axc.text(0, -1.14, "grille carrée : un carré", ha="center", va="top", fontsize=10)
axh = fig.add_subplot(sub[0, 1])
fx = np.linspace(-1.08 * R3, 1.08 * R3, 520)
FXX, FYY = np.meshgrid(fx, fx)
arbre_kd = cKDTree(HEX)
_, idx = arbre_kd.query(np.c_[FXX.ravel(), FYY.ravel()])
vals = zones(HEX[idx, 0], HEX[idx, 1], R3).reshape(FXX.shape)
axh.imshow(vals, cmap=cm, vmin=0, vmax=1, interpolation="nearest", extent=(-1.08, 1.08, -1.08, 1.08), origin="lower")
rh = 2 / np.sqrt(3) * v
hexa = [(rh * np.cos(np.radians(a)), rh * np.sin(np.radians(a))) for a in range(30, 390, 60)]
for p in hexa:
    axh.add_patch(Circle(p, 0.07, fill=False, ec=F.AQUA, lw=1.5, zorder=5))
axh.add_patch(Polygon(hexa, closed=True, fill=False, ec="#7d3c98", lw=1.6, zorder=4))
axh.set_xlim(-1.08, 1.08)
axh.set_ylim(-1.08, 1.08)
axh.set_aspect("equal")
axh.axis("off")
axh.text(0, -1.14, "grille hexagonale : un hexagone", ha="center", va="top", fontsize=10)
cel = gs[0, 2].get_position(fig)
fig.text(cel.x0, cel.y1 + 0.006, "c)  Ton carré vient de la grille des pixels", fontsize=11.5, fontweight="bold", color=F.INK,
         va="bottom")
axc.text(-1.08, -1.38, "Lame de Fresnel, 36 px. Les centres fantômes dessinent le réseau réciproque de la grille :\n"
         "un carré (ton tracé violet) sur des pixels carrés, un hexagone sur des pixels hexagonaux.", fontsize=9,
         color=F.INK2, va="top")

# d) repliement et Perron
sub = gs[1, 0].subgridspec(1, 2, wspace=0.12, width_ratios=[1.1, 1])
axd = fig.add_subplot(sub[0, 0])
xs = np.linspace(0, 1, 600)
f_ = 2.6 * xs
axd.plot(xs, f_, color=F.BASE, lw=1.4, label="fréquence vraie (une « aiguille »)")
axd.plot(xs, f_ - np.floor(f_), color=F.BLEU, lw=1.2, alpha=0.7, label="coupée et descendue d'un entier")
axd.plot(xs, np.abs(f_ - np.round(f_)), color=F.INK, lw=1.8, label="repliée : ce que voit l'écran")
for kk in (1, 2):
    axd.axhline(kk, color=F.GRID, lw=0.8)
axd.set_xlim(0, 1)
axd.set_ylim(0, 2.75)
axd.set_xlabel("position (x/a)")
axd.set_ylabel("fréquence (cycles par pixel)")
axd.legend(fontsize=8.5, loc="upper left")
axp = fig.add_subplot(sub[0, 1])
BASE_, AX_ = 2 / np.sqrt(3), 1 / np.sqrt(3)


def arbre(k_, alphas, base=BASE_, ax0=AX_):
    """Arbre de Perron à 2^k branches (même construction que la partie V)."""
    n_ = 2 ** k_
    xs_ = [base * i / n_ for i in range(n_ + 1)]
    l, r, axs_ = list(xs_[:-1]), list(xs_[1:]), [ax0] * n_
    blocs = [(i, i + 1, l[i], r[i]) for i in range(n_)]
    for alpha in alphas:
        nouveaux = []
        for j in range(0, len(blocs), 2):
            (s1, _, u1_, v1_), (s2, e2, u2_, v2_) = blocs[j], blocs[j + 1]
            largeur = (v1_ - u1_) + (v2_ - u2_)
            dx = (v1_ - u2_) - (1 - alpha) * largeur
            for i in range(s2, e2):
                l[i] += dx
                r[i] += dx
                axs_[i] += dx
            nouveaux.append((s1, e2, u1_, u1_ + alpha * largeur))
        blocs = nouveaux
    return l, r, axs_


l, r, axx = arbre(3, [4 / 5, 3 / 4, 2 / 3])
axp.add_patch(Polygon([[0, 0], [BASE_, 0], [AX_, 1]], closed=True, fill=False, ec=F.BASE, lw=1.1, ls=(0, (4, 3))))
for i in range(len(l)):
    axp.add_patch(Polygon([[l[i], 0], [r[i], 0], [axx[i], 1]], closed=True, fc=F.AQUA, alpha=0.3, ec=F.AQUA, lw=0.6))
schema(axp, (-0.3, 1.2), (-0.35, 1.2))
axp.text(0.45, 1.1, "arbre de Perron (8 branches)", ha="center", fontsize=10)
axd.text(0, 3.05, "d)  Repliement et arbre de Perron : couper, translater", fontsize=11.5, fontweight="bold", color=F.INK)
axp.text(-0.05, -0.12, "Même geste : on coupe, on translate,\non fait se recouvrir. Mais les « V » du\n"
         "spectre sont des droites repliées,\npas des triangles de Perron.", fontsize=9, color=F.INK2, va="top")

# e) Ptolémée
ax = fig.add_subplot(gs[1, 1])
for cx, nside, coul, titre in ((-1.25, 4, "#7d3c98", "carré : d² = 1 + 1, d = √2"), (1.25, 5, F.AQUA, "pentagone : d² = 1 + d, d = φ")):
    F.cercle(ax, (cx, 0), 1, color=F.MUTED, lw=1)
    angs = np.radians(90 + 360 * np.arange(nside) / nside)
    pts = np.c_[cx + np.cos(angs), np.sin(angs)]
    ax.add_patch(Polygon(pts, closed=True, fill=False, ec=F.BASE, lw=1.2))
    quad = pts[:4]
    ax.add_patch(Polygon(quad, closed=True, fc=coul, alpha=0.15, ec=coul, lw=1.6))
    ax.plot([quad[0, 0], quad[2, 0]], [quad[0, 1], quad[2, 1]], color=coul, lw=1.4, ls=(0, (4, 2)))
    ax.plot([quad[1, 0], quad[3, 0]], [quad[1, 1], quad[3, 1]], color=coul, lw=1.4, ls=(0, (4, 2)))
    ax.text(cx, -1.25, titre, ha="center", va="top", fontsize=9.5)
ax.text(-2.3, 1.55, "Ptolémée : dans un quadrilatère inscrit, produit des diagonales\n= somme des produits des côtés opposés.",
        fontsize=9.5, color=F.INK, va="top")
ax.text(-2.3, -1.68, f"La corde de la chèvre est la corde de l'arc {theta:.2f}° : dans la table\n".replace(".", ",")
        + f"de Ptolémée (rayon 60), {sexa[0]};{sexa[1]:02d},{sexa[2]:02.0f}, entre 70°30′ et 71°.", fontsize=9, color=F.INK2,
        va="top")
schema(ax, (-2.35, 2.35), (-2.25, 1.7))
ax.set_title("e)  Ptolémée : le carré donne √2, le pentagone donne φ")

# f) le plan hyperbolique
ax = fig.add_subplot(gs[1, 2])
F.cercle(ax, (0, 0), 1, color=F.INK, lw=1.4)
for h in HYP:
    ax.plot(h[0], h[1], color=F.BLEU, lw=1.0, alpha=0.85)
F.point(ax, *P5, F.INK, 7, 6)
ax.text(P5[0] + 0.05, P5[1] + 0.06, "P", fontsize=10.5, fontweight="bold", bbox=FOND, zorder=7)
ax.text(-1.32, -1.08, "Indice 2/(1 − r²) : le disque de Poincaré. Les rayons partis de P\n"
        "ne se recroisent jamais et filent vers le bord, qu'ils touchent à angle\n"
        "droit. Avec 2/(1 + r²) (l'œil de poisson), ils se recroisent tous :\n"
        "sphère, plan et plan hyperbolique, trois courbures.\n"
        "Ptolémée vaut aussi dans le plan hyperbolique (longueurs λ de Penner),\n"
        "et sa relation du pentagone, x_(n+1) = (1 + x_n)/x_(n−1), revient\n"
        "à son départ en 5 pas, autour du point fixe φ.", fontsize=9, color=F.INK2, va="top")
schema(ax, (-1.35, 1.35), (-2.05, 1.12))
ax.set_title("f)  Le plan hyperbolique, jumeau de l'œil de poisson")
F.sauver(fig, "j1_carre_ptolemee.png")
