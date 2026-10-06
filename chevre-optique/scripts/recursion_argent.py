"""
Partie XVII : les deux foyers du contact, la récursion d'argent et les anneaux de Newton.

    python3 scripts/recursion_argent.py        # ≈ 10 s

Écrit resultats/recursion_argent.md, figures/q1_recursion_argent.png et figures/q2_newton_polyedres.png.

Le petit disque de rayon 1/√2 (aire π/2, la moitié du pré de rayon 1) glisse le long de l'axe OP, P = (1, 0) étant le
point orange de la partie XVI, où la chèvre est attachée.

1. Les positions exactes : contact intérieur en d = 1 − 1/√2, contact extérieur en d = 1 + 1/√2, tous deux en P.
2. Les jumeaux : deux positions d et 1/(2d) coupent le pré aux mêmes points (forme de Newton x·x' = f², f = 1/√2).
   Le seul jumeau de lui-même, d = 1/√2, coupe à ±45° : la lunule d'Hippocrate, d'aire exactement 1/2.
3. La récursion d'argent T(d) = 2 − 1/(2d) (reflet par le piquet ∘ jumeau) : ses points fixes sont les deux contacts,
   de multiplicateurs (√2 ± 1)². Orbites exactes (nombres de Pell), croisements qui glissent vers P.
4. Les anneaux de Newton aux deux contacts : 1/R_eff = √2 − 1 (intérieur) et √2 + 1 (extérieur).
5. La corde de la chèvre attachée en P, encadrée de façon certaine par arithmétique d'intervalles.
6. Les polyèdres nobles : l'octaèdre (sphère médiane = le petit disque au centre), le cube des ménisques, et le
   disphénoïde de deux aiguilles (le tétraèdre régulier pour deux aiguilles croisées à la hauteur √2).
"""

import logging
import math
import os
import sys
from decimal import ROUND_CEILING, ROUND_FLOOR, Decimal
from fractions import Fraction

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
import sympy as sp
from matplotlib.colors import to_rgba
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpmath import iv
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
ROUGE, VIOLET = "#d0342c", "#7d4fc4"
R2 = math.sqrt(2)
RHO = 1 / R2  # rayon du petit disque : aire π/2
D_INT, D_EXT = 1 - RHO, 1 + RHO  # les deux contacts, tous deux au point orange P = (1, 0)
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.6f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


def lentille(d, r=RHO, R=1.0):
    """Aire commune au pré (rayon R, centre O) et au disque de rayon r centré à la distance d."""
    if d + r <= R:
        return math.pi * r * r
    if d >= R + r:
        return 0.0
    a1 = r * r * math.acos((d * d + r * r - R * R) / (2 * d * r))
    a2 = R * R * math.acos((d * d + R * R - r * r) / (2 * d * R))
    return a1 + a2 - 0.5 * math.sqrt((-d + r + R) * (d + r - R) * (d - r + R) * (d + r + R))


def croisement(d):
    """Demi-angle (en degrés, vu de O) des deux points où le petit cercle coupe le pré ; None s'il ne le coupe pas."""
    c = (d * d + 0.5) / (2 * d)
    return math.degrees(math.acos(c)) if c <= 1 else None


T = lambda d: 2 - 1 / (2 * d)  # reflet par le piquet P (d ↦ 2 − d) après le jumeau (d ↦ 1/(2d))
T_inv = lambda d: 1 / (2 * (2 - d))

# ---------------------------------------------------------------------------
# 1. Les positions exactes
# ---------------------------------------------------------------------------
s2 = sp.sqrt(2)
ligne("## 1. Le petit disque (rayon 1/√2) qui glisse : les positions exactes\n")
ligne("| position | d (exact) | d | ce qui se passe | part du pré couverte |")
ligne("|---|---|---|---|---|")
POS = [("au centre", "0", 0.0, "concentrique : couronne d'épaisseur 1 − 1/√2"),
       ("contact intérieur (point orange)", "1 − 1/√2 = (√2 − 1)/√2", D_INT, "touche le pré en P de l'intérieur"),
       ("jumeau de 30°, côté intérieur", "(√3 − 1)/2", (3 ** 0.5 - 1) / 2, "coupe le pré à ±30°"),
       ("jumeau de lui-même", "1/√2", RHO, "passe par O, coupe le pré à ±45° (lunule d'Hippocrate)"),
       ("jumeau de 30°, côté extérieur", "(√3 + 1)/2", (3 ** 0.5 + 1) / 2, "coupe le pré à ±30°"),
       ("au piquet", "1", 1.0, "centré sur P"),
       ("contact extérieur", "1 + 1/√2 = (√2 + 1)/√2", D_EXT, "touche le pré en P de l'extérieur")]
for nom, ex, d, quoi in POS:
    ligne(f"| {nom} | {ex} | {fr(d)} | {quoi} | {fr(lentille(d) / math.pi)} |")
ligne(f"\nTranslation entre les deux contacts : (1 + 1/√2) − (1 − 1/√2) = √2 = {fr(D_EXT - D_INT)}, le diamètre du petit"
      " disque. Produit des deux contacts : (1 − 1/√2)(1 + 1/√2) = 1/2. Rapport : (√2 + 1)² = 3 + 2√2 = "
      f"{fr(D_EXT / D_INT)}.")
ligne(f"\nAux deux contacts, le petit disque atteint l'axe en 1 − √2 = {fr(1 - R2)} et en 1 + √2 = {fr(1 + R2)} : les deux"
      " disques de contact sont inscrits dans le cercle de centre P et de rayon √2 (la corde de dimension infinie).")
h_aire = lentille(RHO)
ligne(f"\nPosition jumelle d'elle-même (d = 1/√2) : aire commune {fr(h_aire, '{:.12f}')} = π/2 − 1/2 ="
      f" {fr(math.pi / 2 - 0.5, '{:.12f}')}. La part perdue, hors du pré, vaut exactement 1/2 : c'est la lunule"
      " d'Hippocrate, égale au triangle O-X₊-X₋ (base √2, hauteur 1/√2).")

