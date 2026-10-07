"""
Partie XXVI : la surface de Kakeya à 10⁻⁵⁰, la virgule du kibi dans son miroir et le cube qui tourne.

    python3 scripts/kakeya_miroir.py        # ≈ 1 min

Écrit resultats/kakeya_miroir.md, figures/aa1_kakeya.png, figures/aa2_virgule_miroir.png et
figures/aa3_cube_hexagone.png.

1. Kakeya au grain δ : la borne L² de Córdoba avec sa constante exacte, π/(1 + 2γ + 2 ln(2/δ)) ; les arbres de Perron
   des parties V et XIV en tubes 1 × δ (un tube par direction), calculés jusqu'à δ = 10⁻⁵ ; la tranche 49 – 55.
2. La virgule du kibi : 2¹⁰/10³ = 128/125 (le diesis des musiciens), 2²⁰/10⁶ = (128/125)² ; le miroir 5⁶/2¹⁴ (les
   chiffres de 5²⁰) ; 9,49 %, 9,72 % et 9,95 % comme trois lectures du même double ; les retenues ; les trois écarts
   des crans sur le cercle des décades, et les puissances de 5 qui en sont le reflet.
3. Le cube qui tourne : l'ombre |u₁| + |u₂| + |u₃|, le mouvement complet autour d'un axe d'ordre 2, les deux carrés
   qui se quittent à l'hexagone, les deux pavages en losanges, le carré de Prince Rupert dans l'hexagone.
"""

import itertools
import logging
import math
import os
import sys
import time
from fractions import Fraction as Fr

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from matplotlib.collections import PolyCollection
from matplotlib.patches import Arc, Circle, Polygon
from scipy.integrate import quad
from scipy.optimize import linprog, minimize_scalar
from scipy.spatial import ConvexHull

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
ROUGE, VIOLET, VERT = "#d0342c", "#7d4fc4", "#1baf7a"
R2, R3 = math.sqrt(2), math.sqrt(3)
T0 = time.time()
mp.mp.dps = 40
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def sup(n):
    return str(n).translate(SUP)


def dec(q, n=None):
    """Écriture décimale exacte d'une fraction dont le dénominateur n'a que des 2 et des 5."""
    s = mp.nstr(mp.mpf(q.numerator) / q.denominator, n or 40, strip_zeros=True)
    return s.replace(".", ",").replace("-", "−")


# ===========================================================================
# 1. Kakeya au grain δ
# ===========================================================================
ligne("# Résultats de la partie XXVI (générés par scripts/kakeya_miroir.py)\n")
ligne("## 1. La surface minimale de Kakeya au grain δ\n")
ligne("Le problème au grain δ : N tubes 1 × δ (des parallélogrammes d'aire δ et de largeur δ), un dans chacune des"
      " directions jπ/N, espacées de δ au plus. Quelle est l'aire minimale de leur union ?\n")

GAM = float(mp.euler)


def somme_csc(N):
    k = np.arange(1, N)
    return float(np.sum(1 / np.sin(k * np.pi / N)))


ligne("### 1.1 La somme des croisements\n")
ligne("Deux tubes dont les directions font l'angle θ se recouvrent au plus de δ²/sin θ (deux bandes de largeur δ"
      " se croisent sur un parallélogramme de cette aire). Pour N directions, la somme vaut :\n")
ligne("| N | Σ csc(jπ/N), j = 1 … N − 1 | (2N/π)(ln(2N/π) + γ) | (écart) × N |")
ligne("|---:|---|---|---|")
for N in (10, 100, 1000, 10000):
    S_ = somme_csc(N)
    A_ = 2 * N / np.pi * (np.log(2 * N / np.pi) + GAM)
    ligne(f"| {N} | {fr(S_, '{:.6f}')} | {fr(A_, '{:.6f}')} | {fr((S_ - A_) * N, '{:.5f}')} |")
ligne(f"\nL'écart vaut −π/(36N) = {fr(-np.pi / 36, '{:.5f}')}/N : la formule est exacte au terme près, ce qui"
      " permet de l'évaluer pour N = π·10⁵⁰.\n")


def borne_cordoba(N, delta):
    """Borne L² (Córdoba 1977) : |∪T| ≥ (Σ|T|)² / Σ_{T,T'} |T ∩ T'|, avec |T ∩ T'| ≤ min(δ, δ²/sin θ)."""
    k = np.arange(1, N)
    s = np.sin(k * np.pi / N)
    return (N * delta) ** 2 / (N * (delta + float(np.sum(np.minimum(delta, delta * delta / s)))))


def borne_tranche(k):
    """La même borne pour δ = 10^−k et N = π/δ : π/(1 + 2γ + 2 ln(2/δ)), au terme O(δ²) près."""
    return mp.pi / (1 + 2 * mp.euler + 2 * mp.log(2) + 2 * k * mp.log(10))


ligne("### 1.2 La borne du bas (Córdoba)\n")
ligne("Cauchy–Schwarz donne |∪T| ≥ (Σ|T|)²/‖Σχ_T‖², et ‖Σχ_T‖² = Σ |T ∩ T'| ≤ N·(δ + δ²·Σ csc) ≈ π·(1 + 2γ + 2 ln(2/δ))."
      " D'où, avec Σ|T| = Nδ = π :\n")
ligne("    |∪T| ≥ π / (1 + 2γ + 2 ln(2/δ)),   donc   1/|∪T| ≤ 1,1270 + 1,4659·k  pour δ = 10⁻ᵏ.\n")
INV0 = (1 + 2 * mp.euler + 2 * mp.log(2)) / mp.pi
PENTE = 2 * mp.log(10) / mp.pi
ligne(f"(constante : (1 + 2γ + 2 ln 2)/π = {fr(float(INV0), '{:.5f}')} ; pente : 2 ln 10/π = {fr(float(PENTE), '{:.5f}')}"
      " par décade)\n")

# --- les arbres de Perron en tubes ---------------------------------------
BASE, APEX = 2 / R3, 1 / R3  # le triangle équilatéral de hauteur 1 (Pál), comme aux parties V et XIV


def arbre(k_, alphas):
    """Arbre de Perron à 2^k branches (même construction que les parties V, X et XIV) : bases [l, r], sommets."""
    n_ = 2 ** k_
    xs_ = [BASE * i / n_ for i in range(n_ + 1)]
    l, r, som = list(xs_[:-1]), list(xs_[1:]), [APEX] * n_
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
                som[i] += dx
            nouveaux.append((s1, e2, u1_, u1_ + alpha * largeur))
        blocs = nouveaux
    return np.array(l), np.array(r), np.array(som)


def telescope(k):
    """Rapports (k+1)/(k+2), …, 3/4, 2/3 de la partie V : l'arbre couvre 2/(k + 2) du triangle."""
    return [(k + 2 - j) / (k + 3 - j) for j in range(1, k + 1)]


def tubes(k, delta):
    """Les tubes de l'éventail de 60° : un par direction, posé dans la branche qui contient cette direction.

    Le tube part du sommet de sa branche (hauteur 1) et descend d'une longueur 1 ; ses côtés horizontaux font
    δ/cos θ, donc son aire vaut δ et sa largeur δ. Renvoie sommets, pentes, demi-largeurs, cos θ, branches."""
    nf = int(math.ceil((math.pi / 3) / delta))
    th = -math.pi / 6 + (np.arange(nf) + 0.5) * (math.pi / 3) / nf
    t = np.tan(th)
    if k == 0:
        som = np.array([APEX])
    else:
        som = arbre(k, telescope(k))[2]
    b = np.minimum(((t + APEX) / BASE * 2 ** k).astype(int), 2 ** k - 1)
    return som[b], t, delta / (2 * np.cos(th)), np.cos(th), b


def aire_union(k, delta, M=1000):
    """Aire de l'union des tubes (tranches horizontales ; la longueur est affine par morceaux en y)."""
    a, t, h, c, _ = tubes(k, delta)
    tot = 0.0
    for y in (np.arange(M) + 0.5) / M:
        act = y >= 1 - c
        cen = a[act] + (1 - y) * t[act]
        g, d = cen - h[act], cen + h[act]
        o = np.argsort(g)
        g, d = g[o], d[o]
        prec = np.concatenate(([-np.inf], np.maximum.accumulate(d)[:-1]))
        tot += float(np.sum(np.maximum(0.0, d - np.maximum(g, prec))))
    return tot / M


def meilleur_arbre(delta):
    """Cherche le nombre de branches optimal (la courbe en k est en cuvette)."""
    L2 = math.log2(1 / delta)
    k = max(0, round(L2 - 2 * math.log2(L2) + 3.5))
    res = {k: aire_union(k, delta)}
    while k > 0:
        res[k - 1] = aire_union(k - 1, delta)
        if res[k - 1] >= res[k]:
            break
        k -= 1
    k = max(res)
    while True:
        res[k + 1] = aire_union(k + 1, delta)
        if res[k + 1] >= res[k]:
            break
        k += 1
    kb = min(res, key=res.get)
    return kb, res


def puiss(d):
    e = -math.log10(d)
    if abs(e - round(e)) < 1e-9:
        return f"10⁻{sup(round(e))}"
    p_ = math.floor(math.log10(d))
    return f"{fr(d / 10 ** p_, '{:.1f}')}·10{sup(p_)}"


T1 = time.time()
DELTAS = [10 ** (-j / 2) for j in range(2, 11)]
CONS = {}
for d in DELTAS:
    CONS[d] = meilleur_arbre(d)
ligne("### 1.3 Les constructions : arbres de Perron en tubes\n")
ligne("Trois éventails de 60° (tournés de 60°) couvrent toutes les directions ; chacun est un arbre de Perron à 2^k"
      " branches (rapports télescopiques de la partie V), et chaque direction reçoit un tube dans sa branche. On calcule"
      " l'aire exacte de l'union (1 000 tranches) et on garde le meilleur k.\n")
ligne("| δ | N directions | meilleur arbre | aire de l'union (3 éventails) | × ln(1/δ) | borne de Córdoba |"
      " construction ÷ borne |")
ligne("|---|---:|---|---|---|---|---|")
PROD = {}
for d in DELTAS:
    kb, res = CONS[d]
    nf = int(math.ceil((math.pi / 3) / d))
    tot = 3 * res[kb]
    bo = borne_cordoba(3 * nf, d)
    PROD[d] = tot * math.log(1 / d)
    ligne(f"| {puiss(d)} | {3 * nf} | k = {kb} ({2 ** kb} branches) | {fr(tot, '{:.4f}')} |"
          f" {fr(PROD[d], '{:.3f}')} | {fr(bo, '{:.4f}')} | {fr(tot / bo, '{:.2f}')} |")
