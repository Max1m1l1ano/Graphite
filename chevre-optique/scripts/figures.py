"""
Génère toutes les figures de l'analyse dans ../figures/.

    python3 scripts/figures.py
"""

import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap, ListedColormap  # noqa: E402

sys.path.insert(0, os.path.dirname(__file__))
import chevre as ch  # noqa: E402

ICI = os.path.dirname(os.path.abspath(__file__))
DOSSIER = os.path.join(ICI, "..", "figures")
os.makedirs(DOSSIER, exist_ok=True)

# --- palette (validée : catégorielle 1-3, rampe ordinale bleue 250→650) -----
SURF, INK, INK2, MUTED, GRID, BASE = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
BLEU, ORANGE, AQUA, JAUNE = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
RAMPE = ["#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#104281"]  # n = 1, 2, 3, 10, 100
SEQ = ["#fcfcfb", "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
       "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"]

plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "axes.edgecolor": BASE, "axes.labelcolor": INK2, "axes.titlecolor": INK,
    "xtick.color": MUTED, "ytick.color": MUTED, "xtick.labelcolor": INK2, "ytick.labelcolor": INK2,
    "text.color": INK, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False, "axes.axisbelow": True,
    "font.size": 10, "axes.titlesize": 11.5, "axes.titleweight": "bold", "axes.titlelocation": "left",
    "lines.linewidth": 1.8, "lines.solid_capstyle": "round", "lines.solid_joinstyle": "round",
    "legend.frameon": False, "mathtext.fontset": "dejavusans",
})


def sauver(fig, nom):
    chemin = os.path.join(DOSSIER, nom)
    fig.savefig(chemin, dpi=160, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print("figure :", chemin)


def point(ax, x, y, couleur=INK, taille=7, z=6):
    ax.plot([x], [y], "o", ms=taille, color=couleur, mec=SURF, mew=1.6, zorder=z)


def cercle(ax, c, r, **kw):
    t = np.linspace(0, 2 * np.pi, 600)
    ax.plot(c[0] + r * np.cos(t), c[1] + r * np.sin(t), **kw)


def remplir_intersection(ax, r, couleur, alpha):
    """Remplit B(O,1) ∩ B(P,r) et B(O,1) \\ B(P,r), P = (1, 0)."""
    xs = np.linspace(-1, 1, 1200)
    haut = np.sqrt(1 - xs**2)
    # bord de la corde : (x-1)² + y² = r²
    yc = np.sqrt(np.clip(r**2 - (xs - 1) ** 2, 0, None))
    lo_lentille = np.minimum(haut, yc)
    ax.fill_between(xs, -lo_lentille, lo_lentille, where=(yc > 0), color=couleur[0], alpha=alpha, lw=0)
    reste = np.where(yc < haut, haut, np.nan)
    ax.fill_between(xs, yc, reste, where=(yc < haut), color=couleur[1], alpha=alpha, lw=0)
    ax.fill_between(xs, -reste, -yc, where=(yc < haut), color=couleur[1], alpha=alpha, lw=0)


# ===========================================================================
# Figure 1 — géométrie : n = 2, coupe n = 3, limite n → ∞
# ===========================================================================
def fig_geometrie():
    r2 = 1.1587284730181215
    r3 = 1.2285448637352209
    part3 = float(ch.aire_lentille(1.0, r3, 1.0) / np.pi)
    fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.4))
    cas = [
        (axs[0], r2, "a)  Plan (n = 2) : r = 1,1587 R", "lentille\n50 %", "lunule\n50 %",
         "aires égales"),
        (axs[1], r3, "b)  Boule (n = 3), coupe : r = 1,2285 R", "lentille\n50 %", "ménisque\n50 %",
         f"lentille biconvexe et ménisque de volumes égaux\n(dans la coupe, la lentille couvre {part3:.0%} de l'aire)".replace("%", " %")),
        (axs[2], np.sqrt(2), "c)  Limite n → ∞ : r = √2 R", "", "",
         "en 2D cette corde broute 68 % de l'aire ;\nen dimension infinie, exactement 50 % du volume"),
    ]
    for ax, r, titre, lab_in, lab_out, note in cas:
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(titre, pad=4)
        remplir_intersection(ax, r, (BLEU, ORANGE), 0.16)
        cercle(ax, (0, 0), 1, color=INK, lw=1.6, zorder=3)
        a = np.arccos(r / 2)  # angle en P entre PO et PQ
        t = np.linspace(np.pi - a, np.pi + a, 300)
        ax.plot(1 + r * np.cos(t), r * np.sin(t), color=BLEU, lw=2, zorder=4)
        t2 = np.linspace(-np.pi + a, np.pi - a, 400)
        ax.plot(1 + r * np.cos(t2), r * np.sin(t2), color=BLEU, lw=1, alpha=0.3, zorder=2)
        x0 = 1 - r**2 / 2
        yq = np.sqrt(1 - x0**2)
        ax.plot([x0, x0], [-yq, yq], color=MUTED, lw=1, zorder=3)
        ax.plot([0, 1], [0, 0], color=INK2, lw=1, zorder=3)
        ax.plot([1, x0], [0, yq], color=INK2, lw=1, zorder=3)
        ax.plot([0, x0], [0, yq], color=INK2, lw=1, zorder=3)
        for (x, y, nom, dx, dy) in [(0, 0, "O", 0.07, -0.15), (1, 0, "P", 0.1, -0.05),
                                    (x0, yq, "Q", -0.06, 0.1), (x0, -yq, "Q'", -0.02, -0.2)]:
            point(ax, x, y, INK, 6)
            ax.text(x + dx, y + dy, nom, fontsize=11, color=INK, ha="center", va="center")
        ta = np.linspace(np.pi - a, np.pi, 40)
        ax.plot(1 + 0.24 * np.cos(ta), 0.24 * np.sin(ta), color=INK, lw=1)
        ax.text(1 - 0.36, 0.12, "α", fontsize=11, ha="center", va="center")
        if lab_in:
            ax.text(0.6, -0.42, lab_in, ha="center", va="center", fontsize=9.5, color=INK)
            ax.text(-0.55, -0.12, lab_out, ha="center", va="center", fontsize=9.5, color=INK)
        x0txt = "0" if abs(x0) < 1e-9 else f"{x0:.3f}".replace(".", ",")
        ax.text(0.5, -1.45, f"QQ' à x₀ = {x0txt} R de O ;  r = 2 cos α", ha="center", fontsize=9, color=INK2)
        ax.text(0.5, -1.65, note, ha="center", va="top", fontsize=9, color=INK2)
        ax.set_xlim(-1.25, 2.45)
        ax.set_ylim(-2.15, 1.35)
    ax = axs[2]
    ax.add_patch(mpatches.Polygon([[0, 0], [1, 0], [1, 1], [0, 1]], closed=True, fill=False,
                                  ec=ORANGE, lw=1.6, zorder=5))
    ax.plot([1, 0], [0, 1], color=ORANGE, lw=2.6, zorder=6)
    ax.text(0.37, 0.37, "√2 R", color=INK, fontsize=12, fontweight="bold", rotation=-45, ha="center",
            va="center", zorder=7)
    ax.text(1.08, 0.62, "carré construit\nsur deux rayons\nperpendiculaires", fontsize=8.8, color=INK2, va="center")
    fig.suptitle("Problème de la chèvre : piquet P sur la clôture, corde r qui donne la moitié du champ",
                 x=0.01, ha="left", fontsize=12.5, fontweight="bold", y=0.99)
    sauver(fig, "fig1_geometrie.png")