# ---------------------------------------------------------------------------
# 2. Les jumeaux
# ---------------------------------------------------------------------------
ligne("\n## 2. Les jumeaux : deux positions, les mêmes points de croisement\n")
ligne("Le petit cercle coupe le pré aux angles ±θ avec cos θ = (d² + 1/2)/(2d). Pour un même θ < 45°, deux positions"
      " d₁, d₂ conviennent : d₁ + d₂ = 2 cos θ et d₁·d₂ = 1/2. C'est la forme de Newton de l'équation des lentilles,"
      " x·x' = f², avec f = 1/√2.\n")
ligne("| θ | d₁ | d₂ | d₁·d₂ | part couverte en d₁ | en d₂ |")
ligne("|---:|---|---|---|---|---|")
for th in (0, 5, 15, 30, 40, 45):
    c = math.cos(math.radians(th))
    rr = math.sqrt(max(c * c - 0.5, 0.0))
    d1, d2 = c - rr, c + rr
    ligne(f"| {th}° | {fr(d1)} | {fr(d2)} | {fr(d1 * d2)} | {fr(lentille(d1) / math.pi)} | {fr(lentille(d2) / math.pi)} |")
ligne("\nLe petit disque ne coupe jamais le pré au-delà de ±45° : à d = 1/√2, la corde commune est son diamètre.")

# ---------------------------------------------------------------------------
# 3. La récursion d'argent
# ---------------------------------------------------------------------------
ligne("\n## 3. La récursion d'argent T(d) = 2 − 1/(2d)\n")
dd = sp.symbols("d")
Ts = 2 - 1 / (2 * dd)
fixes = sp.solve(sp.Eq(Ts, dd), dd)
ligne("T = (reflet par le piquet P : d ↦ 2 − d) ∘ (jumeau : d ↦ 1/(2d)).")
for p in fixes:
    mult = sp.simplify(sp.diff(Ts, dd).subs(dd, p))
    ligne(f"- point fixe d = {sp.sstr(p)} = {fr(float(p))} ; multiplicateur T'(d) = {sp.sstr(sp.nsimplify(mult))} ="
          f" {fr(float(mult))}")
ligne("\nLes deux points fixes sont exactement les deux contacts : (√2 + 1)² en 1 − 1/√2 (repousse), (√2 − 1)² en"
      " 1 + 1/√2 (attire).")
ligne("\n**L'aller-retour depuis le centre** (reflet R, puis jumeau I, puis R, …), en fractions exactes :\n")
z = [Fraction(0)]
for _ in range(10):
    z.append(2 - z[-1])
    z.append(1 / (2 * z[-1]))
ligne("| étape | position | valeur | côté | écart au contact le plus proche |")
ligne("|---:|---|---|---|---|")
for k, x in enumerate(z[:15]):
    xf = float(x)
    cote = "dans le pré (moitié exacte)" if xf <= D_INT else "hors du pré (rien)"
    ecart = abs(xf - (D_INT if xf <= D_INT else D_EXT))
    ligne(f"| {k} | {x} | {fr(xf, '{:.10f}')} | {cote} | {fr(ecart, '{:.3e}')} |")
INT = z[0::2]
err = [abs(float(x) - D_INT) for x in INT]
ligne("\nÉcarts successifs côté intérieur, rapport d'une étape à l'autre : "
      + " ; ".join(fr(err[i + 1] / err[i], "{:.6f}") for i in range(len(err) - 1))
      + f" → 3 − 2√2 = {fr(3 - 2 * R2, '{:.6f}')}. Chaque aller-retour gagne log₁₀(3 + 2√2) ="
      f" {fr(math.log10(3 + 2 * R2), '{:.4f}')} chiffre.")
P_, H_ = [0, 1], [1, 1]
for _ in range(12):
    P_.append(2 * P_[-1] + P_[-2])
    H_.append(2 * H_[-1] + H_[-2])
ligne(f"\nNombres de Pell : {', '.join(map(str, P_[:11]))} ; compagnons : {', '.join(map(str, H_[:11]))}."
      " Les fractions de l'orbite intérieure sont H/(2P) et P/H : "
      + ", ".join(f"{x}" for x in INT[1:9]) + ".")
ok_pell = all(INT[2 * j + 1] == Fraction(H_[2 * j + 1], 2 * P_[2 * j + 2]) and
              INT[2 * j + 2] == Fraction(P_[2 * j + 2], H_[2 * j + 3]) for j in range(4))
ligne(f"Vérification (8 premiers termes) : {'oui' if ok_pell else 'NON'}.")
w0 = (sp.Integer(0) - fixes[0]) / (sp.Integer(0) - fixes[1])
ligne(f"\nForme close : avec w = (d − (1 − 1/√2))/(d − (1 + 1/√2)), chaque pas de T⁻¹ multiplie w par 3 − 2√2. Depuis"
      f" d = 0 : w₀ = {sp.sstr(sp.nsimplify(sp.simplify(w0)))}, donc la k-ième position est connue exactement sans calculer"
      " les précédentes.")

ligne("\n**Dans la zone de croisement**, depuis le jumeau de lui-même d = 1/√2 :\n")
ligne("| k | Tᵏ(1/√2) | T⁻ᵏ(1/√2) | produit | angle de croisement | rapport à l'angle précédent |")
ligne("|---:|---|---|---|---|---|")
a_, b_ = RHO, RHO
ANG = []
prev = None
for k in range(9):
    th = croisement(a_)
    ANG.append(th)
    ligne(f"| {k} | {fr(a_)} | {fr(b_)} | {fr(a_ * b_)} | {fr(th, '{:.4f}')}° |"
          f" {fr(th / prev, '{:.5f}') if prev else '—'} |")
    prev = th
    a_, b_ = T(a_), T_inv(b_)
ligne(f"\nÀ chaque pas, les deux jumeaux coupent le pré aux mêmes points, qui glissent vers P ; l'angle est divisé par"
      f" √2 + 1 (rapport → √2 − 1 = {fr(R2 - 1, '{:.5f}')}).")

