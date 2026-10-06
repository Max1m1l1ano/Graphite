"""
Partie XVI : ménisque et projection. Les disques qui se touchent, en translation, en hyperbole et en triangle.

    python3 scripts/menisque_projection.py        # ≈ 5 s

Écrit resultats/menisque_projection.md, figures/p1_contacts_disques.png et figures/p2_menisque_projection.png.

La chèvre généralisée : le pré est la boule unité B(O, 1) de dimension n, le piquet P est à la distance d de O, la
corde vaut ρ. On cherche ρ_n(d), la corde qui couvre la moitié du pré (d = 1 : la chèvre classique, de corde r_n).

1. En dimension infinie, ρ² = d² + 1. Pour d = 1, c'est la diagonale 1x, 1y : √2. Les arêtes de la grille décalée A_n
   sont toutes des diagonales 1x, 1y (e_i − e_j).
2. r_n² = 1 + g_n² + μ_n : le piquet (1), la projection g_n² = (n−1)/(n+1) et le ménisque μ_n.
3. Le plateau : ρ = 2^(−1/n) tant que le disque ne touche pas le bord (la chèvre s'annule), et le ménisque généralisé.
4. Se toucher, c'est une diagonale à 45° dans le plan (d, ρ) : la géométrie de Laguerre.
5. Les trois déplacements par le point du simplexe (d = 1, ρ = s_n) : translation, hyperbole, triangle.
6. Le terme suivant : ρ² − d² = g² + c_n/ρ², avec c_n = (dispersion de l'ombre − ménisque du bord)/4.
"""

import logging
import math
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from scipy.optimize import brentq, minimize_scalar
from scipy.special import betainc, gamma

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
ROUGE, VIOLET = "#d0342c", "#7d4fc4"
C_TRANS, C_HYP, C_TRI = F.AQUA, VIOLET, F.JAUNE  # les trois déplacements, dans toutes les figures
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


def calotte(n, h):
    """Part de la boule unité de dimension n contenue dans une calotte de hauteur h (0 ≤ h ≤ 2)."""
    if h <= 0:
        return 0.0
    if h >= 2:
        return 1.0
    v = 0.5 * betainc((n + 1) / 2, 0.5, h * (2 - h))
    return v if h <= 1 else 1 - v


def recouvre(n, d, rho):
    """Part du pré B(O, 1) couverte par la boule de rayon rho centrée à la distance d de O."""
    if d + rho <= 1:
        return rho ** n
    if d + 1 <= rho:
        return 1.0
    if d >= 1 + rho:
        return 0.0
    x = (d * d + 1 - rho * rho) / (2 * d)  # plan radical (où les deux sphères se coupent), compté de O vers P
    return calotte(n, 1 - x) + rho ** n * calotte(n, (rho - d + x) / rho)


def rho_moitie(n, d):
    """Corde qui couvre la moitié du pré, piquet à la distance d : le plateau 2^(−1/n) tant que le disque est dedans."""
    r0 = 2 ** (-1 / n)
    if d <= 1 - r0:
        return r0
    return brentq(lambda r: recouvre(n, d, r) - 0.5, max(r0, abs(d - 1)), d + 1, xtol=1e-15)


corde = lambda n: rho_moitie(n, 1.0)
g2 = lambda n: (n - 1) / (n + 1)  # la projection : base du simplexe = rayon quadratique de l'ombre du pré
arete = lambda n: math.sqrt(2 * n / (n + 1))  # s_n, l'arête du simplexe de hauteur 1 (la maille de la grille décalée)
c_n = lambda n: 2 * n * (n - 1) / (3 * (n + 1) ** 3 * (n + 3))
V = lambda n: math.pi ** (n / 2) / gamma(n / 2 + 1)


def maximum(f, a=1.2, b=5.0):
    m = minimize_scalar(lambda n: -f(n), bounds=(a, b), method="bounded", options={"xatol": 1e-9})
    return m.x, -m.fun


# ---------------------------------------------------------------------------
# 1. La dimension infinie : la diagonale 1x, 1y
# ---------------------------------------------------------------------------
ligne("## 1. En dimension infinie : ρ² = d² + 1, et la diagonale 1x, 1y\n")
ligne("Valeurs de ρ_n(d)² − d² (la corde de la moitié, piquet à la distance d) : elles montent vers 1 quand n grandit.\n")
DS1 = (0.0, 0.5, 1.0, 2.0, 5.0)
ligne("| n | " + " | ".join(f"d = {fr(d, '{:g}')}" for d in DS1) + " |")
ligne("|---:|" + "---|" * len(DS1))
for n in (2, 3, 5, 10, 30, 100, 300):
    ligne(f"| {n} | " + " | ".join(fr(rho_moitie(n, d) ** 2 - d * d, "{:.6f}") for d in DS1) + " |")
ligne("| ∞ | " + " | ".join("1" for _ in DS1) + " |")
ligne("\nPourquoi : pour un point X tiré au hasard dans le pré, E|OX|² = n/(n+2) → 1 et E(OX·u)² = 1/(n+2) → 0 dans"
      " toute direction u. En grande dimension, presque tout le pré est à la distance 1 de O et perpendiculaire à OP. La"
      " distance PX est alors l'hypoténuse d'un triangle rectangle de côtés d (le piquet) et 1 (le point) : ρ² = d² + 1,"
      " et pour d = 1, la diagonale 1x, 1y.\n")
ligne("| n | E|OX|² = n/(n+2) | E(OX·u)² = 1/(n+2) | E|PX|² (d = 1) | médiane r_n² |")
ligne("|---:|---|---|---|---|")
for n in (2, 3, 10, 100):
    ligne(f"| {n} | {fr(n / (n + 2))} | {fr(1 / (n + 2))} | {fr(1 + n / (n + 2))} | {fr(corde(n) ** 2)} |")
ligne("| ∞ | 1 | 0 | 2 | 2 |")
ligne("\nLa grille décalée A_n (grille cubique de dimension n+1 coupée par x₀ + … + x_n = 0) : ses arêtes e_i − e_j sont"
      " toutes des diagonales 1x, 1y, de longueur √2, dans toutes les dimensions. Seule la hauteur du simplexe dépend de n.\n")