# ===========================================================================
# Figure 2 — plan complexe : contour d'Ullisch + convergence des trapèzes
# ===========================================================================
def fig_contour():
    f = lambda z: np.sin(z) - z * np.cos(z) - np.pi / 2
    X, Y = np.meshgrid(np.linspace(-1.6, 9.2, 900), np.linspace(-2.6, 2.6, 440))
    Z = X + 1j * Y
    L = np.log10(np.abs(f(Z)) + 1e-12)
    fig, axs = plt.subplots(1, 2, figsize=(14, 4.6), gridspec_kw={"width_ratios": [2.15, 1], "wspace": 0.42})
    ax = axs[0]
    cmap = LinearSegmentedColormap.from_list("bleu", SEQ[1:])
    im = ax.imshow(L, extent=(-1.6, 9.2, -2.6, 2.6), origin="lower", cmap=cmap, vmin=-1, vmax=2.5,
                   aspect="equal", interpolation="bilinear")
    ax.grid(False)
    cb = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.015)
    cb.set_label("log₁₀ |f(z)|", color=INK2)
    cb.outline.set_edgecolor(BASE)
    zeros = [(-0.70571226, -1.4268094), (-0.70571226, 1.4268094), (1.9056957, 0), (4.0903295, 0), (7.9263876, 0)]
    c, rho = 3 * np.pi / 4, np.pi / 4
    cercle(ax, (c, 0), rho, color=INK, lw=2)
    t = 0.9
    ax.annotate("", xy=(c + rho * np.cos(t + 0.25), rho * np.sin(t + 0.25)),
                xytext=(c + rho * np.cos(t), rho * np.sin(t)),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.6, mutation_scale=14))
    for (x, y) in zeros:
        point(ax, x, y, ORANGE, 8)
    ax.text(c, -1.12, "β = 1,9057…", ha="center", fontsize=10, color=INK, fontweight="bold")
    ax.text(c, rho + 0.18, "contour |z − 3π/4| = π/4", ha="center", fontsize=9.5, color=INK)
    ax.text(4.09, 0.25, "autre zéro réel\n(hors contour)", ha="center", fontsize=8.5, color=INK2)
    ax.text(-1.45, 1.78, "zéros complexes", ha="left", fontsize=8.5, color=INK2)
    ax.set_xlabel("Re z")
    ax.set_ylabel("Im z")
    ax.set_title("a)  f(z) = sin z − z cos z − π/2 : un seul zéro dans le contour")
    # convergence
    ax = axs[1]
    mp.mp.dps = 60
    fm = lambda z: mp.sin(z) - z * mp.cos(z) - mp.pi / 2
    beta = mp.findroot(fm, 1.9)
    Ns = [4, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 56, 64, 80, 96]
    errs = [float(abs(ch.racine_par_quotient(fm, 3 * mp.pi / 4, mp.pi / 4, N) - beta)) for N in Ns]
    nth = np.array([4, 96])
    taux = (np.pi / 4) / (4.0903295 - 3 * np.pi / 4)  # rayon du contour / distance au zéro voisin
    ax.semilogy(nth, errs[0] * taux ** (nth - 4.0), color=INK, lw=1.2, ls=(0, (4, 3)))
    ax.semilogy(Ns, errs, "-", color=BLEU, lw=1.8)
    for N, e in zip(Ns, errs):
        point(ax, N, e, BLEU, 6)
    ax.set_xlabel("nombre de points N sur le cercle (règle des trapèzes)")
    ax.set_ylabel("|erreur sur β|")
    ax.set_title("b)  Convergence exponentielle du quotient")
    ax.text(22, 1e-3, "≈ 1 chiffre exact de plus tous les 3 points\n"
            "tirets : prévision $(\\rho/d)^N = 0{,}453^N$\n(d = distance au zéro voisin 4,09)", fontsize=9,
            color=INK2, va="top")
    ax.set_ylim(1e-40, 1)
    sauver(fig, "fig2_contour_ullisch.png")
    mp.mp.dps = 30


