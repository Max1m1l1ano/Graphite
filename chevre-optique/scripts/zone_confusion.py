"""
Partie VI : le ménisque de 0,35 % entre la chèvre et le triangle équilatéral.

    python3 scripts/zone_confusion.py

Écrit resultats/zone_confusion.md et figures/f1_zone_confusion.png.

Conventions : pré = disque unité de centre O, piquet P = (1, 0). Deux cordes :
celle de la chèvre r₂ = 1,1587… (moitié exacte) et le côté du triangle
équilatéral de sommet P et de hauteur PO = 1, a₂ = 2/√3. En dimension n, le
triangle devient le simplexe régulier de sommet P et de hauteur 1, d'arête
a_n = √(2n/(n+1)).
"""

import os
import sys
from math import gcd

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from matplotlib.patches import Polygon

sys.path.insert(0, os.path.dirname(__file__))
import chevre as ch  # noqa: E402
import figures as F  # noqa: E402  (style et palette des parties précédentes)

mp.mp.dps = 30
ICI = os.path.dirname(os.path.abspath(__file__))
PI = mp.pi
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, d=10):
    return mp.nstr(x, d).replace(".", ",")


def lentille(R, r, d):
    """Aire commune de deux disques (rayons R, r ; centres à distance d), en précision arbitraire."""
    a1 = mp.acos((d * d + R * R - r * r) / (2 * d * R))
    a2 = mp.acos((d * d + r * r - R * R) / (2 * d * r))
    return R * R * a1 + r * r * a2 - mp.sqrt((-d + r + R) * (d + r - R) * (d - r + R) * (d + r + R)) / 2


def longueur(y, disques):
    """Longueur de la coupe horizontale (hauteur y) d'une intersection de disques (cx, rayon)."""
    g, d = -mp.inf, mp.inf
    for cx, r in disques:
        if abs(y) >= r:
            return mp.mpf(0)
        h = mp.sqrt(r * r - y * y)
        g, d = max(g, cx - h), min(d, cx + h)
    return max(mp.mpf(0), d - g)


# ---------------------------------------------------------------------------
# 1. La zone de confusion entre les deux cercles
# ---------------------------------------------------------------------------
r2 = ch.corde_moitie_mp(2)
a2 = 2 / mp.sqrt(3)
zone = PI / 2 - lentille(1, a2, 1)
forme_close = (2 * mp.sqrt(2) - mp.acos(mp.mpf(1) / 3)) / 3 - PI / 6
manque = zone / PI
ligne("## 1. La zone entre les deux cercles, dans le pré (R = 1)\n")
ligne(f"- corde de la chèvre r₂ = {fr(r2, 15)} ; côté du triangle 2/√3 = {fr(a2, 15)} ; écart {fr(r2 - a2, 6)} ({fr(100 * (r2 - a2) / r2, 4)} %)")
ligne(f"- aire de la zone (dans le pré, entre les deux cercles) = π/2 − lentille(2/√3) = {fr(zone, 15)}")
ligne(f"- forme close : (2√2 − arccos(1/3))/3 − π/6 = {fr(forme_close, 15)}")
ligne(f"- part du pré : {fr(100 * manque, 8)} % ; part de la moitié visée : {fr(200 * manque, 8)} %")
ligne(f"- corde commune avec la corde 2/√3 : x = 1/3 (centre de gravité du triangle), longueur 4√2/3 = {fr(4 * mp.sqrt(2) / 3, 10)}")
ligne(f"- corde commune de la chèvre : x = 1 − r₂²/2 = {fr(1 - r2 ** 2 / 2, 10)}")