ligne("| n | arête e_i − e_j | hauteur du simplexe √((n+1)/n) | arête ÷ hauteur = s_n | s_n² = 1 + g_n² |")
ligne("|---:|---|---|---|---|")
for n in (2, 3, 4, 10, 100):
    E = np.eye(n + 1)
    a_ = np.linalg.norm(E[0] - E[1])
    h = np.linalg.norm(E[0] - E[1:].mean(0))
    ligne(f"| {n} | {fr(a_, '{:.6f}')} | {fr(h, '{:.6f}')} | {fr(a_ / h, '{:.6f}')} | 1 + {fr(g2(n), '{:.6f}')} |")
ligne("| ∞ | √2 | 1 | √2 | 1 + 1 |")

# ---------------------------------------------------------------------------
# 2. r² = 1 + projection + ménisque
# ---------------------------------------------------------------------------
ligne("\n## 2. Entre 2 et l'infini : r² = 1 + g² + μ\n")
ligne("1 = le piquet (d² avec d = 1) ; g² = (n−1)/(n+1) = la projection (rayon² de la base du simplexe, rayon quadratique"
      " de l'ombre du pré) ; μ = r² − s² = le ménisque.\n")
ligne("| n | r_n² | 1 + g_n² = s_n² | μ_n = r² − s² | μ / (1 − g²) | (r − s)/s |")
ligne("|---:|---|---|---|---|---|")
for n in (1, 1.5, 2, 2.4236, 3, 4, 5, 10, 20, 50, 100, 300):
    r = corde(n)
    mu = r * r - arete(n) ** 2
    ligne(f"| {fr(n, '{:g}')} | {fr(r * r, '{:.6f}')} | {fr(arete(n) ** 2, '{:.6f}')} | {fr(mu, '{:.7f}')} |"
          f" {fr(mu / (1 - g2(n)), '{:.5f}')} | {fr(100 * (r / arete(n) - 1), '{:.3f}')} % |")
ligne("| ∞ | 2 | 2 | 0 | 0 | 0 % |")
MAXI = {}
for nom, f in (("(r − s)/s", lambda n: corde(n) / arete(n) - 1), ("r − s", lambda n: corde(n) - arete(n)),
               ("μ = r² − s²", lambda n: corde(n) ** 2 - arete(n) ** 2), ("c_n (§ 6)", c_n)):
    MAXI[nom] = maximum(f)
ligne("\nLe ménisque culmine entre 2 et 3, de quelque façon qu'on le mesure :\n")
ligne("| mesure | maximum en n = | valeur |")
ligne("|---|---|---|")
for nom, (nm, v) in MAXI.items():
    ligne(f"| {nom} | {fr(nm)} | {fr(v, '{:.7f}')} |")
ligne(f"\nc_n est maximal à la racine de 2n³ − n² − 12n + 3 = 0 : n = {fr(max(np.roots([2, -1, -12, 3]).real), '{:.6f}')}.")

ligne("\n**Pourquoi la base du simplexe et l'ombre du pré ont le même rayon quadratique.** Deux égalités, toutes deux dans"
      " R^{n+1} (l'espace de la grille A_n) :")
ligne("- Archimède : un point uniforme sur la sphère S^n de R^{n+1}, projeté sur n − 1 axes, est uniforme dans la boule"
      " B^{n−1} (la section du pré). Donc E|y|² = (n−1)/(n+1).")
ligne("- Parseval : les n + 1 sommets e_i du simplexe forment un repère orthonormé ; leurs carrés projetés sur un sous-espace"
      " W de dimension n − 1 font en moyenne dim W/(n+1). Le sommet e₀ se projette en O, les n autres sur la sphère de"
      " rayon R_b : (n/(n+1)) R_b² = (n−1)/(n+1), soit R_b²/h² = (n−1)/(n+1) avec h² = (n+1)/n.\n")
ligne("| n | Monte-Carlo : E|y|² (S^n projetée) | E|y|⁴ | P(|y| < 1/2) | attendu (n−1)/(n+1) ; (n−1)/(n+3) ; 2^(1−n) |"
      " (1/(n+1)) Σ |P_W e_i|² | R_b²/h² |")
ligne("|---:|---|---|---|---|---|---|")
rng = np.random.default_rng(1)
for n in (2, 3, 5):
    X = rng.standard_normal((400_000, n + 1))
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    y2 = (X[:, :n - 1] ** 2).sum(1)
    E = np.eye(n + 1)
    u = E[0] - E[1:].mean(0)
    Q, _ = np.linalg.qr(np.column_stack([np.ones(n + 1), u]))
    PW = np.eye(n + 1) - Q @ Q.T
    frame = sum(np.linalg.norm(PW @ E[i]) ** 2 for i in range(n + 1)) / (n + 1)
    rb2h2 = (np.linalg.norm(E[1] - E[1:].mean(0)) / np.linalg.norm(u)) ** 2
    ligne(f"| {n} | {fr(y2.mean())} | {fr((y2 ** 2).mean())} | {fr((y2 < 0.25).mean())} |"
          f" {fr(g2(n))} ; {fr((n - 1) / (n + 3))} ; {fr(0.5 ** (n - 1))} | {fr(frame, '{:.6f}')} | {fr(rb2h2, '{:.6f}')} |")

ligne("\n**Ménisque et translation : μ ≈ 2δ.** δ_n est la translation (partie VI) qui amène le cercle du simplexe à la moitié"
      " exacte. Comme ρ² − d² est la bonne coordonnée, reculer le piquet de δ ajoute 2δ à ρ² − d² au premier ordre.\n")
ligne("| n | δ_n | 2δ_n | μ_n | 2δ/μ |")
ligne("|---:|---|---|---|---|")
DELTA = {}
for n in (2, 2.4236, 3, 5, 10, 30):
    s = arete(n)
    dl = brentq(lambda x: recouvre(n, 1 - x, s) - 0.5, 1e-7, 0.2, xtol=1e-15)
    DELTA[n] = dl
    mu = corde(n) ** 2 - s * s
    ligne(f"| {fr(n, '{:g}')} | {fr(dl, '{:.7f}')} | {fr(2 * dl, '{:.7f}')} | {fr(mu, '{:.7f}')} | {fr(2 * dl / mu, '{:.4f}')} |")

# ---------------------------------------------------------------------------
# 3. Le plateau : la chèvre s'annule loin du bord
# ---------------------------------------------------------------------------
ligne("\n## 3. La chèvre s'annule loin du bord : le plateau\n")
ligne("Tant que le disque de la corde est entièrement dans le pré, la moitié s'obtient avec ρ₀ = 2^(−1/n), où que soit le"
      " piquet. Le plateau s'arrête au contact intérieur, en d₀ = 1 − 2^(−1/n). Ensuite, la chèvre se réveille doucement :"
      " ρ − ρ₀ croît comme (d − d₀)^((n+1)/2).\n")