# ===========================================================================
# Figure 3 — dimensions : fraction broutée, r_n, écart à √(2n/(n+1))
# ===========================================================================
def fig_dimensions():
    fig, axs = plt.subplots(1, 3, figsize=(15.5, 4.6), gridspec_kw={"wspace": 0.3})
    ax = axs[0]
    rr = np.linspace(0, 2, 801)
    ns = [1, 2, 3, 10, 100]
    for n, coul in zip(ns, RAMPE):
        if n == 1:
            y = np.clip(rr / 2, 0, 1)
        else:
            y = ch.fraction_broutee(n, rr, 1.0)
        ax.plot(rr, y, color=coul, lw=2)
        rn = ch.corde_moitie(n, 1.0)
        point(ax, rn, 0.5, coul, 7)
    ax.plot([0, np.sqrt(2), np.sqrt(2), 2], [0, 0, 1, 1], color=INK, lw=1.4, ls=(0, (4, 3)))
    ax.axhline(0.5, color=MUTED, lw=1)
    ax.legend(handles=[plt.Line2D([], [], color=c, lw=2, label=f"n = {n}") for n, c in zip(ns, RAMPE)] +
              [plt.Line2D([], [], color=INK, lw=1.4, ls=(0, (4, 3)), label="n → ∞ (marche en √2)")],
              loc="upper left", fontsize=9)
    ax.text(0.05, 0.53, "moitié du volume", fontsize=9, color=INK2)
    ax.set_xlabel("longueur de corde r / R (piquet sur le bord)")
    ax.set_ylabel("fraction du volume broutée")
    ax.set_title("a)  Fraction broutée selon la corde")
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1.02)
    # r_n vs n
    ax = axs[1]
    n_all = np.array(list(range(1, 21)) + [30, 50, 100, 200, 500, 1000, 3000, 10000])
    r_all = np.array([ch.corde_moitie(int(n), 1.0) if n > 1 else 1.0 for n in n_all])
    nn = np.logspace(0, 4, 400)
    ax.semilogx(nn, np.sqrt(2 * nn / (nn + 1)), color=BASE, lw=3.2, solid_capstyle="round")
    ax.semilogx(n_all, r_all, "o", ms=6, color=BLEU, mec=SURF, mew=1.4, zorder=5)
    ax.axhline(np.sqrt(2), color=INK, lw=1.2, ls=(0, (4, 3)))
    ax.text(1.0, np.sqrt(2) + 0.007, "√2 = 1,41421…  (diagonale du carré de côté R)", fontsize=9, color=INK, va="bottom")
    point(ax, 2, r_all[1], ORANGE, 9)
    ax.annotate("n = 2 : 1,15873 (Ullisch 2020)", xy=(2, r_all[1]), xytext=(4.2, 1.10), fontsize=9,
                color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.annotate("n = 3 : 1,22854 (quartique)", xy=(3, r_all[2]), xytext=(8, 1.19), fontsize=9,
                color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.text(60, 1.335, "trait gris : √(2n/(n+1))", fontsize=9, color=INK2)
    ax.set_xlabel("dimension n")
    ax.set_ylabel("r_n / R")
    ax.set_title("b)  La corde tend vers √2 R")
    ax.set_ylim(0.97, 1.45)
    # écart
    ax = axs[2]
    mp.mp.dps = 30
    n_e = [2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 30, 50, 100, 200, 500, 1000, 3000, 10000]
    ecarts = [float(ch.corde_moitie_mp(n) - mp.sqrt(2 * mp.mpf(n) / (n + 1))) for n in n_e]
    ax.loglog(n_e, ecarts, "-", color=BLEU, lw=1.8)
    for n, e in zip(n_e, ecarts):
        point(ax, n, e, ORANGE if n == 2 else BLEU, 9 if n == 2 else 6)
    nn = np.logspace(np.log10(20), 4, 50)
    ax.loglog(nn, (2 / 3) / (2 * np.sqrt(2)) / nn**2, color=INK, lw=1.2, ls=(0, (4, 3)))
    ax.text(400, 4e-5, "pente −2 :\n≈ 1/(3√2 n²)", fontsize=9, color=INK)
    ax.text(2.4, 0.0048, "maximum en n = 2", fontsize=9, color=INK)
    ax.set_xlabel("dimension n")
    ax.set_ylabel("r_n − √(2n/(n+1))")
    ax.set_title("c)  La loi simple est la moins juste en 2D")
    sauver(fig, "fig3_dimensions.png")


# ===========================================================================
# Figure 4 — volume, surface, concentration de la mesure
# ===========================================================================
def fig_volume_surface():
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.3))
    ns = np.arange(1, 26)
    V = np.array([ch.volume_boule(n) for n in ns])
    S = np.array([ch.surface_sphere(n) for n in ns])
    for ax, val, nom, titre in [(axs[0], V, "V_n", "a)  Volume de la boule unité"),
                                (axs[1], S, "S_{n−1}", "b)  Aire de la sphère unité (= dV/dR)")]:
        ax.bar(ns, val, width=0.62, color=BLEU, zorder=3)
        i = int(np.argmax(val))
        ax.bar(ns[i], val[i], width=0.62, color="#104281", zorder=4)
        ax.text(ns[i], val[i] * 1.03, f"max en n = {ns[i]}\n{val[i]:.3f}".replace(".", ","), ha="center", va="bottom", fontsize=9)
        ax.set_xlabel("dimension n")
        ax.set_title(titre)
        ax.set_ylim(0, val.max() * 1.25)
        ax.grid(axis="x", visible=False)
    axs[0].text(14, 4.2, "V₂ = π,  V₃ = 4π/3\nV₅ = 8π²/15 ≈ 5,264", fontsize=9, color=INK2)
    axs[1].text(13, 30, "S₁ = 2π,  S₂ = 4π\nS₆ = 16π³/15 ≈ 33,07", fontsize=9, color=INK2)
    ax = axs[2]
    n = np.unique(np.round(np.logspace(0, 3, 200)).astype(int))
    coquille = 1 - 0.9**n
    tranche = np.array([1 - 2 * float(ch.fraction_calotte(int(k), np.arccos(0.1))) for k in n])
    ax.semilogx(n, coquille * 100, color=BLEU, lw=2)
    ax.semilogx(n, tranche * 100, color=ORANGE, lw=2)
    ax.text(1.15, 84, "dans la coquille\n0,9 R < |x| < R", fontsize=9, color=INK2)
    ax.text(70, 40, "à moins de 0,1 R\nde l'équateur", fontsize=9, color=INK2)
    ax.legend(handles=[mpatches.Patch(color=BLEU, label="coquille extérieure"),
                       mpatches.Patch(color=ORANGE, label="tranche équatoriale")], loc="lower right", fontsize=9)
    ax.set_xlabel("dimension n")
    ax.set_ylabel("% du volume")
    ax.set_title("c)  Concentration : tout le volume fuit vers le bord… et l'équateur")
    ax.set_ylim(0, 102)
    sauver(fig, "fig4_volume_surface.png")


