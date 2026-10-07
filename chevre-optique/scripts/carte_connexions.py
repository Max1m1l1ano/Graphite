"""
Partie XXVII : la carte des connexions — le graphe de nos chapitres et les liens qu'il prédit.

    python3 scripts/carte_connexions.py        # ≈ 20 s
    python3 scripts/carte_connexions.py 30     # exploration : la carte des parties I à XXX, sans rien réécrire

Écrit resultats/carte_connexions.md, figures/ab1_carte.png, figures/ab2_cercles_arctiques.png et
figures/ab3_liens_predits.png.

1. Le graphe : chaque partie I à XXVI est un nœud ; deux parties sont reliées quand l'une cite l'autre (« partie XIX »,
   « parties V et XIV », ou un lien vers son fichier). Degrés, matrice, et prédiction des liens manquants par les voisins
   communs (indice d'Adamic–Adar).
2. Les cercles arctiques : pavages aléatoires du losange par des dominos (le diamant aztèque, 2^(n(n+1)/2) pavages) et de
   l'hexagone par des losanges (les cubes empilés, MacMahon) ; le désordre ne vit que dans le cercle inscrit.
3. Les autres liens prédits : l'échelle des taux de change du grain (puissances, puis logarithmes) ; l'ombre du cube et
   les 2n chèvres (‖u‖₁·‖u‖∞ ≥ 1, égalité sur les 26 directions du cube de 27 points) ; Archimède dans l'ombre du cube.
"""

import collections
import itertools
import logging
import math
import os
import re
import sys
import textwrap
import time
from fractions import Fraction as Fr

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from matplotlib.collections import PolyCollection
from matplotlib.patches import Circle, Polygon, Rectangle

sys.path.insert(0, os.path.dirname(__file__))
import chevre as ch  # noqa: E402
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
DOSSIER = os.path.join(ICI, "..")
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