ligne("Le ménisque généralisé G_n(d) = ρ_n(d) − max(ρ₀, √(d² + g²)) mesure ce que ni le disque inscrit (le plateau), ni la"
      " projection (l'hyperbole) n'expliquent. Il est nul sur le plateau, vaut r − s en d = 1, culmine exactement là où les"
      " deux lois donnent la même corde (d_b = √(ρ₀² − g²)) et s'éteint au loin comme c_n/(2ρ³).\n")
ligne("| n | ρ₀ = 2^(−1/n) | d₀ (contact) | exposant mesuré | (n+1)/2 | d_b | G max | G(1) = r − s |")
ligne("|---:|---|---|---|---|---|---|---|")
PLATEAU = {}
for n in (2, 3, 5, 10, 30):
    r0 = 2 ** (-1 / n)
    d0 = 1 - r0
    v = [rho_moitie(n, d0 + x) - r0 for x in (1e-4, 1e-3)]
    expo = math.log10(v[1] / v[0]) if v[0] > 0 else None  # au-delà de n = 5, (10⁻⁴)^((n+1)/2) se perd dans l'arrondi
    db = math.sqrt(r0 * r0 - g2(n))
    gmax = rho_moitie(n, db) - r0
    PLATEAU[n] = (r0, d0, db, gmax)
    ligne(f"| {n} | {fr(r0, '{:.6f}')} | {fr(d0, '{:.6f}')} | {fr(expo, '{:.3f}') if expo else '—'} | {fr((n + 1) / 2, '{:g}')} |"
          f" {fr(db, '{:.4f}')} | {fr(gmax, '{:.5f}')} | {fr(corde(n) - arete(n), '{:.6f}')} |")
ligne("| ∞ | 1 | 0 | — | — | 0 | 0 | 0 |")
ok = {}
for n in (2, 3, 5, 10):
    ds = np.concatenate([np.linspace(1e-3, 3, 300), np.geomspace(3, 100, 100)])
    H = np.array([rho_moitie(n, d) ** 2 - d * d for d in ds])
    ok[n] = (bool((H > g2(n)).all()), bool((np.diff(H) <= 1e-12).all()))
ligne("\nVérifications sur 400 positions de d ∈ ]0 ; 100] : la courbe de la chèvre reste au-dessus de son hyperbole"
      " (ρ² − d² > g²) et ρ² − d² décroît : " + ", ".join(f"n = {n} : {'oui' if a and b else 'NON'}" for n, (a, b) in ok.items())
      + ". Pour chaque d, ρ_n(d) croît avec n.")

# ---------------------------------------------------------------------------
# 5. Les trois déplacements par le point du simplexe
# ---------------------------------------------------------------------------
ligne("\n## 4. Les contacts à 45°\n")
ligne("Pas de calcul ici : dans le plan (d, ρ), deux cercles centrés sur la même droite se touchent de l'intérieur quand"
      " |Δd| = |Δρ|, de l'extérieur quand |Δd| = ρ₁ + ρ₂. Avec le pré (0 ; 1) : ρ = 1 − d (corde dans le pré),"
      " ρ = 1 + d (pré dans la corde), ρ = d − 1 (contact extérieur).")
ligne("\n## 5. Les trois déplacements par le point du simplexe (d = 1, ρ = s_n)\n")
ligne("- Translation : la corde reste s_n, le piquet glisse (ligne horizontale du plan (d, ρ)).")
ligne("- Hyperbole : ρ² − d² reste g_n² (la projection est fixe ; tous les cercles passent par la base du simplexe).")
ligne("- Triangle : ρ/d reste s_n (le triangle rectangle O-P-B garde sa forme et grandit depuis O).\n")
ligne("Contacts avec le pré : « intérieur » quand la corde est dans le pré ou le pré dans la corde, « extérieur » quand"
      " les deux disques se touchent de l'extérieur. Contacts avec le cercle de la chèvre (centre P, rayon r_n) : le"
      " ménisque de la partie VI qui devient tangence puis croisement.\n")
ligne("| n | translation : pré dans la corde jusqu'à | tangence avec la chèvre (VI) | moitié | contact extérieur |"
      " hyperbole : corde dans le pré jusqu'à | rayon (cercle circonscrit) | triangle : corde dans le pré jusqu'à |"
      " moitié | pré dans la corde dès |")
ligne("|---:|---|---|---|---|---|---|---|---|---|")
FAM = {}
for n in (2, 3, 5, 10):
    s, r, k = arete(n), corde(n), g2(n)
    dh = brentq(lambda d: recouvre(n, d, s * d) - 0.5, 0.9, 1.2, xtol=1e-15)
    FAM[n] = dict(t_int=s - 1, t_tan=1 - (r - s), t_moit=1 - DELTA.get(n, brentq(lambda x: recouvre(n, 1 - x, s) - 0.5,
                  1e-7, 0.2)), t_ext=1 + s, h_int=1 / (n + 1), h_tan=(k - (r - 1) ** 2) / (2 * (r - 1)),
                  tr_int=1 / (1 + s), tr_tan=(r + 1) / (s + 1), tr_moit=dh, tr_ext=1 / (s - 1))
    f_ = FAM[n]
    ligne(f"| {n} | {fr(f_['t_int'])} | {fr(f_['t_tan'], '{:.5f}')} | {fr(f_['t_moit'], '{:.5f}')} | {fr(f_['t_ext'])} |"
          f" {fr(f_['h_int'])} | {fr(n / (n + 1))} | {fr(f_['tr_int'])} | {fr(dh, '{:.5f}')} | {fr(f_['tr_ext'])} |")
ligne(f"| ∞ | √2 − 1 = {fr(2 ** 0.5 - 1)} | 1 | 1 | √2 + 1 = {fr(2 ** 0.5 + 1)} | 0 | 1 | √2 − 1 | 1 |"
      f" √2 + 1 |")
ligne("\nLes contacts du triangle sont ceux de la translation divisés par la projection : 1/(1 + s) = (s − 1)/g² et"
      " 1/(s − 1) = (s + 1)/g². En dimension infinie, g² = 1 et les deux déplacements touchent le pré aux mêmes"
      " distances, √2 − 1 et √2 + 1 (le nombre d'argent).\n")
