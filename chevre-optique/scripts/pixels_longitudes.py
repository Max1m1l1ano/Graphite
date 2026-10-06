"""
Partie XVIII : faire des ronds avec des carrés. Le mod, les pixels et les longitudes qui manquaient.

    python3 scripts/pixels_longitudes.py        # ≈ 15 s

Écrit resultats/pixels_longitudes.md, figures/r1_pixels_contacts.png et figures/r2_longitudes_lumiere.png.

1. Les huit octants du cercle de pixels (algorithme du point milieu) : bornes à 45°, 135°, 225°, 315°.
2. Le contact vu à travers l'épaisseur du trait puis à travers les pixels : intérieur long, extérieur court.
3. Compter les pixels : le cercle de Gauss, en décimal (317, 31 417…) et en binaire ; l'écart se coupe en un terme
   lisse 4√2 ζ(−1/2) √R (les tangentes verticales) et une somme de dents de scie (le « mod 1 »).
4. L'espace entre les nombres : pixels intérieurs et extérieurs, écart exactement 8R (argument modulo 4),
   l'escalier de périmètre 8R − 4 (« π = 4 »), et la chèvre encadrée de façon certaine par les pixels.
5. Les longitudes : la lame de zones (latitudes) se replie au bord, l'étoile de Siemens (longitudes) au centre ;
   le globe vu du pôle a les deux.
6. La lumière : le pixel qui intègre, le flou optique qui arrondit.
"""

import logging
import math
import os
import sys

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from matplotlib.patches import Polygon, Rectangle
from scipy.ndimage import gaussian_filter
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
ROUGE, VIOLET = "#d0342c", "#7d4fc4"
R2 = math.sqrt(2)
RHO = 1 / R2
D_INT, D_EXT = 1 - RHO, 1 + RHO
R_VRAI_TXT = "1.15872847301812151782823350993"  # corde certifiée (partie XVII), en texte pour garder tous les chiffres
R_VRAI = float(R_VRAI_TXT)
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.6f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


# ---------------------------------------------------------------------------
# 1. Les huit octants
# ---------------------------------------------------------------------------
def point_milieu(R):
    """Pixels du premier octant (de 90° à 45°) par l'algorithme du point milieu, puis les huit reflets."""
    x, y, p = 0, R, 1 - R
    octant = []
    while x <= y:
        octant.append((x, y))
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
    tous = set()
    for a, b in octant:
        for u, v in ((a, b), (b, a), (-a, b), (-b, a), (a, -b), (b, -a), (-a, -b), (-b, -a)):
            tous.add((u, v))
    return octant, tous


ligne("## 1. Les huit octants du cercle de pixels\n")
ligne("L'algorithme du point milieu ne calcule qu'un huitième du cercle, de 90° à 45°, puis le reflète huit fois. Les"
      " frontières sont à 45°, 135°, 225° et 315° (et aux axes). Dans un octant, une coordonnée avance d'un pixel à"
      " chaque pas ; l'autre avance de 0 ou de 1 selon le signe d'une variable de décision : c'est un arrondi, un"
      " « mod 1 ».\n")
ligne("| R (pixels) | pixels du 1er octant | pixels du cercle entier | pas « en diagonale » dans l'octant |")
ligne("|---:|---|---|---|")
for R in (5, 10, 20, 50, 100):
    octant, tous = point_milieu(R)
    diag = sum(1 for i in range(1, len(octant)) if octant[i][1] != octant[i - 1][1])
    ligne(f"| {R} | {len(octant)} | {len(tous)} | {diag} |")
ligne("\nNombre de pixels par unité de longueur d'une courbe de direction θ : |cos θ| + |sin θ|. Il vaut 1 le long des"
      f" axes et √2 = {fr(R2, '{:.4f}')} à 45°, 135°, 225° et 315° : la diagonale 1x, 1y coûte 1 + 1 = 2 pixels pour une"
      f" longueur √2. En moyenne sur le cercle : 4/π = {fr(4 / math.pi, '{:.4f}')}.")

# ---------------------------------------------------------------------------
# 2. Le contact vu par l'épaisseur du trait, puis par les pixels
# ---------------------------------------------------------------------------
ligne("\n## 2. Le contact vu à travers l'épaisseur du trait, puis à travers les pixels\n")
ecart_int = lambda y: math.sqrt(1 - y * y) - (D_INT + math.sqrt(RHO ** 2 - y * y))
ecart_ext = lambda y: (D_EXT - math.sqrt(RHO ** 2 - y * y)) - math.sqrt(1 - y * y)
ligne("Deux traits d'épaisseur w se confondent là où leurs axes sont à moins de w l'un de l'autre. Près de P, l'écart"
      " vaut y²(√2 ∓ 1)/2 : la zone de contact apparent a pour demi-longueur √(2w/(√2 ∓ 1)).\n")
ligne("| w (en rayons du pré) | demi-longueur, contact intérieur | contact extérieur | rapport | arc apparent intérieur | extérieur |")
ligne("|---:|---|---|---|---|---|")
for w in (0.05, 0.021, 0.01, 1e-3, 1e-4):
    yi = brentq(lambda y: ecart_int(y) - w, 1e-12, 0.7)
    ye = brentq(lambda y: ecart_ext(y) - w, 1e-12, 0.7)
    ligne(f"| {fr(w, '{:g}')} | {fr(yi, '{:.5f}')} | {fr(ye, '{:.5f}')} | {fr(yi / ye, '{:.4f}')} |"
          f" {fr(2 * math.degrees(math.asin(yi)), '{:.1f}')}° | {fr(2 * math.degrees(math.asin(ye)), '{:.1f}')}° |")