ROMAINS = [(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def romain(n):
    s = ""
    for v, c in ROMAINS:
        while n >= v:
            s += c
            n -= v
    return s


def depuis_romain(s):
    val = {"I": 1, "V": 5, "X": 10, "L": 50}
    t = 0
    for i, c in enumerate(s):
        v = val[c]
        t += -v if i + 1 < len(s) and val[s[i + 1]] > v else v
    return t


# ===========================================================================
# 1. Le graphe des parties
# ===========================================================================
ligne("# Résultats de la partie XXVII (générés par scripts/carte_connexions.py)\n")
EXPLORATION = len(sys.argv) > 1  # avec un argument N : la carte des parties I à N, affichée seulement
NMAX = int(sys.argv[1]) if EXPLORATION else 26
ligne(f"## 1. Le graphe des parties I à {romain(NMAX)}\n")
TOUS = {}
for f in sorted(os.listdir(DOSSIER)):
    if not f.endswith(".md") or f == "CLAUDE.md":
        continue
    with open(os.path.join(DOSSIER, f)) as fh:
        tete = fh.readline()
    m = re.match(r"# Partie ([IVXL]+)", tete)
    num = depuis_romain(m.group(1)) if m else (1 if f == "README.md" else None)
    if num is not None:
        TOUS[f] = num
FICHIERS = {f: n for f, n in TOUS.items() if n <= NMAX}
assert sorted(FICHIERS.values()) == list(range(1, NMAX + 1))
MOTIF = re.compile(r"[Pp]arties? ((?:[IVXL]+(?:,\s*|\s+et\s+|\s+à\s+|\s*–\s*)?)+)")
CITE = collections.Counter()
for f, n in FICHIERS.items():
    with open(os.path.join(DOSSIER, f)) as fh:
        txt = fh.read()
    lignes_gardees = []
    for l_ in txt.split("\n"):
        refs = [depuis_romain(x) for m_ in MOTIF.finditer(l_) for x in re.findall(r"[IVXL]+", m_.group(1))]
        refs += [TOUS.get(g_, 0) for g_ in re.findall(r"\]\(([a-z0-9-]+\.md)", l_)]
        liens_futurs = any(r_ > NMAX for r_ in refs)  # les lignes ajoutées plus tard renvoient à une partie > NMAX
        if not liens_futurs:
            lignes_gardees.append(l_)
    txt = "\n".join(lignes_gardees)
    for m in MOTIF.finditer(txt):
        groupe = m.group(1)
        nums = re.findall(r"[IVXL]+", groupe)
        if re.search(r"\sà\s|–", groupe) and len(nums) == 2:
            cibles = range(depuis_romain(nums[0]), depuis_romain(nums[1]) + 1)
        else:
            cibles = [depuis_romain(x) for x in nums]
        for c in cibles:
            if 1 <= c <= NMAX and c != n:
                CITE[(n, c)] += 1
    for m in re.finditer(r"\]\(([a-z0-9-]+\.md)", txt):
        g = m.group(1)
        if g in FICHIERS and FICHIERS[g] != n:
            CITE[(n, FICHIERS[g])] += 1
POIDS = collections.Counter()
for (a, b), c in CITE.items():
    POIDS[tuple(sorted((a, b)))] += c
VOIS = {i: set() for i in range(1, NMAX + 1)}
for a, b in POIDS:
    VOIS[a].add(b)
    VOIS[b].add(a)
DEG = {i: len(VOIS[i]) for i in VOIS}
NPAIRES = NMAX * (NMAX - 1) // 2
ligne(f"- {len(POIDS)} paires reliées sur {NPAIRES} ({fr(100 * len(POIDS) / NPAIRES, '{:.1f}')} %) ;"
      f" {sum(CITE.values())} renvois au total.")
ligne(f"- La partie I (le README) porte l'index de la série : elle est reliée à {DEG[1]} parties sur {NMAX - 1}. On ne"
      " prédit donc pas de liens avec elle.")
TITRES = {
    1: "la chèvre (README)", 2: "Archimède, le cube qui tourne", 3: "π, √2 et les dimensions", 4: "les trois solides",
    5: "Kakeya, Perron", 6: "le ménisque de 0,35 %", 7: "les polynômes", 8: "foyer, diaphragme, Fibonacci",
    9: "le moiré de Fibonacci", 10: "le point et le carré, Ptolémée", 11: "l'angle d'or, trois distances",
    12: "144, la douzième lentille", 13: "Perron tournés, cos/sin", 14: "l'aiguille sur une grille",
    15: "la grille décalée", 16: "ménisque et projection", 17: "deux foyers, récursion d'argent",
    18: "faire des ronds avec des carrés", 19: "les bases sont des objets", 20: "deux chèvres au même endroit",
    21: "les trois 24, le miroir 49-50-51", 22: "le carré de neuf points", 23: "la relecture : lentilles, boules, grain",
    24: "un tiers de dimension", 25: "les ouverts, la tranche 49 – 55", 26: "Kakeya à 10⁻⁵⁰, kibi, cube",
    27: "la carte des connexions", 28: "octaèdre, Perron démontré, Venn à 17",
    29: "le Venn à 17 au ppm"}
ligne("\n| partie | sujet | voisins | renvois reçus |")
ligne("|---|---|---:|---:|")
RECUS = collections.Counter()
for (a, b), c in CITE.items():
    RECUS[b] += c
for n in sorted(DEG, key=lambda z: (-DEG[z], z)):
    ligne(f"| {romain(n)} | {TITRES.get(n, next(f for f, v in FICHIERS.items() if v == n))} | {DEG[n]} | {RECUS[n]} |")

ligne("\n### 1.1 Les liens que le graphe prédit\n")
ligne("Pour deux parties qui ne se citent pas, on additionne 1/ln(degré) sur leurs voisins communs (indice d'Adamic–Adar) :"
      " deux chapitres qui fréquentent les mêmes chapitres, surtout des chapitres peu cités, devraient se parler.\n")
PRED = []
for a, b in itertools.combinations(range(2, NMAX + 1), 2):
    if b in VOIS[a]:
        continue
    communs = VOIS[a] & VOIS[b]
    PRED.append((sum(1 / math.log(DEG[z]) for z in communs if DEG[z] > 1), len(communs), a, b))
PRED.sort(key=lambda z: (-z[0], z[2], z[3]))
RANG = {(a, b): i + 1 for i, (_, _, a, b) in enumerate(PRED)}
ETABLIS = {(23, 26): "§ 3 : l'échelle des taux de change", (15, 18): "§ 2 : les cercles arctiques",
           (4, 26): "§ 5 : Archimède dans l'ombre du cube", (22, 26): "§ 4 : les 26 directions et les 2n chèvres",
           (2, 15): "§ 2 : l'hexagone des cubes empilés",
           (15, 26): "§ 2 : la grille décalée et les losanges", (18, 26): "§ 2 : des ronds avec des losanges",
           (2, 18): "§ 2 : la sphère médiane, cercle arctique", (6, 20): "§ 6 : les deux bouts du ménisque",
           (14, 17): "§ 7 : les aiguilles d'argent", (6, 26): "§ 8 : arccos(1/3), le tétraèdre dans le cube"}
ligne("| rang | paire | voisins communs | indice | dans cette partie |")
ligne("|---:|---|---:|---|---|")
for i, (s_, c_, a, b) in enumerate(PRED[:15]):
    ligne(f"| {i + 1} | {romain(a)} – {romain(b)} | {c_} | {fr(s_, '{:.2f}')} | {ETABLIS.get((a, b), '—')} |")
ligne("\nLes pistes (prédites, pas encore établies) et leurs voisins communs :\n")
for s_, c_, a, b in PRED[:15]:
    if (a, b) not in ETABLIS:
        ligne(f"- {romain(a)} – {romain(b)} : " + ", ".join(romain(z) for z in sorted(VOIS[a] & VOIS[b])))
if EXPLORATION:
    sys.exit(0)
ligne("\nRangs des autres paires établies ici : " + " ; ".join(
    f"{romain(a)} – {romain(b)} : {RANG[(a, b)]}e" for (a, b) in ETABLIS if RANG[(a, b)] > 15) + ".")

# ===========================================================================
# 2. Les cercles arctiques
# ===========================================================================
ligne("\n## 2. Les cercles arctiques\n")
rng = np.random.default_rng(27)
DR, DL, DU, DD = 0, 1, 2, 3  # direction du partenaire de la case dans son domino


def diamant(n):
    """Diamant aztèque d'ordre n : cases (i, j) de centre (j − n + ½, n − i − ½) avec |x| + |y| ≤ n."""
    N = 2 * n
    I, J = np.mgrid[0:N, 0:N]
    dedans = np.abs(J - n + 0.5) + np.abs(n - I - 0.5) <= n
    P = -np.ones((N, N), int)
    for i in range(N):
        js = np.where(dedans[i])[0]
        for k in range(0, len(js), 2):
            P[i, js[k]], P[i, js[k] + 1] = DR, DL
    return P, dedans


def balayage_dominos(P, rng):
    """Dynamique de Glauber : chaque bloc 2 × 2 formé de deux dominos parallèles tourne d'un quart de tour avec
    probabilité ½ (blocs disjoints traités ensemble). La loi uniforme sur les pavages est stationnaire."""
    N = P.shape[0]
    for a in (0, 1):
        for b in (0, 1):
            A, B = P[a:N - 1:2, b:N - 1:2], P[a:N - 1:2, b + 1:N:2]
            C, D = P[a + 1:N:2, b:N - 1:2], P[a + 1:N:2, b + 1:N:2]
            m0 = min(A.shape[0], B.shape[0], C.shape[0], D.shape[0])
            m1 = min(A.shape[1], B.shape[1], C.shape[1], D.shape[1])
            A, B, C, D = A[:m0, :m1], B[:m0, :m1], C[:m0, :m1], D[:m0, :m1]
            piece = rng.random(A.shape) < 0.5
            hor = (A == DR) & (C == DR) & piece
            ver = (A == DD) & (B == DD) & piece
            A[hor], B[hor], C[hor], D[hor] = DD, DD, DU, DU
            A[ver], B[ver], C[ver], D[ver] = DR, DL, DR, DL


def compte_dominos(dedans):
    """Nombre exact de pavages par dominos d'une région (programmation dynamique ligne par ligne)."""
    N = dedans.shape[0]
    dp = {0: 1}
    for i in range(N):
        nd = collections.Counter()
        for masque, c in dp.items():
            pile = [(0, masque, 0)]
            while pile:
                j, cur, nxt = pile.pop()
                if j == N:
                    nd[nxt] += c
                    continue
                if not dedans[i, j] or (cur >> j) & 1:
                    pile.append((j + 1, cur, nxt))
                    continue
                if j + 1 < N and dedans[i, j + 1] and not (cur >> (j + 1)) & 1:
                    pile.append((j + 2, cur | (3 << j), nxt))
                if i + 1 < N and dedans[i + 1, j]:
                    pile.append((j + 1, cur | (1 << j), nxt | (1 << j)))
        dp = nd
    return dp.get(0, 0)


def compte_partitions(a):
    """Partitions planes dans une boîte a × a × a (lignes décroissantes, colonnes décroissantes)."""
    lignes_ = [s for s in itertools.product(range(a + 1), repeat=a) if all(s[k] >= s[k + 1] for k in range(a - 1))]
    dp = {s: 1 for s in lignes_}
    for _ in range(a - 1):
        dp = {s: sum(c for t, c in dp.items() if all(x <= y for x, y in zip(s, t))) for s in lignes_}
    return sum(dp.values())


def macmahon(a, b, c):
    q = Fr(1)
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                q *= Fr(i + j + k - 1, i + j + k - 2)
    return q


ligne("### 2.1 Les comptes exacts\n")
ligne("| ordre n | pavages du diamant aztèque (comptés) | 2^(n(n+1)/2) | | côté a | partitions planes a × a × a (comptées) |"
      " MacMahon |")
ligne("|---:|---|---|---|---:|---|---|")
AZT, HEXA = {}, {}
for n in range(1, 7):
    AZT[n] = compte_dominos(diamant(n)[1])
    assert AZT[n] == 2 ** (n * (n + 1) // 2)
for a in range(1, 5):
    HEXA[a] = compte_partitions(a)
    assert HEXA[a] == macmahon(a, a, a)
for n in range(1, 7):
    a_ = f"| {n} | {HEXA[n]} | {macmahon(n, n, n)} |" if n in HEXA else f"| {n} | — | {macmahon(n, n, n)} |"
    ligne(f"| {n} | {AZT[n]} | 2^{n * (n + 1) // 2} | " + a_)
ligne("\n- L'ordre 4 a 2¹⁰ = 1 024 pavages (le kibi) et l'ordre 6 en a 2²¹ = 2 097 152 (les chiffres du 9,72 de la partie"
      " XXVI) : chaque étage n multiplie le compte par 2ⁿ, il compte en crans.")
ligne("- L'hexagone de côté 1 a 2 pavages : les deux lectures du cube de Necker (partie XXVI).")

T1 = time.time()
N_AZ, PAS_AZ = 48, 40000
P_AZ, DEDANS_AZ = diamant(N_AZ)
SUIVI_AZ = []
for s in range(PAS_AZ + 1):
    balayage_dominos(P_AZ, rng)
    if s % 5000 == 0:
        SUIVI_AZ.append((s, float(np.sum((P_AZ == DU) | (P_AZ == DD)) / np.sum(DEDANS_AZ))))


def dominos(P, n):
    """Liste des dominos : (x, y, horizontal, type), type 0–3 selon l'orientation et la couleur du damier."""
    out = []
    N = P.shape[0]
    for i in range(N):
        for j in range(N):
            if P[i, j] == DR:
                out.append((j - n + 1.0, n - i - 0.5, True, (i + j) % 2))
            elif P[i, j] == DD:
                out.append((j - n + 0.5, n - i - 1.0, False, 2 + (i + j) % 2))
    return out


DOM = dominos(P_AZ, N_AZ)
assert len(DOM) == np.sum(DEDANS_AZ) // 2


def profil(points, rayon, bords):
    """Part du type majoritaire de chaque coin, selon la distance au centre (en rayons du cercle inscrit)."""
    res = []
    for r0, r1 in bords:
        sel = [(t, c) for (r, t, c) in points if r0 <= r / rayon < r1]
        if not sel:
            res.append(float("nan"))
            continue
        par_coin = collections.defaultdict(collections.Counter)
        for t, c in sel:
            par_coin[c][t] += 1
        res.append(sum(max(cnt.values()) for cnt in par_coin.values()) / len(sel))
    return res


PTS_AZ = []
for x, y, _, t in DOM:
    coin = int(((math.degrees(math.atan2(y, x)) + 45) % 360) // 90)  # 4 secteurs autour des 4 pointes
    PTS_AZ.append((math.hypot(x, y), t, coin))
BORDS = [(0.0, 0.25), (0.25, 0.5), (0.5, 0.75), (0.75, 0.9), (0.9, 1.0), (1.0, 1.1), (1.1, 1.25), (1.25, 1.42)]
PROF_AZ = profil(PTS_AZ, N_AZ / R2, BORDS)
ligne(f"\n### 2.2 Le losange : un diamant aztèque d'ordre {N_AZ} ({len(DOM)} dominos, {PAS_AZ} balayages)\n")
ligne("Part des dominos verticaux au fil des balayages (½ attendu par symétrie) : "
      + ", ".join(f"{s} : {fr(v, '{:.3f}')}" for s, v in SUIVI_AZ) + ".")
ligne("\n| distance au centre (en rayons du cercle inscrit) | part du type majoritaire de chaque secteur |")
ligne("|---|---|")
for (r0, r1), v in zip(BORDS, PROF_AZ):
    ligne(f"| {fr(r0, '{:.2f}')} – {fr(r1, '{:.2f}')} | {fr(v, '{:.3f}')} |")
ligne("\nDans le cercle, les quatre sortes de dominos se mélangent ; dehors, chaque coin n'en garde qu'une (gelé).")


def balayage_cubes(H, a, rng):
    """Bain thermique sur une partition plane : chaque hauteur est tirée uniformément entre ses voisines."""
    m = H.shape[0]
    I, J = np.indices((m, m))
    for par in (0, 1):
        Hp = np.pad(H, 1, constant_values=0)
        Hp[0, :] = a
        Hp[:, 0] = a
        bas = np.maximum(Hp[2:, 1:-1], Hp[1:-1, 2:])
        haut = np.minimum(Hp[:-2, 1:-1], Hp[1:-1, :-2])
        neuf = bas + np.floor(rng.random((m, m)) * (haut - bas + 1)).astype(int)
        msk = (I + J) % 2 == par
        H[msk] = neuf[msk]


N_HX, PAS_HX = 40, 24000
H_HX = np.zeros((N_HX, N_HX), int)
SUIVI_HX = []
for s in range(PAS_HX + 1):
    balayage_cubes(H_HX, N_HX, rng)
    if s % 4000 == 0:
        SUIVI_HX.append((s, float(H_HX.mean() / N_HX)))
assert np.all(H_HX[:-1] >= H_HX[1:]) and np.all(H_HX[:, :-1] >= H_HX[:, 1:])
S32 = R3 / 2


def iso(x, y, z):
    """Vue le long de la grande diagonale (1, 1, 1)."""
    return ((y - x) * S32, z - (x + y) / 2)


def losanges(H, a):
    """Les 3a² losanges du pavage : faces visibles des cubes empilés (dessus z, côtés x et y)."""
    L = {0: [], 1: [], 2: []}
    for i in range(a):
        for j in range(a):
            h = H[i, j]
            L[2].append([iso(i, j, h), iso(i + 1, j, h), iso(i + 1, j + 1, h), iso(i, j + 1, h)])
    Hx = np.vstack([np.full((1, a), a), H, np.zeros((1, a), int)])
    Hy = np.hstack([np.full((a, 1), a), H, np.zeros((a, 1), int)])
    for i in range(-1, a):
        for j in range(a):
            for k in range(Hx[i + 2, j], Hx[i + 1, j]):
                L[0].append([iso(i + 1, j, k), iso(i + 1, j + 1, k), iso(i + 1, j + 1, k + 1), iso(i + 1, j, k + 1)])
    for i in range(a):
        for j in range(-1, a):
            for k in range(Hy[i, j + 2], Hy[i, j + 1]):
                L[1].append([iso(i, j + 1, k), iso(i + 1, j + 1, k), iso(i + 1, j + 1, k + 1), iso(i, j + 1, k + 1)])
    return L


LOS = losanges(H_HX, N_HX)
assert all(len(v) == N_HX ** 2 for v in LOS.values())
CENTRE_HX = iso(N_HX / 2, N_HX / 2, N_HX / 2)
R_IN_HX = N_HX * S32
PTS_HX = []
for t, polys in LOS.items():
    for q in polys:
        cx = sum(p[0] for p in q) / 4 - CENTRE_HX[0]
        cy = sum(p[1] for p in q) / 4 - CENTRE_HX[1]
        coin = int(((math.degrees(math.atan2(cy, cx)) + 360) % 360) // 60)  # 6 secteurs autour des 6 sommets
        PTS_HX.append((math.hypot(cx, cy), t, coin))
BORDS_HX = [(0.0, 0.25), (0.25, 0.5), (0.5, 0.75), (0.75, 0.9), (0.9, 1.0), (1.0, 1.06), (1.06, 1.12), (1.12, 1.16)]
PROF_HX = profil(PTS_HX, R_IN_HX, BORDS_HX)
ligne(f"\n### 2.3 L'hexagone : cubes empilés dans une boîte {N_HX} × {N_HX} × {N_HX} ({3 * N_HX ** 2} losanges,"
      f" {PAS_HX} balayages)\n")
ligne("Hauteur moyenne ÷ côté au fil des balayages (½ attendu par symétrie) : "
      + ", ".join(f"{s} : {fr(v, '{:.3f}')}" for s, v in SUIVI_HX) + ".")
ligne("\n| distance au centre (en rayons du cercle inscrit) | part du type majoritaire de chaque secteur |")
ligne("|---|---|")
for (r0, r1), v in zip(BORDS_HX, PROF_HX):
    ligne(f"| {fr(r0, '{:.2f}')} – {fr(r1, '{:.2f}')} | {fr(v, '{:.3f}')} |")
ligne(f"\n(échantillonnage : {fr(time.time() - T1, '{:.0f}')} s)")
ligne("\n### 2.4 Les deux cercles\n")
ligne(f"- Losange de sommets (±1, 0), (0, ±1) : cercle inscrit de rayon 1/√2 = {fr(1 / R2, '{:.6f}')}, d'aire π/2 ="
      f" la moitié du disque circonscrit ; il couvre π/4 = {fr(math.pi / 4, '{:.4f}')} du losange.")
ligne(f"- Hexagone du cube (ombre le long de la grande diagonale, côté √(2/3)) : cercle inscrit de rayon √2/2, l'ombre de la"
      f" sphère médiane (partie II) ; il couvre π/(2√3) = {fr(math.pi / (2 * R3), '{:.4f}')} de l'hexagone, la densité"
      " de l'empilement hexagonal des disques.")

# ===========================================================================
# 3. L'échelle des taux de change du grain
# ===========================================================================
ligne("\n## 3. L'échelle des taux de change du grain (XXIII – XXV – XXVI)\n")
EPS_K = 50
SERIE_C = 1.0303  # meilleure précision de la série : ≈ 1,03·2^(−n/2)/n (partie XXV)


def n_serie(k):
    """Dimension à partir de laquelle la série tronquée au mieux atteint 10^−k."""
    f_ = lambda n: math.log10(SERIE_C) - n / 2 * math.log10(2) - math.log10(n) + k
    lo, hi = 1.0, 10.0 * k + 50
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f_(mid) > 0 else (lo, mid)
    return (lo + hi) / 2


def inv_kakeya(k):
    return float((1 + 2 * mp.euler + 2 * mp.log(2) + 2 * k * mp.log(10)) / mp.pi)


ECHELLE = [("l'équateur (la tranche de demi-largeur ε contient la moitié de la boule)", "ε⁻²", lambda k: 0.455 * 10.0 ** (2 * k)),
           ("la coquille (épaisseur ε, la moitié du volume)", "ε⁻¹", lambda k: math.log(2) * 10.0 ** k),
           ("le plan de la lentille", "ε⁻¹", lambda k: 10.0 ** k - 1),
           ("le ménisque (la chèvre et son simplexe)", "ε^(−1/2)", lambda k: 0.577 * 10.0 ** (k / 2)),
           ("la série en 1/n, tronquée au mieux", "≈ 2·log₂(1/ε)", n_serie),
           ("Kakeya : l'inverse de l'aire minimale", "≈ (2/π)·ln(1/ε)", inv_kakeya)]
ligne("| lecture | loi | à 10⁻⁵⁰ | par décade de grain |")
ligne("|---|---|---|---|")
for nom, loi, f_ in ECHELLE:
    v = f_(EPS_K)
    pas = f_(EPS_K + 1) / f_(EPS_K) if loi.startswith("ε") else f_(EPS_K + 1) - f_(EPS_K)
    pas_t = f"× {fr(pas, '{:.4g}')}" if loi.startswith("ε") else f"+ {fr(pas, '{:.3f}')}"
    e_ = math.floor(math.log10(v))
    v_t = f"{fr(v / 10 ** e_, '{:.2f}')}·10{str(e_).translate(str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹'))}" if v > 1e6 \
        else fr(v, '{:.1f}')
    ligne(f"| {nom} | {loi} | {v_t} | {pas_t} |")
ligne(f"\n- La série gagne un facteur √2 par dimension (2^(−n/2)) : un cran de la partie XXI. Une décade de grain coûte donc"
      f" 2·log₂ 10 = {fr(2 * math.log2(10), '{:.4f}')} dimensions, autant de crans qu'il y en a dans une décade.")
ligne("- Les exposants 2, 1, ½ se divisent par deux à chaque marche ; le logarithme est la marche 0 :"
      " ln(1/ε) = lim (ε^(−s) − 1)/s quand s → 0.")
def sci(x):
    e = math.floor(math.log10(x))
    return fr(x, '{:.1f}') if e < 6 else f"{fr(x / 10 ** e, '{:.2f}')}·10{str(e).translate(str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹'))}"


for s_ in (1, 0.5, 0.1, 0.01, 0.001):
    ligne(f"  - s = {fr(s_, '{:g}')} : (ε^(−s) − 1)/s à 10⁻⁵⁰ = {sci((10.0 ** (EPS_K * s_) - 1) / s_)}")
ligne(f"  - limite : ln(10⁵⁰) = {fr(EPS_K * math.log(10), '{:.4f}')}")

# ===========================================================================
# 4. L'ombre du cube et les 2n chèvres
# ===========================================================================
ligne("\n## 4. L'ombre du cube et les 2n chèvres (XXII – XXVI)\n")
err = float("inf")
for _ in range(20000):
    u = rng.normal(size=3)
    u /= np.linalg.norm(u)
    err = min(err, np.abs(u).sum() * np.abs(u).max() - 1)
DIRS = [np.array(v) for v in itertools.product((-1, 0, 1), repeat=3) if any(v)]
PROD = [np.abs(v).sum() / np.linalg.norm(v) * np.abs(v).max() / np.linalg.norm(v) for v in DIRS]
assert all(abs(p - 1) < 1e-12 for p in PROD) and len(DIRS) == 26
ligne(f"- Pour u unitaire : ombre(u) × cos(angle au piquet le plus proche) = ‖u‖₁·‖u‖∞ ≥ ‖u‖₂² = 1"
      f" (sur 20 000 directions au hasard, l'excès minimal au-dessus de 1 vaut {fr(err, '{:.1e}')}).")
ligne("- Égalité exactement quand toutes les composantes non nulles ont la même taille : les 26 directions du cube de"
      " 27 points {−1, 0, 1}³ (partie XXII en 3D).")
CLS = collections.Counter(int(np.abs(v).sum()) for v in DIRS)
ligne(f"  - {CLS[1]} centres de faces : le carré, ombre 1 ; {CLS[2]} milieux d'arêtes : le rectangle, ombre √2 ;"
      f" {CLS[3]} sommets : l'hexagone, ombre √3. L'ombre vaut la distance du point au centre.")
ligne("- Les 2n chèvres de la partie XXII couvrent la clôture quand cos α_n < 1/√n, c'est-à-dire quand 1/cos α_n dépasse"
      " la plus grande ombre du cube de dimension n, √n.\n")
ligne("| n | α_n | 1/cos α_n = 1/x₀ | n + 4/3 − 112/(45n) | plus grande ombre √n | seuil arccos(1/√n) |")
ligne("|---:|---|---|---|---|---|")
CHEV = {}
for n in (2, 3, 4, 5, 8, 10, 24, 50, 100):
    r = ch.corde_moitie_mp(n)
    x0 = 1 - r * r / 2
    CHEV[n] = (float(x0), math.degrees(math.acos(float(x0))))
    ligne(f"| {n} | {fr(CHEV[n][1], '{:.2f}')}° | {fr(1 / float(x0), '{:.4f}')} | {fr(n + 4 / 3 - 112 / (45 * n), '{:.4f}')} |"
          f" {fr(math.sqrt(n), '{:.4f}')} | {fr(math.degrees(math.acos(1 / math.sqrt(n))), '{:.2f}')}° |")

# ===========================================================================
# 5. Archimède dans l'ombre du cube
# ===========================================================================
ligne("\n## 5. Archimède dans l'ombre du cube (III, IV – XXVI)\n")
ligne("Ombres (aires) du cube d'arête 1 et de sa sphère médiane (rayon √2/2, qui passe par les milieux des arêtes) :\n")
ligne("- plus petite ombre du cube : 1 (le carré) ; ombre moyenne : 3/2 (Cauchy : surface 6 ÷ 4) ;")
ligne(f"- ombre de la sphère médiane : π/2 = {fr(math.pi / 2, '{:.6f}')} (dans toutes les directions) ;")
ligne(f"- plus grande ombre du cube : √3 = {fr(R3, '{:.6f}')} (l'hexagone, dont le cercle inscrit est l'ombre de la sphère"
      " médiane, partie II).")
ligne("- Donc 3/2 < π/2 < √3, c'est-à-dire 3 < π < 2√3 : les premières bornes d'Archimède, celles de l'hexagone.")
ligne("  - À droite, c'est la même figure qu'Archimède : un cercle dans l'hexagone circonscrit.")
ligne("  - À gauche, c'est Cauchy : l'ombre moyenne vaut le quart de la surface, et la sphère médiane (2π) a plus de surface"
      " que le cube (6), parce que π > 3.")
ligne(f"- L'écart π/2 − 3/2 = (π − 3)/2 = {fr((math.pi - 3) / 2, '{:.6f}')} : la moitié des « retenues de l'hexagone »"
      " 1/8 + 9/640 + … de la partie IV.")

# ===========================================================================
# 6. Les deux bouts du ménisque (VI – XX – XXIV)
# ===========================================================================
ligne("\n## 6. Les deux chèvres au même endroit sont les deux bouts du ménisque (VI – XX – XXIV)\n")


def menisque(n):
    """Écart relatif entre la corde de la chèvre de dimension n et l'arête √(2n/(n + 1)) du simplexe,
    et la dimension équivalente N − n du simplexe de même corde (r² = 2N/(N + 1))."""
    n = mp.mpf(n)
    r = ch.corde_moitie_mp(n)
    s = mp.sqrt(2 * n / (n + 1))
    return float((r - s) / s), float(r * r / (2 - r * r) - n), float(r - s)


def sommet(f_, a_, b_):
    """Maximum d'une fonction en cloche par la section dorée."""
    a_, b_ = mp.mpf(a_), mp.mpf(b_)
    g_ = (mp.sqrt(5) - 1) / 2
    for _ in range(40):
        c_, d_ = b_ - g_ * (b_ - a_), a_ + g_ * (b_ - a_)
        if f_(c_) > f_(d_):
            b_ = d_
        else:
            a_ = c_
    return float((a_ + b_) / 2)


N_MAX_MEN = sommet(lambda n: menisque(n)[0], "1.8", "2.5")
N_MAX_ABS = sommet(lambda n: menisque(n)[2], "1.9", "2.7")
G_MAX = menisque(N_MAX_MEN)[0]
NS_MEN = np.unique(np.round(np.logspace(0, 3, 64), 4))
MEN = {float(n): menisque(n) for n in NS_MEN}
ligne(f"- L'écart relatif (corde − arête du simplexe) ÷ arête vaut 0 en dimension 1, culmine à"
      f" {fr(100 * G_MAX, '{:.4f}')} % en dimension {fr(N_MAX_MEN, '{:.3f}')} (dimension réelle), et tend vers 0 à"
      f" l'infini. L'écart absolu (corde − arête) culmine en dimension {fr(N_MAX_ABS, '{:.3f}')}, le « n ≈ 2,24 » de la"
      " partie VI.")
ligne(f"- La chèvre plane (n = 2) est à {fr(100 * menisque(2)[0], '{:.4f}')} % : à"
      f" {fr(100 * (1 - menisque(2)[0] / G_MAX), '{:.2f}')} % près du maximum. La chèvre infinie (corde √2) est à 0.")
ligne(f"- En unités de dimension, le même ménisque grandit au contraire de 0 à 1/3 : N − n = {fr(menisque(2)[1], '{:.4f}')}"
      f" en dimension 2, {fr(menisque(10)[1], '{:.4f}')} en 10, {fr(menisque(100)[1], '{:.4f}')} en 100,"
      f" {fr(menisque(1000)[1], '{:.4f}')} en 1 000 (partie XXIV : un tiers de dimension).")

# ===========================================================================
# 7. Les aiguilles d'argent (XIV – XVII)
# ===========================================================================
ligne("\n## 7. Les aiguilles d'argent (XIV – XVII)\n")
PHI, ARG = (1 + mp.sqrt(5)) / 2, 1 + mp.sqrt(2)
FIB, PELL = [0, 1], [0, 1]
for _ in range(14):
    FIB.append(FIB[-1] + FIB[-2])
    PELL.append(2 * PELL[-1] + PELL[-2])
for k in range(1, 13):
    assert FIB[k] * FIB[k + 2] - FIB[k + 1] ** 2 == (-1) ** (k + 1)
    assert PELL[k] * PELL[k + 2] - PELL[k + 1] ** 2 == (-1) ** (k + 1)
    assert abs((PELL[k + 1] - ARG * PELL[k]) - (1 - mp.sqrt(2)) ** k) < mp.mpf(10) ** -30
    assert abs((FIB[k + 1] - PHI * FIB[k]) - (-1 / PHI) ** k) < mp.mpf(10) ** -30
ligne("Deux familles d'aiguilles de la grille, (x, y) = (F_k, F_(k+1)) et (P_k, P_(k+1)) :\n")
ligne("| k | Fibonacci | angle | écart à la direction d'or | Pell | angle | écart à la direction d'argent |")
ligne("|---:|---|---|---|---|---|---|")
AIG = []
for k in range(1, 9):
    af = math.degrees(math.atan2(FIB[k + 1], FIB[k]))
    ap = math.degrees(math.atan2(PELL[k + 1], PELL[k]))
    ef = float((FIB[k + 1] - PHI * FIB[k]) / mp.sqrt(1 + PHI ** 2))
    ep = float((PELL[k + 1] - ARG * PELL[k]) / mp.sqrt(1 + ARG ** 2))
    AIG.append((k, af, ap, ef, ep))
    ligne(f"| {k} | ({FIB[k]}, {FIB[k + 1]}) | {fr(af, '{:.3f}')}° | {fr(ef, '{:+.5f}')} | ({PELL[k]}, {PELL[k + 1]}) |"
          f" {fr(ap, '{:.3f}')}° | {fr(ep, '{:+.6f}')} |")
ligne(f"\n- Direction d'or : arctan φ = {fr(math.degrees(math.atan(float(PHI))), '{:.3f}')}° ; direction d'argent :"
      f" arctan(1 + √2) = {fr(math.degrees(math.atan(float(ARG))), '{:.3f}')}° = 67,5° exactement.")
ligne("- Deux voisines ont toujours un déterminant ±1 (Cassini pour Fibonacci, son analogue pour Pell) : le triangle entre"
      " elles a l'aire ½, la demi-case minimale de la partie XIV. Les écarts changent de signe à chaque pas et se divisent"
      " par φ (or) ou par 1 + √2 (argent).")
T_ = [Fr(1)]
for _ in range(7):
    T_.append(2 - 1 / (2 * T_[-1]))
DSTAR = 1 + 1 / mp.sqrt(2)
ligne("- La récursion d'argent de la partie XVII, T(d) = 2 − 1/(2d), part de 1 et donne "
      + ", ".join(str(t) for t in T_[:7])
      + f"… : des rapports de nombres de Pell, vers le contact d = 1 + 1/√2 = {fr(float(DSTAR), '{:.6f}')}.")
ligne(f"- Ce contact, multiplié par √2, est la pente d'argent : (1 + 1/√2)·√2 = 1 + √2 = tan 67,5°. Et T'(d) ="
      f" 1/(2d²) = {fr(float(1 / (2 * DSTAR ** 2)), '{:.6f}')} = (√2 − 1)² au contact : la récursion avance de deux"
      " aiguilles de Pell par pas.")

# ===========================================================================
# 8. arccos(1/3) : la zone de confusion et le tétraèdre dans le cube (VI – XXVI)
# ===========================================================================
ligne("\n## 8. arccos(1/3) : la zone de confusion et le tétraèdre dans le cube (VI – XXVI)\n")
DIAG = [np.array(v, float) for v in ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))]
COS_D = sorted({round(float(abs(a @ b) / 3), 12) for a, b in itertools.combinations(DIAG, 2)})
ligne(f"- Les quatre grandes diagonales du cube font entre elles des angles de cosinus ±{fr(COS_D[0], '{:.6f}')} = ±1/3 :"
      " ce sont les axes du tétraèdre régulier inscrit (un sommet sur deux). D'où les écarts 70,53° et 109,47° entre les"
      " hexagones du mouvement complet (partie XXVI).")
ligne("- Dans la partie VI, la corde du triangle (2/√3) coupe la clôture à x = 1/3, donc sous l'angle arccos(1/3) : c'est"
      " l'angle qui entre dans l'aire exacte de la zone de confusion.")
ligne("- En dimension n, le plan de la lentille du simplexe est à 1/(n + 1) du centre (partie I) ; et −1/(n + 1) est le"
      " cosinus de l'angle au centre du simplexe régulier de dimension n + 1. La vraie chèvre a cos α_n = x₀, un peu"
      " moins : l'écart d'angle est le ménisque.\n")
ligne("| n | arccos(1/(n + 1)) | simplexe de dimension n + 1 (angle au centre) | α_n de la chèvre | écart (le ménisque) |")
ligne("|---:|---|---|---|---|")
for n in (2, 3, 4, 5, 10):
    a_s = math.degrees(math.acos(1 / (n + 1)))
    a_c = CHEV[n][1] if n in CHEV else math.degrees(math.acos(float(1 - ch.corde_moitie_mp(n) ** 2 / 2)))
    ligne(f"| {n} | {fr(a_s, '{:.3f}')}° | {fr(180 - a_s, '{:.3f}')}° | {fr(a_c, '{:.3f}')}° | {fr(a_c - a_s, '{:.3f}')}° |")

with open(os.path.join(ICI, "..", "resultats", "carte_connexions.md"), "w") as fh:
    fh.write("\n".join(md) + "\n")
print(f"calculs : {time.time() - T0:.1f} s")
T1 = time.time()


# ===========================================================================
# Figures
# ===========================================================================
def legende(ax, texte, y=-0.13, largeur=86):
    """Légende sous le panneau, recoupée en lignes de longueur fixe (pour ne pas déborder sur le voisin)."""
    texte = textwrap.fill(" ".join(texte.split("\n")), largeur)
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


BOITE = dict(boxstyle="round,pad=0.35", fc=F.SURF, ec=F.BASE)
PISTES = [(a, b) for (_, _, a, b) in PRED[:15] if (a, b) not in ETABLIS]

# --------------------------- ab1 : la carte ---------------------------
fig = plt.figure(figsize=(20, 16.5))
gs = fig.add_gridspec(2, 2, wspace=0.16, hspace=0.26)

# a) le graphe
ax = fig.add_subplot(gs[0, 0])
schema(ax, (-1.32, 1.32), (-1.3, 1.3))
POS = {n: (math.cos(math.pi / 2 - 2 * math.pi * (n - 1) / NMAX), math.sin(math.pi / 2 - 2 * math.pi * (n - 1) / NMAX))
       for n in range(1, NMAX + 1)}
WMAX = max(POIDS.values())
for (a, b), w in POIDS.items():
    (xa, ya), (xb, yb) = POS[a], POS[b]
    ax.plot([xa, xb], [ya, yb], color=F.MUTED, lw=0.3 + 2.0 * math.log1p(w) / math.log1p(WMAX), alpha=0.35, zorder=1)
for a, b in PISTES:
    (xa, ya), (xb, yb) = POS[a], POS[b]
    ax.plot([xa, xb], [ya, yb], color=F.ORANGE, lw=1.8, ls=(0, (4, 3)), zorder=2)
for a, b in ETABLIS:
    (xa, ya), (xb, yb) = POS[a], POS[b]
    ax.plot([xa, xb], [ya, yb], color=VERT, lw=2.6, zorder=3)
for n, (x, y) in POS.items():
    ax.plot([x], [y], "o", ms=5 + 0.55 * DEG[n], color=F.BLEU, mec=F.SURF, mew=1.5, zorder=4)
    ax.text(1.12 * x, 1.12 * y, romain(n), ha="center", va="center", fontsize=9.6, color=F.INK, fontweight="bold")
ax.plot([], [], color=F.MUTED, lw=1.5, alpha=0.6, label=f"{len(POIDS)} liens déjà posés (épaisseur : nombre de renvois)")
ax.plot([], [], color=VERT, lw=2.6, label=f"{len(ETABLIS)} liens établis dans cette partie")
ax.plot([], [], color=F.ORANGE, lw=1.8, ls=(0, (4, 3)), label="liens prédits, encore ouverts")
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.1), fontsize=9, ncol=1)
ax.set_title("a)  Les 26 parties et leurs renvois")

# b) la matrice
ax = fig.add_subplot(gs[0, 1])
M = np.zeros((NMAX, NMAX))
for (a, b), w in POIDS.items():
    M[a - 1, b - 1] = M[b - 1, a - 1] = w
ax.imshow(np.log1p(M), cmap=plt.matplotlib.colors.LinearSegmentedColormap.from_list("seq", F.SEQ), origin="upper")
for (a, b) in ETABLIS:
    for (i, j) in ((a - 1, b - 1), (b - 1, a - 1)):
        ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, ec=VERT, lw=2.2))