ligne("**Le déplacement hyperbolique.** Tous ses cercles passent par la base du simplexe (en 2D, les points A et B à"
      " ±1/√3 sur la perpendiculaire à OP). Son membre tangent au pré, en d = 1/(n+1), de rayon n/(n+1), est la sphère"
      " circonscrite au simplexe : elle touche le pré au piquet. Il ne touche jamais le pré de l'extérieur, et n'atteint la"
      " moitié qu'à l'infini (le plan de la base) : il suit exactement l'asymptote de la chèvre.\n")
ligne("| n | part en d = 0 : g^n | part au contact : (n/(n+1))^n | part en d = 1 (simplexe) | déficit 1/2 − part, d = 1 |"
      " d = 2 | d = 5 | d = 20 | prédit en d = 20 : c_n V_{n−1}/(2 V_n ρ³) |")
ligne("|---:|---|---|---|---|---|---|---|---|")
for n in (2, 3, 5, 10):
    k = g2(n)
    dfs = [0.5 - recouvre(n, d, math.sqrt(d * d + k)) for d in (1, 2, 5, 20)]
    rho20 = math.sqrt(400 + k)
    ligne(f"| {n} | {fr(k ** (n / 2), '{:.6f}')} | {fr((n / (n + 1)) ** n, '{:.6f}')} | {fr(0.5 - dfs[0], '{:.6f}')} | "
          + " | ".join(fr(x, "{:.3e}") for x in dfs) + f" | {fr(c_n(n) * V(n - 1) / (2 * V(n) * rho20 ** 3), '{:.3e}')} |")
ligne("| ∞ | 1/e | 1/e | 1/2 | 0 | 0 | 0 | 0 | 0 |")
ligne("\nEn 2D, le déficit en d = 1 (0,0028299, soit 0,566 % de la moitié) est la zone de confusion de la partie VI divisée"
      " par π ; en 3D (0,0033163), c'est la part manquante exacte (59 − 24√6)/64 de la partie VI.")
neg = {}
for n in (2, 3, 5, 10):
    ds = np.concatenate([np.linspace(1e-3, 3, 400), np.geomspace(3, 200, 100)])
    neg[n] = min(0.5 - recouvre(n, d, math.sqrt(d * d + g2(n))) for d in ds)
ligne("Sur 500 positions de d ∈ ]0 ; 200], la part couverte le long de l'hyperbole reste sous 1/2 (plus petit déficit, en"
      " d = 200 : " + ", ".join(f"{fr(v, '{:.2e}')} pour n = {n}" for n, v in neg.items()) + ").")

# ---------------------------------------------------------------------------
# 6. Le terme suivant
# ---------------------------------------------------------------------------
ligne("\n## 6. Le terme suivant : ρ² − d² = g² + c_n/ρ² + …\n")
ligne("Développement au second ordre (fait ici, à la main, puis vérifié) : la coupe par la sphère de la corde est"
      " presque plate, x₁ ≈ (|y|² − H)/(2ρ) + (|y|⁴ − H²)/(8ρ³), et près du bord elle sort du pré. On obtient")
ligne("c_n = (Var|y|² − ménisque du bord)/4, avec Var|y|² = 4(n−1)/((n+1)²(n+3)) (la dispersion de l'ombre) et le"
      " terme du bord (n−1)(1 − g²)³/6 = 4(n−1)/(3(n+1)³). Donc c_n = 2n(n−1)/(3(n+1)³(n+3)).\n")
ligne("| n | c_n (formule) | (ρ² − d² − g²)·ρ², d = 30 | d = 100 | Var|y|² | bord | bord/Var = (n+3)/(3(n+1)) |")
ligne("|---:|---|---|---|---|---|---|")
for n in (2, 3, 5, 10):
    vals = []
    for d in (30.0, 100.0):
        rho = rho_moitie(n, d)
        vals.append((rho * rho - d * d - g2(n)) * rho * rho)
    var = 4 * (n - 1) / ((n + 1) ** 2 * (n + 3))
    bord = 4 * (n - 1) / (3 * (n + 1) ** 3)
    ligne(f"| {n} | {fr(c_n(n), '{:.7f}')} | {fr(vals[0], '{:.7f}')} | {fr(vals[1], '{:.7f}')} | {fr(var, '{:.6f}')} |"
          f" {fr(bord, '{:.6f}')} | {fr(bord / var, '{:.4f}')} |")
ligne("\nEn 3D, le ménisque du bord vaut exactement la moitié de la dispersion de l'ombre ; à l'infini, le tiers.")

