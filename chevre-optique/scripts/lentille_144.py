"""
Partie XII : 144, la douzième lentille. Les angles exacts de l'angle d'or en degrés, et la dimension 2,5.

    python3 scripts/lentille_144.py        # ≈ 30 s

Écrit resultats/lentille_144.md et figures/l1_lentille_144.png.

1. Les approximations de Fibonacci de l'angle d'or, 360°·F(k−2)/F(k), et celles qui tombent juste en degrés.
2. Pourquoi 144 est la dernière : les facteurs premiers des nombres de Fibonacci (théorème de Carmichael).
3. La lentille de Fibonacci à 144 anneaux : ses deux foyers aux mêmes fractions, 55/144 et 89/144.
4. La corde de la chèvre en dimension réelle, autour de 2,5.
"""

import logging
import os
import sys
from fractions import Fraction

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
import sympy as sp
from matplotlib.patches import Wedge
from scipy.optimize import minimize_scalar
from scipy.signal import find_peaks

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
mp.mp.dps = 25
ICI = os.path.dirname(os.path.abspath(__file__))
PHI = (1 + 5 ** 0.5) / 2
OR = 360 / PHI ** 2
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


FIB = [1, 1]
while len(FIB) < 70:
    FIB.append(FIB[-1] + FIB[-2])
Fk = lambda k: FIB[k - 1]  # F(1) = F(2) = 1, F(3) = 2…


def decimal_fini(q):
    d = Fraction(q).denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    return d == 1


# ---------------------------------------------------------------------------
# 1. Les approximations de Fibonacci de l'angle d'or
# ---------------------------------------------------------------------------
ligne("## 1. L'angle d'or approché par les nombres de Fibonacci\n")
ligne(f"Angle d'or exact : 360°/φ² = {fr(OR, '{:.6f}')}° ; complément 360°/φ = {fr(360 / PHI, '{:.6f}')}°.\n")
ligne("| k | F(k) | fraction de tour | angle (degrés) | complément | écart à l'angle d'or | écriture décimale finie ? |")
ligne("|---:|---:|---|---|---|---|---|")
APPROX = []
for k in range(3, 22):
    a = Fraction(360 * Fk(k - 2), Fk(k))
    fini = decimal_fini(a)
    APPROX.append((k, Fk(k), float(a), fini))
    ligne(f"| {k} | {Fk(k)} | {Fk(k - 2)}/{Fk(k)} | {fr(float(a), '{:.6f}')} | {fr(360 - float(a), '{:.6f}')} |"
          f" {fr(float(a) - OR, '{:+.6f}')} | {'oui' if fini else 'non'} |")
ligne(f"\nPour k = 12 : 55/144 de tour = 137,5° et 89/144 = 222,5° exactement ; le pas 360°/144 vaut 2,5° = 5²×10⁻¹,"
      " et 222,5 = 89 × 2,5 = 88 × 2,5 + 2,5 = 220 + 2,5.")
ligne(f"Écart de 137,5° à l'angle d'or : {fr(137.5 - OR, '{:+.6f}')}° ; prévision de Hurwitz 360°/(√5·144²) ="
      f" {fr(360 / (5 ** 0.5 * 144 ** 2), '{:.6f}')}°.")

# ---------------------------------------------------------------------------
# 2. Pourquoi 144 est la dernière
# ---------------------------------------------------------------------------
ligne("\n## 2. Pourquoi 144 est la dernière\n")
ligne("360 = 2³·3²·5. Une fraction F(k−2)/F(k) de tour s'écrit en degrés avec un nombre fini de décimales seulement si F(k)"
      " n'a pas d'autre facteur premier que 2, 3 et 5.\n")
ligne("| k | F(k) | facteurs premiers | nouveau facteur premier (primitif) |")
ligne("|---:|---:|---|---|")
vus = set()
for k in range(3, 26):
    fac = sp.factorint(Fk(k))
    nouveaux = [p for p in fac if p not in vus]
    vus |= set(fac)
    if k <= 16 or k == 25:
        ligne(f"| {k} | {Fk(k)} | {' · '.join(f'{p}^{e}' if e > 1 else str(p) for p, e in fac.items())} |"
              f" {', '.join(map(str, nouveaux)) if nouveaux else 'aucun'} |")
sans_nouveau = []
vus = set()
for k in range(3, 61):
    fac = set(sp.factorint(Fk(k)))
    if not fac - vus:
        sans_nouveau.append(k)
    vus |= fac