for (a, b) in PISTES:
    for (i, j) in ((a - 1, b - 1), (b - 1, a - 1)):
        ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, ec=F.ORANGE, lw=1.6, ls="--"))
ax.set_xticks(range(NMAX))
ax.set_yticks(range(NMAX))
ax.set_xticklabels([romain(n) for n in range(1, NMAX + 1)], fontsize=7.6, rotation=90)
ax.set_yticklabels([romain(n) for n in range(1, NMAX + 1)], fontsize=7.6)
ax.grid(False)
ax.set_title("b)  La matrice des renvois (foncé : souvent cités ensemble)")
legende(ax, "Cases vertes : les paires reliées dans cette partie. Cases orange : les paires que le graphe prédit et qui\n"
        "restent à explorer. La partie I (le README) porte l'index : sa ligne est pleine.", y=-0.08)

# c) les degrés
ax = fig.add_subplot(gs[1, 0])
xs = np.arange(1, NMAX + 1)
ax.bar(xs - 0.2, [DEG[n] for n in xs], width=0.4, color=F.BLEU, label="parties voisines")
ax.bar(xs + 0.2, [RECUS[n] / 4 for n in xs], width=0.4, color=F.ORANGE, label="renvois reçus ÷ 4")
ax.set_xticks(xs)
ax.set_xticklabels([romain(n) for n in xs], fontsize=8.4, rotation=90)
ax.set_ylabel("nombre")
for n, txt in ((1, "la chèvre :\n98 renvois"), (23, "la relecture"), (14, "l'aiguille\nsur la grille"),
               (6, "le ménisque\nde 0,35 %")):
    ax.text(n, max(DEG[n], RECUS[n] / 4) + 0.8, txt, ha="center", va="bottom", fontsize=8.4, color=F.INK2)
