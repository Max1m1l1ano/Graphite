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
import json
import os
import re
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


def ent(n):
    return f"{n:,}".replace(",", " ")


def mpf(x, k=12):
    return mp.nstr(x, k).replace(".", ",").replace("-", "−")


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


def betti_rapide(faces):
    """Les mêmes nombres de Betti, par le rang flottant de numpy (pour les tirages du nul)."""
    ks = sorted(faces)
    idx = {k: {f: i for i, f in enumerate(faces[k])} for k in ks}
    rg = {}
    for k in ks[:-1]:
        if not faces[k + 1] or not faces[k]:
            rg[k] = 0
            continue
        M = np.zeros((len(faces[k + 1]), len(faces[k])))
        for j, g in enumerate(faces[k + 1]):
            for t in range(len(g)):
                M[j, idx[k][g[:t] + g[t + 1:]]] = (-1) ** t
        rg[k] = int(np.linalg.matrix_rank(M))
    return [len(faces[k]) - rg.get(k, 0) - rg.get(k - 1, 0) for k in ks[:-1]]


def curveball(couv, rng, echanges=400):
    """Un recouvrement tiré au hasard avec les mêmes tailles de dossiers et le même nombre de dossiers par élément
    (échanges « curveball » entre deux dossiers : Strona et al., 2014)."""
    noms = sorted(couv)
    rows = [set(couv[n]) for n in noms]
    for _ in range(echanges):
        a_, b_ = rng.choice(len(rows), 2, replace=False)
        commun = rows[a_] & rows[b_]
        A_, B_ = rows[a_] - commun, rows[b_] - commun
        if not A_ or not B_:
            continue
        pool = list(A_ | B_)
        rng.shuffle(pool)
        rows[a_], rows[b_] = commun | set(pool[:len(A_)]), commun | set(pool[len(A_):])
    return dict(zip(noms, rows))


def bloc_json(chemin, apres):
    """Le premier bloc ```json qui suit le texte `apres` dans un fichier Markdown (None s'il n'y en a pas)."""
    if not os.path.exists(chemin):
        return None
    with open(chemin, encoding="utf-8") as fh:
        t = fh.read()
    if apres not in t:
        return None
    m = re.search(r"```json\n(.*?)\n```", t[t.index(apres):], re.S)
    return json.loads(m.group(1)) if m else None


PLAN = os.path.join(REC, "revisions", "plan-001.md")
VERIF = os.path.join(REC, "revisions", "verification-croisee-001.md")
COUV = {"v1": bloc_json(PLAN, "### 1.9")["dossiers"]}
_v2 = None
if os.path.exists(VERIF):
    with open(VERIF, encoding="utf-8") as fh:
        for m_ in re.finditer(r"```json\n(.*?)\n```", fh.read(), re.S):
            try:
                j_ = json.loads(m_.group(1))
            except ValueError:
                continue
            if isinstance(j_, dict) and isinstance(j_.get("dossiers"), dict):
                _v2 = j_["dossiers"]
                break
if _v2:
    COUV["v2"] = _v2


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


ligne()
ligne("### 2.2 Après la révision : les fiches dans les dossiers")
ligne()
ligne("Chaque fiche devient un vecteur d'appartenance aux huit dossiers (une fiche peut tomber dans plusieurs). On centre,"
      " on normalise, et on compare les distances des paires qui partagent au moins un dossier (les liées) à celles des"
      " paires qui n'en partagent aucun. Deux pesées : brute, et à aires égales (chaque dossier divisé par son nombre"
      " de fiches). Le nul : 1 000 recouvrements tirés avec les mêmes tailles de dossiers et le même nombre de dossiers"
      " par fiche (curveball).")
ligne()
ligne("| recouvrement | pesée | paires liées | distance moyenne des liées | paires non liées | distance moyenne des non liées |"
      " non liées sous √2 | écart non liées − liées | p (nul) |")
ligne("|---|---|---:|---:|---:|---:|---:|---:|---:|")
NUMS = sorted(PRIM)


def separation(cf, mode):
    dos = sorted(cf)
    X = np.array([[1.0 if f in cf[d] else 0.0 for d in dos] for f in NUMS])
    garde = X.sum(1) > 0
    X = X[garde]
    Xm = X / np.maximum(X.sum(0), 1) if mode == "aires égales" else X
    Xc = Xm - Xm.mean(0)
    U = Xc / np.linalg.norm(Xc, axis=1, keepdims=True)
    D = np.sqrt(np.maximum(0, 2 - 2 * U @ U.T))
    lie = (X @ X.T) > 0
    iu = np.triu_indices(len(X), 1)
    dl, dn = D[iu][lie[iu]], D[iu][~lie[iu]]
    return dl, dn


T2 = {}
for version, c in COUV.items():
    cf = {k: set(v["fiches"]) for k, v in c.items()}
    for mode in ("brute", "aires égales"):
        dl, dn = separation(cf, mode)
        ecart = dn.mean() - dl.mean()
        rng = np.random.default_rng(7)
        nul = []
        for _ in range(1000):
            a_, b_ = separation(curveball(cf, rng), mode)
            if len(a_) and len(b_):
                nul.append(b_.mean() - a_.mean())
        pv = float(np.mean(np.array(nul) >= ecart))
        T2[(version, mode)] = (len(dl), dl.mean(), len(dn), dn.mean(), float(np.mean(dn < 2**0.5)), ecart, pv)
        ligne(f"| {version} | {mode} | {len(dl)} | {fr(dl.mean())} | {len(dn)} | {fr(dn.mean())} |"
              f" {fr(100 * np.mean(dn < 2**0.5), '{:.0f}')} % | {fr(ecart)} | {fr(pv, '{:.3f}')} |")
ligne()
t_ = T2[("v1", "brute")]
ligne(f"- **Les deux populations se séparent, mais mécaniquement.** Les paires liées sont en moyenne à {fr(t_[1])}, sous"
      f" √2 = 1,4142 ; les paires sans dossier commun sont à {fr(t_[3])}, au-dessus de √2, du côté de l'arête du"
      f" simplexe (√(16/7) = 1,5119 pour huit dossiers à parts égales).")
ligne(f"- **Le nul le montre** : p = {fr(t_[6], '{:.2f}')}. Des dossiers de mêmes tailles, tirés au hasard, séparent"
      " aussi bien. C'est la définition même d'un dossier commun qui rapproche deux fiches : cette mesure ne dit rien"
      " du contenu. Pour qu'elle parle, il faut des liens définis autrement, par exemple ceux que les agents ont"
      " trouvés par le même procédé (section 2.3).")
ligne(f"- **Des liens du cadre restent possibles.** {fr(100 * t_[4], '{:.0f}')} % des paires non liées passent sous √2"
      " en pesée brute : des fiches qui ne partagent rien, mais qui tombent dans de petits dossiers (la règle de la"
      " section 2.1, étendue aux fiches à plusieurs dossiers : P_a + P_b < Σp², où P est la somme des parts des"
      " dossiers de la fiche).")


# ===========================================================================
# 3. Le nerf des dossiers
# ===========================================================================
ligne()
ligne("## 3. Le nerf des dossiers : ce qui se recolle, et les trous")
ligne()
ligne("Un sommet par dossier ; une arête quand deux dossiers partagent un élément ; un triangle quand trois en"
      " partagent un, et ainsi de suite (le procédé de Čech de la partie XX). Trois niveaux : (1) les fiches ;"
      " (2) les fiches sans les deux hasards testés 002 et 004 ; (3) les fiches et les parties. Un **triangle vide** a"
      " ses trois côtés, mais rien de commun aux trois : c'est l'observation qui manque pour les recoller.")
ligne()


def couverture(c, niveau):
    if niveau == 1:
        return {k: set(v["fiches"]) for k, v in c.items()}
    if niveau == 2:
        return {k: set(v["fiches"]) - {"002", "004"} for k, v in c.items()}
    return {k: set(v["fiches"]) | set(v["parties"]) for k, v in c.items()}


NERF = {}
ligne("| recouvrement | niveau | sommets, arêtes, triangles, tétraèdres | Betti b₀, b₁, b₂ | triangles vides |"
      " triangles remplis : éléments communs en moyenne | nul : b₁ moyen | nul : b₂ moyen | nul : triangles vides en moyenne |"
      " p (nul ≥ observé) |")
ligne("|---|---|---|---|---:|---:|---:|---:|---:|---:|")
for version, c in COUV.items():
    for niv in (1, 2, 3):
        cv = couverture(c, niv)
        Fv = nerf(cv, kmax=len(cv) - 1)
        b = betti(Fv)
        tv = triangles_vides(cv)
        mult = np.mean([len(set.intersection(*(cv[x] for x in f))) for f in Fv[2]]) if Fv[2] else 0.0
        rng = np.random.default_rng(10 * niv + len(version))
        nb1, nb2, ntv = [], [], []
        for _ in range(1000):
            cr = curveball(cv, rng)
            Fr = nerf(cr, kmax=3)
            br = betti_rapide(Fr)
            nb1.append(br[1])
            nb2.append(br[2])
            ntv.append(len(triangles_vides(cr)))
        pv = float(np.mean(np.array(ntv) >= len(tv)))
        creux = [q for q in itertools.combinations(sorted(cv), 4)
                 if all(set.intersection(*(cv[x] for x in t3)) for t3 in itertools.combinations(q, 3))
                 and not set.intersection(*(cv[x] for x in q))]
        NERF[(version, niv)] = dict(b=b, tv=tv, mult=mult, nb1=float(np.mean(nb1)), nb2=float(np.mean(nb2)),
                                    pb2=float(np.mean(np.array(nb2) >= b[2])), ntv=float(np.mean(ntv)), p=pv,
                                    creux=creux, faces=[len(Fv[k]) for k in range(4)])
        ligne(f"| {version} | {niv} | {', '.join(str(len(Fv[k])) for k in range(4))} | {', '.join(str(x) for x in b[:3])} |"
              f" {len(tv)} | {fr(mult, '{:.1f}')} | {fr(np.mean(nb1), '{:.2f}')} | {fr(np.mean(nb2), '{:.2f}')} |"
              f" {fr(np.mean(ntv), '{:.1f}')} | {fr(pv, '{:.3f}')} |")
