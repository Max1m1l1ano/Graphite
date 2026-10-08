"""
Partie XI : l'angle d'or, les trous du cercle et les petites aiguilles du spectre.

    python3 scripts/angle_or_aiguilles.py        # ≈ 30 s

Écrit resultats/angle_or_aiguilles.md et figures/k1_angle_or_aiguilles.png.

1. 137,5° et 222,5° sont 1/φ² et 1/φ de tour : la même équation que les deux foyers de Fibonacci (partie IX).
2. Le théorème des trois trous : des directions posées à pas d'angle d'or laissent des trous de 2 ou 3 longueurs,
   puissances de 1/φ, la plus grande égale à la somme des deux autres.
3. Le spectre du diaphragme de Fibonacci (55 anneaux) : composantes de Fibonacci, répliques u + 55k, zéros en 55k.
4. Les petites aiguilles du spectre local (partie IX, panneau c) : combien de composantes il faut pour les expliquer.
"""

import logging
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

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
# 1. Le tour partagé par l'angle d'or
# ---------------------------------------------------------------------------
OR = 360 / PHI ** 2
ligne("## 1. L'angle d'or partage le tour comme les deux foyers partagent la puissance\n")
ligne(f"Angle d'or : 360°/φ² = {fr(OR, '{:.6f}')}° ; complément : 360°/φ = {fr(360 / PHI, '{:.6f}')}°.")
ligne(f"En tours : 1/φ² = {fr(1 / PHI ** 2, '{:.6f}')} et 1/φ = {fr(1 / PHI, '{:.6f}')} ; somme = {fr(1 / PHI ** 2 + 1 / PHI, '{:.12f}')}.")
ligne("Les deux foyers de la lentille de Fibonacci (partie IX) : 1/z₁ + 1/z₂ = 1/z_N avec z₁ → φ², z₂ → φ (en unités de z_N)."
      " Le foyer proche porte 1/φ de la puissance 1/z_N, le foyer lointain 1/φ² : le même partage.")
ligne("222,5° n'est pas un simple arrondi de 360°/φ = 222,4922…° (irrationnel) : c'est exactement 89/144 de tour,"
      " l'approximation de Fibonacci de rang 12 (partie XII ; correction de la révision 001).")

# ---------------------------------------------------------------------------
# 2. Le théorème des trois trous
# ---------------------------------------------------------------------------
ligne("\n## 2. Les trous laissés par l'angle d'or (théorème des trois distances)\n")
ligne("| directions N | longueurs des trous (degrés) | rapports | la plus grande = somme des deux autres ? |")
ligne("|---:|---|---|---|")
TROUS = {}
for N_ in range(2, 61):
    p = np.sort((np.arange(N_) / PHI ** 2) % 1)
    g = np.diff(np.r_[p, p[0] + 1]) * 360
    L = []
    for v in np.sort(g):
        if not L or v - L[-1] > 1e-7:
            L.append(v)
    TROUS[N_] = L
    if N_ in (2, 3, 4, 5, 8, 10, 13, 20, 21, 34, 55):
        rap = ", ".join(fr(L[k + 1] / L[k], "{:.6f}") for k in range(len(L) - 1))
        somme = "oui" if len(L) == 3 and abs(L[2] - L[0] - L[1]) < 1e-7 else ("—" if len(L) == 2 else "non")
        ligne(f"| {N_} | {' ; '.join(fr(v, '{:.3f}') for v in L)} | {rap} | {somme} |")
fib = [n for n in TROUS if len(TROUS[n]) == 2]
ligne(f"\nDeux longueurs seulement pour N = {', '.join(str(n) for n in fib)} : exactement les nombres de Fibonacci.")
ligne("Toutes les longueurs sont des 360°/φ^k : 137,51° ; 84,98° ; 52,52° ; 32,46° ; 20,06° ; 12,40° ; …")

# ---------------------------------------------------------------------------
# 3. Le spectre du diaphragme de Fibonacci
# ---------------------------------------------------------------------------
def mot_fibonacci(j):
    S = ["B", "A"]
    for _ in range(2, j + 1):
        S.append(S[-1] + S[-2])
    return S[j]


Q55 = np.array([c == "A" for c in mot_fibonacci(9)], float)
NZ = len(Q55)


def coef(u):
    """Coefficient de Fourier du motif des anneaux, en ζ = (r/a)² (cellules de largeur 1/N)."""
    if u == 0:
        return Q55.mean() + 0j
    k = np.arange(NZ)
    Q = np.sum(Q55 * np.exp(-2j * np.pi * u * k / NZ))
    return Q * (1 - np.exp(-2j * np.pi * u / NZ)) / (2j * np.pi * u)


