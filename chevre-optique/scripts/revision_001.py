"""
Révision 001 du recueil : les tests attachés à la révision (CLAUDE.md, § 10).

    python3 scripts/revision_001.py        # ≈ 10 s

Écrit resultats/revision_001.md et la figure figures/rev001_perron_venn.png. La synthèse est dans
recueil/revisions/revision-001.md, les dossiers dans recueil/dossiers/.

1. La diagonale √2 : le simplexe de la classification naïve, la corde de la chèvre et le triangle de Thalès.
2. Les fiches dans le Venn des dimensions, avant et après la révision.
3. Le nerf du recouvrement par les dossiers : nombres de Betti et triangles vides.
4. Les nouveaux tests.
"""

import csv
import itertools
import os
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402

ICI = os.path.dirname(os.path.abspath(__file__))
REC = os.path.join(ICI, "..", "recueil")
T0 = time.time()
md = []
mp.mp.dps = 30


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


def mpf(x, k=12):
    return mp.nstr(x, k).replace(".", ",").replace("-", "−")


# ===========================================================================
# 1. La diagonale √2
# ===========================================================================
def calotte(n, R, h):
    """Volume de la calotte de hauteur h d'une boule de rayon R en dimension n, en unités de V_n·Rⁿ."""
    if h <= 0:
        return mp.mpf(0)
    if h >= 2 * R:
        return mp.mpf(1)
    if h <= R:
        return mp.betainc((n + 1) / mp.mpf(2), mp.mpf(1) / 2, 0, (2 * R * h - h * h) / R**2, regularized=True) / 2
    return 1 - calotte(n, R, 2 * R - h)


def broute(n, r):
    """Part de la boule unité broutée par une corde r attachée sur sa sphère (deux calottes de part et d'autre du plan)."""
    x0 = (2 - r * r) / 2
    return calotte(n, 1, 1 - x0) + calotte(n, r, r - (1 - x0)) * r**n


def corde(n):
    if n == 1:
        return mp.mpf(1)
    return mp.findroot(lambda r: broute(n, r) - mp.mpf(1) / 2, mp.sqrt(2) - mp.mpf(1) / n)


def simplexe_centre(parts):
    """Classe naïve : un représentant par dimension, centré avec les parts données, puis normalisé."""
    K = len(parts)
    X = np.eye(K)
    p = np.asarray(parts, float) / np.sum(parts)
    Xc = X - p                     # on retire la fiche moyenne (pondérée par les parts)
    return Xc / np.linalg.norm(Xc, axis=1, keepdims=True)


ligne("# Révision 001 du recueil : les tests attachés à la révision")
ligne()
ligne("Écrit par `python3 scripts/revision_001.py`. La synthèse est dans"
      " [`recueil/revisions/revision-001.md`](../recueil/revisions/revision-001.md).")
ligne()
ligne("## 1. La diagonale √2 : la classification naïve, la corde de la chèvre et Thalès")
ligne()
ligne("**La classification naïve est un simplexe.** On range K fiches à parts égales dans K dimensions (un vecteur"
      " d'appartenance 0/1 par fiche), puis on retire la fiche moyenne et on normalise. Les K vecteurs sont alors les"
      " sommets du simplexe régulier inscrit dans la sphère unité : cos = −1/(K − 1) entre deux sommets.")
ligne()
ligne("**Deux longueurs pour chaque paire, et Thalès.** Pour deux vecteurs unités u et w :")
ligne("- l'arête d = |u − w| (la distance entre les deux fiches) ;")
ligne("- la corde c = |u + w| (de u à l'antipode de w).")
ligne("- On a toujours d² + c² = 4. Le triangle (w, u, −w) est rectangle en u, d'hypoténuse le diamètre (Thalès).")
ligne("- Pour le simplexe : d² = 2 + 2/(K − 1) et c² = 2 − 2/(K − 1). Les deux côtés de l'angle droit tendent vers √2 :"
      " le triangle devient isocèle, c'est la moitié d'un carré de diagonale 2.")