ax.set_ylim(0, 31)
ax.legend(loc="upper right", fontsize=9)
ax.set_title("c)  Les carrefours de la série")
legende(ax, "La chèvre de la partie I reste le sujet le plus cité. Les carrefours sont la relecture (XXIII), l'aiguille\n"
        "sur la grille (XIV) et le ménisque de 0,35 % (VI) : chacun relie des sujets qui ne se citaient pas.")

# d) les prédictions
ax = fig.add_subplot(gs[1, 1])
TOP = PRED[:15]
for i, (sc_, cn_, a, b) in enumerate(TOP):
    est = (a, b) in ETABLIS
    ax.barh(i, sc_, color=VERT if est else F.ORANGE, alpha=0.85 if est else 0.55)
    ax.text(0.05, i, f"{romain(a)} – {romain(b)}", va="center", fontsize=9.2, color=F.INK, fontweight="bold")
    ax.text(sc_ + 0.05, i, ETABLIS[(a, b)].split(" : ")[1] if est else "piste", va="center", fontsize=8.6,
            color=VERT if est else F.INK2)
ax.set_yticks([])
ax.invert_yaxis()
ax.set_xlim(0, 6.6)
ax.set_xlabel("indice d'Adamic–Adar (voisins communs, pondérés)")
ax.set_title("d)  Les 15 liens que le graphe prédit")
legende(ax, f"Vert : établis ici (et {sum(1 for p_ in ETABLIS if RANG[p_] > 15)} autres plus bas dans la liste)."
        " Orange : des pistes. Le graphe ne dit pas ce\n"
        "qui relie deux chapitres ; il dit seulement qu'ils fréquentent les mêmes. Le lien, il faut le calculer.")