ligne(f"\nLe rapport tend vers √2 + 1 = {fr(R2 + 1, '{:.4f}')} quand le trait s'affine. Sur la figure q1 de la partie XVII,"
      " les traits font environ w ≈ 0,021 rayon : le contact intérieur semble couvrir un arc d'environ 35°, l'extérieur"
      " d'environ 15°.")


def anneau(cx, R, L, x0=None, demi=None):
    """Pixels dont le centre est à moins d'un demi-pixel du cercle (centre (cx, 0), rayon R). Par défaut sur
    [−L, L]² ; avec x0 et demi, seulement sur la fenêtre x ∈ [x0 − demi, x0 + demi], y ∈ [−L, L]."""
    if x0 is None:
        ys, xs = np.mgrid[-L:L + 1, -L:L + 1]
    else:
        ys, xs = np.mgrid[-L:L + 1, x0 - demi:x0 + demi + 1]
    return np.abs(np.hypot(xs - cx, ys) - R) < 0.5


ligne("\n**Avec des pixels** (anneau numérique : pixels dont le centre est à moins d'un demi-pixel du cercle). Pré de"
      " N pixels de rayon, petits cercles de N/√2 :\n")
ligne("| N | pixels partagés, contact intérieur | contact extérieur | colonne verticale du petit cercle 2⌊√(N/√2 + 1/4)⌋ + 1 | (4/3)√(2(√2 + 1)N) |")
ligne("|---:|---|---|---|---|")
PARTAGE = []
for N in (8, 16, 32, 64, 128, 256, 512, 1024, 2048):
    L, dx_ = int(4 * math.sqrt(N)) + 10, 16  # le contact est près de P = (N, 0)
    Fr_, I_, E_ = (anneau(0, N, L, N, dx_), anneau(N * D_INT, N * RHO, L, N, dx_),
                   anneau(N * D_EXT, N * RHO, L, N, dx_))
    si, se = int((Fr_ & I_).sum()), int((Fr_ & E_).sum())
    col = 2 * math.floor(math.sqrt(N * RHO + 0.25)) + 1
    PARTAGE.append((N, si, se, col))
    ligne(f"| {N} | {si} | {se} | {col} | {fr(4 / 3 * math.sqrt(2 * (R2 + 1) * N), '{:.1f}')} |")
ligne("\nAu contact extérieur, les pixels partagés sont exactement la colonne verticale du petit cercle au point de"
      " tangence. Au contact intérieur, les deux anneaux restent ensemble bien au-delà de cette colonne.")
ligne("\nColonne verticale au point le plus à droite d'un cercle de N pixels : 2⌊√(N + 1/4)⌋ + 1 pixels.\n")
ligne("| N | " + " | ".join(str(N) for N in range(1, 13)) + " |")
ligne("|---:|" + "---|" * 12)
ligne("| pixels | " + " | ".join(str(2 * math.floor(math.sqrt(N + 0.25)) + 1) for N in range(1, 13)) + " |")
ligne("\nTrois pixels pour les cercles de rayon 1, 2 et 3 : la plus petite tangente verticale.")


# ---------------------------------------------------------------------------
# 3. Compter les pixels : le cercle de Gauss, le décimal, le binaire, le mod 1
# ---------------------------------------------------------------------------
def gauss(R):
    """Nombre de points entiers dans x² + y² ≤ R² (R entier), calcul exact."""
    x = np.arange(-R, R + 1, dtype=np.int64)
    v = R * R - x * x
    y = np.floor(np.sqrt(v.astype(np.float64))).astype(np.int64)
    y = np.where((y + 1) ** 2 <= v, y + 1, y)
    y = np.where(y * y > v, y - 1, y)
    return int((2 * y + 1).sum())


def communs(a, b):
    n = 0
    for ca, cb in zip(a, b):
        if ca != cb:
            break
        n += 1
    return n


ligne("\n## 3. Compter les pixels : le cercle de Gauss, en décimal et en binaire\n")
ligne("N(R) = nombre de pixels (points entiers) dans le disque de rayon R. Gauss a donné N(10) = 317 et N(100) = 31 417.\n")
ligne("| R | N(R) | πR² | écart E = N − πR² | chiffres communs avec π·R² |")
ligne("|---:|---|---|---|---|")
mp.mp.dps = 40
DEC = []
for k in range(0, 7):
    R = 10 ** k
    N = gauss(R)
    piR2 = mp.pi * R * R
    E = float(N - piR2)
    c = communs(str(N), mp.nstr(piR2, 30).replace(".", ""))
    DEC.append((R, N, E))
    ligne(f"| 10^{k} | {N} | {mp.nstr(piR2, 16).replace('.', ',')} | {fr(E, '{:+.2f}')} | {c} |")