ligne(f"\nIndices k ≥ 3 sans nouveau facteur premier, jusqu'à k = 60 : {sans_nouveau} (F(6) = 8 et F(12) = 144)."
      " Théorème de Carmichael (1913) : au-delà de k = 12, chaque F(k) apporte un nouveau premier, forcément ≥ 7."
      " Les fractions de Fibonacci de l'angle d'or tombent donc juste en degrés pour k = 3, 4, 5, 6 et 12, puis plus jamais.")
ligne("144 = 12² est aussi le plus grand carré de la suite de Fibonacci (Cohn, 1964) ; avec 8, c'est la seule puissance"
      " parfaite au-delà de 1 (Bugeaud, Mignotte et Siksek, 2006).")


# ---------------------------------------------------------------------------
# 3. La lentille de Fibonacci à 144 anneaux
# ---------------------------------------------------------------------------
def mot_fibonacci(j):
    S = ["B", "A"]
    for _ in range(2, j + 1):
        S.append(S[-1] + S[-2])
    return S[j]


def intensite_axe(q, u):
    N = len(q)
    z = np.exp(-2j * np.pi * np.asarray(u, float) / N)
    Q = np.zeros_like(z)
    for t in q[::-1]:
        Q = Q * z + t
    return 4 * np.sin(np.pi * np.asarray(u, float) / N) ** 2 * np.abs(Q) ** 2


Q144 = np.array([c == "A" for c in mot_fibonacci(11)], float)
UU = np.linspace(0.3, 143.7, 60 * 144)
I144 = intensite_axe(Q144, UU)
pk, _ = find_peaks(I144)
deux = sorted(pk[np.argsort(I144[pk])[-2:]])
FOY = [minimize_scalar(lambda x: -intensite_axe(Q144, x), bounds=(UU[k - 1], UU[k + 1]), method="bounded",
                       options={"xatol": 1e-11}).x for k in deux]
ligne("\n## 3. La lentille de Fibonacci à 144 anneaux\n")
ligne(f"Ses deux foyers sont en u = {fr(FOY[0])} et {fr(FOY[1])} (partie VIII), soit {fr(FOY[0] / 144, '{:.5f}')} et"
      f" {fr(FOY[1] / 144, '{:.5f}')} du nombre d'anneaux, contre 55/144 = {fr(55 / 144, '{:.5f}')}, 89/144 ="
      f" {fr(89 / 144, '{:.5f}')} et 1/φ² = {fr(1 / PHI ** 2, '{:.5f}')}, 1/φ = {fr(1 / PHI, '{:.5f}')}.")
ligne(f"En degrés (× 2,5°) : {fr(FOY[0] * 2.5, '{:.3f}')}° et {fr(FOY[1] * 2.5, '{:.3f}')}°.")
ligne("\n| anneaux F(k) | foyers (u₁ ; u₂) | rapport u₂/u₁ | approximation de l'angle d'or 360·F(k−2)/F(k) |")
ligne("|---:|---|---|---|")
LENT = []
for j in range(5, 14):
    q = np.array([c == "A" for c in mot_fibonacci(j)], float)
    N = len(q)
    u = np.linspace(0.3, N - 0.3, 80 * N)
    I = intensite_axe(q, u)
    p_, _ = find_peaks(I)
    d_ = sorted(p_[np.argsort(I[p_])[-2:]])
    f_ = [minimize_scalar(lambda x: -intensite_axe(q, x), bounds=(u[k - 1], u[k + 1]), method="bounded").x for k in d_]
    k = FIB.index(N) + 1 if N > 1 else 2
    LENT.append((N, f_[0], f_[1]))
    ligne(f"| {N} | {fr(f_[0], '{:.3f}')} ; {fr(f_[1], '{:.3f}')} | {fr(f_[1] / f_[0], '{:.5f}')} |"
          f" {fr(360 * Fk(k - 2) / N, '{:.4f}')}° |")


# ---------------------------------------------------------------------------
# 4. La corde de la chèvre en dimension réelle, autour de 2,5
# ---------------------------------------------------------------------------
def part(n, r):
    n, r = mp.mpf(n), mp.mpf(r)
    c1 = 1 - r * r / 2
    I1 = mp.betainc((n + 1) / 2, mp.mpf(1) / 2, 0, 1 - c1 * c1, regularized=True)
    if c1 < 0:
        I1 = 2 - I1
    I2 = mp.betainc((n + 1) / 2, mp.mpf(1) / 2, 0, 1 - (r / 2) ** 2, regularized=True)
    return (I1 + r ** n * I2) / 2


