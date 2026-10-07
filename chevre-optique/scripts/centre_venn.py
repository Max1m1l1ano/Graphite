"""
Partie XXX : le centre du Venn — la moitié du disque, les diaphragmes, les grains repositionnés et les tests du hasard.

    python3 scripts/centre_venn.py [chemin/vers/venn17]        # ≈ 2 min

Il faut la même copie du dépôt de Chris Dzoba que pour la partie XXIX (certificats et images sous licence CC BY 4.0) :

    git clone https://github.com/dzoba/venn17

placée par défaut à côté du dossier Graphite (../../.. depuis ce script), ou donnée en argument.

Écrit resultats/centre_venn.md et les figures ae1_centre_moitie.png, ae2_diaphragmes_diffraction.png et
ae3_grains_hasard.png.

1. Les centres : le centre de symétrie d'ordre 17 (corrélation de l'image avec ses rotations, sur la clarté perçue
   OKLab) et les centres de la lumière selon la façon de la peser.
2. La moitié du disque fait la moitié du Venn : l'encre dans le contour réduit de 1/√2 et à chaque cran, pour les deux
   rendus du dépôt (« pression » et « rose ») ; la densité de traits ; le budget en pixels ; les 18 certificats.
3. La sphère et les deux miroirs (Lambert, Archimède, Euler ; l'inversion des jumeaux de la partie XVII).
4. Les diaphragmes : crans et niveaux, de f/1 à f/88, les chèvres dans le Venn, Niven.
5. La figure de diffraction : 34 aigrettes du contour, 34 de l'intérieur.
6. Au plus près du centre : l'empilement des 17 copies (drizzle), la défocalisation, les limites de granularité.
7. Le banc d'essai des tests du hasard.
"""

import json
import logging
import math
import os
import re
import sys
import textwrap
import time
from fractions import Fraction
from math import comb

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from PIL import Image
from scipy import ndimage
from scipy.signal import find_peaks
from scipy.special import j1, jn_zeros

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ICI, "..", "..", "..", "dzoba", "venn17")
CERT = os.path.join(DEPOT, "certificates")
IMG_P = os.path.join(DEPOT, "images", "venn17-pressure-dark-2000.png")
IMG_R = os.path.join(DEPOT, "images", "venn17-rose-dark-2000.png")
if not (os.path.isdir(CERT) and os.path.isfile(IMG_P) and os.path.isfile(IMG_R)):
    sys.exit("Copie du dépôt introuvable : git clone https://github.com/dzoba/venn17, puis donne son chemin en argument.")
ROUGE, VIOLET, VERT = "#d0342c", "#7d4fc4", "#1baf7a"
R2 = math.sqrt(2)
ULL = 1.1587284730181215178282335
T0 = time.time()
md = []
mp.mp.dps = 60


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


def sup(n):
    return str(n).translate(str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))


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


ligne("# Partie XXX : le centre du Venn — la moitié du disque, les diaphragmes, les grains repositionnés et les tests"
      " du hasard\n")
ligne("Tableaux complets, recalculés par `scripts/centre_venn.py` à partir du dépôt de Chris Dzoba"
      " (https://github.com/dzoba/venn17 ; certificats et images sous licence CC BY 4.0).\n")


# ===========================================================================
# 0. Les images, en quatre façons de peser la lumière
# ===========================================================================
def charger(chemin):
    S8 = np.asarray(Image.open(chemin).convert("RGB"))
    S = S8.astype(float) / 255
    lin = np.where(S <= 0.04045, S / 12.92, ((S + 0.055) / 1.055) ** 2.4)
    del S
    l_ = np.cbrt(0.4122214708 * lin[..., 0] + 0.5363325363 * lin[..., 1] + 0.0514459929 * lin[..., 2])
    m_ = np.cbrt(0.2119034982 * lin[..., 0] + 0.6806995451 * lin[..., 1] + 0.1073969566 * lin[..., 2])
    s_ = np.cbrt(0.0883024619 * lin[..., 0] + 0.2817188376 * lin[..., 1] + 0.6299787005 * lin[..., 2])
    L = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_          # clarté perçue (OKLab)
    A = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    B = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
    del l_, m_, s_
    Y = 0.2126 * lin[..., 0] + 0.7152 * lin[..., 1] + 0.0722 * lin[..., 2]  # luminance (photométrie)
    E = lin.sum(2)                                                          # énergie dans les trois primaires
    MO = S8.astype(float).mean(2)                                           # moyenne des canaux sRGB
    del lin
    fond = {k: float(np.median(v[:20, :20])) for k, v in (("L", L), ("Y", Y), ("E", E), ("MO", MO))}
    return dict(S8=S8, L=L, A=A, B=B, Y=Y, E=E, MO=MO, fond=fond)


P_ = charger(IMG_P)
HAUT, LARG = P_["L"].shape
YY, XX = np.mgrid[0:HAUT, 0:LARG]
C_IMG = ((LARG - 1) / 2, (HAUT - 1) / 2)


def centre_symetrie(Lc, depart, ks=(1, 4, 8), pas=(2.0, 0.5, 0.125), sub=4, r0=30, r1=600):
    """Le centre qui rend l'image la plus semblable à ses rotations de 2πk/17 (corrélation sur la clarté lissée)."""
    Ls = ndimage.gaussian_filter(Lc, 1.0)
    yy, xx = YY[::sub, ::sub].astype(float), XX[::sub, ::sub].astype(float)
    u_all = Ls[::sub, ::sub]

    def corr(cx, cy, k):
        a = 2 * np.pi * k / 17
        rr = np.hypot(xx - cx, yy - cy)
        sel = (rr > r0) & (rr < r1)
        X_, Y_ = xx[sel] - cx, yy[sel] - cy
        v = ndimage.map_coordinates(Ls, [cy + X_ * np.sin(a) + Y_ * np.cos(a), cx + X_ * np.cos(a) - Y_ * np.sin(a)],
                                    order=1)
        return float(np.corrcoef(u_all[sel], v)[0, 1])

    def cherche(cx, cy, ks_, pas_):
        grille = None
        for p in pas_:
            grille = []
            for dx in (-2, -1, 0, 1, 2):
                for dy in (-2, -1, 0, 1, 2):
                    grille.append((float(np.mean([corr(cx + dx * p, cy + dy * p, k) for k in ks_])), dx * p, dy * p))
            c_, dx_, dy_ = max(grille)
            cx, cy = cx + dx_, cy + dy_
            grille = [(g_[0], g_[1] - dx_, g_[2] - dy_) for g_ in grille]
        # paraboloïde ajusté sur la dernière grille : le sommet, au sous-pas près
        M = np.array([[1, x_, y_, x_ * x_, x_ * y_, y_ * y_] for _, x_, y_ in grille])
        co = np.linalg.lstsq(M, np.array([g_[0] for g_ in grille]), rcond=None)[0]
        H_ = np.array([[2 * co[3], co[4]], [co[4], 2 * co[5]]])
        dxy = np.linalg.solve(H_, -co[1:3])
        if np.all(np.abs(dxy) < pas_[-1] * 2):
            cx, cy = cx + dxy[0], cy + dxy[1]
        return max(grille)[0], cx, cy

    c0, cx, cy = cherche(depart[0], depart[1], ks, pas)
    par_k = {k: cherche(cx, cy, (k,), (0.5, 0.125))[1:] for k in (1, 2, 4, 8)}
    return (cx, cy), c0, par_k


# ===========================================================================
# 1. Les centres
# ===========================================================================
ligne("## 1. Les centres\n")
LbP = P_["fond"]["L"]
C_SYM, CORR_SYM, PAR_K = centre_symetrie(np.clip(P_["L"] - LbP, 0, None), C_IMG)
D_IMG = math.hypot(C_SYM[0] - C_IMG[0], C_SYM[1] - C_IMG[1])
DISP_K = max(math.hypot(v_[0] - C_SYM[0], v_[1] - C_SYM[1]) for v_ in PAR_K.values())
ligne(f"- Centre de symétrie d'ordre 17 (rotations de 2πk/17, clarté perçue OKLab) : ({fr(C_SYM[0], '{:.3f}')} ;"
      f" {fr(C_SYM[1], '{:.3f}')}), corrélation {fr(CORR_SYM, '{:.4f}')}. Le centre de l'image est"
      f" ({fr(C_IMG[0], '{:.1f}')} ; {fr(C_IMG[1], '{:.1f}')}) : écart {fr(D_IMG, '{:.3f}')} px.")
ligne("- Estimations séparées, rotation par rotation : " + " ; ".join(
    f"k = {k} : ({fr(v_[0], '{:.3f}')} ; {fr(v_[1], '{:.3f}')})" for k, v_ in PAR_K.items())
    + f" (dispersion ≤ {fr(DISP_K, '{:.3f}')} px).")

FONDS = P_["fond"]
POIDS = [
    ("luminance Y (l'œil, photométrie)", lambda: np.clip(P_["Y"] - FONDS["Y"], 0, None)),
    ("masque de clarté OKLab (L > fond + 0,1)", lambda: (P_["L"] > LbP + 0.1).astype(float)),
    ("clarté OKLab L", lambda: np.clip(P_["L"] - LbP, 0, None)),
    ("masque en moyenne RGB (> fond + 25), celui de la partie XXIX", lambda: (P_["MO"] > FONDS["MO"] + 25).astype(float)),
    ("moyenne des canaux RGB", lambda: np.clip(P_["MO"] - FONDS["MO"], 0, None)),
    ("énergie R + G + B linéaire (radiométrie)", lambda: np.clip(P_["E"] - FONDS["E"], 0, None)),
]
BARY = []
for nom, fw in POIDS:
    w = fw()
    sw = w.sum()
    bx, by = float((w * XX).sum() / sw), float((w * YY).sum() / sw)
    BARY.append((nom, bx, by, math.hypot(bx - C_SYM[0], by - C_SYM[1]),
                 math.degrees(math.atan2(-(by - C_SYM[1]), bx - C_SYM[0]))))
del w
# le centre de symétrie cherché sur le masque RGB de la partie XXIX, avec la recherche fine : il est juste
C_SYM_RGB = centre_symetrie((P_["MO"] > FONDS["MO"] + 25).astype(float), C_IMG)[0]
D_RGB = math.hypot(C_SYM_RGB[0] - C_SYM[0], C_SYM_RGB[1] - C_SYM[1])


def centre_grossier(M, depart):
    """Mon premier essai, refait tel quel : masque lissé (σ = 2 px), un pixel sur 4, la seule rotation k = 1, départ au
    barycentre, fenêtre de ±8 px au pas de 2, puis de ±2 px au pas de 0,5."""
    Ms = ndimage.gaussian_filter(M.astype(float), 2)
    m4 = M[::4, ::4].astype(float)
    yy, xx = YY[::4, ::4], XX[::4, ::4]
    a = 2 * np.pi / 17

    def score(cx, cy):
        xr = cx + (xx - cx) * np.cos(a) - (yy - cy) * np.sin(a)
        yr = cy + (xx - cx) * np.sin(a) + (yy - cy) * np.cos(a)
        v = ndimage.map_coordinates(Ms, [yr.ravel(), xr.ravel()], order=1).reshape(m4.shape)
        return float((v * m4).sum() / m4.sum())
    best = max((score(depart[0] + dx, depart[1] + dy), dx, dy) for dx in np.arange(-8, 9, 2.0) for dy in np.arange(-8, 9, 2.0))
    bord1 = max(abs(best[1]), abs(best[2])) == 8
    cx, cy = depart[0] + best[1], depart[1] + best[2]
    best2 = max((score(cx + dx, cy + dy), dx, dy) for dx in np.arange(-2, 2.01, 0.5) for dy in np.arange(-2, 2.01, 0.5))
    bord2 = max(abs(best2[1]), abs(best2[2])) == 2
    return (cx + best2[1], cy + best2[2]), bord1 and bord2


C_ESSAI, BORD_ESSAI = centre_grossier(P_["MO"] > FONDS["MO"] + 25, (BARY[3][1], BARY[3][2]))
ligne("\n| pondération de la lumière | barycentre (x ; y) | écart au centre de symétrie | direction (° , y vers le haut) |")
ligne("|---|---|---:|---:|")
for nom, bx, by, d_, ang in BARY:
    ligne(f"| {nom} | ({fr(bx, '{:.2f}')} ; {fr(by, '{:.2f}')}) | {fr(d_, '{:.2f}')} px | {fr(ang, '{:.0f}')} |")