with open(os.path.join(ICI, "..", "resultats", "menisque_projection.md"), "w") as fh:
    fh.write("# Résultats de la partie XVI (générés par scripts/menisque_projection.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure 1 : les contacts des disques le long des trois déplacements
# ===========================================================================
N2 = 2
S2, R2, K2 = arete(2), corde(2), g2(2)
R0 = 2 ** -0.5
FOND = dict(fc=F.SURF, ec="none", alpha=0.92, pad=2.5)


def pre(ax):
    t = np.linspace(0, 2 * np.pi, 400)
    ax.fill(np.cos(t), np.sin(t), color=F.SEQ[1], zorder=0)
    ax.plot(np.cos(t), np.sin(t), color=F.INK, lw=1.6, zorder=3)
    ax.plot([-1.3, 3.0], [0, 0], color=F.GRID, lw=0.8, zorder=0)
    F.point(ax, 0, 0, F.INK, 5)
    ax.text(-0.04, -0.09, "O", fontsize=10, ha="right", va="top")


def schema(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")


def contact(ax, x, y, couleur, marque="o"):
    ax.plot([x], [y], marque, ms=8, color=couleur, mec=F.SURF, mew=1.5, zorder=8)


fig = plt.figure(figsize=(21, 13.6))
gs = fig.add_gridspec(2, 3, wspace=0.16, hspace=0.12, height_ratios=[0.86, 1])
XL, YL = (-1.3, 2.7), (-1.6, 1.5)  # même cadre pour les trois schémas

# a) translation du disque inscrit
ax = fig.add_subplot(gs[0, 0])
pre(ax)
d0 = 1 - R0
for d, coul, lw, ls in ((0.0, F.BLEU, 1.3, "-"), (0.15, F.BLEU, 1.3, "-"), (d0, F.BLEU, 2.4, "-"),
                        (0.75, F.MUTED, 1.0, "--"), (1.2, F.MUTED, 1.0, "--"), (1 + R0, ROUGE, 2.2, "-")):
    F.cercle(ax, (d, 0), R0, color=coul, lw=lw, ls=ls, zorder=4)
    ax.plot([d], [0], "o", ms=4, color=coul, zorder=5)
    part_ = recouvre(2, d, R0)
    lab = "½" if abs(part_ - 0.5) < 1e-12 else fr(part_, "{:.2f}")
    ax.text(d, R0 + 0.04, lab, fontsize=9.5, color=coul, ha="center", va="bottom", zorder=6,
            bbox=dict(fc=F.SURF, ec="none", alpha=0.85, pad=0.4))
contact(ax, 1, 0, F.ORANGE)
ax.annotate("contact intérieur\nd₀ = 1 − 1/√2 = 0,293", (1, 0), (0.55, -1.12), fontsize=8.6, color=F.ORANGE,
            arrowprops=dict(arrowstyle="-", color=F.ORANGE, lw=0.8), ha="center")
ax.annotate("contact extérieur\nd = 1 + 1/√2", (1, 0), (1.95, -1.12), fontsize=8.6, color=ROUGE,
            arrowprops=dict(arrowstyle="-", color=ROUGE, lw=0.8), ha="center")
ax.text(-1.27, 1.47, "Corde 1/√2 (aire π/2). En bleu : la moitié exacte, où que soit\nle piquet, tant que le disque ne"
        " touche pas le bord : la chèvre\ns'annule. En gris : moins de la moitié.", fontsize=8.4, color=F.INK2, va="top")
schema(ax, XL, YL)
ax.set_title("a)  Translation : le disque inscrit glisse (n = 2)", color=C_TRANS)

# b) le faisceau hyperbolique
ax = fig.add_subplot(gs[0, 1])
pre(ax)
g = math.sqrt(K2)
A_, B_ = (0, g), (0, -g)
ax.plot([0, 0], [-1.45, 1.45], color=C_HYP, lw=1.6, ls="--", zorder=4)
ax.text(-0.05, 1.32, "d → ∞ : la droite AB,\nexactement ½", fontsize=8.4, color=C_HYP, ha="right", va="center")
ax.add_patch(Polygon([(1, 0), A_, B_], closed=True, fc="none", ec=F.INK2, lw=1.0, zorder=5))
for d, coul, lw in ((0.0, F.MUTED, 1.2), (1 / 3, F.ORANGE, 2.2), (1.0, C_HYP, 2.2), (2.0, F.MUTED, 1.1),
                    (5.0, F.MUTED, 1.0)):
    F.cercle(ax, (d, 0), math.sqrt(d * d + K2), color=coul, lw=lw, zorder=4)
for (x, y), nom in ((A_, "A"), (B_, "B")):
    F.point(ax, x, y, C_HYP, 7)
    ax.text(x - 0.07, y + (0.07 if y > 0 else -0.07), nom, fontsize=10, ha="right", va="center", color=C_HYP)
F.point(ax, 1, 0, F.INK, 6)
ax.text(1.04, 0.07, "P", fontsize=10)
contact(ax, 1, 0, F.ORANGE)
F.point(ax, 1 / 3, 0, F.ORANGE, 4)
lab = [(0.02, -0.36, "d = 0 : ⅓", F.MUTED), (0.62, -0.86, "d = 1/3 : 4/9, le cercle\ncirconscrit, tangent au piquet", F.ORANGE),
       (1.0, 1.22, "d = 1 (simplexe) : 0,4972", C_HYP), (2.15, -1.38, "d = 2 : 0,4996", F.MUTED)]
for xx, yy, t_, c in lab:
    ax.text(xx, yy, t_, fontsize=8.4, color=c, ha="center", va="center",
            bbox=dict(fc=F.SURF, ec="none", alpha=0.85, pad=0.6), zorder=7)
schema(ax, XL, (-1.55, 1.55))
ax.set_title("b)  Hyperbolique : tous les cercles passent par A et B", color=C_HYP)

# c) le déplacement en triangle
ax = fig.add_subplot(gs[0, 2])
pre(ax)
dt_int, dt_ext = 1 / (1 + S2), 1 / (S2 - 1)
for d, coul, lw in ((dt_int, F.ORANGE, 2.2), (1.0, C_TRI, 2.2), (1.6, F.MUTED, 1.1)):
    F.cercle(ax, (d, 0), S2 * d, color=coul, lw=lw, zorder=4)
    ax.add_patch(Polygon([(0, 0), (d, 0), (0, g * d)], closed=True, fc=coul, alpha=0.13, ec=coul, lw=1.0, zorder=2))
    F.point(ax, d, 0, coul, 4)
t = np.linspace(math.pi - 0.42, math.pi + 0.42, 200)  # le pré entre dans la corde : grand cercle tangent en (−1, 0)
ax.plot(dt_ext + S2 * dt_ext * np.cos(t), S2 * dt_ext * np.sin(t), color=F.ORANGE, lw=2.2, zorder=4)
contact(ax, 1, 0, F.ORANGE)
contact(ax, -1, 0, F.ORANGE)
F.point(ax, 0, g, C_TRI, 6)
ax.text(-0.06, g, "B", fontsize=10, color="#a86f00", ha="right", va="center")
F.point(ax, 1, 0, F.INK, 6)
ax.text(1.04, 0.06, "P", fontsize=10)
ax.text(0.05, -0.64, "d = 0,464 : la corde touche le bord", fontsize=8.2, color=F.ORANGE, ha="left", va="top",
        bbox=dict(fc=F.SURF, ec="none", alpha=0.85, pad=0.5), zorder=7)
ax.text(0.98, 1.32, "d = 1 : le triangle OPB du simplexe\n(côtés 1, 1/√3, 2/√3)", fontsize=8.4, color="#a86f00",
        ha="left", va="center")
ax.text(-0.78, 1.36, "d = 6,46 : le pré entre dans la corde\n(contact intérieur, de l'autre côté)", fontsize=8.2,
        color=F.ORANGE, ha="left", va="center")
ax.text(1.62, -1.12, "d = 1,6", fontsize=8.2, color=F.MUTED)
ax.text(-1.27, -1.4, "Le triangle rectangle O-P-B garde sa forme ; la corde PB = s·d. Moitié exacte\n"
        "en d = 1,0135, juste après le simplexe. Jamais de contact extérieur.", fontsize=8.4, color=F.INK2, va="top",
        bbox=dict(fc=F.SURF, ec="none", alpha=0.9, pad=0.8), zorder=7)
schema(ax, XL, YL)
ax.set_title("c)  En triangle : le triangle O-P-B grandit", color=C_TRI)

# d) le plan (d, ρ)
ax = fig.add_subplot(gs[1, 0])
dd = np.linspace(0, 3, 600)
ax.fill_between(dd, 0, np.clip(1 - dd, 0, None), color=F.SEQ[2], lw=0, zorder=0)
ax.fill_between(dd, 1 + dd, 4, color="#fbe9c4", lw=0, zorder=0)
ax.fill_between(dd, 0, np.clip(dd - 1, 0, None), color="#ecebe6", lw=0, zorder=0)
ax.plot(dd[dd <= 1], 1 - dd[dd <= 1], color=F.ORANGE, lw=1.6)
ax.plot(dd, 1 + dd, color=F.ORANGE, lw=1.6)
ax.plot(dd[dd >= 1], dd[dd >= 1] - 1, color=ROUGE, lw=1.6)
ax.text(0.12, 0.42, "corde\ndans le pré", fontsize=8.5, color=F.BLEU)
ax.text(0.05, 2.5, "pré dans la corde", fontsize=8.5, color="#a86f00")
ax.text(1.22, 0.07, "disjoints", fontsize=8.5, color=F.MUTED)
ax.text(0.5, 0.43, "contact intérieur", fontsize=8, color=F.ORANGE, rotation=-45, rotation_mode="anchor")
ax.text(1.45, 0.53, "contact extérieur", fontsize=8, color=ROUGE, rotation=45, rotation_mode="anchor")
ax.text(1.05, 2.12, "contact intérieur", fontsize=8, color=F.ORANGE, rotation=45, rotation_mode="anchor")
COUL_N = {2: F.RAMPE[0], 3: F.RAMPE[1], 5: F.RAMPE[2], 10: F.RAMPE[3]}
COURBES = {}
for n, c in COUL_N.items():
    xs = np.concatenate([[0.0], np.linspace(1e-3, 3, 260)])
    COURBES[n] = (xs, np.array([rho_moitie(n, d) for d in xs]))
    ax.plot(*COURBES[n], color=c, lw=1.8, label=f"chèvre, n = {n}")
ax.plot(dd, np.sqrt(1 + dd ** 2), color=F.INK, lw=2.0, label="n = ∞ : ρ² = d² + 1")
ax.plot(dd, np.sqrt(K2 + dd ** 2), color=C_HYP, lw=1.5, ls="--", label="hyperbole ρ² − d² = 1/3")
ax.plot(dd, np.full_like(dd, S2), color=C_TRANS, lw=1.5, ls="--", label="translation ρ = s₂")
ax.plot(dd, S2 * dd, color=C_TRI, lw=1.5, ls="--", label="triangle ρ = s₂·d")
F.point(ax, 1, S2, F.INK, 6)
F.point(ax, 1, 2 ** 0.5, F.INK, 6)
ax.annotate("d = 1 : √2,\nta diagonale 1x, 1y", (1, 2 ** 0.5), (0.12, 1.95), fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color=F.INK2, lw=0.8))
ax.annotate("point du simplexe (1 ; 2/√3)", (1, S2), (1.55, 1.0), fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color=F.INK2, lw=0.8))
for n, c in COUL_N.items():
    r0 = 2 ** (-1 / n)
    ax.plot([0, 1 - r0], [r0, r0], color=c, lw=4, alpha=0.55, solid_capstyle="butt",
            label="plateaux : la chèvre s'annule" if n == 2 else None)