# ===========================================================================
# Figure 5 — diagramme des paramètres (δ, k) en 2D
# ===========================================================================
def etiquette_le_long(ax, x, y, pente, texte, decal, **kw):
    """Texte parallèle à une courbe (repère orthonormé), décalé perpendiculairement de `decal`."""
    ang = np.arctan(pente)
    nx, ny = -np.sin(ang), np.cos(ang)
    ax.text(x + decal * nx, y + decal * ny, texte, rotation=np.degrees(ang), rotation_mode="anchor",
            ha="center", va="center", **kw)


def fig_parametres():
    fig, ax = plt.subplots(figsize=(10.2, 9.4))
    d = np.linspace(0.0005, 3, 700)
    k = np.linspace(0.0005, 3.2, 700)
    D, K = np.meshgrid(d, k)
    F = ch.aire_lentille(1.0, K, D) / np.pi
    niveaux = [0, 1e-9, 0.1, 0.25, 0.5, 0.75, 0.9, 1 - 1e-9, 1.0001]
    couleurs = ["#fcfcfb", "#e6f0fd", "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7"]
    cf = ax.contourf(D, K, F, levels=niveaux, colors=couleurs)
    ax.contour(D, K, F, levels=[0.1, 0.25, 0.75, 0.9], colors=[BASE], linewidths=0.8)
    ax.contour(D, K, F, levels=[0.5], colors=[BLEU], linewidths=2.8)
    ax.grid(False)
    ax.set_aspect("equal")
    cb = fig.colorbar(cf, ax=ax, fraction=0.035, pad=0.02, ticks=[0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0],
                      spacing="proportional")
    cb.ax.set_yticklabels(["0 %", "10 %", "25 %", "50 %", "75 %", "90 %", "100 %"])
    cb.set_label("fraction du champ couverte (herbe broutée, obscuration, lumière transmise…)", color=INK2)
    cb.outline.set_edgecolor(BASE)
    # bande des éclipses réelles
    ax.axhspan(0.90, 1.08, color=JAUNE, alpha=0.18, lw=0)
    ax.text(2.97, 0.99, "éclipses réelles : 0,90–1,08", ha="right", va="center", fontsize=8.5, color=INK2)
    # droites de tangence, courbes remarquables
    x = np.linspace(0, 3, 10)
    for y in (1 - x, x - 1, 1 + x):
        ax.plot(x, y, color=INK, lw=1.3)
    xo = np.linspace(1, 3, 300)
    ax.plot(xo, np.sqrt(xo**2 - 1), color=INK2, lw=1.1, ls=(0, (2, 2.5)))
    xb = np.linspace(0, 3, 300)
    ax.plot(xb, np.sqrt(1 + xb**2), color=INK, lw=1.5, ls=(0, (6, 3)))
    ax.plot([1, 1], [0, 3.2], color=INK2, lw=0.8)
    kw = dict(fontsize=8.8, color=INK)
    etiquette_le_long(ax, 0.47, 0.53, -1, "k = 1 − δ : corde inscrite", 0.13, **kw)
    etiquette_le_long(ax, 2.3, 1.3, 1, "k = δ − 1 : tangence extérieure (1er et 4e contacts)", -0.1, **kw)
    etiquette_le_long(ax, 1.05, 2.05, 1, "k = 1 + δ : champ inscrit dans la corde", 0.1, **kw)
    xh = 2.35
    etiquette_le_long(ax, xh, np.sqrt(1 + xh**2), xh / np.sqrt(1 + xh**2), "k = √(1+δ²) : limite n → ∞", 0.1, **kw)
    x5 = 2.2
    k5 = ch.corde_moitie(2, x5)
    etiquette_le_long(ax, x5, k5, 1.0, "courbe des 50 % : chèvre généralisée", -0.075, fontsize=9.2,
                      color=INK, fontweight="bold")
    ax.text(1.03, 0.04, "δ = 1 : piquet au bord", fontsize=8.5, color=INK2)
    ax.text(0.33, 2.75, "champ entièrement\ndans la corde", fontsize=9, color=INK, ha="center")
    ax.text(0.2, 0.2, "corde\ndans le\nchamp", fontsize=8.5, color=INK2, ha="center")
    ax.text(2.62, 0.74, "disques disjoints", fontsize=9, color=INK2, ha="center")
    # points remarquables (lettres) + clé dans le coin libre
    pts = [(1, 1.1587285, ORANGE, "G", (0.05, 0.05)), (1, 1.0, INK, "V", (0.05, -0.1)),
           (0.8079455, 1.0, AQUA, "M", (-0.12, 0.04)), (0.0, 0.7071068, AQUA, "D", (0.05, 0.05)),
           (1, np.sqrt(2), INK, "√2", (-0.17, 0.04))]
    for (x0, y0, c, lab, (dx, dy)) in pts:
        point(ax, x0, y0, c, 9, z=8)
        ax.text(x0 + dx, y0 + dy, lab, fontsize=10, color=INK, fontweight="bold", zorder=9)
    cle = ("G   chèvre classique : δ = 1, k = 1,1587\n"
           "V   vesica piscis (cercles égaux) : 39,1 %\n"
           "M   FTM50 d'un objectif parfait : δ = 0,808\n"
           "D   un diaphragme : k = 1/√2, la moitié\n"
           "√2  limite de la chèvre quand n → ∞\n"
           "pointillés : k = √(δ²−1), cercle orthogonal\n"
           "     (par les contacts des tangentes du piquet)")
    ax.text(1.62, 0.13, cle, fontsize=8.5, color=INK, va="bottom", ha="left", family="DejaVu Sans",
            linespacing=1.45)
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3.2)
    ax.set_xlabel("δ = distance piquet–centre / R   (Lune–Soleil, décentrement…)")
    ax.set_ylabel("k = corde / R   (rayon Lune/Soleil, rayon du diaphragme…)")
    ax.set_title("Cercle dans un cercle (n = 2) : la carte de tous les recouvrements")
    sauver(fig, "fig5_diagramme_parametres.png")


