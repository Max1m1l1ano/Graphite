"""
Partie XXIX : le Venn à 17 au ppm — l'image retrouvée, l'analyse dimensionnelle et deux ombres du même cube.

    python3 scripts/venn_ppm.py [chemin/vers/venn17]        # ≈ 1 min

Il faut une copie du dépôt de Chris Dzoba (certificats et images sous licence CC BY 4.0) :

    git clone https://github.com/dzoba/venn17

placée par défaut à côté du dossier Graphite (../../.. depuis ce script), ou donnée en argument.

Écrit resultats/venn_ppm.md, figures/ad1_venn_ppm.png et figures/ad2_deux_ombres.png.

1. L'image retrouvée : le rendu « pressure » du dépôt (contour à 17 côtés, trou central, encre).
2. Les comptes au ppm, lus dans les certificats (11, 13, 17 et 19 courbes) : croisements, coins des régions, niveaux.
3. La granularité : remplissage du dessin selon le grain, dimension des veines, pixels par croisement selon n.
4. L'analyse dimensionnelle : ce que coûte 1 ppm pour chacun de nos objets (en bits).
5. Deux ombres du même cube : Perron (direction quelconque) et le Venn (grande diagonale) ; Henderson par les
   racines de l'unité ; l'ombre du cube de dimension 17 dans le plan, un 34-gone.
6. Gelé et liquide : les régions non monotones, rang par rang.
7. Le test des coïncidences au ppm.
"""

import logging
import math
import os
import sys
import textwrap
import time
import json
from decimal import Decimal
from math import comb

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from PIL import Image
from scipy import ndimage
from scipy.spatial import ConvexHull

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ICI, "..", "..", "..", "dzoba", "venn17")
CERT = os.path.join(DEPOT, "certificates")
IMAGE = os.path.join(DEPOT, "images", "venn17-pressure-dark-2000.png")
if not (os.path.isdir(CERT) and os.path.isfile(IMAGE)):
    sys.exit("Copie du dépôt introuvable : git clone https://github.com/dzoba/venn17, puis donne son chemin en argument.")
ROUGE, VIOLET, VERT = "#d0342c", "#7d4fc4", "#1baf7a"
R2 = math.sqrt(2)
GAM = 0.5772156649015329
T0 = time.time()
md = []


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


ligne("# Partie XXIX : le Venn à 17 au ppm — l'image retrouvée, l'analyse dimensionnelle et deux ombres du même cube\n")
ligne("Tableaux complets, recalculés par `scripts/venn_ppm.py` à partir du dépôt de Chris Dzoba"
      " (https://github.com/dzoba/venn17 ; certificats et images sous licence CC BY 4.0).\n")

# ===========================================================================
# 1. L'image retrouvée
# ===========================================================================
ligne("## 1. L'image retrouvée : le rendu « pressure » du dépôt\n")
IM = np.asarray(Image.open(IMAGE).convert("RGB")).astype(float)
LUM = IM.mean(2)
HAUT, LARG = LUM.shape
FOND = float(np.median(LUM[:20, :20]))
ALLUME = LUM > FOND + 25
ys, xs = np.nonzero(ALLUME)
cx0, cy0 = (xs.min() + xs.max()) / 2, (ys.min() + ys.max()) / 2
# le centre : celui du plus grand disque vide autour du milieu (le trou central)
TROU = (-1.0, cx0, cy0)
for ox in np.arange(-15, 16):
    for oy in np.arange(-15, 16):
        m_ = float(np.hypot(xs - (cx0 + ox), ys - (cy0 + oy)).min())
        if m_ > TROU[0]:
            TROU = (m_, cx0 + ox, cy0 + oy)
R_TROU, CX, CY = TROU
YY, XX = np.mgrid[0:HAUT, 0:LARG]
RR = np.hypot(XX - CX, YY - CY)
TH = np.arctan2(YY - CY, XX - CX)
NB = 3600
BINS = ((TH + np.pi) / (2 * np.pi) * NB).astype(int) % NB
RMAX = np.zeros(NB)
np.maximum.at(RMAX, BINS[ALLUME], RR[ALLUME])
HARM = np.abs(np.fft.rfft(RMAX - RMAX.mean()))
HARM_TOP = [int(k) for k in np.argsort(HARM[2:])[::-1][:4] + 2]
R_OUT = float(RMAX.max())
DEDANS = RR < np.interp((TH + np.pi) / (2 * np.pi) * NB, np.arange(NB), RMAX) - 2
AIRE_PX = int(DEDANS.sum())
ENCRE = float(ALLUME[DEDANS].mean())
ligne(f"- Image de {LARG} × {HAUT} pixels ; le contour a pour harmoniques principales {HARM_TOP} : le 17-gone et ses"
      f" multiples. Rayon extérieur ≈ {fr(R_OUT, '{:.0f}')} px, aire intérieure {ent(AIRE_PX)} px.")
ligne(f"- Trou central : disque vide de rayon {fr(R_TROU, '{:.1f}')} px, soit {fr(R_TROU / R_OUT, '{:.4f}')} du rayon et"
      f" {fr(math.pi * R_TROU ** 2 / AIRE_PX * 1e6, '{:.0f}')} ppm de l'aire.")
ligne(f"- Encre (pixels plus clairs que le fond) : {fr(100 * ENCRE, '{:.1f}')} % de l'intérieur.")
ANN = []
for a0, a1 in ((0, 0.2), (0.2, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 0.95)):
    m_ = DEDANS & (RR >= a0 * R_OUT) & (RR < a1 * R_OUT)
    ANN.append((a0, a1, float(ALLUME[m_].mean())))
ligne("  - par anneau : " + " ; ".join(f"{fr(a0, '{:.1f}')}–{fr(a1, '{:.2f}')} : {fr(100 * e_, '{:.0f}')} %"
                                       for a0, a1, e_ in ANN) + " (densité uniforme, comme annoncé).\n")

# ===========================================================================
# 2. Les comptes au ppm
# ===========================================================================
ligne("## 2. Les comptes au ppm, lus dans les certificats\n")
FICHIERS = [("best11-s0.json", 11), ("v3-13-s0.json", 13), ("venn17-local-c3-s2.json", 17), ("venn17-gcp-s12.json", 17),
            ("venn17-gcp-s14.json", 17), ("venn17-gcp-s16.json", 17), ("venn19-closure-s196002.json", 19)]