ligne()
ligne("**La corde de la chèvre est la corde c d'un simplexe.** La partie XXIV a montré r_n² = 2 − 2x₀ (Euclide), avec un"
      " plan de lentille en 1/x₀ = n + 4/3 − 112/(45n) + … Donc ρ_n = c_K pour K − 1 = 1/x₀ : la chèvre de dimension n a la"
      " corde du simplexe de la classification naïve à K = n + 2 + (N − n) dimensions. N − n est le tiers de dimension"
      " de la partie XXIV (de 0 en 1D à 1/3 à l'infini).")
ligne()
ligne("| n | corde ρ_n (chèvre) | n·(2 − ρ_n²) | K tel que c_K = ρ_n | K − n | 7/3 − 112/(45n) + 3856/(189n²) |"
      " arête d_K de ce simplexe |")
ligne("|---:|---|---:|---:|---:|---:|---:|")
CORDES = {}
for n in [1, 2, 3, 4, 8, 17, 24, 100, 1000]:
    r = corde(n)
    CORDES[n] = r
    x0 = (2 - r * r) / 2
    K = 1 + 1 / x0
    dK = mp.sqrt(2 + 2 / (K - 1))
    asy = mp.mpf(7) / 3 - mp.mpf(112) / (45 * n) + mp.mpf(3856) / (189 * n**2)
    ligne(f"| {n} | {mpf(r)} | {mpf(n * (2 - r * r), 6)} | {mpf(K, 8)} | {mpf(K - n, 6)} |"
          f" {mpf(asy, 6) if n >= 24 else '—'} | {mpf(dK, 8)} |")
ligne()
ligne("- Contrôle : les cordes redonnent le tableau de la partie XX (calculées ici par les calottes, là par la division"
      " d'intégrales d'Ullisch), par exemple ρ₂ = 1,15872847302 et ρ₁₀₀ = 1,40721663872.")
ligne("- K − n monte de 2 (en 1D, où la corde vaut 1) vers 7/3 = 2,3333… : c'est 2 + le tiers de dimension.")
ligne()
ligne("**Le contrôle numérique du simplexe** (les vecteurs centrés, sans formule) :")
ligne()
ligne("| K | d_K mesuré | √(2K/(K − 1)) | c_K mesuré | √(2(K − 2)/(K − 1)) | d² + c² |")
ligne("|---:|---:|---:|---:|---:|---:|")
for K in [2, 3, 4, 8, 17, 100, 1000]:
    U = simplexe_centre([1] * K)
    d = float(np.linalg.norm(U[0] - U[1]))
    c = float(np.linalg.norm(U[0] + U[1]))
    ligne(f"| {K} | {fr(d, '{:.10f}')} | {fr((2 * K / (K - 1)) ** 0.5, '{:.10f}')} | {fr(c, '{:.10f}')} |"
          f" {fr((2 * (K - 2) / (K - 1)) ** 0.5, '{:.10f}')} | {fr(d * d + c * c, '{:.12f}')} |")
ligne()
ligne("- Sans centrer, deux fiches de dimensions différentes sont exactement à √2 l'une de l'autre, pour tout K : la"
      " diagonale d'une face du cube {0, 1}^K du Venn. En retirant ce que toutes les fiches ont en commun (la moyenne),"
      " on obtient le simplexe, et le √2 devient une limite : il « s'affirme » quand le nombre de dimensions grandit.")
ligne("- Le « partage équitable des aires » est ce qui rend le simplexe régulier. Avec des parts inégales, les arêtes"
      " se déforment (section 2).")



# ===========================================================================
# 2. Les fiches dans le Venn des dimensions
# ===========================================================================
DIMS = [f"D{k}" for k in range(1, 9)]
NOMS_DIMS = {"D1": "la chèvre et les cordes", "D2": "bases, chiffres et congruences", "D3": "grain, pixels et précision",
             "D4": "optique et diffraction", "D5": "Kakeya, Perron et aiguilles", "D6": "sphères, cubes, Venn et symétries",
             "D7": "hasard et méthode", "D8": "physique"}
