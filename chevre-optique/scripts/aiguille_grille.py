"""
Partie XIV : l'aiguille sur une grille.

    python3 scripts/aiguille_grille.py        # ≈ 20 s

Écrit resultats/aiguille_grille.md, figures/n1_aiguille_grille.png et figures/n2_perron_grille.png.

L'aiguille a ses deux bouts sur une grille de points espacés de 1 (Z², ou Z^d en dimension d).
1. Les directions permises : les points de la grille sur le cercle de rayon L (triangles pythagoriciens).
2. S'inverser : un bout à l'origine (demi-cercle, demi-disque) ou le milieu à l'origine (cercle, disque).
   Les points balayés grandissent comme L², et comme V(d)·L^d en dimension d.
3. Les convergentes : les aiguilles de Fibonacci, une case entre deux voisines, la somme qui donne la suivante.
4. Le pavage de Farey : les directions de la grille dans le disque de Poincaré ; leurs aires suivent Ptolémée.
5. Kakeya sur une grille finie (le plan F_q²) : la moitié du plan.
6. L'arbre de Perron sur une grille n × n : l'aire ne descend que comme 1/log n.
"""

import itertools
import logging
import math
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Rectangle, Wedge
from matplotlib.path import Path
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix
from scipy.special import gamma

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
PHI = (1 + 5 ** 0.5) / 2
ROUGE = "#d0342c"
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


FIB = [0, 1]
while len(FIB) < 30:
    FIB.append(FIB[-1] + FIB[-2])


# ---------------------------------------------------------------------------
# 1. Les directions permises : les points de la grille sur le cercle de rayon L
# ---------------------------------------------------------------------------
def points_cercle(L):
    """Points (a, b) de Z² avec a² + b² = L²."""
    pts = []
    for a in range(-L, L + 1):
        b = math.isqrt(L * L - a * a)
        if b * b == L * L - a * a:
            pts += [(a, b)] + ([(a, -b)] if b else [])
    return pts


def r2_formule(L):
    """Nombre de points de Z² sur le cercle de rayon L : 4·∏(2e + 1) sur les premiers p ≡ 1 (mod 4) de L (Jacobi)."""
    n, f, p = L, 4, 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if p % 4 == 1:
            f *= 2 * e + 1
        p += 1
    return f * 3 if n > 1 and n % 4 == 1 else f


def angles_quart(L):
    return sorted({round(math.degrees(math.atan2(b, a)) % 90, 9) for a, b in points_cercle(L)})


def ecarts(ang):
    g = np.diff(ang + [ang[0] + 90])
    return sorted({round(v, 6) for v in g})


ligne("## 1. Les directions permises sur la grille\n")
ligne("Une aiguille de longueur L, ses deux bouts sur des points de la grille : ses directions sont les points de la grille"
      " sur le cercle de rayon L.\n")
ligne("| L | points sur le cercle (comptés) | formule de Jacobi | directions par quart de tour | plus grand trou |")
ligne("|---:|---:|---:|---:|---|")
for L in (1, 2, 3, 5, 10, 13, 25, 65, 125, 325, 625, 1105, 5525):
    P = points_cercle(L)
    a = angles_quart(L)
    ligne(f"| {L} | {len(P)} | {r2_formule(L)} | {len(a)} | {fr(max(ecarts(a)), '{:.2f}')}° |")
TH0 = math.degrees(math.atan2(4, 3))
ligne(f"\nL'angle du triangle 3-4-5 : arctan(4/3) = 2·arctan(1/2) = {fr(TH0, '{:.6f}')}°.")
ligne("Pour L = 5^k, les directions sont les m × 53,13° (m de −k à k), à un quart de tour près :\n")
ligne("| L | directions par quart de tour | longueurs des trous (degrés) |")
ligne("|---:|---:|---|")
TROUS5 = {}
for k in range(1, 7):
    a = angles_quart(5 ** k)
    pred = sorted({round((m * TH0) % 90, 9) for m in range(-k, k + 1)})
    assert np.allclose(a, pred), "les directions ne sont pas les multiples de 53,13°"
    TROUS5[k] = (a, ecarts(a))
    ligne(f"| 5^{k} = {5 ** k} | {len(a)} | {' ; '.join(fr(v, '{:.3f}') for v in TROUS5[k][1])} |")
ligne("\nJamais plus de trois longueurs de trous : c'est le théorème des trois distances (partie XI), avec 53,13° à la place"
      " de l'angle d'or. Chaque trou est la différence de deux plus grands : 90 − 53,13 = 36,87 ; 53,13 − 36,87 = 16,26 ;"
      " 36,87 − 16,26 = 20,61 ; 20,61 − 16,26 = 4,35…")
ligne("Théorème de Niven : si un angle est un nombre rationnel de degrés et que son cosinus et son sinus sont rationnels,"
      " c'est un multiple de 90°. Toutes les autres rotations de la grille (53,13°, 36,87°, …) sont irrationnelles en degrés.")