STATS = {}
for nom, n_attendu in FICHIERS:
    t1 = time.time()
    with open(os.path.join(CERT, nom)) as fh:
        dd = json.load(fh)
    n = int(dd["n"])
    assert n == n_attendu
    Fc = np.array([[int(lab[::-1], 2) for lab in f_] for f_ in dd["faces"]], dtype=np.int64)
    del dd
    NL = 1 << n
    V = len(Fc)
    pc = np.array([bin(x).count("1") for x in range(NL)], dtype=np.int64)
    deg = np.bincount(Fc.ravel(), minlength=NL)
    rangs = np.sort(pc[Fc], axis=1)
    kk1 = bool(np.all((rangs[:, 1] == rangs[:, 0] + 1) & (rangs[:, 2] == rangs[:, 0] + 1)
                      & (rangs[:, 3] == rangs[:, 0] + 2)))
    lev = rangs[:, 0] + 1
    NLV = np.bincount(lev, minlength=n)[1:n]
    a_ = Fc.ravel()
    b_ = np.roll(Fc, -1, axis=1).ravel()
    haut, bas = np.zeros(NL, bool), np.zeros(NL, bool)
    mo = pc[b_] > pc[a_]
    haut[a_[mo]] = True
    bas[b_[mo]] = True
    mo = pc[b_] < pc[a_]
    bas[a_[mo]] = True
    haut[b_[mo]] = True
    interieur = (pc > 0) & (pc < n)
    nonmono = interieur & ~(haut & bas)
    STATS[nom] = dict(n=n, V=V, deg=deg, pc=pc, kk1=kk1, NLV=NLV, nonmono=nonmono,
                      creux=int((interieur & ~bas).sum()), sommets=int((interieur & ~haut).sum()),
                      t=time.time() - t1)
ligne("| certificat | n | croisements | régions | coins (min–max, hors centre et dehors) | centre et dehors | rangs k, k+1, k+1, k+2 |")
ligne("|---|---:|---:|---:|---|---|---|")
for nom, _ in FICHIERS:
    s_ = STATS[nom]
    n = s_["n"]
    dg = s_["deg"].copy()
    dmid = np.delete(dg, [0, (1 << n) - 1])
    ligne(f"| {nom} | {n} | {ent(s_['V'])} | {ent(1 << n)} | {dmid.min()} – {dmid.max()} | {dg[0]} et {dg[-1]} coins |"
          f" {'partout' if s_['kk1'] else 'non'} |")
S17 = STATS["venn17-local-c3-s2.json"]
V17 = S17["V"]
ligne(f"\n- Un croisement de l'image pèse 1/{ent(V17)} de l'aire = {fr(1e6 / V17, '{:.4f}')} ppm, soit"
      f" {fr(AIRE_PX / V17, '{:.2f}')} pixels.")
ligne(f"- Une région moyenne pèse 2⁻¹⁷ = {str(Decimal(1) / Decimal(2 ** 17)).replace('.', ',')} ="
      f" {fr(2.0 ** -17 * 1e6, '{:.11f}')} ppm : les chiffres de 5¹⁷ = {5 ** 17} (partie XXVI).")
ligne(f"- Coins par région : en moyenne 4·(2ⁿ − 2)/2ⁿ = {fr(4 * V17 / 2 ** 17, '{:.8f}')} (n = 17).\n")
ligne("**La texture : la part des régions à 3, 4, 5, 6, 7 coins et plus.**\n")
ligne("| certificat | 3 coins | 4 | 5 | 6 | 7 et plus |")
ligne("|---|---|---|---|---|---|")
TEXTURE = {}
for nom, _ in FICHIERS:
    s_ = STATS[nom]
    n = s_["n"]
    dmid = np.delete(s_["deg"], [0, (1 << n) - 1])
    parts = [float(np.mean(dmid == c)) for c in (3, 4, 5, 6)] + [float(np.mean(dmid >= 7))]
    TEXTURE[nom] = parts
    ligne(f"| {nom} | " + " | ".join(fr(100 * p_, '{:.1f}') + " %" for p_ in parts) + " |")
ligne("\n**Les niveaux.** Le niveau d'un croisement est le rang moyen de ses quatre régions. Le dessin donne à chaque"
      " niveau un anneau d'aire proportionnelle à son nombre de croisements.\n")
ligne("| niveau l | croisements (c3-s2) | C(17, l) | rapport | rayon cible √(part des niveaux ≥ l) |")
ligne("|---:|---:|---:|---|---|")
NLV17 = S17["NLV"]
CUM17 = np.cumsum(NLV17[::-1])[::-1]
RAYON_NIV = np.sqrt(CUM17 / CUM17[0])
for l_ in range(1, 17):
    ligne(f"| {l_} | {ent(int(NLV17[l_ - 1]))} | {ent(comb(17, l_))} | {fr(NLV17[l_ - 1] / comb(17, l_), '{:.3f}')} |"
          f" {fr(float(RAYON_NIV[l_ - 1]), '{:.4f}')} |")
DEMI = {nom: float(STATS[nom]["NLV"][8:].sum() / STATS[nom]["V"]) for nom, n_ in FICHIERS if n_ == 17}
ligne(f"\n- Σ_l C(17, l) = 2¹⁷ − 2 = {ent(sum(comb(17, l_) for l_ in range(1, 17)))} : en moyenne, un croisement par"
      " région de même rang. Les niveaux 1, 2, 15 et 16 tombent exactement sur C(17, l).")
ligne("- Part des croisements de niveau ≥ 9 (donc dans le disque de rayon R/√2 si le dessin suivait exactement sa cible) : "
      + " ; ".join(f"{nom.replace('.json', '')} : {fr(v_, '{:.5f}')} ({fr((v_ - 0.5) * 1e6, '{:+.0f}')} ppm)"
                   for nom, v_ in DEMI.items()) + ".")
ligne(f"- Les 17 croisements du niveau 16 entourent la région centrale, au rayon cible √(17/{ent(V17)}) ="
      f" {fr(math.sqrt(17 / V17), '{:.4f}')} R, soit {fr(math.sqrt(17 / V17) * R_OUT, '{:.1f}')} px ; le trou mesuré fait"
      f" {fr(R_TROU, '{:.1f}')} px (le dessin relâche un peu sa cible).\n")

# ===========================================================================
# 3. La granularité
# ===========================================================================
ligne("## 3. La granularité\n")