ligne("\nEn binaire (R = 2^k), N(R) écrit en base 2 reproduit les premiers bits de π = 11,0010010000111111011010101…\n")
ligne("| R | N(R) en binaire | bits communs avec π·R² |")
ligne("|---:|---|---|")
BIN = []
pi_bin = mp.nstr(mp.pi, 60)
for k in range(0, 21, 4):
    R = 2 ** k
    N = gauss(R)
    piR2 = mp.pi * R * R
    nb = bin(N)[2:]
    pb = bin(int(mp.floor(piR2 * 2 ** 20)))[2:]  # bits de π·R² (avec 20 bits après la virgule)
    c = communs(nb, pb)
    BIN.append((R, N, float(N - piR2)))
    ligne(f"| 2^{k} | {nb} | {c} |")
ligne("\n**L'écart se coupe en deux, exactement.** Avec ⌊y⌋ = y − ½ − ψ(y), où ψ(y) = (y mod 1) − ½ est la dent de scie :")
ligne("E(R) = T(R) + S(R) + 2, où T(R) = Σ 2√(R² − x²) − πR² (l'erreur des trapèzes) et S(R) = −2 Σ_{|x|<R} ψ(√(R² − x²))"
      " (la somme des dents de scie : le « mod 1 » de chaque colonne).")
ligne(f"Le terme lisse vient des deux tangentes verticales (x = ±R) : T(R) ≈ 4√2 ζ(−1/2) √R ="
      f" {fr(4 * R2 * float(mp.zeta(-0.5)), '{:.6f}')} √R.\n")
ligne("| R | E(R) | T(R) | T/√R | S(R) | T + S + 2 |")
ligne("|---:|---|---|---|---|---|")
GAUSS_PTS = []
for R in (10, 100, 1000, 10 ** 4, 10 ** 5, 10 ** 6):
    x = np.arange(-R, R + 1, dtype=np.float64)
    yv = np.sqrt(R * R - x * x)
    T_ = float(2 * yv.sum() - math.pi * R * R)
    yint = yv[1:-1]
    S_ = float(-2 * ((yint - np.floor(yint)) - 0.5).sum())
    E_ = gauss(R) - math.pi * R * R
    GAUSS_PTS.append((R, E_, T_, S_))
    ligne(f"| {R} | {fr(E_, '{:+.2f}')} | {fr(T_, '{:+.2f}')} | {fr(T_ / math.sqrt(R), '{:.5f}')} | {fr(S_, '{:+.2f}')} |"
          f" {fr(T_ + S_ + 2, '{:+.2f}')} |")
ligne("\nBornes connues : E(R) = O(R^(131/208)) ≈ R^0,6298 (Huxley, 2003), amélioré en R^0,6289 (Li et Yang, prépublication"
      " 2023) ; une prépublication de Bourgain et Watt (2017) annonce R^(517/824) ≈ R^0,6274. Conjecture de Hardy :"
      " R^(1/2 + ε).")

# ---------------------------------------------------------------------------
# 4. L'espace entre les nombres : pixels intérieurs et extérieurs
# ---------------------------------------------------------------------------
ligne("\n## 4. L'espace entre les nombres : pixels intérieurs et extérieurs\n")


def demi_largeurs(cx, R, x, mode):
    """Pour chaque colonne de pixels x, demi-hauteur entière des pixels entièrement dans le disque (mode 'in') ou qui
    le touchent (mode 'out') ; −1 s'il n'y en a aucun."""
    dx = np.abs(x - cx)
    if mode == "in":
        v = R * R - (dx + 0.5) ** 2
        h = np.where(v >= 0, np.floor(np.sqrt(np.clip(v, 0, None)) - 0.5), -1)
        return np.where(h >= 0, h, -1)
    v = R * R - np.maximum(dx - 0.5, 0) ** 2
    h = np.ceil(np.sqrt(np.clip(v, 0, None)) + 0.5) - 1
    return np.where(v > 0, h, -1)


def compte(R, mode, rho=None):
    x = np.arange(-R - 1, R + 2, dtype=np.float64)
    h = demi_largeurs(0.0, R, x, mode)
    if rho is not None:
        h = np.minimum(h, demi_largeurs(float(R), rho, x, mode))
    return float(np.where(h >= 0, 2 * h + 1, 0).sum())


ligne("| R | pixels entièrement dedans | πR² | pixels touchés | écart | 8R | π certain entre |")
ligne("|---:|---|---|---|---|---|---|")
for R in (10, 100, 1000, 10 ** 4):
    n_in, n_out = compte(R, "in"), compte(R, "out")
    ligne(f"| {R} | {int(n_in)} | {fr(math.pi * R * R, '{:.1f}')} | {int(n_out)} | {int(n_out - n_in)} | {8 * R} |"
          f" {fr(n_in / R / R, '{:.6f}')} et {fr(n_out / R / R, '{:.6f}')} |")
ligne("\nL'écart vaut exactement 8R : chaque quart de cercle traverse R lignes verticales et R horizontales de la grille"
      " (2R + 1 pixels), et le cercle ne passe jamais par un coin de pixel, parce qu'un coin a des coordonnées"
      " demi-entières : (2x)² + (2y)² serait la somme de deux carrés impairs, ≡ 2 modulo 4, alors que 4R² ≡ 0 modulo 4.")
