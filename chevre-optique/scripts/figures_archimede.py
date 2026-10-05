"""
Figures de la partie II (préfixe « b »), dans ../figures/.

    python3 scripts/figures_archimede.py
"""

import os
import sys
from math import acos, cos, pi, sqrt

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(__file__))
import archimede as ar  # noqa: E402
import chevre as ch  # noqa: E402
import figures as F  # noqa: E402  (style, palette et utilitaires de la partie I)

BLEU, ORANGE, AQUA, JAUNE = F.BLEU, F.ORANGE, F.AQUA, F.JAUNE
INK, INK2, MUTED, BASE, SURF = F.INK, F.INK2, F.MUTED, F.BASE, F.SURF
PHI = (1 + sqrt(5)) / 2
point, cercle, sauver = F.point, F.cercle, F.sauver


def fr(x, d=3):
    return f"{x:.{d}f}".replace(".", ",")


# ===========================================================================
# b1 — les six projections de la superposition dans le cube
# ===========================================================================
def fig_projections():
    fig, axs = plt.subplots(2, 3, figsize=(13.5, 9.2))
    vues = [("+z (dessus)", "dessus"), ("+x", "cote"), ("+y", "cote"),
            ("−z (dessous)", "dessus"), ("−x", "cote"), ("−y", "cote")]
    t = np.linspace(-1, 1, 400)
    for ax, (nom, genre) in zip(axs.flat, vues):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.add_patch(mpatches.Rectangle((-1, -1), 2, 2, fill=False, ec=INK, lw=1.4))
        if genre == "cote":
            ax.add_patch(mpatches.Rectangle((-1, -1), 2, 2, fc=MUTED, alpha=0.06, lw=0))
            cercle(ax, (0, 0), 1, color=BLEU, lw=2)
            ax.plot([-1, 1], [-1, 1], color=ORANGE, lw=1.8)
            ax.plot([-1, 1], [1, -1], color=ORANGE, lw=1.8)
            ax.plot(t, t * t, color=AQUA, lw=1.8)
            ax.plot(t, -t * t, color=AQUA, lw=1.8)
            a = 1 / sqrt(2)
            for sx in (-1, 1):
                for sy in (-1, 1):
                    point(ax, sx * a, sy * a, INK, 7)
                    point(ax, sx / sqrt(PHI), sy / PHI, INK2, 6)
            point(ax, 0, 0, INK, 6)
            for yv, yt, txt, c in [(a, a + 0.06, "z = 1/√2", INK), (1 / PHI, 1 / PHI - 0.06, "z = 1/φ", INK2),
                                   (-a, -a - 0.06, "z = −1/√2", INK), (-1 / PHI, -1 / PHI + 0.06, "z = −1/φ", INK2)]:
                ax.plot([1.0, 1.05, 1.08], [yv, yv, yt], color=c, lw=0.8)
                ax.text(1.1, yt, txt, fontsize=8.5, color=c, va="center")
        else:
            ax.add_patch(mpatches.Circle((0, 0), 1, fc=BLEU, alpha=0.07, lw=0))
            cercle(ax, (0, 0), 1, color=BLEU, lw=2)
            cercle(ax, (0, 0), 1 / sqrt(2), color=ORANGE, lw=1.6)
            cercle(ax, (0, 0), 1 / sqrt(PHI), color=AQUA, lw=1.4, ls=(0, (4, 3)))
            point(ax, 0, 0, INK, 6)
            c = 1 / sqrt(2)
            ax.plot([-c, c, c, -c, -c], [-c, -c, c, c, -c], color=MUTED, lw=0.8)
            ax.text(0.04, 0.08, "sommet\ndes cônes", fontsize=8, color=INK2)
            ax.text(0.5, -0.86, "r = 1/√2", fontsize=8.5, color=INK, ha="center")
        ax.set_title(nom, fontsize=11)
        ax.set_xlim(-1.2, 1.75)
        ax.set_ylim(-1.2, 1.2)
    handles = [plt.Line2D([], [], color=BLEU, lw=2, label="sphère (contour)"),
               plt.Line2D([], [], color=INK, lw=1.4, label="cylindre et cube (contour)"),
               plt.Line2D([], [], color=ORANGE, lw=1.8, label="double cône (sommet au centre)"),
               plt.Line2D([], [], color=AQUA, lw=1.8, label="double paraboloïde |z| = ρ²")]
    fig.legend(handles=handles, loc="lower center", ncol=4, fontsize=9.5, bbox_to_anchor=(0.5, -0.01))
    fig.suptitle("Sphère, cylindre, double cône et paraboloïdes dans le cube : les six projections (deux types seulement)",
                 x=0.01, ha="left", fontsize=12.5, fontweight="bold", y=0.99)
    fig.text(0.01, 0.945, "De côté, le cercle croise les diagonales du cône en z = ±1/√2 et les paraboles en z = ±1/φ "
             "(nombre d'or). Vu de dessus, tout est concentrique : ces croisements deviennent des cercles.",
             fontsize=9.5, color=INK2)
    sauver(fig, "b1_six_projections.png")