# ===========================================================================
# Figure 6 — courbes des 50 % selon la dimension
# ===========================================================================
def fig_courbes50():
    fig, ax = plt.subplots(figsize=(9.5, 6.6))
    x = np.linspace(0, 3, 10)
    for y in [1 - x, x - 1, 1 + x]:
        ax.plot(x, y, color=BASE, lw=1.2)
    ds = np.linspace(0, 3, 241)
    for n, coul in zip([1, 2, 3, 10, 100], RAMPE):
        ks = [max(0.5, d) if n == 1 else ch.corde_moitie(n, d) for d in ds]
        ax.plot(ds, ks, color=coul, lw=2.2)
        dstar = 1 - 2 ** (-1 / n)
        point(ax, dstar, 2 ** (-1 / n), coul, 7)
        point(ax, 1, ks[80], coul, 7)
    ax.plot(ds, np.sqrt(1 + ds**2), color=INK, lw=1.5, ls=(0, (5, 3)))
    for n, (xx, yy) in zip([1, 2, 3, 10, 100], [(2.45, 2.25), (2.62, 2.58), (2.75, 2.76), (2.85, 2.95), (2.9, 3.13)]):
        pass
    ax.legend(handles=[plt.Line2D([], [], color=c, lw=2.2, label=f"n = {n}") for n, c in
                       zip([1, 2, 3, 10, 100], RAMPE)] +
              [plt.Line2D([], [], color=INK, lw=1.5, ls=(0, (5, 3)), label="n → ∞")],
              loc="upper left", fontsize=9.5, title="dimension", title_fontsize=9.5)
    ax.text(0.03, 0.06, "paliers $k = 2^{-1/n}$ : la boule de corde\nest dans le champ jusqu'à la tangence\nintérieure (point sur k = 1 − δ)",
            fontsize=8.8, color=INK2, va="bottom")
    ax.text(1.9, 0.06, "points sur δ = 1 (piquet au bord) :\nr₁ = 1 ; r₂ = 1,1587 ; r₃ = 1,2285 ;\nr₁₀ = 1,3495 ; r₁₀₀ = 1,4072 ; r∞ = √2",
            fontsize=8.8, color=INK2, va="bottom")
    ax.text(2.2, 0.85, "k = δ − 1", fontsize=8.5, color=MUTED, rotation=33)
    ax.text(0.55, 0.36, "", fontsize=8.5)
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3.3)
    ax.set_xlabel("δ = distance du piquet au centre / R")
    ax.set_ylabel("k = corde qui broute la moitié / R")
    ax.set_title("La chèvre généralisée : corde des 50 % pour tout δ, de la dimension 1 à l'infini")
    sauver(fig, "fig6_courbes50_dimensions.png")