def remplissage(masque, tailles):
    out = []
    for s_ in tailles:
        h_, w_ = (masque.shape[0] // s_) * s_, (masque.shape[1] // s_) * s_
        m_ = masque[:h_, :w_].reshape(h_ // s_, s_, w_ // s_, s_).any(axis=(1, 3))
        ins = INT[:h_, :w_].reshape(h_ // s_, s_, w_ // s_, s_).all(axis=(1, 3))
        out.append((s_, int(m_[ins].sum()), int(ins.sum())))
    return out


INT = RR < 0.9 * R_OUT * math.cos(math.pi / 17)
TAILLES = [1, 2, 3, 4, 5, 6, 8, 12, 16, 24, 32, 48, 64]
REMP = remplissage(ALLUME, TAILLES)
LISSE = ndimage.uniform_filter(LUM, 3)
VEINES = {}
for q_ in (0.90, 0.97, 0.99):
    seuil = float(np.quantile(LISSE[INT], q_))
    VEINES[q_] = remplissage((LISSE > seuil) & INT, TAILLES)


def dim_locale(res, s_lo, s_hi):
    pts = [(s_, n_) for s_, n_, _ in res if s_lo <= s_ <= s_hi]
    x_ = np.log([p_[0] for p_ in pts])
    y_ = np.log([p_[1] for p_ in pts])
    return float(-np.polyfit(x_, y_, 1)[0])


ligne("| grain (pixels) | grain (ppm de l'aire) | dessin rempli à |")
ligne("|---:|---:|---|")
for s_, n_, tot in REMP[:8]:
    ligne(f"| {s_} | {fr(s_ * s_ / AIRE_PX * 1e6, '{:.2f}')} | {fr(100 * n_ / tot, '{:.1f}')} % |")
DIM_V = {q_: dim_locale(VEINES[q_], 3, 32) for q_ in VEINES}
ligne(f"\n- Le dessin est plein dès un grain de 4 à 5 pixels, la taille d'une région ({fr(math.sqrt(AIRE_PX / V17), '{:.2f}')}"
      " px de côté en moyenne) : au-dessus de 7,6 ppm d'aire, il est de dimension 2 ; en dessous, ce sont des lignes.")
ligne("- Les veines (les pixels les plus clairs, après un lissage de 3 px) ont pour dimension de comptage de boîtes, entre"
      " 3 et 32 px : " + " ; ".join(f"les {fr(100 * (1 - q_), '{:.0f}')} % les plus clairs : {fr(d_, '{:.2f}')}"
                                     for q_, d_ in DIM_V.items()) + ". Des lignes, pas des surfaces.\n")
ligne("**Pixels par croisement**, pour un dessin de même type (aire intérieure ∝ largeur²) :\n")
ligne("| courbes n | croisements 2ⁿ − 2 | à 2 000 px | à 8 000 px |")
ligne("|---:|---:|---|---|")
PXC = {}
for n in (5, 7, 11, 13, 17, 19, 23):
    v_ = (1 << n) - 2
    PXC[n] = (AIRE_PX / v_, 16 * AIRE_PX / v_)
    ligne(f"| {n} | {ent(v_)} | " + " | ".join(ent(round(x_)) if x_ >= 100 else fr(x_, '{:.2f}') for x_ in PXC[n]) + " |")
ligne("\n- Chaque courbe de plus double le nombre de croisements : pour garder le même grain, il faut multiplier la"
      " largeur de l'image par √2. Une courbe = un cran de diaphragme (partie I).\n")

# ===========================================================================
# 4. L'analyse dimensionnelle
# ===========================================================================
ligne("## 4. L'analyse dimensionnelle : ce que coûte 1 ppm\n")
EPS = 1e-6


def kakeya_haut(ld):
    best = math.inf
    for N_ in range(2, 120):
        for k in range(0, 80):
            x_ = k * math.log(2) - ld
            if x_ > 30:
                break
            best = min(best, N_ * (math.tan(math.pi / (2 * N_)) * 2 / (k + 2)
                                    + math.exp(x_) / math.cos(math.pi / (2 * N_))))
    return best


N_SERIE = next(n for n in range(2, 200) if 1.03 * 2 ** (-n / 2) / n <= EPS)
LD = math.log(1 / EPS)
PRIX = [
    ("Venn : 2ⁿ régions, grain en aire", "1 bit par courbe", math.log2(1 / EPS), "courbes"),
    ("Venn : grain en longueur", "½ bit par courbe", 2 * math.log2(1 / EPS), "courbes"),
    ("Perron : branches de largeur 2⁻ᵏ", "1 bit par étage", math.log2(1 / EPS), "étages"),
    ("la série de la chèvre (partie XXV) : 1,03·2^(−n/2)/n", "½ bit par dimension", N_SERIE, "dimensions"),
    ("le ménisque de la chèvre : 2/(3n²)", "n ∝ ε^(−1/2)", math.sqrt(2 / (3 * EPS)), "dimensions"),
    ("le diaphragme à N lames : 2π²/(3N²)", "n ∝ ε^(−1/2)", math.pi * math.sqrt(2 / (3 * EPS)), "lames"),
    ("le plan de la lentille : x₀ ≈ 1/n", "n ∝ ε⁻¹", 1 / EPS, "dimensions"),
    ("l'équateur (partie I)", "n ∝ ε⁻²", 1 / EPS ** 2, "dimensions"),
]
ligne("| objet | rythme | pour 1 ppm |")
ligne("|---|---|---|")
for nom, rythme, val, unite in PRIX:
    # le premier nombre entier de pas qui atteint 1 ppm (et la valeur continue quand elle n'est pas entière)
    if val >= 1e5:
        vtxt = f"{ent(round(val)) if val < 1e7 else petit(val)} {unite}"
    elif float(val).is_integer():
        vtxt = f"{ent(int(val))} {unite}"
    else:
        vtxt = f"{ent(math.ceil(val))} {unite} ({fr(val, '{:.2f}')} en continu)"
    ligne(f"| {nom} | {rythme} | {vtxt} |")
KB_PPM, KH_PPM = math.pi / (1 + 2 * GAM + 2 * (math.log(2) + LD)), kakeya_haut(LD)
ligne(f"| Kakeya au grain δ = 1 ppm (parties XXVI et XXVIII) | 1/aire : + 0,441 par bit | aire entre"
      f" {fr(KB_PPM, '{:.4f}')} et {fr(KH_PPM, '{:.4f}')} |")
ligne(f"\n- 2²⁰ = {ent(2 ** 20)} : le « méga » binaire. 10⁶/2²⁰ = {str(Decimal(10 ** 6) / Decimal(2 ** 20)).replace('.', ',')}"
      " a les chiffres de 5²⁰"
      " (partie XXVI) : un ppm décimal vaut 0,954 « ppm binaire ».")
ligne("- Le Venn et Perron sont sur la même marche : un bit par pas. La série de la chèvre gagne un demi-bit par dimension"
      " (le facteur √2, un cran) : elle va au même rythme que le Venn mesuré en longueur, 2·log₂ 10 = 6,644 par décade.\n")

# ===========================================================================
# 5. Deux ombres du même cube
# ===========================================================================
ligne("## 5. Deux ombres du même cube\n")
ligne("### 5.1 Henderson, vu comme une ombre\n")
ligne("L'ombre symétrique du cube {0, 1}ⁿ dans le plan envoie l'ensemble S sur Σ_{i∈S} ω^i (ω = e^(2iπ/n)). La rotation"
      " des étiquettes devient la rotation de 2π/n. Le centre ne reçoit que ∅ et tout, sauf si n est composé :\n")
NUL = {}
for n in range(2, 21):
    w_ = np.exp(2j * np.pi * np.arange(n) / n)
    s_ = np.zeros(1, complex)
    for i in range(n):
        s_ = np.concatenate([s_, s_ + w_[i]])
    NUL[n] = int(np.sum(np.abs(s_[1:-1]) < 1e-9))
ligne("| n | " + " | ".join(str(n) for n in NUL) + " |")
ligne("|---|" + "---:|" * len(NUL))
ligne("| sous-ensembles propres de somme nulle | " + " | ".join(ent(v_) for v_ in NUL.values()) + " |")
PREMIERS_OK = all((NUL[n] == 0) == all(n % d_ for d_ in range(2, n)) for n in NUL)
ligne(f"\n- Zéro exactement pour les n premiers : {'vrai' if PREMIERS_OK else 'faux'} (n ≤ 20).")
n = 17
w17 = np.exp(2j * np.pi * np.arange(n) / n)
OMB = np.zeros(1, complex)
RK = np.zeros(1, int)
for i in range(n):
    OMB = np.concatenate([OMB, OMB + w17[i]])
    RK = np.concatenate([RK, RK + 1])
HULL = ConvexHull(np.c_[OMB.real, OMB.imag])
PH = np.c_[OMB.real, OMB.imag][HULL.vertices]
RAYS = np.hypot(PH[:, 0] - PH[:, 0].mean(), PH[:, 1] - PH[:, 1].mean())
ligne(f"- L'ombre du cube de dimension 17 a pour contour un polygone régulier à {len(HULL.vertices)} côtés (rayons"
      f" {fr(RAYS.min(), '{:.6f}')} à {fr(RAYS.max(), '{:.6f}')}) : le 34-gone des aigrettes et des éventails (partie XXVIII),"
      " comme l'hexagone est l'ombre du cube de dimension 3.")
MOY_RK = {k: float(np.mean(np.abs(OMB[RK == k]) ** 2)) for k in (1, 4, 8, 9, 13, 16)}
ligne("- Les sommets de rang k sont en moyenne à |S|² = k(n − k)/(n − 1) : "
      + " ; ".join(f"k = {k} : {fr(v_, '{:.4f}')} ({fr(k * (17 - k) / 16, '{:.4f}')})" for k, v_ in MOY_RK.items()) + ".\n")
ligne("### 5.2 Perron et le Venn\n")
ligne("- Perron (partie XXVIII) : à la profondeur v, la coupe est l'ombre du cube {0, 1}ᵏ sur la direction"
      " (a₀, …, a_(k−1)) ; les 2ᵏ sommets y restent séparés, rangés dans l'ordre binaire, et fusionnent par moitiés :"
      " 2^(k−j) fentes au niveau j.")
ligne("- Le dessin du Venn : le rayon suit le niveau, c'est-à-dire l'ombre du cube {0, 1}¹⁷ sur sa grande diagonale (le"
      " nombre de 1) ; il y a environ C(17, l) croisements au niveau l, exactement aux deux bouts.")
ligne(f"- Comptes par niveau : Perron, 2^(k − j) (une suite géométrique) ; Venn, C(17, l) (une binomiale). Au niveau 8, la"
      f" binomiale donne {ent(comb(17, 8))} et le certificat {ent(int(NLV17[7]))}.\n")

# ===========================================================================
# 6. Gelé et liquide
# ===========================================================================
ligne("## 6. Gelé et liquide : les régions non monotones\n")
ligne("Une région de rang k est monotone si elle touche une région de rang k − 1 et une de rang k + 1 (Bultena, Grünbaum,"
      " Ruskey). Sinon, c'est un creux ou un sommet de la « hauteur » (le rang).\n")
ligne("| certificat | non monotones | creux | sommets | rangs gelés (aucune non monotone) |")
ligne("|---|---:|---:|---:|---|")
GEL = {}
for nom, _ in FICHIERS:
    s_ = STATS[nom]
    n = s_["n"]
    par = [int(s_["nonmono"][s_["pc"] == r_].sum()) for r_ in range(n + 1)]
    gel = [r_ for r_ in range(n + 1) if par[r_] == 0]
    GEL[nom] = par
    ligne(f"| {nom} | {ent(int(s_['nonmono'].sum()))} ({fr(100 * s_['nonmono'].sum() / (1 << n), '{:.1f}')} %) |"
          f" {ent(s_['creux'])} | {ent(s_['sommets'])} | {', '.join(map(str, gel))} |")
GEL_AIRE = (sum(comb(17, r_) for r_ in (0, 1, 2, 15, 16, 17)) - 2) / (2 ** 17 - 2)
ligne(f"\n- Rangs gelés : les trois du bord (0, 1, 2) et les trois du centre (15, 16, 17) pour les Venn à 17 courbes ; ils"
      f" ne pèsent que {fr(100 * GEL_AIRE, '{:.2f}')} % des régions.")
ligne("- La couche gelée garde la même épaisseur (2 à 3 rangs) de 11 à 19 courbes : sa part relative diminue avec n.\n")

# ===========================================================================
# 7. Le test des coïncidences au ppm
# ===========================================================================
ligne("## 7. Le test des coïncidences au ppm\n")
r_ull = 1.158728473018121
NOS = {
    "corde de la chèvre plane (Ullisch)": r_ull, "corde de la chèvre en 3D": 1.2285448637352209,
    "√2 (chèvre infinie)": R2, "1/√2 (un cran, demi-aire)": 1 / R2, "√3": math.sqrt(3), "√7": math.sqrt(7),
    "1 + √2 (argent)": 1 + R2, "φ (or)": (1 + math.sqrt(5)) / 2, "π/4 (losange)": math.pi / 4,
    "π/(2√3) (hexagone)": math.pi / (2 * math.sqrt(3)), "β d'Ullisch": 1.905695729, "arccos(1/3)": math.acos(1 / 3),
    "le ménisque de 0,35 %": r_ull * math.sqrt(3) / 2 - 1, "Córdoba : 1 + 2γ + 2 ln 2": 1 + 2 * GAM + 2 * math.log(2),
    "2 ln 10/π": 2 * math.log(10) / math.pi, "128/125 (diesis)": 128 / 125, "10⁶/2²⁰": 10 ** 6 / 2 ** 20,
    "35,10 % (ombres égales)": 6 * math.acos(1 / 3) / math.pi - 2, "2·log₂ 10": 2 * math.log2(10),
    "π·ln 2": math.pi * math.log(2), "2√3·ln 2": 2 * math.sqrt(3) * math.log(2), "2·ln 2": 2 * math.log(2),
    "e^(−1/2)·√(ln 2/π)": math.exp(-0.5) * math.sqrt(math.log(2) / math.pi), "4/405 (c₂)": 4 / 405,
    "1/96 (c₃)": 1 / 96, "π": math.pi, "1/2": 0.5, "2/3": 2 / 3, "3/2": 1.5, "1/3": 1 / 3, "4/3": 4 / 3,
}
dm17 = np.delete(S17["deg"], [0, 2 ** 17 - 1])
VENN = {
    "2⁻¹⁷": 2.0 ** -17, "1/131 070": 1 / 131070, "7 710/2¹⁷": 7710 / 2 ** 17,
    "part des triangles": float(np.mean(dm17 == 3)), "part des quadrilatères": float(np.mean(dm17 == 4)),
    "part des pentagones": float(np.mean(dm17 == 5)), "part des hexagones": float(np.mean(dm17 == 6)),
    "part non monotone": float(S17["nonmono"].sum() / 2 ** 17), "part des niveaux ≥ 9": DEMI["venn17-local-c3-s2.json"],
    "N₈/C(17, 8)": float(NLV17[7] / comb(17, 8)), "N₉/C(17, 9)": float(NLV17[8] / comb(17, 9)),
    "cos(2π/17)": math.cos(2 * math.pi / 17), "lumière du 17-gone": 17 / (2 * math.pi) * math.sin(2 * math.pi / 17),
    "34·tan(π/34)": 34 * math.tan(math.pi / 34), "(−1 + √17)/2": (-1 + math.sqrt(17)) / 2, "√17": math.sqrt(17),
    "1/17": 1 / 17, "coins moyens": 4 * (2 ** 17 - 2) / 2 ** 17, "creux / 2¹⁷": S17["creux"] / 2 ** 17,
    "sommets / 2¹⁷": S17["sommets"] / 2 ** 17,
}
PAIRES = []
for na, a_ in NOS.items():
    for nb, b_ in VENN.items():
        for mode, val in (("=", b_ / a_), ("× = 1", a_ * b_)):
            PAIRES.append((abs(math.log(val)), na, nb, mode))
PAIRES.sort()
TOLS = [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 1e-4, 1e-5, 1e-6]
LV = np.log([*NOS.values(), *VENN.values()])
LARGEUR = float(LV.max() - LV.min())
OBS = {t_: sum(1 for p_ in PAIRES if p_[0] < t_) for t_ in TOLS}
# hasard : le catalogue du Venn brouillé (chaque nombre multiplié par e^u, u ~ N(0 ; 0,2)), 4 000 tirages
rng = np.random.default_rng(29)
LA = np.log(np.array(list(NOS.values())))[:, None]
LB = np.log(np.array(list(VENN.values())))[None, :]
CPT = np.zeros(len(TOLS))
NTIR = 4000
for _ in range(NTIR):
    lb = LB + rng.normal(0, 0.2, LB.shape)
    e_ = np.concatenate([np.abs(lb - LA).ravel(), np.abs(lb + LA).ravel()])
    CPT += np.array([(e_ < t_).sum() for t_ in TOLS])
ATT = {t_: c_ / NTIR for t_, c_ in zip(TOLS, CPT)}
ligne(f"- {len(NOS)} constantes de nos objets, {len(VENN)} nombres du Venn à 17 ; on compare chaque paire directement"
      f" (b ≈ a) et en inverse (a·b ≈ 1) : {ent(len(PAIRES))} comparaisons. Pour le hasard, on brouille les nombres du Venn"
      " (chacun multiplié par un facteur aléatoire autour de 1, à ±20 %) : ils gardent leur répartition, mais perdent"
      " toute relation exacte.\n")
ligne("| tolérance | coïncidences observées | attendues par hasard (catalogue brouillé de ±20 %, 4 000 tirages) |")
ligne("|---|---:|---|")
for t_ in TOLS:
    ligne(f"| {fr(t_ * 100, '{:g}')} % ({ent(round(t_ * 1e6))} ppm) | {OBS[t_]} |"
          f" {fr(ATT[t_], '{:.3f}') if ATT[t_] >= 1e-3 else petit(ATT[t_], 1) if ATT[t_] > 0 else 'moins de 0,0003'} |")
ligne("\nLes plus proches :\n")
ligne("| écart | nos objets | le Venn à 17 | relation |")
ligne("|---|---|---|---|")
for e_, na, nb, mode in PAIRES[:10]:
    ligne(f"| {fr(e_ * 1e6, '{:.0f}')} ppm | {na} | {nb} | {'b ≈ a' if mode == '=' else 'a·b ≈ 1'} |")
ligne("")
DUREE = time.time() - T0
ligne(f"(calculs : {fr(DUREE, '{:.0f}')} s)")
with open(os.path.join(ICI, "..", "resultats", "venn_ppm.md"), "w") as fh:
    fh.write("\n".join(md) + "\n")
print(f"calculs : {DUREE:.1f} s")
T1 = time.time()


# ===========================================================================
# Figures
# ===========================================================================
def legende(ax, texte, y=-0.13, largeur=86):
    texte = textwrap.fill(" ".join(texte.split("\n")), largeur)
    ax.text(0.5, y, texte, transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)


BOITE = dict(boxstyle="round,pad=0.35", fc=F.SURF, ec=F.BASE)

# --------------------------- ad1 : l'image au ppm ---------------------------
fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.2, hspace=0.36)

# a) l'image, avec le cercle de demi-aire et les anneaux de niveaux
ax = fig.add_subplot(gs[0, 0])
pas = 2
ax.imshow(IM[::pas, ::pas].astype(np.uint8), extent=(-CX / R_OUT, (LARG - CX) / R_OUT, -(HAUT - CY) / R_OUT, CY / R_OUT))
tt = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(tt) / R2, np.sin(tt) / R2, color="#ffffff", lw=1.4, ls="--")
ax.text(0.0, -1 / R2 - 0.07, "R/√2 : la moitié de l'aire, donc des croisements", color="#ffffff", ha="center",
        fontsize=8.6)
ax.set_xlim(-1.04, 1.04)
ax.set_ylim(-1.04, 1.04)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("a)  Ton image : le Venn à 17 de Chris Dzoba")
legende(ax, f"Image : Chris Dzoba, dépôt dzoba/venn17, licence CC BY 4.0. Contour : un 17-gone imposé par la méthode de"
        f" dessin. Chaque croisement occupe la même aire : 1/131 070, soit 7,63 ppm ou {fr(AIRE_PX / V17, '{:.1f}')} pixels."
        f" Trou central : {fr(R_TROU, '{:.0f}')} px de rayon. Encre : {fr(100 * ENCRE, '{:.0f}')} % de l'image.", y=-0.03)

# b) les niveaux : C(17, l) contre le certificat
ax = fig.add_subplot(gs[0, 1])
ls_ = np.arange(1, 17)
ax.bar(ls_, [comb(17, int(l_)) for l_ in ls_], color=F.GRID, width=0.8, label="C(17, l) : l'ombre du cube sur sa diagonale")
for nom, mk, col in (("venn17-local-c3-s2.json", "o", F.BLEU), ("venn17-gcp-s12.json", "s", F.ORANGE),
                     ("venn17-gcp-s14.json", "^", VERT), ("venn17-gcp-s16.json", "D", VIOLET)):
    ax.plot(ls_, STATS[nom]["NLV"], mk, color=col, ms=5, label=nom.replace(".json", ""))
ax.set_xlabel("niveau l du croisement (rang moyen de ses quatre régions)")
ax.set_ylabel("croisements")
ax.set_xticks(range(1, 17))
ax.legend(loc="upper left", fontsize=8.2)
ax.set_title("b)  Les anneaux de l'image suivent la binomiale")
legende(ax, "Le dessin range les croisements par niveau, du bord (1) au centre (16), dans des anneaux d'aire"
        " proportionnelle à leur nombre. Ce nombre suit C(17, l) à ±17 % près, et exactement aux deux bouts : le rayon"
        " de ton image lit l'ombre du cube {0, 1}¹⁷ sur sa grande diagonale.", y=-0.13)

# c) gelé et liquide
ax = fig.add_subplot(gs[0, 2])
for nom, col, lab in (("best11-s0.json", F.RAMPE[0], "11 courbes"), ("v3-13-s0.json", F.RAMPE[1], "13 courbes"),
                      ("venn17-local-c3-s2.json", F.RAMPE[3], "17 courbes (c3-s2)"),
                      ("venn19-closure-s196002.json", F.RAMPE[4], "19 courbes")):
    n = STATS[nom]["n"]
    fr_ = [GEL[nom][r_] / comb(n, r_) for r_ in range(n + 1)]
    ax.plot(np.arange(n + 1) / n, np.array(fr_) * 100, "o-", color=col, ms=4, lw=1.5, label=lab)
ax.axvspan(0, 2.5 / 17, color=F.BLEU, alpha=0.07)
ax.axvspan(14.5 / 17, 1, color=F.BLEU, alpha=0.07)
ax.text(0.01, 75, "gelé", color=F.BLEU, fontsize=9.5)
ax.text(0.9, 75, "gelé", color=F.BLEU, fontsize=9.5)
ax.text(0.45, 75, "liquide", color=F.ORANGE, fontsize=9.5)
ax.set_xlabel("rang de la région ÷ n")
ax.set_ylabel("régions non monotones (%)")
ax.set_ylim(0, 85)
ax.legend(loc="upper center", fontsize=8.2, bbox_to_anchor=(0.5, 0.86), ncol=2)
ax.set_title("c)  Gelé au bord et au centre, liquide entre les deux")
legende(ax, "Une région est un creux ou un sommet du rang quand elle ne touche pas les deux rangs voisins. Au bord et"
        " au centre (trois rangs de chaque côté à 17 courbes), il n'y en a aucune : c'est gelé, comme hors d'un cercle"
        " arctique (partie XXVII). Entre les deux, 10 à 20 % des régions sont des creux ou des sommets.", y=-0.13)

# d) la texture
ax = fig.add_subplot(gs[1, 0])
labels_t = ["3 coins", "4", "5", "6", "7 et plus"]
noms_t = [("best11-s0.json", "11"), ("v3-13-s0.json", "13"), ("venn17-local-c3-s2.json", "17"),
          ("venn19-closure-s196002.json", "19")]
larg_b = 0.2
for j_, (nom, lab) in enumerate(noms_t):
    ax.bar(np.arange(5) + (j_ - 1.5) * larg_b, np.array(TEXTURE[nom]) * 100, width=larg_b, color=F.RAMPE[[0, 1, 3, 4][j_]],
           label=f"{lab} courbes")
ax.set_xticks(range(5))
ax.set_xticklabels(labels_t)
ax.set_ylabel("part des régions (%)")
ax.legend(loc="upper right", fontsize=8.6)
ax.set_title("d)  La même texture à 11, 13, 17 et 19 courbes")
legende(ax, "Le nombre de coins des régions (sans le centre et le dehors, qui en ont n). La répartition ne dépend presque"
        " pas de n : une courbe de plus ne change pas le grain local, elle double seulement le nombre de régions. En"
        " moyenne, une région a 4·(2ⁿ − 2)/2ⁿ coins, presque 4 : un quadrilatère.", y=-0.13)

# e) le remplissage selon le grain
ax = fig.add_subplot(gs[1, 1])
ss = np.array([s_ for s_, _, _ in REMP])
ax.semilogx(ss, [100 * n_ / t_ for _, n_, t_ in REMP], "o-", color=F.BLEU, lw=2, label="tout le dessin")
for q_, col in ((0.90, F.RAMPE[1]), (0.97, F.ORANGE), (0.99, ROUGE)):
    ax.semilogx(ss, [100 * n_ / t_ for _, n_, t_ in VEINES[q_]], "s--", color=col, ms=4, lw=1.3,
                label=f"veines : {fr(100 * (1 - q_), '{:.0f}')} % les plus clairs (dimension {fr(DIM_V[q_], '{:.2f}')})")
ax.axvline(math.sqrt(AIRE_PX / V17), color=F.MUTED, ls=":", lw=1.2)
ax.text(math.sqrt(AIRE_PX / V17) * 0.95, 70, "une région\n(7,6 ppm) →", fontsize=8.6, color=F.INK2, ha="right")
ax.set_xlabel("grain : côté de la boîte (pixels)")
ax.set_ylabel("boîtes touchées (%)")
ax.set_ylim(-3, 138)
ax.set_yticks(range(0, 101, 20))
ax.legend(loc="upper center", fontsize=8.2, ncol=1)
ax.set_title("e)  La granularité de ton image")
legende(ax, "On recouvre l'image de boîtes de plus en plus grosses. Le dessin est plein dès 4 à 5 pixels, la taille"
        " d'une région : au-dessus de 7,6 ppm, il a la dimension 2. Les veines claires gardent une dimension proche de 1 :"
        " ce sont des faisceaux de lignes, pas des surfaces comme un arbre de Perron.", y=-0.13)

# f) pixels par croisement selon n
ax = fig.add_subplot(gs[1, 2])
nn = np.array(list(PXC))
ax.semilogy(nn, [PXC[k][0] for k in nn], "o-", color=F.BLEU, lw=2, label="image de 2 000 px")
ax.semilogy(nn, [PXC[k][1] for k in nn], "s-", color=F.ORANGE, lw=2, label="image de 8 000 px")
ax.axhline(1, color=ROUGE, lw=1.2, ls="--")
ax.text(5.2, 1.25, "un pixel par croisement", color=ROUGE, fontsize=8.6)
for k in nn:
    ax.text(k, PXC[k][0] * 1.5, str(k), ha="center", fontsize=8.4, color=F.INK2)
ax.set_xlabel("nombre de courbes n (premier)")
ax.set_ylabel("pixels par croisement")
ax.legend(loc="upper right", fontsize=8.6)
ax.set_title("f)  Une courbe de plus = un cran d'image")
legende(ax, "Chaque courbe double le nombre de croisements : à grain égal, l'image doit gagner √2 en largeur, un cran"
        " de diaphragme. À 2 000 px, 17 courbes donnent 22,6 px par croisement, 19 courbes 5,6 px, et 23 courbes moins d'un"
        " pixel : il faut 8 000 px pour les voir.", y=-0.13)
F.sauver(fig, "ad1_venn_ppm.png")

# --------------------------- ad2 : l'analyse dimensionnelle et les deux ombres ---------------------------
fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.22, hspace=0.38)