for R in (10, 100, 1000):
    i = np.arange(-R - 1, R + 2)
    I, J = np.meshgrid(i, i)
    M = (((np.abs(I) + 0.5) ** 2 + (np.abs(J) + 0.5) ** 2) <= R * R).astype(int)
    per = int(np.abs(np.diff(M, axis=0)).sum() + np.abs(np.diff(M, axis=1)).sum())
    ligne(f"- R = {R} : périmètre de l'escalier intérieur = {per} = 8R − 4 ; rapport au cercle {fr(per / (2 * math.pi * R), '{:.4f}')}"
          f" → 4/π = {fr(4 / math.pi, '{:.4f}')}.")


def corde_centres(R):
    """Chèvre comptée par les centres de pixels : corde qui couvre la moitié des pixels du pré."""
    cible = gauss(R) / 2
    x0 = np.arange(-R, R + 1, dtype=np.float64)
    yf = np.floor(np.sqrt(np.clip(R * R - x0 * x0, 0, None)))

    def nb(rho):
        v = rho * rho - (x0 - R) ** 2
        yc = np.floor(np.sqrt(np.clip(v, 0, None)))
        return float(np.where(v >= 0, 2 * np.minimum(yf, yc) + 1, 0).sum())

    lo, hi = 1.0 * R, 1.5 * R
    for _ in range(70):
        m = (lo + hi) / 2
        lo, hi = (lo, m) if nb(m) >= cible else (m, hi)
    return hi / R


def corde_certaine(R):
    """Encadrement certain de la corde par les pixels : intérieur et extérieur, pour le pré et pour la lentille."""
    f_in, f_out = compte(R, "in"), compte(R, "out")
    lo, hi = 1.0 * R, 1.5 * R
    for _ in range(64):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if compte(R, "out", m) < f_in / 2 else (lo, m)
    bas = lo
    lo, hi = 1.0 * R, 1.6 * R
    for _ in range(64):
        m = (lo + hi) / 2
        lo, hi = (lo, m) if compte(R, "in", m) > f_out / 2 else (m, hi)
    return bas / R, hi / R


ligne("\n**La chèvre en pixels.** Deux façons de la compter, sur un pré de R pixels de rayon :")
ligne("- par les centres des pixels (rapide, mais sans garantie) ;")
ligne("- par les pixels entièrement dedans et ceux qui touchent (lent, mais certain : la vraie corde est forcément dans"
      " l'intervalle).\n")
ligne("| R | corde par les centres | écart à r | encadrement certain | largeur | r dedans ? |")
ligne("|---:|---|---|---|---|---|")
CHEVRE = []
for base, ks in ((10, range(1, 6)), (2, range(3, 18, 2))):
    for k in ks:
        R = base ** k
        rc = corde_centres(R)
        b, h = corde_certaine(R)
        CHEVRE.append((base, R, rc - R_VRAI, h - b))
        ligne(f"| {base}^{k} | {fr(rc, '{:.10f}')} | {fr(rc - R_VRAI, '{:+.2e}')} | [{fr(b, '{:.8f}')} ; {fr(h, '{:.8f}')}] |"
              f" {fr(h - b, '{:.2e}')} | {'oui' if b <= R_VRAI <= h else 'NON'} |")
ligne("\nL'encadrement certain gagne exactement un chiffre par niveau décimal (×10) et un bit par niveau binaire (×2) :"
      " sa largeur vaut environ 4,6/R. Le comptage par les centres va plus vite (environ R^−1,5), mais sans garantie.")
r_mp = mp.mpf(R_VRAI_TXT)
ligne(f"\nLa corde en décimal : {R_VRAI_TXT.replace('.', ',')}… ; en binaire : 1,"
      + "".join(str(int(mp.floor(r_mp * 2 ** (i + 1))) % 2) for i in range(48)) + "…")

# ---------------------------------------------------------------------------
# 5 et 6. Les longitudes et la lumière (rayons de Nyquist)
# ---------------------------------------------------------------------------
NPX = 241
S2_ZONES = 100.0   # lame de zones : phase π r²/s², repli au-delà de r = s²/2
N_RAYONS = 72      # étoile de Siemens : 72 périodes sur le tour, repli en deçà de r = N/π
ligne("\n## 5. Les longitudes qui manquaient\n")
ligne(f"- Lame de zones (les latitudes vues du pôle) : phase π r²/s² avec s² = {S2_ZONES:g} pixels² ; fréquence locale r/s²,"
      f" repliement au-delà de r = s²/2 = {fr(S2_ZONES / 2, '{:g}')} pixels.")
ligne(f"- Étoile de Siemens (les longitudes) : {N_RAYONS} périodes sur le tour ; période locale 2πr/{N_RAYONS},"
      f" repliement en deçà de r = {N_RAYONS}/π = {fr(N_RAYONS / math.pi, '{:.1f}')} pixels.")
ligne("\n**Où se recréent les centres.** Aux points entiers, cos φ(x) = cos(φ(x) − 2π m·x) pour tout vecteur entier m :"
      " un nouveau centre apparaît là où ∇φ = 2π m.")
ligne(f"- Lame de zones, φ = π r²/s² : ∇φ = 2π x/s², donc les centres fantômes sont aux points s²·m du réseau"
      f" (à {fr(S2_ZONES, '{:g}')}, {fr(S2_ZONES * R2, '{:.1f}')}, {fr(2 * S2_ZONES, '{:g}')} pixels…), hors du disque de Nyquist.")