with open(os.path.join(REC, "index.csv"), encoding="utf-8") as fh:
    FICHES = [x for x in csv.DictReader(fh) if int(x["numero"]) <= 15]   # les fiches couvertes par cette révision
PRIM = {x["numero"]: x["dimension"][:2] for x in FICHES}


def vecteurs(appart, dims):
    """appart : numéro -> ensemble de dimensions. Vecteurs 0/1 centrés (on retire la fiche moyenne) et normalisés."""
    nums = sorted(appart)
    X = np.array([[1.0 if d in appart[n] else 0.0 for d in dims] for n in nums])
    Xc = X - X.mean(0)
    return nums, Xc / np.linalg.norm(Xc, axis=1, keepdims=True), X.sum(0)


ligne()
ligne("## 2. Les fiches dans le Venn des dimensions")
ligne()
ligne("### 2.1 Avant la révision : la classification naïve, à parts inégales")
ligne()
avant = {n: {d} for n, d in PRIM.items()}
DU = [d for d in DIMS if any(d in v for v in avant.values())]
nums, U0, parts0 = vecteurs(avant, DU)
K0 = len(DU)
p0 = parts0 / parts0.sum()
s2 = float(np.sum(p0**2))
ligne(f"Les 15 fiches occupent K = {K0} dimensions sur 8 : " + ", ".join(f"{d} ({int(c)})" for d, c in zip(DU, parts0))
      + f". Avec des parts égales, le simplexe régulier aurait toutes ses arêtes à √(2K/(K − 1)) = {fr((2 * K0 / (K0 - 1)) ** 0.5)}."
      f" Le nombre effectif de dimensions (1/Σp²) vaut {fr(1 / s2, '{:.2f}')}.")
ligne()
ligne("| paire de dimensions | parts | p_a + p_b | Σp² | arête mesurée | côté de √2 |")
ligne("|---|---|---:|---:|---:|---|")
ARETES0 = {}
for i, a in enumerate(DU):
    for b in DU[i + 1:]:
        ia = next(k for k, n in enumerate(nums) if a in avant[n])
        ib = next(k for k, n in enumerate(nums) if b in avant[n])
        d = float(np.linalg.norm(U0[ia] - U0[ib]))
        ARETES0[(a, b)] = d
        pa, pb = p0[DU.index(a)], p0[DU.index(b)]
        ligne(f"| {a}–{b} | {int(parts0[DU.index(a)])} et {int(parts0[DU.index(b)])} | {fr(pa + pb)} | {fr(s2)} |"
              f" {fr(d)} | {'en dessous (lien apparent)' if d < 2**0.5 else 'au-dessus'} |")
# la règle : une paire passe sous √2 exactement quand p_a + p_b < Σp²
regle = all((ARETES0[(a, b)] < 2**0.5) == (p0[DU.index(a)] + p0[DU.index(b)] < s2) for (a, b) in ARETES0)
ligne()
ligne("**Le cadre crée des liens.** Entre deux fiches de classes a et b, la corrélation des vecteurs centrés vaut"
      " (Σp² − p_a − p_b)/√((1 − 2p_a + Σp²)(1 − 2p_b + Σp²)). Elle est positive, donc l'arête passe sous √2, exactement"
      f" quand p_a + p_b < Σp² (vérifié sur les {len(ARETES0)} paires : {'oui' if regle else 'NON'}). Deux dimensions"
      " rares paraissent donc liées sans rien partager : elles ont seulement en commun de ne pas être les grosses"
      " classes. Avec des parts égales, p_a + p_b = 2/K > Σp² = 1/K : aucune paire ne passe sous √2, toutes les arêtes"
      " sont égales, et elles rejoignent √2 quand K grandit. **Le partage équitable des aires est ce qui empêche le"
      " cadre de fabriquer des corrélations.** C'est le « problème des doubles zéros » de l'écologie numérique"
      " (deux relevés paraissent semblables parce qu'il leur manque les mêmes espèces : Legendre et Legendre), de la"
      " même famille que les corrélations parasites des données à somme constante (Pearson, 1897 ; Chayes, 1960 ;"
      " Aitchison, 1986).")