US = np.arange(1, 601)
C = np.array([coef(u) for u in US])
ORDRE = np.argsort(np.abs(C))[::-1]
FIBS = {1, 2, 3, 5, 8, 13, 21, 34, 89, 144, 233, 377}
LUCAS = {1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521}
ligne("\n## 3. Le spectre du diaphragme de Fibonacci (55 anneaux)\n")
ligne("| rang | composante u | amplitude | nature |")
ligne("|---:|---:|---|---|")
for rang, t in enumerate(ORDRE[:16], 1):
    u = int(US[t])
    nat = []
    if u in FIBS:
        nat.append("nombre de Fibonacci")
    if u in LUCAS:
        nat.append("nombre de Lucas")
    for base in (21, 34, 13, 8):
        if u > 55 and (u - base) % 55 == 0:
            nat.append(f"réplique {base} + {(u - base) // 55}×55")
    ligne(f"| {rang} | {u} | {fr(abs(C[t]))} | {', '.join(nat) if nat else 'somme ou différence de nombres de Fibonacci'} |")
ligne(f"\nMultiples de 55 : amplitude exactement nulle ({fr(abs(coef(55)), '{:.1e}')} pour 55, {fr(abs(coef(220)), '{:.1e}')} pour 220).")
ligne(f"u = 11 : {fr(abs(coef(11)))} ; u = 66 = 11 + 55 : {fr(abs(coef(66)))} ; u = 121 = 11 + 2×55 : {fr(abs(coef(121)))} ;"
      f" rapport 121/11 : {fr(abs(coef(121)) / abs(coef(11)), '{:.6f}')} = 11/121 = 1/11.")
ligne("Les répliques u + 55k viennent des marches des anneaux, comme les ordres d'un réseau : leur amplitude décroît en 1/(u + 55k).")


# ---------------------------------------------------------------------------
# 4. Les petites aiguilles du spectre local
# ---------------------------------------------------------------------------
R = 60
II = np.arange(-R, R + 1)
ZE = II * II / R ** 2
KZ = np.floor(NZ * ZE).astype(int)
RANGEE = np.where(KZ < NZ, Q55[np.minimum(KZ, NZ - 1)], 0.0)