ligne(f"\n(calcul : {fr(time.time() - T1, '{:.0f}')} s)")
A_PLAT = float(np.mean([PROD[d] for d in DELTAS[-3:]]))
A_LIM = 2 * R3 * math.log(2)
ligne(f"\nLe produit aire × ln(1/δ) reste vers {fr(A_PLAT, '{:.2f}')} de 10⁻² à 10⁻⁵ : l'aire suit 1/ln(1/δ). Si la"
      f" formule 2/(k + 2) de la partie V tient pour tout k, la famille tend lentement vers 2√3·ln 2 ="
      f" {fr(A_LIM, '{:.3f}')} (le débord des tubes devient négligeable).")
d4 = DELTAS[-3]
ligne(f"\nÀ δ = 10⁻³, un éventail couvre {fr(CONS[1e-3][1][CONS[1e-3][0]] * R3, '{:.3f}')} du triangle (la grille de la"
      " partie XIV donnait 0,28 pour n = 1024).")
DELTOIDE, PAL, DISQUE = math.pi / 8, 1 / R3, math.pi / 4
croise = [d for d in DELTAS if 3 * CONS[d][1][CONS[d][0]] < DELTOIDE]
ligne(f"Les arbres battent le deltoïde (π/8 = {fr(DELTOIDE, '{:.4f}')}) à partir de δ = {puiss(croise[0])}"
      " seulement.\n")

ligne("### 1.4 La tranche 10⁻⁴⁹ – 10⁻⁵⁵\n")
ligne("| δ | borne de Córdoba (démontrée) | 1/borne | construction extrapolée (2,40 à "
      f"{fr(A_PLAT, '{:.2f}')} sur ln(1/δ)) | part du deltoïde |")
ligne("|---|---|---|---|---|")
TR = list(range(49, 56))
BT = {k: borne_tranche(k) for k in TR}
for k in TR:
    lnd = k * math.log(10)
    ligne(f"| 10⁻{sup(k)} | {fr(float(BT[k]), '{:.6f}')} | {fr(float(1 / BT[k]), '{:.4f}')} |"
          f" {fr(A_LIM / lnd, '{:.4f}')} – {fr(A_PLAT / lnd, '{:.4f}')} |"
          f" {fr(100 * float(BT[k]) / DELTOIDE, '{:.2f}')} – {fr(100 * A_PLAT / lnd / DELTOIDE, '{:.2f}')} % |")
miroir_h = 1 / BT[49] + 1 / BT[51] - 2 / BT[50]
ligne(f"\n- Miroir harmonique : 1/L(49) + 1/L(51) − 2/L(50) = {'0' if abs(miroir_h) < mp.mpf(10) ** -30 else mp.nstr(miroir_h, 3)}"
      " (exactement : 1/L est affine en k).")
ligne(f"- Sur la tranche, la borne ne baisse que de {fr(100 * (1 - float(BT[55] / BT[49])), '{:.2f}')} % "
      f"(L(49)/L(55) = {fr(float(BT[49] / BT[55]), '{:.4f}')} ; 55/49 = {fr(55 / 49, '{:.4f}')}), quand le grain"
      " est divisé par 10⁶.")
L50 = float(BT[50])
ligne(f"- Pour une aiguille de longueur √3 (la grande diagonale du cube), l'aire se multiplie par 3 :"
      f" au moins {fr(3 * float(mp.pi / (1 + 2 * mp.euler + 2 * mp.log(2 * R3 * mp.mpf(10) ** 50))), '{:.4f}')}"
      f" à 10⁻⁵⁰, contre 3π/8 = {fr(3 * DELTOIDE, '{:.4f}')} pour le deltoïde et 3π/4 = {fr(3 * DISQUE, '{:.4f}')}"
      " pour le disque qu'elle balaie en tournant sur son milieu.")

# ===========================================================================
# 2. La virgule du kibi dans son miroir
# ===========================================================================
ligne("\n## 2. La virgule du kibi et son miroir\n")
C = Fr(2 ** 20, 10 ** 6) - 1
MIR = Fr(10 ** 6, 2 ** 20)
assert MIR == Fr(5 ** 6, 2 ** 14) and Fr(2 ** 10, 10 ** 3) == Fr(128, 125) and Fr(128, 125) ** 2 == 1 + C
SPAN, DOUBLE, CARRE = (1 + C) - MIR, 2 * C, (1 + C) ** 2 - 1
assert 1 - MIR == C / (1 + C) and SPAN == C * (2 + C) / (1 + C) and DOUBLE - SPAN == C * C / (1 + C)
assert CARRE - DOUBLE == C * C
ligne("### 2.1 Les nombres exacts\n")
ligne(f"- virgule : c = 2²⁰/10⁶ − 1 = {dec(C)} ; 2¹⁰/10³ = 128/125 (le diesis), 2²⁰/10⁶ = (128/125)² = 16384/15625")
ligne(f"- miroir : 10⁶/2²⁰ = 5⁶/2¹⁴ = 15625/16384 = {dec(MIR)} (les chiffres de 5²⁰ = {5 ** 20})")
ligne(f"- 1 − miroir = c/(1 + c) = {dec(1 - MIR)}")
ligne(f"- écart entre le cran et son miroir : (1 + c) − 1/(1 + c) = {dec(SPAN)}")
ligne(f"- double linéaire : 2c = {dec(DOUBLE)} (les chiffres de 2²¹ = {2 ** 21})")
ligne(f"- carré : (1 + c)² − 1 = 2c + c² = {dec(CARRE)} (2⁴⁰ = {2 ** 40}, le téra contre le tébi)")
ligne(f"- les deux retenues : 2c − écart = c²/(1 + c) = {dec(DOUBLE - SPAN)} ; carré − 2c = c² = {dec(C * C)}")
moy = (SPAN + CARRE) / 2
ligne(f"- milieu de l'écart et du carré : {dec(moy)} = 2c + c³/(2(1 + c)) ; le double est au milieu à"
      f" {dec(moy - DOUBLE)} près")
LG = mp.log10(mp.mpf(2) ** 20 / 10 ** 6)
ligne(f"- en logarithme : log₁₀(1 + c) = {fr(float(LG), '{:.12f}')} ; le miroir est à {fr(-float(LG), '{:.12f}')} ;"
      f" l'écart, le double et le carré valent tous 2·log₁₀(1 + c) = {fr(2 * float(LG), '{:.12f}')} décade.")