F.sauver(fig, "ab1_carte.png")
print(f"ab1 : {time.time() - T1:.1f} s")

# --------------------------- ab2 : les cercles arctiques ---------------------------
fig = plt.figure(figsize=(21, 14.4))
gs = fig.add_gridspec(2, 3, wspace=0.16, hspace=0.32)
COUL_D = [F.BLEU, F.ORANGE, VERT, F.JAUNE]

# a) le losange en dominos
ax = fig.add_subplot(gs[0, 0])
schema(ax, (-N_AZ - 1, N_AZ + 1), (-N_AZ - 1, N_AZ + 1))
rects = {t: [] for t in range(4)}
for x, y, hor, t in DOM:
    if hor:
        rects[t].append([(x - 1, y - 0.5), (x + 1, y - 0.5), (x + 1, y + 0.5), (x - 1, y + 0.5)])
    else:
        rects[t].append([(x - 0.5, y - 1), (x + 0.5, y - 1), (x + 0.5, y + 1), (x - 0.5, y + 1)])
for t in range(4):
    ax.add_collection(PolyCollection(rects[t], facecolors=COUL_D[t], edgecolors=F.SURF, linewidths=0.25))
ax.add_patch(Circle((0, 0), N_AZ / R2, fill=False, ec=F.INK, lw=1.8))
ax.set_title(f"a)  Le losange en dominos : {len(DOM)} pièces au hasard")
legende(ax, f"Diamant aztèque d'ordre {N_AZ}, pavé au hasard (dynamique de Glauber, {PAS_AZ} balayages). Hors du cercle\n"
        "inscrit, chaque coin est gelé : une seule sorte de domino. Dedans, les quatre se mélangent. Des carrés\n"
        "(les pixels de la partie XVIII, deux par domino) dessinent un rond.", y=-0.02, largeur=78)