# ===========================================================================
# Figure 7 — optique : FTM de diffraction, éclipses
# ===========================================================================
def fig_optique():
    fig, axs = plt.subplots(1, 2, figsize=(13.5, 4.8))
    ax = axs[0]
    s = np.linspace(0, 1, 500)
    ax.plot(s, ch.ftm_diffraction(s), color=BLEU, lw=2)
    ax.fill_between(s, 0, ch.ftm_diffraction(s), color=BLEU, alpha=0.08, lw=0)
    s50 = 0.4039727533
    ax.plot([s50, s50], [0, 0.5], color=MUTED, lw=1)
    ax.plot([0, s50], [0.5, 0.5], color=MUTED, lw=1)
    point(ax, s50, 0.5, ORANGE, 9)
    point(ax, 0.5, 0.39100222, INK, 7)
    ax.text(s50 + 0.025, 0.53, "FTM50 = 0,404 $\\nu_c$\n(ψ − sin ψ = π/2 : Kepler avec e = 1)", fontsize=9)
    ax.text(0.52, 0.40, "décalage d'un rayon :\nvesica piscis, 39,1 %", fontsize=9, color=INK2)
    # vignettes de pupilles
    for (sx, yy) in [(0.13, 0.13), (0.78, 0.62)]:
        pass
    ax.text(0.6, 0.86, "FTM(ν) = aire commune de deux\npupilles décalées de λ f ν\n($\\nu_c$ = 1/(λN))", fontsize=9,
            color=INK2)
    ax.set_xlabel("fréquence spatiale $\\nu / \\nu_c$")
    ax.set_ylabel("FTM (pupille circulaire parfaite)")
    ax.set_title("a)  Objectif limité par la diffraction")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.02)
    ax = axs[1]
    for k, coul in zip([0.90, 1.00, 1.08], [BLEU, ORANGE, AQUA]):
        d = np.linspace(abs(1 - k) + 1e-6, 1 + k, 600)
        mag = (1 + k - d) / 2
        obs = ch.aire_lentille(1.0, k, d) / np.pi
        ax.plot(mag, obs * 100, color=coul, lw=2)
        point(ax, k / 2, float(ch.aire_lentille(1.0, k, 1.0) / np.pi) * 100, coul, 7)
    ax.axhline(50, color=MUTED, lw=1)
    ax.text(0.03, 52, "50 % de la surface du Soleil", fontsize=9, color=INK2)
    ax.text(0.47, 20, "•  centre de la Lune\n    sur le bord du Soleil", fontsize=9, color=INK2)
    ax.text(0.62, 44, "≈ magnitude 0,6", fontsize=9, color=INK2)
    ax.legend(handles=[plt.Line2D([], [], color=c, lw=2, label=f"Lune/Soleil = {k:.2f}".replace(".", ",")) for k, c in
                       zip([0.90, 1.00, 1.08], [BLEU, ORANGE, AQUA])], loc="upper left", fontsize=9)
    ax.set_xlabel("magnitude (fraction du diamètre solaire couverte)")
    ax.set_ylabel("obscuration (% de la surface couverte)")
    ax.set_title("b)  Éclipse partielle : la même aire de lentille")
    ax.set_xlim(0, 1.05)
    ax.set_ylim(0, 102)
    sauver(fig, "fig7_optique.png")