def spectre_local(s, Lw=16, nfft=512):
    w = np.hanning(Lw)
    out = []
    for c0 in range(len(s)):
        seg = np.array([s[j] if 0 <= j < len(s) else 0.0 for j in range(c0 - Lw // 2, c0 - Lw // 2 + Lw)])
        seg = (seg - np.sum(seg * w) / np.sum(w)) * w
        out.append(np.abs(np.fft.rfft(seg, nfft)))
    return np.array(out)


def reconstruit(K):
    r = np.full(len(II), coef(0).real)
    for t in ORDRE[:K]:
        r = r + 2 * np.real(C[t] * np.exp(2j * np.pi * US[t] * ZE))
    return np.where(ZE < 1, r, 0.0)


S0 = spectre_local(RANGEE)
ligne("\n## 4. Les petites aiguilles du spectre local (rayon 60 px, le long de l'axe)\n")
ligne("On reconstruit la rangée de pixels avec les K composantes les plus fortes, et on compare son spectre local au spectre mesuré.\n")
ligne("| composantes gardées K | composantes ajoutées | ressemblance des spectres (corrélation) |")
ligne("|---:|---|---|")
CORR = {}
prec = 0
for K in (1, 2, 3, 4, 6, 8, 12, 16, 24, 40, 80, 200, 600):
    cc = np.corrcoef(S0.ravel(), spectre_local(reconstruit(K)).ravel())[0, 1]
    CORR[K] = cc
    ajout = ", ".join(str(int(US[t])) for t in ORDRE[prec:K]) if K <= 16 else "…"
    ligne(f"| {K} | {ajout} | {fr(cc, '{:.3f}')} |")
    prec = K
ligne("\nAvec les deux seules composantes de la partie IX (21 et 34), la ressemblance n'est que de 0,71 : les autres aiguilles"
      " manquaient.")

with open(os.path.join(ICI, "..", "resultats", "angle_or_aiguilles.md"), "w") as fh:
    fh.write("# Résultats de la partie XI (générés par scripts/angle_or_aiguilles.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure
# ===========================================================================
fig = plt.figure(figsize=(20, 12.8))
gs = fig.add_gridspec(2, 3, wspace=0.17, hspace=0.27)


def schema(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")


# a) le tour partagé
ax = fig.add_subplot(gs[0, 0])
ax.add_patch(Wedge((0, 0), 1, 90 - OR, 90, width=0.22, fc=F.BLEU, alpha=0.75, ec=F.SURF))
ax.add_patch(Wedge((0, 0), 1, 90, 90 + 360 - OR, width=0.22, fc=F.ORANGE, alpha=0.75, ec=F.SURF))
ax.text(0.98, 0.72, "137,5° = 1/φ² de tour", fontsize=10, color=F.BLEU, ha="left")
ax.text(-1.0, -1.02, "222,5° = 1/φ de tour", fontsize=10, color=F.ORANGE, ha="right", va="top")
ax.text(0, 0.06, "1/φ² + 1/φ = 1", ha="center", fontsize=13, fontweight="bold")
ax.text(0, -0.2, "(φ² = φ + 1)", ha="center", fontsize=10, color=F.INK2)
ax.text(-1.55, -1.42, "C'est l'équation des deux foyers de la lentille de Fibonacci (partie IX) :\n"
        "1/z₁ + 1/z₂ = 1/z_N, avec z₁ = φ² et z₂ = φ. L'angle d'or partage le tour\n"
        "comme les deux foyers partagent la puissance de la lentille.\n"
        "Valeur exacte du complément : 360°/φ = 222,4922…°, un nombre irrationnel.", fontsize=9, color=F.INK2,
        va="top")
schema(ax, (-1.6, 2.1), (-2.15, 1.25))
ax.set_title("a)  L'angle d'or partage le tour en 1/φ² et 1/φ")

# b) les trous pour N = 13 et N = 10
ax = fig.add_subplot(gs[0, 1])
couleurs = [F.AQUA, F.BLEU, F.ORANGE]
for cx, N_ in ((-1.2, 13), (1.2, 10)):
    ang = (np.arange(N_) * OR) % 360
    ordre_ = np.argsort(ang)
    a_s = ang[ordre_]
    L = TROUS[N_]
    for k in range(N_):
        a1, a2 = a_s[k], (a_s[(k + 1) % N_] if k + 1 < N_ else a_s[0] + 360)
        lg = a2 - a1
        idx = int(np.argmin([abs(lg - v) for v in L]))
        ax.add_patch(Wedge((cx, 0), 1, 90 - a2, 90 - a1, width=0.16, fc=couleurs[idx], alpha=0.8, ec=F.SURF, lw=1.2))
    for j, a_ in enumerate(ang):
        x_, y_ = cx + 1.13 * np.sin(np.radians(a_)), 1.13 * np.cos(np.radians(a_))
        ax.text(x_, y_, str(j), ha="center", va="center", fontsize=7.5, color=F.INK2)
    ax.text(cx, 0.08, f"N = {N_}", ha="center", fontsize=11, fontweight="bold")
    ax.text(cx, -0.2, ("2 longueurs" if len(L) == 2 else "3 longueurs"), ha="center", fontsize=9.5, color=F.INK2)
    ax.text(cx, -1.32, " ; ".join(f"{v:.1f}°" for v in L).replace(".", ","), ha="center", va="top", fontsize=9)
ax.text(-2.4, -1.65, "Directions posées une à une à pas d'angle d'or (numéros = ordre de pose).\n"
        "Les trous n'ont jamais plus de 3 longueurs, toutes des 360°/φ^k ; la plus grande est\n"
        "la somme des deux autres. Pour N de Fibonacci (13), il n'en reste que 2.", fontsize=9, color=F.INK2, va="top")
schema(ax, (-2.45, 2.45), (-2.25, 1.3))
ax.set_title("b)  Les trous de l'angle d'or : 2 ou 3 longueurs")

# c) l'escalier des trous
ax = fig.add_subplot(gs[0, 2])
for N_, L in TROUS.items():
    for v in L:
        ax.semilogy(N_, v, "o", color=F.AQUA if len(L) == 2 else F.BLEU, ms=4.2, mec=F.SURF, mew=0.6)
for n in (2, 3, 5, 8, 13, 21, 34, 55):
    ax.axvline(n, color=F.GRID, lw=1, zorder=0)
    if n > 2:
        ax.text(n, 330, str(n), ha="center", fontsize=8.5, color=F.INK2)
for k in range(2, 10):
    ax.axhline(360 / PHI ** k, color=F.BASE, lw=0.6, ls=":", zorder=0)
ax.set_xlim(1, 61)
ax.set_ylim(3, 420)
ax.set_xlabel("nombre de directions N")
ax.set_ylabel("longueur des trous (degrés)")
ax.text(60, 250, "vert : 2 longueurs (N de Fibonacci)\nbleu : 3 longueurs\npointillés : 360°/φ^k", ha="right", va="top",
        fontsize=9, color=F.INK2)
ax.set_title("c)  L'escalier des trous : des puissances de 1/φ")

# d) les petites aiguilles : avant / après
sub = gs[1, 0:2].subgridspec(1, 2, wspace=0.08)
NIVEAUX = [(ORDRE[:2], F.ORANGE, 1.5), (ORDRE[2:5], F.BLEU, 1.1), (ORDRE[5:8], F.AQUA, 0.9)]
xx = np.linspace(-1, 1, 1201)
for col, (nb, titre) in enumerate(((1, f"deux composantes (21, 34) : ressemblance {CORR[2]:.2f}"),
                                   (3, f"huit composantes : ressemblance {CORR[8]:.2f}"))):
    ax = fig.add_subplot(sub[0, col])
    ax.imshow(S0.T, origin="lower", aspect="auto", extent=(-1, 1, 0, 0.5), cmap="Greys", vmax=np.percentile(S0, 99.5))
    for sel, coul, lw in NIVEAUX[:nb]:
        for t in sel:
            fl = 2 * US[t] * np.abs(xx) / R
            ax.plot(xx, np.abs(fl - np.round(fl)), color=coul, lw=lw, alpha=0.9)
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 0.5)
    ax.grid(False)
    ax.set_xlabel("position sur l'axe (x/a), R = 60 px")
    if col == 0:
        ax.set_ylabel("fréquence des franges vues (cycles par pixel)")
        ax.text(-1, 0.535, "d)  Les petites aiguilles : ce sont les composantes suivantes", fontsize=11.5, fontweight="bold",
                color=F.INK)
    else:
        ax.set_yticklabels([])
    ax.set_title(titre.replace(".", ","), fontsize=10, fontweight="normal", loc="center")
ax.text(0.985, 0.985, "orange : 21, 34\nbleu : 13, 76, 89\nvert : 26, 29, 8", transform=ax.transAxes, fontsize=9, color=F.INK,
        va="top", ha="right", bbox=dict(fc=F.SURF, ec="none", alpha=0.9, pad=3))

# e) le spectre du diaphragme
ax = fig.add_subplot(gs[1, 2])
umax = 235
uu = US[:umax]
amp = np.abs(C[:umax])
couleur = []
for u in uu:
    if u in FIBS:
        couleur.append(F.BLEU)
    elif any(u > 55 and (u - b) % 55 == 0 for b in (21, 34, 13, 8)):
        couleur.append(F.ORANGE)
    else:
        couleur.append(F.BASE)
ax.vlines(uu, 0, amp, colors=couleur, lw=1.3)
for u in (55, 110, 165, 220):
    ax.plot(u, 0, "x", color=F.INK, ms=7, mew=1.6)
for u, lab, dy in ((21, "21", 0.008), (34, "34", 0.008), (13, "13", 0.008), (8, "8", 0.008), (76, "76", 0.006),
                   (89, "89", 0.006), (144, "144", 0.006)):
    ax.text(u, abs(coef(u)) + dy, lab, ha="center", fontsize=8.5)
ax.annotate("121 = 11 + 2×55 :\namplitude exactement 1/11\nde celle de 11", xy=(121, abs(coef(121))), xytext=(120, 0.12), fontsize=8.5,
            ha="center", arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.annotate("220 = 4×55 : zéro exact", xy=(220, 0), xytext=(185, 0.07), fontsize=8.5, ha="center",
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.set_xlim(0, umax)
ax.set_ylim(0, 0.25)
ax.set_xlabel("composante u (nombre d'anneaux par unité de ζ = (r/a)²)")
ax.set_ylabel("amplitude dans le motif")
ax.text(234, 0.235, "bleu : nombres de Fibonacci\norange : répliques u + 55k\n× : multiples de 55, zéros exacts", ha="right",
        va="top", fontsize=9, color=F.INK2)
ax.set_title("e)  Le spectre du diaphragme : Fibonacci et répliques")
F.sauver(fig, "k1_angle_or_aiguilles.png")