# a) le prix de 1 ppm
ax = fig.add_subplot(gs[0, 0])
noms_p = ["Venn (aire)", "Perron", "Venn (longueur)", "série de la chèvre", "ménisque de la chèvre", "diaphragme",
          "plan de la lentille", "équateur"]
vals_p = [PRIX[0][2], PRIX[2][2], PRIX[1][2], PRIX[3][2], PRIX[4][2], PRIX[5][2], PRIX[6][2], PRIX[7][2]]
cols_p = [F.BLEU, F.BLEU, F.RAMPE[1], F.RAMPE[1], F.ORANGE, F.ORANGE, VIOLET, ROUGE]
ax.barh(range(len(vals_p)), vals_p, color=cols_p)
ax.set_xscale("log")
ax.set_yticks(range(len(vals_p)))
ax.set_yticklabels(noms_p)
ax.invert_yaxis()
for i, v_ in enumerate(vals_p):
    ax.text(v_ * 1.3, i, (ent(math.ceil(v_ - 1e-9)) if v_ < 1e5 else (ent(round(v_)) if v_ < 1e7 else petit(v_))),
            va="center", fontsize=8.6, color=F.INK2)
ax.set_xlim(5, 1e15)
ax.set_xlabel("pas nécessaires pour une précision de 1 ppm (courbes, étages, dimensions, lames)")
ax.set_title("a)  Ce que coûte 1 ppm")
legende(ax, "Bleu : un bit par pas (le Venn compté en aire et Perron, 20 pas). Bleu clair : un demi-bit par pas (le Venn"
        " compté en longueur, 40 courbes, et la série de la chèvre, 31 dimensions). Orange : une loi en 1/n² (le ménisque"
        " de la chèvre et le diaphragme, même forme x²/6). Puis le plan de la lentille (ε⁻¹) et l'équateur (ε⁻²) de la"
        " partie XXIII.", y=-0.13)