ligne()
for version in COUV:
    tv1 = NERF[(version, 1)]["tv"]
    tv3 = set(NERF[(version, 3)]["tv"])
    tv2 = set(NERF[(version, 2)]["tv"])
    recueil = [t for t in tv1 if t not in tv3]
    corpus = [t for t in tv1 if t in tv3]
    hasard = [t for t in tv2 if t not in set(tv1)]
    ligne(f"**{version} : les triangles vides au niveau des fiches** ({len(tv1)}) :")
    for t in tv1:
        nature = "trou du corpus (vide aussi avec les parties)" if t in tv3 else "trou du recueil (une partie les réunit, la fiche manque)"
        ligne(f"- {' · '.join(t)} : {nature}.")
    if hasard:
        ligne(f"- En retirant les deux hasards testés, {len(hasard)} triangle(s) se vident en plus : "
              + " ; ".join(' · '.join(t) for t in hasard) + ". Un hasard testé y tenait la place d'une observation de structure.")
    ligne(f"- Bilan {version} : {len(recueil)} trous du recueil, {len(corpus)} trous du corpus.")
    n1 = NERF[(version, 1)]
    ligne(f"- Les fiches laissent {len(tv1)} triangles vides, contre {fr(n1['ntv'], '{:.1f}')} en moyenne pour des dossiers"
          f" de mêmes tailles tirés au hasard (p = {fr(n1['p'], '{:.2f}')}) : un peu plus que le hasard, sans plus. Les trous"
          " se lisent donc un par un, comme des pistes, pas comme une preuve.")
    n3 = NERF[(version, 3)]
    ligne(f"- **Avec les parties (niveau 3), les boucles se remplissent** (b₁ = {n3['b'][1]}), mais il reste"
          f" b₂ = {n3['b'][2]} cavités (nul : {fr(n3['nb2'], '{:.2f}')} en moyenne, p = {fr(n3['pb2'], '{:.3f}')}). Une"
          f" cavité, ce sont quatre dossiers dont les quatre triplets se recollent, sans élément commun aux quatre :"
          f" un trou d'un étage plus haut. Les {len(n3['creux'])} tétraèdres creux :")
    for q in n3["creux"]:
        ligne(f"  - {' · '.join(q)}")
    ligne()


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
    ligne(f"| 10^{E} | {ent(six)} | {ent(deux)} | {ent(quatre)} | {fr(rap)} | {fr(larges)} |")
DERIVE = []
for E in np.arange(3.5, 8.01, 0.125):
    M_ = int(round(10**E / 10)) * 10
    Dz = crible[:M_].reshape(-1, 10)
    u1, u3, u7, u9 = Dz[:, 1], Dz[:, 3], Dz[:, 7], Dz[:, 9]
    six = int(np.sum(u1 & ~u3 & u7 & ~u9)) + int(np.sum(~u1 & u3 & ~u7 & u9))
    autres = sum(int(np.sum(m_)) for m_ in (u1 & u3 & ~u7 & ~u9, ~u1 & ~u3 & u7 & u9, ~u1 & u3 & u7 & ~u9, u1 & ~u3 & ~u7 & u9))
    larg = (int(np.sum(u1 & u7)) + int(np.sum(u3 & u9))) / (int(np.sum(u1 & u3)) + int(np.sum(u7 & u9)))
    DERIVE.append((M_, (six / 2) / (autres / 4), larg))
del crible
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
TESTS.append(("015", "variation de la taille N (10⁴ à 10⁸)",
              f"le rapport par motif dérive ({fr(RAPPORTS[4][0], '{:.2f}')} → {fr(RAPPORTS[8][0], '{:.2f}')}) ; les paires larges restent à 2"))
assert abs(RAPPORTS[6][0] - 2 * 2**0.5) < 0.005 and abs(RAPPORTS[5][0] - np.pi) < 0.005 and RAPPORTS[8][0] < 2.6
assert all(abs(v[1] - 2) < 0.1 for v in RAPPORTS.values())