# ===========================================================================
# b2 — tranches d'Archimède
# ===========================================================================
def fig_tranches():
    fig, axs = plt.subplots(1, 2, figsize=(13.5, 4.8), gridspec_kw={"wspace": 0.28})
    ax = axs[0]
    z = np.linspace(0, 1, 400)
    ax.plot(z, np.pi * (1 - z * z), color=BLEU, lw=2.2)
    ax.plot(z, np.pi * z * z, color=ORANGE, lw=2)
    ax.plot(z, np.pi * z, color=AQUA, lw=2)
    ax.axhline(np.pi, color=INK, lw=1.2)
    ax.axhline(np.pi / 2, color=MUTED, lw=1)
    point(ax, 1 / sqrt(2), np.pi / 2, INK, 8)
    point(ax, 1 / PHI, np.pi / PHI, INK2, 7)
    ax.text(0.03, np.pi + 0.07, "cylindre : π", fontsize=9, color=INK)
    ax.text(0.03, 2.55, "hémisphère π(1 − z²)\n= cylindre − cône", fontsize=9, color=INK2)
    ax.text(0.62, 0.62, "cône πz²", fontsize=9, color=INK2)
    ax.text(0.2, 0.98, "paraboloïde πz", fontsize=9, color=INK2)
    ax.text(1 / sqrt(2) + 0.03, np.pi / 2 - 0.25, "z = 1/√2 : π/2,\nla moitié", fontsize=9, color=INK)
    ax.text(1 / PHI - 0.05, np.pi / PHI + 0.12, "z = 1/φ", fontsize=9, color=INK2, ha="right")
    ax.set_xlabel("hauteur z / R")
    ax.set_ylabel("aire de la tranche / R²")
    ax.set_title("a)  Les tranches d'Archimède")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 3.5)
    ax = axs[1]
    noms = ["cylindre", "paraboloïde (bol)", "cône (pointe en bas)", "hémisphère\n= cylindre − cône"]
    zs = [0.5, 1 / sqrt(2), 2 ** (-1 / 3), 2 * cos(np.radians(80))]
    eq = ["z = 1/2", "z = 1/√2", "z = 2^(−1/3)", "z³ − 3z + 1 = 0\nz = 2 cos 80°"]
    y = np.arange(len(noms))[::-1]
    ax.hlines(y, 0, zs, color=BASE, lw=3)
    for yi, zi, e in zip(y, zs, eq):
        point(ax, zi, yi, BLEU, 10)
        ax.text(zi + 0.03, yi, f"{fr(zi, 4)}   {e}", va="center", fontsize=9, color=INK)
    ax.set_yticks(y)
    ax.set_yticklabels(noms)
    ax.set_xlim(0, 1.25)
    ax.set_xlabel("hauteur du plan qui coupe le volume en deux (depuis la base)")
    ax.set_title("b)  Couper chaque solide en deux volumes égaux")
    ax.grid(axis="y", visible=False)
    sauver(fig, "b2_tranches_archimede.png")