# b) deux ombres du même cube (k = 6)
ax = fig.add_subplot(gs[0, 1])
k6 = 6
idx = np.arange(2 ** k6)
bits6 = (idx[:, None] >> np.arange(k6)[None, :]) & 1
v6 = 0.5
a6 = 2.0 ** np.arange(k6) * (v6 - np.arange(k6) - 2)
c6 = bits6 @ a6
rk6 = bits6.sum(1)
cmap_rk = LinearSegmentedColormap.from_list("rk", ["#cde2fb", F.BLEU, "#104281"])
c6n = (c6 - c6.min()) / (c6.max() - c6.min())
ax.scatter(c6n, np.full(len(c6n), 1.55), c=rk6, cmap=cmap_rk, s=26, zorder=3, edgecolors="none")
ax.text(0.5, 1.72, "Perron : une direction quelconque (a₀, …, a₅)", fontsize=9, color=F.INK2, ha="center")
ax.text(0.5, 1.38, "64 points tous séparés, en ordre binaire (couleur : nombre de 1)", fontsize=8.4, color=F.MUTED,
        ha="center")
for r_ in range(k6 + 1):
    m_ = rk6 == r_
    ax.scatter(np.full(int(m_.sum()), r_ / k6), 0.05 + 0.04 * np.arange(int(m_.sum())), color=cmap_rk(r_ / k6), s=26,
               zorder=3, edgecolors="none")
    ax.text(r_ / k6, -0.06, f"{comb(k6, r_)}", ha="center", va="top", fontsize=8.8, color=F.INK2)