# b) l'hexagone en losanges
ax = fig.add_subplot(gs[0, 1])
schema(ax, (-N_HX * 1.02, N_HX * 1.02), (-N_HX * 1.04, N_HX * 1.04))
for t, col in zip(range(3), (F.BLEU, F.ORANGE, F.JAUNE)):
    ax.add_collection(PolyCollection(LOS[t], facecolors=col, edgecolors=F.SURF, linewidths=0.2))
ax.add_patch(Circle(CENTRE_HX, R_IN_HX, fill=False, ec=F.INK, lw=1.8))
ax.set_title("b)  L'hexagone en losanges : des cubes au hasard")
legende(ax, f"Cubes empilés au hasard dans une boîte {N_HX} × {N_HX} × {N_HX}, vus le long de la grande diagonale : chaque\n"
        "losange est une face de cube (parties II et XXVI). Le désordre s'arrête au cercle inscrit, qui est l'ombre\n"
        "de la sphère médiane du cube (partie II).", y=-0.02, largeur=78)

# c) les profils
ax = fig.add_subplot(gs[0, 2])
for bords, prof, col, nom, base in ((BORDS, PROF_AZ, F.ORANGE, "losange (dominos)", 0.25),
                                     (BORDS_HX, PROF_HX, F.BLEU, "hexagone (losanges)", 1 / 3)):
    xs_ = [b_[0] for b_ in bords] + [bords[-1][1]]
    ax.stairs(prof, xs_, color=col, lw=2.4, label=nom, baseline=None)
    ax.axhline(base, color=col, lw=1, ls=":")
ax.axvline(1, color=F.INK, lw=1.4, ls="--")
ax.text(1.02, 0.55, "le cercle\ninscrit", fontsize=9.2, color=F.INK)
ax.text(0.05, 0.27, "¼ : quatre sortes à égalité", fontsize=8.6, color=F.ORANGE)
ax.text(0.05, 0.355, "⅓ : trois sortes à égalité", fontsize=8.6, color=F.BLEU)
ax.set_xlim(0, 1.45)
ax.set_ylim(0.2, 1.06)
ax.set_xlabel("distance au centre ÷ rayon du cercle inscrit")
ax.set_ylabel("part de la sorte majoritaire, par secteur")
ax.legend(loc="center left", fontsize=9)
ax.set_title("c)  Mélangé dedans, gelé dehors")
legende(ax, "Dans chaque secteur (un par coin), on compte la sorte de pièce la plus fréquente. Dedans : un mélange\n"
        "(proche de ¼ ou ⅓, avec le bruit d'un seul tirage). Dehors : 100 %, une seule sorte. La marche est au\n"
        "cercle : c'est le théorème du cercle arctique (Jockusch–Propp–Shor ; Cohn–Larsen–Propp).")

# d) les plus petits cas
ax = fig.add_subplot(gs[1, 0])
schema(ax, (-0.4, 9.6), (-2.9, 2.2))
for dx_, hor in ((0.0, True), (2.6, False)):
    if hor:
        for y0 in (0, 1):
            ax.add_patch(Rectangle((dx_, y0 - 1), 2, 1, fc=COUL_D[y0], ec=F.SURF, lw=2))
    else:
        for x0 in (0, 1):
            ax.add_patch(Rectangle((dx_ + x0, -1), 1, 2, fc=COUL_D[2 + x0], ec=F.SURF, lw=2))
ax.text(2.3, -1.75, "losange d'ordre 1 :\n2 pavages", ha="center", va="top", fontsize=9.4, color=F.INK2)
h_, w_ = np.array([0, 0, 1.0]), None
u_ = np.array([1.0, 1, 1]) / R3
e1 = np.array([1.0, -1, 0]) / R2
e2 = np.cross(u_, e1)


def face_hex(i, s_, dx_):
    j, k = [m for m in range(3) if m != i]
    pts = []
    for a_, b_ in ((0, 0), (1, 0), (1, 1), (0, 1)):
        p_ = np.zeros(3)
        p_[i], p_[j], p_[k] = s_, a_, b_
        pts.append([p_ @ e1 * 1.25 + dx_, p_ @ e2 * 1.25 - 0.62])
    return np.array(pts)


for dx_, s_, cols_ in ((6.1, 1, (F.BLEU, F.ORANGE, F.JAUNE)), (8.55, 0, (F.BLEU, F.ORANGE, F.JAUNE))):
    for i in range(3):
        ax.add_patch(Polygon(face_hex(i, s_, dx_ - (0.0 if s_ else 0.0)), closed=True, fc=cols_[i], ec=F.SURF, lw=2))