# ---------------------------------------------------------------------------
# 2. S'inverser : demi-cercle ou disque, et les points balayés
# ---------------------------------------------------------------------------
LF = 10  # l'aiguille de la figure
DEMI = sorted([p for p in points_cercle(LF) if p[1] > 0 or (p[1] == 0)], key=lambda p: math.atan2(p[1], p[0]))
PAS = np.diff([math.degrees(math.atan2(y, x)) for x, y in DEMI])
DETS = [DEMI[i][0] * DEMI[i + 1][1] - DEMI[i][1] * DEMI[i + 1][0] for i in range(len(DEMI) - 1)]
ligne("\n## 2. S'inverser : demi-cercle ou disque\n")
ligne(f"Aiguille de longueur {LF}, un bout à l'origine : l'autre bout passe par {len(DEMI)} points de la grille, "
      + " → ".join(fr(x, "({:d}, ") + fr(y, "{:d})") for x, y in DEMI) + ".")
ligne("Pas : " + " ; ".join(fr(v, '{:.2f}') + "°" for v in PAS) + ".")
ligne(f"Entre deux positions, le triangle balayé a l'aire |det|/2 : " + ", ".join(str(d) for d in DETS)
      + f" (en demi-cases) ; total {sum(DETS) / 2:g}, contre π·L²/2 = {fr(math.pi * LF * LF / 2, '{:.2f}')} pour le demi-disque.")
ligne(f"Le milieu à l'origine : les bouts sont en ±w avec |w| = {LF // 2} ; {len(points_cercle(LF // 2)) // 2} positions de"
      " l'aiguille, les deux bouts font le tour complet et l'aiguille balaie le disque de rayon L/2.")
ligne("Sur la grille, un pas de rotation autour d'un bout fixe balaie au moins une demi-case : le triangle (0, v, w) a"
      " l'aire |det(v, w)|/2, et un déterminant entier non nul vaut au moins 1.\n")


def deltoide(L, n=6000):
    """Deltoïde dont la tangente intérieure a la longueur L (aire πL²/8), centré à l'origine."""
    r = L / 4
    t = np.linspace(0, 2 * np.pi, n)
    return np.c_[2 * r * np.cos(t) + r * np.cos(2 * t), 2 * r * np.sin(t) - r * np.sin(2 * t)]


COMPTES = {}
ligne("Points de la grille balayés, comparés à l'aire :\n")
ligne("| L | demi-disque (un bout fixe) | πL²/2 | disque (milieu fixe) | πL²/4 | deltoïde (Kakeya) | πL²/8 |")
ligne("|---:|---:|---|---:|---|---:|---|")
for L in (4, 8, 16, 32, 64, 128, 256):
    xs = np.arange(-L, L + 1)
    X, Y = np.meshgrid(xs, xs)
    R2 = X * X + Y * Y
    c = (((R2 <= L * L) & (Y >= 0)).sum(), (4 * R2 <= L * L).sum(),
         Path(deltoide(L)).contains_points(np.c_[X.ravel(), Y.ravel()]).sum())
    COMPTES[L] = c
    ligne(f"| {L} | {c[0]} | {fr(math.pi * L * L / 2, '{:.1f}')} | {c[1]} | {fr(math.pi * L * L / 4, '{:.1f}')} | {c[2]} |"
          f" {fr(math.pi * L * L / 8, '{:.1f}')} |")
ligne("\nLes trois comptes grandissent comme L² (le problème du cercle de Gauss : l'écart à l'aire est de l'ordre du"
      " périmètre, ou moins). Les rapports demi-disque : disque : deltoïde tendent vers 4 : 2 : 1.\n")
VB = {}
ligne("En dimension d, points de la grille dans la boule de rayon 12, comparés à V(d)·12^d (V(d) : le volume de la boule"
      " unité, celui de la chèvre en dimension d) :\n")
ligne("| d | points | V(d)·12^d | rapport |")
ligne("|---:|---:|---|---|")
for d in range(1, 6):
    xs = np.arange(-12, 13)
    S = sum(g * g for g in np.meshgrid(*([xs] * d), indexing="ij"))
    c = int((S <= 144).sum())
    V = math.pi ** (d / 2) / gamma(d / 2 + 1) * 12 ** d
    VB[d] = c / V
    ligne(f"| {d} | {c} | {fr(V, '{:.1f}')} | {fr(c / V, '{:.4f}')} |")

# ---------------------------------------------------------------------------
# 3. Les convergentes : les aiguilles de Fibonacci
# ---------------------------------------------------------------------------
ligne("\n## 3. Les aiguilles de Fibonacci : une case entre deux voisines\n")
ligne("La direction d'or (1, φ) n'a aucun point de la grille. Les aiguilles (F(k), F(k+1)) l'approchent :\n")
ligne("| k | aiguille | écart vertical à la droite y = φx | (−1/φ)^k | déterminant avec la suivante | angle × longueur² |")
ligne("|---:|---|---|---|---:|---|")
for k in range(1, 13):
    v, w = (FIB[k], FIB[k + 1]), (FIB[k + 1], FIB[k + 2])
    e = FIB[k + 1] - PHI * FIB[k]
    det = v[0] * w[1] - v[1] * w[0]
    ang = abs(math.atan2(v[1], v[0]) - math.atan2(PHI, 1))
    ligne(f"| {k} | ({v[0]}, {v[1]}) | {fr(e, '{:+.6f}')} | {fr((-1 / PHI) ** k, '{:+.6f}')} | {det:+d} |"
          f" {fr(ang * (v[0] ** 2 + v[1] ** 2), '{:.5f}')} |".replace(f"| {det:+d} |", f"| {fr(det, '{:+d}')} |"))