# ---------------------------------------------------------------------------
# 2. Déplacer le petit cercle : les croissants
# ---------------------------------------------------------------------------
delta = mp.findroot(lambda d: lentille(1, a2, 1 - d) - PI / 2, 0.004)
xc = 1 - (r2 ** 2 - a2 ** 2 + delta ** 2) / (2 * delta)  # croisement des deux cercles
yc = mp.sqrt(r2 ** 2 - (xc - 1) ** 2)
yQ = mp.sqrt(1 - (1 - r2 ** 2 / 2) ** 2)
PRE, CHEVRE, DEPLACE = (0, 1), (1, r2), (1 - delta, a2)
aire = lambda disques: 2 * mp.quad(lambda y: longueur(y, disques), [0, yc, yQ, mp.mpf("0.99"), 1])
commun = aire([PRE, CHEVRE, DEPLACE])
gain, perte = aire([PRE, DEPLACE]) - commun, aire([PRE, CHEVRE]) - commun
ligne("\n## 2. Déplacer le cercle du triangle vers O\n")
ligne(f"- déplacement qui donne exactement la moitié : δ = {fr(delta, 12)} R (premier ordre : aire / corde = {fr(zone / (4 * mp.sqrt(2) / 3), 8)})")
ligne(f"- les deux cercles se croisent en ({fr(xc, 6)} ; ±{fr(yc, 6)}), dans le pré")
ligne(f"- croissant gagné (au milieu) = {fr(gain, 8)} ; croissants perdus (aux deux bouts) = {fr(perte, 8)} ; écart {mp.nstr(gain - perte, 2)} (précision de l'intégration)")
ligne(f"- épaisseur maximale : +{fr(a2 + delta - r2, 6)} au milieu ; −{fr(r2 - a2, 6)} sans déplacement")

# ---------------------------------------------------------------------------
# 3. En dimension n : le simplexe régulier
# ---------------------------------------------------------------------------
ligne("\n## 3. En dimension n : le simplexe régulier de sommet P et de hauteur R\n")
ligne("| n | arête du simplexe √(2n/(n+1)) | corde de la chèvre r_n | écart | n²(r_n² − arête²) | part manquante | déplacement δ_n |")
ligne("|---:|---|---|---|---|---|---|")
DIMS = list(range(2, 13)) + [15, 20]
tab = {}
for n in DIMS:
    an = mp.sqrt(mp.mpf(2 * n) / (n + 1))
    rn = ch.corde_moitie_mp(n)
    sn = mp.mpf(1) / 2 - ch.fraction_broutee_mp(n, an, 1)
    dn = mp.findroot(lambda d: ch.fraction_broutee_mp(n, an, 1 - d) - mp.mpf(1) / 2, 0.004)
    tab[n] = (an, rn, sn, dn)
    ligne(f"| {n} | {fr(an, 8)} | {fr(rn, 8)} | {fr(rn - an, 4)} | {fr(n * n * (rn ** 2 - an ** 2), 4)} | {fr(100 * sn, 4)} % | {fr(dn, 6)} |")
for n in (100, 400):
    rn = ch.corde_moitie_mp(n)
    ligne(f"\nn = {n} : n²(r_n² − 2n/(n+1)) = {fr(n * n * (rn ** 2 - mp.mpf(2 * n) / (n + 1)), 6)} (limite 2/3)")
ligne(f"\n3D exact : part manquante = (59 − 24√6)/64 = {fr((59 - 24 * mp.sqrt(6)) / 64, 12)}")
ligne(f"δ₂ = {fr(tab[2][3], 12)} ; δ₃ = {fr(tab[3][3], 12)} (écart relatif {mp.nstr(abs(tab[3][3] / tab[2][3] - 1), 2)})")
ligne("Avec la corde du simplexe, les deux sphères se coupent sur l'hyperplan x = 1 − n/(n+1) = 1/(n+1),"
      " qui passe par le centre de gravité du simplexe.")

# ---------------------------------------------------------------------------
# 3 bis. En dimension réelle : les écarts forment une bosse
# ---------------------------------------------------------------------------


def calotte(n, t):
    """Part de la boule unité de dimension réelle n dans la calotte d'angle au centre t (bêta incomplète)."""
    if t <= PI / 2:
        return mp.betainc((n + 1) / 2, mp.mpf(1) / 2, 0, mp.sin(t) ** 2, regularized=True) / 2
    return 1 - calotte(n, PI - t)


def broutee(n, k, D=1):
    """Part de la boule unité (dimension réelle n) à moins de k d'un piquet placé à la distance D du centre."""
    x = (D * D + 1 - k * k) / (2 * D)  # abscisse de l'hyperplan où les deux sphères se coupent
    return calotte(n, mp.acos(x)) + k ** n * calotte(n, mp.acos((D - x) / k))