ligne("\n### 2.2 Les retenues du doublement\n")
chiffres, ret, sortie = "048576", 0, []
RETENUES = []
for ch in reversed(chiffres):
    v = 2 * int(ch) + ret
    RETENUES.append((int(ch), v, v // 10))
    sortie.append(v % 10)
    ret = v // 10
ligne("| chiffre (de droite à gauche) | 2 × chiffre + retenue | écrit | retenue |")
ligne("|---|---|---|---|")
for ch, v, r_ in RETENUES:
    ligne(f"| {ch} | {v} | {v % 10} | {r_} |")
ligne(f"\n2 × 048576 = {''.join(map(str, reversed(sortie)))} : quatre retenues de suite, que le 4 absorbe en devenant 9."
      " Arrondi : 4,86 × 2 = 9,72.")

ligne("\n### 2.3 Les paliers des octets et leurs miroirs\n")
ligne("| palier | 2^(10j)/10^(3j) | virgule | miroir 10^(3j)/2^(10j) | chiffres de | ce qu'affiche un disque |")
ligne("|---|---|---|---|---|---|")
PALIERS = []
for j, nom, aff in ((1, "kilo/kibi", "1 ko → 0,977 Kio"), (2, "méga/mébi", "1 Mo → 0,954 Mio"),
                    (3, "giga/gibi", "1 To → 931 Gio"), (4, "téra/tébi", "1 To → 0,909 Tio")):
    q = Fr(2 ** (10 * j), 10 ** (3 * j))
    m_ = 1 / q
    assert m_ == Fr(5 ** (3 * j), 2 ** (7 * j))
    assert str(5 ** (10 * j)).startswith(dec(m_).split(",")[1].rstrip("0")[:12])
    PALIERS.append((j, float(q - 1), float(m_ - 1)))
    ligne(f"| {nom} | {dec(q)} | +{fr(100 * float(q - 1), '{:.4f}')} % | {dec(m_)} | 5^{10 * j} |"
          f" {aff} |")

ligne("\n### 2.4 Les trois écarts sur le cercle des décades\n")
ligne("On place les crans 2⁰, 2¹, …, 2^(N−1) sur un cercle dont un tour vaut une décade (la position de 2ʲ est la partie"
      " fractionnaire de j·log₁₀ 2). Le théorème des trois distances (conjecturé par Steinhaus, démontré en 1958 par Sós, Surányi et"
      " Świerczkowski ; partie XI)"
      " dit qu'il n'y a jamais plus de trois écarts différents. Chaque écart est un rapport 2^a/10^b, donc 2^x·5^y.\n")
L2D = mp.log10(2)


def trois_ecarts(N):
    p = sorted(mp.frac(j * L2D) for j in range(N))
    g = [p[i + 1] - p[i] for i in range(N - 1)] + [1 + p[0] - p[-1]]
    out = {}
    for x in g:
        cle = mp.nstr(x, 12)
        if cle not in out:
            s, t = min(((abs(s * L2D - t - x), s, t) for s in range(-250, 251) for t in range(-80, 81)),
                       key=lambda z: z[0])[1:]
            q = Fr(2 ** s, 1) / Fr(10) ** t if s >= 0 else Fr(10) ** (-t) / Fr(2 ** (-s), 1)
            out[cle] = [x, q, 0]
        out[cle][2] += 1
    return sorted(out.values(), key=lambda z: z[0])


def rapport(q):
    """2^a/10^b écrit en fraction réduite (2^x·5^y), ou en puissances quand c'est trop long."""
    if q.numerator < 10 ** 6 and q.denominator < 10 ** 6:
        return f"{q.numerator}/{q.denominator}"
    n_, d_ = q.numerator, q.denominator
    f_ = lambda m: "·".join(f"{p}{sup(e)}" for p in (2, 5) for e in [next(e for e in range(400) if m % p ** (e + 1))]
                            if e) or "1"
    return f"{f_(n_)}/{f_(d_)}"


ECARTS = {}
ligne("| crans | écarts (en décade) | rapports exacts | combien |")
ligne("|---:|---|---|---|")
for N in (4, 11, 21, 94):
    ECARTS[N] = trois_ecarts(N)
    ligne(f"| {N} | " + " ; ".join(fr(float(x), '{:.6f}') for x, _, _ in ECARTS[N]) + " | "
          + " ; ".join(rapport(q) for _, q, _ in ECARTS[N]) + " | "
          + " ; ".join(str(n_) for _, _, n_ in ECARTS[N]) + " |")
e21 = ECARTS[21]
assert e21[0][1] == Fr(128, 125) and e21[2][1] == Fr(5, 4) and e21[0][1] * e21[1][1] == e21[2][1]
ligne("\nPour 21 crans (2⁰ à 2²⁰) : 11 diesis 128/125, 8 écarts 625/512 = (5/4)⁴/2 et 2 tierces 5/4 ; le grand est le"
      " produit des deux petits. Les puissances de 5 occupent les positions symétriques (log₁₀ 5ʲ = j − log₁₀ 2ʲ) :"
      " mêmes écarts, dans l'ordre inverse.")

ligne("\n### 2.5 Les crans les plus proches des décades, et leurs reflets\n")


def fc(x, n):
    a = []
    for _ in range(n):
        q = int(mp.floor(x))
        a.append(q)
        x = 1 / (x - q)
    return a


FC = fc(L2D, 10)
ligne(f"Fraction continue de log₁₀ 2 : [{FC[0]}; {', '.join(map(str, FC[1:]))}, …]. Ses réduites donnent les crans qui"
      " tombent le plus près d'une décade, alternativement au-dessus et au-dessous.\n")
ligne("| j | 2ʲ ≈ 10ᵇ | écart de 2ʲ | 5ʲ ≈ 10^(j−b) | écart de 5ʲ | (1 + écart)(1 + écart miroir) |")
ligne("|---:|---|---|---|---|---|")
CONV = []
for j in (3, 10, 93, 196, 485, 2136):
    b = int(mp.nint(j * L2D))
    g2 = mp.mpf(2) ** j / mp.mpf(10) ** b - 1
    g5 = mp.mpf(5) ** j / mp.mpf(10) ** (j - b) - 1
    CONV.append((j, float(g2), float(g5)))
    ligne(f"| {j} | 10{sup(b)} | {fr(100 * float(g2), '{:+.4f}')} % | 10{sup(j - b)} | {fr(100 * float(g5), '{:+.4f}')} % |"
          f" {'1 (exact)' if abs((1 + g2) * (1 + g5) - 1) < mp.mpf(10) ** -30 else mp.nstr((1 + g2) * (1 + g5), 15)} |")

ligne("\n### 2.6 La tranche en crans\n")
ligne("| décade | cran le plus proche | 2⁻ᵐ ÷ 10⁻ᵏ | chiffres de 5ᵐ (les mêmes que 2⁻ᵐ) |")
ligne("|---|---|---|---|")
CRANS_TR = {}
for k in TR:
    m_ = int(mp.nint(k / L2D))
    rap = mp.mpf(10) ** k / mp.mpf(2) ** m_
    CRANS_TR[k] = (m_, float(rap))
    ligne(f"| 10⁻{sup(k)} | 2⁻{sup(m_)} | {fr(float(rap), '{:.4f}')} | {str(5 ** m_)[:12]}… |")
ligne(f"\nMiroir autour de 50 : 2⁻¹⁶³ × 2⁻¹⁶⁹ = (2⁻¹⁶⁶)², comme 10⁻⁴⁹ × 10⁻⁵¹ = (10⁻⁵⁰)² ; les écarts suivent :"
      f" {fr(CRANS_TR[49][1] * CRANS_TR[51][1], '{:.6f}')} = {fr(CRANS_TR[50][1] ** 2, '{:.6f}')}.")
assert CRANS_TR[49][0] + CRANS_TR[51][0] == 2 * CRANS_TR[50][0]

# ===========================================================================
# 3. Le cube qui tourne
# ===========================================================================
ligne("\n## 3. Le cube qui tourne : de deux carrés à l'hexagone\n")
SOMMETS = np.array(list(itertools.product((-0.5, 0.5), repeat=3)))
ARETES = [(i, j) for i in range(8) for j in range(i + 1, 8) if np.sum(np.abs(SOMMETS[i] - SOMMETS[j])) == 1]
rng = np.random.default_rng(26)


def repere(u, w=None):
    u = u / np.linalg.norm(u)
    if w is None:
        a = np.array([1.0, 0, 0]) if abs(u[0]) < 0.9 else np.array([0, 1.0, 0])
        w = a - (a @ u) * u
    w = w / np.linalg.norm(w)
    return w, np.cross(u, w)


def ombre_poly(u, w=None):
    e1, e2 = repere(u, w)
    P = np.c_[SOMMETS @ e1, SOMMETS @ e2]
    return P[ConvexHull(P).vertices]


def vect(a, b):
    """Produit vectoriel de deux vecteurs du plan (un nombre)."""
    return a[0] * b[1] - a[1] * b[0]


def aire_poly(P):
    x, y = P[:, 0], P[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))


err = 0.0
for _ in range(2000):
    u = rng.normal(size=3)
    u /= np.linalg.norm(u)
    err = max(err, abs(aire_poly(ombre_poly(u)) - np.abs(u).sum()))
ligne(f"- L'ombre du cube unité dans la direction u vaut |u₁| + |u₂| + |u₃| (2 000 directions au hasard, écart max"
      f" {err:.1e}). C'est √3·cos(angle avec la grande diagonale la plus proche).")
ligne("- Vues spéciales : face (carré) 1 ; diagonale de face (rectangle coupé en deux) √2 ; grande diagonale"
      " (hexagone) √3.")
mc = np.abs(rng.normal(size=(200000, 3)))
mc = (mc / np.linalg.norm(mc, axis=1)[:, None]).sum(axis=1).mean()
ligne(f"- Moyenne sur toutes les directions : 3/2 (Cauchy : un quart de la surface 6 ; ou 3 × ½ par la boîte à chapeau"
      f" d'Archimède, u₁ étant uniforme sur [−1, 1]). Monte-Carlo : {fr(mc, '{:.4f}')}.")

T_HEX = math.degrees(math.atan(1 / R2))
ligne("\n### 3.1 Le mouvement complet autour d'un axe d'ordre 2\n")
ligne("On tourne autour de l'axe (1, −1, 0)/√2, qui passe par les milieux de deux arêtes opposées ; la direction de vue"
      " est u(t) = cos t·(1, 1, 0)/√2 + sin t·(0, 0, 1). C'est le seul type d'axe dont le tour passe par les trois vues"
      " spéciales.\n")
ligne("    ombre(t) = √2·|cos t| + |sin t|\n")
ligne("| t | vue | ombre |")
ligne("|---|---|---|")
for t_, nom in ((0, "rectangle (diagonale de face)"), (T_HEX, "hexagone (grande diagonale)"), (90, "carré (face)"),
                (180 - T_HEX, "hexagone"), (180, "rectangle")):
    tr_ = math.radians(t_)
    ligne(f"| {fr(t_, '{:.2f}')}° | {nom} | {fr(R2 * abs(math.cos(tr_)) + abs(math.sin(tr_)), '{:.6f}')} |")
G1, G2 = math.degrees(math.acos(1 / 3)), math.degrees(math.acos(-1 / 3))
ligne(f"\n- Hexagones à ±{fr(T_HEX, '{:.2f}')}° et 180° ± {fr(T_HEX, '{:.2f}')}° : quatre par tour, séparés tour à tour"
      f" par {fr(G1, '{:.2f}')}° (autour du rectangle) et {fr(G2, '{:.2f}')}° (autour du carré), cos = ±1/3 : les angles"
      " du losange de la partie II.")
MOY = quad(lambda t: R2 * abs(math.cos(t)) + abs(math.sin(t)), 0, math.pi)[0] / math.pi
ligne(f"- Moyenne sur le tour : {fr(MOY, '{:.6f}')} = (2/π)(1 + √2) = {fr(2 / math.pi * (1 + R2), '{:.6f}')}.")
ligne(f"- Autres axes : d'ordre 4 (une face) 4/π = {fr(4 / math.pi, '{:.4f}')} ; d'ordre 3 (la grande diagonale, le tour"
      f" de la partie II vu de côté) (2/π)√6 = {fr(2 / math.pi * math.sqrt(6), '{:.4f}')}, le plus grand possible.")

ligne("\n### 3.2 Les deux carrés\n")


def recouvrement_num(u):
    """Aire commune des ombres des faces z = −½ et z = +½ (découpage de polygones convexes)."""
    e1, e2 = repere(u)
    def face(z):
        P = np.array([[x_, y_, z] for x_, y_ in ((-.5, -.5), (.5, -.5), (.5, .5), (-.5, .5))])
        Q = np.c_[P @ e1, P @ e2]
        return Q if vect(Q[1] - Q[0], Q[2] - Q[1]) > 0 else Q[::-1]
    sujet, coupe = list(face(-0.5)), face(0.5)
    for i in range(4):
        a, b = coupe[i], coupe[(i + 1) % 4]
        dedans = [vect(b - a, p - a) >= -1e-15 for p in sujet]
        nouv = []
        for j in range(len(sujet)):
            p, q = sujet[j - 1], sujet[j]
            dp, dq = dedans[j - 1], dedans[j]
            if dq:
                if not dp:
                    nouv.append(p + (q - p) * vect(b - a, a - p) / vect(b - a, q - p))
                nouv.append(q)
            elif dp:
                nouv.append(p + (q - p) * vect(b - a, a - p) / vect(b - a, q - p))
        sujet = nouv
        if not sujet:
            return 0.0
    return aire_poly(np.array(sujet)) if len(sujet) >= 3 else 0.0


def recouvrement(u):
    a, b, c = np.abs(u) / np.linalg.norm(u)
    return (c - a) * (c - b) / c if (a <= c and b <= c and c > 0) else 0.0


err = 0.0
for _ in range(1000):
    u = rng.normal(size=3)
    err = max(err, abs(recouvrement_num(u) - recouvrement(u)))
ligne(f"- Les faces avant et arrière (z = ±½) se projettent en deux parallélogrammes d'aire |u₃| décalés de l'ombre de"
      f" l'arête verticale. Leur partie commune vaut (|u₃| − |u₁|)(|u₃| − |u₂|)/|u₃| tant que |u₁|, |u₂| ≤ |u₃|, et 0"
      f" ensuite (1 000 directions, écart max {err:.1e}).")
ligne("- Sur le mouvement, de la face (t = 90°) à l'hexagone (t = 35,26°), elle passe de 1 à 0 : les deux carrés se"
      " quittent exactement à l'hexagone, où ils ne se touchent plus qu'au centre (les sommets (½, ½, ½) et"
      " (−½, −½, −½) s'y projettent tous les deux).")
ligne("- À l'hexagone, les trois paires de faces sont dans ce cas en même temps : six losanges de 60°/120°, d'aire"
      f" 1/√3 = {fr(1 / R3, '{:.5f}')} chacun ; trois devant (un pavage de l'hexagone), trois derrière (l'autre pavage)."
      " Le dessin en fil de fer superpose les deux : les six rayons.")

ligne("\n### 3.3 Le carré passe dans l'hexagone (Prince Rupert)\n")


def carre_lp(poly, phi):
    """Plus grand carré d'orientation phi dans le polygone convexe (programme linéaire en centre et côté)."""
    n = len(poly)
    A, b = [], []
    for i in range(n):
        p, q = poly[i], poly[(i + 1) % n]
        nr = np.array([q[1] - p[1], p[0] - q[0]])
        A.append(nr)
        b.append(nr @ p)
    R = np.array([[math.cos(phi), -math.sin(phi)], [math.sin(phi), math.cos(phi)]])
    rows, rhs = [], []
    for s1 in (-0.5, 0.5):
        for s2 in (-0.5, 0.5):
            wv = R @ np.array([s1, s2])
            for ai, bi in zip(A, b):
                rows.append([ai[0], ai[1], ai @ wv])
                rhs.append(bi)
    res = linprog([0, 0, -1], A_ub=rows, b_ub=rhs, bounds=[(None, None), (None, None), (0, None)], method="highs")
    return res.x[2], res.x[:2]


def carre_max(u, n_phi=12):
    poly = ombre_poly(np.asarray(u, float))
    phis = np.linspace(0, math.pi / 2, n_phi, endpoint=False)
    i = int(np.argmax([carre_lp(poly, p)[0] for p in phis]))
    r = minimize_scalar(lambda p: -carre_lp(poly, p)[0], bounds=(phis[i] - math.pi / 20, phis[i] + math.pi / 20),
                        method="bounded", options=dict(xatol=1e-11))
    s, c = carre_lp(poly, r.x)
    return s, r.x, c, poly


T1 = time.time()
WALLIS = carre_max([1, 1, 1])
NIEUW = carre_max([2, 2, 1])
GRILLE = []
for th in np.radians(np.linspace(8, 88, 9)):
    for ph in np.radians(np.linspace(2, 43, 6)):
        u = np.array([math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th)])
        GRILLE.append((carre_max(u, 8)[0], u))