def corde(n):
    return mp.findroot(lambda r: part(n, r) - mp.mpf(1) / 2, 1.2)


ligne("\n## 4. La corde de la chèvre en dimension réelle, autour de 2,5\n")
ligne("| dimension n | corde de la chèvre |")
ligne("|---:|---|")
for n in (2, 2.187, 2.24, 2.42, 2.45, 2.5, 2.55, 3):
    ligne(f"| {fr(n, '{:.3f}')} | {fr(float(corde(n)), '{:.6f}')} |")
pent = 2 * mp.sin(mp.pi / 5)
nP = mp.findroot(lambda n: corde(n) - pent, 2.2)
ligne(f"\nLa corde vaut celle du pentagone, 2 sin 36° (avec r² = 3 − φ), en n = {fr(float(nP), '{:.4f}')}.")
ligne("Bosse des écarts entre la chèvre et le simplexe (partie VI) : sommets en n = 2,24 (cordes), 2,42 (déplacement)"
      " et 3,20 (part manquante).")
NN = np.linspace(1.2, 3.6, 49)
CC = [float(corde(n)) for n in NN]

with open(os.path.join(ICI, "..", "resultats", "lentille_144.md"), "w") as fh:
    fh.write("# Résultats de la partie XII (générés par scripts/lentille_144.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure
# ===========================================================================
fig, axs = plt.subplots(2, 2, figsize=(16, 12), gridspec_kw={"wspace": 0.22, "hspace": 0.3})

# a) les approximations
ax = axs[0, 0]
ks = [a[0] for a in APPROX]
vals = [a[2] for a in APPROX]
ax.axhline(OR, color=F.ORANGE, lw=1.2, label="angle d'or exact, 137,5078°")
ax.plot(ks, vals, "-", color=F.BASE, lw=1)
for k, Nk, v, fini in APPROX:
    ax.plot(k, v, "o", color=F.BLEU if fini else F.MUTED, ms=8 if fini else 5, mec=F.SURF, zorder=5)
    if fini and k != 12:  # 137,5° est légendé à part
        ax.annotate(f"{v:g}°".replace(".", ","), xy=(k, v), xytext=(6, -15) if k == 6 else (6, 6),
                    textcoords="offset points", fontsize=9.5, color=F.BLEU)
ax.annotate("55/144 de tour = 137,5° exactement\n(pas de 2,5° = 5²×10⁻¹)", xy=(12, 137.5), xytext=(13.2, 160),
            fontsize=9.5, arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.set_ylim(110, 185)
ax.set_xticks(range(3, 22))
ax.set_xlabel("k (approximation 360°·F(k−2)/F(k))")
ax.set_ylabel("angle (degrés)")
ax.plot([], [], "o", color=F.BLEU, ms=8, label="tombe juste en degrés")
ax.plot([], [], "o", color=F.MUTED, ms=5, label="écriture décimale infinie")
ax.legend(fontsize=9, loc="upper right")
axi = ax.inset_axes([0.42, 0.05, 0.55, 0.24])
axi.semilogy(ks, [abs(v - OR) for v in vals], "o-", color=F.INK2, ms=3.5, lw=1)
axi.semilogy(12, abs(137.5 - OR), "o", color=F.BLEU, ms=6)
axi.set_title("écart à l'angle d'or (degrés)", fontsize=8.5, fontweight="normal", loc="center")
axi.tick_params(labelsize=7.5)
axi.set_xticks([3, 6, 9, 12, 15, 18, 21])
ax.set_title("a)  Les fractions de Fibonacci de l'angle d'or")

# b) le cercle en 144 pas
ax = axs[0, 1]
ax.set_aspect("equal")
ax.axis("off")
ax.add_patch(Wedge((0, 0), 1, 90 - 137.5, 90, width=0.2, fc=F.BLEU, alpha=0.75, ec=F.SURF))
ax.add_patch(Wedge((0, 0), 1, 90, 90 + 222.5, width=0.2, fc=F.ORANGE, alpha=0.75, ec=F.SURF))
for i in range(144):
    t = np.radians(90 - 2.5 * i)
    lg = 0.1 if i % 12 == 0 else 0.045
    ax.plot([np.cos(t), (1 + lg) * np.cos(t)], [np.sin(t), (1 + lg) * np.sin(t)], color=F.INK2, lw=0.9 if i % 12 == 0 else 0.5)
ax.text(0, 0.12, "144 pas de 2,5°", ha="center", fontsize=12, fontweight="bold")
ax.text(0, -0.12, "144 = F(12) = 12²", ha="center", fontsize=10, color=F.INK2)
ax.text(1.05, 0.75, "55 pas = 137,5°", fontsize=10, color=F.BLEU)
ax.text(-1.08, -0.95, "89 pas = 222,5°\n= 88 × 2,5 + 2,5 = 220 + 2,5", fontsize=10, color=F.ORANGE, ha="right", va="top")
ax.text(-1.55, -1.55, "Traits longs : tous les 12 pas (30°). La division du tour en degrés, faite\n"
        "sur 12, rencontre la suite de Fibonacci exactement en 144 = 12².", fontsize=9, color=F.INK2, va="top")
ax.set_xlim(-1.6, 1.75)
ax.set_ylim(-1.95, 1.3)
ax.set_title("b)  Le tour en 144 pas : 55 + 89")

# c) la lentille à 144 anneaux
ax = axs[1, 0]
ax.plot(UU, I144 / I144.max(), color=F.BLEU, lw=1.3)
for f_, lab in zip(FOY, ("u₁", "u₂")):
    ax.annotate(f"{lab} = {f_:.2f}\n= {2.5 * f_:.2f}°".replace(".", ","), xy=(f_, 1), xytext=(f_ + (-28 if lab == "u₁" else 6), 0.82),
                fontsize=9.5, arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
for v in (55, 89):
    ax.axvline(v, color=F.ORANGE, lw=0.9, ls=":")
ax.set_xlim(0, 144)
ax.set_ylim(0, 1.15)
ax.set_xlabel("u = a²/(2λz), sur 144 anneaux")
ax.set_ylabel("intensité sur l'axe (normalisée)")
haut = ax.secondary_xaxis("top", functions=(lambda u: 2.5 * u, lambda d: d / 2.5))
haut.set_xlabel("le même axe en degrés (× 2,5°)")
haut.set_xticks([0, 45, 90, 137.5, 180, 222.5, 270, 315, 360])
haut.set_xticklabels(["0", "45", "90", "137,5", "180", "222,5", "270", "315", "360"], fontsize=8)
ax.set_title("c)  La lentille à 144 anneaux : ses deux foyers en 55 et 89", pad=34)

# d) la dimension réelle
ax = axs[1, 1]
ax.axvspan(2.45, 2.55, color=F.JAUNE, alpha=0.25, lw=0, label="ta bande 2,45–2,55")
ax.plot(NN, CC, color=F.INK, lw=1.8, label="corde de la chèvre")
ax.axhline(float(pent), color=F.AQUA, lw=1.1, ls="--", label="corde du pentagone 2 sin 36° (φ)")
F.point(ax, float(nP), float(pent), F.AQUA, 7)
ax.annotate(f"n = {float(nP):.3f}".replace(".", ","), xy=(float(nP), float(pent)), xytext=(1.5, 1.19), fontsize=9,
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
for n_, lab in ((2.24, "2,24"), (2.42, "2,42"), (3.20, "3,20")):
    ax.axvline(n_, color=F.BLEU, lw=0.9, ls=":")
    ax.text(n_ + 0.02, 1.075, lab, fontsize=8.5, color=F.BLEU, rotation=90, va="bottom")
for n_ in (2, 3):
    F.point(ax, n_, float(corde(n_)), F.INK, 6)
ax.set_xlim(1.2, 3.6)
ax.set_ylim(1.07, 1.27)
ax.set_xlabel("dimension n (réelle)")
ax.set_ylabel("corde de la moitié (R = 1)")
ax.text(2.62, 1.135, "pointillés bleus : sommets de la bosse\nchèvre–simplexe (partie VI)", ha="left", va="center",
        fontsize=9, color=F.BLEU)
ax.legend(fontsize=9, loc="upper left")
ax.set_title("d)  La chèvre entre 2D et 3D : pas de Fibonacci vers 2,5")
F.sauver(fig, "l1_lentille_144.png")