# ---------------------------------------------------------------------------
# 4. Les anneaux de Newton
# ---------------------------------------------------------------------------
ligne("\n## 4. Les anneaux de Newton aux deux contacts\n")
ligne("Lame entre les deux surfaces près du contact (flèches exactes, s_a(x) = a − √(a² − x²)) : intérieur"
      " t = s_{1/√2} − s_1 ; extérieur t = s_{1/√2} + s_1. Au premier ordre t ≈ x²/(2R_eff) avec 1/R_eff = √2 ∓ 1.\n")
LAM = 1e-3
ligne(f"| anneau sombre m (λ = {fr(LAM, '{:g}')} R) | rayon, contact intérieur | contact extérieur | rapport | approx. √(mλR_eff) int. | ext. |")
ligne("|---:|---|---|---|---|---|")
fl = lambda a, x: a - math.sqrt(a * a - x * x)
t_int = lambda x: fl(RHO, x) - fl(1.0, x)
t_ext = lambda x: fl(RHO, x) + fl(1.0, x)
for m in (1, 2, 3, 5, 10, 30):
    ri = brentq(lambda x: 2 * t_int(x) - m * LAM, 1e-12, 0.7)
    re_ = brentq(lambda x: 2 * t_ext(x) - m * LAM, 1e-12, 0.7)
    ligne(f"| {m} | {fr(ri)} | {fr(re_)} | {fr(ri / re_, '{:.4f}')} | {fr(math.sqrt(m * LAM / (R2 - 1)))} |"
          f" {fr(math.sqrt(m * LAM / (R2 + 1)))} |")
ligne(f"\nRapport limite des rayons : √((√2 + 1)/(√2 − 1)) = √2 + 1 = {fr(R2 + 1)} ; rapport des aires entre deux"
      f" anneaux : (√2 + 1)² = {fr((R2 + 1) ** 2)}.")
ligne(f"Au centre (d = 0), la lame est une couronne d'épaisseur constante 1 − 1/√2 = {fr(1 - RHO)} : une teinte uniforme,"
      " sans anneaux.")
ligne("\nExemple physique : pré de rayon 100 mm, petit disque de 70,7 mm, lumière du sodium (589 nm) : premier anneau"
      f" sombre à {fr(math.sqrt(589e-6 * 100 / (R2 - 1)), '{:.3f}')} mm au contact intérieur et à"
      f" {fr(math.sqrt(589e-6 * 100 / (R2 + 1)), '{:.3f}')} mm au contact extérieur.")

# ---------------------------------------------------------------------------
# 5. La corde de la chèvre attachée en P, certifiée
# ---------------------------------------------------------------------------
ligne("\n## 5. La chèvre attachée au point orange : une corde certifiée\n")
ligne("Avec le pré de rayon 1 et le piquet sur le bord, la corde vaut r = 2 cos(α/2), où α vérifie"
      " g(α) = sin α − α cos α − π/2 = 0. g est croissante sur ]0 ; π[ (g' = α sin α > 0).")
iv.dps = 40
mp.mp.dps = 50
alpha = mp.findroot(lambda a: mp.sin(a) - a * mp.cos(a) - mp.pi / 2, 1.9)
g_iv = lambda a: iv.sin(iv.mpf(a)) - iv.mpf(a) * iv.cos(iv.mpf(a)) - iv.pi / 2
ENC = []


def borne(x, sens, chiffres=25):
    """Borne décimale sûre d'un intervalle : arrondie vers le bas (sens = −1) ou vers le haut (sens = +1)."""
    bas_, haut_ = str(x).strip("[]").split(",")
    v = Decimal(bas_.strip() if sens < 0 else haut_.strip())
    return v.quantize(Decimal(1).scaleb(-chiffres), rounding=ROUND_FLOOR if sens < 0 else ROUND_CEILING)


for eps in ("1e-12", "1e-25"):
    lo = mp.nstr(alpha - mp.mpf(eps), 45)
    hi = mp.nstr(alpha + mp.mpf(eps), 45)
    glo, ghi = g_iv(lo), g_iv(hi)
    certifie = bool(glo.b < 0) and bool(ghi.a > 0)
    r_lo = borne(2 * iv.cos(iv.mpf(hi) / 2), -1)
    r_hi = borne(2 * iv.cos(iv.mpf(lo) / 2), +1)
    ENC.append((eps, certifie, r_lo, r_hi))
    ligne(f"- α entre {lo[:28].replace('.', ',')}… et {hi[:28].replace('.', ',')}… : g(bas) ≤ {fr(float(glo.b), '{:.2e}')} < 0 et g(haut) ≥"
          f" {fr(float(ghi.a), '{:.2e}')} > 0 (calcul par intervalles), certifié : {'oui' if certifie else 'NON'}.")
    ligne(f"  Donc r ∈ [{str(r_lo).replace('.', ',')} ; {str(r_hi).replace('.', ',')}].")
ligne(f"\nValeur : r = {mp.nstr(2 * mp.cos(alpha / 2), 30).replace('.', ',')}…")
ligne("La plus grande corde de la récursion qui broute exactement la moitié est 1/√2 (contact intérieur) ; au-delà, la"
      " chèvre doit allonger sa corde (partie XVI).")

# ---------------------------------------------------------------------------
# 6. Les polyèdres nobles
# ---------------------------------------------------------------------------
ligne("\n## 6. Les polyèdres nobles\n")
ligne(f"- Octaèdre inscrit dans le pré (sommets (±1, 0, 0)…) : arêtes √2 (diagonales 1x, 1y), rayon de la sphère médiane"
      f" {fr(np.linalg.norm([0.5, 0.5, 0]))} = 1/√2. Le petit disque au centre est cette sphère médiane ; il touche les"
      " 12 arêtes en leurs milieux (les sommets du cuboctaèdre). En 2D : le cercle inscrit du carré des diagonales 1x, 1y.")