# ===========================================================================
# b3 — le cube qui tourne : losange, hyperboloïde, ménisque, sphère médiane
# ===========================================================================
def fig_cube_tournant():
    fig, axs = plt.subplots(1, 3, figsize=(15, 5.6), gridspec_kw={"width_ratios": [1.25, 0.85, 1], "wspace": 0.05})
    ax_notes = axs[1]
    ax_notes.axis("off")
    axs = [axs[0], axs[2]]
    ax = axs[0]
    L = sqrt(3)
    s = np.linspace(0, L, 1200)
    r = np.sqrt([ar.profil_balayé(x) for x in s])
    ax.fill_between(s, -r, r, color=BLEU, alpha=0.13, lw=0)
    ax.plot(s, r, color=BLEU, lw=2.2)
    ax.plot(s, -r, color=BLEU, lw=2.2)
    # losange (bicône prolongé)
    ax.plot([0, L / 2, L, L / 2, 0], [0, sqrt(1.5), 0, -sqrt(1.5), 0], color=INK, lw=1.2, ls=(0, (5, 3)))
    # cylindre des sommets et ménisque
    a, b = 1 / L, 2 / L
    ax.plot([a, b], [sqrt(2 / 3)] * 2, color=ORANGE, lw=1.6)
    ax.plot([a, b], [-sqrt(2 / 3)] * 2, color=ORANGE, lw=1.6)
    sm = np.linspace(a, b, 300)
    rm = np.sqrt([ar.profil_balayé(x) for x in sm])
    ax.fill_between(sm, rm, sqrt(2 / 3), color=ORANGE, alpha=0.35, lw=0)
    ax.fill_between(sm, -sqrt(2 / 3), -rm, color=ORANGE, alpha=0.35, lw=0)
    # asymptotes de l'hyperboloïde
    for sg in (1, -1):
        ax.plot([L / 2 - 0.55, L / 2 + 0.55], [-sg * sqrt(2) * 0.55, sg * sqrt(2) * 0.55], color=MUTED, lw=1, ls=(0, (2, 2)))
    # sphère médiane et contacts
    cercle(ax, (L / 2, 0), sqrt(2) / 2, color=AQUA, lw=2)
    for (x, y) in [(L / 6, sqrt(2) * L / 6), (L / 6, -sqrt(2) * L / 6), (5 * L / 6, sqrt(2) * L / 6),
                   (5 * L / 6, -sqrt(2) * L / 6), (L / 2, sqrt(2) / 2), (L / 2, -sqrt(2) / 2)]:
        point(ax, x, y, INK, 7)
    ax.axhline(0, color=MUTED, lw=0.8)
    notes = [(1.05, "losange (tirets) : angles 109,47° et 70,53°,\ndiagonales √3 et √6 (rapport √2)"),
             (0.55, "cônes des bouts (bleu) : demi-angle\narctan √2 = 54,74°, « l'angle magique »"),
             (0.05, "col hyperbolique : r = √2/2 ;\nasymptotes (pointillés) parallèles aux cônes"),
             (-0.45, "ménisque (orange) : entre le cylindre\ndes sommets et le col, 1/9 du volume"),
             (-0.95, "sphère médiane (vert) : touche le solide\nle long de 3 cercles, 6 points dans la coupe")]
    for i, (y, t) in enumerate(notes):
        ax_notes.text(0.0, 0.9 - i * 0.2, t, fontsize=8.8, color=INK, va="center", transform=ax_notes.transAxes)
    ax.set_aspect("equal")
    ax.set_xlim(-0.1, L + 0.1)
    ax.set_ylim(-1.35, 1.38)
    ax.set_xlabel("position le long de la grande diagonale (arête du cube = 1)")
    ax.set_ylabel("rayon")
    ax.set_title("a)  Coupe du solide balayé : π/√3, la moitié de son cylindre")
    # ombre isométrique
    ax = axs[1]
    ax.set_aspect("equal")
    ax.axis("off")
    R6 = sqrt(2 / 3)
    hexa = [(R6 * cos(pi / 6 + k * pi / 3), R6 * np.sin(pi / 6 + k * pi / 3)) for k in range(6)]
    cols = [BLEU, ORANGE, AQUA]
    for i in range(3):
        P = [(0, 0), hexa[2 * i], hexa[(2 * i + 1) % 6], hexa[(2 * i + 2) % 6]]
        ax.add_patch(mpatches.Polygon(P, closed=True, fc=cols[i], alpha=0.18, ec=INK, lw=1.3))
    cercle(ax, (0, 0), sqrt(2) / 2, color=AQUA, lw=2)
    point(ax, 0, 0, INK, 6)
    ax.text(0, -0.92, "vu le long de la diagonale : hexagone régulier\n= 3 losanges de 60°/120° ; "
            "le cercle inscrit\nest l'ombre de la sphère médiane (rayon √2/2)", ha="center", va="top", fontsize=9, color=INK2)
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-1.45, 0.95)
    ax.set_title("b)  L'ombre du cube")
    sauver(fig, "b3_cube_tournant.png")