ligne(f"- Étoile, φ = Nθ : ∇φ = N(−y, x)/r², donc les centres fantômes sont aux points (N/2π)·(m₂, −m₁)/|m|² : le réseau"
      f" inversé (x ↦ x/|x|²), tourné de 90°, à {fr(N_RAYONS / (2 * math.pi), '{:.2f}')}, {fr(N_RAYONS / (2 * math.pi) / R2, '{:.2f}')},"
      f" {fr(N_RAYONS / (4 * math.pi), '{:.2f}')} pixels… du centre, dans le disque de Nyquist.")
ligne(f"- Pour un même m, distance du fantôme des anneaux × distance du fantôme des rayons = s²N/(2π) ="
      f" {fr(S2_ZONES * N_RAYONS / (2 * math.pi), '{:.1f}')} : la forme de Newton x·x' = f² (partie XVII).")
ligne("- Globe vu du pôle, parallèles et méridiens tous les 5° : les méridiens se replient près du pôle (rayon"
      f" 2/(5° en radians) = {fr(2 / math.radians(5), '{:.1f}')} pixels), les parallèles près du bord.")
ligne("\n## 6. La lumière\n")
ligne(f"- 300 pixels par pouce vus à 30 cm : un pixel sous-tend {fr(math.degrees(25.4e-3 / 300 / 0.3) * 60, '{:.2f}')}"
      " minute d'arc (l'acuité « 10/10 » vaut environ 1 minute).")
ligne(f"- Pupille de 3 mm, lumière à 550 nm : limite de diffraction 1,22 λ/D = {fr(math.degrees(1.22 * 550e-9 / 3e-3) * 60, '{:.2f}')}"
      " minute d'arc.")
ligne("- Sous un flou plus large que le pixel, un pixel carré de côté p devient indiscernable d'un disque de rayon"
      " p/√3 (même étalement), l'écart décroissant comme (p/σ)⁴ (partie X).")