cap = (1 - RHO) / 2
rng = np.random.default_rng(0)
X = rng.standard_normal((2_000_000, 3))
X /= np.linalg.norm(X, axis=1, keepdims=True)
mc = (np.abs(X).max(1) >= RHO).mean()
double = ((np.abs(X) >= RHO).sum(1) >= 2).mean()
ligne(f"- Six petits disques à la position d'Hippocrate (d = 1/√2, sur ±x, ±y, ±z) : chacun coupe la sphère du pré"
      f" selon une calotte de 45°. Elles se touchent deux à deux (axes à 90°), sans se chevaucher (Monte-Carlo :"
      f" {fr(double, '{:.4f}')}). Elles couvrent 6 × (1 − 1/√2)/2 = 3 − 3/√2 = {fr(6 * cap, '{:.6f}')} de la sphère"
      f" (Monte-Carlo : {fr(mc, '{:.6f}')}). Restent 8 ménisques triangulaires, centrés sur les sommets du cube, soit"
      f" (3√2 − 4)/2 = {fr(1 - 6 * cap, '{:.6f}')}, de rayon angulaire arccos(1/√3) − 45° ="
      f" {fr(math.degrees(math.acos(1 / 3 ** 0.5)) - 45, '{:.4f}')}°.")
ligne("- En 2D, quatre disques d'Hippocrate (±x, ±y) pavent exactement la circonférence : quatre arcs de 90° qui se"
      " touchent aux diagonales 1x, 1y. Pas de ménisque en 2D ; les ménisques naissent en 3D.\n")
ligne("**Deux aiguilles font toujours un polyèdre noble.** Une aiguille de longueur 2 centrée sur l'axe vertical, à la"
      " hauteur h, et la même tournée de α, à la hauteur −h : leurs quatre bouts forment un tétraèdre dont les arêtes"
      " opposées sont égales deux à deux, donc aux quatre faces égales (un disphénoïde, polyèdre noble).\n")
ligne("| α | h | côtés d'une face | quatre faces égales ? |")
ligne("|---:|---|---|---|")


def disphenoide(alpha, h, a=1.0):
    V = np.array([[a, 0, h], [-a, 0, h], [a * math.cos(alpha), a * math.sin(alpha), -h],
                  [-a * math.cos(alpha), -a * math.sin(alpha), -h]])
    faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    cotes = [tuple(sorted(round(float(np.linalg.norm(V[i] - V[j])), 9) for i, j in ((f[0], f[1]), (f[1], f[2]),
                                                                                     (f[0], f[2])))) for f in faces]
    return V, cotes


for al, h in ((90, RHO), (90, 0.3), (45, 0.5), (45, 1e-6), (60, 0.8), (30, 1.2)):
    _, c = disphenoide(math.radians(al), h)
    ligne(f"| {al}° | {fr(h, '{:.4g}')} | {', '.join(fr(x, '{:.6f}') for x in c[0])} | {'oui' if len(set(c)) == 1 else 'NON'} |")
ligne("\nPour α = 90° et 2h = √2 (les deux aiguilles séparées d'une diagonale 1x, 1y), c'est le tétraèdre régulier"
      " d'arête 2 : le simplexe de la grille décalée en 3D (parties XV et XVI).")
ligne(f"Pour α = 45° (la première bissection de l'arbre de Perron sur l'angle droit), les arêtes latérales aplaties valent"
      f" 2 sin 22,5° et 2 cos 22,5° : leur rapport est tan 22,5° = √2 − 1 = {fr(R2 - 1)}.")