ax.set_xlim(0, 3)
ax.set_ylim(0, 3.2)
ax.set_aspect("equal")
ax.set_xlabel("d : distance du piquet au centre")
ax.set_ylabel("ρ : longueur de la corde")
ax.legend(loc="upper left", ncol=2, fontsize=7.4, frameon=True, facecolor=F.SURF, edgecolor="none", framealpha=0.95,
          columnspacing=1.0, handlelength=1.6)
ax.set_title("d)  Le plan (piquet, corde) : les contacts à 45°")

# e) zoom sur le point du simplexe
ax = fig.add_subplot(gs[1, 1])
dz = np.linspace(0.955, 1.04, 300)
rz = np.array([rho_moitie(2, d) for d in dz])
ax.plot(dz, rz, color=F.RAMPE[0], lw=2.2, label="chèvre (moitié exacte)")
ax.plot(dz, np.sqrt(K2 + dz ** 2), color=C_HYP, lw=1.8, label="hyperbole (asymptote)")
ax.plot(dz, np.full_like(dz, S2), color=C_TRANS, lw=1.8, label="translation")
ax.plot(dz, S2 * dz, color=C_TRI, lw=1.8, label="triangle")
ax.plot(dz, R2 - np.abs(dz - 1), color=F.ORANGE, lw=1.0, ls=":", label="tangence avec le cercle de la chèvre")
f2 = FAM[2]
for x, y, c, m in ((f2["t_tan"], S2, F.ORANGE, "o"), (f2["t_moit"], S2, F.INK, "*"),
                   (f2["h_tan"], math.sqrt(K2 + f2["h_tan"] ** 2), F.ORANGE, "o"),
                   (f2["tr_tan"], S2 * f2["tr_tan"], F.ORANGE, "o"), (f2["tr_moit"], S2 * f2["tr_moit"], F.INK, "*")):
    ax.plot([x], [y], m, ms=9 if m == "o" else 13, color=c, mec=F.SURF, mew=1.2, zorder=7)
F.point(ax, 1, S2, F.INK, 6)
F.point(ax, 1, R2, F.RAMPE[0], 7)
ax.annotate("", (1.0, R2), (1.0, S2), arrowprops=dict(arrowstyle="<->", color=F.INK, lw=1.0))
ax.annotate("r − s = 0,00403 :\nle ménisque en d = 1", (1.0, (R2 + S2) / 2), (1.012, 1.1435), fontsize=8.4,
            arrowprops=dict(arrowstyle="-", color=F.INK2, lw=0.8))
ax.text(0.9565, S2 + 0.0012, "translation : tangence en 0,99597 (VI),\nmoitié ★ en 0,99529 (δ = 0,00471)",
        fontsize=8.2, color="#0f7d57", va="bottom")
ax.annotate("triangle : tangence\nen 1,00187 (hors du pré),\nmoitié ★ en 1,0135", (1.0135, S2 * 1.0135),
            (1.0148, 1.1615), fontsize=8.2, color="#a86f00", va="top",
            arrowprops=dict(arrowstyle="-", color="#a86f00", lw=0.8))