ax.text(7.3, -1.75, "hexagone de côté 1 :\n2 pavages (Necker)", ha="center", va="top", fontsize=9.4, color=F.INK2)
ax.set_title("d)  Les plus petits cas : 2 et 2")
legende(ax, "Le losange d'ordre 1 est un carré 2 × 2 : deux dominos couchés ou deux debout. L'hexagone de côté 1\n"
        "est l'ombre d'un seul cube : la boîte vide ou pleine, les deux lectures du cube de Necker (partie XXVI).",
        y=-0.02)

# e) les comptes
ax = fig.add_subplot(gs[1, 1])
ns_ = np.arange(1, 9)
ax.plot(ns_, ns_ * (ns_ + 1) / 2, "o-", color=F.ORANGE, ms=7, lw=1.6, label="losange : 2^(n(n+1)/2) pavages")
ax.plot(ns_, [math.log2(float(macmahon(n, n, n))) for n in ns_], "s-", color=F.BLEU, ms=6, lw=1.6,
        label="hexagone : MacMahon")
for n, txt in ((4, "2¹⁰ = 1 024 : le kibi"), (6, "2²¹ = 2 097 152")):
    ax.annotate(txt, (n, n * (n + 1) / 2), (n + 0.35, n * (n + 1) / 2 - 7), fontsize=9, color=F.ORANGE,
                arrowprops=dict(arrowstyle="-", color=F.ORANGE, lw=0.8), ha="left")
ax.set_xlabel("ordre n (losange) ou côté a (hexagone)")
ax.set_ylabel("log₂ du nombre de pavages (en crans)")
ax.legend(loc="upper left", fontsize=9)
ax.set_title("e)  Combien de pavages : des crans")
legende(ax, "Le losange compte en crans : l'ordre n multiplie le nombre de pavages par 2ⁿ (Elkies, Kuperberg,\n"
        "Larsen, Propp 1992). Vérifié exactement jusqu'à l'ordre 6, et les partitions planes jusqu'au côté 4.")

# f) les deux cercles
ax = fig.add_subplot(gs[1, 2])
schema(ax, (-1.25, 3.85), (-1.45, 1.3))
ax.add_patch(Polygon([(1, 0), (0, 1), (-1, 0), (0, -1)], closed=True, fc=F.ORANGE, alpha=0.18, ec=F.ORANGE, lw=1.6))
ax.add_patch(Circle((0, 0), 1, fill=False, ec=F.MUTED, lw=1.2, ls="--"))
ax.add_patch(Circle((0, 0), 1 / R2, fc=F.ORANGE, alpha=0.25, ec=F.INK, lw=1.6))
HEXP = np.array([[math.cos(math.pi / 6 + k * math.pi / 3), math.sin(math.pi / 6 + k * math.pi / 3)] for k in range(6)])
HEXP = HEXP * math.sqrt(2 / 3) + [2.6, 0]
ax.add_patch(Polygon(HEXP, closed=True, fc=F.BLEU, alpha=0.15, ec=F.BLEU, lw=1.6))
ax.add_patch(Circle((2.6, 0), R2 / 2 * math.sqrt(2 / 3) / (R2 / 2) * (R3 / 2), fc=F.BLEU, alpha=0.25, ec=F.INK, lw=1.6))
ax.text(0, -1.12, f"losange : le cercle inscrit\nfait π/4 = {fr(math.pi / 4, '{:.3f}')} du losange\net la moitié du disque"
        " circonscrit\n(le disque de demi-aire, XVII)", ha="center", va="top", fontsize=8.8, color=F.INK)
ax.text(2.6, -1.12, f"hexagone : le cercle inscrit\nfait π/(2√3) = {fr(math.pi / (2 * R3), '{:.3f}')}\n(l'empilement"
        " hexagonal, XV)\nombre de la sphère médiane (II)", ha="center", va="top", fontsize=8.8, color=F.INK)
ax.set_title("f)  Les deux cercles arctiques")
F.sauver(fig, "ab2_cercles_arctiques.png")
print(f"ab2 : {time.time() - T1:.1f} s")

# --------------------------- ab3 : les autres liens ---------------------------
fig = plt.figure(figsize=(21, 14.4))
gs = fig.add_gridspec(2, 3, wspace=0.2, hspace=0.38)

# a) l'échelle des taux de change
ax = fig.add_subplot(gs[0, 0])
kk = np.linspace(1, 60, 240)
COUL_E = [ROUGE, F.ORANGE, F.JAUNE, VIOLET, F.BLEU, VERT]
NOMS_E = ["équateur : ε⁻²", "coquille : ε⁻¹", "plan : ε⁻¹", "ménisque : ε^(−1/2)", "série tronquée : log",
          "Kakeya, 1/aire : log"]
for (nom, loi, f_), col, nm in zip(ECHELLE, COUL_E, NOMS_E):
    ax.semilogy(kk, [math.log10(f_(k)) for k in kk], color=col, lw=2.2 if "log" in nm else 1.8,
                ls="--" if "coquille" in nm else "-", label=nm)
ax.axvline(50, color=F.INK2, lw=1, ls=":")
for (nom, loi, f_), col in zip(ECHELLE, COUL_E):
    if "coquille" in nom:
        continue
    v = f_(50)
    ax.text(51, math.log10(v), sci(v) if v > 1e6 else fr(v, '{:.0f}'), va="center", fontsize=8.6, color=col)
ax.set_yticks([1, 2, 5, 10, 25, 50, 100])
ax.set_yticklabels(["1", "2", "5", "10", "25", "50", "100"])
ax.set_ylim(0.6, 160)
ax.set_xlim(0, 62)
ax.set_xlabel("chiffres du grain : k (ε = 10⁻ᵏ)")
ax.set_ylabel("chiffres de la dimension nécessaire (log₁₀ n)")
ax.legend(loc="upper left", fontsize=8.4, ncol=2)
ax.set_title("a)  L'échelle des taux de change du grain")
legende(ax, "Les pentes 2, 1, ½ (parties I et XXIII) se divisent par deux à chaque marche : 100, 50, 25 chiffres à"
        " 10⁻⁵⁰. La série de la chèvre (XXV) et Kakeya (XXVI) sont la marche 0, le logarithme : 316 dimensions et"
        " 1/aire = 74. La série gagne un cran de √2 par dimension : 6,64 dimensions par décade, autant que de crans"
        " dans une décade (XXI).")

# b) les 26 directions et le tétraèdre
ax = fig.add_subplot(gs[0, 1])
schema(ax, (-1.85, 1.85), (-2.25, 2.55))
U3 = np.array([1.0, 0.82, 0.55])
U3 /= np.linalg.norm(U3)
B1 = np.cross([0, 0, 1.0], U3)
B1 /= np.linalg.norm(B1)
B2 = np.cross(U3, B1)


def pr(p_):
    return np.array([np.dot(p_, B1), np.dot(p_, B2)])


for v1 in itertools.product((-1, 1), repeat=3):
    for i in range(3):
        if v1[i] == -1:
            w1 = list(v1)
            w1[i] = 1
            P1, P2 = pr(np.array(v1, float)), pr(np.array(w1, float))
            ax.plot([P1[0], P2[0]], [P1[1], P2[1]], color=F.BASE, lw=1.2, zorder=1)
TET = [np.array(v, float) for v in ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))]
for p_, q_ in itertools.combinations(TET, 2):
    P1, P2 = pr(p_), pr(q_)
    ax.plot([P1[0], P2[0]], [P1[1], P2[1]], color=VERT, lw=1.3, alpha=0.75, zorder=2)
for v in DIRS:
    k_ = int(np.abs(v).sum())
    P = pr(v.astype(float))
    ax.plot([P[0]], [P[1]], {1: "s", 2: "D", 3: "h"}[k_], ms={1: 9, 2: 8, 3: 11}[k_],
            color={1: F.ORANGE, 2: VIOLET, 3: ROUGE}[k_], mec=F.SURF, mew=1.2, zorder=4)
F.point(ax, 0, 0, F.INK, 7)
for k_, txt, col in ((1, "6 centres de faces : carré, ombre 1", F.ORANGE), (2, "12 milieux d'arêtes : rectangle, √2", VIOLET),
                     (3, "8 sommets : hexagone, √3", ROUGE)):
    ax.text(-1.8, 2.62 - 0.22 * k_, txt, fontsize=9, color=col, va="center")
ax.text(-1.8, -1.95, "vert : le tétraèdre inscrit ; ses axes sont les grandes\ndiagonales, à arccos(±1/3) l'une de"
        " l'autre", fontsize=8.6, color=VERT, va="center")