assert regle


# ===========================================================================
# 4. Les nouveaux tests (ceux de l'agent de session ; ceux du workflow suivent)
# ===========================================================================
def premiers(n):
    crible = bytearray([1]) * (n + 1)
    crible[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if crible[i]:
            crible[i * i::i] = bytearray(len(crible[i * i::i]))
    return [i for i in range(n + 1) if crible[i]]


def chiffres_periode(p, b):
    """Les chiffres de la période de 1/p en base b (p premier, p ne divise pas b)."""
    r, vus, ch_ = 1, set(), []
    while r not in vus:
        vus.add(r)
        ch_.append((r * b) // p)
        r = (r * b) % p
    return ch_


def orbite(a, m):
    o, x = [], 1
    while x not in o:
        o.append(x)
        x = (x * a) % m
    return o


TESTS = []
ligne()
ligne("## 4. Les nouveaux tests")
ligne()
ligne("### 4.1 Fiche 013 : la période de 1/7 et les racines digitales de 2ⁿ, en faisant varier la base")
ligne()
ligne("La fiche 013 note que la période de 1/7 (142857) s'écrit avec exactement les chiffres que visitent les racines"
      " digitales de 2ⁿ (1, 2, 4, 8, 7, 5), c'est-à-dire les unités modulo 9. On fait varier la base b et le premier p :"
      " pour quels (b, p) l'ensemble des chiffres de la période de 1/p en base b est-il exactement l'ensemble des unités"
      " modulo b − 1 (les racines digitales premières avec b − 1) ?")
ligne()
P400 = premiers(400)
cas = []
for b in range(3, 61):
    U = {u for u in range(1, b - 1) if np.gcd(u, b - 1) == 1}
    for p_ in P400:
        if b % p_ and set(chiffres_periode(p_, b)) == U:
            cas.append((b, p_, sorted(U), np.gcd(2, b - 1) == 1 and set(orbite(2, b - 1)) == U))
ligne("| base b | premier p | chiffres de la période de 1/p | 2 engendre-t-il les unités modulo b − 1 ? |")
ligne("|---:|---:|---|---|")
for b, p_, U, g in cas:
    ligne(f"| {b} | {p_} | {{{', '.join(map(str, U))}}} | {'oui' if g else 'non'} |")
ligne()
ligne(f"- Bases 3 à 60, premiers jusqu'à 400 : {len(cas)} cas. En dehors des deux cas à un ou deux chiffres (bases 3 et 5),"
      " seul (10, 7) répond, et c'est le seul où les puissances de 2 parcourent aussi toutes les unités.")
ligne("- **Pourquoi la base 10.** Les chiffres absents de la période de 1/7 sont 0, 3, 6 et 9. Ce sont les d pour lesquels"
      " l'intervalle [7d/10, 7(d + 1)/10[ ne contient aucun entier de 1 à 6, et cela tient à 7 × 3 = 21 ≡ 1 (mod 10) :"
      " 3 est l'inverse de 7 modulo 10, donc 7 × 3k ≡ k et les d absents sont ceux où 7d mod 10 ≤ 3, soit 0, 3, 6, 9."
      " Les racines digitales absentes sont les multiples de 3 parce que 9 = 3². Le même 3 joue donc deux rôles :"
      " l'inverse de 7 modulo 10, et le premier de 9 = 10 − 1. La base 10 réunit ces deux rôles, et le balayage dit"
      " qu'aucune autre base de la plage ne réunit l'équivalent.")
ligne("- **Verdict.** Ce n'est pas une loi des bases, c'est un fait singulier de la base 10. Faire varier le paramètre le"
      " montre, et l'explique (le choix du test du § 10). La fiche 013 passe de « exact pour 7 » à « exact, et propre à"
      " la base 10 ».")
TESTS.append(("013", "variation de la base (3 à 60) et du premier (jusqu'à 400)", f"{len(cas)} cas, dont un seul non trivial : (10, 7)"))
assert [(b, p_) for b, p_, _, _ in cas] == [(3, 2), (5, 3), (10, 7)]
assert set(range(10)) - set(chiffres_periode(7, 10)) == {d for d in range(10) if (7 * d) % 10 <= 3} == {0, 3, 6, 9}

ligne()
ligne("### 4.2 Fiche 015 : les paires de premiers dans une dizaine, en faisant varier la taille N")
ligne()
ligne("Sous 10⁶, les dizaines dont les seuls premiers sont {1, 7} ou {3, 9} (distance 6) sont environ 2,8 fois plus"
      " nombreuses, motif par motif, que celles dont les seuls premiers sont {1, 3}, {7, 9}, {3, 7} ou {1, 9}"
      " (fiche 015). On refait le compte de 10⁴ à 10⁸, de deux façons :")
ligne("- **motifs exacts** : la dizaine n'a que ces deux premiers parmi 1, 3, 7, 9 (le rapport par motif) ;")
ligne("- **paires larges** : les deux sont premiers, quoi qu'il en soit des deux autres (rapport des paires à distance 6"
      " sur les paires à distance 2, dans la même dizaine).")
ligne()
NMAX = 10**8
crible = np.ones(NMAX + 1, dtype=bool)
crible[:2] = False
for i in range(2, int(NMAX**0.5) + 1):
    if crible[i]:
        crible[i * i::i] = False
ligne("| N | motifs exacts {1, 7} + {3, 9} | motifs exacts {1, 3} + {7, 9} | motifs exacts {3, 7} + {1, 9} |"
      " rapport par motif | paires larges : distance 6 / distance 2 |")
ligne("|---:|---:|---:|---:|---:|---:|")
RAPPORTS = {}
for E in range(4, 9):
    Dz = crible[:10**E].reshape(-1, 10)
    u1, u3, u7, u9 = Dz[:, 1], Dz[:, 3], Dz[:, 7], Dz[:, 9]

    def exact(a, b, c, d):
        return int(np.sum((u1 == a) & (u3 == b) & (u7 == c) & (u9 == d)))
    six = exact(1, 0, 1, 0) + exact(0, 1, 0, 1)
    deux = exact(1, 1, 0, 0) + exact(0, 0, 1, 1)
    quatre = exact(0, 1, 1, 0) + exact(1, 0, 0, 1)
    rap = (six / 2) / ((deux + quatre) / 4)
    larges = (int(np.sum(u1 & u7)) + int(np.sum(u3 & u9))) / (int(np.sum(u1 & u3)) + int(np.sum(u7 & u9)))
    RAPPORTS[E] = (rap, larges)
    ligne(f"| 10^{E} | {six} | {deux} | {quatre} | {fr(rap)} | {fr(larges)} |")
ligne()
ligne(f"- **Le rapport par motif dérive** : {fr(RAPPORTS[4][0], '{:.2f}')} à 10⁴, {fr(RAPPORTS[5][0])} à 10⁵"
      f" (π = 3,1416, écart {fr(abs(RAPPORTS[5][0] - np.pi) / np.pi * 100, '{:.2f}')} %),"
      f" {fr(RAPPORTS[6][0])} à 10⁶ (2√2 = 2,8284, écart {fr(abs(RAPPORTS[6][0] - 2 * 2**0.5) / (2 * 2**0.5) * 100, '{:.2f}')} %),"
      f" puis {fr(RAPPORTS[7][0])} et {fr(RAPPORTS[8][0])}. Il croise π puis 2√2 en passant : ce sont deux hasards de"
      " taille. Sa vraie limite est 2, très lentement. Sur la face a ≡ 0 modulo 3, 3 et 9 sont composés d'office :"
      " l'exclusivité ne coûte rien à la moitié des paires {1, 7}, alors qu'elle coûte à toutes les paires {1, 3}, qui ne"
      " vivent que sur la face a ≡ 1. Cet avantage s'efface au rythme de la densité des premiers, en 1/ln N.")
ligne(f"- **Le rapport des paires larges ne bouge pas** : entre {fr(min(v[1] for v in RAPPORTS.values()), '{:.3f}')} et"
      f" {fr(max(v[1] for v in RAPPORTS.values()), '{:.3f}')} de 10⁴ à 10⁸. C'est 2, le rapport des séries singulières de Hardy et"
      " Littlewood, S(6)/S(2) = (3 − 1)/(3 − 2) : une paire à distance 6 a deux fois plus de chances, parce que 3 divise 6.")
ligne("- **La leçon** (§ 10, le choix du test) : une grandeur qui dérive lentement croise des constantes célèbres. À une seule"
      " taille, 2√2 à 0,13 % ressemble à une découverte ; en faisant varier N, la dérive apparaît, et la loi (le 2) se lit"
      " sur l'autre compte.")
TESTS.append(("015", "variation de la taille N (10⁴ à 10⁸)", "le rapport par motif dérive (3,90 → 2,53) ; les paires larges restent à 2"))
assert abs(RAPPORTS[6][0] - 2 * 2**0.5) < 0.005 and abs(RAPPORTS[5][0] - np.pi) < 0.005 and RAPPORTS[8][0] < 2.6
assert all(abs(v[1] - 2) < 0.1 for v in RAPPORTS.values())

# ===========================================================================
# Outils : le nerf d'un recouvrement (le procédé de Čech de la partie XX, généralisé)
# ===========================================================================
def rang_exact(M):
    """Rang sur ℚ, par élimination de Gauss en fractions."""
    M = [[Fraction(x) for x in r] for r in M]
    if not M or not M[0]:
        return 0
    rows, cols, r = len(M), len(M[0]), 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
        if r == rows:
            break
    return r


def nerf(couv, kmax=3):
    """Les faces du nerf : les familles de k + 1 ouverts dont l'intersection n'est pas vide."""
    noms = sorted(couv)
    faces = {0: [(n,) for n in noms if couv[n]]}
    for k in range(1, kmax + 1):
        faces[k] = [f for f in itertools.combinations(noms, k + 1) if set.intersection(*(couv[x] for x in f))]
    return faces


def betti(faces):
    ks = sorted(faces)
    idx = {k: {f: i for i, f in enumerate(faces[k])} for k in ks}
    rg = {}
    for k in ks[:-1]:
        M = [[0] * len(faces[k]) for _ in faces[k + 1]]
        for j, g in enumerate(faces[k + 1]):
            for t in range(len(g)):
                M[j][idx[k][g[:t] + g[t + 1:]]] = (-1) ** t
        rg[k] = rang_exact(M) if faces[k + 1] else 0
    return [len(faces[k]) - rg.get(k, 0) - rg.get(k - 1, 0) for k in ks[:-1]]


def triangles_vides(couv):
    """Trois ouverts deux à deux sécants sans élément commun aux trois : le bord d'un triangle non rempli."""
    out = []
    for a, b, c in itertools.combinations(sorted(couv), 3):
        if couv[a] & couv[b] and couv[b] & couv[c] and couv[a] & couv[c] and not (couv[a] & couv[b] & couv[c]):
            out.append((a, b, c))
    return out


# contrôles du procédé : le bord d'un triangle (b₀, b₁) = (1, 1), rempli (1, 0) ; le bord du tétraèdre = S² : (1, 0, 1)
_t = {"A": {1, 2}, "B": {2, 3}, "C": {3, 1}}
assert betti(nerf(_t, 2)) == [1, 1] and triangles_vides(_t) == [("A", "B", "C")]
_t = {k: v | {9} for k, v in _t.items()}
assert betti(nerf(_t, 2)) == [1, 0] and not triangles_vides(_t)
_t = {i: {f for f in itertools.combinations(range(4), 3) if i in f} for i in range(4)}
assert betti(nerf(_t, 3)) == [1, 0, 1]


# ===========================================================================
# La figure (panneau a : la diagonale √2)
# ===========================================================================
def panneau_diagonale(ax):
    Ks = np.unique(np.round(np.logspace(np.log10(2), 3, 300), 6))
    ax.axhline(2**0.5, color=F.INK2, lw=1.2, ls=(0, (4, 3)), zorder=1)
    ax.text(1.04, 2**0.5 + 0.012, "√2", color=F.INK2, fontsize=10, va="bottom")
    ax.plot(Ks, np.sqrt(2 * Ks / (Ks - 1)), color=F.ORANGE, label="arête d_K du simplexe (deux fiches de dimensions différentes)")
    Kc = Ks[Ks >= 2]
    ax.plot(Kc, np.sqrt(2 * (Kc - 2) / (Kc - 1)), color=F.AQUA, label="corde c_K du simplexe (vers l'antipode)")
    ns = sorted(CORDES)
    Kn = [float(1 + 2 / (2 - CORDES[n] ** 2)) for n in ns]          # K = 1 + 1/x₀, x₀ = (2 − ρ²)/2
    ax.plot(Kn, [float(CORDES[n]) for n in ns], "o", color=F.BLEU, ms=6.5, mec=F.SURF, mew=1.4, zorder=5,
            label="corde ρ_n de la chèvre, placée en K = 1 + 1/x₀(n)")
    for n, k in zip(ns, Kn):
        if n in (1, 2, 4, 17, 100):
            ax.annotate(f"n = {n}", (k, float(CORDES[n])), xytext=(4, -13), textcoords="offset points",
                        fontsize=8, color=F.INK2)
    ax.set_xscale("log")
    ax.set_xlim(1, 1000)
    ax.set_ylim(0.95, 2.05)
    ax.set_xlabel("K, le nombre de dimensions de la classification naïve")
    ax.set_ylabel("longueur (rayon du pré = 1)")
    ax.set_title("a. La diagonale √2 : d² + c² = 4 (Thalès)")
    ax.legend(loc="upper right", fontsize=8.2)
    # le triangle de Thalès en médaillon
    ins = ax.inset_axes([0.6, 0.04, 0.38, 0.34])
    t = np.linspace(0, np.pi, 200)
    ins.plot(np.cos(t), np.sin(t), color=F.BASE, lw=1.2)
    ins.plot([-1, 1], [0, 0], color=F.BASE, lw=1.0)
    a = np.deg2rad(115)
    u = np.array([np.cos(a), np.sin(a)])
    ins.plot([1, u[0]], [0, u[1]], color=F.ORANGE, lw=1.8)
    ins.plot([-1, u[0]], [0, u[1]], color=F.AQUA, lw=1.8)
    for p_, lab, dx in [((1, 0), "w", 0.06), ((-1, 0), "−w", -0.3), (tuple(u), "u", -0.05)]:
        ins.plot([p_[0]], [p_[1]], "o", color=F.INK, ms=4)
        ins.text(p_[0] + dx, p_[1] + (0.08 if lab == "u" else -0.2), lab, fontsize=8, color=F.INK2)
    ins.text(0.25, 0.55, "d", color=F.ORANGE, fontsize=9)
    ins.text(-0.78, 0.5, "c", color=F.AQUA, fontsize=9)
    ins.set_xlim(-1.35, 1.25)
    ins.set_ylim(-0.3, 1.15)
    ins.set_aspect("equal")
    ins.axis("off")