best_g = max(GRILLE, key=lambda z: z[0])
voisins = []
for eps in ((0.01, 0, 0), (-0.01, 0, 0), (0, 0.01, 0), (0, -0.01, 0), (0, 0, 0.01), (0.007, -0.007, 0.004)):
    voisins.append(carre_max(np.array([2, 2, 1]) / 3 + np.array(eps))[0])
ligne(f"- Le long de la grande diagonale (l'hexagone, Wallis 1693) : côté {fr(WALLIS[0], '{:.8f}')} ;"
      f" √6 − √2 = {fr(math.sqrt(6) - R2, '{:.8f}')}.")
ligne(f"- Le long de (2, 2, 1)/3 (Nieuwland, publié en 1816) : côté {fr(NIEUW[0], '{:.8f}')} ;"
      f" 3√2/4 = {fr(3 * R2 / 4, '{:.8f}')} ; ombre 5/3 ; aire du carré 9/8.")
ligne(f"- Aucune des {len(GRILLE)} directions de la grille ne fait mieux (meilleure : {fr(best_g[0], '{:.5f}')}),"
      f" ni les 6 voisines de (2, 2, 1)/3 (meilleure : {fr(max(voisins), '{:.6f}')}).")
ligne("- (2, 2, 1) est le plus petit quadruplet de Pythagore : 1² + 2² + 2² = 3².")
T_NIEUW = math.degrees(math.asin(1 / 3))
ligne(f"- (2, 2, 1)/3 est sur le mouvement complet du § 3.1 : t = arcsin(1/3) = {fr(T_NIEUW, '{:.2f}')}°, entre le rectangle"
      f" (0°) et l'hexagone ({fr(T_HEX, '{:.2f}')}°), à {fr(T_HEX - T_NIEUW, '{:.2f}')}° de l'hexagone ; ombre"
      f" √2·cos t + sin t = 4/3 + 1/3 = 5/3. (calcul : {fr(time.time() - T1, '{:.0f}')} s)")

with open(os.path.join(ICI, "..", "resultats", "kakeya_miroir.md"), "w") as fh:
    fh.write("\n".join(md) + "\n")
print(f"calculs : {time.time() - T0:.1f} s")
T1 = time.time()


# ===========================================================================
# Figures
# ===========================================================================
def legende(ax, texte, y=-0.13):
    ax.text(0.5, y, texte, transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)


def schema(ax, xlim, ylim, egal=True):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if egal:
        ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for sp_ in ax.spines.values():
        sp_.set_visible(False)


def polys_tubes(k, delta, dx=0.0):
    a, t, h, c, b = tubes(k, delta)
    x0 = a + c * t  # bas du tube : a + sin θ
    return [[(ai - hi + dx, 1), (ai + hi + dx, 1), (xi + hi + dx, 1 - ci), (xi - hi + dx, 1 - ci)]
            for ai, hi, xi, ci in zip(a, h, x0, c)], b


BOITE = dict(boxstyle="round,pad=0.35", fc=F.SURF, ec=F.BASE)

# --------------------------- aa1 : Kakeya ---------------------------
fig = plt.figure(figsize=(21, 14.4))
gs = fig.add_gridspec(2, 3, wspace=0.2, hspace=0.42)

# a) les mêmes tubes, rangés en arbre
ax = fig.add_subplot(gs[0, 0])
D2 = 1e-2
KB2 = CONS[D2][0]
P0, _ = polys_tubes(0, D2)
P1, b1 = polys_tubes(KB2, D2)
x0max = max(p[0] for q in P0 for p in q)
x1min = min(p[0] for q in P1 for p in q)
dx1 = x0max - x1min + 0.22
P1, b1 = polys_tubes(KB2, D2, dx1)
x1max = max(p[0] for q in P1 for p in q)
ax.add_collection(PolyCollection(P0, facecolors=F.BLEU, edgecolors="none", alpha=0.3))
ax.add_collection(PolyCollection(P1, facecolors=[F.ORANGE if bb % 2 == 0 else VIOLET for bb in b1],
                                 edgecolors="none", alpha=0.32))
ax.plot([0, BASE, APEX, 0], [0, 0, 1, 0], color=F.MUTED, lw=1, ls="--")
schema(ax, (-0.08, x1max + 0.06), (-0.42, 1.12))
A0, A1 = aire_union(0, D2), CONS[D2][1][KB2]
nf2 = int(math.ceil((math.pi / 3) / D2))
ax.text(APEX, -0.1, f"un seul sommet (k = 0)\naire {fr(A0, '{:.3f}')}", ha="center", va="top", fontsize=9.6,
        color=F.BLEU)
ax.text((dx1 + x1max) / 2, -0.1, f"arbre de Perron, {2 ** KB2} branches\naire {fr(A1, '{:.3f}')}", ha="center",
        va="top", fontsize=9.6, color=F.ORANGE)
ax.text(APEX, 1.06, "triangle de Pál (pointillé)", ha="center", fontsize=8.6, color=F.MUTED)
ax.set_title(f"a)  Les mêmes {nf2} tubes, rangés en arbre")
legende(ax, f"Au grain δ = 10⁻² : {nf2} tubes 1 × δ, un par direction sur 60°. À gauche, ils partent tous du\n"
        f"même sommet ; à droite, l'arbre de Perron des parties V et XIV les recolle et les rapproche :\n"
        f"{fr(A0 / A1, '{:.1f}')} fois moins d'aire. Trois éventails tournés de 60° couvrent toutes les directions.",
        y=-0.02)

# b) l'aire contre le grain
ax = fig.add_subplot(gs[0, 1])
XK = np.array([-math.log10(d) for d in DELTAS])
CONS3 = np.array([3 * CONS[d][1][CONS[d][0]] for d in DELTAS])
xx = np.linspace(0.8, 6.3, 300)
bas = np.array([math.pi / (1 + 2 * GAM + 2 * (math.log(2) + x * math.log(10))) for x in xx])
ax.fill_between(XK, [borne_cordoba(3 * int(math.ceil((math.pi / 3) / d)), d) for d in DELTAS],
                np.minimum(CONS3, DELTOIDE), color=F.JAUNE, alpha=0.2, lw=0)
ax.plot(xx, bas, color=F.BLEU, lw=2.2, label="borne de Córdoba π/(1 + 2γ + 2 ln(2/δ)) : démontrée")
ax.plot(XK, CONS3, "o-", color=F.ORANGE, ms=6, lw=1.6, label="arbres de Perron en tubes : calculés")
for x_, d, v in zip(XK, DELTAS, CONS3):
    ax.text(x_, v * 1.07, f"2{sup(CONS[d][0])}", ha="center", fontsize=8.4, color=F.ORANGE)
ax.axhline(DELTOIDE, color=VERT, ls="--", lw=1.5)
ax.text(6.25, DELTOIDE * 1.04, "deltoïde de Kakeya, π/8", ha="right", fontsize=9, color=VERT)
ax.axhline(PAL, color=F.MUTED, ls=":", lw=1.5)
ax.text(6.25, PAL * 1.04, "triangle de Pál, 1/√3", ha="right", fontsize=9, color=F.MUTED)
ax.text(4.6, 0.17, "l'aire minimale\nest dans la bande", ha="center", fontsize=9.2, color=F.INK2)
ax.set_yscale("log")
ax.set_ylim(0.09, 1.6)
ax.set_xlim(0.8, 6.3)
ax.set_xlabel("chiffres du grain : k, avec δ = 10⁻ᵏ")
ax.set_ylabel("aire de l'union (toutes les directions)")
ax.legend(loc="upper right", bbox_to_anchor=(1.0, 0.86), fontsize=8.6, frameon=True, facecolor=F.SURF,
          edgecolor="none")
ax.set_title("b)  L'aire minimale contre le grain")
legende(ax, f"En exposant : 2³ = 8 branches à 10⁻¹, 2¹³ = 8192 à 10⁻⁵. Les arbres ne battent le deltoïde\n"
        f"qu'à partir de {puiss(croise[0])} : Besicovitch gagne, mais lentement. Le rapport construction ÷ borne\n"
        f"passe de {fr(CONS3[0] / borne_cordoba(33, 0.1), '{:.1f}')} à "
        f"{fr(CONS3[-1] / borne_cordoba(3 * int(math.ceil((math.pi / 3) / 1e-5)), 1e-5), '{:.1f}')} : la fenêtre se resserre.")