D_ESSAI = math.hypot(C_ESSAI[0] - C_SYM[0], C_ESSAI[1] - C_SYM[1])
ligne(f"\n- Mon premier essai (recherche grossière partie du barycentre du masque RGB) : ({fr(C_ESSAI[0], '{:.2f}')} ;"
      f" {fr(C_ESSAI[1], '{:.2f}')}), à {fr(D_ESSAI, '{:.2f}')} px du vrai centre ;"
      f" {'il s’est arrêté au bord de ses deux fenêtres de recherche' if BORD_ESSAI else 'pas au bord de ses fenêtres'}."
      f" Avec la recherche fine, le même masque RGB donne ({fr(C_SYM_RGB[0], '{:.3f}')} ; {fr(C_SYM_RGB[1], '{:.3f}')}),"
      f" à {fr(D_RGB, '{:.3f}')} px : ce n'est pas le masque qui trompait, c'est le point de départ.")

# les couleurs des 17 courbes, mesurées dans l'image (teintes 25° + 360°·i/17 de la palette du traceur)
Cc = np.hypot(P_["A"], P_["B"])
Hc = np.degrees(np.arctan2(P_["B"], P_["A"])) % 360
SAT = (Cc > 0.08) & (P_["L"] > 0.3)
COUL = []
for i in range(17):
    hc = (25 + 360 * i / 17) % 360
    s_ = SAT & (np.abs((Hc - hc + 180) % 360 - 180) < 4)
    Ls_ = P_["L"][s_]
    top = Ls_ > np.quantile(Ls_, 0.95)
    rgb = P_["S8"][s_][top].mean(0)
    lin_ = np.where(rgb / 255 <= 0.04045, rgb / 255 / 12.92, ((rgb / 255 + 0.055) / 1.055) ** 2.4)
    COUL.append(dict(h=hc, rgb=rgb, mo=float(rgb.mean()), L=float(Ls_[top].mean()),
                     Y=float(0.2126 * lin_[0] + 0.7152 * lin_[1] + 0.0722 * lin_[2]), E=float(lin_.sum())))
OM = np.exp(2j * np.pi * np.arange(17) / 17)


def dipole(v):
    v = np.asarray(v, float)
    return float(abs((v * OM).sum()) / v.sum())


DIP = {k: dipole([c_[k] for c_ in COUL]) for k in ("mo", "L", "Y", "E")}
ligne(f"\n- Les couleurs des 17 courbes (mesurées : les 5 % de pixels les plus clairs de chaque teinte) ont une clarté"
      f" perçue de {fr(min(c_['L'] for c_ in COUL), '{:.2f}')} à {fr(max(c_['L'] for c_ in COUL), '{:.2f}')}, une"
      f" moyenne RGB de {fr(min(c_['mo'] for c_ in COUL), '{:.0f}')} à {fr(max(c_['mo'] for c_ in COUL), '{:.0f}')}.")
ligne("- Premier harmonique (le dipôle) des 17 poids, selon la pesée : " + " ; ".join(
    f"{lab} {fr(100 * DIP[k], '{:.1f}')} %" for lab, k in (("clarté L", "L"), ("luminance Y", "Y"),
                                                         ("moyenne RGB", "mo"), ("énergie linéaire", "E"))) + ".")
ligne("- Si les 17 courbes pesaient pareil, le barycentre serait exactement le centre de symétrie : la rotation d'ordre"
      " 17 annule tout premier harmonique. Tout écart vient donc des poids, pas de la géométrie.")
ligne(f"- Précision du centre de symétrie : {fr(DISP_K, '{:.3f}')} px. L'écart du masque de la partie XXIX"
      f" ({fr(BARY[3][3], '{:.1f}')} px) en vaut {ent(round(BARY[3][3] / max(DISP_K, 1e-3)))} fois.")

# le trou central, vu du centre de symétrie
ENCRE_L = P_["L"] > LbP + 0.1
cxi, cyi = int(round(C_SYM[0])), int(round(C_SYM[1]))
bx_ = ENCRE_L[cyi - 60:cyi + 61, cxi - 60:cxi + 61]
yb, xb = np.nonzero(bx_)
R_TROU = float(np.hypot(xb + cxi - 60 - C_SYM[0], yb + cyi - 60 - C_SYM[1]).min())
EDT = ndimage.distance_transform_edt(~ENCRE_L)
sb_ = EDT[cyi - 40:cyi + 41, cxi - 40:cxi + 41]
iy_, ix_ = np.unravel_index(np.argmax(sb_), sb_.shape)
TROU_EDT = (cxi - 40 + ix_, cyi - 40 + iy_, float(sb_.max()))
ligne(f"- Trou central, vu du centre de symétrie : rayon {fr(R_TROU, '{:.2f}')} px. Le plus grand disque vide centré sur"
      f" un pixel est en ({TROU_EDT[0]} ; {TROU_EDT[1]}), à {fr(math.hypot(TROU_EDT[0] - C_SYM[0], TROU_EDT[1] - C_SYM[1]), '{:.2f}')}"
      f" px : la grille des pixels ne peut pas mieux faire.\n")


# ===========================================================================
# 2. La moitié du disque fait la moitié du Venn
# ===========================================================================
ligne("## 2. La moitié du disque fait la moitié du Venn\n")


def mesure_moitie(L, Lb, c, seuil=0.1, masque=None):
    M = (L > Lb + seuil) if masque is None else masque
    RR = np.hypot(XX - c[0], YY - c[1])
    TH = np.arctan2(YY - c[1], XX - c[0])
    NB = 3600
    Bn = ((TH + np.pi) / (2 * np.pi) * NB).astype(int) % NB
    RMAX = np.zeros(NB)
    np.maximum.at(RMAX, Bn[M], RR[M])
    rout = np.interp((TH + np.pi) / (2 * np.pi) * NB, np.arange(NB), RMAX)
    DED = RR < rout - 2
    RHO = RR / np.maximum(rout, 1.0)
    ENC = M & DED
    rho = RHO[ENC]
    Rc = float(RMAX.max())
    out = dict(Rc=Rc, aire=int(DED.sum()), encre=float(ENC.sum() / DED.sum()), RMAX=RMAX,
               contour=float(np.mean(rho <= 1 / R2)), cercle=float(np.mean(RR[ENC] <= Rc / R2)),
               mediane=float(np.median(rho)), m2=float(np.mean(rho ** 2)),
               crans=[float(np.mean(rho <= 2 ** (-j / 2))) for j in range(15)])
    q = np.sort(rho ** 2)
    out["cumul"] = (np.linspace(0, 1, 201), np.searchsorted(q, np.linspace(0, 1, 201), side="right") / len(q))
    dens = []
    for t in np.linspace(0.02, 0.98, 25):
        r = t * Rc
        n = max(64, int(4 * math.pi * r))
        a = np.linspace(0, 2 * math.pi, n, endpoint=False)
        v = ndimage.map_coordinates(M.astype(float), [c[1] + r * np.sin(a), c[0] + r * np.cos(a)], order=0)
        dens.append((t, np.count_nonzero(np.diff(np.r_[v, v[0]]) > 0.5) / (2 * math.pi * r)))
    out["densite"] = dens
    return out


MP = mesure_moitie(P_["L"], LbP, C_SYM)
MP_NAIF = mesure_moitie(P_["L"], LbP, (BARY[3][1], BARY[3][2]), masque=P_["MO"] > FONDS["MO"] + 25)
R_ = charger(IMG_R)
C_ROSE, CORR_ROSE, _ = centre_symetrie(np.clip(R_["L"] - R_["fond"]["L"], 0, None), C_IMG, ks=(1, 4), pas=(1.0, 0.25))
MR = mesure_moitie(R_["L"], R_["fond"]["L"], C_ROSE)
IM_ROSE = R_["S8"][::2, ::2].copy()
del R_
ligne(f"- Centre de symétrie du rendu « rose » : ({fr(C_ROSE[0], '{:.2f}')} ; {fr(C_ROSE[1], '{:.2f}')}),"
      f" corrélation {fr(CORR_ROSE, '{:.3f}')}.\n")
ligne("| rendu | encre de l'intérieur | dans le contour réduit de 1/√2 | dans le cercle R/√2 | rayon médian ρ | ⟨ρ²⟩ |")
ligne("|---|---:|---:|---:|---:|---:|")
for nom, m_ in (("pression, centre de symétrie, clarté", MP), ("pression, barycentre et masque de la partie XXIX", MP_NAIF),
                ("rose, centre de symétrie, clarté", MR)):
    ligne(f"| {nom} | {fr(100 * m_['encre'], '{:.1f}')} % | {fr(100 * m_['contour'], '{:.2f}')} % |"
          f" {fr(100 * m_['cercle'], '{:.2f}')} % | {fr(m_['mediane'], '{:.4f}')} | {fr(m_['m2'], '{:.4f}')} |")
ligne(f"\n- Pour une densité uniforme, ρ² est uniforme sur [0, 1] : le contour réduit de 1/√2 contient la moitié, le rayon"
      f" médian vaut 1/√2 = {fr(1 / R2, '{:.4f}')} et ⟨ρ²⟩ = 1/2. Le cercle de demi-aire est aussi le cercle quadratique"
      f" moyen (l'« étalement » de la partie X).")
ligne(f"- Le centre change la moitié mesurée : {fr(100 * MP_NAIF['cercle'], '{:.2f}')} % depuis le barycentre de la partie"
      f" XXIX, {fr(100 * MP['cercle'], '{:.2f}')} % depuis le centre de symétrie (cercle R/√2).\n")

ligne("**Les crans du diaphragme dans l'image** (part de l'encre dans le contour réduit de 2^(−j/2)) :\n")
ligne("| cran j | rayon | f/… | part attendue 2⁻ʲ | pression | rose |")
ligne("|---:|---:|---:|---:|---:|---:|")
F_NOM = ["1", "1,4", "2", "2,8", "4", "5,6", "8", "11", "16", "22", "32", "45", "64", "90", "128"]
for j in range(15):
    ligne(f"| {j} | {fr(2 ** (-j / 2), '{:.4f}')} | f/{F_NOM[j]} | {fr(2.0 ** -j, '{:.6f}')} | {fr(MP['crans'][j], '{:.6f}')} |"
          f" {fr(MR['crans'][j], '{:.6f}')} |")
ligne("\n**Traits par pixel d'arc**, le long de cercles (densité de lignes) :\n")
ligne("| rayon / R | " + " | ".join(fr(t, '{:.2f}') for t, _ in MP["densite"][::3]) + " |")
ligne("|---|" + "---:|" * len(MP["densite"][::3]))
ligne("| pression | " + " | ".join(fr(d_, '{:.3f}') for _, d_ in MP["densite"][::3]) + " |")
ligne("| rose | " + " | ".join(fr(d_, '{:.3f}') for _, d_ in MR["densite"][::3]) + " |")

# budget en pixels du cercle de demi-aire (partie XVIII)
r_dem = MP["Rc"] / R2
dxp, dyp = np.abs(XX - C_SYM[0]), np.abs(YY - C_SYM[1])
N_IN = int((np.hypot(dxp + 0.5, dyp + 0.5) <= r_dem).sum())
N_TOUCH = int((np.hypot(np.maximum(dxp - 0.5, 0), np.maximum(dyp - 0.5, 0)) < r_dem).sum())
N_CENT = int((np.hypot(dxp, dyp) <= r_dem).sum())
A_DEM = math.pi * r_dem ** 2
V17 = 131070
A_CROIS = MP["aire"] / V17
N_FROLE = 2 * math.pi * r_dem / math.sqrt(A_CROIS)
BUD_PIX = (N_TOUCH - N_IN) / 2 / A_DEM * 1e6
BUD_CROIS = N_FROLE / 2 / V17 * 1e6
ligne(f"\n- Le cercle de demi-aire en pixels (rayon {fr(r_dem, '{:.1f}')} px, aire {ent(round(A_DEM))}) : comptés par leur"
      f" centre, {ent(N_CENT)} pixels ({fr((N_CENT / A_DEM - 1) * 1e6, '{:+.0f}')} ppm) ; entièrement dedans {ent(N_IN)}, qui"
      f" le touchent {ent(N_TOUCH)} : écart {ent(N_TOUCH - N_IN)} = 8r à {fr(abs(N_TOUCH - N_IN - 8 * r_dem), '{:.1f}')} près"
      f" (partie XVIII), soit ±{fr(BUD_PIX, '{:.0f}')} ppm de façon certaine.")
ligne(f"- Au grain d'un croisement ({fr(A_CROIS, '{:.2f}')} pixels), le cercle en frôle environ {ent(round(N_FROLE))} :"
      f" ±{fr(BUD_CROIS, '{:.0f}')} ppm. L'image ne peut pas trancher la moitié mieux que cela ; le certificat, si.\n")