# --- 4.3 K3 : la famille b = q² + 1 ----------------------------------------------------------------------------------
def est_premier(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True


def ordre_mult(a, p):
    o, x = 1, a % p
    while x != 1:
        x = (x * a) % p
        o += 1
    return o


ligne()
ligne("### 4.3 K3 : la famille b = q² + 1 explique le cas (10, 7) (plan, § 3.2)")
ligne()
ligne("Pour q premier, on pose b = q² + 1 et p = q² − q + 1. Quatre propriétés se vérifient pour tout q :"
      " q² ≡ −1 (mod b), donc q est le i de la base b ; q·p ≡ 1 (mod b), donc q est l'inverse de p ; p − 1 = q(q − 1) = φ(b − 1) ;"
      " et p divise q³ + 1 = (q + 1)·p, donc la période de 1/p en base b divise 6.")
ligne()
ligne("| q | b = q² + 1 | p = q² − q + 1 | p premier ? | q² mod b | q·p mod b | φ(b − 1) | période de 1/p en base b | chiffres = unités mod b − 1 ? |")
ligne("|---:|---:|---:|---|---:|---:|---:|---:|---|")
K3 = []
for q in [2, 3, 5, 7, 11, 13, 17, 19]:
    b, p_ = q * q + 1, q * q - q + 1
    pr = est_premier(p_)
    per = ordre_mult(b, p_) if pr and b % p_ else None
    U = {u for u in range(1, b - 1) if np.gcd(u, b - 1) == 1}
    egal = pr and set(chiffres_periode(p_, b)) == U
    K3.append((q, b, p_, pr, per, egal))
    assert (q * q) % b == b - 1 and (q * p_) % b == 1 and p_ - 1 == len(U)
    ligne(f"| {q} | {b} | {p_} | {'oui' if pr else 'non'} | {(q * q) % b} (= −1) | {(q * p_) % b} | {len(U)} |"
          f" {per if per else '—'} | {'oui' if egal else 'non'} |")
ligne()
ligne("- La période remplit tout le groupe des unités seulement si q(q − 1) ≤ 6, soit q = 2 (b = 5, p = 3) et q = 3"
      " (b = 10, p = 7) : exactement les deux cas non triviaux du balayage 4.1. Au-delà, p reste premier pour q = 7"
      " (b = 50, p = 43) et q = 13 (b = 170, p = 157), mais la période vaut 6.")
ligne("- **Ce qui se recolle** : le 3 de la fiche 013 (l'inverse de 7 modulo 10) et le 3 de la partie XIX (3 ≡ i modulo"
      " 10, l'aiguille de pente i) sont le même 3. La fiche 013 et la partie XIX se recollent par la famille q² + 1.")
assert [x[0] for x in K3 if x[5]] == [2, 3] and all(x[4] == 6 for x in K3 if x[3] and x[0] >= 3)
TESTS.append(("013 et XIX", "la famille b = q² + 1 (q premier jusqu'à 19)", "q = 2 et 3 seulement ; ailleurs période 6"))


# --- 4.4 T3 et K10 : le ménisque x²/6, ordre par ordre ; le seuil du centre --------------------------------------------
import sympy as sp  # noqa: E402

ligne()
ligne("### 4.4 T3 : la chèvre et le polygone, ordre par ordre (K1), et le seuil du centre du Venn (K10)")
ligne()
nn, ss, xx = sp.symbols("n s x", positive=True)
MU = {2: sp.Rational(2, 3), 3: sp.Rational(-98, 15), 4: sp.Rational(5966, 105), 5: sp.Rational(-1698106, 2835),
      6: sp.Rational(247172734, 31185)}        # resultats/tiers_dimension.md, § 2
chevre = sum(c * nn**(-j) for j, c in MU.items())
defaut = 1 - sp.sin(xx) / xx                          # la lumière qui manque au polygone inscrit, x = 2π/N
poly = sp.series(defaut.subs(xx, 2 / (nn + ss)), nn, sp.oo, 7).removeO()
coef = {j: sp.simplify(sp.expand(poly).coeff(nn, -j)) for j in range(2, 7)}
s3 = sp.solve(sp.Eq(coef[3], MU[3]), ss)[0]
ligne("On écrit la lumière qui manque au polygone inscrit à N côtés, 1 − sin(x)/x = x²/6 − x⁴/120 + …, avec x = 2π/N et"
      " N = π(n + s) : l'ordre 2 donne exactement le 2/(3n²) de la chèvre (le facteur π est imposé). Il reste le décalage s.")
ligne()
ligne("| ordre | chèvre μ_j | polygone, s = 0 | polygone, s qui recolle l'ordre 3 |")
ligne("|---:|---:|---:|---:|")
for j in range(2, 7):
    ligne(f"| 1/n^{j} | {MU[j]} ({fr(float(MU[j]), '{:.4g}')}) | {sp.nsimplify(coef[j].subs(ss, 0))} |"
          f" {fr(float(coef[j].subs(ss, s3)), '{:.4g}')} |")
ligne()
ligne(f"- L'ordre 3 se recolle pour s = {s3} : la chèvre et le polygone ont la même forme x²/6, et un décalage d'environ"
      f" cinq dimensions rattrape l'ordre suivant. L'ordre 4 ne se recolle plus : {fr(float(coef[4].subs(ss, s3)), '{:.2f}')}"
      f" contre {fr(float(MU[4]), '{:.2f}')}.")
ligne("- **Verdict** : le même exposant et le même 1/6, pas le même ménisque. Les deux séries n'ont pas la même nature :"
      " celle de la chèvre diverge (rapports μ_(j+1)/μ_j ≈ −j·2/ln 2, partie XXIV), celle du sinus converge partout."
      " L'obstruction est d'ordre 4 dès qu'on autorise un décalage, d'ordre 3 sans décalage. Elle désigne l'asymétrie"
      " de la coquille (partie XXIV, § 1), qu'un polygone à un seul rayon n'a pas.")
assert s3 == sp.Rational(49, 10) and coef[2].subs(ss, 0) == MU[2] and abs(float(coef[4].subs(ss, s3) - MU[4])) > 5
ligne()
ligne("**K10, le seuil du centre du Venn** (partie XXX, § 6.4). Le centre demande W_c = (2/π)·√(n(2ⁿ − 2)) pixels, le"
      " reste W_r = 4·√((2ⁿ − 2)/π). Leur rapport vaut exactement √(n/(4π)) : le centre devient le goulot à n* = 4π.")
Vn = 2**nn - 2
rapport = sp.simplify((2 / sp.pi * sp.sqrt(nn * Vn)) / (4 * sp.sqrt(Vn / sp.pi)))
assert sp.simplify(rapport - sp.sqrt(nn / (4 * sp.pi))) == 0
n_poly = float(sp.pi / sp.atan(sp.Rational(1, 4)))
ligne(f"- **Pourquoi 4π.** Le centre doit loger n croisements à 2 px l'un de l'autre sur un cercle : son périmètre vaut"
      f" L = 2n. Il doit aussi loger n régions d'au moins 2 × 2 px : son aire vaut A = 4n. Pour un cercle, L²/A = 4π (la"
      f" constante isopérimétrique), d'où 4n² = 4π·4n, soit n* = 4π = {fr(4 * np.pi, '{:.3f}')}.")
ligne(f"- **Avec des segments.** Si les n croisements du centre sont joints par des segments, le centre est un"
      f" n-gone régulier, dont la constante isopérimétrique vaut 4n·tan(π/n). Le seuil devient tan(π/n*) = 1/4, soit"
      f" n* = π/arctan(1/4) = {fr(n_poly, '{:.3f}')}. Dans les deux cas, le centre devient le goulot dès 13 courbes.")
ligne("- **Ce qui se recolle** : n·tan(π/n) est exactement la quantité de la fiche 003 (34·tan(π/34) ≈ π). Le seuil du"
      " centre du Venn et le polygone circonscrit des éventails de Perron sont la même constante isopérimétrique.")
assert abs(n_poly - 12.8240) < 1e-3
TESTS.append(("011 et 003", "le seuil du centre : cercle contre n-gone",
              f"4π = {fr(4 * np.pi, '{:.3f}')} et π/arctan(1/4) = {fr(n_poly, '{:.3f}')} : 13 courbes dans les deux cas"))


# --- 4.5 T7 : les trois 4/3 ----------------------------------------------------------------------------------------------
ligne()
ligne("### 4.5 T7 : les trois 4/3 (K8)")
ligne()
fen, prec = [], None
for b in range(3, 10**6 + 1):
    c2 = int(np.floor(np.log2(b - 0.5))) + 1    # 1, 2, 4, … < b
    c3 = int(np.floor(np.log(b - 0.5) / np.log(3))) + 1
    ok = 3 * c2 == 4 * c3
    if ok and prec != b - 1:
        fen.append([b, b])
    if ok:
        fen[-1][1] = b
        prec = b
ligne("On compte, pour chaque base b de 3 à 10⁶, les puissances de 2 et de 3 inférieures à b (1 compris). En base 10 :"
      " 1, 2, 4, 8 et 1, 3, 9, soit 4 et 3.")
ligne()
ligne("- Le rapport vaut 4/3 sur " + " et ".join(f"b = {a} à {z}" for a, z in fen)
      + " seulement. Ensuite il tend vers log₂ 3 = 1,585 (le rapport du comma pythagoricien de la partie XX).")
ligne("- V₃/V₂ = 4/3 est un pas de Wallis (partie III) : la suite V_(n+1)/V_n tend vers 0. Le 4/3 de 1/x₀ = n + 4/3"
      " (partie XXIV) est une constante de la série de la corde (1 pour le simplexe, 1/3 pour le ménisque).")
ligne("- **Verdict** : trois procédés différents donnent la même valeur pour de petits nombres. C'est une coïncidence"
      " de petits entiers, répliquée nulle part ailleurs ; le lien qui reste passe par log₂ 3 et les réduites de"
      " l'arbre P6 (19/12, le comma).")
assert fen == [[10, 16], [244, 256]]
TESTS.append(("recueil (4/3)", "les bases de 3 à 10⁶", "4/3 seulement pour " + " et ".join(f"b = {a} à {z}" for a, z in fen)))


# --- 4.6 T6 : Midy en Perron, la tour 2-adique des périodes ------------------------------------------------------------------
def v_ell_ordre(a, p, ell):
    """Valuation ℓ-adique de l'ordre de a modulo p, sans calculer l'ordre."""
    e, m = 0, p - 1
    while m % ell == 0:
        m //= ell
        e += 1
    x = pow(a, m, p)
    k = 0
    while x != 1:
        x = pow(x, ell, p)
        k += 1
    return k


ligne()
ligne("### 4.6 T6 : Midy en Perron, la tour 2-adique des périodes (K9)")
ligne()
ligne("La période de 1/p en base 10 est l'ordre L(p) de 10 modulo p. Midy demande L pair ; Midy étendu à ℓ blocs demande"
      " ℓ | L. On mesure, pour les premiers p < N (sauf 2 et 5), la part des v₂(L) = 0, 1, 2, 3… (la tour 2-adique)"
      " et la part des ℓ | L.")
ligne()
PREM6 = [q for q in premiers(10**6)]
ligne("| base | N | L pair | v₂ = 0 | v₂ = 1 | v₂ = 2 | v₂ = 3 | 3 \| L | 5 \| L | 7 \| L |")
ligne("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
TOUR = {}
for base in (10, 2, 3, 7, 12):
    for Nb in (10**3, 10**4, 10**5, 10**6):
        ps = [q for q in PREM6 if q < Nb and base % q]
        v2 = np.array([v_ell_ordre(base, q, 2) for q in ps])
        l3 = np.mean([v_ell_ordre(base, q, 3) > 0 for q in ps])
        l5 = np.mean([v_ell_ordre(base, q, 5) > 0 for q in ps])
        l7 = np.mean([v_ell_ordre(base, q, 7) > 0 for q in ps])
        TOUR[(base, Nb)] = (np.mean(v2 > 0), [np.mean(v2 == k) for k in range(4)], l3, l5, l7)
        if base == 10 or Nb == 10**6:
            t = TOUR[(base, Nb)]
            ligne(f"| {base} | 10^{int(np.log10(Nb))} | {fr(t[0])} | " + " | ".join(fr(x) for x in t[1])
                  + f" | {fr(l3)} | {fr(l5)} | {fr(l7)} |")
ligne()
t = TOUR[(10, 10**6)]
ligne(f"- **La tour se divise par deux.** En base 10 sous 10⁶ : v₂(L) = 0, 1, 2, 3 pour {', '.join(fr(x, '{:.3f}') for x in t[1])}"
      " des premiers. Au-delà du premier étage, chaque étage garde à peu près la moitié du précédent (1/3, 1/3, 1/6,"
      " 1/12 attendus) : un arbre de Perron sur les périodes, dont les fentes se referment de moitié à chaque étage.")
ligne(f"- **Les aires ne sont pas égales.** La part des périodes paires vaut {fr(t[0], '{:.4f}')} en base 10 (2/3 = 0,6667,"
      f" Hasse, 1966) et {fr(TOUR[(2, 10**6)][0], '{:.4f}')} en base 2 (17/24 = 0,7083). Le « Venn de Midy » de l'auteur"
      " est donc un Venn à aires inégales par nature : deux tiers pour les périodes paires, un tiers pour les impaires.")
t2 = TOUR[(2, 10**6)][1]
ligne(f"- **La base 2 a sa propre tour** : {', '.join(fr(x, '{:.3f}') for x in t2)} pour v₂ = 0 à 3. L'étage 2 y est"
      " plus lourd parce que 2 est un carré modulo p exactement quand p ≡ ±1 (mod 8) : c'est de là que vient le 17/24 de"
      " Hasse. Les bases 3, 7, 10 et 12 suivent la tour générique.")
ligne(f"- **Midy étendu.** La part des ℓ | L vaut {fr(t[2], '{:.3f}')}, {fr(t[3], '{:.3f}')} et {fr(t[4], '{:.3f}')} pour"
      " ℓ = 3, 5, 7, contre ℓ/(ℓ² − 1) = 0,375, 0,208 et 0,146 pour une base générique (valeurs attendues ; à confirmer"
      " dans la littérature sur la conjecture d'Artin).")
assert abs(t[0] - 2 / 3) < 0.01 and abs(TOUR[(2, 10**6)][0] - 17 / 24) < 0.01
assert abs(t[1][0] - 1 / 3) < 0.01 and abs(t[1][2] - 1 / 6) < 0.01 and abs(t[1][3] - 1 / 12) < 0.01
TESTS.append(("recueil (Midy)", "la tour 2-adique, bornes 10³ à 10⁶, bases 2, 3, 7, 10, 12", "2/3 pair en base 10, 17/24 en base 2 ; 1/3, 1/3, 1/6, 1/12"))


# --- 4.7 T5 : la moitié de Kakeya fini, en caractéristique 2 ------------------------------------------------------------
from scipy.optimize import Bounds, LinearConstraint, milp  # noqa: E402
from scipy.sparse import lil_matrix  # noqa: E402

IRRED = {4: (2, [1, 1, 1]), 8: (2, [1, 1, 0, 1]), 9: (3, [1, 0, 1]), 16: (2, [1, 1, 0, 0, 1]), 27: (3, [1, 2, 0, 1])}
# polynômes unitaires, coefficients du degré 0 au degré k : x²+x+1, x³+x+1, x²+1, x⁴+x+1, x³+2x+1

def corps(q):
    """Tables d'addition et de multiplication de F_q (éléments codés 0..q-1 en base p)."""
    if q in IRRED:
        p, f = IRRED[q]
        k = len(f) - 1
    else:
        p, k, f = q, 1, None
    def dec(a):
        return [(a // p**i) % p for i in range(k)]
    def enc(v):
        return sum(c * p**i for i, c in enumerate(v))
    add = np.zeros((q, q), int); mul = np.zeros((q, q), int)
    for a in range(q):
        for b in range(q):
            va, vb = dec(a), dec(b)
            add[a, b] = enc([(x + y) % p for x, y in zip(va, vb)])
            if f is None:
                mul[a, b] = (a * b) % p
            else:
                prod = [0] * (2 * k - 1)
                for i, x in enumerate(va):
                    for j, y in enumerate(vb):
                        prod[i + j] = (prod[i + j] + x * y) % p
                for d in range(2 * k - 2, k - 1, -1):       # réduction par f (unitaire)
                    c = prod[d]
                    if c:
                        for i in range(k + 1):
                            prod[d - k + i] = (prod[d - k + i] - c * f[i]) % p
                mul[a, b] = enc(prod[:k])
    return add, mul

def verifie_corps(q, add, mul):
    # chaque élément non nul a un inverse ; distributivité sur un échantillon
    for a in range(1, q):
        assert any(mul[a, b] == 1 for b in range(1, q)), (q, a)
    for a, b, c in itertools.product(range(q), repeat=3):
        assert mul[a, add[b, c]] == add[mul[a, b], mul[a, c]]

def minimum_kakeya_fq(q, limite=120):
    add, mul = corps(q)
    verifie_corps(q, add, mul)
    lignes = []
    for m in range(q):
        for c in range(q):
            if m == 0 and c != 0:
                continue
            if m == 1 and c not in (0, 1):
                continue
            lignes.append((m, [(x, add[mul[m, x], c]) for x in range(q)]))
    lignes.append(("inf", [(0, y) for y in range(q)]))
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
        lb.append(1); ub.append(1); r += 1
    for j, (_, l) in enumerate(lignes):
        for p in l:
            A[r, idx[p]] = 1; A[r, nP + j] = -1
            lb.append(0); ub.append(np.inf); r += 1
    res = milp(np.r_[np.ones(nP), np.zeros(nL)], constraints=LinearConstraint(A.tocsr()[:r], lb, ub),
               integrality=np.ones(nP + nL), bounds=Bounds(0, 1), options={"time_limit": limite})
    y = np.round(res.x[nP:]).astype(int)
    # multiplicités des points couverts
    mult = np.zeros(nP, int)
    for j, (_, l) in enumerate(lignes):
        if y[j]:
            for p in l:
                mult[idx[p]] += 1
    return round(res.fun), res.status, np.bincount(mult[mult > 0])


ligne()
ligne("### 4.7 T5 : la moitié de Kakeya fini, en caractéristique 2 (K4)")
ligne()
ligne("La partie XIV a trouvé qu'un ensemble de Kakeya du plan F_q² (une droite entière dans chacune des q + 1 directions)"
      " occupe environ la moitié du plan, et l'a expliqué par les carrés modulo q : l'involution x ↦ −x. En"
      " caractéristique 2, cette involution est l'identité. On calcule donc le minimum exact dans les corps F_q, q = 2,"
      " 3, 4, 5, 7, 8, 9 (tables d'addition et de multiplication construites par des polynômes irréductibles), avec les"
      " symétries de la partie XIV, et on compte dans l'ensemble trouvé les points couverts 1, 2 ou 3 fois.")
ligne()
ligne("| q | caractéristique | minimum (calculé) | q(q + 1)/2 | excès | points simples | doubles | triples | durée |")
ligne("|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
KAKF = {}
for q in [2, 3, 4, 5, 7, 8, 9]:
    t0 = time.time()
    mini, statut, bc = minimum_kakeya_fq(q)
    bc = list(bc) + [0] * (4 - len(bc))
    KAKF[q] = (mini, statut, bc)
    car = 2 if q in (2, 4, 8) else 3 if q in (3, 9) else q
    ligne(f"| {q} | {car} | {mini} | {q * (q + 1) // 2} | {mini - q * (q + 1) // 2} | {bc[1]} | {bc[2]} | {bc[3]} |"
          f" {fr(time.time() - t0, '{:.1f}')} s |")
ligne()
ligne("- **L'identité exacte.** Les q + 1 droites se coupent deux à deux en un seul point. En comptant chaque point avec"
      " sa multiplicité m_P (le nombre de droites qui y passent), 1 = m − C(m, 2) + C(m − 1, 2) pour tout m ≥ 1. On en"
      " tire |K| = q(q + 1) − C(q + 1, 2) + Σ C(m_P − 1, 2) = q(q + 1)/2 + Σ C(m_P − 1, 2).")
ligne("- **La moitié vient de l'inclusion–exclusion**, tronquée à l'ordre 2 : c'est l'inégalité de Bonferroni"
      " |∪L| ≥ Σ|L| − Σ|L ∩ L′|, vraie dans toutes les caractéristiques. Elle est atteinte pour q = 2, 4, 8 : tous les"
      " points sont doubles, aucun n'est triple.")
ligne("- **La parité ne compte que l'excès.** Pour q impair, le minimum dépasse la borne de (q − 1)/2, et l'ensemble"
      " optimal a exactement (q − 1)/2 points triples (Blokhuis et Mazzocca pour le minimum). Pour q pair, l'excès est"
      " nul. Les carrés modulo q (l'involution) n'expliquent donc que l'excès, pas la moitié.")
ligne("- **Verdict.** La piste XIV–XX de la carte (partie XXVII, § 9) se ferme par une obstruction : la moitié de Kakeya"
      " fini et celle des hémisphères ne viennent pas du même procédé. Un autre lien s'ouvre : l'inégalité de"
      " Bonferroni, tronquée à l'ordre 1, est la correction de Bonferroni de la fiche 012 ; tronquée à l'ordre 2, elle"
      " donne la moitié de Kakeya fini. Même procédé : tronquer l'inclusion–exclusion.")
for q, (mini, statut, bc) in KAKF.items():
    assert statut == 0
    attendu = q * (q + 1) // 2 + (0 if q % 2 == 0 else (q - 1) // 2)
    assert mini == attendu and bc[3] == (0 if q % 2 == 0 else (q - 1) // 2), (q, mini, bc)
TESTS.append(("XIV et 012", "Kakeya dans F_q, q = 2 à 9", "q(q + 1)/2 exactement pour q pair ; + (q − 1)/2 points triples pour q impair"))


# --- 4.8 T4 : le dipôle du centre de la lumière, la palette, l'ordre de dessin ou le seuil ? ------------------------------
from scipy.stats import spearmanr  # noqa: E402

IMG_P = "/home/user/dzoba/venn17/images/venn17-pressure-dark-2000.png"   # copie locale du dépôt de Dzoba (CC BY 4.0)
C_SYM = (999.497, 999.499)                                              # resultats/centre_venn.md, § 1
ligne()
ligne("### 4.8 T4 : le centre de la lumière se déplace par la palette, par l'ordre de dessin ou par le seuil ? (K6)")
ligne()
if not os.path.exists(IMG_P):
    ligne(f"L'image `{IMG_P}` est absente : ce test demande une copie du dépôt dzoba/venn17 (comme les parties XXIX et XXX).")
else:
    from PIL import Image  # noqa: E402
    S8 = np.asarray(Image.open(IMG_P).convert("RGB"))
    lin = S8.astype(float) / 255
    lin = np.where(lin <= 0.04045, lin / 12.92, ((lin + 0.055) / 1.055) ** 2.4)
    l_ = np.cbrt(0.4122214708 * lin[..., 0] + 0.5363325363 * lin[..., 1] + 0.0514459929 * lin[..., 2])
    m_ = np.cbrt(0.2119034982 * lin[..., 0] + 0.6806995451 * lin[..., 1] + 0.1073969566 * lin[..., 2])
    s_ = np.cbrt(0.0883024619 * lin[..., 0] + 0.2817188376 * lin[..., 1] + 0.6299787005 * lin[..., 2])
    Lk = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_
    Ak = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    Bk = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
    del l_, m_, s_, lin
    fondL = float(np.median(Lk[:20, :20]))
    yy_, xx_ = np.mgrid[0:Lk.shape[0], 0:Lk.shape[1]]
    zz = (xx_ - C_SYM[0]) + 1j * (C_SYM[1] - yy_)
    del yy_, xx_
    Ck = np.hypot(Ak, Bk)
    teinte = np.degrees(np.arctan2(Bk, Ak)) % 360
    hcent = (25 + 360 * np.arange(17) / 17) % 360          # les teintes de la palette (plotter_svg.py, lu)
    dd = (teinte[..., None] - hcent + 180) % 360 - 180
    cls = np.argmin(np.abs(dd), -1)
    dmin = np.take_along_axis(np.abs(dd), cls[..., None], -1)[..., 0]
    del dd, Ak, Bk, teinte
    OM17 = np.exp(2j * np.pi * np.arange(17) / 17)
    rng = np.random.default_rng(1)
    ligne("On classe chaque pixel d'encre (clarté L > fond + 0,1) par sa teinte OKLab, au plus près des 17 teintes"
          " h_i = 25° + 360°·i/17 de la palette du traceur, et on mesure pour chaque classe son aire visible A_i et son"
          " moment M_i = Σ (z − c) autour du centre de symétrie c.")
    ligne()
    ligne("| chroma minimal | pixels classés | étendue des phases de M_i, rotation retirée | premier harmonique des aires A_i |"
          " meilleure montée cyclique des A_i (Spearman) | p (2 000 permutations) |")
    ligne("|---:|---:|---:|---:|---:|---:|")
    T4 = {}
    for seuilC in (0.04, 0.06):
        classe = (Lk > fondL + 0.1) & (Ck > seuilC) & (dmin < 6)
        Ai = np.array([(classe & (cls == i)).sum() for i in range(17)])
        Mi = np.array([zz[classe & (cls == i)].sum() for i in range(17)])
        phases = np.degrees(np.ptp(np.unwrap(np.angle(Mi * np.conj(OM17)))))
        h1 = abs((Ai * OM17).sum()) / Ai.sum()
        rho = max(spearmanr(np.arange(17), np.roll(Ai, -k))[0] for k in range(17))
        nul = [max(spearmanr(np.arange(17), np.roll(pp, -k))[0] for k in range(17))
               for pp in (rng.permutation(Ai) for _ in range(2000))]
        pv = float(np.mean(np.array(nul) >= rho))
        T4[seuilC] = (int(classe.sum()), phases, h1, rho, pv)
        ligne(f"| {fr(seuilC, '{:.2f}')} | {ent(int(classe.sum()))} |"
              f" {fr(phases, '{:.1f}')}° | {fr(100 * h1, '{:.1f}')} % | {fr(rho, '{:.2f}')} | {fr(pv, '{:.2f}')} |")
    ligne()
    ligne("- **Les couleurs suivent les courbes.** Une fois la rotation de 2π·i/17 retirée, les phases des 17 moments ne"
          " s'étalent que de quelques degrés : la classe de teinte i est bien la courbe i, et les teintes tournent dans"
          " l'ordre des rotations.")
    ligne("- **Pas de signature d'ordre de dessin.** Si les courbes étaient dessinées de 0 à 16, la dernière couvrant les"
          " autres à chaque croisement, l'aire visible monterait le long d'un tour. La meilleure montée cyclique reste"
          " dans le nul des permutations, et le profil des A_i change avec le chroma minimal : il mesure surtout"
          " l'efficacité du classement selon la teinte.")
    ligne()
    ligne("**Le seuil, seconde cause.** Un masque binaire donne le même poids à tout pixel d'encre : il ne voit ni la"
          " palette (aucun poids) ni l'ordre de dessin (aux croisements, l'encre reste de l'encre). Pourtant son centre"
          " bouge avec le seuil de clarté :")
    ligne()
    ligne("| masque L > fond + t | pixels | écart au centre de symétrie | direction (°, y vers le haut) |")
    ligne("|---:|---:|---:|---:|")
    MASQ = []
    for t_ in (0.02, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4):
        mm = Lk > fondL + t_
        bb = zz[mm].mean()
        MASQ.append((t_, int(mm.sum()), abs(bb), np.degrees(np.angle(bb))))
        ligne(f"| {fr(t_, '{:.2f}')} | {ent(int(mm.sum()))} | {fr(abs(bb), '{:.2f}')} px | {fr(np.degrees(np.angle(bb)), '{:.0f}')} |")
    ligne()
    ligne(f"- L'écart passe de {fr(MASQ[0][2], '{:.2f}')} px (presque toute l'encre) à {fr(MASQ[-1][2], '{:.1f}')} px (les seuls"
          " cœurs des traits les plus clairs), dans une direction stable vers −130°. Plus le seuil est haut, plus il ne"
          " garde que les courbes claires : le seuil transforme la couleur en largeur visible, par l'anticrénelage des bords.")
    ligne("- **Verdict.** La cause unique « le premier harmonique des poids » ne suffit pas (K6), mais la seconde cause"
          " n'est pas l'ordre de dessin : c'est le seuil. La couleur déplace le centre par deux canaux, le poids (la"
          " pesée) et la largeur visible au-dessus d'un seuil. La phrase de la partie XXX, « tout écart vient des poids »,"
          " devient « tout écart vient de la couleur, par le poids et par le seuil » ; la géométrie reste symétrique.")
    ligne("- **Le lien avec le sujet d'étude.** Restreindre le cadre (monter le seuil) fabrique un déplacement qui"
          " n'est pas dans la géométrie, comme le partage inégal des aires fabrique des liens (section 2.1). En"
          " astrométrie, c'est la différence entre un centroïde isophote (au-dessus d'un seuil) et un centroïde pondéré"
          " (Bertin et Arnouts, SExtractor, 1996), et la raison des corrections de chromaticité des catalogues.")
    assert T4[0.04][1] < 10 and T4[0.04][4] > 0.05 and T4[0.06][4] > 0.05
    assert MASQ[0][2] < 0.5 and MASQ[-1][2] > 20 and all(-140 < m_[3] < -120 for m_ in MASQ[2:])
    # --- 4.9 la question de l'auteur : quel masque, quel seuil, et que vaut 0,37 px ? -------------------------------
    ligne()
    ligne("### 4.9 Le masque binaire : de quoi, où, et ce que vaut 0,37 px (question de l'auteur)")
    ligne()
    coin = S8[:20, :20].reshape(-1, 3)
    vals_, cnt_ = np.unique(coin, axis=0, return_counts=True)
    FOND_RGB = tuple(int(v) for v in vals_[np.argmax(cnt_)])
    bord = np.concatenate([S8[:50].reshape(-1, 3), S8[-50:].reshape(-1, 3), S8[:, :50].reshape(-1, 3), S8[:, -50:].reshape(-1, 3)])
    part_fond = float(np.mean(np.all(bord == np.array(FOND_RGB, np.uint8), axis=1)))
    ligne(f"- **L'image** : `{os.path.basename(IMG_P)}` (dépôt de Dzoba, copie locale ; c'est l'image de son README, celle des"
          f" parties XXIX et XXX), {S8.shape[1]} × {S8.shape[0]} pixels, trois canaux de 8 bits non signés (0 à 255,"
          f" type `{S8.dtype}`). Le fond est une couleur exacte, RGB = {FOND_RGB} : un gris bleuté ({fr(100 * part_fond, '{:.1f}')} %"
          " des pixels des bandes de 50 px au bord).")
    ligne(f"- **Le seuil, de quoi** : de la clarté perçue OKLab L (0 = noir, 1 = blanc), calculée pixel par pixel à partir des"
          f" trois canaux. Le fond vaut L = {fr(fondL, '{:.4f}')} (médiane du coin 20 × 20). Le masque est l'ensemble des pixels"
          " où L > fond + t : chacun pèse 1, les autres 0. Son centre est la moyenne des positions de ses pixels ; on le"
          " compare au centre de symétrie d'ordre 17, (999,497 ; 999,499), connu à 0,003 px (partie XXX, § 1).")
    ligne("- **Où** : partie XXX ([centre-venn.md](../centre-venn.md), § 1, la deuxième des six pesées, « masque de clarté"
          " OKLab (L > fond + 0,1) » ; § 2, la mesure de la moitié avec le même seuil) ; script `scripts/centre_venn.py`"
          " (section 1, liste `POIDS` ; fonction `mesure_moitie`, `seuil=0.1`) ; balayage du seuil : `scripts/revision_001.py`,"
          " sections 4.8 et 4.9 ; figure `rev001_diagonale_cadre.png`, panneau c ; fiche 018. La partie XXIX utilisait un"
          " autre masque binaire, sur la moyenne des canaux : moyenne RGB > fond + 25.")
    ligne()
    hR = np.bincount(S8[..., 0].ravel(), minlength=256)
    hB = np.bincount(S8[..., 2].ravel(), minlength=256)
    rap = lambda h_, k: h_[k + 1] / h_[k]  # noqa: E731
    sauts = [abs(np.log(rap(h_, 127)) - np.median([np.log(rap(h_, k)) for k in range(110, 145) if k != 127])) for h_ in (hR, hB)]
    ligne(f"**Signé ou non signé ?** Un passage par des octets signés (−128 à 127) replierait les valeurs au-delà de 127 :"
          f" l'histogramme des canaux sauterait entre 127 et 128. Il est lisse (rouge : {ent(int(hR[127]))} puis {ent(int(hR[128]))} ;"
          f" bleu : {ent(int(hB[127]))} puis {ent(int(hB[128]))} ; l'écart du rapport 128/127 à ses voisins est de"
          f" {fr(100 * max(sauts), '{:.1f}')} % au plus). Et le calcul lui-même ne passe jamais par des entiers signés : les"
          " canaux sont lus de 0 à 255 puis divisés par 255.")
    ligne()
    zz = None
    yy_, xx_ = np.mgrid[0:S8.shape[0], 0:S8.shape[1]]
    zz = (xx_ - C_SYM[0]) + 1j * (C_SYM[1] - yy_)
    del yy_, xx_
    diff = np.any(S8 != np.array(FOND_RGB, np.uint8), axis=2)
    b0 = zz[diff].mean()
    ligne("**Le seuil, descendu jusqu'à zéro** :")
    ligne()
    ligne("| masque | pixels | écart au centre de symétrie | direction (°, y vers le haut) |")
    ligne("|---|---:|---:|---:|")
    ligne(f"| tout pixel différent du fond exact {FOND_RGB} (aucun seuil) | {ent(int(diff.sum()))} | {fr(abs(b0), '{:.3f}')} px |"
          f" {fr(np.degrees(np.angle(b0)), '{:.0f}')} |")
    BAS = []
    for t_ in (0.001, 0.002, 0.005, 0.01, 0.015, 0.02, 0.03, 0.05):
        mm = Lk > fondL + t_
        bb = zz[mm].mean()
        BAS.append((t_, abs(bb)))
        ligne(f"| L > fond + {fr(t_, '{:.3f}')} | {ent(int(mm.sum()))} | {fr(abs(bb), '{:.3f}')} px | {fr(np.degrees(np.angle(bb)), '{:.0f}')} |")
    ligne()
    ligne(f"- **0,37 px n'est pas une constante** : c'est la valeur du balayage à t = 0,02. Sans aucun seuil, l'encre est"
          f" centrée à {fr(abs(b0), '{:.3f}')} px près ; jusqu'à t = 0,01, l'écart reste entre"
          f" {fr(min(v for t_, v in BAS if t_ <= 0.01), '{:.2f}')} et {fr(max(v for t_, v in BAS if t_ <= 0.01), '{:.2f}')} px (le niveau du bruit) ;"
          " au-delà, il monte avec le seuil. Rapporté au rayon du dessin (984 px), 0,37 px fait 3,8·10⁻⁴, soit 380 ppm :"
          " petit, mais cent fois la précision du centre.")
    biais = (999.5 - 1000.0) + 1j * (1000.0 - 999.5)
    ligne(f"- **Le zéro qui déséquilibre** : ton intuition a un vrai pendant dans l'image. Un axe de 2 000 pixels n'a pas de"
          f" pixel central : le milieu tombe entre 999 et 1 000, en 999,5, comme le milieu de −128 … 127 tombe en −0,5."
          f" Qui prendrait 1 000 (= 2 000/2) pour centre se tromperait d'un demi-pixel sur chaque axe : {fr(abs(biais), '{:.4f}')} px"
          f" = √2/2, vers {fr(np.degrees(np.angle(biais)), '{:.0f}')}°. Le centre de symétrie mesuré, (999,497 ; 999,499), dit que le"
          " dessin respecte la bonne convention. Et le masque ne suit pas ce biais : sa direction est opposée en hauteur"
          " (−99° à −136°) et sa taille grandit avec le seuil. Il passe par 0,71 px à t = 0,05, à 1 % de √2/2 : encore une"
          " dérive qui croise une constante, comme les dizaines de premiers croisent π puis 2√2 (section 4.2).")
    ligne(f"- **Le 10/3** : le fond n'est pas un zéro neutre. Ses canaux valent {FOND_RGB}, donc sa moyenne RGB vaut"
          f" ({FOND_RGB[0]} + {FOND_RGB[1]} + {FOND_RGB[2]})/3 = 22/3, dont 10/3 viennent du bleu. Ce décalage est uniforme : il est"
          " retranché avant la pesée, et un fond uniforme n'a pas de dipôle (son centre est celui du cadre). Il agit"
          " seulement aux bords anticrénelés, où chaque courbe se mélange à ce zéro bleuté : il fait partie de l'effet du"
          " seuil. Pour le séparer, il faudrait un rendu sur un fond neutre (piste).")
    ligne()
    ligne("**Ce que le seuil change, et ce qu'il ne change pas** (la mesure de la moitié de la partie XXX, § 2, refaite à"
          " chaque seuil ; ρ est le rayon rapporté au contour, mesuré angle par angle) :")
    ligne()
    ligne("| seuil t | part de l'intérieur qui est de l'encre | encre dans le contour réduit de 1/√2 | ρ médian (1/√2 = 0,7071) |"
          " ⟨ρ²⟩ | écart du centre |")
    ligne("|---:|---:|---:|---:|---:|---:|")
    RR_ = np.abs(zz)
    TH_ = np.angle(zz)
    NB_ = 3600
    Bn_ = ((TH_ + np.pi) / (2 * np.pi) * NB_).astype(int) % NB_
    MOIT = []
    for t_ in (0.005, 0.02, 0.05, 0.1, 0.2, 0.3):
        mm = Lk > fondL + t_
        RMAX_ = np.zeros(NB_)
        np.maximum.at(RMAX_, Bn_[mm], RR_[mm])
        rout = np.interp((TH_ + np.pi) / (2 * np.pi) * NB_, np.arange(NB_), RMAX_)
        DED_ = RR_ < rout - 2
        rho_ = (RR_ / np.maximum(rout, 1.0))[mm & DED_]
        MOIT.append((t_, (mm & DED_).sum() / DED_.sum(), np.mean(rho_ <= 2**-0.5), np.median(rho_), np.mean(rho_**2), abs(zz[mm].mean())))
        ligne(f"| {fr(t_, '{:.3f}')} | {fr(100 * MOIT[-1][1], '{:.1f}')} % | {fr(100 * MOIT[-1][2], '{:.2f}')} % | {fr(MOIT[-1][3])} |"
              f" {fr(MOIT[-1][4])} | {fr(MOIT[-1][5], '{:.2f}')} px |")
    ligne()
    ligne(f"- Le seuil change la quantité d'encre de {fr(100 * MOIT[0][1], '{:.0f}')} % à {fr(100 * MOIT[-1][1], '{:.0f}')} %, et le centre"
          f" de {fr(MOIT[0][5], '{:.2f}')} à {fr(MOIT[-1][5], '{:.1f}')} px. Mais la moitié reste à sa place : entre"
          f" {fr(100 * min(m_[2] for m_ in MOIT), '{:.2f}')} % et {fr(100 * max(m_[2] for m_ in MOIT), '{:.2f}')} % de l'encre dans le contour"
          f" réduit de 1/√2, ρ médian entre {fr(min(m_[3] for m_ in MOIT))} et {fr(max(m_[3] for m_ in MOIT))}.")
    ligne("- **Pourquoi.** Le seuil change la couleur en largeur, et les couleurs tournent autour du centre : il touche le"
          " premier harmonique (le dipôle, donc le centre). La moitié ne regarde que la distance au centre, en moyenne sur"
          " toutes les courbes : l'harmonique zéro, que la rotation d'ordre 17 protège. Le résultat de la partie XXX sur la"
          " moitié est donc robuste au cadre ; ses centres de la lumière, eux, dépendent du cadre.")
    assert abs(b0) < 0.1 and max(v for t_, v in BAS if t_ <= 0.01) < 0.2 and abs(abs(biais) - 2**-0.5) < 1e-12
    assert max(m_[2] for m_ in MOIT) - min(m_[2] for m_ in MOIT) < 0.01 and MOIT[-1][5] > 10
    assert max(sauts) < 0.05
    del zz, RR_, TH_, Bn_
    del Lk, Ck, cls, dmin
    TESTS.append(("006 et 007", "classes de teinte, montée cyclique, masques sans seuil puis de t = 0,001 à 0,40",
                  f"pas d'ordre de dessin ni de repli signé ; sans seuil {fr(abs(b0), '{:.3f}')} px, puis le seuil déplace le centre"
                  f" jusqu'à {fr(MASQ[-1][2], '{:.0f}')} px ; la moitié reste entre {fr(100 * min(m_[2] for m_ in MOIT), '{:.1f}')}"
                  f" et {fr(100 * max(m_[2] for m_ in MOIT), '{:.1f}')} %"))

# --- 4.10 trois énoncés des dossiers, refaits ici avant d'être cités ------------------------------------------------------
from math import comb, factorial  # noqa: E402

ligne()
ligne("### 4.10 Trois énoncés des dossiers, vérifiés avant d'être cités")
ligne()


def derangements(j):
    return sum((-1) ** (j - k) * comb(j, k) * factorial(k) for k in range(j + 1))


def moment_exp(j):
    """E[(1 − E)^j] pour E exponentielle de moyenne 1 (moments E[E^k] = k!)."""
    return sum(comb(j, k) * (-1) ** k * factorial(k) for k in range(j + 1))


ok_a = all(moment_exp(j) == (-1) ** j * derangements(j) for j in range(1, 21))
ligne(f"- **Dossier corde, § 3.3** : E[(1 − E)^j] = (−1)^j·!j pour une loi exponentielle (!j : les dérangements"
      f" {', '.join(str(derangements(j)) for j in range(1, 7))}…). Vérifié pour j = 1 à 20 : {'oui' if ok_a else 'NON'}."
      " Le « dernier 2 » du ménisque 2/3 = 2 × 1/6 × 2 (partie XXIV) est donc −E[(1 − E)³] = !3 = 2.")
ok_b = (10**2 - 10 + 1 == 91 == 7 * 13) and pow(10, 3, 91) == 90 and pow(10, 6, 91) == 1
ligne(f"- **Dossier bases, § 3.2** : Φ₆(10) = 10² − 10 + 1 = 91 = 7 × 13, et 10³ ≡ −1 (mod 91) : 1/7 et 1/13 ont la même"
      f" période 6 parce qu'ils sont les deux facteurs du même polynôme cyclotomique. Vérifié : {'oui' if ok_b else 'NON'}."
      " C'est pourquoi la fiche 013 s'était demandé si 1/13 se comportait comme 1/7.")
ok_c = []
for q in range(2, 31):
    b_, p_ = q * q + 1, q * q - q + 1
    manque = set(range(b_)) - {(b_ * r) // p_ for r in range(1, p_)}
    ok_c.append(manque == {k * q for k in range(q + 1)})
ligne(f"- **Dossier bases, § 3.2 (le lemme des chiffres)** : pour b = q² + 1 et p = q² − q + 1, les chiffres que peut"
      f" prendre un développement de r/p en base b sont tous les chiffres sauf les multiples k·q (k = 0 … q). Vérifié pour"
      f" q = 2 à 30 : {'oui' if all(ok_c) else 'NON'}. Pour q premier, ces chiffres sont exactement les unités modulo b − 1 = q² :"
      " le cas (10, 7) de la section 4.1 n'est plus un fait isolé, c'est le lemme quand la période est pleine.")
assert ok_a and ok_b and all(ok_c)
TESTS.append(("dossiers corde et bases", "trois énoncés refaits", "dérangements (j ≤ 20), Φ₆(10) = 7 × 13, lemme des chiffres (q ≤ 30) : vérifiés"))


# --- 4.11 le « 93 % » de la défocalisation, contre le taux de base (dossier lumière, N4) --------------------------------
from scipy.special import j1  # noqa: E402

ligne()
ligne("### 4.11 Le « 93 % » de la défocalisation, contre un prédicteur constant (dossier lumière)")
ligne()
with open(os.path.join(ICI, "..", "resultats", "centre_venn.md"), encoding="utf-8") as fh:
    txt_cv = fh.read()
m_def = re.search(r"mesurée de (\d+) à (\d+) px\. Signes en accord avec 2 J₁\(x\)/x sur (\d+) % des rayons fiables"
                  r" au-delà du trou \((\d+) rayons de (\d+) à (\d+) px", txt_cv)
r_inv0, r_inv1, pct, n_ray, r0_, r1_ = (int(g) for g in m_def.groups())
RS_ = np.arange(r0_, r1_ + 1)
assert len(RS_) == n_ray
signe_th = np.sign(2 * j1(4 * 17 / RS_) / (4 * 17 / RS_))          # le modèle de Hopkins (disque de 4 px, harmonique 17)
signe_mes = np.where((RS_ >= r_inv0) & (RS_ <= r_inv1), -1, 1)      # l'inversion mesurée par la partie XXX
acc_modele = int(np.sum(signe_th == signe_mes))
acc_constant = int(np.sum(signe_mes == 1))
ligne(f"La partie XXX (§ 6.3) annonce des signes en accord avec 2 J₁(x)/x sur {pct} % des {n_ray} rayons de {r0_} à {r1_} px,"
      f" avec une inversion mesurée de {r_inv0} à {r_inv1} px. Le modèle prévoit l'inversion de 9,7 à 17,7 px : sur les rayons"
      f" étudiés, seulement {int(np.sum(signe_th < 0))} sont négatifs ({', '.join(str(r) for r in RS_[signe_th < 0])} px).")
ligne()
ligne(f"- Le modèle est d'accord sur {acc_modele} rayons sur {n_ray} ({fr(100 * acc_modele / n_ray, '{:.1f}')} %).")
ligne(f"- Un prédicteur constant, « positif partout », l'est sur {acc_constant} ({fr(100 * acc_constant / n_ray, '{:.1f}')} %) :"
      " c'est le taux de base.")
ligne(f"- **Verdict** : le 93 % ne bat le taux de base que d'{'un rayon' if acc_modele - acc_constant == 1 else str(acc_modele - acc_constant) + ' rayons'}."
      " La couronne inversée est réelle (de 16 à 21 px), mais cette statistique ne la teste pas : presque tous les rayons"
      " sont positifs, pour le modèle comme pour la mesure. Le bon test fait varier le rayon du flou b et l'harmonique"
      " (17, 34, 51) et vérifie que la couronne suit r entre m·b/7,016 et m·b/3,832 (dossier lumière, N4).")
assert acc_modele == 71 and acc_constant == 70
TESTS.append(("XXX § 6.3", "le score du modèle contre un prédicteur constant", f"{acc_modele}/{n_ray} contre {acc_constant}/{n_ray} : le « 93 % » est le taux de base"))


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
            ax.annotate(f"n = {n}", (k, float(CORDES[n])), xytext=(7, -3) if n == 1 else (4, -13),
                        textcoords="offset points", fontsize=8, color=F.INK2)
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



def panneau_cadre(ax):
    paires = sorted(ARETES0.items(), key=lambda kv: kv[1])
    ys = np.arange(len(paires))
    for y, ((a_, b_), d) in zip(ys, paires):
        c_ = F.ORANGE if d < 2**0.5 else F.BLEU
        ax.plot([1.30, d], [y, y], color=c_, lw=5, solid_capstyle="butt")
        ax.text(max(d, 2**0.5) + 0.006, y, f"{a_}–{b_}", va="center", fontsize=7.6, color=F.INK2)
    ax.axvline(2**0.5, color=F.INK2, lw=1.2, ls=(0, (4, 3)))
    ax.axvline((2 * K0 / (K0 - 1)) ** 0.5, color=F.MUTED, lw=1.0, ls=":")
    ax.text(2**0.5 - 0.004, len(paires) - 0.4, "√2", ha="right", fontsize=9, color=F.INK2)
    ax.text((2 * K0 / (K0 - 1)) ** 0.5 + 0.004, len(paires) - 0.4, "parts égales : √(2K/(K − 1))", fontsize=7.8,
            color=F.MUTED)
    ax.set_yticks([])
    ax.set_xlim(1.30, 1.79)
    ax.set_ylim(-1.2, len(paires) - 0.2)
    ax.set_xlabel("distance entre deux fiches de dimensions différentes (vecteurs centrés)")
    ax.set_title("b. Le cadre fabrique des liens : p_a + p_b < Σp²")
    ax.plot([], [], color=F.ORANGE, lw=5, label="sous √2 : lien apparent (deux dimensions rares)")
    ax.plot([], [], color=F.BLEU, lw=5, label="au-dessus de √2")
    ax.legend(loc="lower right", fontsize=7.8)
    ax.grid(axis="y", visible=False)


def panneau_seuil(ax):
    if "MASQ" not in globals():
        ax.text(0.5, 0.5, "image de Dzoba absente", ha="center", transform=ax.transAxes)
        return
    pts = sorted({round(t_, 4): e_ for t_, e_ in [(m_[0], m_[2]) for m_ in MASQ] + BAS}.items())
    t_ = [a_ for a_, _ in pts]
    e_ = [b_ for _, b_ in pts]
    ax.plot(t_, e_, "-o", color=F.BLEU, ms=5.5, mec=F.SURF, mew=1.2, label="masque L > fond + t : écart du centre")
    ax.axhline(abs(b0), color=F.AQUA, lw=1.2, ls=(0, (4, 3)))
    ax.text(0.0012, abs(b0) * 1.12, f"aucun seuil (tout pixel ≠ fond {FOND_RGB}) : {fr(abs(b0), '{:.3f}')} px", fontsize=7.8, color=F.INK2)
    ax.axhline(2**-0.5, color=F.ORANGE, lw=1.2, ls=(0, (4, 3)))
    ax.text(0.0012, 2**-0.5 * 1.12, "centre pris en 1 000 au lieu de 999,5 : √2/2 = 0,707 px", fontsize=7.8, color=F.INK2)
    for tt, ee in pts:
        if tt in (0.02, 0.1, 0.4):
            ax.annotate(f"t = {fr(tt, '{:.2f}')} : {fr(ee, '{:.2f}') if ee < 10 else fr(ee, '{:.1f}')} px", (tt, ee),
                        xytext={0.4: (-112, -3), 0.1: (-100, 9), 0.02: (6, -13)}[tt], textcoords="offset points",
                        fontsize=7.8, color=F.INK2)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.0009, 0.5)
    ax.set_ylim(0.02, 60)
    ax.set_xlabel("seuil t du masque binaire (clarté OKLab au-dessus du fond)")
    ax.set_ylabel("écart au centre de symétrie (px)")
    ax.set_title("c. Le seuil déplace le centre ; la moitié ne bouge pas")
    ax.text(0.03, 0.8, "encre dans le contour réduit de 1/√2 :\nde " + fr(100 * min(m_[2] for m_ in MOIT), '{:.1f}') + " à "
            + fr(100 * max(m_[2] for m_ in MOIT), '{:.1f}') + " % pour t = 0,005 à 0,3", transform=ax.transAxes, fontsize=8,
            color=F.INK2, va="top")


def panneau_derive(ax):
    Ns = np.array([d_[0] for d_ in DERIVE], float)
    ax.plot(Ns, [d_[1] for d_ in DERIVE], "-", color=F.BLEU, label="motifs exacts : {1, 7} + {3, 9} contre les autres paires")
    ax.plot(Ns, [d_[2] for d_ in DERIVE], "-", color=F.AQUA, label="paires larges : distance 6 / distance 2")
    for val, lab, c_ in ((np.pi, "π", F.ORANGE), (2 * 2**0.5, "2√2", F.ORANGE), (2.0, "2", F.INK2)):
        ax.hlines(val, Ns[0], Ns[-1], color=c_, lw=1.0, ls=(0, (4, 3)))
        ax.text(Ns[-1] * 1.25, val, lab, va="center", fontsize=8.8, color=c_)
    ax.text(2e5, 1.85, "la loi : S(6)/S(2) = 2 (Hardy et Littlewood)", fontsize=8, color=F.INK2)
    for E in (5, 6):
        ax.plot([10.0**E], [RAPPORTS[E][0]], "o", color=F.ORANGE, ms=7, mec=F.SURF, mew=1.4, zorder=5)
    ax.set_xscale("log")
    ax.set_xlim(Ns[0], Ns[-1] * 3.5)
    ax.set_ylim(1.7, 4.6)
    ax.set_xlabel("N (premiers sous N, groupés par dizaines)")
    ax.set_ylabel("rapport, motif par motif")
    ax.set_title("d. Une dérive croise π puis 2√2 ; la loi reste à 2")
    ax.legend(loc="upper right", fontsize=7.8)


fig, axs = F.plt.subplots(2, 2, figsize=(13.2, 10.2))
panneau_diagonale(axs[0, 0])
panneau_cadre(axs[0, 1])
panneau_seuil(axs[1, 0])
panneau_derive(axs[1, 1])
fig.subplots_adjust(wspace=0.22, hspace=0.3)
F.sauver(fig, "rev001_diagonale_cadre.png")



# ===========================================================================
# La figure de la synthèse : le nerf des dossiers, puis les arbres « en Perron » dans les disques
# ===========================================================================
ARBRES = [  # plan-001.md, § 2.2 (corrigé par la vérification croisée : recueil/revisions/verification-croisee-001.md)
    ("P1", "l'ombre du cube {0, 1}ⁿ", "D6", ["D5", "D2"], ["003", "004", "005", "008", "009", "015"]),
    ("P2", "la moitié", "D1", ["D4", "D6"], ["005", "010"]),
    ("P3", "le terme x²/6", "D1", ["D4"], ["002", "003", "011"]),
    ("P4", "le quart de tour i mod b", "D2", ["D5"], ["001", "013", "014"]),
    ("P5", "le budget en bits", "D3", ["D5"], ["006", "007", "008", "011"]),
    ("P6", "les réduites", "D2", ["D5", "D4"], ["002", "014"]),
    ("P7", "la loi de l'écart", "D7", ["D3"], ["002", "003", "004", "005", "007", "012"]),
    ("P8", "le cône à sommet imaginaire", "D8", ["D1", "D4"], ["006"]),
]
ANNEAU = ["D1", "D6", "D5", "D2", "D3", "D7", "D8", "D4"]   # les dimensions voisines côte à côte
COUL_D = {d: c_ for d, c_ in zip(ANNEAU, [F.BLEU, F.AQUA, F.JAUNE, F.ORANGE, F.BLEU, F.AQUA, F.JAUNE, F.ORANGE])}
COURT = {"corde-et-dimensions": "corde", "moities-et-crans": "moitiés", "bases-congruences-premiers": "bases",
         "grain-pixels-centres": "grain", "lumiere-et-physique": "lumière", "aiguilles-kakeya-perron": "aiguilles",
         "ombres-cube-venn": "ombres", "hasard-et-methode": "méthode"}


def panneau_nerf(ax, version):
    cv = couverture(COUV[version], 1)
    noms = sorted(cv, key=lambda n: list(COURT).index(n) if n in COURT else 99)
    ang = {n: np.pi / 2 - 2 * np.pi * i / len(noms) for i, n in enumerate(noms)}
    pos = {n: (np.cos(a_), np.sin(a_)) for n, a_ in ang.items()}
    for t in itertools.combinations(noms, 3):
        if set.intersection(*(cv[x] for x in t)):
            ax.fill(*zip(*[pos[x] for x in t]), color=F.AQUA, alpha=0.10, lw=0)
    for a_, b_ in itertools.combinations(noms, 2):
        k = len(cv[a_] & cv[b_])
        if k:
            ax.plot(*zip(pos[a_], pos[b_]), color=F.BLEU, lw=0.6 + 1.0 * k, alpha=0.45, solid_capstyle="round")
    tv3 = set(NERF[(version, 3)]["tv"])
    for t in NERF[(version, 1)]["tv"]:
        c_ = F.INK if t in tv3 else F.ORANGE
        pts = np.array([pos[x] for x in t])
        g = pts.mean(0)
        pts = g + 0.78 * (pts - g)                     # rétréci vers son centre, pour se détacher des arêtes
        xs, ys = zip(*np.vstack([pts, pts[:1]]))
        ax.plot(xs, ys, color=c_, lw=1.4, ls=(0, (3, 2.2)), zorder=4)
    for n, (x, y) in pos.items():
        ax.plot([x], [y], "o", color=F.INK, ms=8, mec=F.SURF, mew=1.5, zorder=6)
        ax.text(1.2 * x, 1.2 * y, f"{COURT.get(n, n)} ({len(cv[n])})", ha="center", va="center", fontsize=8.8, color=F.INK)
    ax.plot([], [], color=F.BLEU, lw=2.5, label="arête : fiches partagées (épaisseur)")
    ax.fill([], [], color=F.AQUA, alpha=0.3, label="triangle rempli : une fiche commune aux trois")
    ax.plot([], [], color=F.ORANGE, lw=1.3, ls=(0, (3, 2.5)), label="triangle vide, trou du recueil (une partie les réunit)")
    ax.plot([], [], color=F.INK, lw=1.3, ls=(0, (3, 2.5)), label="triangle vide, trou du corpus (aucune partie)")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), fontsize=7.8, ncol=2)
    b = NERF[(version, 1)]["b"]
    ax.set_title(f"a. Le nerf des dossiers (fiches, {version}) : b₀ = {b[0]}, b₁ = {b[1]}")
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.32, 1.3)
    ax.set_aspect("equal")
    ax.axis("off")


def arbre_perron(ax, base, largeur, hauteur, n_branches, couleur, etiquettes):
    """Un petit arbre de Perron : n branches fines qui partent d'en haut et se rejoignent dans le triangle du bas."""
    bx, by = base
    demi = 0.065 * (n_branches - 1)
    sommets = np.linspace(bx - demi, bx + demi, n_branches) if n_branches > 1 else [bx]
    for k, sx in enumerate(sommets):
        ax.fill([bx - largeur / 2, bx + largeur / 2, sx], [by, by, by + hauteur], color=couleur, alpha=0.28, lw=0.6,
                ec=couleur)
        if k < len(etiquettes):
            ax.text(sx, by + hauteur + 0.04, etiquettes[k], ha="center", va="bottom", fontsize=6.6, color=F.INK2, rotation=90)
    ax.fill([bx - largeur / 2, bx + largeur / 2, bx], [by, by, by - 0.55 * largeur], color=couleur, alpha=0.9, lw=0)


def panneau_perron(ax):
    R_anneau, r_d = 1.55, 1.0
    cen = {d: (R_anneau * np.cos(np.pi / 2 - 2 * np.pi * i / 8), R_anneau * np.sin(np.pi / 2 - 2 * np.pi * i / 8))
           for i, d in enumerate(ANNEAU)}
    for d, (x, y) in cen.items():
        F.cercle(ax, (x, y), r_d, color=COUL_D[d], lw=1.3, alpha=0.8)
        u = np.hypot(x, y)
        ax.text(x * (1 + (r_d + 0.28) / u), y * (1 + (r_d + 0.22) / u), f"{d}\n{NOMS_DIMS[d]}", ha="center", va="center",
                fontsize=7.8, color=F.INK2)
    # où poser chaque triangle du bas : dans son disque, du côté des disques qu'il touche (placement à la main)
    decale = {"P1": (0.25, -0.35), "P2": (0.38, -0.12), "P3": (-0.42, 0.02), "P4": (0.45, 0.45), "P5": (0.3, 0.32),
              "P6": (-0.15, -0.62), "P7": (0.35, -0.22), "P8": (0.3, 0.38)}
    for nom, titre, disque, contre, fiches in ARBRES:
        x0, y0 = cen[disque]
        bx, by = x0 + decale.get(nom, (0, 0))[0], y0 + decale.get(nom, (0, 0))[1]
        arbre_perron(ax, (bx, by - 0.2), 0.16, 0.38, len(fiches), COUL_D[disque], fiches)
        ax.text(bx, by - 0.33, f"{nom}\n{titre}", ha="center", va="top", fontsize=7.0, color=F.INK, linespacing=1.15)
    ax.set_title("b. La synthèse en Perron : les arbres dans leurs disques")
    ax.set_xlim(-3.6, 3.6)
    ax.set_ylim(-3.2, 3.3)
    ax.set_aspect("equal")
    ax.axis("off")


fig, axs = F.plt.subplots(1, 2, figsize=(15.5, 7.8))
panneau_nerf(axs[0], "v2" if "v2" in COUV else "v1")
panneau_perron(axs[1])
fig.subplots_adjust(wspace=0.05)
F.sauver(fig, "rev001_perron_venn.png")


# ===========================================================================
# Le tableau des tests, puis l'écriture des résultats
# ===========================================================================
ligne()
ligne("## 5. Le tableau des tests de la révision")
ligne()
ligne("| fiche ou partie | ce qui varie | verdict |")
ligne("|---|---|---|")
for qui, quoi, verdict in TESTS:
    ligne(f"| {qui} | {quoi} | {verdict} |")
ligne()
ligne(f"(calculs : {fr(time.time() - T0, '{:.0f}')} s)")
with open(os.path.join(ICI, "..", "resultats", "revision_001.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(md) + "\n")