# c) la série harmonique des croisements
ax = fig.add_subplot(gs[0, 2])
Nm = int(round(math.pi / 1e-4))
dm = math.pi / Nm
jj = np.arange(1, Nm // 2 + 1)
cum = np.cumsum(np.minimum(1.0, dm / np.sin(jj * math.pi / Nm)))
ax.semilogx(jj, cum, color=F.BLEU, lw=2.4, label="recouvrement avec les j plus proches voisins (÷ δ)")
ax.semilogx(jj, np.log(jj) + GAM, color=F.ORANGE, lw=1.4, ls="--", label="ln j + γ (la série harmonique)")
for e in range(1, 5):
    j_ = 10 ** e
    ax.plot([j_, j_], [cum[j_ - 1] - math.log(10), cum[j_ - 1]], color=ROUGE, lw=1.6)
    ax.plot([j_ / 10, j_], [cum[j_ - 1] - math.log(10)] * 2, color=ROUGE, lw=0.8, ls=":")
ax.text(1.4e3, 3.5, "chaque décade de voisins\ncoûte ln 10 = 2,303", fontsize=9.2, color=ROUGE)
tot = 1 + 2 * cum[-1]
ax.text(1.3, 9.4, f"δ = 10⁻⁴, N = {Nm} directions\nrecouvrement total : 1 + 2 × {fr(cum[-1], '{:.3f}')} = "
        f"{fr(tot, '{:.3f}')}\n1 + 2γ + 2 ln(2/δ) = {fr(1 + 2 * GAM + 2 * math.log(2e4), '{:.3f}')}\n"
        f"aire ≥ π/{fr(tot, '{:.2f}')} = {fr(math.pi / tot, '{:.4f}')}", fontsize=9, va="top", bbox=BOITE)
ax.set_xlabel("j : rang du voisin (angle jδ)")
ax.set_ylabel("Σ min(1, δ/sin(iδ)), i ≤ j")
ax.set_ylim(0, 11.5)
ax.legend(loc="lower right", fontsize=8.6)
ax.set_title("c)  D'où vient le log : la série harmonique")
legende(ax, "Un tube croise son j-ième voisin (angle jδ) sur δ²/sin(jδ) ≈ δ/j au plus. Sur toutes les\n"
        "directions, son recouvrement vaut δ·(1 + 2γ + 2 ln(2/δ)). Cauchy–Schwarz (Córdoba, 1977)\n"
        "le change en aire minimale : π divisé par ce nombre. Le log vient de la série 1 + 1/2 + 1/3 + …")

# d) l'inverse de l'aire compte les chiffres
ax = fig.add_subplot(gs[1, 0])
kk = np.linspace(0, 57, 300)
haut = float(INV0) + float(PENTE) * kk
c_bas, c_haut = kk * math.log(10) / A_PLAT, kk * math.log(10) / A_LIM
ax.fill_between(kk, c_haut, haut, color=F.JAUNE, alpha=0.22, lw=0)
ax.plot(kk, haut, color=F.BLEU, lw=2.2, label="1/borne = 1,127 + 1,466·k : exact, aucun ensemble au-dessus")
ax.fill_between(kk, c_bas, c_haut, color=F.ORANGE, alpha=0.3, lw=0, label="constructions extrapolées (2,40 à "
                f"{fr(A_PLAT, '{:.2f}')} / ln(1/δ))")
ax.plot(XK, 1 / CONS3, "o", color=F.ORANGE, ms=6, label="constructions calculées (k ≤ 5)")
ax.axvspan(49, 55, color=F.JAUNE, alpha=0.25)
ax.text(52, 6, "tranche\n49 – 55", ha="center", fontsize=9.2, color=F.INK2)
ax.axhline(1 / DELTOIDE, color=VERT, ls="--", lw=1.3)
ax.text(30, 1 / DELTOIDE + 1.2, "deltoïde (1/(π/8) = 2,55)", fontsize=8.8, color=VERT)
ax.text(30, 62, "1/(aire minimale)\nest dans la bande jaune", ha="center", fontsize=9.2, color=F.INK2)
ax.set_xlim(0, 57)
ax.set_ylim(0, 88)
ax.set_xlabel("k (grain δ = 10⁻ᵏ)")
ax.set_ylabel("1 / aire")
ax.legend(loc="upper left", fontsize=8.5)
ax.set_title("d)  L'inverse de l'aire compte les chiffres")
legende(ax, "La borne est une droite en k : chaque chiffre de précision coûte le même inverse d'aire,\n"
        "2 ln 10/π = 1,466. L'aire de Kakeya lit l'exposant du grain, pas sa valeur.")

# e) la tranche
ax = fig.add_subplot(gs[1, 1])
for k in TR:
    lnd = k * math.log(10)
    lo, h1, h2 = 100 * float(BT[k]), 100 * A_LIM / lnd, 100 * A_PLAT / lnd
    ax.plot([k, k], [lo, h1], color=F.JAUNE, lw=10, alpha=0.45, solid_capstyle="butt")
    ax.plot([k, k], [h1, h2], color=F.ORANGE, lw=10, alpha=0.75, solid_capstyle="butt")
    F.point(ax, k, lo, F.BLEU, 8)
    ax.text(k, lo - 0.07, fr(lo / 100, '{:.4f}'), ha="center", va="top", fontsize=8.4, color=F.BLEU)
    ax.text(k, h2 + 0.06, fr(h2 / 100, '{:.4f}'), ha="center", va="bottom", fontsize=8.4, color=F.ORANGE)
ax.annotate("", (51, 1.06), (49, 1.06), arrowprops=dict(arrowstyle="<->", color=VIOLET, lw=1.3))
ax.text(50, 1.0, "1/L(49) + 1/L(51) = 2/L(50) : exact", ha="center", va="top", fontsize=9, color=VIOLET)
ax.set_xticks(TR)
ax.set_xticklabels([f"10⁻{sup(k)}" for k in TR])
ax.set_ylim(0.85, 2.85)
ax.set_xlim(48.4, 55.6)
ax.set_ylabel("aire (centièmes)")
ax.set_title("e)  La tranche : entre 1,2 et 2,6 centièmes")
legende(ax, f"Bleu : la borne démontrée. Orange : les arbres extrapolés (la plage 2,40 – {fr(A_PLAT, '{:.2f}')} sur\n"
        f"ln(1/δ)). L'aire minimale est entre les deux. Sur toute la tranche, elle ne perd que "
        f"{fr(100 * (1 - float(BT[55] / BT[49])), '{:.0f}')} %,\nalors que le grain est divisé par un million.")

# f) les deux couches
ax = fig.add_subplot(gs[1, 2])
kk = np.linspace(0, 56, 300)
ax.semilogy(kk, 10.0 ** -kk, color=F.INK, lw=2, label="le grain 10⁻ᵏ : la chèvre lit ce nombre")
ax.semilogy(kk, [float(borne_tranche(x)) for x in kk], color=F.BLEU, lw=2.2, label="Kakeya, borne du bas")
k4 = kk[kk >= 4]
ax.fill_between(k4, k4 * 0 + np.minimum(A_LIM / (k4 * math.log(10)), DELTOIDE),
                np.minimum(A_PLAT / (k4 * math.log(10)), DELTOIDE), color=F.ORANGE, alpha=0.35, lw=0,
                label="Kakeya, constructions")
ax.axvspan(49, 55, color=F.JAUNE, alpha=0.25)
ax.text(52, 1e-12, "×10⁻⁶\nsur la\ntranche", ha="center", fontsize=9, color=F.INK)
ax.text(40, 0.25, f"× {fr(float(BT[55] / BT[49]), '{:.3f}')} sur la tranche", ha="center", fontsize=9, color=F.BLEU)
ax.set_ylim(1e-58, 5)
ax.set_xlim(0, 56)
ax.set_xlabel("k (grain δ = 10⁻ᵏ)")
ax.set_ylabel("valeur (échelle log)")
ax.legend(loc="lower left", fontsize=8.6)
ax.set_title("f)  Deux couches : la chèvre lit 10⁻ᵏ, Kakeya lit k")
legende(ax, "En échelle log, le grain descend d'une décade par chiffre (la couche linéaire des chiffres) ;\n"
        "l'aire de Kakeya ne bouge qu'en 1/k (la couche des exposants). Les deux couches de la partie XIX\n"
        "se lisent ici sur le même grain.")
F.sauver(fig, "aa1_kakeya.png")
print(f"aa1 : {time.time() - T1:.1f} s")

# --------------------------- aa2 : la virgule et son miroir ---------------------------
fig = plt.figure(figsize=(21, 14.4))
gs = fig.add_gridspec(2, 3, wspace=0.2, hspace=0.42)
COUL_E = {Fr(128, 125): ROUGE, Fr(625, 512): VIOLET, Fr(5, 4): F.AQUA}

# a) le cercle des décades
ax = fig.add_subplot(gs[0, 0])
schema(ax, (-1.62, 1.62), (-1.55, 1.68))
ax.add_patch(Circle((0, 0), 1, fill=False, ec=F.BASE, lw=1.2))
POS = [float(mp.frac(j * L2D)) for j in range(21)]


def angle(p_):
    return math.pi / 2 - 2 * math.pi * p_


ordre = sorted(range(21), key=lambda j: POS[j])
for i in range(21):
    j1, j2 = ordre[i], ordre[(i + 1) % 21]
    p1, p2 = POS[j1], POS[j2] + (1 if i == 20 else 0)
    q = min(COUL_E, key=lambda r_: abs(float(mp.log10(mp.mpf(r_.numerator) / r_.denominator)) - (p2 - p1)))
    ax.add_patch(Arc((0, 0), 2.16, 2.16, theta1=math.degrees(angle(p2)), theta2=math.degrees(angle(p1)),
                     color=COUL_E[q], lw=4.5))
for j in range(21):
    a_ = angle(POS[j])
    F.point(ax, math.cos(a_), math.sin(a_), F.ORANGE, 7)
    rr = 1.24 + 0.15 * (j // 10)
    ax.text(rr * math.cos(a_), rr * math.sin(a_), str(j), ha="center", va="center", fontsize=8.4, color=F.ORANGE)
    b_ = math.pi - a_  # le reflet : log₁₀ 5ʲ = j − log₁₀ 2ʲ
    ax.plot(0.88 * math.cos(b_), 0.88 * math.sin(b_), "o", ms=4.5, color=F.BLEU)
ax.text(0, 1.60, "10ᵏ : le début de chaque décade", ha="center", fontsize=9, color=F.INK2)
y_ = 0.34
for q, nom in ((Fr(128, 125), "128/125, le diesis"), (Fr(625, 512), "625/512 = (5/4)⁴/2"), (Fr(5, 4), "5/4, la tierce")):
    n_ = next(c_ for _, r_, c_ in ECARTS[21] if r_ == q)
    ax.plot([-0.6, -0.46], [y_, y_], color=COUL_E[q], lw=4.5)
    ax.text(-0.42, y_, f"{nom} : × {n_}", va="center", fontsize=8.5, color=F.INK)
    y_ -= 0.19
ax.text(0, -0.36, "orange : 2ʲ (j = 0 … 20)\nbleu : 5ʲ, au reflet", ha="center", va="center", fontsize=8.8,
        color=F.INK2)
ax.set_title("a)  Le cercle des décades : 21 crans, trois écarts")
legende(ax, "Un tour = une décade ; 2ʲ est placé en j·log₁₀ 2. Les 21 crans de 2⁰ à 2²⁰ ne laissent que trois\n"
        "écarts (théorème des trois distances), tous des rapports exacts de 2 et de 5. Les puissances de 5\n"
        "occupent les places symétriques, puisque 2ʲ·5ʲ = 10ʲ : mêmes écarts, lus dans l'autre sens.", y=-0.02)

# b) les paliers et leurs miroirs
ax = fig.add_subplot(gs[0, 1])
js = np.array([1, 2, 3, 4])
haut_ = np.array([100 * g for _, g, _ in PALIERS])
bas_ = np.array([100 * m for _, _, m in PALIERS])
ax.bar(js - 0.18, haut_, width=0.34, color=F.ORANGE, alpha=0.85, label="virgule : 2^(10j)/10^(3j) − 1")
ax.bar(js + 0.18, bas_, width=0.34, color=F.BLEU, alpha=0.85, label="miroir : 10^(3j)/2^(10j) − 1")
for j_, h_, b_ in zip(js, haut_, bas_):
    ax.plot([j_ - 0.36, j_ - 0.0], [2.4 * j_] * 2, color=F.INK, lw=1.4, ls="--")
    ax.plot([j_ + 0.0, j_ + 0.36], [-2.4 * j_] * 2, color=F.INK, lw=1.4, ls="--")
    ax.text(j_ - 0.18, h_ + 0.25, f"+{fr(h_, '{:.2f}')}", ha="center", fontsize=8.8, color=F.ORANGE)
    ax.text(j_ + 0.18, -2.4 * j_ - 0.35, fr(b_, '{:.2f}'), ha="center", va="top", fontsize=8.8, color=F.BLEU)
for j_, txt in ((1, "0,9765625\n(5¹⁰)"), (2, "0,953674…\n(5²⁰)"), (3, "0,931322…\n(5³⁰)"), (4, "0,909494…\n(5⁴⁰)")):
    ax.text(j_ + 0.18, -12.9, txt, ha="center", va="top", fontsize=8.2, color=F.BLEU)
ax.text(3.18, -10.0, "« 1 To » →\n931 Go", ha="center", va="top", fontsize=8.2, color=F.INK2)
ax.plot([], [], color=F.INK, lw=1.4, ls="--", label="± 2,4 % × j : le compte sans retenue")
ax.axhline(0, color=F.INK, lw=1)
ax.set_xticks(js)
ax.set_xticklabels(["kilo / kibi", "méga / mébi", "giga / gibi", "téra / tébi"])
ax.set_ylim(-17.0, 13.5)
ax.set_ylabel("écart (%)")
ax.legend(loc="upper left", fontsize=8.6)
ax.set_title("b)  Kilo, méga, giga, téra : la virgule et son miroir")
legende(ax, "La virgule se multiplie (× 128/125 par palier) : en chiffres, elle dépasse 2,4 % × j de ses\n"
        "retenues, et le miroir reste en deçà. Le miroir est un nombre exact à chiffres finis, ceux de\n"
        "5¹⁰, 5²⁰, 5³⁰, 5⁴⁰ : c'est le « 1 To » qu'un ordinateur affiche 931 Go.")

# c) trois lectures du même double
ax = fig.add_subplot(gs[0, 2])
vals = [(float(SPAN) * 100, "cran − miroir\n(1 + c) − 1/(1 + c)", F.BLEU),
        (float(DOUBLE) * 100, "double 2c\n(chiffres de 2²¹)", F.ORANGE),
        (float(CARRE) * 100, "carré (1 + c)² − 1\n(le téra)", VIOLET)]
x0_ = 9.2
YB = [3.0, 2.0, 1.0]
for (v, nom, col), y_ in zip(vals, YB):
    ax.barh(y_, v - x0_, left=x0_, height=0.5, color=col, alpha=0.8)
    ax.text(v + 0.015, y_, f"{fr(v, '{:.4f}')} %", va="center", fontsize=9.6, color=col, fontweight="bold")
ax.set_yticks(YB)
ax.set_yticklabels([n_ for _, n_, _ in vals], fontsize=9)
ax.annotate("", (vals[1][0], 2.5), (vals[0][0], 2.5), arrowprops=dict(arrowstyle="<->", color=ROUGE, lw=1.3))
ax.text(vals[1][0] + 0.015, 2.5, "retenue c²/(1 + c) = 0,2250 %", va="center", fontsize=8.6, color=ROUGE)
ax.annotate("", (vals[2][0], 1.5), (vals[1][0], 1.5), arrowprops=dict(arrowstyle="<->", color=ROUGE, lw=1.3))
ax.text(vals[2][0] + 0.015, 1.5, "retenue c² = 0,2360 %", va="center", fontsize=8.6, color=ROUGE)
ax.text(x0_ + 0.02, 0.35, f"En log, les trois valent exactement 2 × {fr(float(LG), '{:.4f}')} = "
        f"{fr(2 * float(LG), '{:.4f}')} décade :\nle miroir est un reflet parfait et le double est exact.\n"
        "Les chiffres (la couche linéaire) le cassent en trois,\nséparés par les deux retenues.",
        fontsize=9.2, va="top", bbox=BOITE)
ax.set_xlim(x0_, 10.45)
ax.set_ylim(-1.0, 3.5)
ax.set_xlabel("écart (%), axe coupé à 9,2")
ax.set_title("c)  9,49 – 9,72 – 9,95 : trois lectures du même double")
legende(ax, "c = 0,048576, la virgule du méga. La distance du cran à son miroir (9,49 %) est presque le\n"
        "double de 4,86 % ; le double « à la main » donne 9,72 % ; le vrai cran suivant, le téra, est\n"
        "à 9,95 %. Le double est presque au milieu des deux autres : à c³/(2(1 + c)) = 0,0055 % près.")

# d) la retenue court jusqu'au 9
ax = fig.add_subplot(gs[1, 0])
schema(ax, (0, 10), (-0.8, 7.2), egal=False)
X0 = 2.6
haut_r = {1: 1, 2: 1, 3: 1, 4: 1}  # retenues reçues par les colonnes 1 à 4 (en partant de la gauche)
for i, ch in enumerate("048576"):
    x_ = X0 + i * 0.95
    ax.text(x_, 5.0, ch, ha="center", fontsize=24, family="monospace", color=F.INK)
    ax.text(x_, 3.9, ch, ha="center", fontsize=24, family="monospace", color=F.INK)
    r_ = "097152"[i]
    ax.text(x_, 2.3, r_, ha="center", fontsize=24, family="monospace",
            color=ROUGE if i == 1 else F.ORANGE, fontweight="bold")
    if i in haut_r:
        ax.text(x_, 6.25, "1", ha="center", fontsize=14, family="monospace", color=ROUGE)
        ax.annotate("", (x_ + 0.12, 6.45), (x_ + 0.9, 5.85), arrowprops=dict(arrowstyle="->", color=ROUGE, lw=1.1,
                                                                            connectionstyle="arc3,rad=0.4"))
ax.text(X0 - 0.95, 3.9, "+", ha="center", fontsize=24, family="monospace", color=F.INK)
ax.plot([X0 - 1.2, X0 + 5.4], [3.55, 3.55], color=F.INK, lw=1.5)
ax.text(X0 - 0.95, 2.3, "=", ha="center", fontsize=24, family="monospace", color=F.INK)
ax.text(X0 + 5.6, 6.25, "retenues", va="center", fontsize=9.5, color=ROUGE)
ax.text(0.3, 1.35, "1,048576 × 2 = 2,097152 = 2²¹/10⁶ : le double se lit\ndans les chiffres du cran suivant.",
        fontsize=9.6, color=F.INK, va="center")
ax.text(0.3, 0.35, "4,86 % × 2 = 9,72 % ; mais 1,048576² = 1,099511627776 : 9,95 %.", fontsize=9.6, color=F.INK,
        va="center")
ax.text(0.3, -0.35, "Le 4 absorbe la dernière retenue et devient le 9.", fontsize=9.6, color=ROUGE, va="center")
ax.set_title("d)  La retenue court jusqu'au 9")
legende(ax, "6 + 6 = 12, 7 + 7 + 1 = 15, 5 + 5 + 1 = 11, 8 + 8 + 1 = 17 : quatre retenues de suite, de droite\n"
        "à gauche, jusqu'au 4 qui devient 9. Le double linéaire 9,72 % est exact en chiffres ; ce qui le\n"
        "sépare du carré (9,95 %) est la retenue de la multiplication, c² = 0,236 %.", y=-0.02)

# e) les réduites et leurs reflets
ax = fig.add_subplot(gs[1, 1])
for j, g2, g5 in CONV:
    ax.plot(j, abs(g2) * 100, marker="^" if g2 > 0 else "v", color=F.ORANGE, ms=11, ls="none")
    ax.plot(j * 1.28, abs(g5) * 100, marker="^" if g5 > 0 else "v", color=F.BLEU, ms=11, ls="none")
    ax.text(j * 0.85, abs(g2) * 100, f"2{sup(j)}", ha="right", va="center", fontsize=9, color=F.ORANGE)
    ax.text(j * 1.5, abs(g5) * 100, f"5{sup(j)}", ha="left", va="center", fontsize=9, color=F.BLEU)
ax.plot([], [], "^", color=F.INK2, ls="none", label="au-dessus de la décade")
ax.plot([], [], "v", color=F.INK2, ls="none", label="au-dessous")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1.8, 12000)
ax.set_ylim(0.008, 60)
ax.set_xlabel("j (les dénominateurs des réduites de log₁₀ 2)")
ax.set_ylabel("|écart à la décade la plus proche| (%)")
ax.legend(loc="upper right", fontsize=8.8)
ax.text(2.2, 0.012, "log₁₀ 2 = [0; 3, 3, 9, 2, 2, 4, 6, 2, 1, …]\n(1 + écart de 2ʲ)(1 + écart de 5ʲ) = 1",
        fontsize=9, bbox=BOITE)
ax.set_title("e)  Les crans les plus près des décades, et leurs reflets")
legende(ax, "2³ ≈ 10, 2¹⁰ ≈ 10³, 2⁹³ ≈ 10²⁸, 2¹⁹⁶ ≈ 10⁵⁹, 2⁴⁸⁵ ≈ 10¹⁴⁶, 2²¹³⁶ ≈ 10⁶⁴³ : tour à tour au-dessus et\n"
        "au-dessous. Chaque fois, 5ʲ tombe de l'autre côté de sa décade, au même écart en log : les gaps\n"
        "sont des nombres (des rapports exacts de 2 et de 5), et viennent par paires de reflets.")

# f) vingt crans dans la tranche, dans les deux sens
ax = fig.add_subplot(gs[1, 2])
schema(ax, (-48.6, -55.75), (-2.4, 3.3), egal=False)
ax.plot([-49, -55], [2.1, 2.1], color=F.INK, lw=1.4)
for k in TR:
    ax.plot([-k, -k], [1.95, 2.25], color=F.INK, lw=1.6)
    ax.text(-k, 2.45, f"10⁻{sup(k)}", ha="center", fontsize=9.6, color=F.INK)
lg2 = math.log10(2)
ax.plot([-49, -49 - 20 * lg2], [0.9, 0.9], color=F.ORANGE, lw=1.4)
ax.plot([-55, -55 + 20 * lg2], [-0.5, -0.5], color=F.BLEU, lw=1.4)
for j in range(21):
    ax.plot([-49 - j * lg2] * 2, [0.78, 1.02], color=F.ORANGE, lw=1.1 if j % 5 else 2)
    ax.plot([-55 + j * lg2] * 2, [-0.62, -0.38], color=F.BLEU, lw=1.1 if j % 5 else 2)
ax.text(-49.05, 1.25, "20 crans descendus depuis 10⁻⁴⁹", fontsize=9.2, color=F.ORANGE, fontweight="bold")
ax.text(-55.0, -0.2, "20 crans montés depuis 10⁻⁵⁵", ha="right", fontsize=9.2, color=F.BLEU, fontweight="bold")
for x_, y_ in ((-55, 0.9), (-49, -0.5)):
    ax.plot([x_, x_], [y_ - 0.35, 2.1], color=F.MUTED, lw=0.8, ls=":")
F.point(ax, -49 - 20 * lg2, 0.9, ROUGE, 8)
F.point(ax, -55 + 20 * lg2, -0.5, ROUGE, 8)
ax.text(-55.0, 0.62, "−4,63 % : le miroir, 0,95367431640625·10⁻⁵⁵ = 5²⁰·10⁻⁶⁹", ha="right", va="top",
        fontsize=8.6, color=ROUGE)
ax.text(-49.0, -1.0, "+4,86 % : 1,048576·10⁻⁴⁹ = 2²⁰·10⁻⁵⁵", ha="left", va="top", fontsize=8.6, color=ROUGE)
ax.text(-52, -1.75, "les deux règles sont le reflet l'une de l'autre autour de 10⁻⁵² ;\n"
        "chacune dépasse la tranche d'une virgule (0,0206 décade), d'un côté différent", ha="center", va="top",
        fontsize=9, color=F.INK2)
ax.set_title("f)  Vingt crans dans la tranche, dans les deux sens")
legende(ax, "La règle du panneau f de la partie XXV, et son reflet. Descendus depuis 10⁻⁴⁹, vingt crans tombent\n"
        "4,63 % sous 10⁻⁵⁵ : le miroir, aux chiffres de 5²⁰. Montés depuis 10⁻⁵⁵, ils dépassent 10⁻⁴⁹ de\n"
        "4,86 % : la virgule. La mesure qui manquait a donc un sens des deux côtés.", y=-0.02)
F.sauver(fig, "aa2_virgule_miroir.png")
print(f"aa2 : {time.time() - T1:.1f} s")


# --------------------------- aa3 : le cube qui tourne ---------------------------
fig = plt.figure(figsize=(21, 19.5))
gs_h = fig.add_gridspec(1, 1, top=0.975, bottom=0.835)
gs = fig.add_gridspec(2, 3, top=0.775, bottom=0.07, wspace=0.2, hspace=0.42)
W_AXE = np.array([1.0, -1.0, 0.0]) / R2
FACE = {(i, s_): [k for k in itertools.product((-0.5, 0.5), repeat=2)] for i in range(3) for s_ in (-0.5, 0.5)}


def vue(t):
    """Direction de vue au temps t (degrés) et repère d'écran : horizontale w × u, verticale = l'axe de rotation."""
    tr = math.radians(t)
    u = np.array([math.cos(tr) / R2, math.cos(tr) / R2, math.sin(tr)])
    return u, np.cross(W_AXE, u), W_AXE


def coins_face(i, s_):
    """Les 4 sommets de la face x_i = s_, dans l'ordre du tour."""
    j, k = [m for m in range(3) if m != i]
    pts = []
    for a_, b_ in ((-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5)):
        p_ = np.zeros(3)
        p_[i], p_[j], p_[k] = s_, a_, b_
        pts.append(p_)
    return np.array(pts)


def projette(P, h, w, dx=0.0, dy=0.0):
    return np.c_[P @ h + dx, P @ w + dy]


def dessine_cube(ax, t, dx, dy=0.0, faces=True, lw=1.1):
    u, h, w = vue(t)
    P = projette(SOMMETS, h, w, dx, dy)
    for a_, b_ in ARETES:
        ax.plot(P[[a_, b_], 0], P[[a_, b_], 1], color=F.INK2, lw=lw, zorder=3)
    if faces:
        for s_, col in ((0.5, F.ORANGE), (-0.5, F.BLEU)):
            Q = projette(coins_face(2, s_), h, w, dx, dy)
            ax.add_patch(Polygon(Q, closed=True, fc=col, alpha=0.28, ec=col, lw=1.8, zorder=2))
    return u


# a) le mouvement complet
ax = fig.add_subplot(gs_h[0, 0])
T_NIEUW = math.degrees(math.asin(1 / 3))
TS = [(0, "rectangle\n√2"), (T_NIEUW, "trou de Nieuwland\n5/3"), (T_HEX, "hexagone\n√3"), (54, "deux carrés\n{}"),
      (72, "deux carrés\n{}"), (90, "carré\n1"), (108, "deux carrés\n{}"), (126, "deux carrés\n{}"),
      (180 - T_HEX, "hexagone\n√3"), (180 - T_NIEUW, "trou de Nieuwland\n5/3"), (180, "rectangle\n√2")]
PAS = 1.95
schema(ax, (-1.0, PAS * (len(TS) - 1) + 1.0), (-1.75, 1.05), egal=False)
for i, (t, nom) in enumerate(TS):
    u = dessine_cube(ax, t, i * PAS)
    A_ = np.abs(u).sum()
    ax.text(i * PAS, -1.02, f"{fr(t, '{:.2f}').rstrip('0').rstrip(',')}°", ha="center", va="top", fontsize=9.6,
            color=F.INK, fontweight="bold")
    ax.text(i * PAS, -1.3, nom.format(fr(A_, '{:.3f}')), ha="center", va="top", fontsize=9,
            color=ROUGE if "hexagone" in nom else F.INK2)
ax.annotate("", (PAS * 10 + 0.6, 0.93), (-0.6, 0.93), arrowprops=dict(arrowstyle="->", color=F.MUTED, lw=1.2))
ax.set_title("a)  Le mouvement complet : du rectangle au rectangle, par l'hexagone, les deux carrés et le carré")
legende(ax, "Vue orthographique, rotation autour de l'axe vertical, qui passe par les milieux de deux arêtes "
        "opposées. Orange : la face avant ; bleu : la face arrière (les « deux carrés »). Sous chaque image, l'aire de "
        "l'ombre.\n Les deux carrés se recouvrent près du carré, ne se touchent plus qu'au centre à "
        "l'hexagone, puis s'écartent. Un demi-tour ramène le cube sur lui-même : c'est le « mouvement complet », "
        "comme le demi-tour de l'aiguille de Kakeya.", y=-0.02)

# b) l'ombre pendant le tour
ax = fig.add_subplot(gs[0, 0])
tt = np.linspace(0, 360, 2881)
A_t = R2 * np.abs(np.cos(np.radians(tt))) + np.abs(np.sin(np.radians(tt)))
ax.plot(tt, A_t, color=F.BLEU, lw=2.2)
HEX = [T_HEX, 180 - T_HEX, 180 + T_HEX, 360 - T_HEX]
ax.plot(HEX, [R3] * 4, "h", color=ROUGE, ms=11, label="hexagone : √3")
ax.plot([90, 270], [1, 1], "s", color=F.ORANGE, ms=9, label="carré : 1")
ax.plot([0, 180, 360], [R2] * 3, "D", color=VIOLET, ms=8, label="rectangle : √2", clip_on=False)
NV = [T_NIEUW, 180 - T_NIEUW, 180 + T_NIEUW, 360 - T_NIEUW]
ax.plot(NV, [5 / 3] * 4, "*", color=F.INK, ms=12, label="trou de Nieuwland : 5/3")
ax.axhline(MOY, color=F.AQUA, ls="--", lw=1.4, label=f"moyenne du tour : (2/π)(1 + √2) = {fr(MOY, '{:.3f}')}")
ax.axhline(1.5, color=F.MUTED, ls=":", lw=1.4, label="moyenne sur toutes les directions : 3/2")
for a_, b_, txt in ((HEX[0], HEX[1], f"{fr(G2, '{:.2f}')}°"), (HEX[1], HEX[2], f"{fr(G1, '{:.2f}')}°"),
                    (HEX[2], HEX[3], f"{fr(G2, '{:.2f}')}°")):
    ax.annotate("", (b_, 1.83), (a_, 1.83), arrowprops=dict(arrowstyle="<->", color=ROUGE, lw=1.2))
    ax.text((a_ + b_) / 2, 1.85, txt, ha="center", va="bottom", fontsize=9, color=ROUGE)
ax.set_xticks([0, 90, 180, 270, 360])
ax.set_xlim(0, 360)
ax.set_ylim(0.42, 1.97)
ax.set_xlabel("t (degrés)")
ax.set_ylabel("aire de l'ombre")
ax.legend(loc="lower center", fontsize=8.2, ncol=2, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("b)  L'ombre pendant le tour : √2·|cos t| + |sin t|")
legende(ax, "Quatre hexagones par tour, séparés tour à tour par 109,47° (autour du\n"
        "carré) et 70,53° (autour du rectangle) : les angles du losange de la partie II,\n"
        "cos = ∓1/3. Les creux sont des miroirs (la courbe y est symétrique). Partout,\n"
        "l'ombre vaut √3 × cos(angle avec la grande diagonale la plus proche).")

# c) les deux carrés se quittent à l'hexagone
ax = fig.add_subplot(gs[0, 1])
tt = np.linspace(0.2, 90, 600)
ov = [recouvrement(vue(t)[0]) for t in tt]
ax.plot(tt, np.sin(np.radians(tt)), color=F.ORANGE, lw=1.6, ls="--", label="aire de chaque carré vu : sin t")
ax.plot(tt, ov, color=VIOLET, lw=2.4, label="leur partie commune : (sin t − cos t/√2)²/sin t")
tc = np.arange(5, 91, 5)
ax.plot(tc, [recouvrement_num(vue(t)[0]) for t in tc], "o", color=VIOLET, ms=5, mfc=F.SURF,
        label="découpage des polygones (contrôle)")
ax.axvline(T_HEX, color=ROUGE, ls=":", lw=1.4)
ax.text(T_HEX - 1, 0.66, "hexagone (35,26°) :\nils se quittent,\nil reste le centre", ha="right", fontsize=9,
        color=ROUGE)
ax.plot([T_NIEUW] * 2, [0, 0.22], color=F.INK2, ls=":", lw=1)
ax.text(T_NIEUW + 0.8, 0.04, "Nieuwland", fontsize=8.6, color=F.INK2)
ax.set_xlim(0, 92)
ax.set_ylim(0, 1.08)
ax.set_xlabel("t (0° : rectangle ; 90° : carré)")
ax.set_ylabel("aire")
ax.legend(loc="upper left", fontsize=8.4)
ax.set_title("c)  Les deux carrés se quittent à l'hexagone")
legende(ax, "Les faces avant et arrière se projettent en deux parallélogrammes d'aire |u₃|,\n"
        "décalés de l'ombre de l'arête qui les relie. Leur partie commune\n"
        "(|u₃| − |u₁|)(|u₃| − |u₂|)/|u₃| tombe à 0 exactement à l'hexagone, où les\n"
        "sommets (½, ½, ½) et (−½, −½, −½) se projettent au même point.")

# d) l'hexagone : trois losanges devant, trois derrière
ax = fig.add_subplot(gs[0, 2])
schema(ax, (-1.15, 3.55), (-2.75, 1.75))
u_, h_, w_ = vue(T_HEX)
COUL_F = {0: F.AQUA, 1: F.JAUNE, 2: F.ORANGE}
for (s_, dx_, dy_, titre) in ((0.5, 0.0, 0.75, "devant : un pavage"), (-0.5, 2.4, 0.75, "derrière : l'autre pavage")):
    for i in range(3):
        Q = projette(coins_face(i, s_), h_, w_, dx_, dy_)
        col = COUL_F[i] if s_ > 0 else [F.BLEU, VIOLET, F.MUTED][i]
        ax.add_patch(Polygon(Q, closed=True, fc=col, alpha=0.45, ec=F.INK2, lw=1.2))
    ax.text(dx_, dy_ - 0.98, titre, ha="center", va="top", fontsize=9.4, color=F.INK2)
dessine_cube(ax, T_HEX, 1.2, -1.45, faces=False, lw=1.3)
for s_, col in ((0.5, F.ORANGE), (-0.5, F.BLEU)):
    Q = projette(coins_face(2, s_), h_, w_, 1.2, -1.45)
    ax.add_patch(Polygon(Q, closed=True, fc=col, alpha=0.35, ec=col, lw=1.8))
F.point(ax, 1.2, -1.45, ROUGE, 8)
ax.text(2.35, -1.45, "fil de fer :\nles deux à la fois,\nsix rayons", ha="left", va="center", fontsize=9.4,
        color=F.INK2)
ax.set_title("d)  L'hexagone : trois losanges devant, trois derrière")
legende(ax, "Le long de la grande diagonale, les six carrés deviennent des losanges de\n"
        "60°/120° d'aire 1/√3. Les trois de devant pavent l'hexagone d'une façon, les\n"
        "trois de derrière de l'autre : le cube de Necker qui s'inverse. Le fil de fer\n"
        "montre les deux ; les deux carrés d'une paire (orange, bleu) ne se touchent\n"
        "qu'au centre (point rouge).", y=-0.02)

# e) le carré passe dans l'hexagone
ax = fig.add_subplot(gs[1, 0])
schema(ax, (-1.05, 3.55), (-1.65, 1.15))
for (res, u_r, dx_, txt) in ((WALLIS, np.array([1.0, 1, 1]), 0.0,
                              f"le long de la grande diagonale\n(Wallis, 1693) : côté √6 − √2\n= {fr(WALLIS[0], '{:.4f}')}"),
                             (NIEUW, np.array([2.0, 2, 1]), 2.45,
                              f"le long de (2, 2, 1)/3\n(Nieuwland, 1816) : côté 3√2/4\n= {fr(NIEUW[0], '{:.4f}')}")):
    s_c, phi_c, c_c, poly = res
    e1, e2 = repere(u_r)
    P = np.c_[SOMMETS @ e1 + dx_, SOMMETS @ e2]
    ax.add_patch(Polygon(poly + [dx_, 0], closed=True, fc=F.BLEU, alpha=0.13, ec=F.BLEU, lw=1.6))
    for a_, b_ in ARETES:
        ax.plot(P[[a_, b_], 0], P[[a_, b_], 1], color=F.MUTED, lw=0.8)
    R_ = np.array([[math.cos(phi_c), -math.sin(phi_c)], [math.sin(phi_c), math.cos(phi_c)]])
    coins = np.array([c_c + s_c * R_ @ np.array(v) for v in ((-.5, -.5), (.5, -.5), (.5, .5), (-.5, .5))])
    ax.add_patch(Polygon(coins + [dx_, 0], closed=True, fill=False, ec=ROUGE, lw=2.2))
    ax.text(dx_, -1.08, txt, ha="center", va="top", fontsize=9.2, color=F.INK)
ax.text(0, 1.0, "ombre √3", ha="center", fontsize=9, color=F.BLEU)
ax.text(2.45, 1.0, "ombre 5/3", ha="center", fontsize=9, color=F.BLEU)
ax.set_title("e)  Le carré passe dans l'hexagone (Prince Rupert)")
legende(ax, "Un cube passe par un trou percé dans un cube de même taille si un carré\n"
        "de côté 1 tient dans l'ombre. Dans l'hexagone, le plus grand carré a pour\n"
        "côté 1,035 ; le meilleur trou suit la direction pythagoricienne (2, 2, 1)/3\n"
        "(1 + 4 + 4 = 9) : côté 1,0607. Elle est sur le même tour, à 19,47°.", y=-0.02)

# f) l'ombre sur toute la sphère
ax = fig.add_subplot(gs[1, 1])
lon = np.linspace(-180, 180, 721)
lat = np.linspace(-90, 90, 361)
LO, LA = np.meshgrid(np.radians(lon), np.radians(lat))
OMB = np.abs(np.cos(LA) * np.cos(LO)) + np.abs(np.cos(LA) * np.sin(LO)) + np.abs(np.sin(LA))
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402

ax.imshow(OMB, extent=(-180, 180, -90, 90), origin="lower", aspect="auto",
          cmap=LinearSegmentedColormap.from_list("seq", F.SEQ[:11]))
ax.contour(lon, lat, OMB, levels=[1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7], colors=F.SURF, linewidths=0.6)
LH = math.degrees(math.atan(1 / R2))
ax.plot([45, 135, -45, -135] * 2, [LH] * 4 + [-LH] * 4, "h", color=ROUGE, ms=11, ls="none",
        label="hexagones √3 (grandes diagonales)")
ax.plot([0, 90, 180, -90, -180, 0, 0], [0, 0, 0, 0, 0, 89, -89], "s", color=F.ORANGE, ms=8, ls="none",
        label="carrés 1 (faces)")
ax.plot([45, 135, -45, -135, 0, 90, 180, -90, -180] * 1 + [0, 90, 180, -90, -180],
        [0] * 4 + [45] * 5 + [-45] * 5, "D", color=VIOLET, ms=6, ls="none", label="rectangles √2 (diagonales de face)")
ax.plot([45, 45], [-90, 90], color=ROUGE, lw=1.6, ls="--", label="le mouvement complet")
ax.plot([-135, -135], [-90, 90], color=ROUGE, lw=1.6, ls="--")
ax.plot([45, 45, -135, -135], [T_NIEUW, -T_NIEUW, T_NIEUW, -T_NIEUW], "*", color=F.INK, ms=12, ls="none",
        label="trou de Nieuwland (5/3)")
ax.set_xlim(-180, 180)
ax.set_ylim(-90, 90)
ax.set_xticks([-180, -90, 0, 90, 180])
ax.set_yticks([-90, -45, 0, 45, 90])
ax.set_xlabel("longitude de la direction de vue (°)")
ax.set_ylabel("latitude (°)")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize=8.4)
ax.set_title("f)  L'ombre sur toute la sphère des directions")
legende(ax, "|u₁| + |u₂| + |u₃| : 8 sommets √3 (les hexagones), 6 creux 1 (les carrés),\n"
        "12 cols √2 (les rectangles). Le mouvement complet suit un méridien :\n"
        "un rectangle, un hexagone, le carré au pôle, puis l'autre hexagone.", y=-0.25)

# g) la grande diagonale se retourne
ax = fig.add_subplot(gs[1, 2])
schema(ax, (-1.45, 1.45), (-1.4, 1.5))
ax.add_patch(Circle((0, 0), R3 / 2, fc=F.BLEU, alpha=0.1, ec=F.BLEU, lw=1.4))
th_ = np.linspace(0, 2 * math.pi, 600)
xd0 = R3 / 4 * (2 * np.cos(th_) + np.cos(2 * th_))
yd0 = R3 / 4 * (2 * np.sin(th_) - np.sin(2 * th_))
cr_, sr_ = math.cos(math.pi / 3), math.sin(math.pi / 3)
xd, yd = cr_ * xd0 - sr_ * yd0, sr_ * xd0 + cr_ * yd0  # pointes à 60°, 180° et 300°
ax.fill(xd, yd, color=VERT, alpha=0.25, lw=0)
ax.plot(xd, yd, color=VERT, lw=1.6)
for t in np.arange(0, 180, 12):
    a_ = math.radians(T_HEX - t)
    ax.plot([-R3 / 2 * math.cos(a_), R3 / 2 * math.cos(a_)], [-R3 / 2 * math.sin(a_), R3 / 2 * math.sin(a_)],
            color=F.INK2, lw=0.8, alpha=0.55)
ax.plot([-R3 / 2, R3 / 2], [0, 0], color=ROUGE, lw=2.4)
ax.annotate("", (1.08, 0), (1.38, 0), arrowprops=dict(arrowstyle="->", color=ROUGE, lw=1.4))
ax.text(1.23, 0.08, "œil", ha="center", fontsize=9, color=ROUGE)
L3 = 3 * float(mp.pi / (1 + 2 * mp.euler + 2 * mp.log(2 * R3 * mp.mpf(10) ** 50)))
ax.text(-1.42, 1.45, f"disque balayé (bleu) : 3π/4 = {fr(3 * math.pi / 4, '{:.3f}')}\ndeltoïde (vert) : 3π/8 = "
        f"{fr(3 * math.pi / 8, '{:.3f}')}\nau grain 10⁻⁵⁰ : au moins {fr(L3, '{:.3f}')}", fontsize=9, va="top",
        bbox=BOITE)
ax.set_title("g)  La grande diagonale se retourne")
legende(ax, "Dans le plan du mouvement, chaque grande diagonale (l'aiguille la plus\n"
        "longue du cube, √3) fait un demi-tour sur son milieu et balaie un disque ; face\n"
        "à l'œil (rouge), c'est l'hexagone. Le deltoïde de Kakeya retourne la même\n"
        "aiguille dans moitié moins d'aire ; Besicovitch, dans aussi peu qu'on veut.", y=-0.02)
F.sauver(fig, "aa3_cube_hexagone.png")
print(f"figures : {time.time() - T1:.1f} s ; total : {time.time() - T0:.1f} s")