ax.text(0.5, -0.2, "Venn : la grande diagonale (1, …, 1) — les points s'empilent, C(6, k) par couche", fontsize=9,
        color=F.INK2, ha="center")
ax.set_xlim(-0.06, 1.06)
ax.set_ylim(-0.3, 1.8)
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
for sp_ in ax.spines.values():
    sp_.set_visible(False)
ax.set_title("b)  Deux ombres du même cube {0, 1}⁶")
legende(ax, "En haut, la coupe d'un arbre de Perron (partie XXVIII) : l'ombre du cube sur une direction quelconque, où"
        " chaque sommet a sa place, rangée en binaire. En bas, l'ombre sur la grande diagonale, celle que lit le rayon de"
        " ton image : les sommets s'empilent par nombre de 1, C(n, k) par couche. Même cube, deux regards.", y=-0.03)

# c) l'ombre du cube de dimension 17 dans le plan
ax = fig.add_subplot(gs[0, 2])
ordre = np.argsort(RK)
ax.scatter(OMB.real[ordre], OMB.imag[ordre], c=RK[ordre], cmap=LinearSegmentedColormap.from_list(
    "r17", ["#cde2fb", F.BLEU, "#104281", F.ORANGE]), s=0.15, rasterized=True, edgecolors="none")
ax.add_patch(plt.Polygon(PH, closed=True, fill=False, ec=F.ORANGE, lw=1.4))
F.point(ax, 0, 0, ROUGE, 6)
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
for sp_ in ax.spines.values():
    sp_.set_visible(False)