ax.annotate("hyperbole : tangence en 0,9707,\njamais la moitié", (f2["h_tan"], math.sqrt(K2 + f2["h_tan"] ** 2)),
            (0.9725, 1.1262), fontsize=8.2, color=C_HYP, arrowprops=dict(arrowstyle="-", color=C_HYP, lw=0.8))
ax.set_xlim(0.955, 1.04)
ax.set_ylim(1.124, 1.174)
ax.set_xlabel("d")
ax.set_ylabel("ρ")
ax.legend(loc="upper left", fontsize=7.8, frameon=True, facecolor=F.SURF, edgecolor="none", framealpha=0.95)
ax.set_title("e)  Zoom sur le point du simplexe (n = 2)")

# f) la part du pré le long des déplacements
ax = fig.add_subplot(gs[1, 2])
dl = np.geomspace(0.01, 60, 700)
A_inscr = [recouvre(2, d, R0) for d in dl]
A_tr = [recouvre(2, d, S2) for d in dl]
A_hyp = [recouvre(2, d, math.sqrt(K2 + d * d)) for d in dl]
A_tri = [recouvre(2, d, S2 * d) for d in dl]
ax.axhline(0.5, color=F.INK, lw=0.9, ls=":")
ax.plot(dl, A_inscr, color=C_TRANS, lw=1.6, ls="--", label="translation, disque inscrit")
ax.plot(dl, A_tr, color=C_TRANS, lw=2.0, label="translation, ρ = s₂")
ax.plot(dl, A_hyp, color=C_HYP, lw=2.0, label="hyperbole, ρ² − d² = 1/3")
ax.plot(dl, A_tri, color=C_TRI, lw=2.0, label="triangle, ρ = s₂·d")
for x, y, c, m in ((d0, 0.5, F.ORANGE, "o"), (1 + R0, 0, ROUGE, "D"), (S2 - 1, 1, F.ORANGE, "o"),
                   (1 + S2, 0, ROUGE, "D"), (1 / 3, 4 / 9, F.ORANGE, "o"), (dt_int, (S2 * dt_int) ** 2, F.ORANGE, "o"),
                   (dt_ext, 1, F.ORANGE, "o"), (f2["t_moit"], 0.5, F.INK, "*"), (f2["tr_moit"], 0.5, F.INK, "*")):
    ax.plot([x], [y], m, ms=8 if m != "*" else 12, color=c, mec=F.SURF, mew=1.2, zorder=7, clip_on=False)
ax.set_xscale("log")
ax.set_xlim(0.01, 60)
ax.set_ylim(-0.02, 1.02)
ax.set_xlabel("d (échelle log)")
ax.set_ylabel("part du pré couverte")
ax.legend(loc="upper left", fontsize=7.6, bbox_to_anchor=(0.0, 0.95), frameon=True, facecolor=F.SURF, edgecolor="none")
ax.text(3.0, 0.515, "l'hyperbole n'atteint ½ qu'à l'infini", fontsize=8.2, color=C_HYP, va="bottom")
ax.text(0.0115, 0.03, "● contact intérieur   ◆ contact extérieur   ★ moitié exacte", fontsize=8, color=F.INK2)
ins = ax.inset_axes([0.62, 0.1, 0.35, 0.27])
dd2 = np.geomspace(0.6, 60, 120)
ins.loglog(dd2, [0.5 - recouvre(2, d, math.sqrt(K2 + d * d)) for d in dd2], color=C_HYP, lw=1.8)
ins.loglog(dd2, [c_n(2) * V(1) / (2 * V(2) * (K2 + d * d) ** 1.5) for d in dd2], color=F.INK, lw=0.9, ls="--")
ins.set_title("½ − part le long de l'hyperbole\n= le ménisque seul, ∝ 1/d³", fontsize=8, fontweight="normal")
ins.tick_params(labelsize=7)
ax.set_title("f)  La part du pré le long des déplacements (n = 2)")
F.sauver(fig, "p1_contacts_disques.png")

# ===========================================================================
# Figure 2 : ménisque et projection, de 2 à l'infini
# ===========================================================================
fig = plt.figure(figsize=(17, 13))
gs = fig.add_gridspec(2, 2, wspace=0.2, hspace=0.27)
NS = (2, 3, 5, 10, 30, 100)
CN = {2: F.SEQ[5], 3: F.SEQ[7], 5: F.SEQ[8], 10: F.SEQ[10], 30: F.SEQ[11], 100: F.SEQ[13]}

# a) la chèvre comme médiane : |PX|² → 1² + 1²
ax = fig.add_subplot(gs[0, 0])
tt = np.linspace(0, 4, 500)
for n in NS:
    ax.plot(tt, [recouvre(n, 1, math.sqrt(x)) for x in tt], color=CN[n], lw=1.8, label=f"n = {n}")
    rn = corde(n) ** 2
    ax.plot([rn], [0.5], "o", ms=6, color=CN[n], mec=F.SURF, mew=1.2, zorder=6)
ax.plot([0, 2, 2, 4], [0, 0, 1, 1], color=F.INK, lw=2.0, label="n = ∞ : tout en 2 = 1² + 1²")
ax.axhline(0.5, color=F.INK, lw=0.8, ls=":")
ax.set_xlabel("|PX|² (P sur le bord, X au hasard dans le pré)")
ax.set_ylabel("part du pré à moins de cette distance")
ax.legend(loc="upper left", fontsize=8.5, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.text(2.06, 0.08, "les points ● sont les cordes r_n² :\n1,3427 ; 1,5093 ; 1,6734 ; 1,8212 ; 1,9360 ; 1,9803",
        fontsize=8.4, color=F.INK2)
ins = ax.inset_axes([0.66, 0.3, 0.31, 0.38])
ins.add_patch(Polygon([(0, 0), (1, 0), (0, 1)], closed=True, fc=F.SEQ[2], ec=F.INK, lw=1.2))
ins.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color=F.GRID, lw=0.8)
ins.text(0.5, -0.12, "1x : le piquet", ha="center", va="top", fontsize=8)
ins.text(-0.06, 0.5, "1y : le point", ha="right", va="center", fontsize=8, rotation=90)
ins.text(0.55, 0.55, "√2", fontsize=11, color=F.INK, fontweight="bold")
ins.text(-0.05, -0.05, "O", fontsize=8, ha="right", va="top")
ins.text(1.03, -0.03, "P", fontsize=8, va="top")
ins.text(0.03, 1.03, "X", fontsize=8)
ins.set_xlim(-0.35, 1.25)
ins.set_ylim(-0.35, 1.2)
ins.set_aspect("equal")
ins.axis("off")
ax.set_title("a)  La chèvre est une médiane : à l'infini, |PX|² = 1² + 1²")