arete = lambda n: mp.sqrt(2 * n / (n + 1))
ECARTS = {
    "écart des cordes r − arête": lambda n: mp.findroot(lambda k: broutee(n, k) - mp.mpf(1) / 2, arete(n) + mp.mpf("0.003")) - arete(n),
    "déplacement δ": lambda n: mp.findroot(lambda d: broutee(n, arete(n), 1 - d) - mp.mpf(1) / 2, mp.mpf("0.004")),
    "part manquante": lambda n: mp.mpf(1) / 2 - broutee(n, arete(n)),
}
controle = max(abs(broutee(mp.mpf(n), mp.mpf("1.2")) - ch.fraction_broutee_mp(n, mp.mpf("1.2"), 1)) for n in (2, 3, 5, 8))
ligne("\n## 3 bis. En dimension réelle n (fonction bêta incomplète)\n")
ligne(f"Contrôle contre la formule des dimensions entières : écart max {mp.nstr(controle, 2)}")
ligne("En dimension 1 : corde de la chèvre = arête = 1 (moitié d'un segment), donc tous les écarts sont nuls.\n")
ligne("| n | écart des cordes | déplacement δ | part manquante |")
ligne("|---:|---|---|---|")
for n in ("1.25", "1.5", "2", "2.25", "2.5", "3", "4", "6", "10"):
    ligne(f"| {n.replace('.', ',')} | " + " | ".join(fr(f(mp.mpf(n)), 6) for f in ECARTS.values()) + " |")
SOMMETS = {}
for nom, f in ECARTS.items():
    g, lo, hi = (mp.sqrt(5) - 1) / 2, mp.mpf("1.2"), mp.mpf("4.5")
    for _ in range(60):
        u, v = hi - g * (hi - lo), lo + g * (hi - lo)
        lo, hi = (lo, v) if f(u) > f(v) else (u, hi)
    SOMMETS[nom] = (lo + hi) / 2
    ligne(f"- sommet de « {nom} » en n = {fr(SOMMETS[nom], 6)}, valeur {fr(f(SOMMETS[nom]), 6)}")
d_ = ECARTS["déplacement δ"]
retour = mp.findroot(lambda n: d_(n) - tab[2][3], mp.mpf(3))
ligne(f"- la courbe δ(n) repasse au niveau de δ₂ en n = {fr(retour, 8)} : à {mp.nstr(retour - 3, 2)} de la dimension 3")

# ---------------------------------------------------------------------------
# 4. π − 3 : les vraies routes et le test des coïncidences
# ---------------------------------------------------------------------------
ligne("\n## 4. π − 3\n")
nila = 4 * mp.nsum(lambda k: (-1) ** (k + 1) / ((2 * k) * (2 * k + 1) * (2 * k + 2)), [1, mp.inf])
newton = mp.nsum(lambda k: 3 * mp.binomial(2 * k, k) / ((2 * k + 1) * 16 ** k), [1, mp.inf])
ligne(f"- Nilakantha avec les cônes c_n = 1/n : 4(c₂c₃c₄ − c₄c₅c₆ + …) = {fr(nila, 20)}")
ligne(f"- retenues de l'hexagone (partie IV) : 1/8 + 9/640 + 15/7168 + … = {fr(newton, 20)}")
ligne(f"- π − 3 = {fr(PI - 3, 20)}")
CIBLES = {"part manquante (0,283 %)": manque, "écart des cordes": r2 - a2, "déplacement δ": delta, "aire de la zone": zone}
CONSTANTES = {"π − 3": PI - 3, "√2": mp.sqrt(2), "√3": mp.sqrt(3), "√5": mp.sqrt(5), "φ": (1 + mp.sqrt(5)) / 2, "e": mp.e,
              "π": PI, "ln 2": mp.log(2), "γ": mp.euler, "ρ": mp.findroot(lambda x: x ** 3 - x - 1, 1.3), "ζ(3)": mp.zeta(3),
              "1": mp.mpf(1)}
ligne("\nTest : formules p·C/q (p ≤ 10, q ≤ 1000, 12 constantes C) à moins de 0,1 % de la cible\n")
ligne("| cible | valeur | formules à moins de 0,1 % | les trois meilleures | avec π − 3 |")
ligne("|---|---|---:|---|---|")
for nom, t in CIBLES.items():
    tf, touches = float(t), []
    for cn, c in CONSTANTES.items():
        cf = float(c)
        for q in range(1, 1001):
            for p in range(1, 11):
                if gcd(p, q) == 1 and abs(p * cf / q / tf - 1) < 1e-3:
                    nom_c = f"{p}/{q}" if cn == "1" else (f"{p}·" if p > 1 else "") + (f"({cn})" if " " in cn else cn) + f"/{q}"
                    touches.append((abs(p * cf / q / tf - 1), nom_c))
    touches.sort()
    pm3 = [f"{f} ({100 * e:.3f} %)".replace(".", ",") for e, f in touches if "π − 3" in f][:2]
    ligne(f"| {nom} | {tf:.6g} | {len(touches)} | ".replace(".", ",") + " ; ".join(f"{f} ({100 * e:.3f} %)".replace(".", ",") for e, f in touches[:3])
          + f" | {' ; '.join(pm3) if pm3 else 'aucune'} |")