ax.set_xlim(-6.1, 6.1)
ax.set_ylim(-6.1, 6.1)
ax.text(-6.0, 5.9, "au centre : seulement ∅ et\nles 17 courbes (17 est premier)", fontsize=8.6, color=ROUGE, va="top")
ax.set_title("c)  Le cube de dimension 17, vu dans le plan")
legende(ax, "Chaque région S du Venn devient le point Σ ω^i (i dans S), ω = e^(2iπ/17) : 131 072 points, colorés par"
        " rang. La rotation des étiquettes est la rotation de 2π/17. Le contour est un 34-gone régulier. Le centre ne"
        " reçoit que les deux régions fixes : c'est le théorème de Henderson, lu sur une ombre.", y=-0.02)

# d) Henderson : sommes nulles
ax = fig.add_subplot(gs[1, 0])
nn_ = np.array(list(NUL))
vv_ = np.array([NUL[n] for n in nn_])
cols_h = [F.BLEU if v_ == 0 else F.ORANGE for v_ in vv_]
ax.bar(nn_, vv_ + 1, color=cols_h)
ax.set_yscale("log")
ax.set_xticks(nn_)
ax.set_xlabel("n")
ax.set_ylabel("sous-ensembles propres non vides de somme nulle (+ 1)")
for n, v_ in zip(nn_, vv_):
    if v_ == 0:
        ax.text(n, 1.15, "0", ha="center", fontsize=8.6, color=F.BLEU)