ligne(f"\nL'écart vaut exactement (−1/φ)^k : les aiguilles passent d'un côté à l'autre de la direction d'or, chaque fois"
      f" φ fois plus près. Angle × longueur² → 1/√5 = {fr(1 / 5 ** 0.5, '{:.5f}')} : la constante de Hurwitz (partie IX).")
ligne("Le déterminant de deux voisines vaut ±1 (identité de Cassini) : elles enferment exactement une case, et le triangle"
      " entre elles a l'aire 1/2 sans aucun point de la grille dedans (théorème de Pick).")
ligne("La suivante est la somme des deux précédentes : (F(k+2), F(k+3)) = (F(k), F(k+1)) + (F(k+1), F(k+2)).")
ligne("\nLa même somme dans le spectre (partie XIII) : le nœud miroir de F(k−2) et F(k−1) est au centre fantôme de leur"
      " somme F(k), en x/a = R/(2F(k)), à la fréquence F(k−2)/F(k).\n")
ligne("| nœud | x/a (R = 60) | fréquence | ce qu'est la somme |")
ligne("|---|---|---|---|")
for k in (8, 9, 10):
    u, v = FIB[k - 2], FIB[k - 1]
    xa = 60 / (2 * FIB[k])
    ligne(f"| {u} × {v} | {fr(xa, '{:.4f}')}{' (hors du disque)' if xa > 1 else ''} | {u}/{FIB[k]} = {fr(u / FIB[k], '{:.5f}')} |"
          f" {FIB[k]} = la suivante{', le nombre d’anneaux de la lentille' if FIB[k] == 55 else ''} |")
ligne("\nLa chaîne s'arrête là dans la lentille à 55 anneaux : la composante 55 est nulle (partie XI), elle ne fait pas"
      " d'aiguille.")


# ---------------------------------------------------------------------------
# 4. Le pavage de Farey : les directions de la grille dans le plan hyperbolique
# ---------------------------------------------------------------------------
def det2(u, v):
    return u[0] * v[1] - u[1] * v[0]


FRAC = sorted({(p, q) for q in range(0, 5) for p in range(-4, 5) if math.gcd(p, q) == 1 and not (q == 0 and p != 1)},
              key=lambda f: math.atan2(f[0], f[1]) % math.pi)
VECS = [(q, p) for p, q in FRAC]  # l'aiguille de pente p/q
n_quad = ok_quad = 0
for A_, B_, C_, D_ in itertools.combinations(VECS, 4):
    n_quad += 1
    ok_quad += abs(det2(A_, C_) * det2(B_, D_)) == abs(det2(A_, B_) * det2(C_, D_)) + abs(det2(A_, D_) * det2(B_, C_))


def lambda_ford(f1, f2):
    """λ-longueur de Penner entre les cercles de Ford en p/q (diamètre 1/q²) : |x1 − x2|/√(h1·h2)."""
    (p1, q1), (p2, q2) = f1, f2
    return abs(p1 / q1 - p2 / q2) / math.sqrt(1 / q1 ** 2 / q2 ** 2)


ex_l = [((1, 2), (2, 3)), ((1, 3), (2, 3)), ((2, 5), (3, 4)), ((3, 5), (8, 13))]
ligne("\n## 4. Le pavage de Farey : les directions de la grille dans le disque de Poincaré\n")
ligne("Chaque direction de la grille est une pente p/q, un point du bord du plan hyperbolique. Deux aiguilles voisines"
      " (déterminant ±1) sont reliées par une géodésique : ce sont les arêtes du pavage de Farey, fait de triangles"
      " idéaux.")
ligne("λ-longueurs de Penner avec les cercles de Ford comme horocycles, comparées au déterminant des deux aiguilles :\n")
ligne("| pentes | λ (cercles de Ford) | déterminant |")
ligne("|---|---|---|")
for (p1, q1), (p2, q2) in ex_l:
    ligne(f"| {p1}/{q1} et {p2}/{q2} | {fr(lambda_ford((p1, q1), (p2, q2)), '{:.6f}')} | {abs(p1 * q2 - p2 * q1)} |")
ligne(f"\nRelation de Ptolémée λ₁₃·λ₂₄ = λ₁₂·λ₃₄ + λ₁₄·λ₂₃ sur les aires de quatre aiguilles rangées par direction"
      f" ({len(VECS)} directions de pentes p/q, |p| ≤ 4, q ≤ 4) : vraie pour {ok_quad} quadruplets sur {n_quad}.")


# ---------------------------------------------------------------------------
# 5. Kakeya sur une grille finie : le plan F_q²
# ---------------------------------------------------------------------------
def droites(q):
    D = {m: [frozenset((x, (m * x + c) % q) for x in range(q)) for c in range(q)] for m in range(q)}
    D["∞"] = [frozenset((c, y) for y in range(q)) for c in range(q)]
    return D


def kakeya_parabole(q):
    """Les tangentes à la parabole y = x² (une par pente non verticale), plus la droite x = 0."""
    inv4 = pow(4, q - 2, q)
    K = set()
    for a in range(q):
        K |= {(x, (a * x - a * a * inv4) % q) for x in range(q)}
    return K | {(0, y) for y in range(q)}