# ===========================================================================
# Figure 8 — anneaux de Newton : contact plan, intérieur, extérieur
# ===========================================================================
def fig_newton():
    lam = 589.3e-9
    demi = 3.0e-3
    x = np.linspace(-demi, demi, 1400)
    X, Y = np.meshgrid(x, x)
    rho2 = X**2 + Y**2
    cmap = LinearSegmentedColormap.from_list("sodium", ["#141413", "#7a5200", "#f7c548", "#fff3c4"])
    cas = [(1.0, "lentille R₁ = 1 m sur un plan\n(sphère tangente à un plan)", "$R_\\mathrm{eff}$ = R₁ = 1 m"),
           (3.0, "dans un concave R₂ = 1,5 m\n(sphère dans une sphère)", "$1/R_\\mathrm{eff}$ = 1/R₁ − 1/R₂ → 3 m"),
           (0.6, "sur un convexe R₂ = 1,5 m\n(tangentes extérieurement)", "$1/R_\\mathrm{eff}$ = 1/R₁ + 1/R₂ → 0,6 m")]
    fig, axs = plt.subplots(1, 3, figsize=(13.5, 5.2))
    for ax, (Reff, titre, sous) in zip(axs, cas):
        t = rho2 / (2 * Reff)
        I = np.sin(2 * np.pi * t / lam) ** 2  # réflexion : noir au contact (déphasage π)
        ax.imshow(I, extent=(-demi * 1e3, demi * 1e3, -demi * 1e3, demi * 1e3), cmap=cmap, vmin=0, vmax=1,
                  origin="lower", interpolation="bilinear")
        ax.grid(False)
        r1 = np.sqrt(lam * Reff) * 1e3
        for m, ls in [(1, "-"), (2, (0, (3, 2)))]:
            cercle(ax, (0, 0), r1 * np.sqrt(m), color="#5598e7", lw=1.4, ls=ls)
        ax.set_title(titre, fontsize=10.5)
        ax.set_xlabel(f"{sous}\nρ₁ = {r1:.2f} mm ; ρ₂ = √2·ρ₁ (tirets)".replace(".", ","), fontsize=9.5)
        ax.set_yticks([])
        ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
        for sp in ax.spines.values():
            sp.set_visible(False)
    fig.suptitle("Anneaux de Newton en lumière du sodium (λ = 589,3 nm), même échelle en mm : "
                 "$\\rho_m = \\sqrt{m\\,\\lambda\\,R_\\mathrm{eff}}$, anneaux d'aires égales", x=0.01, ha="left",
                 fontsize=12, fontweight="bold", y=1.02)
    sauver(fig, "fig8_anneaux_newton.png")