ax.set_title("b)  Les 26 directions du cube de 27 points")
legende(ax, "ombre × cos(angle au piquet le plus proche) = ‖u‖₁·‖u‖∞ ≥ 1, avec égalité exactement dans ces 26\n"
        "directions (le carré de neuf points de la partie XXII, en 3D). L'ombre y vaut la distance au centre :\n"
        "1, √2, √3. Les 4 grandes diagonales sont les axes du tétraèdre : l'angle arccos(1/3) de la partie VI.")

# c) les chèvres et le cube
ax = fig.add_subplot(gs[0, 2])
ns_ = sorted(CHEV)
ax.loglog(ns_, [1 / CHEV[n][0] for n in ns_], "o", color=F.BLEU, ms=7, label="chèvre : 1/cos α_n = 1/x₀")
nn = np.logspace(math.log10(2), 2, 200)
ax.loglog(nn, nn + 4 / 3 - 112 / (45 * nn), color=F.BLEU, lw=1.2, ls="--", label="n + 4/3 − 112/(45n) (partie XXIV)")
ax.loglog(nn, np.sqrt(nn), color=ROUGE, lw=2, label="plus grande ombre du cube : √n (hexagone en 3D)")
ax.fill_between(nn, np.sqrt(nn), nn + 4 / 3, color=VERT, alpha=0.12)
ax.text(6, 3.6, "les 2n chèvres\ncouvrent la clôture", fontsize=9.2, color=VERT)
ax.set_xlabel("dimension n")
ax.set_ylabel("1/cosinus")
ax.legend(loc="upper left", fontsize=8.6)
ax.set_title("c)  Les 2n chèvres et la plus grande ombre du cube")
legende(ax, "Les chèvres aux ±e_i (partie XXII) couvrent la clôture tant que 1/cos α_n dépasse √n, la plus grande\n"
        "ombre du cube : c'est le même seuil, lu par l'inégalité ‖u‖₁·‖u‖∞ ≥ 1. La chèvre a une marge d'un\n"
        "facteur ≈ √n : 1/x₀ = n + 4/3 − … (XXIV) contre √n.")

# d) Archimède dans l'ombre du cube
ax = fig.add_subplot(gs[1, 0])
schema(ax, (0.92, 1.82), (-0.95, 1.05), egal=False)
ax.plot([0.95, 1.79], [0, 0], color=F.INK, lw=1.4)
for v, txt, col, y_t in ((1, "1\nle carré", F.ORANGE, -0.12), (1.5, "3/2\nombre moyenne\ndu cube", F.INK, 0.12),
                         (math.pi / 2, "π/2\nla sphère\nmédiane", F.BLEU, -0.12), (R3, "√3\nl'hexagone", ROUGE, 0.12)):
    ax.plot([v, v], [-0.06, 0.06], color=col, lw=2.6)
    ax.text(v, y_t, txt, ha="center", va="bottom" if y_t > 0 else "top", fontsize=9.2, color=col)
for (x0_, x1_), y_, txt in (((1.5, math.pi / 2), 0.72, "π > 3 (Cauchy)"), ((math.pi / 2, R3), 0.92, "π < 2√3 (Archimède)")):
    ax.plot([x0_, x0_], [0.08, y_], color=F.MUTED, lw=0.8, ls=":")
    ax.plot([x1_, x1_], [0.08, y_], color=F.MUTED, lw=0.8, ls=":")
    ax.annotate("", (x1_, y_), (x0_, y_), arrowprops=dict(arrowstyle="<->", color=F.INK2, lw=1.1))
    ax.text(x0_ - 0.012, y_, txt, va="center", ha="right", fontsize=9.6, color=F.INK2)
ax.set_title("d)  Archimède dans l'ombre du cube")
legende(ax, "Les ombres du cube d'arête 1 vont de 1 à √3 ; sa moyenne vaut 3/2 et la sphère médiane fait π/2 dans"
        " toutes les directions. 3/2 < π/2 < √3, c'est 3 < π < 2√3 : les bornes d'Archimède par l'hexagone (parties"
        " III et IV). À droite, c'est sa figure même, le cercle dans l'hexagone ; à gauche, c'est Cauchy : la sphère"
        " médiane a plus de surface (2π) que le cube (6).", y=-0.02)

# e) les deux bouts du ménisque
ax = fig.add_subplot(gs[1, 1])
nm_ = np.array(sorted(MEN))
ax.semilogx(nm_, [100 * MEN[n][0] for n in nm_], color=F.BLEU, lw=2.2, label="écart relatif de la corde (%)")
ax.plot([N_MAX_MEN], [100 * G_MAX], "*", color=ROUGE, ms=13)
ax.text(N_MAX_MEN * 1.25, 100 * G_MAX + 0.008, f"sommet : dimension {fr(N_MAX_MEN, '{:.2f}')}", fontsize=9,
        color=ROUGE)
F.point(ax, 2, 100 * menisque(2)[0], F.ORANGE, 8)
ax.annotate("la chèvre plane (n = 2,\npartie XX)", (2, 100 * menisque(2)[0]), (1.04, 0.395), fontsize=9,
            color=F.ORANGE, arrowprops=dict(arrowstyle="-", color=F.ORANGE, lw=0.8))
ax.text(300, 0.03, "la chèvre infinie :\nécart 0 (√2)", ha="center", fontsize=9, color=F.INK2)
ax.set_ylim(0, 0.43)
ax.set_xlabel("dimension n (réelle)")
ax.set_ylabel("(corde − arête du simplexe) ÷ arête, en %", color=F.BLEU)
ax2 = ax.twinx()
ax2.semilogx(nm_, [MEN[n][1] for n in nm_], color=VIOLET, lw=1.8, ls="--")
ax2.axhline(1 / 3, color=VIOLET, lw=0.8, ls=":")
ax2.set_ylim(0, 0.43)
ax2.set_ylabel("N − n : le ménisque en dimensions", color=VIOLET)
ax2.text(400, 0.345, "⅓", fontsize=11, color=VIOLET)
ax2.grid(False)
ax.set_title("e)  Les deux chèvres sont les deux bouts du ménisque")
legende(ax, "En longueur (bleu), le ménisque de la partie VI culmine près de la dimension 2 et s'éteint à l'infini :\n"
        "les deux chèvres au même endroit (partie XX) sont le sommet et la fin de la bosse. En dimensions (violet),\n"
        "le même ménisque monte vers ⅓ : le tiers de dimension de la partie XXIV.")

# f) les aiguilles d'argent
ax = fig.add_subplot(gs[1, 2])
schema(ax, (-0.6, 13.5), (-0.6, 13.6))
for gx in range(0, 14):
    ax.plot([gx, gx], [0, 13.2], color=F.GRID, lw=0.6, zorder=0)
for gy in range(0, 14):
    ax.plot([0, 13.2], [gy, gy], color=F.GRID, lw=0.6, zorder=0)
for pente, col, nom in ((float(PHI), F.ORANGE, "direction d'or (58,28°)"), (float(ARG), F.BLEU, "direction d'argent (67,5°)")):
    xe = 13.2 / max(pente, 1)
    ax.plot([0, xe], [0, xe * pente], color=col, lw=1.2, ls="--")
FV = [(FIB[k], FIB[k + 1]) for k in range(1, 7)]
PV = [(PELL[k], PELL[k + 1]) for k in range(1, 4)]
for vs_, col, cote in ((FV, F.ORANGE, 1), (PV, F.BLEU, -1)):
    for (x1, y1), (x2, y2) in zip(vs_[:-1], vs_[1:]):
        ax.add_patch(Polygon([(0, 0), (x1, y1), (x2, y2)], closed=True, fc=col, alpha=0.12, ec="none"))
    for x, y in vs_:
        ax.annotate("", (x, y), (0, 0), arrowprops=dict(arrowstyle="-|>", color=col, lw=1.6, mutation_scale=10))
        if (x, y) == (1, 2) and cote < 0:
            continue
        ax.text(x + 0.3 * cote, y, f"({x}, {y})", fontsize=8.4, color=col, va="center", ha="left" if cote > 0 else "right")
ax.text(6.5, 1.0, "or : Fibonacci (partie XIV)\nargent : Pell (partie XVII)\nchaque triangle : aire ½",
        fontsize=9, color=F.INK2, bbox=BOITE)
ax.set_title("f)  Les aiguilles d'argent")
legende(ax, "Les aiguilles de Pell (1, 2), (2, 5), (5, 12)… visent la direction 67,5° en coûtant une demi-case par pas,\n"
        "comme celles de Fibonacci visent l'angle d'or. La récursion d'argent de la partie XVII en est le reflet : ses\n"
        "rapports sont des nombres de Pell, et son contact 1 + 1/√2, fois √2, donne la pente 1 + √2 = tan 67,5°.",
        y=-0.02)
F.sauver(fig, "ab3_liens_predits.png")
print(f"figures : {time.time() - T1:.1f} s ; total : {time.time() - T0:.1f} s")