with open(os.path.join(ICI, "..", "resultats", "recursion_argent.md"), "w") as fh:
    fh.write("# Résultats de la partie XVII (générés par scripts/recursion_argent.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure 1 : les deux foyers et la récursion d'argent
# ===========================================================================
ORANGE = F.ORANGE


def pre(ax, x0=-1.6, x1=3.0):
    t = np.linspace(0, 2 * np.pi, 500)
    ax.fill(np.cos(t), np.sin(t), color=F.SEQ[1], zorder=0)
    ax.plot(np.cos(t), np.sin(t), color=F.INK, lw=1.6, zorder=3)
    ax.plot([x0, x1], [0, 0], color=F.GRID, lw=0.8, zorder=0)
    F.point(ax, 0, 0, F.INK, 5)
    ax.text(-0.05, -0.08, "O", fontsize=10, ha="right", va="top")


def schema(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")


def contact(ax, x, y, c=ORANGE, ms=9):
    ax.plot([x], [y], "o", ms=ms, color=c, mec=F.SURF, mew=1.5, zorder=9)


BOITE = dict(fc=F.SURF, ec="none", alpha=0.88, pad=0.5)
fig = plt.figure(figsize=(21, 14.2))
gs = fig.add_gridspec(2, 3, wspace=0.13, hspace=0.2)

# a) les deux foyers
ax = fig.add_subplot(gs[0, 0])
pre(ax)
ax.add_patch(Polygon([(1, 0), (0, 1), (-1, 0), (0, -1)], closed=True, fc="none", ec=F.INK2, lw=1.0, ls="--", zorder=2))
F.cercle(ax, (0, 0), RHO, color=F.BLEU, lw=1.2, ls="--", zorder=4)
F.cercle(ax, (D_INT, 0), RHO, color=F.BLEU, lw=2.4, zorder=5)
F.cercle(ax, (D_EXT, 0), RHO, color=ROUGE, lw=2.4, zorder=5)
F.cercle(ax, (1, 0), R2, color=F.INK, lw=1.0, ls=":", zorder=4)
for x, c in ((D_INT, F.BLEU), (D_EXT, ROUGE)):
    F.point(ax, x, 0, c, 5)
for x in (1 - R2, 1 + R2):
    F.point(ax, x, 0, F.INK, 5)
contact(ax, 1, 0)
ax.text(1.05, 0.08, "P", fontsize=11, fontweight="bold")
ax.text(D_INT, -0.12, "1 − 1/√2", fontsize=8.6, color=F.BLEU, ha="center", va="top", bbox=BOITE, zorder=7)
ax.text(D_EXT, -0.12, "1 + 1/√2", fontsize=8.6, color=ROUGE, ha="center", va="top", bbox=BOITE, zorder=7)
ax.text(1 - R2, 0.1, "1 − √2", fontsize=8.6, ha="center", va="bottom", bbox=BOITE, zorder=7)
ax.text(1 + R2, 0.1, "1 + √2", fontsize=8.6, ha="center", va="bottom", bbox=BOITE, zorder=7)
ax.annotate("", (D_EXT, -0.52), (D_INT, -0.52), arrowprops=dict(arrowstyle="<->", color=F.INK, lw=1.0))
ax.text(1, -0.56, "translation entre les deux foyers : √2", fontsize=8.6, ha="center", va="top", bbox=BOITE, zorder=7)
ax.text(-1.55, -1.52, "Bleu : contact intérieur (le point orange, début de la chèvre). Rouge : contact\nextérieur"
        " (séparation complète). Pointillé : cercle de centre P et de rayon √2\n(la corde de dimension infinie)."
        " Tirets : le petit disque au centre, cercle\ninscrit du carré des diagonales 1x, 1y.", fontsize=8.3,
        color=F.INK2, va="top")
schema(ax, (-1.6, 2.6), (-2.2, 1.5))
ax.set_title("a)  Les deux foyers : deux contacts au même point P")

# b) les jumeaux et la lunule d'Hippocrate
ax = fig.add_subplot(gs[0, 1])
pre(ax, x1=2.0)
xs = np.linspace(RHO, RHO + RHO, 300)  # moitié droite du petit cercle : la lunule hors du pré
yh = np.sqrt(np.clip(RHO ** 2 - (xs - RHO) ** 2, 0, None))
yp = np.sqrt(np.clip(1 - xs ** 2, 0, None))
ax.fill_between(xs, np.minimum(yp, yh), yh, color=F.JAUNE, alpha=0.55, lw=0, zorder=2)
ax.fill_between(xs, -yh, -np.minimum(yp, yh), color=F.JAUNE, alpha=0.55, lw=0, zorder=2)
ax.add_patch(Polygon([(0, 0), (RHO, RHO), (RHO, -RHO)], closed=True, fc=F.JAUNE, alpha=0.3, ec="#a86f00", lw=1.0,
                     zorder=2))
F.cercle(ax, (RHO, 0), RHO, color="#a86f00", lw=2.2, zorder=5)
for th, c in ((15, VIOLET), (30, F.AQUA)):
    cth = math.cos(math.radians(th))
    rr = math.sqrt(cth * cth - 0.5)
    for d_, ls in ((cth - rr, "-"), (cth + rr, "--")):
        F.cercle(ax, (d_, 0), RHO, color=c, lw=1.6, ls=ls, zorder=4)
        F.point(ax, d_, 0, c, 4)
    for sg in (1, -1):
        F.point(ax, cth, sg * math.sin(math.radians(th)), c, 7)
for sg in (1, -1):
    F.point(ax, RHO, sg * RHO, "#a86f00", 8)
contact(ax, 1, 0, ms=7)
ax.text(0.27, 0.12, "triangle\naire ½", fontsize=8.4, color="#7a5200", ha="center", zorder=7)
ax.text(1.32, 0.66, "lunule\naire ½", fontsize=8.4, color="#7a5200", ha="center", zorder=7)
ax.text(RHO + 0.03, RHO + 0.08, "45°", fontsize=8.6, color="#a86f00")
ax.text(-1.55, 1.42, "Deux positions d et 1/(2d) coupent le pré aux mêmes points\n(violet : ±15°, vert : ±30° ; trait"
        " plein et tirets = les deux\njumeaux). Seule d = 1/√2 est son propre jumeau : elle coupe\nà ±45° et perd"
        " exactement la lunule d'Hippocrate, d'aire ½.", fontsize=8.3, color=F.INK2, va="top")
schema(ax, (-1.6, 2.6), (-2.2, 1.5))
ax.set_title("b)  Les jumeaux, et la lunule d'Hippocrate à 45°")

# c) l'aller-retour depuis le centre : un escalier entre les deux foyers
ax = fig.add_subplot(gs[0, 2])
NZ = 15
zf = [float(x) for x in z[:NZ]]
ax.axhspan(-0.05, D_INT, color=F.SEQ[1], zorder=0)
ax.axhspan(D_EXT, 2.7, color="#f6dcd8", zorder=0)
ax.axhline(D_INT, color=F.BLEU, lw=1.3, ls="--")
ax.axhline(D_EXT, color=ROUGE, lw=1.3, ls="--")
ax.axhline(1, color=F.ORANGE, lw=0.9, ls=":")
ax.axhline(RHO, color="#a86f00", lw=0.9, ls=":")
ax.plot(range(NZ), zf, color=F.MUTED, lw=1.0, zorder=2)
for k, x in enumerate(zf):
    ax.plot([k], [x], "o" if x <= D_INT else "s", ms=7, color=F.BLEU if x <= D_INT else ROUGE, mec=F.SURF, mew=1.2,
            zorder=5)
for k in range(9):
    x = zf[k]
    ax.text(k + 0.15, x + (0.06 if x > 1 else -0.06), str(z[k]), fontsize=8.4, va="bottom" if x > 1 else "top",
            ha="left", color=F.INK, bbox=dict(fc=F.SURF, ec="none", alpha=0.8, pad=0.3), zorder=7)
ax.text(14.2, D_INT - 0.03, "foyer intérieur 1 − 1/√2\n(dans le pré : la moitié exacte)", fontsize=8.5, color=F.BLEU,
        ha="right", va="top")
ax.text(14.2, D_EXT + 0.03, "foyer extérieur 1 + 1/√2\n(hors du pré : rien)", fontsize=8.5, color=ROUGE, ha="right",
        va="bottom")
ax.text(14.2, 1.02, "P : reflet d ↦ 2 − d", fontsize=8.3, color=F.ORANGE, ha="right", va="bottom")
ax.text(14.2, RHO + 0.02, "1/√2 : jumeau d ↦ 1/(2d)", fontsize=8.3, color="#a86f00", ha="right", va="bottom")
ax.text(7.5, 2.6, "Depuis le petit disque au centre (d = 0), on alterne le reflet par\nle piquet et le jumeau :"
        " 0 → 2 → 1/4 → 7/4 → 2/7 → 12/7 → …\nChaque aller-retour divise l'écart par (√2 + 1)² = 5,83.",
        fontsize=8.4, color=F.INK2, va="top", ha="center", bbox=dict(fc=F.SURF, ec="none", alpha=0.9, pad=2))
ax.set_xlim(-0.5, 14.5)
ax.set_ylim(-0.05, 2.65)
ax.set_xlabel("étape")
ax.set_ylabel("d : position du centre du petit disque")
ax.set_title("c)  La récursion d'argent : allers-retours entre les foyers")

# d) les croisements glissent vers P
ax = fig.add_subplot(gs[1, 0])
pre(ax, x0=-0.3, x1=1.9)
a_, b_ = RHO, RHO
cols = [F.SEQ[13], F.SEQ[11], F.SEQ[9], F.SEQ[7], F.SEQ[5]]
for k in range(5):
    th = croisement(a_)
    c = cols[k]
    if k < 4:
        F.cercle(ax, (a_, 0), RHO, color=c, lw=1.4, zorder=4)
        if k:
            F.cercle(ax, (b_, 0), RHO, color=c, lw=1.4, ls="--", zorder=4)
    for sg in (1, -1):
        F.point(ax, math.cos(math.radians(th)), sg * math.sin(math.radians(th)), c, 8)
    if k < 4:
        yy = math.sin(math.radians(th))
        ax.annotate(f"k = {k} : {fr(th, '{:.2f}')}°", (math.cos(math.radians(th)), yy), (1.45, 1.25 - 0.22 * k),
                    fontsize=8.4, color=c, va="center", arrowprops=dict(arrowstyle="-", color=c, lw=0.7),
                    bbox=BOITE, zorder=8)
    a_, b_ = T(a_), T_inv(b_)
contact(ax, 1, 0)
ax.text(-0.25, 1.72, "Depuis d = 1/√2 (45°), chaque pas de T (trait plein) et de T⁻¹ (tirets)\ndonne deux jumeaux qui"
        " coupent le pré aux mêmes points.\nCes points glissent vers P : l'angle est divisé par √2 + 1 à chaque pas.",
        fontsize=8.3, color=F.INK2, va="top")
schema(ax, (-0.3, 2.6), (-1.25, 1.75))
ax.set_title("d)  Les croisements glissent vers le point orange")

# e) la convergence
ax = fig.add_subplot(gs[1, 1])
kk = np.arange(len(INT))
ax.semilogy(kk, [abs(float(x) - D_INT) for x in INT], "o-", color=F.BLEU, label="écart au foyer intérieur (orbite depuis 0)")
EXT = [z[k] for k in range(1, len(z), 2)]
ax.semilogy(np.arange(1, len(EXT) + 1), [abs(float(x) - D_EXT) for x in EXT], "s-", color=ROUGE,
            label="écart au foyer extérieur (orbite depuis 2)")
ax.semilogy(np.arange(len(ANG)), ANG, "^-", color=F.ORANGE, label="angle de croisement (degrés), depuis 45°")
ax.semilogy(kk, 0.15 * (3 - 2 * R2) ** kk, color=F.INK, lw=0.9, ls="--", label="pente (√2 − 1)² = 3 − 2√2")
ax.semilogy(np.arange(len(ANG)), 30 * (R2 - 1) ** np.arange(len(ANG)), color=F.INK2, lw=0.9, ls=":",
            label="pente √2 − 1")
ax.set_xlabel("étape k")
ax.set_ylabel("écart (échelle log)")
ax.legend(loc="lower left", fontsize=8.2, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("e)  Certitude : chaque pas gagne 0,77 chiffre")

# f) les jumeaux en coordonnées (d, ρ) : courbe d·d' = 1/2
ax = fig.add_subplot(gs[1, 2])
th = np.linspace(0, 45, 400)
c_ = np.cos(np.radians(th))
rr_ = np.sqrt(np.clip(c_ * c_ - 0.5, 0, None))
ax.plot(c_ - rr_, th, color=F.BLEU, lw=2.2, label="jumeau intérieur d₁")
ax.plot(c_ + rr_, th, color=ROUGE, lw=2.2, label="jumeau extérieur d₂ = 1/(2d₁)")
ax.axvline(RHO, color="#a86f00", lw=1.0, ls=":")
ax.text(RHO + 0.02, 46.5, "d = 1/√2 : 45°, Hippocrate", fontsize=8.4, color="#a86f00")
for x, c in ((D_INT, F.BLEU), (D_EXT, ROUGE)):
    ax.plot([x], [0], "D", ms=9, color=c, mec=F.SURF, mew=1.3, zorder=6, clip_on=False)
for k, (x, y) in enumerate(zip([RHO], [45])):
    ax.plot([x], [y], "*", ms=14, color="#a86f00", mec=F.SURF, zorder=6)
for th_, cc in ((15, VIOLET), (30, F.AQUA)):
    cth = math.cos(math.radians(th_))
    rr = math.sqrt(cth * cth - 0.5)
    ax.plot([cth - rr, cth + rr], [th_, th_], color=cc, lw=1.2, ls="--")
    ax.plot([cth - rr, cth + rr], [th_, th_], "o", color=cc, ms=6)
ax.text(1.02, 16.5, "±15°", fontsize=8.4, color=VIOLET)
ax.text(0.9, 31.5, "±30° : (√3 ∓ 1)/2", fontsize=8.4, color="#0f7d57")
ax.set_xlim(0.2, 1.8)
ax.set_ylim(0, 52)
ax.set_xlabel("d : position du centre")
ax.set_ylabel("demi-angle de croisement θ (degrés)")
ax.legend(loc="upper right", fontsize=8.3, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.text(0.22, 3.0, "◆ les deux foyers (θ = 0, au point orange)\nd₁ + d₂ = 2 cos θ ; d₁·d₂ = 1/2 (Newton : x·x' = f²)",
        fontsize=8.3, color=F.INK2)
ax.set_title("f)  Les jumeaux : la forme de Newton x·x' = f²")
F.sauver(fig, "q1_recursion_argent.png")

# ===========================================================================
# Figure 2 : les anneaux de Newton et les polyèdres nobles
# ===========================================================================
fig = plt.figure(figsize=(20, 12.6))
gs = fig.add_gridspec(2, 3, wspace=0.14, hspace=0.16)


def anneaux(ax, lame, titre, sous_titre, rmax=0.16, lam=2e-3):
    n = 700
    u = np.linspace(-rmax, rmax, n)
    XX, YY = np.meshgrid(u, u)
    rho_ = np.hypot(XX, YY)
    t_ = lame(np.clip(rho_, 0, 0.69))
    I = np.sin(2 * np.pi * t_ / lam) ** 2  # réflexion : sombre là où 2t = mλ
    I[rho_ > rmax] = np.nan
    cmap = plt.get_cmap("YlOrBr_r").copy()
    cmap.set_bad(F.SURF)
    ax.imshow(I, extent=(-rmax, rmax, -rmax, rmax), cmap=cmap, vmin=-0.15, vmax=1.05, origin="lower")
    ax.set_title(titre, fontsize=10.5)
    ax.text(0, -rmax * 1.12, sous_titre, fontsize=8.6, ha="center", va="top", color=F.INK2)
    ax.axis("off")
    ax.set_xlim(-rmax, rmax)
    ax.set_ylim(-rmax * 1.4, rmax)


sub = gs[0, :2].subgridspec(1, 3, wspace=0.05)
ax = fig.add_subplot(sub[0, 0])
anneaux(ax, lambda x: np.full_like(x, 1 - RHO), "au centre", "lame uniforme 1 − 1/√2 :\nteinte plate, pas d'anneaux")
ax = fig.add_subplot(sub[0, 1])
anneaux(ax, lambda x: (RHO - np.sqrt(RHO ** 2 - x ** 2)) - (1 - np.sqrt(1 - x ** 2)), "contact intérieur (orange)",
        "ménisque : 1/R_eff = √2 − 1\nanneaux larges")
ax = fig.add_subplot(sub[0, 2])
anneaux(ax, lambda x: (RHO - np.sqrt(RHO ** 2 - x ** 2)) + (1 - np.sqrt(1 - x ** 2)), "contact extérieur (rouge)",
        "dos à dos : 1/R_eff = √2 + 1\nanneaux √2 + 1 fois plus serrés")
fig.text(0.13, 0.93, "a)  Les anneaux de Newton aux deux foyers (mêmes λ, même échelle)", fontsize=11.5, fontweight="bold")

# b) rayons des anneaux
ax = fig.add_subplot(gs[0, 2])
LAMF = 2e-4
ms_ = np.arange(1, 31)
ri = np.array([brentq(lambda x: 2 * t_int(x) - m * LAMF, 1e-12, 0.7) for m in ms_])
re_ = np.array([brentq(lambda x: 2 * t_ext(x) - m * LAMF, 1e-12, 0.7) for m in ms_])
ax.plot(ms_, ri, "o", ms=4, color=F.BLEU, label="contact intérieur")
ax.plot(ms_, re_, "s", ms=4, color=ROUGE, label="contact extérieur")
ax.plot(ms_, np.sqrt(ms_ * LAMF * (R2 + 1)), color=F.BLEU, lw=0.9)
ax.plot(ms_, np.sqrt(ms_ * LAMF * (R2 - 1)), color=ROUGE, lw=0.9)
ax2 = ax.twinx()
ax2.plot(ms_, ri / re_, color=F.INK, lw=1.6, label="rapport des rayons")
ax2.axhline(R2 + 1, color=F.INK, lw=0.8, ls=":")
ax2.text(2, R2 + 1 + 0.0015, "√2 + 1", fontsize=8.6)
ax2.set_ylim(2.38, 2.42)
ax2.set_ylabel("rapport des rayons")
ax2.grid(False)
ax2.spines["right"].set_visible(True)
ax.set_xlabel(f"numéro m de l'anneau sombre (λ = {fr(LAMF, '{:g}')} R)")
ax.set_ylabel("rayon de l'anneau (unités de R)")
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, loc="center right", fontsize=8.3, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("b)  Rayons des anneaux : √(mλR_eff), rapport √2 + 1")


def sphere_fil(ax, r=1.0, c=F.BASE, lw=0.5, n=13):
    u = np.linspace(0, 2 * np.pi, 120)
    for v in np.linspace(-np.pi / 2, np.pi / 2, n):
        ax.plot(r * np.cos(u) * np.cos(v), r * np.sin(u) * np.cos(v), r * np.sin(v) * np.ones_like(u), color=c, lw=lw)
    for w in np.linspace(0, np.pi, n):
        ax.plot(r * np.cos(w) * np.cos(u), r * np.sin(w) * np.cos(u), r * np.sin(u), color=c, lw=lw)


def cadre3d(ax, lim=1.05, elev=20, azim=32):
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_box_aspect((1, 1, 1), zoom=1.3)
    ax.set_axis_off()
    ax.view_init(elev=elev, azim=azim)


# c) l'octaèdre et sa sphère médiane
ax = fig.add_subplot(gs[1, 0], projection="3d")
sphere_fil(ax, 1.0, F.GRID, 0.4)
uu, vv = np.meshgrid(np.linspace(0, 2 * np.pi, 60), np.linspace(0, np.pi, 30))
ax.plot_surface(RHO * np.cos(uu) * np.sin(vv), RHO * np.sin(uu) * np.sin(vv), RHO * np.cos(vv), color=F.BLEU, alpha=0.18,
                lw=0)
S6 = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], float)
for i in range(6):
    for j in range(i + 1, 6):
        if abs(np.dot(S6[i], S6[j])) < 1e-9:
            ax.plot(*zip(S6[i], S6[j]), color=F.INK, lw=1.3)
            m_ = (S6[i] + S6[j]) / 2
            ax.scatter(*m_, color=F.ORANGE, s=22, depthshade=False)
ax.scatter(*S6.T, color=F.INK, s=18, depthshade=False)
cadre3d(ax)
ax.set_title("c)  L'octaèdre : ses arêtes sont des diagonales 1x, 1y,\nle petit disque au centre est sa sphère médiane",
             fontsize=10.5)
ax.text2D(0.02, 0.02, "points orange : les 12 contacts (milieux des arêtes,\nsommets du cuboctaèdre)", fontsize=8.4,
          color=F.INK2, transform=ax.transAxes)

# d) les six calottes de 45° et les huit ménisques, vus le long de la diagonale (1, 1, 1) (projection orthographique)
ax = fig.add_subplot(gs[1, 1])
e3 = np.array([1, 1, 1]) / math.sqrt(3)  # direction de vue
e1 = np.array([-1, 1, 0]) / math.sqrt(2)  # vers la droite
e2 = np.array([-1, -1, 2]) / math.sqrt(6)  # vers le haut : +z en haut
npx = 900
u = np.linspace(-1, 1, npx)
UU, VV = np.meshgrid(u, u)
W2 = 1 - UU ** 2 - VV ** 2
dedans = W2 >= 0
PTS = (UU[..., None] * e1 + VV[..., None] * e2 + np.sqrt(np.clip(W2, 0, None))[..., None] * e3)
A = np.abs(PTS)
img = np.ones(UU.shape + (4,))
img[..., :3] = to_rgba(F.SURF)[:3]
couleurs_axes = [to_rgba(F.BLEU, 1.0), to_rgba(F.AQUA, 1.0), to_rgba(VIOLET, 1.0)]
idx = np.argmax(A, axis=2)
for k_ in range(3):
    m_ = dedans & (idx == k_)
    img[m_] = couleurs_axes[k_]
img[dedans & (A.max(axis=2) < RHO)] = to_rgba(F.ORANGE, 1.0)
lum = 0.55 + 0.45 * np.sqrt(np.clip(W2, 0, None))  # léger ombrage
img[..., :3] = np.where(dedans[..., None], img[..., :3] * lum[..., None] + (1 - lum[..., None]) * 0.98, img[..., :3])
ax.imshow(img, extent=(-1, 1, -1, 1), origin="lower", interpolation="bilinear")
t_ = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(t_), np.sin(t_), color=F.INK, lw=1.2)
proj = lambda v: (np.dot(v, e1), np.dot(v, e2), np.dot(v, e3))
cube = np.array([[x, y, zc] for x in (-1, 1) for y in (-1, 1) for zc in (-1, 1)]) / math.sqrt(3)
for v in cube:
    x_, y_, z_ = proj(v)
    if z_ > 0:
        ax.plot([x_], [y_], "o", ms=6, color=F.INK, mec=F.SURF, mew=1.0, zorder=5)
for v in [np.array(c_) / math.sqrt(2) for c_ in ((1, 1, 0), (1, 0, 1), (0, 1, 1), (1, -1, 0), (-1, 1, 0), (1, 0, -1),
                                                 (-1, 0, 1), (0, 1, -1), (0, -1, 1))]:
    x_, y_, z_ = proj(v)
    if z_ > 0:
        ax.plot([x_], [y_], "o", ms=5, color="white", mec=F.INK, mew=0.8, zorder=5)
for v, nom in ((np.array([1.0, 0, 0]), "+x"), (np.array([0, 1.0, 0]), "+y"), (np.array([0, 0, 1.0]), "+z")):
    x_, y_, _ = proj(v)
    ax.text(x_, y_, nom, color="white", fontsize=10, fontweight="bold", ha="center", va="center", zorder=6)
ax.set_xlim(-1.05, 1.05)
ax.set_ylim(-1.32, 1.05)
ax.set_aspect("equal")
ax.axis("off")
ax.text(0, -1.1, "noir : les ménisques (sommets du cube) ; blanc : les contacts (cuboctaèdre)\ncalottes : 3 − 3/√2 = 87,9 %"
        " de la sphère ; ménisques : (3√2 − 4)/2 = 12,1 %", fontsize=8.4, color=F.INK2, ha="center", va="top")
ax.set_title("d)  Six disques d'Hippocrate (±x, ±y, ±z) : six calottes\nde 45° qui se touchent, huit ménisques (le cube)",
             fontsize=10.5)

# e) deux aiguilles : le disphénoïde et le tétraèdre régulier
ax = fig.add_subplot(gs[1, 2], projection="3d")
for (al, h, c, dx) in ((90, RHO, F.BLEU, -1.25), (45, 0.5, F.JAUNE, 1.25)):
    V, _ = disphenoide(math.radians(al), h)
    V = V + np.array([dx, 0, 0])
    for i in range(4):
        for j in range(i + 1, 4):
            aig = (i, j) in ((0, 1), (2, 3))
            ax.plot(*zip(V[i], V[j]), color=F.INK if aig else c, lw=3.2 if aig else 1.4)
    ax.add_collection3d(Poly3DCollection([V[list(f)] for f in ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))],
                                         facecolor=c, alpha=0.18, edgecolor="none"))
ax.text(-1.25, 0, 1.15, "α = 90°, écart √2 :\ntétraèdre régulier", fontsize=8.6, color=F.BLEU, ha="center")
ax.text(1.25, 0, 1.05, "α = 45° : disphénoïde\n(4 faces égales)", fontsize=8.6, color="#a86f00", ha="center")
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(-1.2, 1.2)
ax.set_box_aspect((2, 1, 1), zoom=1.25)
ax.set_axis_off()
ax.view_init(elev=18, azim=-62)
ax.set_title("e)  Deux aiguilles (en noir) font toujours un polyèdre noble", fontsize=10.5)
ax.text2D(0.02, 0.02, "aiguille de longueur 2 à la hauteur +h, la même tournée de α à −h ;\nα = 45° (1re bissection de"
          " Perron) : arêtes aplaties dans le rapport √2 − 1", fontsize=8.4, color=F.INK2, transform=ax.transAxes)
F.sauver(fig, "q2_newton_polyedres.png")