def est_kakeya(K, q):
    return all(any(l <= K for l in ls) for ls in droites(q).values())


def minimum_kakeya(q):
    """Plus petit ensemble de F_q² contenant une droite dans chaque direction (programmation linéaire en nombres entiers).
    Les symétries du plan affine permettent d'imposer x = 0, y = 0, et y = x + c avec c = 0 ou 1."""
    lignes = [(m, [(x, (m * x + c) % q) for x in range(q)]) for m in range(q) for c in range(q)
              if not (m == 0 and c != 0) and not (m == 1 and c not in (0, 1))]
    lignes.append(("∞", [(0, y) for y in range(q)]))
    pts = [(x, y) for x in range(q) for y in range(q)]
    idx = {p: i for i, p in enumerate(pts)}
    dirs = sorted({d for d, _ in lignes}, key=str)
    nP, nL = len(pts), len(lignes)
    A = lil_matrix((len(dirs) + nL * q, nP + nL))
    lb, ub, r = [], [], 0
    for d in dirs:
        for j, (dd, _) in enumerate(lignes):
            if dd == d:
                A[r, nP + j] = 1
        lb.append(1)
        ub.append(1)
        r += 1
    for j, (_, l) in enumerate(lignes):
        for p in l:
            A[r, idx[p]] = 1
            A[r, nP + j] = -1
            lb.append(0)
            ub.append(np.inf)
            r += 1
    res = milp(np.r_[np.ones(nP), np.zeros(nL)], constraints=LinearConstraint(A.tocsr()[:r], lb, ub),
               integrality=np.ones(nP + nL), bounds=Bounds(0, 1))
    return round(res.fun)


ligne("\n## 5. Kakeya sur une grille finie : la moitié du plan\n")
ligne("Le plan F_q² : q × q points, l'arithmétique modulo q (q premier), q + 1 directions, q droites de q points par"
      " direction. Un ensemble de Kakeya contient une droite entière dans chaque direction.\n")
ligne("| q | tangentes à la parabole + une verticale | ensemble de Kakeya ? | q(q+1)/2 + (q−1)/2 | minimum exact (calculé) | part du plan |")
ligne("|---:|---:|---|---:|---|---|")
KAK = {}
for q in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
    K = kakeya_parabole(q)
    mini = minimum_kakeya(q) if q <= 7 else None
    KAK[q] = (len(K), mini)
    ligne(f"| {q} | {len(K)} | {'oui' if est_kakeya(K, q) else 'non'} | {q * (q + 1) // 2 + (q - 1) // 2} |"
          f" {mini if mini is not None else '—'} | {fr(len(K) / q / q, '{:.3f}')} |")
ligne("\nPourquoi la moitié : un point (x, y) est sur une tangente de pente a si a² − 4ax + 4y = 0, c'est-à-dire si x² − y"
      " est un carré modulo q. Les carrés non nuls sont exactement la moitié des nombres non nuls : chaque colonne a"
      " (q+1)/2 points couverts, d'où q(q+1)/2, plus (q−1)/2 pour la verticale.")
ligne("Blokhuis et Mazzocca (2008) ont démontré que c'est le minimum pour tout q impair ; le calcul exact le confirme pour"
      " q = 3, 5 et 7.")


# ---------------------------------------------------------------------------
# 6. L'arbre de Perron sur une grille n × n
# ---------------------------------------------------------------------------
BASE_, AX_ = 2 / np.sqrt(3), 1 / np.sqrt(3)


def arbre(k_, alphas, base=BASE_, ax0=AX_):
    """Arbre de Perron à 2^k branches (même construction que les parties V et X)."""
    n_ = 2 ** k_
    xs_ = [base * i / n_ for i in range(n_ + 1)]
    l, r, axs_ = list(xs_[:-1]), list(xs_[1:]), [ax0] * n_
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
                axs_[i] += dx
            nouveaux.append((s1, e2, u1_, u1_ + alpha * largeur))
        blocs = nouveaux
    return np.array(l), np.array(r), np.array(axs_)


telescope = lambda k: [(k + 2 - j) / (k + 3 - j) for j in range(1, k + 1)]  # rapports de la partie V : aire 2/(k+2)


def cases(l, r, ax, n, garder=False):
    """Cases d'une grille de pas 1/n touchées par l'union des triangles (bases [l, r] en y = 0, sommets en y = 1)."""
    h, tot, rangs = 1 / n, 0, []
    for j in range(n):
        y0, y1 = j * h, (j + 1) * h
        a = np.floor(np.minimum(l + (ax - l) * y0, l + (ax - l) * y1) / h).astype(np.int64)
        b = np.ceil(np.maximum(r + (ax - r) * y0, r + (ax - r) * y1) / h).astype(np.int64)
        o = np.argsort(a)
        a, b = a[o], b[o]
        fin = np.concatenate(([np.iinfo(np.int64).min], np.maximum.accumulate(b)[:-1]))
        tot += int(np.maximum(0, b - np.maximum(a, fin)).sum())
        if garder:
            rangs.append((a, b))
    return (tot, rangs) if garder else tot