# ===========================================================================
# Figure 9 — éclipses : contacts (tangences) et cônes d'ombre (tangentes communes)
# ===========================================================================
def fig_eclipse():
    fig = plt.figure(figsize=(13.5, 7.0))
    # --- ligne du haut : contacts d'une éclipse annulaire (k = 0,94) ---
    k = 0.94
    etapes = [(1 + k, "1er contact\ntangence extérieure"), (1.0, "partielle"),
              (1 - k, "2e contact\ntangence intérieure"), (0.0, "maximum\ncercle dans le cercle"),
              (-(1 - k), "3e contact\ntangence intérieure"), (-(1 + k), "4e contact\ntangence extérieure")]
    for i, (dx, lab) in enumerate(etapes):
        ax = fig.add_axes([0.005 + i * 0.166, 0.64, 0.16, 0.26])
        ax.set_aspect("equal")
        ax.axis("off")
        sol = mpatches.Circle((0, 0), 1, color=JAUNE, alpha=0.85, lw=0)
        ax.add_patch(sol)
        lune = mpatches.Circle((dx, 0), k, color="#3a3a38", lw=0)
        ax.add_patch(lune)
        ob = float(ch.aire_lentille(1.0, k, abs(dx)) / np.pi)
        ax.set_xlim(-2.95, 2.95)
        ax.set_ylim(-1.75, 1.05)
        ax.text(0, -1.12, f"{lab}\nobscuration {ob:.0%}".replace("%", " %"), ha="center", va="top", fontsize=9)
    fig.text(0.01, 0.93, "Éclipse annulaire (Lune/Soleil = 0,94) : les quatre contacts sont des tangences",
             fontsize=12, fontweight="bold")
    # --- ligne du bas : cônes d'ombre ---
    ax = fig.add_axes([0.03, 0.0, 0.94, 0.58])
    ax.set_aspect("equal")
    ax.axis("off")
    R1, R2, D = 1.6, 0.5, 5.4
    Ex = D * R1 / (R1 - R2)
    Ix = D * R1 / (R1 + R2)
    phi = np.arcsin((R1 - R2) / D)
    psi = np.arcsin((R1 + R2) / D)
    xmax = 12.5
    # pénombre : entre tangentes intérieures (au-delà de la Lune)
    yi = lambda x, s: s * (-np.tan(psi)) * (x - Ix)
    ye = lambda x, s: s * (-np.tan(phi)) * (x - Ex)
    xs = np.linspace(D, xmax, 200)
    ax.fill_between(xs, ye(xs, 1), yi(xs, -1), color="#9ec5f4", alpha=0.45, lw=0)
    ax.fill_between(xs, -ye(xs, 1), yi(xs, 1), color="#9ec5f4", alpha=0.45, lw=0)
    xu = np.linspace(D, Ex, 100)
    ax.fill_between(xu, -ye(xu, 1), ye(xu, 1), color="#1c5cab", alpha=0.75, lw=0)
    xa = np.linspace(Ex, xmax, 100)
    ax.fill_between(xa, ye(xa, 1), -ye(xa, 1), color="#6da7ec", alpha=0.55, lw=0)
    for s in (1, -1):
        xl = np.linspace(R1 * np.sin(phi) - 0.2, xmax, 10)
        ax.plot(xl, ye(xl, s), color=INK, lw=1.1)
        xl2 = np.linspace(R1 * np.sin(psi) - 0.2, xmax, 10)
        ax.plot(xl2, yi(xl2, s), color=INK2, lw=1.1, ls=(0, (5, 3)))
    ax.add_patch(mpatches.Circle((0, 0), R1, color=JAUNE, alpha=0.9, lw=0, zorder=5))
    ax.add_patch(mpatches.Circle((D, 0), R2, color="#3a3a38", lw=0, zorder=5))
    point(ax, Ex, 0, ORANGE, 8, z=7)
    point(ax, Ix, 0, AQUA, 8, z=7)
    ax.text(0, -R1 - 0.35, "Soleil", ha="center", fontsize=10)
    ax.text(D, -R2 - 0.35, "Lune", ha="center", fontsize=10)
    ax.text(Ex + 0.2, 0.5, "centre d'homothétie externe\n(sommet de l'ombre)", ha="center", fontsize=8.8)
    ax.text(Ix, -0.75, "centre d'homothétie\ninterne", ha="center", fontsize=8.8)
    ax.annotate("ombre : totale", xy=(6.6, -0.12), xytext=(6.45, -1.2), ha="center", fontsize=9, color=INK,
                arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
    ax.text(10.9, 0.05, "anti-ombre : annulaire", ha="center", va="center", fontsize=9, color=INK)
    ax.text(10.4, 1.25, "pénombre : partielle", ha="center", fontsize=9, color=INK)
    ax.text(-1.7, 2.3, "trait plein : tangentes extérieures communes (cône d'ombre)\n"
            "tirets : tangentes intérieures communes (cône de pénombre) — schéma, pas à l'échelle",
            fontsize=9, color=INK2, va="top")
    ax.set_xlim(-1.8, xmax)
    ax.set_ylim(-2.0, 2.4)
    sauver(fig, "fig9_eclipses.png")


if __name__ == "__main__":
    quoi = sys.argv[1:] or ["geometrie", "contour", "dimensions", "volume", "parametres", "courbes50",
                            "optique", "newton", "eclipse"]
    table = {"geometrie": fig_geometrie, "contour": fig_contour, "dimensions": fig_dimensions,
             "volume": fig_volume_surface, "parametres": fig_parametres, "courbes50": fig_courbes50,
             "optique": fig_optique, "newton": fig_newton, "eclipse": fig_eclipse}
    for q in quoi:
        table[q]()