with open(os.path.join(ICI, "..", "resultats", "pixels_longitudes.md"), "w") as fh:
    fh.write("# Résultats de la partie XVIII (générés par scripts/pixels_longitudes.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure 1 : les pixels et les contacts
# ===========================================================================
BOITE = dict(fc=F.SURF, ec="none", alpha=0.88, pad=0.5)
fig = plt.figure(figsize=(21, 14))
gs = fig.add_gridspec(2, 3, wspace=0.16, hspace=0.2)


def bande(ax, cx, R, w, couleur, alpha):
    t = np.linspace(-np.pi, np.pi, 800)
    ext = np.c_[cx + (R + w / 2) * np.cos(t), (R + w / 2) * np.sin(t)]
    inn = np.c_[cx + (R - w / 2) * np.cos(t[::-1]), (R - w / 2) * np.sin(t[::-1])]
    ax.add_patch(Polygon(np.r_[ext, inn], closed=True, fc=couleur, ec="none", alpha=alpha))


# a) l'épaisseur du trait près du point de contact
ax = fig.add_subplot(gs[0, 0])
W = 0.021
bande(ax, 0, 1, W, F.INK, 0.55)
bande(ax, D_INT, RHO, W, F.BLEU, 0.55)
bande(ax, D_EXT, RHO, W, ROUGE, 0.55)
yi = brentq(lambda y: ecart_int(y) - W, 1e-12, 0.7)
ye = brentq(lambda y: ecart_ext(y) - W, 1e-12, 0.7)
for y_, c in ((yi, F.BLEU), (ye, ROUGE)):
    for sg in (1, -1):
        x_ = math.sqrt(1 - y_ * y_)
        ax.plot([x_], [sg * y_], "o", ms=7, color=c, mec=F.SURF, mew=1.2, zorder=6)
ax.plot([1], [0], "o", ms=10, color=F.ORANGE, mec=F.SURF, mew=1.5, zorder=7)
ax.annotate(f"contact apparent intérieur :\n± {fr(math.degrees(math.asin(yi)), '{:.1f}')}° autour de P", (math.sqrt(1 - yi * yi), yi),
            (0.45, 0.47), fontsize=8.6, color=F.BLEU, arrowprops=dict(arrowstyle="-", color=F.BLEU, lw=0.8))
ax.annotate(f"contact apparent extérieur :\n± {fr(math.degrees(math.asin(ye)), '{:.1f}')}° autour de P", (math.sqrt(1 - ye * ye), -ye),
            (1.1, -0.47), fontsize=8.6, color=ROUGE, arrowprops=dict(arrowstyle="-", color=ROUGE, lw=0.8))
ax.text(1.27, 0.3, "Traits de même épaisseur\nw = 0,021 rayon (ceux de\nla figure q1). Ils se\nconfondent là où l'écart\n"
        "des cercles est < w :\ndemi-longueur √(2w/(√2 ∓ 1)),\nrapport → √2 + 1.", fontsize=8.4, color=F.INK2, va="top")
ax.set_xlim(0.6, 1.75)
ax.set_ylim(-0.75, 0.6)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("a)  L'épaisseur du trait fabrique une zone de contact")

# b) les mêmes cercles en pixels
ax = fig.add_subplot(gs[0, 1])
NB = 18
L = int(NB * 1.25)
Fr_, I_, E_ = anneau(0, NB, L * 2), anneau(NB * D_INT, NB * RHO, L * 2), anneau(NB * D_EXT, NB * RHO, L * 2)
img = np.ones(Fr_.shape + (3,))
coul = {"F": (0.35, 0.35, 0.35), "I": plt.matplotlib.colors.to_rgb(F.BLEU), "E": plt.matplotlib.colors.to_rgb(ROUGE),
        "X": plt.matplotlib.colors.to_rgb(F.ORANGE)}
img[Fr_] = coul["F"]
img[I_] = coul["I"]
img[E_] = coul["E"]
img[(Fr_ & I_) | (Fr_ & E_)] = coul["X"]
cxp = L * 2
ax.imshow(img, extent=(-2 * L - 0.5, 2 * L + 0.5, -2 * L - 0.5, 2 * L + 0.5), origin="lower", interpolation="nearest")
for k in range(-2 * L, 2 * L + 2):
    ax.axvline(k - 0.5, color="white", lw=0.3)
    ax.axhline(k - 0.5, color="white", lw=0.3)
ax.set_xlim(NB - 13.5, NB + 14.5)
ax.set_ylim(-11.5, 11.5)
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
si = int((Fr_ & I_).sum())
se = int((Fr_ & E_).sum())
ax.text(0.0, -0.02, f"Pré de {NB} pixels de rayon (gris), petits cercles de {NB}/√2 : bleu = contact intérieur,\n"
        f"rouge = contact extérieur, orange = pixels partagés : {si} avec le bleu, {se} avec le rouge.\n"
        "Le rouge ne partage que la colonne verticale de la tangente.", fontsize=8.4, va="top", transform=ax.transAxes,
        color=F.INK2)
ax.set_title("b)  Les mêmes contacts en pixels")

# c) pixels partagés selon la taille
ax = fig.add_subplot(gs[0, 2])
Ns = np.array([p[0] for p in PARTAGE])
ax.loglog(Ns, [p[1] for p in PARTAGE], "o-", color=F.BLEU, label="partagés au contact intérieur")
ax.loglog(Ns, [p[2] for p in PARTAGE], "s-", color=ROUGE, label="partagés au contact extérieur")
nn = np.geomspace(8, 2048, 100)
ax.loglog(nn, 4 / 3 * np.sqrt(2 * (R2 + 1) * nn), color=F.BLEU, lw=0.9, ls="--", label="(4/3)√(2(√2 + 1)N)")
ax.loglog(nn, 2 * np.sqrt(nn * RHO), color=ROUGE, lw=0.9, ls="--", label="colonne verticale ≈ 2√(N/√2)")
ax.set_xlabel("rayon du pré N (pixels)")
ax.set_ylabel("pixels partagés")
ax.legend(loc="upper left", fontsize=8.3, frameon=True, facecolor=F.SURF, edgecolor="none")
ins = ax.inset_axes([0.58, 0.08, 0.38, 0.3])
Ns_ = np.arange(1, 13)
ins.step(Ns_, [2 * math.floor(math.sqrt(N + 0.25)) + 1 for N in Ns_], where="mid", color=F.INK, lw=1.4)
ins.set_title("colonne verticale d'un cercle de N px", fontsize=8, fontweight="normal")
ins.set_yticks([3, 5, 7])
ins.tick_params(labelsize=7)
ins.text(1.2, 3.25, "3 pixels", fontsize=7.5)
ax.set_title("c)  Le contact extérieur = la tangente verticale")

# d) les huit octants et 225°
ax = fig.add_subplot(gs[1, 0])
RO = 12
octant, tous = point_milieu(RO)
COUL8 = [F.BLEU, F.AQUA, VIOLET, F.JAUNE, F.ORANGE, ROUGE, F.SEQ[10], F.MUTED]
for (u, v) in tous:
    ang = math.degrees(math.atan2(v, u)) % 360
    k8 = int(((ang + 0.0001) % 360) // 45)
    ax.add_patch(Rectangle((u - 0.5, v - 0.5), 1, 1, fc=COUL8[k8], ec="white", lw=0.6, alpha=0.85))
t = np.linspace(0, 2 * np.pi, 400)
ax.plot(RO * np.cos(t), RO * np.sin(t), color=F.INK, lw=0.9)
for a in range(0, 360, 45):
    ax.plot([0, 15 * math.cos(math.radians(a))], [0, 15 * math.sin(math.radians(a))], color=F.INK2, lw=0.8, ls=":")
    ax.text(16.3 * math.cos(math.radians(a)), 16.3 * math.sin(math.radians(a)), f"{a}°", ha="center", va="center",
            fontsize=9, color=F.INK if a != 225 else ROUGE, fontweight="bold" if a == 225 else "normal")
ax.text(-16.5, -18.2, "Le point milieu calcule un octant (de 90° à 45°) et le reflète huit fois. 225° = 180 + 45 = 270 − 45 :\n"
        "à chaque diagonale, le pas change de nature (droit ou en diagonale). C'est là qu'un trait de pixels\n"
        "coûte le plus : |cos θ| + |sin θ| = √2 pixels par unité de longueur.", fontsize=8.3, color=F.INK2, va="top")
ax.set_xlim(-18, 18)
ax.set_ylim(-21.5, 18)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("d)  Les huit octants du cercle de pixels")

# e) l'escalier : intérieur (bleu), extérieur (rouge), π = 4
ax = fig.add_subplot(gs[1, 1])
RE = 9
for i_ in range(-RE - 1, RE + 2):
    for j_ in range(-RE - 1, RE + 2):
        far = (abs(i_) + 0.5) ** 2 + (abs(j_) + 0.5) ** 2
        near = max(abs(i_) - 0.5, 0) ** 2 + max(abs(j_) - 0.5, 0) ** 2
        if far <= RE * RE:
            ax.add_patch(Rectangle((i_ - 0.5, j_ - 0.5), 1, 1, fc=F.SEQ[4], ec="white", lw=0.5))
        elif near < RE * RE:
            ax.add_patch(Rectangle((i_ - 0.5, j_ - 0.5), 1, 1, fc="#f2b6ae", ec="white", lw=0.5))
ax.plot(RE * np.cos(t), RE * np.sin(t), color=F.INK, lw=1.6)
n_in, n_out = compte(RE, "in"), compte(RE, "out")
ax.text(-RE - 1.4, RE + 4.9, f"Bleu : {int(n_in)} pixels entièrement dedans ; rouge : {int(n_out - n_in)} = 8R pixels"
        f" du bord.\nπR² = {fr(math.pi * RE * RE, '{:.1f}')} est forcément entre {int(n_in)} et {int(n_out)} :"
        " comme le cercle bleu et le cercle rouge,\nl'intérieur et l'extérieur enferment le vrai disque. Le périmètre"
        f" de l'escalier\nbleu vaut 8R − 4 = {8 * RE - 4}, contre 2πR = {fr(2 * math.pi * RE, '{:.1f}')} : rapport → 4/π.",
        fontsize=8.3, color=F.INK2, va="top")
ax.set_xlim(-RE - 1.6, RE + 1.6)
ax.set_ylim(-RE - 1.6, RE + 5.2)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("e)  Dedans, dehors : l'espace entre les nombres")

# f) l'écart du cercle de Gauss : lisse (tangentes) + dents de scie (mod 1)
ax = fig.add_subplot(gs[1, 2])
Rs = np.unique(np.round(np.geomspace(10, 3e5, 160)).astype(int))
Es, Ts, Ss = [], [], []
for R in Rs:
    x = np.arange(-R, R + 1, dtype=np.float64)
    yv = np.sqrt(R * R - x * x)
    T_ = 2 * yv.sum() - math.pi * R * R
    yint = yv[1:-1]
    S_ = -2 * ((yint - np.floor(yint)) - 0.5).sum()
    Es.append(gauss(int(R)) - math.pi * R * R)
    Ts.append(T_)
    Ss.append(S_)
Es, Ts, Ss = map(np.array, (Es, Ts, Ss))
ax.plot(Rs, Es / np.sqrt(Rs), "o", ms=3, color=F.INK, label="E(R)/√R : l'écart total")
ax.plot(Rs, Ts / np.sqrt(Rs), color=F.BLEU, lw=2, label="T(R)/√R : la part lisse (tangentes verticales)")
ax.plot(Rs, Ss / np.sqrt(Rs), "^", ms=3, color=F.ORANGE, label="S(R)/√R : les dents de scie (mod 1)")
ax.axhline(4 * R2 * float(mp.zeta(-0.5)), color=F.BLEU, lw=0.8, ls=":")
ax.text(12, 4 * R2 * float(mp.zeta(-0.5)) - 0.55, "4√2 ζ(−1/2) = −1,1760", fontsize=8.4, color=F.BLEU)
ax.set_xscale("log")
ax.set_xlabel("rayon R (pixels)")
ax.set_ylabel("écart divisé par √R")
ax.legend(loc="upper left", fontsize=8.2, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.text(12, -7.4, "N(10) = 317, N(100) = 31 417 (Gauss), N(10⁶) = 3 141 592 649 625 :\nles chiffres de π sortent du"
        " comptage, en décimal comme en binaire.", fontsize=8.3, color=F.INK2)
ax.set_ylim(-7.8, 6)
ax.set_title("f)  Compter les pixels : la tangente et le mod 1")
F.sauver(fig, "r1_pixels_contacts.png")

# ===========================================================================
# Figure 2 : les longitudes, les latitudes et la lumière
# ===========================================================================
SUR = 8  # sur-échantillonnage pour l'intégration sur le pixel


def motif(f, mode, sigma=0.0):
    """Image NPX × NPX d'un motif f(x, y) (coordonnées en pixels, centre au milieu) : 'point' = valeur au centre du
    pixel ; 'boite' = moyenne sur le pixel (le capteur) ; 'flou' = flou gaussien (optique) puis moyenne."""
    c = (NPX - 1) / 2
    if mode == "point":
        y, x = np.mgrid[0:NPX, 0:NPX] - c
        return f(x, y)
    u = (np.arange(NPX * SUR) + 0.5) / SUR - 0.5 - c
    Y, X = np.meshgrid(u, u, indexing="ij")
    v = f(X, Y)
    if sigma > 0:
        v = gaussian_filter(v, sigma * SUR)
    return v.reshape(NPX, SUR, NPX, SUR).mean(axis=(1, 3))


zones = lambda x, y: 0.5 + 0.5 * np.cos(np.pi * (x * x + y * y) / S2_ZONES)
etoile = lambda x, y: 0.5 + 0.5 * np.cos(N_RAYONS * np.arctan2(y, x))
RG = (NPX - 1) / 2 - 2


def globe(x, y):
    rr = np.hypot(x, y) / RG
    th = np.arcsin(np.clip(rr, 0, 1))  # angle au pôle
    lam = np.arctan2(y, x)
    v = 0.5 + 0.25 * np.cos(2 * np.pi * th / math.radians(5)) + 0.25 * np.cos(2 * np.pi * lam / math.radians(5))
    return np.where(rr <= 1, v, 1.0)


fig = plt.figure(figsize=(20, 13.6))
gs = fig.add_gridspec(2, 3, wspace=0.08, hspace=0.16)


def montre(ax, im, titre, legende, cercles=(), zoom=None):
    ext = (-(NPX - 1) / 2 - 0.5, (NPX - 1) / 2 + 0.5, -(NPX - 1) / 2 - 0.5, (NPX - 1) / 2 + 0.5)
    ax.imshow(im, cmap="gray", vmin=0, vmax=1, extent=ext, origin="lower", interpolation="nearest")
    if zoom:
        ax.set_xlim(-zoom, zoom)
        ax.set_ylim(-zoom, zoom)
    tt = np.linspace(0, 2 * np.pi, 300)
    for r_, c in cercles:
        ax.plot(r_ * np.cos(tt), r_ * np.sin(tt), color=c, lw=1.4, ls="--")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(titre, fontsize=11)
    ax.text(0.0, -0.03, legende, transform=ax.transAxes, fontsize=8.4, color=F.INK2, va="top")


ax = fig.add_subplot(gs[0, 0])
for m1 in (-1, 0, 1):
    for m2 in (-1, 0, 1):
        if (m1, m2) != (0, 0):
            ax.plot([S2_ZONES * m1], [S2_ZONES * m2], "o", ms=16, mfc="none", mec=F.ORANGE, mew=1.6, zorder=5)
montre(ax, motif(zones, "point"), "a)  Les latitudes : lame de zones en pixels",
       f"Anneaux de plus en plus serrés vers le bord. Au-delà de r = s²/2 = {S2_ZONES / 2:g} px (tirets), ils se\n"
       "replient : de nouveaux centres (cercles) apparaissent aux points s²·m du réseau.", [(S2_ZONES / 2, F.ORANGE)])
ax = fig.add_subplot(gs[0, 1])
montre(ax, motif(etoile, "point"), "b)  Les longitudes : étoile de Siemens en pixels",
       f"Rayons de plus en plus serrés vers le centre. En deçà de r = {N_RAYONS}/π = {fr(N_RAYONS / math.pi, '{:.1f}')} px (tirets),\n"
       "ils se replient : un disque de confusion se recrée au centre.", [(N_RAYONS / math.pi, F.ORANGE)])
ax = fig.add_subplot(gs[0, 2])
montre(ax, motif(globe, "point"), "c)  Le globe vu du pôle : parallèles et méridiens",
       "Les méridiens (tous les 5°) se replient près du pôle, les parallèles près du bord :\nles deux disques"
       " se recréent, au centre et en couronne.", [(2 / math.radians(5), F.ORANGE)])
ax = fig.add_subplot(gs[1, 0])
for m1 in range(-2, 3):
    for m2 in range(-2, 3):
        n2 = m1 * m1 + m2 * m2
        if 0 < n2 <= 2:
            k_ = N_RAYONS / (2 * math.pi) / n2
            ax.plot([k_ * m2], [-k_ * m1], "o", ms=13, mfc="none", mec=F.ORANGE, mew=1.5, zorder=5)
montre(ax, motif(etoile, "point"), "d)  Zoom du centre : le point au centre du pixel",
       "Échantillonnage pur. Les petites étoiles fantômes (cercles) sont au réseau inversé,\n(N/2π)·(m₂, −m₁)/|m|² :"
       " sur les axes et les diagonales à 45°, 135°, 225°, 315°.", [(N_RAYONS / math.pi, F.ORANGE)], zoom=34.5)
ax = fig.add_subplot(gs[1, 1])
montre(ax, motif(etoile, "boite"), "e)  Zoom : le pixel qui intègre (le capteur)",
       "Chaque pixel moyenne la lumière sur son carré : le moiré s'affaiblit mais reste.\nL'effet de bord du pixel est un"
       " flou carré, imparfait.", [(N_RAYONS / math.pi, F.ORANGE)], zoom=34.5)
ax = fig.add_subplot(gs[1, 2])
montre(ax, motif(etoile, "flou", sigma=0.7), "f)  Zoom : la lumière floutée avant les pixels",
       "Un flou optique (σ = 0,7 pixel, comme le filtre passe-bas des appareils photo)\nefface le moiré : le centre"
       " devient un disque gris uniforme, sans fausse structure.", [(N_RAYONS / math.pi, F.ORANGE)], zoom=34.5)
F.sauver(fig, "r2_longitudes_lumiere.png")