# b) r² = 1 + projection + ménisque
ax = fig.add_subplot(gs[0, 1])
nn = np.geomspace(1.0001, 1000, 260)
proj = np.array([g2(n) for n in nn])
mus = np.array([corde(n) ** 2 - arete(n) ** 2 for n in nn])
ax.axvspan(2, 3, color=F.SEQ[1], zorder=0)
ax.plot(nn, proj, color=F.BLEU, lw=2.2, label="projection g² = (n−1)/(n+1)  (→ 1 : le « 1y »)")
ax.plot(nn, 1 - proj, color=F.BLEU, lw=1.2, ls="--", label="ce qui manque à la projection : 2/(n+1)")
ax.set_xscale("log")
ax.set_ylim(0, 1.05)
ax.set_xlabel("dimension n (échelle log)")
ax.set_ylabel("projection")
ax2 = ax.twinx()
ax2.plot(nn, 100 * mus, color=F.ORANGE, lw=2.2, label="ménisque μ = r² − s² (× 100, axe de droite)")
ax2.set_ylim(0, 1.15)
ax2.set_ylabel("ménisque μ × 100", color=F.ORANGE)
ax2.grid(False)
ax2.spines["right"].set_visible(True)
lignes_max = ["maxima du ménisque, tous entre 2 et 3 :"]
for nom, c in (("(r − s)/s", F.INK2), ("r − s", F.INK2), ("μ = r² − s²", F.ORANGE), ("c_n (§ 6)", VIOLET)):
    nm = MAXI[nom][0]
    ax2.plot([nm, nm], [0, 100 * (corde(nm) ** 2 - arete(nm) ** 2)], color=c, lw=1.0, ls=":")
    lignes_max.append(f"{nom} : n = {fr(nm, '{:.2f}')}")
ax2.text(28, 0.47, "\n".join(lignes_max), fontsize=8.4, color=F.INK2, va="top", linespacing=1.5)
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, loc="center right", bbox_to_anchor=(1.0, 0.62), fontsize=8.3, frameon=True,
          facecolor=F.SURF, edgecolor="none")
ax.set_title("b)  r² = 1 (le piquet) + projection + ménisque")

# c) le terme suivant
ax = fig.add_subplot(gs[1, 0])
var = np.array([4 * (n - 1) / ((n + 1) ** 2 * (n + 3)) for n in nn])
bord = np.array([4 * (n - 1) / (3 * (n + 1) ** 3) for n in nn])
ax.axvspan(2, 3, color=F.SEQ[1], zorder=0)
ax.plot(nn, var, color=F.BLEU, lw=2.0, label="dispersion de l'ombre Var|y|²")
ax.plot(nn, bord, color=F.ORANGE, lw=2.0, label="ménisque du bord (n−1)(1−g²)³/6")
ax.plot(nn, var - bord, color=VIOLET, lw=2.4, label="4·c_n = dispersion − bord")
nm = MAXI["c_n (§ 6)"][0]
ax.plot([nm], [4 * c_n(nm)], "o", ms=7, color=VIOLET, mec=F.SURF, mew=1.2)
ax.annotate(f"max de c_n en n = {fr(nm, '{:.3f}')}", (nm, 4 * c_n(nm)), (5, 0.075), fontsize=8.5, color=VIOLET,
            arrowprops=dict(arrowstyle="-", color=VIOLET, lw=0.8))
ax.set_xscale("log")
ax.set_xlabel("dimension n (échelle log)")
ax.set_ylabel("coefficient")
ax3 = ax.twinx()
ax3.plot(nn, bord / var, color=F.INK2, lw=1.2, ls="--", label="bord ÷ dispersion = (n+3)/(3(n+1))")
ax3.axhline(1 / 3, color=F.MUTED, lw=0.7, ls=":")
ax3.plot([3], [0.5], "o", ms=6, color=F.INK2)
ax3.text(3.3, 0.505, "n = 3 : exactement ½", fontsize=8.3, color=F.INK2)
ax3.text(300, 0.34, "→ ⅓", fontsize=8.3, color=F.INK2)
ax3.set_ylim(0, 0.75)
ax3.set_ylabel("bord ÷ dispersion", color=F.INK2)
ax3.grid(False)
ax3.spines["right"].set_visible(True)
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax3.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, loc="upper right", fontsize=8.3, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.text(14, 0.012, "loin du pré : ρ² − d² = g² + c_n/ρ² + …", fontsize=8.6, color=F.INK2)
ax.set_title("c)  Le terme suivant : dispersion de l'ombre contre ménisque du bord")

# d) le ménisque généralisé
ax = fig.add_subplot(gs[1, 1])
for n in (2, 3, 5, 10, 30):
    r0, d0_, db, gmax = PLATEAU[n]
    xs = np.concatenate([np.geomspace(d0_ + 1e-5, db, 80), np.geomspace(db, 100, 160)])
    G = np.array([rho_moitie(n, d) - max(r0, math.sqrt(d * d + g2(n))) for d in xs])
    c = CN[n]
    ax.plot(xs, np.clip(G, 1e-9, None), color=c, lw=1.8, label=f"n = {n}")
    ax.plot([d0_], [1.4e-7], "|", ms=22, mew=2.4, color=c, clip_on=False)
    ax.plot([1], [corde(n) - arete(n)], "o", ms=5, color=c, mec=F.SURF, mew=1.0, zorder=6)
d_far = np.geomspace(3, 100, 40)
ax.plot(d_far, [c_n(2) / (2 * (d * d + K2) ** 1.5) for d in d_far], color=F.INK, lw=1, ls="--")
ax.text(9, 2.5e-5, "c₂/(2ρ³)", fontsize=8.5)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(1e-7, 0.08)
ax.set_xlim(0.015, 100)
ax.set_xlabel("d : distance du piquet au centre (échelle log)")
ax.set_ylabel("G = ρ − max(plateau, hyperbole)")
ax.legend(loc="upper right", fontsize=8.3, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.text(3.0, 3.5e-3, "| : contact intérieur ; avant lui,\nG = 0 : la chèvre s'annule\n● : en d = 1, G = r − s,\n"
        "le ménisque des parties VI et XV\nn = ∞ : G = 0 partout", fontsize=8.3, color=F.INK2, va="top", linespacing=1.4)
ax.set_title("d)  Le ménisque généralisé : nul loin du bord, il vit près du contact")
F.sauver(fig, "p2_menisque_projection.png")