# les 18 certificats
ligne("**La moitié dans les 18 certificats** (croisements de niveau ≥ (n + 1)/2) :\n")
CERTS = []
for nom in sorted(os.listdir(CERT)):
    if not nom.endswith(".json"):
        continue
    with open(os.path.join(CERT, nom)) as fh:
        dd = json.load(fh)
    n = int(dd["n"])
    faces = dd["faces"]
    del dd
    lev = np.fromiter((min(lab.count("1") for lab in f_) + 1 for f_ in faces), dtype=np.int16, count=len(faces))
    tri = None
    if nom in ("best11-s0.json", "v3-13-s0.json", "venn17-local-c3-s2.json", "venn19-closure-s196002.json"):
        deg = np.bincount(np.fromiter((int(lab[::-1], 2) for f_ in faces for lab in f_), dtype=np.int64,
                                      count=4 * len(faces)), minlength=1 << n)
        tri = float(np.mean(deg[1:-1] == 3))
    del faces
    NL = np.bincount(lev, minlength=n)[1:n].astype(np.int64)
    pole = int(NL[0] + NL[-1])
    V = int(NL.sum())
    haut = int(NL[(n + 1) // 2 - 1:].sum())
    CERTS.append(dict(nom=nom.replace(".json", ""), n=n, V=V, NL=NL, haut=haut, ppm=(haut / V - 0.5) * 1e6,
                      orb=(haut - V // 2) // n, reste=(haut - V // 2) % n, polaire=bool(np.all(NL == NL[::-1])),
                      dmax=int(np.abs(NL - NL[::-1]).max()), pole=pole, tri=tri))
assert all(c_["reste"] == 0 for c_ in CERTS)
ligne("| certificat | n | croisements | moitié haute | écart | en orbites de n | symétrie polaire (N_l = N_(n−l)) |")
ligne("|---|---:|---:|---:|---:|---:|---|")
for c_ in CERTS:
    ligne(f"| {c_['nom']} | {c_['n']} | {ent(c_['V'])} | {ent(c_['haut'])} | {fr(c_['ppm'], '{:+.0f}')} ppm |"
          f" {fr(c_['orb'], '{:+d}')} | {'oui' if c_['polaire'] else 'non (écart max ' + ent(c_['dmax']) + ')'} |")
C19 = [c_ for c_ in CERTS if c_["n"] == 19]
SIG19 = math.sqrt(np.mean([c_["orb"] ** 2 for c_ in C19]))
P0 = math.erf(0.5 / (SIG19 * R2))
P0_12 = 1 - (1 - P0) ** len(C19)
EXACT = [c_ for c_ in C19 if c_["orb"] == 0]
ligne(f"\n- Moitié exacte : {', '.join(c_['nom'] for c_ in EXACT)} met {ent(EXACT[0]['haut'])} croisements de chaque côté"
      f" (2¹⁸ − 1 = 19 × {ent((2 ** 18 - 1) // 19)} : Fermat rend l'égalité possible en orbites entières)."
      if EXACT else "\n- Aucune moitié exacte.")
ligne(f"- Les 12 Venn à 19 courbes s'écartent de la moitié de ±{fr(SIG19, '{:.1f}')} orbites (écart quadratique)."
      f" Pour un tirage normal de cette largeur, la probabilité de tomber pile sur 0 est {fr(100 * P0, '{:.1f}')} %, et"
      f" celle qu'au moins un des 12 y tombe, {fr(100 * P0_12, '{:.0f}')} %.")
ligne(f"- Chaque certificat a exactement n croisements autour de chacun des deux pôles (∅ et tout) : "
      f"{'vrai' if all(c_['pole'] == 2 * c_['n'] for c_ in CERTS) else 'faux'} pour les 18. L'écart à la moitié est"
      f" toujours un nombre entier d'orbites : 2^(n−1) − 1 est divisible par n (Fermat).\n")

S17 = next(c_ for c_ in CERTS if c_["nom"] == "venn17-local-c3-s2")
NL17 = S17["NL"].astype(float)
CUM17 = np.cumsum(NL17[::-1])[::-1]
RHO17 = np.r_[np.sqrt(CUM17 / CUM17[0]), 0.0]


# ===========================================================================
# 3. La sphère et les deux miroirs
# ===========================================================================
ligne("## 3. La sphère et les deux miroirs\n")
CB = [comb(17, l_) for l_ in range(1, 17)]
CUMB = [sum(CB[l_ - 1:]) for l_ in range(1, 17)]
VB = CUMB[0]
miroir_exact = all(Fraction(CUMB[l_ - 1], VB) + Fraction(CUMB[17 - l_], VB) == 1 for l_ in range(2, 17))
stereo = []
for l_ in range(2, 17):
    a_, b_ = CUMB[l_ - 1] / VB, CUMB[17 - l_] / VB
    rs1 = math.sqrt(a_ / (1 - a_)) / R2
    rs2 = math.sqrt(b_ / (1 - b_)) / R2
    stereo.append(rs1 * rs2)
dev17 = max(abs(CUM17[l_ - 1] / CUM17[0] + CUM17[17 - l_] / CUM17[0] - 1) for l_ in range(2, 17))
ligne("- Euler sur la sphère : croisements = régions − 2 = 2ⁿ − 2 (χ = 2). La rotation fixe exactement deux régions,"
      " les pôles ∅ et tout : le nombre de Lefschetz d'une rotation de la sphère vaut χ = 2.")
ligne(f"- Lambert (aire conservée) : un point à l'angle θ du pôle va au rayon 2 sin(θ/2), sa corde depuis le pôle."
      f" L'équateur va à la corde √2 = {fr(R2, '{:.6f}')}, dans un disque de rayon 2 : rapport 1/√2. Archimède : la zone"
      f" entre deux plans a l'aire 2πR·h.")
ligne(f"- Miroir d'aire (le complément, en dessin à aire égale) : ρ_l² + ρ_(18−l)² = 1 pour la binomiale :"
      f" {'exact' if miroir_exact else 'faux'} (fractions exactes, l = 2 … 16). Pour le certificat de l'image, l'écart"
      f" maximal est {fr(dev17 * 1e6, '{:.0f}')} ppm.")
ligne(f"- Miroir conforme (le même complément, en projection stéréographique, équateur à R/√2) : r·r′ = R²/2, de"
      f" {fr(min(stereo), '{:.12f}')} à {fr(max(stereo), '{:.12f}')} pour la binomiale. Les deux foyers de la partie XVII"
      f" sont jumeaux : (1 − 1/√2)(1 + 1/√2) = {fr((1 - 1 / R2) * (1 + 1 / R2), '{:.12f}')}.\n")


# ===========================================================================
# 4. Les diaphragmes
# ===========================================================================
ligne("## 4. Les diaphragmes\n")
Cbin = np.array(CUMB, float)
ligne("| cran j | rayon 2^(−j/2) | f/… | part 2⁻ʲ | niveau (certificat) | niveau (binomiale) |")
ligne("|---:|---:|---:|---:|---:|---:|")
NIV_CRAN = []
for j in range(14):
    f_ = 2.0 ** -j
    lv = float(np.interp(-math.log(f_), -np.log(CUM17 / CUM17[0]), np.arange(1, 17)))
    lb = float(np.interp(-math.log(f_), -np.log(Cbin / Cbin[0]), np.arange(1, 17)))
    NIV_CRAN.append((j, lv, lb))
    ligne(f"| {j} | {fr(2 ** (-j / 2), '{:.4f}')} | f/{F_NOM[j]} | {fr(f_, '{:.6f}')} | {fr(lv, '{:.3f}')} | {fr(lb, '{:.3f}')} |")
ligne(f"\n- Du bord à l'orbite centrale (17 croisements, 1/7 710 de l'aire) : log₂ 7 710 = {fr(math.log2(7710), '{:.3f}')}"
      f" crans, soit un diaphragme fermé de f/1 à f/{fr(math.sqrt(7710), '{:.1f}')}.")
ligne("- Une courbe de plus double les croisements : il faut ouvrir d'un cran (f/N → f/(N/√2)) pour les résoudre.")


def lentille(d, r1, r2):
    """Aire commune de deux disques de rayons r1 et r2 dont les centres sont à la distance d (partie I)."""
    if r1 <= 0 or r2 <= 0 or d >= r1 + r2:
        return 0.0
    if d <= abs(r1 - r2):
        return math.pi * min(r1, r2) ** 2
    a1 = r1 * r1 * math.acos((d * d + r1 * r1 - r2 * r2) / (2 * d * r1))
    a2 = r2 * r2 * math.acos((d * d + r2 * r2 - r1 * r1) / (2 * d * r2))
    return a1 + a2 - 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))


CHEVRES = [("au centre, corde R/√2", 0.0, 1 / R2), ("point orange (partie XVII)", 1 - 1 / R2, 1 / R2),
           ("Ullisch, piquet sur le bord", 1.0, ULL)]
BROUTE = {}
ligne("\n| chèvre | part des croisements broutés | niveau moyen brouté | part des niveaux ≥ 9 dans ce qu'elle broute |")
ligne("|---|---:|---:|---:|")
for nom, d_, k_ in CHEVRES:
    frs = []
    for l_ in range(1, 17):
        ro, ri = RHO17[l_ - 1], RHO17[l_]
        frs.append((lentille(d_, ro, k_) - lentille(d_, ri, k_)) / (math.pi * (ro * ro - ri * ri)))
    frs = np.array(frs)
    g_ = frs * NL17
    BROUTE[nom] = frs
    ligne(f"| {nom} | {fr(g_.sum() / NL17.sum(), '{:.6f}')} | {fr((np.arange(1, 17) * g_).sum() / g_.sum(), '{:.3f}')} |"
          f" {fr(g_[8:].sum() / g_.sum(), '{:.4f}')} |")
PHI_U = math.degrees(math.acos(1 - ULL ** 2 / 2))
ligne(f"\n- La chèvre d'Ullisch broute {fr(100 * BROUTE[CHEVRES[2][0]][0], '{:.2f}')} % du niveau 1 : la limite exacte est"
      f" 2 × {fr(PHI_U, '{:.2f}')}° / 360° = {fr(PHI_U / 180, '{:.5f}')} (l'arc de la partie XX, la corde de Ptolémée de la"
      f" partie X : cos φ = 1 − k²/2).\n")
ligne("**Niven : les cercles inscrit et circonscrit d'un polygone régulier, en crans** (−2·log₂ cos(π/N)) :\n")
NIVEN = [(N, -2 * math.log2(math.cos(math.pi / N))) for N in range(3, 25)]
ligne("| N | " + " | ".join(str(N) for N, _ in NIVEN) + " |")
ligne("|---|" + "---:|" * len(NIVEN))
ligne("| crans | " + " | ".join(fr(c_, '{:.3f}') for _, c_ in NIVEN) + " |")
ENTIERS = [N for N, c_ in NIVEN if abs(c_ - round(c_)) < 1e-12]
ligne(f"\n- Nombre entier de crans : N = {', '.join(map(str, ENTIERS))} seulement (2 crans pour le triangle, 1 pour le"
      f" carré). Niven : si cos(2π/N) est rationnel, il vaut 0, ±1/2 ou ±1.\n")


# ===========================================================================
# 5. La figure de diffraction
# ===========================================================================
ligne("## 5. La figure de diffraction de l'image\n")
IL = np.clip(P_["L"] - LbP, 0, None)
cF = HAUT // 2
KX, KY = (XX - cF) / LARG, (YY - cF) / HAUT
KK = np.hypot(KX, KY)
AK = np.mod(np.arctan2(KY, KX), 2 * np.pi)


def spectre(Z):
    return np.abs(np.fft.fftshift(np.fft.fft2(Z))) ** 2


def rayons(Pw, a=0.08, b=0.2):
    m_ = (KK > a) & (KK < b)
    nb = 2040
    ib = (AK[m_] / (2 * np.pi) * nb).astype(int) % nb
    prof = np.bincount(ib, np.log(Pw[m_] + 1), nb) / np.maximum(np.bincount(ib, None, nb), 1)
    k_ = np.exp(-0.5 * (np.arange(-6, 7) / 2.0) ** 2)
    pr = np.convolve(np.r_[prof[-6:], prof, prof[:6]], k_ / k_.sum(), "same")[6:-6]
    pk, _ = find_peaks(pr, prominence=0.15)
    return pk / nb * 360


def profil_harmoniques(th, w, mmax=80, nb=8192):
    prof = np.bincount((np.mod(th, 2 * np.pi) / (2 * np.pi) * nb).astype(int) % nb, w, nb)
    tb = (np.arange(nb) + 0.5) / nb * 2 * np.pi
    return np.array([abs((prof * np.exp(-1j * k * tb)).sum()) / prof.sum() for k in range(1, mmax + 1)])


def harmoniques(Pw, a, b, mmax=80):
    m_ = (KK > a) & (KK < b)
    return profil_harmoniques(AK[m_], Pw[m_], mmax)


PS = spectre(IL)
ANG = rayons(PS)
PAS17 = 180 / 17
RES = np.mod(ANG, PAS17)
# sommets du contour (les 17 coins épinglés) et la famille prévue pour ses aigrettes
RM = MP["RMAX"]
pk_, _ = find_peaks(np.r_[RM, RM[:60]], distance=150)
pk_ = np.unique(pk_ % 3600)
ang_s = (pk_ / 3600 * 360 - 180) % 360
PSI0 = math.degrees(np.angle(np.mean(np.exp(1j * np.radians(ang_s) * 17)))) / 17 % (360 / 17)
RES_CONTOUR = PSI0 % PAS17


def ecart_res(r, ref):
    return np.abs((r - ref + PAS17 / 2) % PAS17 - PAS17 / 2)


FAM_C = ANG[ecart_res(RES, RES_CONTOUR) < 1.5]
FAM_I = ANG[ecart_res(RES, RES_CONTOUR) >= 1.5]
RES_I = math.degrees(np.angle(np.mean(np.exp(1j * np.radians(np.mod(FAM_I, PAS17)) * 34)))) / 34 % PAS17
RHOP = np.hypot(XX - C_SYM[0], YY - C_SYM[1]) / np.maximum(
    np.interp((np.arctan2(YY - C_SYM[1], XX - C_SYM[0]) + np.pi) / (2 * np.pi) * 3600, np.arange(3600), RM), 1.0)
ANG_MASQUE = rayons(spectre((RHOP < 1).astype(float)))
fen = np.clip((0.7 - RHOP) / 0.1, 0, 1)
ANG_COEUR = rayons(spectre(IL * (0.5 - 0.5 * np.cos(np.pi * fen))))
ok_m = np.mean(ecart_res(np.mod(ANG_MASQUE, PAS17), RES_CONTOUR) < 1.5)
ok_c = np.mean(ecart_res(np.mod(ANG_COEUR, PAS17), RES_I) < 1.5)
ligne(f"- {len(ANG)} aigrettes entre 0,08 et 0,2 cycle par pixel : {len(FAM_C)} dans la famille du contour (résidu"
      f" {fr(RES_CONTOUR, '{:.2f}')}° modulo 180°/17, prévu par les 17 coins), {len(FAM_I)} dans une seconde famille"
      f" (résidu {fr(RES_I, '{:.2f}')}°), tournée de {fr(ecart_res(RES_I, RES_CONTOUR), '{:.2f}')}°.")
ligne(f"- Le contour seul (le masque du 17-gone) donne {len(ANG_MASQUE)} aigrettes, dont {fr(100 * ok_m, '{:.0f}')} %"
      f" dans la famille du contour. Le cœur seul (ρ < 0,6) en donne {len(ANG_COEUR)}, dont {fr(100 * ok_c, '{:.0f}')} %"
      f" dans la seconde famille : elle vient de l'intérieur.")
ligne("\n| anneau de fréquences (cycle/px) | harmoniques angulaires dominantes du spectre |")
ligne("|---|---|")
HARM_SP = {}
for a, b in ((0.01, 0.03), (0.03, 0.08), (0.08, 0.2), (0.2, 0.25), (0.25, 0.45)):
    h_ = harmoniques(PS, a, b)
    HARM_SP[(a, b)] = h_
    top = np.argsort(h_)[::-1][:5] + 1
    ligne(f"| {fr(a, '{:.2f}')} – {fr(b, '{:.2f}')} | " + ", ".join(f"{int(k)} ({fr(h_[k - 1], '{:.3f}')})" for k in top) + " |")
ENC_IN = ENCRE_L & (RHOP < 0.98)
THE = np.arctan2(YY[ENC_IN] - C_SYM[1], XX[ENC_IN] - C_SYM[0])
HARM_ENC = profil_harmoniques(THE, np.ones(THE.size))
BRUIT_E = float(np.max([HARM_ENC[k - 1] for k in range(1, 81) if k % 17]))
ligne(f"\n- Harmoniques angulaires de l'encre, vue du centre de symétrie : 17 ({fr(HARM_ENC[16], '{:.4f}')}), 34"
      f" ({fr(HARM_ENC[33], '{:.4f}')}), 51 ({fr(HARM_ENC[50], '{:.4f}')}), 68 ({fr(HARM_ENC[67], '{:.4f}')}) ; le plus"
      f" grand des autres : {fr(BRUIT_E, '{:.4f}')}. Le spectre, lui, ne garde que les multiples de 34 (Friedel :"
      f" |F(k)| = |F(−k)|).\n")
LOGP = np.log10(PS[cF - 400:cF + 400, cF - 400:cF + 400] + 1)
del PS


# ===========================================================================
# 6. Au plus près du centre
# ===========================================================================
ligne("## 6. Au plus près du centre\n")


def drizzle(img, c, h=48, sc=4, goutte=0.5):
    """Empile les 17 copies tournées sur une grille sc fois plus fine (gouttes de goutte px de côté)."""
    n = 2 * h * sc
    acc = np.zeros(n * n)
    cnt = np.zeros(n * n)
    hs = int(h * 1.45) + 3
    y0, x0 = int(c[1]) - hs, int(c[0]) - hs
    ys, xs = np.mgrid[y0:y0 + 2 * hs + 1, x0:x0 + 2 * hs + 1]
    v = img[ys, xs].ravel()
    px, py = xs.ravel() - c[0], ys.ravel() - c[1]
    off = (np.arange(int(goutte * sc)) - (int(goutte * sc) - 1) / 2) / sc
    for k in range(17):
        a = -2 * np.pi * k / 17
        qx, qy = px * np.cos(a) - py * np.sin(a), px * np.sin(a) + py * np.cos(a)
        for ox in off:
            for oy in off:
                ix = np.floor((qx + ox + h) * sc).astype(int)
                iy = np.floor((qy + oy + h) * sc).astype(int)
                ok = (ix >= 0) & (ix < n) & (iy >= 0) & (iy < n)
                acc += np.bincount(iy[ok] * n + ix[ok], v[ok], n * n)
                cnt += np.bincount(iy[ok] * n + ix[ok], None, n * n)
    acc, cnt = acc.reshape(n, n), cnt.reshape(n, n)
    acc_s, cnt_s = ndimage.gaussian_filter(acc, 0.7), ndimage.gaussian_filter(cnt, 0.7)
    return np.where(cnt > 0, acc / np.maximum(cnt, 1), acc_s / np.maximum(cnt_s, 1e-9)), cnt


def incoherence(img, c, h=80, sc=4, r0=6, r1=80):
    """Part de la variance que les 17 copies ne partagent pas (0 : alignement parfait ; 1 : hasard)."""
    n = 2 * h * sc
    acc, acc2, cnt = np.zeros(n * n), np.zeros(n * n), np.zeros(n * n)
    y0, x0 = int(c[1]) - h - 3, int(c[0]) - h - 3
    ys, xs = np.mgrid[y0:y0 + 2 * h + 7, x0:x0 + 2 * h + 7]
    v = img[ys, xs].ravel()
    px, py = xs.ravel() - c[0], ys.ravel() - c[1]
    for k in range(17):
        a = -2 * np.pi * k / 17
        qx, qy = px * np.cos(a) - py * np.sin(a), px * np.sin(a) + py * np.cos(a)
        rq = np.hypot(qx, qy)
        ix = np.floor((qx + h) * sc).astype(int)
        iy = np.floor((qy + h) * sc).astype(int)
        ok = (ix >= 0) & (ix < n) & (iy >= 0) & (iy < n) & (rq > r0) & (rq < r1)
        idx = iy[ok] * n + ix[ok]
        acc += np.bincount(idx, v[ok], n * n)
        acc2 += np.bincount(idx, v[ok] ** 2, n * n)
        cnt += np.bincount(idx, None, n * n)
    sel = cnt >= 2
    moy = acc[sel] / cnt[sel]
    var_in = (acc2[sel] / cnt[sel] - moy ** 2) * cnt[sel] / (cnt[sel] - 1)
    tout = acc.sum() / cnt.sum()
    return float(var_in.mean() / (acc2.sum() / cnt.sum() - tout ** 2))


DIR = np.array([BARY[3][1] - C_SYM[0], BARY[3][2] - C_SYM[1]])
DIR /= np.linalg.norm(DIR)
PERP = np.array([-DIR[1], DIR[0]])
DECALS = [0, 0.125, 0.25, 0.5, 1, 1.5, 2, 3, 4, 8, BARY[3][3]]
INCOH = [(d_, incoherence(IL, (C_SYM[0] + d_ * DIR[0], C_SYM[1] + d_ * DIR[1]))) for d_ in DECALS]
INCOH_P = [(d_, incoherence(IL, (C_SYM[0] + d_ * PERP[0], C_SYM[1] + d_ * PERP[1]))) for d_ in (0.5, 1, 2)]
ligne("**Empiler les 17 copies tournées** (r de 6 à 80 px) : part de la variance que les copies ne partagent pas.\n")
ligne("| décalage du centre d'empilement | " + " | ".join(fr(d_, '{:g}') + " px" for d_, _ in INCOH) + " |")
ligne("|---|" + "---:|" * len(INCOH))
ligne("| incohérence | " + " | ".join(fr(100 * v_, '{:.1f}') + " %" for _, v_ in INCOH) + " |")
ligne("\n- Dans la direction perpendiculaire : " + " ; ".join(f"{fr(d_, '{:g}')} px : {fr(100 * v_, '{:.1f}')} %"
                                                            for d_, v_ in INCOH_P) + ".")
DRZ, DRZ_N = drizzle(IL, C_SYM)
DRZ_BIAIS, _ = drizzle(IL, C_ESSAI)
INCOH_ESSAI = incoherence(IL, C_ESSAI)
ligne(f"- Autour de mon premier centre ({fr(D_ESSAI, '{:.2f}')} px du bon) : incohérence {fr(100 * INCOH_ESSAI, '{:.1f}')} %.")
CRU = IL[int(round(C_SYM[1])) - 48:int(round(C_SYM[1])) + 48, int(round(C_SYM[0])) - 48:int(round(C_SYM[0])) + 48]
ligne(f"- Grille 4 fois plus fine (0,25 px) : {fr(DRZ_N.mean(), '{:.1f}')} échantillons par case en moyenne (17 copies,"
      f" gouttes de 0,5 px).\n")

# la défocalisation : le contraste s'inverse là où 2 J₁(x)/x < 0
B_DEF = 4.0
hh = 256
sub_ = IL[int(C_SYM[1]) - hh:int(C_SYM[1]) + hh, int(C_SYM[0]) - hh:int(C_SYM[0]) + hh]
ocx, ocy = C_SYM[0] - (int(C_SYM[0]) - hh), C_SYM[1] - (int(C_SYM[1]) - hh)
nk = int(math.ceil(B_DEF)) + 2
yf, xf = (np.mgrid[0:(2 * nk + 1) * 8, 0:(2 * nk + 1) * 8] + 0.5) / 8 - nk - 0.5
KER = (np.hypot(xf, yf) <= B_DEF).astype(float).reshape(2 * nk + 1, 8, 2 * nk + 1, 8).mean((1, 3))
FLOU = ndimage.convolve(sub_, KER / KER.sum(), mode="nearest")


def harmo_cercle(img, r, mm):
    nn = max(256, int(8 * math.pi * r))
    a = np.linspace(0, 2 * np.pi, nn, endpoint=False)
    v = ndimage.map_coordinates(img, [ocy + r * np.sin(a), ocx + r * np.cos(a)], order=1)
    return (v * np.exp(-1j * mm * a)).mean()


RS = np.arange(6, 91, 1.0)
A0 = np.array([harmo_cercle(sub_, r, 17) for r in RS])
A1 = np.array([harmo_cercle(FLOU, r, 17) for r in RS])
GAIN = np.array([np.real((A1[i0:i0 + 5] * np.conj(A0[i0:i0 + 5])).sum()) / (np.abs(A0[i0:i0 + 5]) ** 2).sum()
                 for i0 in np.clip(np.arange(len(RS)) - 2, 0, len(RS) - 5)])
FIABLE = (np.abs(A0) > 0.2 * np.median(np.abs(A0[RS >= 15]))) & (RS >= 15)
XJ = B_DEF * 17 / RS
GAIN_TH = 2 * j1(XJ) / XJ
Z1 = jn_zeros(1, 2)
ACC_SIGNE = float(np.mean(np.sign(GAIN[FIABLE]) == np.sign(GAIN_TH[FIABLE])))
INV = RS[(GAIN < 0) & FIABLE]
ligne(f"**Défocalisation** (disque de rayon {fr(B_DEF, '{:g}')} px, harmonique 17) : inversion prévue entre"
      f" {fr(B_DEF * 17 / Z1[1], '{:.1f}')} et {fr(B_DEF * 17 / Z1[0], '{:.1f}')} px (zéros de J₁) ; mesurée de"
      f" {fr(INV.min(), '{:.0f}')} à {fr(INV.max(), '{:.0f}')} px. Signes en accord avec 2 J₁(x)/x sur"
      f" {fr(100 * ACC_SIGNE, '{:.0f}')} % des rayons fiables au-delà du trou ({int(FIABLE.sum())} rayons de 15 à 90 px ;"
      f" on écarte ceux où l'harmonique 17 est presque nulle).\n")

# les limites de granularité : le centre contre le reste
ligne("**Largeur d'image nécessaire** (pixels) : le reste à 2 px par côté de croisement, le centre à 2 px d'arc entre"
      " les n croisements de l'orbite centrale ; repositionner les grains divise ces largeurs par 2 au mieux.\n")
GRAN = []
for n in range(11, 26):
    Vn = 2 ** n - 2
    wb = 4 * math.sqrt(Vn / math.pi)
    wc = 2 / math.pi * math.sqrt(n * Vn)
    GRAN.append((n, wb, wc))
ligne("| n | " + " | ".join(str(n) for n, _, _ in GRAN) + " |")
ligne("|---|" + "---:|" * len(GRAN))
ligne("| reste | " + " | ".join(ent(round(wb)) for _, wb, _ in GRAN) + " |")
ligne("| centre | " + " | ".join(ent(round(wc)) for _, _, wc in GRAN) + " |")


def n_max(W, fact=1.0, centre=True):
    lo, hi = 3.0, 60.0
    for _ in range(80):
        mid = (lo + hi) / 2
        Vn = 2 ** mid - 2
        w = (2 / math.pi * math.sqrt(mid * Vn) if centre else 4 * math.sqrt(Vn / math.pi)) / fact
        lo, hi = (mid, hi) if w <= W else (lo, mid)
    return lo


NM = {(W, f_, c_): n_max(W, f_, c_) for W in (2000, 8000) for f_ in (1.0, 2.0) for c_ in (True, False)}
ligne(f"\n- À 2 000 px : le centre résout jusqu'à n = {fr(NM[(2000, 1.0, True)], '{:.2f}')} courbes, le reste jusqu'à"
      f" {fr(NM[(2000, 1.0, False)], '{:.2f}')} ; en repositionnant les grains, {fr(NM[(2000, 2.0, True)], '{:.2f}')} et"
      f" {fr(NM[(2000, 2.0, False)], '{:.2f}')}. À 8 000 px : {fr(NM[(8000, 1.0, True)], '{:.2f}')} et"
      f" {fr(NM[(8000, 1.0, False)], '{:.2f}')}.")
R_CIBLE = MP["Rc"] * math.sqrt(17 / V17)
ligne(f"- L'orbite centrale de l'image : cible {fr(R_CIBLE, '{:.1f}')} px, trou mesuré {fr(R_TROU, '{:.1f}')} px, soit"
      f" {fr(2 * math.pi * R_TROU / 17, '{:.2f}')} px d'arc entre deux croisements (le dessin élargit le centre).\n")


# ===========================================================================
# 7. Le banc d'essai des tests du hasard
# ===========================================================================
ligne("## 7. Le banc d'essai des tests du hasard\n")
TOL_TXT = open(os.path.join(ICI, "..", "resultats", "venn_ppm.md"), encoding="utf-8").read()
NUL = []
for m_ in re.finditer(r"\| [0-9,]+ % \(([0-9  ]+) ppm\) \| (\d+) \| ([0-9,]+) \|", TOL_TXT):
    NUL.append((float(m_.group(1).replace(" ", "").replace(" ", "")) * 1e-6, float(m_.group(3).replace(",", "."))))
NUL.sort()
LAMBDA = (NUL[-1][1] / NUL[-1][0]) if NUL else 410.0
ref_ = [v_ / t_ for t_, v_ in NUL if t_ <= 0.01]
LAMBDA = float(np.median(ref_)) if ref_ else LAMBDA
NCOMP = 1240


def ecart_rel(a, b):
    return abs(float(a / b - 1))


lum17 = mp.mpf(17) / 2 * mp.sin(2 * mp.pi / 17) / mp.pi
CAS = [
    ("E1", "moitié des régions : Σ_(k ≥ 9) C(17, k) = 2¹⁶", "exact", mp.mpf(sum(comb(17, k) for k in range(9, 18))) / 2 ** 17, mp.mpf(1) / 2),
    ("E2", "2⁻¹⁷·10¹⁷ = 5¹⁷", "exact", mp.mpf(10) ** 17 / mp.mpf(2) ** 17, mp.mpf(5) ** 17),
    ("E3", "la corde d'Ullisch est la corde de son arc : 2 arcsin(k/2) = arccos(1 − k²/2)", "exact",
     2 * mp.asin(mp.mpf(ULL) / 2), mp.acos(1 - mp.mpf(ULL) ** 2 / 2)),
    ("E4", "disque uniforme : ⟨r²⟩ = R²/2", "exact", mp.quad(lambda r: r ** 3, [0, 1]) * 2, mp.mpf(1) / 2),
    ("S1", "34·tan(π/34) ≈ π (polygone → cercle)", "structure", 34 * mp.tan(mp.pi / 34), mp.pi),
    ("S2", "lumière du 17-gone ≈ 1 − 2π²/(3·17²)", "structure", lum17, 1 - 2 * mp.pi ** 2 / (3 * 17 ** 2)),
    ("S3", "croisements des niveaux ≥ 9 ≈ ½ (certificat de l'image)", "structure", mp.mpf(S17["haut"]) / S17["V"], mp.mpf(1) / 2),
    ("S4", "encre dans le contour réduit de 1/√2 ≈ ½ (image)", "structure", mp.mpf(MP["contour"]), mp.mpf(1) / 2),
    ("C1", "(128/125) × lumière du 17-gone ≈ 1", "hasard", mp.mpf(128) / 125 * lum17, mp.mpf(1)),
    ("C2", "part des triangles ≈ ombres égales de l'octaèdre (35,10 %)", "hasard", mp.mpf(S17["tri"]),
     2 / mp.pi * (3 * mp.acos(mp.mpf(1) / 3) - mp.pi)),
]
# variation du paramètre : chaque relation suit-elle une loi quand on change n, N, k ?


def varie(code):
    if code == "E1":
        return all(sum(comb(n, k) for k in range((n + 1) // 2, n + 1)) == 2 ** (n - 1) for n in range(3, 40, 2)), \
            "vrai pour tout n impair (3 à 39)"
    if code == "E2":
        return all(10 ** j == 2 ** j * 5 ** j for j in range(1, 60)), "vrai pour tout j (1 à 59)"
    if code == "E3":
        ks = [mp.mpf(x) / 10 for x in range(1, 20)]
        return all(abs(2 * mp.asin(k / 2) - mp.acos(1 - k * k / 2)) < mp.mpf(10) ** -50 for k in ks), \
            "vrai pour toute corde k (19 valeurs)"
    if code == "E4":
        return True, "vrai pour tout R (intégrale exacte)"
    if code == "S1":
        lois = [float((2 * N * mp.tan(mp.pi / (2 * N)) - mp.pi) * N ** 2) for N in (17, 170, 1700)]
        return abs(lois[-1] - float(mp.pi ** 3 / 12)) < 1e-4, f"écart × N² → π³/12 = {fr(float(mp.pi ** 3 / 12), '{:.4f}')}" \
            f" ({', '.join(fr(x, '{:.4f}') for x in lois)})"
    if code == "S2":
        lois = [float((N / 2 * mp.sin(2 * mp.pi / N) / mp.pi - 1 + 2 * mp.pi ** 2 / (3 * N ** 2)) * N ** 4)
                for N in (17, 170, 1700)]
        return abs(lois[-1] - float(2 * mp.pi ** 4 / 15)) < 1e-3, f"écart × N⁴ → 2π⁴/15 = {fr(float(2 * mp.pi ** 4 / 15), '{:.3f}')}"
    if code == "S3":
        dv = [c_["ppm"] for c_ in CERTS if c_["n"] >= 13]
        return abs(np.mean(dv)) < 3 * np.std(dv) / math.sqrt(len(dv)), \
            f"17 certificats : moyenne {fr(np.mean(dv), '{:+.0f}')} ppm, dispersion {fr(np.std(dv), '{:.0f}')} ppm"
    if code == "S4":
        return abs(MR["contour"] - 0.5) > 0.1, f"tient pour le dessin à aire égale, pas pour la rose ({fr(100 * MR['contour'], '{:.1f}')} %)"
    if code == "C1":
        Ns = mp.findroot(lambda N: mp.mpf(128) / 125 * N / 2 * mp.sin(2 * mp.pi / N) / mp.pi - 1, 17)
        return False, f"ne vaut 1 qu'en N = {fr(float(Ns), '{:.2f}')}, un passage par zéro sans loi"
    if code == "C2":
        tri = [100 * c_["tri"] for c_ in CERTS if c_["tri"] is not None]
        return False, f"11, 13, 17, 19 courbes : {', '.join(fr(t_, '{:.1f}') for t_ in tri)} % ; rien ne suit 35,10 %"
    return None, ""


BANC = []
for code, nom, verite, a, b in CAS:
    d = ecart_rel(a, b)
    p1 = min(1.0, 2 * math.log1p(d) / math.log(1e4)) if d > 0 else 0.0
    p2 = min(1.0, NCOMP * p1)
    p3 = 1 - math.exp(-LAMBDA * d)
    bits = -math.log2(max(d, 2.0 ** -166)) - math.log2(NCOMP)
    exact50 = abs(a - b) < mp.mpf(10) ** -45 if code[0] in "EC" or code in ("S1", "S2") else None
    loi, txt = varie(code)
    BANC.append(dict(code=code, nom=nom, verite=verite, d=d, p1=p1, p2=p2, p3=p3, bits=bits, exact50=exact50,
                     loi=loi, txt=txt))


def verdict(tech, c):
    """True = « pas le hasard », False = « hasard », None = ne s'applique pas."""
    if tech == "T1":
        return c["p1"] < 0.05
    if tech == "T2":
        return c["p2"] < 0.05
    if tech == "T3":
        return c["p3"] < 0.05
    if tech == "T4":
        return None if c["exact50"] is None else bool(c["exact50"]) or None
    if tech == "T5":
        return c["loi"]
    if tech == "T6":
        return c["bits"] > 0


TECHS = [("T1", "p naïve (une comparaison)"), ("T2", "Bonferroni (× 1 240)"), ("T3", "nul brouillé (partie XXIX)"),
         ("T4", "précision poussée (50 chiffres)"), ("T5", "variation du paramètre"), ("T6", "longueur de description")]
ligne(f"- Nul brouillé de la partie XXIX : λ(d) ≈ {fr(LAMBDA, '{:.0f}')}·d paires attendues à la tolérance d (lu dans"
      f" resultats/venn_ppm.md).\n")
ligne("| cas | vérité | écart | " + " | ".join(t_[1] for t_ in TECHS) + " |")
ligne("|---|---|---:|" + "---|" * len(TECHS))
SCORE = {t_[0]: [0, 0] for t_ in TECHS}
for c in BANC:
    cells = []
    for t_, _ in TECHS:
        v_ = verdict(t_, c)
        if v_ is None:
            cells.append("—")
            continue
        juste = (v_ and c["verite"] != "hasard") or (not v_ and c["verite"] == "hasard")
        SCORE[t_][0] += int(juste)
        SCORE[t_][1] += 1
        cells.append(("pas le hasard" if v_ else "hasard") + (" ✓" if juste else " ✗"))
    dtxt = "0" if c["d"] == 0 else (fr(c["d"] * 1e6, '{:.0f}') + " ppm" if c["d"] < 0.1 else fr(100 * c["d"], '{:.1f}') + " %")
    ligne(f"| {c['code']} {c['nom']} | {c['verite']} | {dtxt} | " + " | ".join(cells) + " |")
ligne("\n| technique | justes / jugés |")
ligne("|---|---:|")
for t_, nom in TECHS:
    ligne(f"| {nom} | {SCORE[t_][0]} / {SCORE[t_][1]} |")
ligne("\n**Variation du paramètre, le détail :**\n")
for c in BANC:
    ligne(f"- {c['code']} : {c['txt']}.")

# des paires au hasard : les faux positifs de chaque technique
rng = np.random.default_rng(30)
ALEA = 10 ** rng.uniform(-2, 2, size=(20000, 2))
DA = np.abs(ALEA[:, 0] / ALEA[:, 1] - 1)
FP = {"T1": float(np.mean(2 * np.log1p(DA) / math.log(1e4) < 0.05)),
      "T2": float(np.mean(NCOMP * 2 * np.log1p(DA) / math.log(1e4) < 0.05)),
      "T3": float(np.mean(1 - np.exp(-LAMBDA * DA) < 0.05)),
      "T6": float(np.mean(-np.log2(np.maximum(DA, 2.0 ** -166)) - math.log2(NCOMP) > 0))}
ligne("\n- Sur 20 000 paires tirées au hasard (log-uniformes sur 4 décades), part déclarée « pas le hasard » : "
      + " ; ".join(f"{dict(TECHS)[k]} : {fr(100 * v_, '{:.2f}')} %" for k, v_ in FP.items()) + ".")
ligne(f"- Un réel tombe pile sur une constante donnée, à 50 chiffres, avec une probabilité de l'ordre de 10⁻⁵⁰ ; un"
      f" compte entier dispersé de ±{fr(SIG19, '{:.0f}')} orbites tombe pile sur sa moitié avec {fr(100 * P0, '{:.1f}')} %.")

ligne(f"\n(calculs : {time.time() - T0:.0f} s)")
with open(os.path.join(ICI, "..", "resultats", "centre_venn.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(md) + "\n")
print(f"calculs : {time.time() - T0:.1f} s")
T1_ = time.time()


# ===========================================================================
# Figures
# ===========================================================================
def legende(ax, texte, y=-0.13, largeur=86):
    texte = textwrap.fill(" ".join(texte.split("\n")), largeur)
    ax.text(0.5, y, texte, transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)


BOITE = dict(boxstyle="round,pad=0.35", fc=F.SURF, ec=F.BASE)
COUL_BARY = [F.AQUA, VERT, F.JAUNE, F.ORANGE, ROUGE, VIOLET]
COURT = ["Y (l'œil)", "masque de clarté", "clarté L", "masque RGB (XXIX)", "moyenne RGB", "énergie linéaire"]

# --------------------------- ae1 : le centre et la moitié ---------------------------
fig = plt.figure(figsize=(21.5, 14.8))
gs = fig.add_gridspec(2, 3, wspace=0.32, hspace=0.36)

# a) le centre, pixel par pixel
ax = fig.add_subplot(gs[0, 0])
h_ = 50
cx0, cy0 = int(round(C_SYM[0])), int(round(C_SYM[1]))
ax.imshow(P_["S8"][cy0 - h_:cy0 + h_, cx0 - h_:cx0 + h_], interpolation="nearest",
          extent=(cx0 - h_ - 0.5 - C_SYM[0], cx0 + h_ - 0.5 - C_SYM[0], cy0 + h_ - 0.5 - C_SYM[1], cy0 - h_ - 0.5 - C_SYM[1]))
tt = np.linspace(0, 2 * np.pi, 300)
ax.plot(R_TROU * np.cos(tt), R_TROU * np.sin(tt), color="#ffffff", lw=1.1, ls="--")
ax.plot(R_CIBLE * np.cos(tt), R_CIBLE * np.sin(tt), color="#ffffff", lw=0.9, ls=":")
ax.plot(0, 0, "+", color="#ffffff", ms=16, mew=2.2)
for (nom, bx, by, d_, _), col in zip(BARY, COUL_BARY):
    dx_, dy_ = bx - C_SYM[0], by - C_SYM[1]
    if max(abs(dx_), abs(dy_)) < h_ - 2:
        ax.plot(dx_, dy_, "o", color=col, ms=7, mec="#ffffff", mew=1.0)
    else:
        f_ = (h_ - 4) / max(abs(dx_), abs(dy_))
        ax.annotate("", xy=(dx_ * f_, dy_ * f_), xytext=(dx_ * f_ * 0.8, dy_ * f_ * 0.8),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=2))
ax.set_xlim(-h_, h_)
ax.set_ylim(h_, -h_)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("a)  Le centre de ton image, pixel par pixel")
legende(ax, f"100 × 100 pixels autour du centre de symétrie (+, à {fr(D_IMG, '{:.3f}')} px du centre exact de l'image)."
        f" Tirets : le trou central ({fr(R_TROU, '{:.1f}')} px) ; pointillés : la cible du dessin ({fr(R_CIBLE, '{:.1f}')} px)."
        " Points et flèches : les centres de la lumière du panneau b, mêmes couleurs. Image : Chris Dzoba, dzoba/venn17,"
        " CC BY 4.0.", y=-0.03)

# b) les centres de la lumière
ax = fig.add_subplot(gs[0, 1])
ax.plot(0, 0, "+", color=F.INK, ms=18, mew=2.4, zorder=6)
ax.add_patch(plt.Circle((0, 0), R_TROU, fill=False, ls="--", color=F.MUTED, lw=1))
ax.text(0, -R_TROU - 1.5, "trou central", color=F.MUTED, fontsize=8.6, ha="center")
for (nom, bx, by, d_, _), col, ct in zip(BARY, COUL_BARY, COURT):
    dx_, dy_ = bx - C_SYM[0], by - C_SYM[1]
    ax.plot([0, dx_], [0, dy_], color=col, lw=1.2, alpha=0.6)
    ax.plot(dx_, dy_, "o", color=col, ms=9, mec=F.INK, mew=0.6, zorder=5, label=f"{ct} : {fr(d_, '{:.1f}')} px")
ax.legend(loc="lower left", fontsize=8.6, title="centre de la lumière, pesée par…", title_fontsize=8.6)
# l'anneau des 17 couleurs : longueur = moyenne RGB mesurée
ax_in = ax.inset_axes([0.66, 0.0, 0.34, 0.34])
mo_ = np.array([c_["mo"] for c_ in COUL])
for i, c_ in enumerate(COUL):
    a_ = math.radians(c_["h"])
    ax_in.plot([0, mo_[i] / mo_.max() * math.cos(a_)], [0, mo_[i] / mo_.max() * math.sin(a_)],
               color=np.array(c_["rgb"]) / 255, lw=5, solid_capstyle="butt")
ax_in.add_patch(plt.Circle((0, 0), np.mean(mo_) / mo_.max(), fill=False, ls=":", color=F.MUTED))
ax_in.set_xlim(-1.1, 1.1)
ax_in.set_ylim(-1.1, 1.1)
ax_in.set_aspect("equal")
ax_in.axis("off")
ax_in.set_title("les 17 couleurs\n(longueur : moyenne RGB)", fontsize=8, fontweight="normal", color=F.INK2)
ax.set_xlim(-52, 40)
ax.set_ylim(40, -26)
ax.set_aspect("equal")
ax.set_xlabel("x − centre de symétrie (pixels)")
ax.set_ylabel("y − centre de symétrie (pixels, comme dans l'image)")
ax.set_title("b)  Où est le centre de la lumière ?")
legende(ax, "Même dessin, même centre géométrique ; seul change ce qu'on appelle « lumière ». Les 17 courbes ont des"
        f" couleurs différentes : en moyenne RGB, du simple au double (dipôle de {fr(100 * DIP['mo'], '{:.0f}')} %)."
        " Pesées ainsi, elles déplacent le barycentre comme les deux couleurs d'une étoile double déplacent son"
        " photocentre (Wielen, 1996). La luminance de l'œil (Y) reste au centre à 0,6 px près.", y=-0.13)

# c) la pression, avec le contour réduit de 1/√2 et les crans
ax = fig.add_subplot(gs[0, 2])
pas = 2
Rv = MP["Rc"]
ax.imshow(P_["S8"][::pas, ::pas], extent=(-C_SYM[0] / Rv, (LARG - C_SYM[0]) / Rv, (HAUT - C_SYM[1]) / Rv, -C_SYM[1] / Rv))
thb = (np.arange(3600) + 0.5) / 3600 * 2 * np.pi - np.pi
RMs = ndimage.uniform_filter1d(MP["RMAX"], 9, mode="wrap") / Rv
for j in range(1, 7):
    f_ = 2 ** (-j / 2)
    ax.plot(f_ * RMs * np.cos(thb), f_ * RMs * np.sin(thb), color="#ffffff", lw=1.6 if j == 1 else 0.7,
            ls="--" if j == 1 else ":")
ax.text(0, -0.79, f"contour réduit de 1/√2 : {fr(100 * MP['contour'], '{:.1f}')} % de l'encre", color="#ffffff",
        ha="center", fontsize=9)
ax.set_xlim(-1.04, 1.04)
ax.set_ylim(1.04, -1.04)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("c)  La moitié du disque fait la moitié du Venn")
legende(ax, "Le rendu « pression », vu du centre de symétrie. Tirets : le contour réduit de 1/√2, qui enferme la moitié"
        " de l'aire. Pointillés : les crans suivants, 1/2, 1/(2√2), … de rayon ; chacun garde la moitié de l'encre du"
        " précédent (panneau e).", y=-0.03)

# d) la rose
ax = fig.add_subplot(gs[1, 0])
Rr = MR["Rc"]
ax.imshow(IM_ROSE, extent=(-C_ROSE[0] / Rr, (LARG - C_ROSE[0]) / Rr, (HAUT - C_ROSE[1]) / Rr, -C_ROSE[1] / Rr))
RMr = ndimage.uniform_filter1d(MR["RMAX"], 9, mode="wrap") / Rr
ax.plot(RMr / R2 * np.cos(thb), RMr / R2 * np.sin(thb), color="#ffffff", lw=1.6, ls="--")
ax.text(0, 0.12, f"{fr(100 * MR['contour'], '{:.1f}')} % de l'encre\ndans le contour réduit", color="#ffffff",
        ha="center", fontsize=9)
ax.set_xlim(-1.04, 1.04)
ax.set_ylim(1.04, -1.04)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("d)  Le même Venn, dessiné en « rose »")
legende(ax, "L'autre rendu du dépôt (le dessin de Tutte, harmonique : chaque croisement au barycentre de ses voisins)."
        " Les croisements s'y serrent dans un anneau, et la région centrale est immense : le contour réduit de 1/√2 n'a"
        " plus que le quart de l'encre. La moitié du disque ne fait la moitié du Venn que dans un dessin à aire égale."
        " Image : Chris Dzoba, CC BY 4.0.", y=-0.03)

# e) l'encre en fonction de l'aire, et les crans
ax = fig.add_subplot(gs[1, 1])
for m_, col, lab in ((MP, F.BLEU, "pression"), (MR, F.ORANGE, "rose")):
    ax.plot(m_["cumul"][0], m_["cumul"][1], color=col, lw=2.2, label=lab)
    ax.plot([2.0 ** -j for j in range(1, 11)], m_["crans"][1:11], "o", color=col, ms=5)
ax.plot([0, 1], [0, 1], color=F.INK, lw=1, ls="--", label="densité uniforme")
ax.axvline(0.5, color=F.MUTED, lw=0.8, ls=":")
ax.axhline(0.5, color=F.MUTED, lw=0.8, ls=":")
ax.set_xlabel("part de l'aire (ρ² : le contour réduit d'un facteur ρ)")
ax.set_ylabel("part de l'encre à l'intérieur")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.legend(loc="lower right", bbox_to_anchor=(0.99, 0.12), fontsize=8.6)
axi = ax.inset_axes([0.07, 0.56, 0.4, 0.38])
js = np.arange(0, 15)
axi.semilogy(js, 2.0 ** -js, color=F.INK, lw=1, ls="--")
axi.semilogy(js, np.maximum(MP["crans"], 1e-7), "o-", color=F.BLEU, ms=3.5, lw=1.2)
axi.semilogy(js[:3], np.maximum(MR["crans"][:3], 1e-7), "o-", color=F.ORANGE, ms=3.5, lw=1.2)
axi.axvline(math.log2(7710), color=F.MUTED, lw=0.8, ls=":")
axi.set_xticks([0, 2, 4, 6, 8, 10, 12, 14])
axi.set_xticklabels(["f/1", "2", "4", "8", "16", "32", "64", "128"], fontsize=7)
axi.tick_params(labelsize=7)
axi.set_title("crans j (f/…) : la part 2⁻ʲ", fontsize=8, fontweight="normal", color=F.INK2)
ax.set_title("e)  L'encre suit l'aire, cran après cran")
legende(ax, "Si la densité est uniforme, la part d'encre dans le contour réduit d'un facteur ρ vaut ρ² : la diagonale. La"
        " pression la suit (points : les crans) ; la rose s'en écarte, puis tombe à zéro dès le troisième cran. En"
        " encart, les crans en échelle de diaphragme : 2⁻ʲ jusqu'au 6ᵉ cran, puis le centre se vide (trou central ;"
        f" pointillés : log₂ 7 710 = {fr(math.log2(7710), '{:.2f}')}, l'orbite centrale).", y=-0.13)

# f) la moitié dans les 18 certificats
ax = fig.add_subplot(gs[1, 2])
noms_c = [c_["nom"].replace("venn19-", "19 ").replace("venn17-", "17 ").replace("best11-s0", "11").replace("v3-13-s0", "13")
          for c_ in CERTS]
vals = np.array([c_["ppm"] for c_ in CERTS])
cols_c = [F.RAMPE[0] if c_["n"] < 17 else (F.BLEU if c_["n"] == 17 else F.RAMPE[4]) for c_ in CERTS]
yv = np.arange(len(CERTS))
ax.axvspan(-BUD_CROIS, BUD_CROIS, color=F.ORANGE, alpha=0.08)
ax.axvspan(-BUD_PIX, BUD_PIX, color=F.ORANGE, alpha=0.12)
ax.barh(yv, np.clip(vals, -5200, 5200), color=cols_c)
for i, c_ in enumerate(CERTS):
    if abs(c_["ppm"]) > 5200:
        ax.text(-5150, i, f"← {fr(c_['ppm'], '{:+.0f}')}", va="center", fontsize=8, color="#ffffff", fontweight="bold")
    if c_["orb"] == 0 and c_["n"] > 11:
        ax.text(150, i, "0 : moitié exacte (262 143 de chaque côté)", va="center", fontsize=8.4, color=ROUGE)
ax.set_yticks(yv)
ax.set_yticklabels(noms_c, fontsize=8)
ax.set_xlim(-5200, 5200)
ax.axvline(0, color=F.INK, lw=0.8)
ax.set_xlabel("écart à la moitié (ppm) : croisements de niveau ≥ (n + 1)/2")
ax.set_ylim(len(CERTS) - 0.4, -1.6)
ax.text(BUD_PIX - 60, -1.05, "pixels\ncertains", fontsize=7.6, color=F.ORANGE, ha="right", va="center")
ax.text(BUD_CROIS - 60, -1.05, "un\ncroisement", fontsize=7.6, color=F.ORANGE, ha="right", va="center")
ax.set_title("f)  La moitié de chaque Venn de Dzoba")
legende(ax, f"Aucun Venn n'est symétrique par le complément (N_l ≠ N_(n−l)), donc aucun ne coupe forcément ses croisements"
        f" en deux. Bandes : ce que l'image peut trancher (±{fr(BUD_PIX, '{:.0f}')} ppm en pixels certains,"
        f" ±{fr(BUD_CROIS, '{:.0f}')} ppm au grain d'un croisement). Un Venn à 19 courbes tombe pile sur la moitié :"
        f" {fr(100 * P0, '{:.1f}')} % de chances pour un tirage, {fr(100 * P0_12, '{:.0f}')} % pour au moins un sur 12.", y=-0.13)
F.sauver(fig, "ae1_centre_moitie.png")

# --------------------------- ae2 : diaphragmes, sphère, chèvres, diffraction ---------------------------
fig = plt.figure(figsize=(21, 14.8))
gs = fig.add_gridspec(2, 3, wspace=0.22, hspace=0.36)

# a) Lambert et Archimède
ax = fig.add_subplot(gs[0, 0])
ax.add_patch(plt.Circle((0, 0), 1, fill=False, color=F.INK, lw=1.6))
ax.plot([-2.3, 2.3], [-1, -1], color=F.MUTED, lw=1)
for l_ in range(2, 17):
    z_ = 1 - 2 * (CUMB[l_ - 1] / VB)          # hauteur de la frontière de niveau, pôle « tout » en bas
    xr = math.sqrt(max(0.0, 1 - z_ * z_))
    ax.plot([-xr, xr], [-z_, -z_], color=F.RAMPE[2] if l_ != 9 else ROUGE, lw=0.8 if l_ != 9 else 2.0, alpha=0.8)
# la corde du pôle à l'équateur, rabattue sur le plan
ax.plot([0, 1], [-1, 0], color=ROUGE, lw=2.2)
t_arc = np.linspace(math.pi / 4, 0, 60)
ax.plot(R2 * np.cos(t_arc), -1 + R2 * np.sin(t_arc), color=ROUGE, lw=1, ls=":")
ax.plot([-R2, R2], [-1, -1], color=ROUGE, lw=3, solid_capstyle="butt")
ax.plot([-2, 2], [-1.04, -1.04], color=F.BLEU, lw=3, solid_capstyle="butt")
ax.text(0.36, -0.36, "corde √2", color=ROUGE, fontsize=9.5, rotation=45, ha="center", va="center")
ax.text(0, -1.22, "disque de demi-aire : rayon √2 = 2/√2", color=ROUGE, ha="center", fontsize=9)
ax.text(0, -1.42, "toute la sphère : rayon 2", color=F.BLEU, ha="center", fontsize=9)
ax.text(0, 1.08, "∅ (dehors)", ha="center", fontsize=9.5)
ax.text(-1.06, -0.93, "tout (le centre)", fontsize=9, ha="right")
ax.text(1.05, 0.05, "équateur = niveau 8,5", color=ROUGE, fontsize=9)
ax.set_xlim(-2.3, 2.6)
ax.set_ylim(-1.6, 1.3)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("a)  Le Venn est une sphère ; R/√2 est son équateur")
legende(ax, "Coupe de la sphère, pôle « tout » en bas. Les traits sont les frontières des niveaux pour la binomiale, aux"
        " hauteurs qui leur donnent leur part d'aire (Archimède : une zone a l'aire 2πR·h). La projection de Lambert pose"
        " chaque point à sa corde depuis le pôle : l'équateur (rouge) tombe à √2 dans un disque de rayon 2, soit R/√2."
        " C'est la corde de la chèvre de dimension infinie (partie XX).", y=-0.03)

# b) les deux miroirs
ax = fig.add_subplot(gs[0, 1])
rr = np.linspace(0.02, 1, 400)
ax.plot(rr, np.sqrt(1 - rr ** 2), color=F.BLEU, lw=2.2, label="miroir d'aire : r² + r′² = R² (Lambert)")
ri = np.linspace(0.3, 1.7, 400)
ax.plot(ri, 1 / (2 * ri), color=F.ORANGE, lw=2.2, label="miroir conforme : r·r′ = R²/2 (stéréographie)")
ax.plot([0, 1.75], [0, 1.75], color=F.MUTED, lw=0.8, ls=":")
ax.plot(1 / R2, 1 / R2, "o", color=ROUGE, ms=9, zorder=6)
ax.annotate("R/√2 : fixe pour les deux", (1 / R2, 1 / R2), xytext=(0.84, 1.05), fontsize=9, color=ROUGE,
            arrowprops=dict(arrowstyle="-", color=ROUGE, lw=0.8))
lp = [(RHO17[l_ - 1], RHO17[17 - l_]) for l_ in range(2, 17)]
ax.plot([a_ for a_, _ in lp], [b_ for _, b_ in lp], "s", color=F.BLEU, ms=4.5, label="niveaux l et 18 − l (certificat)")
d1, d2 = 1 - 1 / R2, 1 + 1 / R2
ax.plot([d1, d2], [d2 * 0 + 1 / (2 * d1), 1 / (2 * d2)], "D", color=VIOLET, ms=7, label="les deux foyers (partie XVII)")
ax.set_xlim(0, 1.75)
ax.set_ylim(0, 1.75)
ax.set_aspect("equal")
ax.set_xlabel("r / R")
ax.set_ylabel("r′ / R : son complément")
ax.legend(loc="upper right", fontsize=8.2)
ax.set_title("b)  Deux miroirs pour la même moitié")
legende(ax, "Le complément (S ↔ tout − S) échange les deux hémisphères. Dans un dessin à aire égale, c'est le miroir d'aire ;"
        " en projection conforme, c'est l'inversion de rayon R/√2 : les jumeaux d·d′ = 1/2 de la partie XVII, la forme de"
        " Newton x·x′ = f² des parties XVII et XVIII, l'inversion qui recolle les deux cartes de la partie XX. Les"
        f" niveaux du certificat s'écartent du miroir d'au plus {fr(dev17 * 1e6, '{:.0f}')} ppm.", y=-0.13)

# c) crans et niveaux
ax = fig.add_subplot(gs[0, 2])
jj = np.array([j for j, _, _ in NIV_CRAN])
ax.plot(jj, [lv for _, lv, _ in NIV_CRAN], "o-", color=F.BLEU, lw=2, ms=6, label="certificat de l'image")
ax.plot(jj, [lb for _, _, lb in NIV_CRAN], "s--", color=F.ORANGE, lw=1.2, ms=4, label="binomiale C(17, l)")
ax.axhline(9, color=ROUGE, lw=0.8, ls=":")
ax.annotate("1ᵉʳ cran : la moitié par le complément\n(niveau 9, exactement)", (1, 9), xytext=(2.2, 6.2), fontsize=9,
            color=ROUGE, arrowprops=dict(arrowstyle="-", color=ROUGE, lw=0.8))
ax.set_xticks(jj)
ax.set_xticklabels([f"{j}\nf/{F_NOM[j]}" for j in jj], fontsize=8)
ax.set_xlabel("cran j du diaphragme (rayon 2^(−j/2), part 2⁻ʲ)")
ax.set_ylabel("niveau des croisements à ce rayon")
ax.set_ylim(0, 17)
ax.legend(loc="lower right", fontsize=8.6)
ax.set_title("c)  Les crans comptent en binaire, les niveaux en binomiale")
legende(ax, "Fermer le diaphragme d'un cran garde la moitié des croisements (binaire, comme Perron). Les niveaux, eux,"
        " suivent la binomiale. Les deux ne coïncident qu'au premier cran, par la symétrie du complément ; ensuite il faut"
        f" de moins en moins de niveaux par cran, jusqu'à l'orbite centrale ({fr(math.log2(7710), '{:.2f}')} crans,"
        f" f/{fr(math.sqrt(7710), '{:.0f}')}).", y=-0.16)

# d) les chèvres dans le Venn
ax = fig.add_subplot(gs[1, 0])
for (nom, _, _), col, mk in zip(CHEVRES, (F.BLEU, VIOLET, F.ORANGE), ("o", "D", "s")):
    ax.plot(np.arange(1, 17), BROUTE[nom], mk + "-", color=col, lw=1.8, ms=5, label=nom)
ax.axhline(PHI_U / 180, color=F.ORANGE, lw=0.8, ls=":")
ax.text(1.2, PHI_U / 180 + 0.03, f"2 × {fr(PHI_U, '{:.2f}')}° / 360° = {fr(PHI_U / 180, '{:.4f}')}", color=F.ORANGE,
        fontsize=8.8)
ax.set_xlabel("niveau l (1 : le bord ; 16 : autour du centre)")
ax.set_ylabel("part du niveau broutée")
ax.set_xticks(range(1, 17))
ax.set_ylim(-0.03, 1.08)
ax.legend(loc="center left", fontsize=8.6)
ax.set_title("d)  Trois chèvres broutent chacune la moitié du Venn")
legende(ax, "Dans le dessin à aire égale, toute moitié de l'aire contient la moitié des croisements. La chèvre au centre"
        " (corde R/√2 : un cran) broute exactement les niveaux 9 à 16 ; le petit disque au point orange de la partie XVII"
        " et la chèvre d'Ullisch broutent aussi 50,0000 %, mais un mélange de niveaux. Au bord, Ullisch prend 39,34 % de"
        " chaque anneau : 70,81° de chaque côté du piquet, la corde de Ptolémée (partie X).", y=-0.13)

# e) la figure de diffraction
ax = fig.add_subplot(gs[1, 1])
ext = 400 / LARG
cm_ = LinearSegmentedColormap.from_list("nb", ["#000000", "#ffffff"])
lo_, hi_ = np.percentile(LOGP, 50), np.percentile(LOGP, 99.95)
ax.imshow(np.clip((LOGP - lo_) / (hi_ - lo_), 0, 1), cmap=cm_, extent=(-ext, ext, ext, -ext))
for a_ in FAM_C:
    ax.plot([0.165 * math.cos(math.radians(a_)), 0.19 * math.cos(math.radians(a_))],
            [0.165 * math.sin(math.radians(a_)), 0.19 * math.sin(math.radians(a_))], color=F.ORANGE, lw=1.6)
for a_ in FAM_I:
    ax.plot([0.165 * math.cos(math.radians(a_)), 0.19 * math.cos(math.radians(a_))],
            [0.165 * math.sin(math.radians(a_)), 0.19 * math.sin(math.radians(a_))], color=F.AQUA, lw=1.6)
ax.set_xlim(-ext, ext)
ax.set_ylim(ext, -ext)
ax.set_aspect("equal")
ax.set_xlabel("fréquence (cycles par pixel)")
ax.set_title("e)  La figure de diffraction de ton Venn")
legende(ax, f"Le spectre de l'image (log, comme tes deux images en noir et blanc). {len(ANG)} aigrettes : en orange, les"
        f" {len(FAM_C)} du contour à 17 côtés, celles du diaphragme à 17 lames (partie XXVIII) ; en vert, {len(FAM_I)}"
        f" venues de l'intérieur (les veines), tournées de {fr(ecart_res(RES_I, RES_CONTOUR), '{:.1f}')}°. Une étoile"
        " photographiée à travers un diaphragme à 17 lames ferait les mêmes 34 aigrettes.", y=-0.13)

# f) les harmoniques
ax = fig.add_subplot(gs[1, 2])
ms_ = np.arange(1, 81)
ax.bar(ms_ - 0.2, HARM_ENC / HARM_ENC.max(), width=0.45, color=F.BLEU, label="l'encre (vue du centre)")
hsp = HARM_SP[(0.08, 0.2)]
ax.bar(ms_ + 0.25, hsp / hsp.max(), width=0.45, color=F.ORANGE, label="le spectre (0,08 – 0,2 cycle/px)")
hpx = HARM_SP[(0.25, 0.45)]
ax.plot(ms_, hpx / hpx.max(), color=F.INK2, lw=0.9, label="le spectre aux plus hautes fréquences")
for k in (17, 34, 51, 68):
    ax.axvline(k, color=F.MUTED, lw=0.6, ls=":")
ax.set_xlim(0, 81)
ax.set_xticks([4, 17, 34, 51, 68])
ax.set_xlabel("ordre m de l'harmonique angulaire")
ax.set_ylabel("amplitude relative")
ax.legend(loc="upper right", fontsize=8.4)
ax.set_title("f)  17 dans l'image, 34 dans sa diffraction, 4 dans les pixels")
legende(ax, "L'image n'a que des harmoniques multiples de 17 (sa symétrie). Son spectre n'a que des multiples de 34 :"
        " une image réelle a un spectre symétrique, |F(k)| = |F(−k)|, ce qui double l'ordre. Aux plus hautes fréquences,"
        " c'est l'ordre 4 qui domine : la grille carrée des pixels (parties X et XVIII).", y=-0.13)
F.sauver(fig, "ae2_diaphragmes_diffraction.png")

# --------------------------- ae3 : les grains repositionnés, la granularité et le hasard ---------------------------
fig = plt.figure(figsize=(21, 14.8))
gs = fig.add_gridspec(2, 3, wspace=0.22, hspace=0.36)
vmax = float(np.percentile(CRU, 99.5))

ax = fig.add_subplot(gs[0, 0])
ax.imshow(CRU, cmap="gray", vmin=0, vmax=vmax, interpolation="nearest", extent=(-48, 48, 48, -48))
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("a)  Le centre brut : un grain par pixel")
legende(ax, "La clarté perçue autour du centre, 96 × 96 pixels : la région centrale (les 17 ensembles) et ses 17 coins,"
        " puis les arcs qui en partent, comme les rayons d'une étoile de Siemens (partie XVIII). Chaque pixel moyenne la"
        " lumière sur son carré.", y=-0.03)

ax = fig.add_subplot(gs[0, 1])
ax.imshow(DRZ, cmap="gray", vmin=0, vmax=vmax, interpolation="nearest", extent=(-48, 48, 48, -48))
axb = ax.inset_axes([0.0, 0.0, 0.34, 0.34])
axb.imshow(DRZ_BIAIS[96:288, 96:288], cmap="gray", vmin=0, vmax=vmax, interpolation="nearest")
axb.set_xticks([])
axb.set_yticks([])
for s_ in axb.spines.values():
    s_.set_color(F.ORANGE)
    s_.set_linewidth(2)
axb.set_title(f"centre faux de {fr(D_ESSAI, '{:.1f}')} px", fontsize=8, color=F.ORANGE, fontweight="normal")
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("b)  Les 17 copies empilées : un grain de 0,25 pixel")
legende(ax, "Les 17 rotations de l'image, recalées sur le centre de symétrie et déposées sur une grille 4 fois plus fine"
        " (le « drizzle » du télescope Hubble). Chaque copie tombe sur la grille des pixels avec un décalage différent :"
        f" ensemble, elles échantillonnent le motif 17 fois. En encart, le même empilement autour de mon premier centre"
        f" ({fr(D_ESSAI, '{:.1f}')} px du bon) : le motif se brouille.", y=-0.03)

ax = fig.add_subplot(gs[0, 2])
dd_ = np.array([d_ for d_, _ in INCOH[1:]])
vv_ = np.array([v_ for _, v_ in INCOH[1:]])
ax.semilogx(dd_, 100 * vv_, "o-", color=F.BLEU, lw=2, ms=6, label="vers le barycentre de la partie XXIX")
ax.semilogx([d_ for d_, _ in INCOH_P], [100 * v_ for _, v_ in INCOH_P], "s", color=F.ORANGE, ms=7,
            label="perpendiculairement")
ax.axhline(100 * INCOH[0][1], color=F.INK2, lw=0.9, ls=":")
ax.text(0.32, 100 * INCOH[0][1] + 2, f"au centre de symétrie : {fr(100 * INCOH[0][1], '{:.1f}')} %", fontsize=8.6,
        color=F.INK2)
ax.plot([D_ESSAI], [100 * INCOH_ESSAI], "*", color=ROUGE, ms=14, label="mon premier centre", zorder=6)
for d_, nom in ((D_ESSAI, "mon 1ᵉʳ essai"), (BARY[3][3], "barycentre XXIX")):
    ax.axvline(d_, color=F.MUTED, lw=0.8, ls="--")
    ax.text(d_ * 1.05, 18, nom, rotation=90, fontsize=8.4, color=F.INK2)
ax.set_xlabel("erreur sur le centre (pixels)")
ax.set_ylabel("variance que les 17 copies ne partagent pas (%)")
ax.set_ylim(0, 105)
ax.legend(loc="upper left", fontsize=8.6)
ax.set_title("c)  Ton écart est significatif : au centre, 1 px coûte la moitié")
legende(ax, "Si le centre est faux de d, la copie k est décalée de 2d·sin(πk/17), jusqu'à 2d : à 0,5 px, un quart de"
        " l'information n'est plus commune aux 17 copies, la moitié à 1 px, presque tout au-delà de 8 px. Le barycentre de"
        f" l'encre ({fr(BARY[3][3], '{:.1f}')} px) rend l'empilement aussi mauvais que le hasard.", y=-0.13)

ax = fig.add_subplot(gs[1, 0])
ax.plot(RS[FIABLE], GAIN[FIABLE], "o-", color=F.BLEU, lw=1.6, ms=3.5,
        label="mesuré sur ton Venn (harmonique 17, moyenne sur ±2 px)")
ax.plot(RS, GAIN_TH, color=F.ORANGE, lw=1.6, ls="--", label="2 J₁(x)/x, x = 17·b/r (disque de flou)")
ax.axhline(0, color=F.INK, lw=0.8)
ax.axvspan(B_DEF * 17 / Z1[1], B_DEF * 17 / Z1[0], color=F.ORANGE, alpha=0.1)
ax.axvspan(0, R_TROU, color=F.GRID, alpha=0.6)
ax.text(1.5, 0.85, "trou\ncentral", fontsize=8.4, color=F.INK2)
ax.text(B_DEF * 17 / Z1[1] + 1, -0.32, "contraste inversé", fontsize=8.8, color=F.ORANGE)
ax.set_xlabel("rayon r (pixels)")
ax.set_ylabel("contraste après flou / avant")
ax.set_xlim(0, 90)
ax.set_ylim(-0.45, 1.12)
ax.legend(loc="center right", bbox_to_anchor=(0.99, 0.33), fontsize=8.4)
ax.set_title(f"d)  Défocalisé, le centre inverse ses rayons (b = {fr(B_DEF, '{:g}')} px)")
legende(ax, "Un flou de défocalisation est un disque ; sa fonction de transfert 2 J₁(x)/x devient négative (ta figure de"
        " la FTO, partie VIII) : là, le noir et le blanc des rayons s'échangent, comme sur une mire de Siemens défocalisée"
        f" (la « fausse résolution »). Signes en accord sur {fr(100 * ACC_SIGNE, '{:.0f}')} % des rayons hors du trou.", y=-0.13)

ax = fig.add_subplot(gs[1, 1])
nn_ = np.array([n for n, _, _ in GRAN])
ax.semilogy(nn_, [wb for _, wb, _ in GRAN], "o-", color=F.BLEU, lw=2, ms=5, label="le reste : 2 px par croisement")
ax.semilogy(nn_, [wc for _, _, wc in GRAN], "s-", color=F.ORANGE, lw=2, ms=5, label="le centre : 2 px d'arc entre rayons")
ax.semilogy(nn_, [wc / 2 for _, _, wc in GRAN], "s:", color=F.ORANGE, lw=1.2, ms=3.5,
            label="le centre, grains repositionnés (÷ 2)")
ax.axhline(2000, color=F.INK2, lw=0.9, ls="--")
ax.text(11.2, 2200, "ton image : 2 000 px", fontsize=8.6, color=F.INK2)
ax.axhline(8000, color=F.MUTED, lw=0.8, ls=":")
ax.text(11.2, 8800, "8 000 px", fontsize=8.4, color=F.MUTED)
for n_ in (17, 19, 23):
    ax.axvline(n_, color=F.GRID, lw=1.2)
ax.set_xlabel("nombre de courbes n")
ax.set_ylabel("largeur d'image nécessaire (pixels)")
ax.set_xticks(range(11, 26, 2))
ax.legend(loc="upper left", fontsize=8.4)
ax.set_title("e)  Le centre est le goulot de la granularité")
legende(ax, f"Comme Perron sur une grille (partie XIV), le Venn bute sur le grain : au centre, n rayons doivent tenir"
        f" sur un tout petit cercle. À 2 000 px, le centre résout jusqu'à n = {fr(NM[(2000, 1.0, True)], '{:.1f}')} : le"
        f" Venn à 19 courbes y est juste à la limite. En repositionnant les grains, on gagne au plus un facteur 2 de"
        f" fréquence (la FTM du pixel s'annule à 1 cycle par pixel), soit environ deux courbes"
        f" ({fr(NM[(2000, 2.0, True)], '{:.1f}')}).", y=-0.13)

ax = fig.add_subplot(gs[1, 2])
X0 = 4.4
ax.set_xlim(0, len(TECHS) + X0)
ax.set_ylim(len(BANC) + 0.2, -1.3)
ax.axis("off")
ENTETES = ["p naïve", "Bonfer-\nroni", "nul\nbrouillé", "50\nchiffres", "varia-\ntion", "descrip-\ntion"]
for j, et_ in enumerate(ENTETES):
    ax.text(X0 + j + 0.5, -0.15, et_, ha="center", va="bottom", fontsize=7.8, color=F.INK2)
ax.text(X0 - 0.45, -0.15, "vérité", ha="center", va="bottom", fontsize=7.8, color=F.INK2)
COURTS = {"E1": "moitié des régions (2¹⁶)", "E2": "2⁻¹⁷·10¹⁷ = 5¹⁷", "E3": "la corde de l'arc de 70,81°",
          "E4": "⟨r²⟩ = R²/2 (disque)", "S1": "34·tan(π/34) ≈ π", "S2": "lumière du 17-gone",
          "S3": "niveaux ≥ 9 ≈ ½", "S4": "encre dans R/√2 ≈ ½", "C1": "(128/125) × lumière ≈ 1",
          "C2": "triangles ≈ 35,10 %"}
for i, c in enumerate(BANC):
    ax.text(0.02, i + 0.5, f"{c['code']}  {COURTS[c['code']]}", va="center", fontsize=7.8, color=F.INK)
    ax.text(X0 - 0.45, i + 0.5, c["verite"], va="center", ha="center", fontsize=7.8, color=F.INK2)
    for j, (t_, _) in enumerate(TECHS):
        v_ = verdict(t_, c)
        if v_ is None:
            col, txt = F.GRID, "—"
        else:
            juste = (v_ and c["verite"] != "hasard") or (not v_ and c["verite"] == "hasard")
            col, txt = ("#bfe3d2" if juste else "#f4c2bd"), ("non" if v_ else "hasard")
        ax.add_patch(plt.Rectangle((X0 + j + 0.04, i + 0.06), 0.92, 0.88, color=col, ec="none"))
        ax.text(X0 + j + 0.5, i + 0.5, txt, ha="center", va="center", fontsize=7.6, color=F.INK)
ax.set_title("f)  Quel test du hasard convient ici ?")
legende(ax, "Six techniques jugent dix relations dont on connaît la nature. Vert : verdict juste ; rouge : faux ; « non » :"
        " pas le hasard. Les tests à tolérance (colonnes 1 à 3, 6) déclarent « hasard » des liens de structure qui ont un"
        " petit écart connu ; la précision poussée et la variation du paramètre ne se trompent jamais ici. C'est ta"
        " remarque : plusieurs techniques concluraient au hasard.", y=-0.03)
F.sauver(fig, "ae3_grains_hasard.png")
print(f"figures : {time.time() - T1_:.1f} s ; total : {time.time() - T0:.1f} s")