ax.set_title("d)  Henderson par les racines de l'unité")
legende(ax, "Pour n premier (bleu), aucune somme de racines n-ièmes de l'unité, prise sur une partie propre non vide, ne"
        " s'annule : le polynôme 1 + x + … + x^(n−1) est irréductible. Pour n composé (orange), les polygones réguliers"
        " inscrits s'annulent : leur région serait fixée par une rotation, et le Venn symétrique est impossible.", y=-0.13)

# e) le test des coïncidences
ax = fig.add_subplot(gs[1, 1])
tt_ = np.array(TOLS)
zero = [OBS[t_] == 0 for t_ in TOLS]
ax.loglog(tt_ * 1e6, [max(OBS[t_], 0.05) for t_ in TOLS], "-", color=F.BLEU, lw=2)
ax.loglog(tt_[~np.array(zero)] * 1e6, [OBS[t_] for t_, z_ in zip(TOLS, zero) if not z_], "o", color=F.BLEU, ms=7,
          label="coïncidences observées")
ax.loglog(tt_[np.array(zero)] * 1e6, [0.05] * sum(zero), "o", mfc=F.SURF, mec=F.BLEU, ms=7, label="aucune")
ax.loglog(tt_ * 1e6, [max(ATT[t_], 1e-9) for t_ in TOLS], "--", color=F.ORANGE, lw=1.6,
          label="attendues par hasard (catalogue brouillé)")
ax.axvline(1, color=F.MUTED, ls=":", lw=1.2)
ax.text(1.15, 60, "1 ppm", color=F.INK2, fontsize=9)
COURT = {"lumière du 17-gone": ("17-gone", "hasard"), "part des niveaux ≥ 9": ("niveaux ≥ 9", "le complément"),
         "34·tan(π/34)": ("34·tan(π/34)", "polygone → cercle")}
COURT_NOS = {"128/125 (diesis)": "diesis", "1/2": "½", "π": "π"}
txt_ = "Les trois plus proches :\n" + "\n".join(
    f"{fr(e_ * 1e6, '{:.0f}')} ppm : " + (f"{COURT.get(nb, (nb,))[0]} ≈ {COURT_NOS.get(na, na)}" if mode == "="
                                          else f"{COURT.get(nb, (nb,))[0]} × {COURT_NOS.get(na, na)} ≈ 1")
    + f" ({COURT.get(nb, (nb, 'hasard'))[1]})" for e_, na, nb, mode in PAIRES[:3])
ax.text(1.3, 2.6, txt_, fontsize=8, color=F.INK2, va="center", bbox=BOITE)
ax.set_xlabel("tolérance (ppm)")
ax.set_ylabel("nombre de paires")
ax.set_ylim(0.03, 300)
ax.legend(loc="upper left", fontsize=8.4)
ax.set_title("e)  Au ppm, les coïncidences disparaissent")
legende(ax, f"{len(NOS)} constantes de nos parties contre {len(VENN)} nombres du Venn à 17. À 3 % et à 1 %, autant de"
        " rapprochements que le hasard en prévoit (catalogue brouillé). Entre 0,1 et 0,3 % : deux liens expliqués (la"
        " symétrie du complément, le polygone qui tend vers le cercle) et un hasard. En dessous de 100 ppm : aucun.",
        y=-0.13)

# f) le cercle de demi-aire
ax = fig.add_subplot(gs[1, 2])
rr_ = np.r_[RAYON_NIV, 0.0]
for l_ in range(16):
    ax.add_patch(plt.Circle((0, 0), rr_[l_], fc=F.RAMPE[min(4, l_ // 4)] if l_ % 2 else F.SURF, ec=F.GRID, lw=0.4,
                            alpha=0.55))
F.cercle(ax, (0, 0), 1 / R2, color=ROUGE, lw=2, ls="--")
ax.text(0.0, 1 / R2 + 0.03, "R/√2", color=ROUGE, ha="center", fontsize=9.5)
D17 = DEMI["venn17-local-c3-s2.json"]
ax.text(0.0, 0.0, f"niveaux ≥ 9\n{fr(100 * D17, '{:.2f}')} %", ha="center", va="center", fontsize=9.5, color=F.INK)
ax.text(0.0, -0.86, f"niveaux ≤ 8 : {fr(100 * (1 - D17), '{:.2f}')} %", ha="center", fontsize=9.5, color=F.INK)
ax.set_xlim(-1.05, 1.05)
ax.set_ylim(-1.05, 1.05)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("f)  Le cercle de demi-aire coupe ton image en deux")
legende(ax, "Les anneaux de niveaux de l'image, à leurs rayons cibles. Le cercle de rayon R/√2 (le cran de la partie I,"
        " le disque de demi-aire de la partie XVII) sépare les croisements des niveaux 9 à 16 de ceux des niveaux 1 à 8"
        f" : {fr(100 * D17, '{:.2f}')} % et {fr(100 * (1 - D17), '{:.2f}')} %, à {fr(abs(D17 - 0.5) * 1e6, '{:.0f}')} ppm"
        " de la moitié exacte, parce que C(17, l) = C(17, 17 − l).", y=-0.02)
F.sauver(fig, "ad2_deux_ombres.png")
print(f"figures : {time.time() - T1:.1f} s ; total : {time.time() - T0:.1f} s")