# ===========================================================================
# b4 — le ménisque réel
# ===========================================================================
def fig_menisque():
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.9), gridspec_kw={"width_ratios": [0.85, 1.1, 1.1], "wspace": 0.3})
    ax = axs[0]
    ax.set_aspect("equal")
    ax.axis("off")
    ax.plot([-1, -1], [-1.3, 1.25], color=INK, lw=2)
    ax.plot([1, 1], [-1.3, 1.25], color=INK, lw=2)
    xs = np.linspace(-1, 1, 300)
    men = 1 - np.sqrt(1 - xs * xs)  # hémisphère : bas en z = 0, bords en z = 1
    ax.fill_between(xs, -1.2, 0, color=BLEU, alpha=0.25, lw=0)
    # anneau oublié : le liquide au-dessus du bas du ménisque
    ax.fill_between(xs, 0, men, color=ORANGE, alpha=0.55, lw=0)
    ax.plot(xs, men, color=BLEU, lw=2)
    ax.plot([-1, 1], [0, 0], color=INK, lw=1, ls=(0, (4, 3)))
    # cône de même volume (tranches de même aire π(a − z)²)
    ax.plot([-1, 0, 1], [0, 1, 0], color=INK2, lw=1, ls=(0, (2, 2)))
    ax.text(0, -0.2, "lecture au bas du ménisque", ha="center", fontsize=8.5, color=INK)
    ax.text(0, 1.12, "anneau oublié (orange) = cylindre − hémisphère\n= le cône pointillé : π a³/3", ha="center", fontsize=8.5, color=INK)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.35, 1.5)
    ax.set_title("a)  Eau dans un tube fin")
    ax = axs[1]
    th = np.linspace(0, 180, 721)
    th = th[np.abs(th - 90) > 0.05]
    ax.plot(th, ar.anneau_menisque(th), color=BLEU, lw=2.2)
    ax.axvline(90, color=MUTED, lw=1)
    for (t, nom, xt, yt, ha) in [(0, "eau (θ ≈ 0°)", 8, 0.315, "left"), (140, "mercure (θ ≈ 140°)", 136, 0.235, "right")]:
        v = float(ar.anneau_menisque(t))
        point(ax, t, v, ORANGE if t else AQUA, 9)
        ax.text(xt, yt, f"{nom}\n{fr(v, 3)} π a³", fontsize=9, ha=ha, va="top", color=INK)
    ax.text(36, 0.07, "concave\n(le liquide mouille)", fontsize=9, color=INK2, ha="center")
    ax.text(144, 0.07, "convexe\n(il ne mouille pas)", fontsize=9, color=INK2, ha="center")
    ax.set_xlabel("angle de contact θ (°)")
    ax.set_ylabel("volume oublié / (π a³) = hauteur / a")
    ax.set_title("b)  L'inversion vient du mouillage")
    ax.set_xlim(0, 180)
    ax.set_ylim(0, 0.37)
    ax = axs[2]
    a = np.logspace(-4.3, -2, 200)
    for liq, coul in [("eau", AQUA), ("mercure", ORANGE)]:
        lc = ar.longueur_capillaire(liq)
        ok = a <= lc
        ax.loglog(a[ok] * 1000, np.abs(ar.jurin(liq, a[ok])) * 1000, color=coul, lw=2)
        ax.loglog(a[~ok] * 1000, np.abs(ar.jurin(liq, a[~ok])) * 1000, color=coul, lw=1.2, alpha=0.35)
        ax.axvline(lc * 1000, color=coul, lw=1, ls=(0, (4, 3)))
    ax.text(0.07, 300, "eau : monte", fontsize=9, color=INK)
    ax.text(0.07, 30, "mercure : descend", fontsize=9, color=INK)
    ax.text(0.06, 1.0, "tirets : longueurs capillaires (1,9 et 2,7 mm) ;\nau-delà, la loi de Jurin ne vaut plus", fontsize=8.8, color=INK2)
    ax.set_xlabel("rayon du tube a (mm)")
    ax.set_ylabel("hauteur de Jurin |h| (mm)")
    ax.set_title("c)  Plus le tube est fin, plus ça monte")
    sauver(fig, "b4_menisque.png")