# ---------------------------------------------------------------------------
# 5. La lunule d'Hippocrate : un croissant sans π
# ---------------------------------------------------------------------------
R = mp.mpf(1)
lunule = PI * (R / mp.sqrt(2)) ** 2 / 2 - (PI * R ** 2 / 4 - R ** 2 / 2)  # demi-disque sur AC − segment du grand cercle
ligne("\n## 5. La lunule d'Hippocrate\n")
ligne(f"- grand cercle de rayon 1, petit cercle de rayon 1/√2 (rapport √2) : aire de la lunule = {fr(lunule, 20)} = aire du triangle (1/2)")

with open(os.path.join(ICI, "..", "resultats", "zone_confusion.md"), "w") as fh:
    fh.write("# Résultats de la partie VI (générés par scripts/zone_confusion.py)\n\n" + "\n".join(md) + "\n")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, axs = plt.subplots(2, 2, figsize=(15.5, 11.5), gridspec_kw={"wspace": 0.18, "hspace": 0.26})
r2f, a2f, df = float(r2), float(a2), float(delta)
G = 25  # grossissement des écarts radiaux pour les rendre visibles

# a) la zone de confusion (écart grossi)
ax = axs[0, 0]
ax.set_aspect("equal")
F.remplir_intersection(ax, r2f, (F.BLEU, F.SURF), 0.14)
F.cercle(ax, (0, 0), 1, color=F.INK, lw=1.6)
tQ = np.arctan2(float(yQ), float(1 - r2 ** 2 / 2) - 1)
t = np.linspace(tQ, 2 * np.pi - tQ, 600)
ax.plot(1 + r2f * np.cos(t), r2f * np.sin(t), color=F.BLEU, lw=1.8)
ag = r2f - G * (r2f - a2f)  # rayon grossi du cercle du triangle
xs_g, ys_g = 1 + ag * np.cos(t), ag * np.sin(t)
dedans = xs_g ** 2 + ys_g ** 2 <= 1
ax.fill(np.concatenate([1 + r2f * np.cos(t[dedans]), (1 + ag * np.cos(t[dedans]))[::-1]]),
        np.concatenate([r2f * np.sin(t[dedans]), (ag * np.sin(t[dedans]))[::-1]]), color=F.ORANGE, alpha=0.45, lw=0)