ligne("\n## 6. L'arbre de Perron sur une grille\n")
ligne("On dessine l'arbre de Perron de la partie V (2^k branches, aire exacte 2/(k+2) du triangle) sur une grille de"
      " n × n cases, et on compte les cases touchées, rapportées à celles du triangle.\n")
GRILLES = (16, 64, 256, 1024)
KS = list(range(1, 15))
PERRON = {}
ligne("| k (branches 2^k) | aire exacte 2/(k+2) | " + " | ".join(f"grille {n}" for n in GRILLES) + " |")
ligne("|---:|---|" + "---|" * len(GRILLES))
TRI = {n: cases(np.array([0.0]), np.array([BASE_]), np.array([AX_]), n) for n in GRILLES}
for k in KS:
    l, r, ax = arbre(k, telescope(k))
    PERRON[k] = [cases(l, r, ax, n) / TRI[n] for n in GRILLES]
    ligne(f"| {k} ({2 ** k}) | {fr(2 / (k + 2), '{:.3f}')} | " + " | ".join(fr(v, '{:.3f}') for v in PERRON[k]) + " |")
MINI = {n: min((PERRON[k][i], k) for k in KS) for i, n in enumerate(GRILLES)}
ligne("\n| grille n | meilleur arbre | part minimale | × log₂ n |")
ligne("|---:|---|---|---|")
for n, (v, k) in MINI.items():
    ligne(f"| {n} | k = {k} ({2 ** k} branches) | {fr(v, '{:.3f}')} | {fr(v * math.log2(n), '{:.2f}')} |")
ligne("\nAu-delà du meilleur arbre, ajouter des branches fait remonter l'aire : une branche plus fine qu'une case occupe"
      " quand même une case par rangée. Le minimum ne baisse que comme 1/log n (son produit par log₂ n reste presque"
      " constant). Córdoba (1977) a montré qu'on ne peut pas faire mieux que cet ordre, et Keich (1999) qu'il est atteint.")