# ===========================================================================
# b5 — Riemann, niveaux, contour
# ===========================================================================
def fig_decoupes():
    r2 = 1.1587284730181215
    mp.mp.dps = 30
    fz = lambda z: mp.sin(z) - z * mp.cos(z) - mp.pi / 2
    Ns = np.unique(np.round(np.logspace(np.log10(4), 3, 22)).astype(int))
    e1 = [abs(brentq(lambda r: ar.aire_riemann(r, N) - pi / 2, 0.8, 1.6, xtol=1e-15) - r2) for N in Ns]
    e2 = [abs(brentq(lambda r: ar.aire_niveaux(r, N) - pi / 2, 0.8, 1.6, xtol=1e-15) - r2) for N in Ns]
    Ng = [2, 3, 4, 5, 6, 7, 8, 10, 12, 14]
    e3 = [max(abs(brentq(lambda r: ar.aire_niveaux(r, N, True) - pi / 2, 0.8, 1.6, xtol=1e-15) - r2), 1e-16) for N in Ng]
    Nc = [4, 6, 8, 12, 16, 24, 32, 40, 48]
    e4 = [max(float(abs(2 * mp.cos(ch.racine_par_quotient(fz, 3 * mp.pi / 4, mp.pi / 4, N).real / 2)
                         - mp.mpf("1.1587284730181215178282335"))), 1e-16) for N in Nc]
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    for xs, ys, c, lab in [(Ns, e1, BLEU, "bandes verticales (Riemann) : erreur en N^−1,5"),
                           (Ns, e2, ORANGE, "niveaux de distance, point milieu : en N^−2"),
                           (Ng, e3, AQUA, "niveaux de distance, Gauss : exponentielle"),
                           (Nc, e4, INK, "contour d'Ullisch : exponentielle (0,453^N)")]:
        ax.loglog(xs, ys, "-o", color=c, lw=1.8, ms=4.5, mec=SURF, mew=1, label=lab)
    ax.set_ylim(1e-17, 0.1)
    ax.set_xlabel("nombre de subdivisions N")
    ax.set_ylabel("erreur sur la corde de la chèvre")
    ax.set_title("Comment on découpe change tout : 4 façons de calculer la même aire")
    ax.legend(loc="lower left", fontsize=9)
    sauver(fig, "b5_riemann_lebesgue_contour.png")