ax.plot(xs_g[dedans], ys_g[dedans], color=F.ORANGE, lw=1.4, ls=(0, (4, 3)))
tri = np.array([[1, 0], [0, 1 / np.sqrt(3)], [0, -1 / np.sqrt(3)]])
ax.add_patch(Polygon(tri, closed=True, fill=False, ec=F.ORANGE, lw=1.5))
F.point(ax, 1 / 3, 0, F.ORANGE, 7)
ax.plot([1 / 3, 1 / 3], [-np.sqrt(8) / 3, np.sqrt(8) / 3], color=F.ORANGE, lw=1, ls=":")
F.point(ax, 1, 0, F.INK, 8)
F.point(ax, 0, 0, F.INK, 6)
ax.text(1.05, 0.06, "P", fontsize=11)
ax.text(-0.12, 0.06, "O", fontsize=11)
ax.annotate("centre de gravité :\nla corde commune y passe\n(avec la corde 2/√3)", xy=(1 / 3, 0), xytext=(1.08, -0.5), fontsize=9,
            color=F.INK2, arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.annotate(f"zone de confusion (écart grossi {G} fois)\naire exacte = (2√2 − arccos(1/3))/3 − π/6\n= 0,00889 R², soit 0,283 % du pré",
            xy=(-0.1, 0.3), xytext=(-1.15, 1.52), fontsize=9.5, color=F.INK, va="top",
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.set_xlim(-1.2, 2.0)
ax.set_ylim(-1.15, 1.55)
ax.axis("off")
ax.set_title("a)  La zone de confusion entre la chèvre et le triangle")

# b) déplacer le petit cercle : l'épaisseur des croissants le long de l'arc
ax = axs[0, 1]
th = np.linspace(tQ, 2 * np.pi - tQ, 1500)
for dd, coul, lab in ((0.0, F.ORANGE, "sans déplacement : tout manque (0,35 %)"),
                      (df, F.BLEU, f"petit cercle déplacé de δ = {df:.5f} R vers O".replace(".", ","))):
    tt = -dd * np.cos(th) + np.sqrt(a2f ** 2 - dd ** 2 * np.sin(th) ** 2)  # distance de P au cercle déplacé, rayon par rayon
    e = (tt - r2f) * 1e3
    ax.plot(np.degrees(th), e, color=coul, lw=2, label=lab)
    if dd > 0:
        ax.fill_between(np.degrees(th), 0, e, where=e > 0, color=F.BLEU, alpha=0.25, lw=0)
        ax.fill_between(np.degrees(th), 0, e, where=e < 0, color=F.ORANGE, alpha=0.25, lw=0)
ax.axhline(0, color=F.INK, lw=1)
ax.text(180, 0.18, f"croissant gagné\n{float(gain):.2e} R²".replace(".", ",").replace("e-04", "·10⁻⁴"), ha="center", fontsize=9.5,
        color=F.BLEU)
ax.text(137, -1.6, "croissants perdus\n(même aire au total)", ha="center", fontsize=9.5, color=F.ORANGE)
ax.set_xlabel("direction vue depuis le piquet P (degrés), de Q à Q' en passant par O")
ax.set_ylabel("épaisseur du croissant (10⁻³ R)")
ax.set_title("b)  Déplacer le petit cercle : deux croissants qui s'équilibrent")
ax.legend(fontsize=9, loc="lower center", bbox_to_anchor=(0.5, 0.12))
ax.set_ylim(-4.6, 1.3)

# c) en dimension n : simplexe et chèvre vers √2
ax = axs[1, 0]
ns = np.array(DIMS)
ax.plot(ns, [float(tab[n][1]) for n in ns], "-o", color=F.BLEU, ms=5, mec=F.SURF, label="corde de la chèvre r_n")
ax.plot(ns, [float(tab[n][0]) for n in ns], "--s", color=F.ORANGE, ms=4.5, mec=F.SURF, label="arête du simplexe √(2n/(n+1))")
ax.axhline(np.sqrt(2), color=F.INK, lw=1.2)
ax.text(19.6, np.sqrt(2) + 0.006, "√2", fontsize=11, ha="right")
ax.annotate("n = 2 : triangle équilatéral\nécart 0,35 %", xy=(2, float(tab[2][0])), xytext=(4.2, 1.17), fontsize=9, color=F.INK2,
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.annotate("n = 3 : tétraèdre régulier\nécart 0,31 %", xy=(3, float(tab[3][0])), xytext=(6.2, 1.26), fontsize=9, color=F.INK2,
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.set_xlabel("dimension n")
ax.set_ylabel("longueur / R")
ax.set_xticks(ns)
ax.set_title("c)  En dimension n : le simplexe suit la chèvre jusqu'à √2")
ax.legend(fontsize=9.5, loc="lower right")

# d) les écarts qui se referment
ax = axs[1, 1]
ax.loglog(ns, [float(tab[n][1] - tab[n][0]) for n in ns], "-o", color=F.INK, ms=5, mec=F.SURF, label="écart des cordes r_n − arête")
ax.loglog(ns, [float(tab[n][2]) for n in ns], "-o", color=F.ORANGE, ms=5, mec=F.SURF, label="part manquante du pré")
ax.loglog(ns, [float(tab[n][3]) for n in ns], "-o", color=F.BLEU, ms=5, mec=F.SURF, label="déplacement δ_n qui la rattrape")
ax.loglog(ns, 0.236 / ns.astype(float) ** 2, color=F.MUTED, lw=1, ls=(0, (4, 3)), label="pente finale de l'écart : 0,236/n²")
ax.annotate("δ₂ ≈ δ₃ à 10⁻⁵ près\n(coïncidence)", xy=(2.45, float(tab[2][3])), xytext=(2.05, 1.05e-2), fontsize=9, color=F.INK2,
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.set_xlabel("dimension n")
ax.set_ylabel("écart (en R, ou en part du pré)")
ax.set_title("d)  La zone de confusion se referme quand n grandit")
ax.legend(fontsize=9, loc="lower left")
ax.set_ylim(3e-4, 1.5e-2)
ax.set_xticks([2, 3, 4, 5, 6, 8, 10, 15, 20])
ax.set_xticklabels(["2", "3", "4", "5", "6", "8", "10", "15", "20"])
ax.minorticks_off()
F.sauver(fig, "f1_zone_confusion.png")

# Figure 2 : les écarts en dimension réelle
fig, axs = plt.subplots(1, 2, figsize=(15.5, 5.3), gridspec_kw={"wspace": 0.22})
ax = axs[0]
nr = [mp.mpf(1) + mp.mpf(i) / 20 for i in range(1, 221)]
STY = {"écart des cordes r − arête": (F.INK, "écart des cordes (en R)"), "déplacement δ": (F.BLEU, "déplacement δ qui rattrape (en R)"),
       "part manquante": (F.ORANGE, "part manquante du pré")}
for nom, f in ECARTS.items():
    coul, lab = STY[nom]
    ax.plot([1.0] + [float(n) for n in nr], [0.0] + [float(f(n)) for n in nr], color=coul, lw=2, label=lab)
    ax.plot(range(1, 13), [0.0] + [float(f(mp.mpf(n))) for n in range(2, 13)], "o", color=coul, ms=5, mec=F.SURF)
    ax.axvline(float(SOMMETS[nom]), color=coul, lw=0.9, ls=":")
ax.annotate("nuls en dimension 1 :\nla chèvre et le « simplexe »\nsont le même demi-segment", xy=(1, 0), xytext=(3.6, 0.0007), fontsize=9,
            color=F.INK2, arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.text(8.2, 0.0038, "→ 0 quand n → ∞ :\nles deux vont à √2", fontsize=9, color=F.INK2)
ax.text(3.45, 0.0053, "sommets (pointillés) en n = 2,24 ; 2,42 ; 3,20", fontsize=9, color=F.INK2, va="center")
ax.set_xlabel("dimension n (réelle)")
ax.set_ylabel("écart")
ax.set_xticks(range(1, 13))
ax.set_ylim(0, 0.0056)
ax.set_title("a)  La bosse : le triangle (n = 2) est près du sommet")
ax.legend(fontsize=9, loc="center right", bbox_to_anchor=(1.0, 0.55))
ax = axs[1]
nz = [mp.mpf("1.8") + mp.mpf(i) / 200 for i in range(0, 301)]
ax.plot([float(n) for n in nz], [float(d_(n)) * 1e3 for n in nz], color=F.BLEU, lw=2.2)
ax.axhline(float(tab[2][3]) * 1e3, color=F.MUTED, lw=1, ls=(0, (4, 3)))
for n in (2, 3):
    F.point(ax, n, float(tab[n][3]) * 1e3, F.BLEU, 8)
F.point(ax, float(SOMMETS["déplacement δ"]), float(d_(SOMMETS["déplacement δ"])) * 1e3, F.INK, 7)
ax.annotate(f"sommet en n = {float(SOMMETS['déplacement δ']):.2f}".replace(".", ","), xy=(float(SOMMETS["déplacement δ"]), float(d_(SOMMETS["déplacement δ"])) * 1e3),
            xytext=(2.42, 4.83), fontsize=9.5, color=F.INK, ha="center")
ax.annotate("δ₂ et δ₃ sont de part et d'autre du sommet :\nproches, c'est la forme de la bosse",
            xy=(2.0, float(tab[2][3]) * 1e3), xytext=(1.83, 4.6), fontsize=9.5, color=F.INK2,
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.annotate(f"la courbe repasse au niveau de δ₂ en n = {float(retour):.5f},\nà 9·10⁻⁵ de la dimension 3 : ça, c'est le hasard".replace(".", ","),
            xy=(3.0, float(tab[3][3]) * 1e3), xytext=(2.25, 4.42), fontsize=9.5, color=F.INK2,
            arrowprops=dict(arrowstyle="-", color=F.MUTED, lw=0.8))
ax.set_xlabel("dimension n (réelle)")
ax.set_ylabel("déplacement δ (10⁻³ R)")
ax.set_title("b)  δ₂ ≈ δ₃ : la bosse explique la proximité, pas les décimales")
F.sauver(fig, "f2_dimension_reelle.png")