with open(os.path.join(ICI, "..", "resultats", "aiguille_grille.md"), "w") as fh:
    fh.write("# Résultats de la partie XIV (générés par scripts/aiguille_grille.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure 1 : l'aiguille sur la grille
# ===========================================================================
fig = plt.figure(figsize=(20, 13.4))
gs = fig.add_gridspec(2, 3, wspace=0.16, hspace=0.24)
FOND = dict(fc=F.SURF, ec="none", alpha=0.92, pad=2.5)


def schema(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")


# a) demi-cercle et disque
ax = fig.add_subplot(gs[0, 0])
gx, gy = np.meshgrid(np.arange(-11, 12), np.arange(0, 12))
ax.plot(gx, gy, ".", color=F.BASE, ms=3)
ax.add_patch(Wedge((0, 0), LF, 0, 180, fc=F.BLEU, alpha=0.12, ec="none"))
for i, (x, y) in enumerate(DEMI):
    ax.plot([0, x], [0, y], color=F.BLEU, lw=1.4, alpha=0.85)
    F.point(ax, x, y, F.ORANGE, 6)
ax.plot([p[0] for p in DEMI], [p[1] for p in DEMI], color=F.ORANGE, lw=1, ls=":")
ax.plot([0, 6, 6], [0, 0, 8], color=F.AQUA, lw=1.6)
ax.text(3, -0.7, "6", ha="center", fontsize=8.5, color=F.AQUA)
ax.text(6.4, 4, "8", fontsize=8.5, color=F.AQUA)
F.point(ax, 0, 0, F.INK, 7)
ax.text(0, 11.4, f"un bout à l'origine : {len(DEMI)} positions, le demi-disque", ha="center", fontsize=10)
oy = -8
gx2, gy2 = np.meshgrid(np.arange(-6, 7), np.arange(oy - 6, oy + 7))
ax.plot(gx2, gy2, ".", color=F.BASE, ms=3)
ax.add_patch(plt.Circle((0, oy), LF / 2, fc=F.ORANGE, alpha=0.12, ec="none"))
for x, y in points_cercle(LF // 2):
    if y > 0 or (y == 0 and x > 0):
        ax.plot([x, -x], [oy + y, oy - y], color=F.ORANGE, lw=1.3, alpha=0.85)
for x, y in points_cercle(LF // 2):
    F.point(ax, x, oy + y, F.BLEU, 5)
F.point(ax, 0, oy, F.INK, 7)
ax.text(0, oy - 7.2, f"le milieu à l'origine : {len(points_cercle(LF // 2)) // 2} positions, le disque", ha="center", fontsize=10)
ax.text(11.5, 6.5, f"aiguille de longueur {LF}\nsur une grille de pas 1 :\nses bouts ne peuvent être\nque sur les points (6, 8),\n"
        "(8, 6), (10, 0)…\nles triangles 3-4-5", fontsize=9, color=F.INK2, va="top")
ax.text(7.5, oy + 1, f"aire balayée :\ndemi-disque πL²/2,\ndisque πL²/4,\ndeltoïde πL²/8", fontsize=9, color=F.INK2, va="top")
schema(ax, (-11.5, 18), (oy - 8, 12))
ax.set_title("a)  S'inverser sur la grille : demi-cercle ou disque")

# b) les directions permises, l'angle du 3-4-5
ax = fig.add_subplot(gs[0, 1])
for k in range(0, 7):
    rr = 1 + k
    t = np.linspace(0, np.pi / 2, 200)
    ax.plot(rr * np.cos(t), rr * np.sin(t), color=F.GRID, lw=1)
    angs = [0.0] if k == 0 else TROUS5[k][0]
    for a in angs + [90.0]:
        ar = math.radians(a)
        ax.plot([rr * math.cos(ar)], [rr * math.sin(ar)], "o", color=F.ORANGE if k else F.INK, ms=4.5, mec=F.SURF, mew=0.6)
    ax.text(rr, -0.25, "1" if k == 0 else f"5{'' if k == 1 else chr(0x2070 + k) if k > 3 else '²³'[k - 2]}", ha="center",
            va="top", fontsize=8.5, color=F.INK2)
ax.text(3.5, -0.85, "longueur L de l'aiguille", ha="center", fontsize=9, color=F.INK2)
ar = math.radians(TH0)
ax.plot([0, 7.4 * math.cos(ar)], [0, 7.4 * math.sin(ar)], color=F.BLEU, lw=1, ls="--")
ax.text(7.5 * math.cos(ar) + 0.1, 7.5 * math.sin(ar), "53,13° = arctan(4/3)", fontsize=9, color=F.BLEU)
ax.text(-0.2, 8.6, "Directions permises dans un quart de tour, pour L = 1, 5, 25, …, 5⁶ :\n"
        "les m × 53,13° (l'angle du 3-4-5), à un quart de tour près.\n"
        "Les trous n'ont jamais plus de 3 longueurs (théorème des trois distances,\n"
        "comme l'angle d'or, partie XI). Seul L = 1 n'a que les quarts de tour.", fontsize=9, color=F.INK2, va="top")
schema(ax, (-0.5, 9.5), (-1.2, 9.2))
ax.set_title("b)  Les directions permises : l'angle du triangle 3-4-5")

# c) compter les points : comme L², et comme V(d)·L^d
ax = fig.add_subplot(gs[0, 2])
Ls = sorted(COMPTES)
for i, (nom, aire, coul) in enumerate((("demi-disque (un bout fixe)", 0.5, F.BLEU), ("disque (milieu fixe)", 0.25, F.ORANGE),
                                       ("deltoïde (Kakeya)", 0.125, F.AQUA))):
    ax.loglog(Ls, [COMPTES[L][i] for L in Ls], "o", color=coul, ms=6, mec=F.SURF, label=nom)
    xx = np.array([3, 300])
    ax.loglog(xx, aire * math.pi * xx ** 2, color=coul, lw=1)
ax.set_xlabel("longueur L de l'aiguille (en pas de grille)")
ax.set_ylabel("points de la grille balayés")
ax.legend(fontsize=9, loc="upper left", frameon=True, facecolor=F.SURF, edgecolor="none")
ax.text(0.97, 0.36, "traits : πL²/2, πL²/4, πL²/8\n(pente 2 : « comme n² »)", transform=ax.transAxes, ha="right", fontsize=9,
        color=F.INK2)
axi = ax.inset_axes([0.6, 0.06, 0.36, 0.23])
axi.bar(range(1, 6), [VB[d] for d in range(1, 6)], color=F.BASE)
axi.axhline(1, color=F.INK2, lw=0.8)
axi.set_ylim(0.9, 1.06)
axi.set_xticks(range(1, 6))
axi.tick_params(labelsize=7)
axi.set_title("dimension d : points / (V(d)·12^d)", fontsize=7.5, fontweight="normal", loc="center")
axi.set_facecolor(F.SURF)
ax.set_title("c)  Compter les points : comme n², par dimension")

# d) les aiguilles de Fibonacci
ax = fig.add_subplot(gs[1, 0])
gx, gy = np.meshgrid(np.arange(0, 8), np.arange(0, 10))
ax.plot(gx, gy, ".", color=F.BASE, ms=4.5)
xx = np.linspace(0, 5.9, 10)
ax.plot(xx, PHI * xx, color=F.INK, lw=1, ls="--")
ax.text(6.05, 9.35, "y = φx", fontsize=9, ha="left", va="center")
for k in range(1, 6):
    v, w = (FIB[k], FIB[k + 1]), (FIB[k + 1], FIB[k + 2])
    coul = F.ORANGE if k % 2 else F.BLEU
    if k < 5:
        ax.add_patch(Polygon([(0, 0), v, w], closed=True, fc=coul, alpha=0.25, ec=coul, lw=0.6))
    ax.annotate("", xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=coul, lw=1.5, shrinkA=0, shrinkB=0))
    ax.text(v[0] + (0.18 if k % 2 else -0.18), v[1], f"({v[0]}, {v[1]})", fontsize=9, ha="left" if k % 2 else "right",
            va="center")
F.point(ax, 0, 0, F.INK, 6)
ax.text(2.6, 2.3, "Chaque triangle entre deux voisines a\nl'aire 1/2 et aucun point de la grille\ndedans (Cassini, Pick) : une demi-case.\n"
        "La suivante est la somme des deux\nprécédentes : (3, 5) + (5, 8) = (8, 13).", fontsize=9, color=F.INK2, va="top", bbox=FOND)
axi = ax.inset_axes([0.02, 0.64, 0.38, 0.3])
kk = np.arange(1, 13)
gap = np.array([FIB[k + 1] - PHI * FIB[k] for k in kk])
axi.axhline(0, color=F.INK, lw=0.8, ls="--")
axi.vlines(kk, 0, gap, colors=[F.ORANGE if k % 2 else F.BLEU for k in kk], lw=2)
axi.plot(kk, PHI ** -kk.astype(float), color=F.MUTED, lw=0.8)
axi.plot(kk, -PHI ** -kk.astype(float), color=F.MUTED, lw=0.8)
axi.set_xticks([1, 4, 8, 12])
axi.tick_params(labelsize=7)
axi.set_title("écart à la direction d'or y = φx : (−1/φ)^k", fontsize=7.5, fontweight="normal", loc="center")
axi.set_xlabel("k", fontsize=7.5, labelpad=1)
axi.set_facecolor(F.SURF)
schema(ax, (-0.6, 7.6), (-0.6, 9.6))
ax.set_title("d)  Les convergentes : une demi-case entre voisines")


# e) le pavage de Farey dans le disque de Poincaré, centré sur la suite de Fibonacci
def T(x):
    return (x - PHI) / (x + 1 / PHI)  # isométrie (Möbius) : φ → 0, −1/φ → ∞


LAMB = 1 / math.sqrt(abs(T(FIB[5] / FIB[4]) * T(FIB[6] / FIB[5])))


def bord(p, q):
    if q == 0:
        z = LAMB * 1.0
    else:
        z = LAMB * T(p / q)
    w = (z - 1j) / (z + 1j)
    return np.array([w.real, w.imag])


def geodesique(A_, B_, n=60):
    ta, tb = math.atan2(A_[1], A_[0]), math.atan2(B_[1], B_[0])
    d = (tb - ta + np.pi) % (2 * np.pi) - np.pi
    if abs(abs(d) - np.pi) < 1e-9:
        return np.c_[np.linspace(A_[0], B_[0], n), np.linspace(A_[1], B_[1], n)]
    tm = ta + d / 2
    c = np.array([math.cos(tm), math.sin(tm)]) / math.cos(d / 2)
    rr = abs(math.tan(d / 2))
    a1, a2 = math.atan2(A_[1] - c[1], A_[0] - c[0]), math.atan2(B_[1] - c[1], B_[0] - c[0])
    da = (a2 - a1 + np.pi) % (2 * np.pi) - np.pi
    t = np.linspace(a1, a1 + da, n)
    return np.c_[c[0] + rr * np.cos(t), c[1] + rr * np.sin(t)]


ax = fig.add_subplot(gs[1, 1])
t = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(t), np.sin(t), color=F.INK, lw=1.3)
FR = sorted({(p, q) for q in range(0, 22) for p in range(-126, 127) if math.gcd(p, q) == 1 and not (q == 0 and p != 1)})
for i, a in enumerate(FR):
    for b in FR[i + 1:]:
        if abs(a[0] * b[1] - a[1] * b[0]) == 1:
            A_, B_ = bord(*a), bord(*b)
            if np.linalg.norm(A_ - B_) > 0.012:
                g = geodesique(A_, B_)
                ax.plot(g[:, 0], g[:, 1], color=F.BLEU, lw=0.45, alpha=0.55)
for k in range(1, 9):
    pts = [bord(FIB[k + 1], FIB[k]), bord(FIB[k + 2], FIB[k + 1]), bord(FIB[k + 3], FIB[k + 2])]
    cont = np.vstack([geodesique(pts[0], pts[1]), geodesique(pts[1], pts[2]), geodesique(pts[2], pts[0])])
    ax.add_patch(Polygon(cont, closed=True, fc=F.ORANGE if k % 2 else F.JAUNE, alpha=0.45, ec="none"))
for k in range(2, 8):
    B_ = bord(FIB[k + 1], FIB[k])
    ax.text(1.08 * B_[0], 1.08 * B_[1], f"({FIB[k]}, {FIB[k + 1]})", ha="center", va="center", fontsize=8.5, bbox=FOND)
P_ = bord(PHI, 1)
F.point(ax, *P_, F.INK, 6)
ax.text(P_[0] - 0.07, P_[1] + 0.02, "φ", ha="right", va="center", fontsize=12)
ax.text(-1.15, -1.22, "Chaque point du bord est une direction de la grille (une pente p/q).\n"
        "Arêtes : deux aiguilles voisines (une case). Triangles colorés : trois\n"
        "aiguilles de Fibonacci de suite, en route vers φ. Les aires des\n"
        f"aiguilles sont les λ-longueurs de Penner : Ptolémée exact ({ok_quad} cas sur {n_quad}).", fontsize=9,
        color=F.INK2, va="top")
schema(ax, (-1.25, 1.25), (-1.75, 1.3))
ax.set_title("e)  Les directions de la grille dans le disque de Poincaré")

# f) Kakeya sur une grille finie
ax = fig.add_subplot(gs[1, 2])
q = 13
K = kakeya_parabole(q)
for x in range(q):
    for y in range(q):
        if (x, y) in K:
            ax.add_patch(Rectangle((x - 0.42, y - 0.42), 0.84, 0.84, fc=F.BLEU, alpha=0.75, ec="none"))
        else:
            ax.plot(x, y, ".", color=F.BASE, ms=3)
for x in range(q):
    ax.plot(x, (x * x) % q, "o", color=F.ORANGE, ms=5.5, mec=F.SURF, mew=0.6)
ax.set_xlim(-0.8, q + 6.6)
ax.set_ylim(-1.2, q + 3.2)
ax.set_aspect("equal")
ax.axis("off")
ax.text(-0.5, q + 2.2, f"F₁₃² : {q * q} points. En bleu, les {q} tangentes à la parabole y = x² (orange)\n"
        f"et une verticale : {len(K)} points, une droite dans chaque direction.\n"
        "Modulo 13, les droites s'enroulent sur la grille : elles ne se voient plus droites.", fontsize=9, color=F.INK2,
        va="top")
axi = ax.inset_axes([0.735, 0.12, 0.26, 0.5])
qs = np.arange(3, 60)
axi.plot(qs, (qs * (qs + 1) / 2 + (qs - 1) / 2) / qs ** 2, color=F.BLEU, lw=1.2)
for qq, (s, mi) in KAK.items():
    axi.plot(qq, s / qq ** 2, "o", color=F.ORANGE if mi is not None else F.BLEU, ms=4, mec=F.SURF, mew=0.5)
axi.axhline(0.5, color=F.INK2, lw=0.8, ls="--")
axi.set_ylim(0.45, 0.8)
axi.set_xlabel("q", fontsize=8, labelpad=1)
axi.tick_params(labelsize=7)
axi.set_title("part minimale du plan\n(orange : calculée exactement)", fontsize=7.5, fontweight="normal", loc="center")
axi.set_facecolor(F.SURF)
ax.set_title("f)  Kakeya sur une grille finie : la moitié du plan")
F.sauver(fig, "n1_aiguille_grille.png")

# ===========================================================================
# Figure 2 : l'arbre de Perron sur la grille
# ===========================================================================
fig, axs = plt.subplots(1, 3, figsize=(20, 6.8), gridspec_kw={"wspace": 0.12, "width_ratios": [1, 1, 1.25]})
n_ = 64
T64 = TRI[n_]
BORNES = [arbre(k, telescope(k)) for k in (MINI[n_][1], 10)]
X0 = min(min(b[0].min(), b[2].min()) for b in BORNES) - 0.03
X1 = max(max(b[1].max(), b[2].max()) for b in BORNES) + 0.03
for ax, k in zip(axs[:2], (MINI[n_][1], 10)):
    l, r, ax_ = arbre(k, telescope(k))
    tot, rangs = cases(l, r, ax_, n_, garder=True)
    h = 1 / n_
    for j, (a, b) in enumerate(rangs):
        couv = set()
        for x0, x1 in zip(a, b):
            couv.update(range(x0, x1))
        for c in couv:
            ax.add_patch(Rectangle((c * h, j * h), h, h, fc=F.BLEU, alpha=0.55, ec="none"))
    if k <= 6:
        for i in range(len(l)):
            ax.add_patch(Polygon([[l[i], 0], [r[i], 0], [ax_[i], 1]], closed=True, fill=False, ec=F.INK, lw=0.35, alpha=0.6))
    ax.add_patch(Polygon([[0, 0], [BASE_, 0], [AX_, 1]], closed=True, fill=False, ec=F.MUTED, lw=1, ls=(0, (4, 3))))
    ax.set_xlim(X0, X1)
    ax.set_ylim(-0.03, 1.03)
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")
    ax.text(0.5, -0.06, f"{2 ** k} branches : {tot} cases, soit {tot / T64:.2f} du triangle (aire exacte {2 / (k + 2):.2f})"
            .replace(".", ","), transform=ax.transAxes, ha="center", va="top", fontsize=9.5)
axs[0].set_title(f"a)  Grille {n_} × {n_} : le meilleur arbre ({2 ** MINI[n_][1]} branches)")
axs[1].set_title("b)  1024 branches : la grille les épaissit")
ax = axs[2]
couls = [F.AQUA, F.BLEU, F.ORANGE, ROUGE]
for i, n in enumerate(GRILLES):
    ax.plot(KS, [PERRON[k][i] for k in KS], "o-", color=couls[i], ms=4, lw=1.3, label=f"grille {n} × {n}")
    v, k = MINI[n]
    ax.plot(k, v, "o", color=couls[i], ms=10, mfc="none", mew=1.5)
ax.plot(KS, [2 / (k + 2) for k in KS], color=F.INK, lw=1.2, ls="--", label="sans grille : 2/(k+2), vers 0")
ax.set_xlabel("k (l'arbre a 2^k branches)")
ax.set_ylabel("part du triangle couverte")
ax.set_ylim(0, 1.06)
ax.legend(fontsize=9, loc="upper left", ncol=2, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.text(0.03, 0.04, "Cercles : le meilleur arbre de chaque grille. Le minimum ne baisse\nque comme 1/log n : "
        + ", ".join(f"{v:.2f}" for v, _ in MINI.values()).replace(".", ",") + " pour n = 16, 64, 256, 1024.",
        transform=ax.transAxes, fontsize=9, color=F.INK2)
ax.set_title("c)  Sur une grille, Perron ne descend plus à zéro")
F.sauver(fig, "n2_perron_grille.png")