# ===========================================================================
# b6 — dimensions : la projection de la sphère, l'unité qui déplace les maxima
# ===========================================================================
def fig_dimensions_unite():
    fig, axs = plt.subplots(1, 2, figsize=(13.5, 4.8), gridspec_kw={"wspace": 0.28})
    ax = axs[0]
    z = np.linspace(-0.995, 0.995, 600)
    labs = {2: "n = 2 : l'aire file vers les bords", 3: "n = 3 : uniforme (Archimède)", 4: "n = 4",
            10: "n = 10 : presque tout sur l'équateur"}
    for n, c in zip([2, 3, 4, 10], ["#86b6ef", ORANGE, "#2a78d6", "#104281"]):
        ax.plot(z, ar.densite_projection(n, z), color=c, lw=2.2 if n == 3 else 1.8, label=labs[n])
    ax.legend(loc="upper center", fontsize=9)
    ax.set_ylim(0, 1.75)
    ax.set_xlabel("hauteur z sur l'axe")
    ax.set_ylabel("densité de l'aire de la sphère projetée")
    ax.set_title("a)  La 3D est le point d'équilibre")
    ax = axs[1]
    R = np.linspace(0.6, 3.2, 120)
    nv = [ar.dimension_du_maximum(x) for x in R]
    ns = [ar.dimension_du_maximum(x, "surface") for x in R]
    ax.step(R, nv, where="mid", color=BLEU, lw=2)
    ax.step(R, ns, where="mid", color=ORANGE, lw=2)
    ax.plot(R, 2 * np.pi * R * R - 1, color=INK, lw=1.2, ls=(0, (4, 3)))
    point(ax, 1, 5, BLEU, 9)
    point(ax, 1, 7, ORANGE, 9)
    ax.annotate("R = 1 : maxima en\nn = 5 (volume) et 7 (aire)", xy=(1.0, 6.0), xytext=(0.65, 26), fontsize=9,
                color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.text(2.2, 22, "tirets : 2πR² − 1", fontsize=9, color=INK2)
    ax.legend(handles=[plt.Line2D([], [], color=BLEU, lw=2, label="dimension du volume maximal"),
                       plt.Line2D([], [], color=ORANGE, lw=2, label="dimension de l'aire maximale")], loc="upper left", fontsize=9)
    ax.set_xlabel("rayon R choisi comme unité")
    ax.set_ylabel("dimension n")
    ax.set_title("b)  Les maxima en 5 et 7 viennent de l'unité R = 1")
    sauver(fig, "b6_dimensions_unite.png")


# ===========================================================================
# b7 — chèvres entre la 2D et la 3D
# ===========================================================================
def fig_cordes():
    import json
    with open(os.path.join(os.path.dirname(__file__), "..", "resultats", "archimede.json")) as fh:
        c = json.load(fh)["cordes_T"]
    lignes = [("disque", c["disque"], "2D", BLEU), ("carré (milieu d'un côté)", c["carre"], "2D", BLEU),
              ("boule", c["boule"], "3D", ORANGE), ("cylindre − double cône\n(même volume que la boule)", c["anneau"], "3D", ORANGE),
              ("cylindre", c["cylindre"], "3D", ORANGE), ("cube", c["cube"], "3D", ORANGE)]
    fig, ax = plt.subplots(figsize=(9.5, 4.6))
    y = np.arange(len(lignes))[::-1]
    for yi, (nom, v, d, col) in zip(y, lignes):
        ax.hlines(yi, 1.1, v, color=BASE, lw=2)
        point(ax, v, yi, col, 10)
        ax.text(v + 0.006, yi + 0.18, fr(v, 4), fontsize=9.5, color=INK)
    ax.axvline(sqrt(2), color=INK, lw=1.2, ls=(0, (4, 3)))
    ax.text(sqrt(2) - 0.004, y[0] + 0.3, "√2", fontsize=10, color=INK, ha="right")
    ax.set_yticks(y)
    ax.set_yticklabels([l[0] for l in lignes])
    ax.set_xlim(1.1, 1.45)
    ax.set_xlabel("corde qui broute la moitié (piquet au contact sphère–cylindre–cube)")
    ax.set_title("Même piquet, contenants différents")
    ax.grid(axis="y", visible=False)
    sauver(fig, "b7_cordes_2D_3D.png")


# ===========================================================================
# b8 — glisser le disque de la moitié
# ===========================================================================
def fig_glissement():
    d_eq = brentq(lambda d: ch.corde_moitie(2, d) - 1.0, 0.5, 1.0)
    d_p = brentq(lambda d: ch.corde_moitie(2, d) ** 2 + d * d - 1, 0.4, 0.8)
    cas = [(0.0, "δ = 0 : concentrique"), (1 - 1 / sqrt(2), "δ = 0,293 : tangence intérieure"),
           (d_p, "δ = 0,566 : la corde commune passe par P"), (d_eq, "δ = 0,808 : k = 1 (FTM50)"),
           (1.0, "δ = 1 : chèvre classique"), (1.6, "δ = 1,6 : piquet dehors")]
    fig, axs = plt.subplots(2, 3, figsize=(13.5, 9.0))
    for ax, (d, titre) in zip(axs.flat, cas):
        k = ch.corde_moitie(2, d)
        ax.set_aspect("equal")
        ax.axis("off")
        # lentille / disque
        ax.add_patch(mpatches.Circle((0, 0), 1, fc=BLEU, alpha=0.07, lw=0))
        cercle(ax, (0, 0), 1, color=INK, lw=1.6)
        xs = np.linspace(-1, 1, 800)
        hf = np.sqrt(np.clip(1 - xs * xs, 0, None))
        hc = np.sqrt(np.clip(k * k - (xs - d) ** 2, 0, None))
        h = np.minimum(hf, hc)
        ax.fill_between(xs, -h, h, where=h > 0, color=BLEU, alpha=0.3, lw=0)
        cercle(ax, (d, 0), k, color=BLEU, lw=1.8)
        point(ax, d, 0, ORANGE, 8)
        if k < 1 - 1e-9:
            w = sqrt(1 - k * k)
            ax.plot([-w, w], [k, k], color=AQUA, lw=1.4)
            ax.plot([-w, w], [-k, -k], color=AQUA, lw=1.4)
            for sx in (-w, w):
                for sy in (-k, k):
                    point(ax, sx, sy, AQUA, 6)
        if d > abs(1 - k) + 1e-9:
            x0 = (1 + d * d - k * k) / (2 * d)
            y0 = sqrt(max(0, 1 - x0 * x0))
            ax.plot([d, x0, d, x0], [0, y0, 0, -y0], color=INK2, lw=1)
            point(ax, x0, y0, INK, 6)
            point(ax, x0, -y0, INK, 6)
            ax.text(1.07, -2.0, f"k = {fr(k, 4)} ; Q à x₀ = {fr(x0, 3)}, y₀ = ±{fr(y0, 3)}", ha="center", fontsize=9, color=INK2)
        else:
            ax.text(1.07, -2.0, f"k = {fr(k, 4)} ; pas encore de point d'intersection", ha="center", fontsize=9, color=INK2)
        ax.set_title(titre, fontsize=10.5)
        ax.set_xlim(-1.2, 3.35)
        ax.set_ylim(-2.15, 1.8)
    fig.suptitle("Le disque de la moitié glisse : la proportion reste 50 %, la forme se réorganise",
                 x=0.01, ha="left", fontsize=12.5, fontweight="bold")
    fig.text(0.01, 0.935, "Vert : les tangentes au disque de corde parallèles à la ligne des centres coupent le champ en 4 points "
             "(un carré tant que k = 1/√2, rien dès que k ≥ 1). Points noirs : Q et Q'.", fontsize=9.5, color=INK2)
    sauver(fig, "b8_glissement_50.png")


# ===========================================================================
# b9 — erreur des polygones et des polyèdres
# ===========================================================================
def fig_polygones():
    import json
    with open(os.path.join(os.path.dirname(__file__), "..", "resultats", "archimede.json")) as fh:
        d = json.load(fh)
    r2, r3 = 1.1587284730181215, 1.2285448637352209
    P2 = np.array(d["polygones"], float)
    fig, axs = plt.subplots(1, 2, figsize=(13.5, 4.9), gridspec_kw={"wspace": 0.25})
    ax = axs[0]
    ax.loglog(P2[:, 0], np.abs(P2[:, 1] - r2), "-o", color=BLEU, lw=1.8, ms=5, mec=SURF, label="polygone inscrit, piquet sur un sommet")
    ax.loglog(P2[:, 0], np.abs(P2[:, 2] - r2), "-o", color=ORANGE, lw=1.8, ms=5, mec=SURF, label="polygone circonscrit, piquet au milieu d'un côté")
    n = np.array([6, 200])
    ax.loglog(n, 1.0 / n ** 2, color=INK, lw=1, ls=(0, (4, 3)))
    ax.text(30, 1.6e-3, "1/n²", fontsize=9.5, color=INK)
    point(ax, 96, abs(P2[P2[:, 0] == 96][0, 1] - r2), BLEU, 9)
    ax.text(70, 4e-5, "96 côtés,\ncomme Archimède", fontsize=9, color=INK2, ha="right")
    ax.set_xlabel("nombre de côtés n")
    ax.set_ylabel("|corde − 1,158728|")
    ax.set_title("a)  Plan : erreur en 1/n²")
    ax.legend(loc="lower left", fontsize=9)
    ax = axs[1]
    noms = [p[0] for p in d["polyedres"]]
    faces = np.array([p[2] for p in d["polyedres"]], float)
    err = np.array([abs(p[4] - r3) for p in d["polyedres"]])
    ax.loglog(faces, err, "o", color=ORANGE, ms=8, mec=SURF)
    nf = np.array([20, 2000])
    ax.loglog(nf, 1.65 / nf, color=INK, lw=1, ls=(0, (4, 3)))
    ax.text(300, 9e-3, "1,65 / faces", fontsize=9.5, color=INK)
    lab = {"tetra": "tétraèdre", "octa": "octaèdre", "cube": "cube", "icosa": "icosaèdre", "dodeca": "dodécaèdre",
           "geo2": "géodésique ν=2", "geo4": "ν=4", "geo8": "ν=8"}
    pos = {"tetra": (1.1, 1.15), "octa": (0.55, 0.78), "cube": (1.1, 1.18), "icosa": (1.12, 1.15),
           "dodeca": (1.12, 0.82), "geo2": (1.12, 1.15), "geo4": (1.12, 0.82), "geo8": (1.1, 1.18)}
    for nm, f_, e in zip(noms, faces, err):
        fx, fy = pos[nm]
        ax.text(f_ * fx, e * fy, lab[nm], fontsize=8.5, color=INK2, ha="right" if fx < 1 else "left")
    ax.set_xlabel("nombre de faces triangulaires")
    ax.set_ylabel("|corde − 1,228545|")
    ax.set_title("b)  Espace : erreur en 1/(nombre de faces)")
    sauver(fig, "b9_polygones_polyedres.png")


if __name__ == "__main__":
    quoi = sys.argv[1:] or ["projections", "tranches", "cube", "menisque", "decoupes", "dims", "cordes", "glissement", "polygones"]
    table = {"projections": fig_projections, "tranches": fig_tranches, "cube": fig_cube_tournant,
             "menisque": fig_menisque, "decoupes": fig_decoupes, "dims": fig_dimensions_unite,
             "cordes": fig_cordes, "glissement": fig_glissement, "polygones": fig_polygones}
    for q in quoi:
        table[q]()
