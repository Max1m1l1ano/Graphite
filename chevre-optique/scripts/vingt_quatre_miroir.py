"""
Partie XXI : les trois 24 se rejoignent en 5² et 7². Le miroir 49-50-51, √7 vu du sommet e₃ et le croisement du plan.

    python3 scripts/vingt_quatre_miroir.py        # ≈ 10 s

Écrit resultats/vingt_quatre_miroir.md, figures/v1_vingt_quatre.png et figures/v2_racine_sept.png.

1. Les trois 24 : 24 + 1 = 5², 2·24 + 1 = 7², 24/6 = 2². Les boulets de Leech (1² + … + 24² = 70²), les nombres
   pentagonaux et η(24τ) = q − q²⁵ − q⁴⁹ + …, le triangle 7-24-25, Δ = η²⁴ et le thêta de Leech, la partie VII.
2. Le miroir 49, 50, 51 : l'inversion, les trois « −1·7² », l'aiguille de 50 et les formules de π à la Machin,
   le doublement de l'aire (Ménon, diaphragme, faisceau gaussien) et les trois paires de tritons.
3. √7 : la boîte 1 × 1 × 2 dont la section est le carré rectifié, vue du sommet e₃ ; Legendre ; les boîtes de √2.
4. Le croisement du plan : l'échelle des chèvres, les cercles inscrit et circonscrit, l'échange √3 ↔ √7, le comma.
"""

import itertools
import logging
import math
import os
import sys
from fractions import Fraction
from math import comb, gcd, isqrt

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.patches import Polygon
from scipy.optimize import brentq
from scipy.special import betainc

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
ROUGE, VIOLET = "#d0342c", "#7d4fc4"
R2 = math.sqrt(2)
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def sup(n):
    return str(n).translate(SUP)


def qp(e):
    return "q" if e == 1 else "q" + sup(e)


def serie(coefs):
    """Écrit une série {exposant: coefficient} : q − 24q² + …"""
    out = ""
    for i, (e, c) in enumerate(sorted(coefs.items())):
        mono = qp(e) if abs(c) == 1 else f"{abs(c)}{qp(e)}"
        out += (("−" if c < 0 else "") if i == 0 else (" − " if c < 0 else " + ")) + mono
    return out


def cents(r):
    return 1200 * math.log2(r)


def deux_carres(n):
    return [(x, y) for x in range(isqrt(n) + 1) for y in range(x, isqrt(n) + 1) if x * x + y * y == n]


def trois_carres(n):
    return [(x, y, z) for x in range(isqrt(n) + 1) for y in range(x, isqrt(n) + 1) for z in range(y, isqrt(n) + 1)
            if x * x + y * y + z * z == n]


def est_trois_carres(n):
    for x in range(isqrt(n // 3) + 1):
        for y in range(x, isqrt((n - x * x) // 2) + 1):
            if carre(n - x * x - y * y):
                return True
    return False


def gmul(*zs):
    """Produit d'entiers de Gauss donnés en couples (a, b) = a + bi."""
    re, im = 1, 0
    for a, b in zs:
        re, im = re * a - im * b, re * b + im * a
    return re, im


def carre(n):
    return n >= 0 and isqrt(n) ** 2 == n


# ---------------------------------------------------------------------------
# 1. Les trois 24
# ---------------------------------------------------------------------------
ligne("## 1. Les trois 24 se rejoignent en 5² et 7²\n")
ligne("24 + 1 = 25 = 5², 2·24 + 1 = 49 = 7², 24/6 = 4 = 2². Les trois candidats passent par ces trois carrés.\n")

SOMME = 24 * 25 * 49 // 6
assert SOMME == sum(k * k for k in range(1, 25)) == 70 ** 2
BOULETS = [n for n in range(1, 200000) if carre(n * (n + 1) * (2 * n + 1) // 6)]
PELL_N = [n for n in range(0, 10 ** 6) if carre(n + 1) and carre(2 * n + 1)]
assert BOULETS == [1, 24] and PELL_N == [0, 24, 840, 28560, 970224]
ligne(f"**Les boulets de Leech.** 1² + 2² + … + 24² = 24·25·49/6 = 2²·5²·7² = {SOMME} = 70². Lucas (1875) demande quand"
      " une pyramide de boulets à base carrée contient un nombre carré de boulets ; Watson (1918) démontre que 24 est la"
      " seule réponse au-delà de 1.")
ligne(f"- Vérifié : 1² + … + n² est un carré pour n < 200 000 seulement en n = {', '.join(map(str, BOULETS))}.")
ligne(f"- n + 1 et 2n + 1 sont tous deux des carrés pour n = {', '.join(map(str, PELL_N))} (n < 10⁶). Alors"
      " (2n + 1) − 2(n + 1) = −1 : ce sont les solutions de Pell de √2. Parmi elles, n/6 n'est un carré qu'en"
      f" n = {', '.join(str(n) for n in PELL_N if n % 6 == 0 and carre(n // 6))}.")
ligne("- Conway (1983) : dans le réseau lorentzien II₂₅,₁ (norme x₀² + … + x₂₄² − x₂₅²), le vecteur"
      " w = (0, 1, 2, …, 24 | 70) est de norme nulle, et le réseau de Leech est w^⊥/w. Borcherds (1990) : w est le"
      " vecteur de Weyl de l'algèbre de Lie du « faux monstre », dont la formule du dénominateur contient"
      " ∏(1 − e^(mw))²⁴, c'est-à-dire Δ = η²⁴.")
ligne("- **Le carré qui manque.** Les 24 carrés de côtés 1 à 24 ont ensemble l'aire du carré 70 × 70, mais ils ne le"
      " pavent pas (vérifié par ordinateur, puis démontré sans ordinateur en 2024). Le meilleur rangement envoyé à"
      " Martin Gardner (environ 250 réponses) laisse vide une aire de 49 = 7² : il omet le carré 7 × 7.\n")

PENTA = sorted({k * (3 * k - 1) // 2 for k in range(-6, 7) if k})
assert all(carre(24 * p + 1) and isqrt(24 * p + 1) % 6 in (1, 5) for p in PENTA)
NQ = 24 * 27
A = [0] * (NQ + 1)
A[1] = 1
for n in range(1, NQ // 24 + 1):
    for e in range(NQ, 24 * n, -1):
        A[e] -= A[e - 24 * n]
ETA24 = {e: c for e, c in enumerate(A) if c}
chi12 = lambda m: 1 if m % 12 in (1, 11) else -1
assert set(ETA24) == {m * m for m in range(1, isqrt(NQ) + 1) if gcd(m, 6) == 1}
assert all(e % 24 == 1 and c == chi12(isqrt(e)) for e, c in ETA24.items())
UNITES24 = [x for x in range(24) if gcd(x, 24) == 1]
assert {x * x % 24 for x in UNITES24} == {1}
ligne(f"**Le pont : les nombres pentagonaux.** Pour tout nombre pentagonal P = k(3k − 1)/2"
      f" ({', '.join(map(str, PENTA[:8]))}…), 24·P + 1 = (6k − 1)² est un carré. Les deux carrés des boulets,"
      " 24·1 + 1 = 5² et 24·2 + 1 = 7², sont les deux premiers. Ce sont aussi les exposants de"
      " η(24τ) = q·∏(1 − q^(24n)), par le théorème pentagonal d'Euler :\n")
ligne(f"η(24τ) = {serie(ETA24)} + …\n")
ligne(f"- Les exposants sont les carrés des nombres premiers avec 6. Ils valent tous 1 modulo 24, parce que les unités"
      f" modulo 24 ({', '.join(map(str, UNITES24))}) ont toutes pour carré 1 (partie XIX : seuls les diviseurs de 24 ont"
      " cette propriété).")
ligne("- Le signe vaut −1 devant 5² et 7², +1 devant 11² et 13², et ainsi de suite (selon n modulo 12) : c'est le"
      " « −1·(7²) ».\n")

ligne("**La paire de Pell (7, 5).** 7² − 2·5² = −1. Les puissances du nombre d'argent :\n")
ligne("| n | (1 + √2)ⁿ | a² − 2b² |")
ligne("|---:|---|---:|")
PELL = []
a, b = 1, 0
for n in range(1, 201):
    a, b = a + 2 * b, a + b
    PELL.append((n, a, b))
    if n <= 8:
        ligne(f"| {n} | {a} + {b if b > 1 else ''}√2 | {fr(a * a - 2 * b * b, '{:+d}')} |")
IMPAIRS = [(x, y) for n, x, y in PELL if n % 2 == 1]
assert all(x * x + 1 == 2 * y * y for x, y in IMPAIRS)
LJ = [(x, y) for x, y in IMPAIRS if carre(y)]
assert LJ == [(1, 1), (239, 169)]
ligne("\n- Les puissances impaires donnent x² + 1 = 2y² : (1, 1), (7, 5), (41, 29), (239, 169)… L'aiguille (x, 1) a"
      " pour carré l'aire doublée du carré de côté y.")
ligne("- Ljunggren (1942) : y n'est lui-même un carré que pour y = 1 et y = 169 = 13², c'est-à-dire que x² + 1 = 2y⁴ n'a"
      " pas d'autre solution que x = 1 et x = 239 (vérifié ici sur les 100 premières solutions).")
ligne("- (1 + √2)⁶ = 99 + 70√2 = (7 + 5√2)² : 70 = 2·5·7, le côté du carré des boulets, est le coefficient de √2.")
assert gmul((7, 1), (7, 1)) == (48, 14) == (2 * 24, 2 * 7) and gmul((4, 3), (4, 3)) == (7, 24)
assert 7 ** 2 + 24 ** 2 == 25 ** 2
ligne("- **Le triangle des boulets.** 2·24 + 1 = 7² veut dire 7² + 24² = 25² : le triangle rectangle 7-24-25, dont"
      " l'hypoténuse 25 = 5² est elle-même un carré. Et 7 + 24i = (4 + 3i)² : c'est le triangle 3-4-5 de la partie XIV,"
      " au carré (angle doublé). La partie XIII l'avait croisé : avec la corde 6/5, la chèvre touche le bord du pré en"
      " (7/25, 24/25).\n")

M = 8
D = [0] * (M + 1)
D[0] = 1
for n in range(1, M + 1):
    for _ in range(24):
        for e in range(M, n - 1, -1):
            D[e] -= D[e - n]
TAU = {e + 1: D[e] for e in range(M)}
assert [TAU[n] for n in range(1, 9)] == [1, -24, 252, -1472, 4830, -6048, -16744, 84480]
sig11 = lambda n: sum(d ** 11 for d in range(1, n + 1) if n % d == 0)
C12 = Fraction(65520, 691)
THETA = {n: C12 * (sig11(n) - TAU[n]) for n in (1, 2, 3)}
assert THETA == {1: 0, 2: 196560, 3: 16773120}
assert all((sig11(n) - TAU[n]) % 691 == 0 for n in range(1, 9))
ligne(f"**Δ = η²⁴ et le réseau de Leech.** Δ = {serie({n: TAU[n] for n in range(1, 6)})} + … Le thêta de Leech (le"
      " nombre de vecteurs de chaque longueur) vaut E₁₂ − (65520/691)·Δ :\n")
ligne("| n | σ₁₁(n) | τ(n) | σ₁₁(n) − τ(n) | × 65520/691 : vecteurs de longueur √(2n) |")
ligne("|---:|---:|---:|---|---:|")
for n in (1, 2, 3):
    dif = sig11(n) - TAU[n]
    ligne(f"| {n} | {sig11(n)} | {fr(TAU[n], '{:d}')} | {dif}" + (f" = {dif // 691}·691" if dif else "")
          + f" | {int(THETA[n]):,} |".replace(",", " "))
ligne("\n- Aucun vecteur de longueur √2, et 196 560 de longueur 2 : le nombre de sphères qui en touchent une dans"
      " l'empilement de Leech, le maximum possible en dimension 24.")
ligne("- Le −24 de τ(2) vient de la puissance 24. La congruence de Ramanujan (1916), τ(n) ≡ σ₁₁(n) (mod 691), rend"
      " tous ces nombres entiers : 2049 − (−24) = 3·691, 177148 − 252 = 256·691 (vérifié jusqu'à n = 8).\n")

K24 = Fraction(comb(24, 12), 2 ** 24)
H = {0: Fraction(1, 2), 1: Fraction(1)}
for n in range(2, 26):
    H[n] = H[n - 2] * Fraction(n - 1, n)
assert K24 == Fraction(676039, 4194304) and 676039 == 7 * 13 * 17 * 19 * 23
assert H[24] == K24 / 2 and K24 * H[25] == Fraction(1, 25) and H[24] * H[25] == Fraction(1, 50)
ligne(f"**La partie VII.** κ₂₄ = C(24, 12)/2²⁴ = {K24} : la chance d'avoir exactement 12 piles en 24 lancers, avec"
      " 676039 = 7·13·17·19·23. Les dimensions 6, 12 et 24 (m = 3, 6, 12, soit 11, 110, 1100 en binaire, deux retenues)"
      " sont les diviseurs de 24 de la forme 3·2ᵏ.")
ligne("- La réciprocité de la partie VII donne κ₂₄·h₂₅ = 1/25 = 1/5², et celle de la partie IV h₂₄·h₂₅ = π/(2·25) = π/50."
      " Le 25 des boulets et le 50 du miroir (§ 2) sont dans la paire de dimensions (24, 25).")
ligne("- Ce qui ne se rejoint pas : le polynôme de degré 24 de la dimension 13 a pour groupe de Galois S₂₄, sans symétrie"
      " particulière. Le réseau de Leech se construit avec le code de Golay, dont la symétrie est M₂₄. Les deux 24 se"
      " rejoignent par l'arithmétique (5², 7², les diviseurs), pas par la symétrie.")

# ---------------------------------------------------------------------------
# 2. Le miroir 49, 50, 51
# ---------------------------------------------------------------------------
ligne("\n## 2. Le miroir 49, 50, 51\n")
RAC50 = [x for x in range(50) if (x * x + 1) % 50 == 0]
assert RAC50 == [7, 43] and (-49) % 50 == 1
ligne("**L'inversion.** Prends 10⁻⁵⁰ comme unité : c'est le miroir, il reste fixe. Alors 10⁻⁴⁹ = 10 et 10⁻⁵¹ = 1/10, et"
      " x ↦ 1/x les échange : 10⁻⁴⁹ × 10⁻⁵¹ = (10⁻⁵⁰)². C'est la forme de Newton x·x′ = f² avec f = 10⁻⁵⁰. Le"
      " grandissement vaut −f/x = −1/10 : l'image est retournée (le −1) et dix fois plus petite. Sur les exposants,"
      " c'est s ↦ 100 − s. Et modulo 50, l'exposant −49 = −1·7² vaut +1, puisque 7² ≡ −1.\n")
CHIFFRES = str(sum(c * 10 ** (NQ - e) for e, c in ETA24.items())).zfill(NQ)
assert all(CHIFFRES[e - 1] in "0189" and (e - 1) % 24 == 0 for e in ETA24)


def plages(s):
    out, i = [], 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        out.append(s[i] if j - i == 1 else f"{s[i]}×{j - i}")
        i = j
    return " ".join(out)


ligne("**Les trois « −1·7² ».**")
ligne("- Dans η(24τ) : le terme −q⁴⁹ = −1·q^(7²). En q = 1/10 (la base 10 comme objet, partie XIX), c'est littéralement"
      f" −1·10⁻⁴⁹. Les 168 premiers chiffres de η(24τ) valent alors 0,{plages(CHIFFRES[:168])} … (« 9×23 » : 23"
      " chiffres 9). Rangés par 24, tous les termes tombent dans la première colonne (figure v1 c).")
ligne(f"- Modulo 50 : 7² = 49 ≡ −1, donc 7 est un i (les racines de −1 modulo 50 sont {RAC50[0]} et {RAC50[1]}). C'est"
      " le théorème de la partie XIX, avec 50 = 7² + 1².")
ligne("- Pell : 7² − 2·5² = −1.\n")
ligne("| n | sommes de deux carrés | sommes de trois carrés |")
ligne("|---:|---|---|")
for n in (49, 50, 51):
    ligne(f"| {n} | {' ; '.join(f'{x}² + {y}²' for x, y in deux_carres(n)) or '—'} |"
          f" {' ; '.join(f'{x}² + {y}² + {z}²' for x, y, z in trois_carres(n))} |")
DEUX_FACONS = next(n for n in range(1, 200) if sum(1 for x, y in deux_carres(n) if x > 0) >= 2)
assert DEUX_FACONS == 50
ligne("\n- 49, 50, 51 = 7², 7² + 1², 7² + 1² + 1² : l'aiguille (7), (7, 1), (7, 1, 1), une dimension de plus à chaque"
      " cran. De 49 à 51, on ajoute 1² + 1² = 2, l'aire du carré construit sur la diagonale du carré unité.")
ligne(f"- {DEUX_FACONS} = 1² + 7² = 5² + 5² : le plus petit nombre qui soit somme de deux carrés non nuls de deux façons."
      " Et 50 = 3² + 4² + 5² : la boîte 3 × 4 × 5 a pour diagonale 5√2, celle du carré 5 × 5, puisque 3² + 4² = 5².\n")

assert gmul((1, -1), (2, 1), (2, 1)) == (7, 1)
assert gmul((2, 1), (2, 1), (7, -1)) == (25, 25) and gmul((3, 1), (3, 1), (7, 1)) == (50, 50)
assert gmul((5, 1), (5, 1), (5, 1), (5, 1), (239, -1)) == (114244, 114244) and 239 ** 2 + 1 == 2 * 13 ** 4
for f_ in (2 * math.atan(1 / 2) - math.atan(1 / 7), 2 * math.atan(1 / 3) + math.atan(1 / 7),
           4 * math.atan(1 / 5) - math.atan(1 / 239)):
    assert abs(f_ - math.pi / 4) < 1e-15
ligne("**L'aiguille de 50.** 7 + i = (1 − i)(2 + i)² : l'aiguille 3-4-5 = (2 + i)², tournée de −45° et agrandie de √2.")
ligne("- Au carré : (7 + i)² = 48 + 14i = 2·(24 + 7i), et |24 + 7i| = 25. Doubler l'angle de l'aiguille de 50 donne"
      f" le triangle des boulets, 7-24-25 ({fr(math.degrees(math.atan2(1, 7)), '{:.2f}')}° × 2 ="
      f" {fr(math.degrees(math.atan2(7, 24)), '{:.2f}')}°).")
ligne("- Avec 45° : (2 + i)²(7 − i) = 25·(1 + i) et (3 + i)²(7 + i) = 50·(1 + i). Ce sont les formules"
      " π/4 = 2 arctan(1/2) − arctan(1/7) (dite de Hermann) et π/4 = 2 arctan(1/3) + arctan(1/7) (dite de Hutton ; les"
      " attributions sont incertaines). 3 et 7 sont i et −i modulo 10 (partie XIX) : leurs aiguilles se complètent"
      " exactement en 45°, la diagonale 1x, 1y.")
ligne("- Machin (1706) : π/4 = 4 arctan(1/5) − arctan(1/239), et 239 + 169√2 = (1 + √2)⁷. On retrouve la solution de"
      " Ljunggren : 239² + 1 = 2·13⁴.\n")

U = np.linspace(0, 3, 30001)
x_img = U / (1 + U ** 2)
assert abs(U[np.argmax(x_img)] - 1) < 1e-3 and abs(1 * (1 / 2) - 0.5) < 1e-15
ligne("**Le doublement de l'aire et la lumière divisée par deux.** Trois lectures exactes :")
ligne("- **Le Ménon (Platon).** Le carré construit sur la diagonale d'un carré a une aire double. Sur le carré 5 × 5,"
      " ça donne 50 = 2·5². Le carré 7 × 7 le manque d'une unité (7² = 2·5² − 1, Pell), et l'aiguille (7, 1) ferme"
      " exactement l'écart : |7 + i|² = 2·5².")
ligne(f"- **Le diaphragme.** √2 sur le diamètre, 2 sur l'aire, ½ sur la lumière ({fr(-10 * math.log10(2))} dB). Une"
      f" décade de longueur (de 10⁻⁵⁰ à 10⁻⁵¹) vaut 100 en aire, soit {fr(math.log2(100), '{:.3f}')} diaphragmes : en base"
      " 10, un cran d'exposant n'est pas un doublement. Il faut un pas de √2.")
ligne("- **Le faisceau gaussien.** Son paramètre complexe q = z + i·z_R (le sommet complexe de la partie XIX) a pour"
      " module √2·z_R aux points de Rayleigh z = ±z_R : la largeur y vaut √2 fois le col, l'aire double, l'intensité"
      " au centre tombe de moitié. La forme de Newton devient x′ = f²·x/(x² + z_R²) (Self, 1983). En x = z_R, l'image est"
      " la plus lointaine et le produit x·x′ tombe à f²/2 (vérifié). La lumière et le produit de Newton sont divisés"
      " par deux au même point, parce que |x + i·z_R|² = 2x² à 45°. Avec f = 1, c'est le produit ½ des jumeaux de la"
      " chèvre (partie XVII).\n")

TRITONS = [("3 (Pythagore)", Fraction(1024, 729), Fraction(729, 512), "le comma pythagoricien"),
           ("5", Fraction(45, 32), Fraction(64, 45), "le diaschisma"),
           ("7", Fraction(7, 5), Fraction(10, 7), "le jubilisma")]
assert all(lo * hi == 2 for _, lo, hi, _ in TRITONS)
assert TRITONS[0][2] / TRITONS[0][1] == Fraction(3 ** 12, 2 ** 19) and TRITONS[2][2] / TRITONS[2][1] == Fraction(50, 49)
assert abs(cents(729 / 512 / R2) - cents(3 ** 12 / 2 ** 19) / 2) < 1e-9
ligne("**Le même miroir en musique.** x ↦ 2/x échange un intervalle et son complément dans l'octave ; il fixe √2 = 600"
      " cents, le triton tempéré. Chaque famille de nombres premiers a sa paire de tritons, symétrique autour de √2 :\n")
ligne("| famille | triton bas | triton haut | écart |")
ligne("|---|---|---|---|")
for fam, lo, hi, nom in TRITONS:
    ligne(f"| {fam} | {lo} = {fr(cents(float(lo)), '{:.2f}')} | {hi} = {fr(cents(float(hi)), '{:.2f}')} |"
          f" {hi / lo} = {fr(cents(float(hi / lo)), '{:.2f}')} cents, {nom} |")
ligne("\n- La gamme à 12 notes met les trois paires sur √2 : elle efface les trois écarts.")
ligne("- (10/7)/(7/5) = 50/49 = 2·5²/7² : le jubilisma est le rapport entre l'aire doublée 2·5² et le carré 7². C'est le"
      " Ménon en musique.")
ligne("- Le triton pythagoricien dépasse √2 d'exactement un demi-comma : (3⁶/2⁹)² = 2 × 3¹²/2¹⁹.")

# ---------------------------------------------------------------------------
# 3. √7
# ---------------------------------------------------------------------------
ligne("\n## 3. √7 : la boîte 1 × 1 × 2, l'octaèdre rectifié et le sommet e₃\n")
COINS = [np.array(c) for c in itertools.product((-1.0, 1.0), (-0.5, 0.5), (-0.5, 0.5))]
E3 = np.array([0.0, 0.0, 1.0])
D2 = sorted({round(float(np.sum((E3 - c) ** 2)), 12) for c in COINS})
assert D2 == [1.5, 3.5] and abs(np.sum((COINS[0] - COINS[-1]) ** 2) - 6) < 1e-12
ligne("**Le montage.** L'octaèdre ±e₁, ±e₂, ±e₃. Le carré Σ_z (e₁, e₂, −e₁, −e₂) et le carré perpendiculaire Σ_x"
      " (e₂, e₃, −e₂, −e₃). On rectifie Σ_x (on le recoupe par les milieux de ses côtés) : on obtient un carré de côté 1,"
      " posé sur le cercle inscrit de Σ_x. On l'étire de −e₁ à e₁ : c'est la boîte 1 × 1 × 2, dont les deux bouts sont"
      " centrés sur ±e₁.")
ligne("- Du sommet e₃, les quatre coins du dessus sont à √(3/2), les quatre du dessous à √(7/2).")
ligne("- En prenant pour unité 1/√2, on obtient **√3 et √7**. Cette unité est l'arête de l'octaèdre rectifié (le"
      " cuboctaèdre), égale à son rayon : le rayon de la sphère des milieux de l'octaèdre.")
ligne("- En demi-unités, le vecteur vers un coin du dessous est (2, 1, 3), et 1² + 2² + 3² = 14 = 2·7 : ton segment"
      " {1, 2, 3} de la partie XIX, divisé par la diagonale √2.")
ligne("- La diagonale de la boîte elle-même vaut √(1 + 1 + 4) = √6.\n")

NON3 = [n for n in range(1, 129) if not est_trois_carres(n)]
assert NON3 == [n for n in range(1, 129) if not trois_carres(n)]
assert all(any(n == 4 ** a_ * (8 * b_ + 7) for a_ in range(4) for b_ in range(17)) for n in NON3)
assert not [k for k in range(1, 201) if est_trois_carres(7 * k * k)]
ligne("**Pourquoi il faut l'unité 1/√2.** 7 n'est pas une somme de trois carrés de fractions. Si 7 = a² + b² + c² avec"
      " des fractions de dénominateur k, alors 7k² est une somme de trois carrés entiers. Écrivons k = 2ᵐ·k′ avec k′"
      " impair : 7k² = 4ᵐ·(7k′²), et 7k′² ≡ 7 (mod 8). C'est la forme interdite de Legendre (1798), 4ᵃ(8b + 7)."
      " Donc **√7 n'est jamais la distance de deux points à coordonnées rationnelles**, dans aucune boîte à côtés"
      f" rationnels (vérifié pour k ≤ 200). Jusqu'à 128, les nombres interdits sont {', '.join(map(str, NON3))}.")
ligne("- Il faut donc une mesure irrationnelle : l'unité 1/√2 (ci-dessus), une arête √2 (la boîte 1 × √2 × 2), ou une"
      " quatrième dimension (la boîte 1 × 1 × 1 × 2).\n")
ligne("**Les boîtes des puissances de √2.** Une boîte de côtés 1, √2, 2, …, (√2)^(k−1) (une dimension par côté) a"
      " pour diagonale √(2ᵏ − 1) : les carrés construits sur ses côtés ont pour aires 1, 2, 4… et chacun double le"
      " précédent.\n")
ligne("| k | côtés | diagonale | 2ᵏ − 1 mod 8 | somme de trois carrés ? |")
ligne("|---:|---|---|---:|---|")
for k in range(1, 7):
    n7 = 2 ** k - 1
    ligne(f"| {k} | {', '.join(['1', '√2', '2', '2√2', '4', '4√2'][:k])} | √{n7} | {n7 % 8} |"
          f" {'oui' if trois_carres(n7) else 'non'} |")
ligne("\n- Du sommet e₃ : √3 = √(2² − 1) et √7 = √(2³ − 1), les diagonales des boîtes 1 × √2 et 1 × √2 × 2.")
ligne("- La boîte 1 × √2 × 2 a pour côtés le rayon, l'arête et le diamètre de l'octaèdre : sa diagonale est √7.")
ligne("- 1, 3, 7 = 2ᵏ − 1 : le nombre d'unités imaginaires des complexes, des quaternions et des octonions (S¹, S³, S⁷,"
      " partie XX). À partir de k = 3, 2ᵏ − 1 ≡ 7 (mod 8) n'est jamais une somme de trois carrés.")
ligne("- Et 49 = 2² + 3² + 6² : la boîte 2 × 3 × 6 a une diagonale entière, 7. Le carré 7² est une somme de trois"
      " carrés, 7 ne l'est pas.")

# ---------------------------------------------------------------------------
# 4. Le croisement du plan
# ---------------------------------------------------------------------------
ligne("\n## 4. Le croisement du plan : la chèvre avant, √2 au croisement\n")


def calotte(n, h):
    if h <= 0:
        return 0.0
    if h >= 2:
        return 1.0
    v = 0.5 * betainc((n + 1) / 2, 0.5, h * (2 - h))
    return v if h <= 1 else 1 - v


def corde(n):
    """Corde de la chèvre de dimension n, piquet sur la clôture (comme rho_moitie(n, 1) de la partie XX)."""
    def recouvre(r):
        x = (2 - r * r) / 2
        return calotte(n, 1 - x) + r ** n * calotte(n, (r - 1 + x) / r)
    return brentq(lambda r: recouvre(r) - 0.5, 0.5, 2.0, xtol=1e-14)


NS = (2, 3, 4, 8, 24, 100)
ALPHA = {n: math.degrees(2 * math.asin(corde(n) / 2)) for n in NS}
assert abs(ALPHA[2] - 70.812) < 1e-3 and all(ALPHA[a_] < ALPHA[b_] < 90 for a_, b_ in zip(NS, NS[1:]))
ligne("Le sommet e₃ tourne dans le plan de Σ_x vers −e₃ (angle φ). Il traverse le plan de Σ_z en e₂ (φ = 90°), un sommet"
      " de Σ_z, sur son cercle circonscrit. Avant d'y arriver, il passe le bord des chèvres de toutes les dimensions,"
      " piquet en e₃ :\n")
ligne("| dimension n | " + " | ".join(map(str, NS)) + " | ∞ |")
ligne("|---|" + "---|" * (len(NS) + 1))
ligne("| bord de la chèvre α_n | " + " | ".join(fr(ALPHA[n], "{:.2f}") + "°" for n in NS) + " | 90° |")
ligne("| écart au croisement 90° − α_n | " + " | ".join(fr(90 - ALPHA[n], "{:.2f}") + "°" for n in NS) + " | 0 |")
ligne("| arcsin(1/(n + 1)) | " + " | ".join(fr(math.degrees(math.asin(1 / (n + 1))), "{:.2f}") + "°" for n in NS)
      + " | 0 |")
ligne("\n- La chèvre de dimension infinie a pour corde l'arête e₃e₂ = √2 : son bord est exactement le croisement.")
ligne("- L'écart se referme comme 1/(n + 1) radian (à un ménisque près, partie XX), et seulement à l'infini, comme le"
      " ménisque de la partie XVI.")
ligne("- Le retournement e₃ → e₂ → −e₃ est i·i = −1 : deux quarts de tour, par le croisement (partie XX).")
phis = np.radians(np.linspace(0, 180, 181))
for th in (45, 135, 225, 315):
    cy, cz = math.cos(math.radians(th)) / R2, math.sin(math.radians(th)) / R2
    for x0 in (-1.0, 1.0):
        Pp = np.stack([np.zeros_like(phis), np.sin(phis), np.cos(phis)], axis=1)
        d2u = 2 * np.sum((Pp - np.array([x0, cy, cz])) ** 2, axis=1)
        assert np.allclose(d2u, 5 - 2 * R2 * np.sin(phis + math.radians(th)))
ligne("\n**Les cercles inscrit et circonscrit.** En unités de 1/√2, le sommet mobile est sur le cercle circonscrit de Σ_x"
      " (rayon √2), et les coins de la section sur son cercle inscrit (rayon 1). Avec la demi-longueur de la boîte (√2) :")
ligne("- d² = 5 − 2√2·sin(φ + θ), où θ est l'angle du coin dans la section (45°, 135°, 225°, 315° ; loi des cosinus,"
      " vérifiée) ;")
ligne("- en e₃, en e₂ et en −e₃, d² vaut 3 ou 7 : √3 et √7 ;")
ligne(f"- à mi-chemin (φ = 45°), le sommet est aligné avec un coin : d² = 2 + (√2 ∓ 1)², avec les nombres d'argent"
      f" √2 ∓ 1 de la partie XVII (d = {fr(math.sqrt(5 - 2 * R2))} et {fr(math.sqrt(5 + 2 * R2))}) ;")
ligne("- au croisement (φ = 90°), la moitié des coins ont échangé √3 et √7 ; en −e₃, tous.")
ligne("\n**Le partage d'aire et le comma au croisement.**")
ligne("- Rayon circonscrit / rayon inscrit = √2 : l'aire du disque inscrit est la moitié de celle du disque"
      " circonscrit. Le cercle inscrit (rayon 1/√2 du pré) est aussi celui des positions qui sont leur propre jumeau"
      " (partie XVII : d = 1/(2d) donne d = 1/√2).")
ligne("- √2 est aussi le triton tempéré, le point fixe de x ↦ 2/x sur l'octave. Les deux chemins de quintes (six vers"
      " le haut, Fa♯ = 729/512 ; six vers le bas, Sol♭ = 1024/729) s'y manquent d'un comma, les tritons de 7 d'un"
      " jubilisma.")
ligne("- Le comma ne s'annule jamais (3ᵃ ≠ 2ᵇ), et l'écart 90° − α_n non plus en dimension finie. La gamme à 12 notes"
      " ferme le premier en tempérant, la dimension infinie ferme le second.")

with open(os.path.join(ICI, "..", "resultats", "vingt_quatre_miroir.md"), "w") as fh:
    fh.write("# Résultats de la partie XXI (générés par scripts/vingt_quatre_miroir.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure v1 : les trois 24 et le miroir 49-50-51
# ===========================================================================
COUL = {2: F.ORANGE, 3: F.JAUNE, 4: F.AQUA, 8: F.SEQ[7], 24: F.SEQ[10], 100: F.SEQ[13]}


def cercle(ax, r, cx=0.0, cy=0.0, t0=0.0, t1=2 * np.pi, **kw):
    t = np.linspace(t0, t1, 400)
    ax.plot(cx + r * np.cos(t), cy + r * np.sin(t), **kw)


def schema(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)


def legende(ax, texte, y=-0.02):
    ax.text(0.5, y, texte, transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)


fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.18, hspace=0.3)

# a) la carte des trois 24
ax = fig.add_subplot(gs[0, 0])


def boite(x, y, txt, c, fs=9.0, gras=False):
    ax.text(x, y, txt, ha="center", va="center", fontsize=fs, color=F.INK, linespacing=1.4, zorder=5,
            fontweight="bold" if gras else "normal",
            bbox=dict(boxstyle="round,pad=0.55", fc=F.SURF, ec=c, lw=1.9))


def lien(a, b, c, txt, at, rad=0.0, ls="-"):
    ax.annotate("", b, a, zorder=3, arrowprops=dict(arrowstyle="-|>", color=c, lw=1.5, ls=ls, shrinkA=4, shrinkB=4,
                                                    connectionstyle=f"arc3,rad={rad}"))
    ax.text(at[0], at[1], txt, ha="center", va="center", fontsize=8.5, color=c, zorder=4, linespacing=1.3,
            bbox=dict(fc=F.SURF, ec="none", alpha=0.92, pad=1.5))


boite(5.0, 5.15, "24 + 1 = 5²    2·24 + 1 = 7²    24/6 = 2²\n7² + 24² = 25²    7² − 2·5² = −1", ROUGE, fs=10.2,
      gras=True)
boite(1.75, 9.0, "Partie VII\n6, 12, 24 : m = 11, 110, 1100\n(deux retenues en base 2)\nκ₂₄ = 676039/2²²", F.BLEU)
boite(8.25, 9.0, "Diviseurs de 24\nles unités ont toutes\npour carré 1 :\n1, 5, 7, 11, 13, 17, 19, 23", F.AQUA)
boite(5.0, 0.75, "Réseau de Leech\nθ = E₁₂ − (65520/691)·Δ\n= 1 + 196 560 q² + 16 773 120 q³ + …", VIOLET)
lien((2.2, 7.75), (3.6, 5.75), F.BLEU, "κ₂₄·h₂₅ = 1/5²\nh₂₄·h₂₅ = π/50", (1.75, 6.55))
lien((7.8, 7.75), (6.4, 5.75), F.AQUA, "η(24τ) = q − q^(5²)\n− q^(7²) + …", (8.3, 6.55))
lien((5.0, 1.75), (5.0, 4.5), VIOLET, "1² + … + 24² = 70²\nw = (0, 1, …, 24 | 70)", (5.0, 3.1))
lien((9.0, 7.75), (6.6, 1.2), F.AQUA, "Δ = η²⁴\nτ(2) = −24", (9.05, 3.4), rad=-0.25)
lien((1.0, 7.75), (3.4, 1.2), F.MUTED, "groupe : S₂₄, pas M₂₄\n(la symétrie\nne passe pas)", (0.95, 3.4), rad=0.25,
     ls="--")
schema(ax, (-0.4, 10.4), (-0.3, 10.3))
ax.set_title("a)  Les trois 24 se rejoignent en 5² et 7²")
legende(ax, "Les trois candidats de la partie XX, reliés par ce qu'ils partagent. Les flèches portent des égalités"
        "\nexactes (§ 1). Seule la symétrie ne passe pas : le polynôme de degré 24 de la partie VII est quelconque"
        "\n(S₂₄) ; le réseau de Leech est exceptionnel (sa symétrie, le groupe de Conway, contient M₂₄).")

# b) η(24τ) : les carrés premiers avec 6
ax = fig.add_subplot(gs[0, 1])
ax.axhline(0, color=F.INK2, lw=0.9)
for e, c in ETA24.items():
    col = F.BLEU if c > 0 else ROUGE
    gros = e in (25, 49)
    ax.plot([e, e], [0, c], color=col, lw=3.0 if gros else 2.0)
    ax.plot([e], [c], "o", ms=13 if gros else 8, color=col, mec=F.SURF, mew=1.6, zorder=5)
    ax.text(e + {25: -4, 49: 4}.get(e, 0), c + 0.16 * c, f"{isqrt(e)}²", ha={25: "right", 49: "left"}.get(e, "center"),
            va="bottom" if c > 0 else "top", fontsize=10, color=col, fontweight="bold")
    ax.text(e, -0.1 * c, f"24·{(e - 1) // 24} + 1" if e > 1 else "1", ha="center", va="top" if c > 0 else "bottom",
            fontsize=7.6, color=F.MUTED, rotation=90)
ax.annotate("les deux carrés\ndes boulets :\n−1·5² et −1·7²", (37, -1.0), (95, -1.55), fontsize=9.2, color=ROUGE,
            ha="left", va="center", fontweight="bold", arrowprops=dict(arrowstyle="-", color=ROUGE, lw=1.0))
ax.set_xlim(-15, NQ + 15)
ax.set_ylim(-1.95, 1.75)
ax.set_xticks([1, 25, 49, 121, 169, 289, 361, 529, 625])
ax.tick_params(axis="x", labelsize=8.2, rotation=0)
ax.set_yticks([-1, 0, 1])
ax.set_xlabel("exposant de q")
ax.set_ylabel("coefficient de η(24τ)")
ax.set_title("b)  η(24τ) : les carrés des nombres premiers avec 6")
legende(ax, "η(24τ) = q·∏(1 − q^(24n)). Le théorème pentagonal d'Euler ne garde que les exposants 24·P + 1, P"
        "\npentagonal (1, 2, 5, 7, 12…) : ce sont des carrés, tous ≡ 1 (mod 24). Les deux premiers après q, 25 et 49,"
        "\nsont ceux des boulets, avec le signe −1. Le signe suit n modulo 12 (bleu +1, rouge −1).", y=-0.13)

# c) les chiffres de η(24τ) en q = 1/10, par rangées de 24
ax = fig.add_subplot(gs[0, 2])
NR, NC = NQ // 24, 24
MAT = np.array([int(ch_) for ch_ in CHIFFRES[:NR * NC]]).reshape(NR, NC)
cmap = ListedColormap(["#efeee8", F.ORANGE] + [F.GRID] * 6 + [ROUGE, F.SEQ[10]])
ax.imshow(MAT, cmap=cmap, vmin=-0.5, vmax=9.5, interpolation="nearest", aspect="equal")
for r in range(NR):
    for c_ in range(NC):
        v = MAT[r, c_]
        ax.text(c_, r, str(v), ha="center", va="center", fontsize=5.6,
                color=F.SURF if v in (8, 9) else (F.INK if v == 1 else F.MUTED))
ax.add_patch(plt.Rectangle((-0.5, -0.5), 1, NR, fill=False, ec=ROUGE, lw=2.0))
ax.set_yticks([(e - 1) // 24 for e in ETA24])
ax.set_yticklabels([("+" if c > 0 else "−") + f"10⁻{sup(e)}  ({isqrt(e)}²)" for e, c in ETA24.items()], fontsize=8.0)
for t_, (e, c) in zip(ax.get_yticklabels(), ETA24.items()):
    t_.set_color(F.BLEU if c > 0 else ROUGE)
ax.set_xticks([0, 5, 11, 17, 23])
ax.set_xticklabels(["1", "6", "12", "18", "24"], fontsize=8.0)
ax.tick_params(axis="x", top=True, labeltop=True, bottom=False, labelbottom=False)
ax.grid(False)
ax.text(24.2, 1, "← le 8 : la retenue\n    de −1·10⁻⁴⁹", fontsize=8.6, color=ROUGE, va="center", fontweight="bold")
ax.text(24.2, 11, "← des rangées\n    entières de 9 :\n    les retenues", fontsize=8.6, color=F.SEQ[10], va="center")
ax.text(24.2, 22, "← les termes +1\n    (orange)", fontsize=8.6, color=F.ORANGE, va="center")
ax.set_xlim(-0.5, 33)
ax.set_title("c)  η(24τ) en q = 1/10, rangé par 24 chiffres")
legende(ax, "Les 648 premiers chiffres de η(24τ) en base 10, 24 par rangée. Chaque terme ±10^(−n²) tombe dans la"
        "\npremière colonne (cadre rouge), parce que n² ≡ 1 (mod 24). Entre deux termes négatifs, les retenues"
        "\nremplissent des rangées de 9 : c'est la base 10 comme objet, avec la grille de 24 qui la range.")

# d) l'aiguille de 50
ax = fig.add_subplot(gs[1, 0])
for i in range(0, 9):
    for j in range(0, 9):
        ax.plot([i], [j], "o", ms=2.2, color=F.BASE, zorder=1)
for r2_, nom in ((5, "|z|² = 5"), (10, "10"), (25, "25"), (50, "50")):
    cercle(ax, math.sqrt(r2_), t0=0, t1=math.pi / 2, color=F.BASE, lw=0.9, ls="--")
    ax.text(math.sqrt(r2_) * math.cos(math.radians(84)) - 0.05, math.sqrt(r2_) * math.sin(math.radians(84)) + 0.12, nom,
            fontsize=7.8, color=F.MUTED, ha="center")
for ang, nom, c in ((math.atan2(7, 24), "24 + 7i\n(norme 25²)", VIOLET),
                   (math.atan2(24, 7), "7 + 24i = (4 + 3i)²", VIOLET), (math.pi / 4, "1 + i : 45°", F.INK)):
    ax.plot([0, 8.4 * math.cos(ang)], [0, 8.4 * math.sin(ang)], color=c, lw=1.1, ls=":")
    ax.text(8.55 * math.cos(ang), 8.55 * math.sin(ang), nom, fontsize=8.6, color=c, linespacing=1.2,
            ha="center" if ang > 1.2 else "left", va="bottom" if ang > 1.2 else "center")
for (x_, y_), nom, c, lw, pos in (((2, 1), "2 + i", F.AQUA, 2.0, (1.75, 1.18, "center", "bottom")),
                                   ((3, 1), "3 + i", F.JAUNE, 2.0, (3.12, 0.98, "left", "top")),
                                   ((3, 4), "3 + 4i = (2 + i)²", F.BLEU, 2.0, (3.12, 4.05, "left", "bottom")),
                                   ((7, 1), "7 + i", ROUGE, 3.0, (7.1, 1.15, "center", "bottom"))):
    ax.annotate("", (x_, y_), (0, 0), arrowprops=dict(arrowstyle="-|>", color=c, lw=lw, shrinkA=0, shrinkB=0), zorder=5)
    ax.text(pos[0], pos[1], nom, fontsize=9.4, color=c, fontweight="bold", ha=pos[2], va=pos[3], zorder=6)
ax.text(11.3, 7.9, "7 + i = (1 − i)·(2 + i)²\n\n(7 + i)² = 2·(24 + 7i)\n|24 + 7i| = 25 = 5²\n\n7 + 24i = (4 + 3i)²\n\n"
        "(2 + i)²·(7 − i) = 25·(1 + i)\n(3 + i)²·(7 + i) = 50·(1 + i)\n\n(5 + i)⁴·(239 − i) = 114 244·(1 + i)",
        fontsize=9.0, va="top", color=F.INK, linespacing=1.3, bbox=dict(fc=F.SURF, ec=F.BASE, pad=5))
schema(ax, (-0.4, 16.9), (-0.6, 9.4))
ax.set_title("d)  L'aiguille de 50 : son carré, 7-24-25, et 45°")
legende(ax, "7 est i modulo 50, l'aiguille (7, 1) a pour norme 50 = 2·5². Doubler son angle donne le triangle des"
        "\nboulets 7-24-25 ; avec 2 + i ou 3 + i (3 est i modulo 10), elle complète exactement 45° : les formules"
        "\nde π dites de Hermann et de Hutton. Machin utilise 239, la 7e puissance d'argent (Ljunggren).")

# e) le miroir des exposants
ax = fig.add_subplot(gs[1, 1])
ax.plot([47.55, 52.45], [0, 0], color=F.INK2, lw=1.2)
xs_ = np.linspace(49, 51, 300)
ax.plot(xs_, 1.05 * np.sqrt(np.clip(1 - (xs_ - 50) ** 2, 0, None)), color=F.BLEU, lw=1.6)
ax.plot([50, 50], [-0.5, 2.5], color=ROUGE, lw=2.0)
for s in range(48, 53):
    ax.plot([s], [0], "o", ms=12 if s in (49, 50, 51) else 7, color=ROUGE if s == 50 else F.INK, mec=F.SURF, mew=1.6,
            zorder=6)
    ax.text(s, -0.17, f"10⁻{sup(s)}", ha="center", va="top", fontsize=10.5, fontweight="bold" if s in (49, 50, 51) else
            "normal", color=ROUGE if s == 50 else F.INK, bbox=dict(fc=F.SURF, ec="none", pad=0.5), zorder=5)
for s, txt in ((49, "7²"), (50, "7² + 1²\n= 5² + 5²"), (51, "7² + 1² + 1²")):
    ax.text(s, -0.62, txt, ha="center", va="top", fontsize=8.8, color=F.BLEU)
ax.text(50, 1.2, "10⁻⁴⁹ × 10⁻⁵¹ = (10⁻⁵⁰)²", ha="center", va="bottom", fontsize=9.6, color=F.BLEU, fontweight="bold",
        bbox=dict(fc=F.SURF, ec="none", pad=1), zorder=5)
ax.text(50.08, 2.42, "miroir 10⁻⁵⁰ (fixe)", ha="left", va="top", fontsize=9.0, color=ROUGE, fontweight="bold")
ax.text(50.08, 2.08, "modulo 50 : −49 ≡ +1,\ncar 7² ≡ −1", ha="left", va="top", fontsize=8.8, color=ROUGE)
PAS = math.log10(R2)
for k in range(-6, 7):
    ax.plot([50 + k * PAS] * 2, [-1.18, -1.36], color=F.AQUA, lw=1.4)
ax.plot([50, 50 + PAS], [-1.55, -1.55], color=F.AQUA, lw=3)
ax.text(50 + PAS + 0.06, -1.55, "1 diaphragme : × √2 (aire × 2, lumière × ½)", fontsize=8.6, color=F.AQUA,
        va="center")
ax.text(48.25, -1.55, "1 décade = 6,644 diaphragmes", fontsize=8.6, color=F.AQUA, va="center", ha="center")
ax.text(50, -2.02, "Newton x·x′ = f² avec f = 10⁻⁵⁰ : grandissement −1/10 (le −1 retourne l'image)", fontsize=8.6,
        color=F.INK2, ha="center", va="center")
ins = ax.inset_axes([0.0, 0.6, 0.33, 0.4])
ins.add_patch(Polygon([(0, 0), (5, 0), (5, 5), (0, 5)], closed=True, fc=F.SEQ[1], ec=F.BLEU, lw=1.2))
ins.add_patch(Polygon([(2.5, -2.5), (7.5, 2.5), (2.5, 7.5), (-2.5, 2.5)], closed=True, fill=False, ec=ROUGE, lw=1.4))
ins.add_patch(Polygon([(8.5, -2.5), (15.5, -1.5), (14.5, 5.5), (7.5, 4.5)], closed=True, fc="#f7dcd9", ec=ROUGE, lw=1.4))
ins.add_patch(Polygon([(8.5, -2.5), (15.5, -2.5), (15.5, 4.5), (8.5, 4.5)], closed=True, fill=False, ec=F.INK2, lw=0.9,
                      ls="--"))
ins.text(2.5, 2.5, "5²", ha="center", va="center", fontsize=8.6, color=F.BLEU)
ins.text(2.5, 8.1, "2·5² = 50", ha="center", va="bottom", fontsize=8.2, color=ROUGE)
ins.text(12, 1.0, "|7 + i|²\n= 50", ha="center", va="center", fontsize=8.0, color=ROUGE)
ins.text(12, 6.2, "7² = 49 (tirets)", ha="center", va="bottom", fontsize=8.0, color=F.INK2)
schema(ins, (-3, 16.2), (-3.2, 10))
ax.set_xlim(47.45, 52.55)
ax.set_ylim(-2.25, 2.6)
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
for s_ in ax.spines.values():
    s_.set_visible(False)
ax.set_title("e)  Le miroir : 10⁻⁴⁹ et 10⁻⁵¹ autour de 10⁻⁵⁰")
legende(ax, "L'inversion de rayon 10⁻⁵⁰ échange 10⁻⁴⁹ et 10⁻⁵¹ (arc bleu). Le doublement de l'aire est un pas de √2"
        "\n(un diaphragme, traits verts), pas un pas de 10. En haut à gauche : les deux carrés d'aire 50, sur la"
        "\ndiagonale de 5 × 5 (Ménon) et sur l'aiguille (7, 1) ; le carré 7 × 7 (tirets) manque d'une unité (Pell).")

# f) le faisceau gaussien : tout se coupe en deux au point de Rayleigh
ax = fig.add_subplot(gs[1, 2])
u = np.linspace(0, 3, 600)
ax.axhline(1, color=F.MUTED, lw=1.0, ls="--")
ax.plot(u, 1 + u ** 2, color=F.ORANGE, lw=2.2, label="aire du faisceau w²/w₀² = 1 + u²")
ax.plot(u, 1 / (1 + u ** 2), color=F.BLEU, lw=2.2, label="intensité au centre I/I₀ = 1/(1 + u²)")
ax.plot(u, u ** 2 / (1 + u ** 2), color=VIOLET, lw=2.2, label="produit de Newton x·x′/f² = u²/(1 + u²)")
ax.plot(u, u / (1 + u ** 2), color=F.AQUA, lw=2.2, label="image x′·z_R/f² = u/(1 + u²)")
ax.plot([], [], color=F.MUTED, lw=1.0, ls="--", label="Newton géométrique (z_R → 0)")
ax.axvline(1, color=ROUGE, lw=1.2, ls="--")
for y_, c in ((2, F.ORANGE), (0.5, ROUGE)):
    ax.plot([1], [y_], "o", ms=11, color=c, mec=F.SURF, mew=1.6, zorder=6)
ax.text(1.06, 1.07, "u = 1 : aire × 2 ; intensité, produit\net image : ½ (l'image au plus loin)", color=ROUGE,
        fontsize=8.8, fontweight="bold", va="bottom")
ax.legend(loc="upper right", fontsize=8.4, frameon=True, facecolor=F.SURF, edgecolor="none")
ins = ax.inset_axes([0.02, 0.56, 0.21, 0.42])
ins.add_patch(Polygon([(0, 0), (1, 0), (1, 1)], closed=True, fc=F.SEQ[1], ec="none"))
ins.annotate("", (1, 1), (0, 0), arrowprops=dict(arrowstyle="-|>", color=ROUGE, lw=2.0, shrinkA=0, shrinkB=0))
ins.plot([0, 1, 1], [0, 0, 1], color=F.INK2, lw=1.2)
ins.text(0.5, -0.1, "x = z_R", ha="center", va="top", fontsize=8.2, color=F.INK2)
ins.text(1.06, 0.5, "i·z_R", ha="left", va="center", fontsize=8.2, color=F.INK2)
ins.text(0.32, 0.62, "√2·z_R", ha="center", va="center", fontsize=8.6, color=ROUGE, fontweight="bold", rotation=45)
ins.text(0.3, 0.08, "45°", fontsize=8.0, color=F.INK2)
schema(ins, (-0.15, 1.45), (-0.3, 1.15))
ax.set_xlim(0, 3)
ax.set_ylim(0, 2.75)
ax.set_xlabel("u = z/z_R (le faisceau)  ou  x/z_R (la position de l'objet)")
ax.set_ylabel("rapport")
ax.set_title("f)  Le faisceau gaussien : tout se coupe en deux en z_R")
legende(ax, "Au point de Rayleigh, |z + i·z_R| = √2·z_R : l'aire double, l'intensité au centre tombe de moitié."
        "\nLa forme de Newton de Self (1983), x′ = f²x/(x² + z_R²), y atteint son maximum, et le produit x·x′ y vaut"
        "\nf²/2 : la moitié du produit géométrique. Avec f = 1, c'est le ½ des jumeaux de la chèvre (partie XVII).",
        y=-0.13)
F.sauver(fig, "v1_vingt_quatre.png")

# ===========================================================================
# Figure v2 : √7, le sommet e₃ et le croisement
# ===========================================================================
fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.18, hspace=0.3)


def vue(az, el):
    a_, e_ = math.radians(az), math.radians(el)
    droite = np.array([-math.sin(a_), math.cos(a_), 0.0])
    haut = np.array([-math.sin(e_) * math.cos(a_), -math.sin(e_) * math.sin(a_), math.cos(e_)])
    oeil = np.array([math.cos(e_) * math.cos(a_), math.cos(e_) * math.sin(a_), math.sin(e_)])
    return (lambda v: np.array([droite @ v, haut @ v])), (lambda v: oeil @ v)


# a) la boîte 1 × 1 × 2 vue du sommet e₃
ax = fig.add_subplot(gs[0, 0])
proj, prof = vue(-140, 22)
e1, e2, e3 = np.eye(3)
SOM = [s * v for v in (e1, e2, e3) for s in (1, -1)]
for a_, b_ in itertools.combinations(SOM, 2):
    if abs(a_ @ b_) < 1e-9:
        pa, pb = proj(a_), proj(b_)
        der = prof(a_) + prof(b_) < -0.2
        ax.plot([pa[0], pb[0]], [pa[1], pb[1]], color=F.BASE, lw=0.9, ls=":" if der else "-", zorder=1)


def poly3(pts, **kw):
    P_ = np.array([proj(p) for p in pts])
    ax.add_patch(Polygon(P_, closed=True, **kw))


poly3([e1, e2, -e1, -e2], fc=ROUGE, alpha=0.06, ec="none")
poly3([e1, e2, -e1, -e2], fill=False, ec=ROUGE, lw=1.4, ls="--")
poly3([e2, e3, -e2, -e3], fc=F.ORANGE, alpha=0.08, ec="none")
poly3([e2, e3, -e2, -e3], fill=False, ec=F.ORANGE, lw=1.6)
RECT = [np.array([0, y_, z_]) for y_, z_ in ((0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5), (0.5, -0.5))]
poly3(RECT, fc=VIOLET, alpha=0.16, ec=VIOLET, lw=1.8)
t_ = np.linspace(0, 2 * np.pi, 300)
for rr, c in ((1 / R2, VIOLET), (1.0, F.ORANGE)):
    C3 = np.array([proj(np.array([0, rr * math.cos(x), rr * math.sin(x)])) for x in t_])
    ax.plot(C3[:, 0], C3[:, 1], color=c, lw=0.9, ls=":")
BOX = {c: np.array(c) for c in itertools.product((-1.0, 1.0), (-0.5, 0.5), (-0.5, 0.5))}
for c1, c2 in itertools.combinations(BOX, 2):
    if sum(1 for u_, v_ in zip(c1, c2) if u_ != v_) == 1:
        p1, p2 = proj(BOX[c1]), proj(BOX[c2])
        der = prof(BOX[c1]) + prof(BOX[c2]) < -0.6
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=F.BLEU, lw=1.0 if der else 2.0, ls="--" if der else "-",
                zorder=3)
PRES, LOIN = np.array([1.0, -0.5, 0.5]), np.array([-1.0, 0.5, -0.5])
for q_, c, nom in ((PRES, F.AQUA, "√3"), (LOIN, ROUGE, "√7")):
    p3, pq_ = proj(e3), proj(q_)
    ax.plot([p3[0], pq_[0]], [p3[1], pq_[1]], color=c, lw=2.6, zorder=5)
    ax.plot([pq_[0]], [pq_[1]], "o", ms=8, color=c, mec=F.SURF, zorder=6)
    m_ = (p3 + pq_) / 2
    ax.text(m_[0] + (0.1 if nom == "√3" else -0.13), m_[1] + 0.03, nom, color=c, fontsize=13, fontweight="bold",
            zorder=7,
            bbox=dict(fc=F.SURF, ec="none", alpha=0.85, pad=1))
for v, nom in ((e1, "e₁"), (-e1, "−e₁"), (e2, "e₂"), (-e2, "−e₂"), (e3, "e₃"), (-e3, "−e₃")):
    p_ = proj(v)
    ax.plot([p_[0]], [p_[1]], "o", ms=8, color=F.INK, mec=F.SURF, zorder=6)
    ax.text(p_[0] + 0.09 * np.sign(p_[0]) + (0.0 if abs(p_[0]) > 0.1 else 0.1), p_[1] + 0.08, nom, fontsize=11,
            fontweight="bold", ha="center", zorder=7, bbox=dict(fc=F.SURF, ec="none", alpha=0.8, pad=0.5))
for i, (txt, c) in enumerate((("Σ_z (e₁, e₂, −e₁, −e₂) : le plan à traverser (tirets)", ROUGE),
                              ("Σ_x (e₂, e₃, −e₂, −e₃) : le carré perpendiculaire", F.ORANGE),
                              ("Σ_x rectifié : côté 1, sur le cercle inscrit de Σ_x", VIOLET),
                              ("la boîte 1 × 1 × 2, de −e₁ à e₁ (bouts centrés sur ±e₁)", F.BLEU))):
    ax.text(-1.62, -1.12 - 0.13 * i, txt, color=c, fontsize=8.8)
schema(ax, (-1.65, 1.65), (-1.62, 1.12))
ax.set_title("a)  La boîte 1 × 1 × 2 vue du sommet e₃")
legende(ax, "On rectifie le carré Σ_x et on l'étire de −e₁ à e₁. Du sommet e₃, les coins du dessus sont à √3, ceux"
        "\ndu dessous à √7, en unités de 1/√2 (l'arête de l'octaèdre rectifié, égale à son rayon). La diagonale de"
        "\nla boîte vaut √6. Sans l'unité 1/√2, √7 serait impossible entre points rationnels (panneau c).")

# b) la spirale des puissances de √2
ax = fig.add_subplot(gs[0, 1])
JAMBES = [1, R2, 2, 2 * R2, 4]
NOMS_J = ["1", "√2", "2", "2√2", "4"]
NOMS_H = ["1", "√3", "√7", "√15", "√31"]
PTS = [np.zeros(2), np.array([1.0, 0.0])]
for L in JAMBES[1:]:
    Pk = PTS[-1]
    PTS.append(Pk + L * np.array([-Pk[1], Pk[0]]) / np.linalg.norm(Pk))
COUL_T = [F.SEQ[2], F.AQUA, ROUGE, F.SEQ[5], F.SEQ[8]]
for k in range(1, 5):
    O_, A_, B_ = PTS[0], PTS[k], PTS[k + 1]
    ax.add_patch(Polygon([O_, A_, B_], closed=True, fc=COUL_T[k], alpha=0.13 if k in (1, 2) else 0.07, ec="none"))
for k in range(1, 6):
    debut = PTS[k - 1]
    ax.plot([debut[0], PTS[k][0]], [debut[1], PTS[k][1]], color=F.INK, lw=2.0)
    m_ = (debut + PTS[k]) / 2
    nrm = np.array([PTS[k][1] - debut[1], -(PTS[k][0] - debut[0])])
    nrm = nrm / np.linalg.norm(nrm)
    ax.text(*(m_ + 0.32 * nrm), f"{NOMS_J[k - 1]}\n(aire {2 ** (k - 1)})", ha="center", va="center", fontsize=8.6,
            color=F.INK)
for k in range(2, 6):
    c = F.AQUA if k == 2 else (ROUGE if k == 3 else F.INK2)
    ax.plot([0, PTS[k][0]], [0, PTS[k][1]], color=c, lw=3.0 if k in (2, 3) else 1.4, zorder=4)
    m_ = 0.55 * PTS[k]
    ax.text(m_[0], m_[1], NOMS_H[k - 1], color=c, fontsize=13 if k in (2, 3) else 10, fontweight="bold",
            ha="center", va="center", zorder=6, bbox=dict(fc=F.SURF, ec="none", alpha=0.85, pad=1))
ax.plot([0], [0], "o", ms=8, color=F.INK, zorder=7)
ax.text(-0.3, 0.05, "O", fontsize=10, fontweight="bold")
proj2, prof2 = vue(-35, 22)
B0 = np.array([2.6, -1.4])
BX = {c: np.array(c) for c in itertools.product((0.0, 1.0), (0.0, R2), (0.0, 2.0))}
for c1, c2 in itertools.combinations(BX, 2):
    if sum(1 for u_, v_ in zip(c1, c2) if u_ != v_) == 1:
        p1, p2 = B0 + 0.95 * proj2(BX[c1]), B0 + 0.95 * proj2(BX[c2])
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=F.BLEU, lw=1.5)
pa, pb = B0 + 0.95 * proj2(BX[(0.0, 0.0, 0.0)]), B0 + 0.95 * proj2(BX[(1.0, R2, 2.0)])
ax.plot([pa[0], pb[0]], [pa[1], pb[1]], color=ROUGE, lw=2.4)
ax.text(B0[0] + 1.5, B0[1] + 1.0, "√7", color=ROUGE, fontsize=12, fontweight="bold")
ax.text(B0[0] + 0.65, B0[1] - 0.75, "la boîte 1 × √2 × 2", color=F.BLEU, fontsize=8.8, ha="center")
schema(ax, (-6.0, 4.6), (-2.4, 3.3))
ax.set_title("b)  Les puissances de √2 et leurs racines : √3, √7, √15…")
legende(ax, "Chaque pas ajoute une jambe (√2)ᵏ perpendiculaire : l'aire de son carré double à chaque fois (1, 2, 4,"
        "\n8, 16) et l'hypoténuse passe de √(2ᵏ − 1) à √(2ᵏ⁺¹ − 1). En 3D, les trois premières jambes peuvent être"
        "\nperpendiculaires entre elles : la boîte 1 × √2 × 2 (rayon, arête, diamètre de l'octaèdre), de diagonale √7.")

# c) Legendre en rangées de 8
ax = fig.add_subplot(gs[0, 2])
NL = 16
for n in range(1, 8 * NL + 1):
    r, c_ = (n - 1) // 8, (n - 1) % 8
    interdit = not trois_carres(n)
    ax.add_patch(plt.Rectangle((c_ - 0.46, -r - 0.42), 0.92, 0.84, fc="#f4c9c4" if interdit else "#f1f0ea",
                               ec=ROUGE if interdit else "none", lw=1.0))
    ax.text(c_, -r, str(n), ha="center", va="center", fontsize=8.6, color=ROUGE if interdit else F.INK2,
            fontweight="bold" if interdit else "normal")
    if n in (1, 3, 7, 15, 31, 63, 127):
        ax.add_patch(plt.Circle((c_, -r), 0.43, fill=False, ec=F.BLEU, lw=1.8))
    if n in (6, 14, 49, 50, 51):
        ax.add_patch(plt.Rectangle((c_ - 0.46, -r - 0.42), 0.92, 0.84, fill=False, ec=VIOLET, lw=2.0))
for c_ in range(8):
    ax.text(c_, 0.75, f"≡ {(c_ + 1) % 8}", ha="center", va="bottom", fontsize=8.6, color=F.INK2)
ax.text(3.5, 1.35, "n modulo 8", ha="center", va="bottom", fontsize=9, color=F.INK2)
ax.text(8.0, -1.0, "rouge : pas somme\nde trois carrés\n(4ᵃ(8b + 7))", fontsize=8.6, color=ROUGE, va="center")
ax.text(8.0, -3.6, "cercle bleu :\n2ᵏ − 1 (1, 3, 7,\n15, 31, 63, 127)", fontsize=8.6, color=F.BLEU, va="center")
ax.text(8.0, -6.4, "cadre violet :\n6 = 1 + 1 + 4 (√6)\n14 = 1 + 4 + 9 (2·7)\n49 = 4 + 9 + 36\n50 et 51", fontsize=8.6,
        color=VIOLET, va="center")
schema(ax, (-0.7, 10.6), (-NL + 0.4, 2.0))
ax.set_title("c)  Legendre : la colonne de 7 n'est jamais somme de trois carrés")
legende(ax, "Les nombres de 1 à 128 rangés par 8 (la base 2 à trois chiffres, partie XIX). Toute la colonne ≡ 7 est"
        "\ninterdite, ainsi que 4 fois ces nombres (28, 60, 92, 112, 124). Donc √7 n'est jamais une distance entre"
        "\npoints rationnels de l'espace. Les 2ᵏ − 1 à partir de 7 sont tous dans la colonne interdite.")

# d) le croisement : e₃ passe le bord de toutes les chèvres avant e₂
ax = fig.add_subplot(gs[1, 0])
ax.add_patch(plt.Circle((0, 0), 1 / R2, fc=VIOLET, alpha=0.08, ec="none"))
cercle(ax, 1, color=F.ORANGE, lw=1.4)
cercle(ax, 1 / R2, color=VIOLET, lw=1.2, ls="--")
ax.add_patch(Polygon([(1, 0), (0, 1), (-1, 0), (0, -1)], closed=True, fill=False, ec=F.ORANGE, lw=1.2))
ax.add_patch(Polygon([(0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5), (0.5, -0.5)], closed=True, fc=VIOLET, alpha=0.12,
                     ec=VIOLET, lw=1.5))
ax.plot([-1.45, 1.45], [0, 0], color=ROUGE, lw=1.4, ls="--")
ax.text(1.2, -0.1, "plan de Σ_z\n(e₁, −e₁, e₂),\nvu par la tranche", color=ROUGE, fontsize=8.6, va="top")
P3 = np.array([0.0, 1.0])
for n in NS:
    a_ = math.radians(ALPHA[n])
    Q_ = np.array([math.sin(a_), math.cos(a_)])
    ax.plot([P3[0], Q_[0]], [P3[1], Q_[1]], color=COUL[n], lw=1.6 if n in (2, 100) else 1.0)
    ax.plot([Q_[0]], [Q_[1]], "o", ms=7, color=COUL[n], mec=F.SURF, zorder=6)
ax.plot([0, 1], [1, 0], color=F.INK, lw=2.4)
for i, n in enumerate(NS):
    ax.text(1.12, 1.18 - 0.11 * i, f"n = {n} : {fr(ALPHA[n], '{:.1f}')}°", color=COUL[n], fontsize=8.6,
            fontweight="bold", va="top")
ax.text(1.12, 1.18 - 0.11 * len(NS), "n = ∞ : 90°, en e₂ ;\nsa corde √2 est l'arête", color=F.INK, fontsize=8.6,
        fontweight="bold", va="top")
tt_ = np.linspace(math.pi / 2, -math.pi / 2, 100)
ax.plot(1.13 * np.cos(tt_), 1.13 * np.sin(tt_), color=F.INK2, lw=1.0)
ax.annotate("", (0.02, -1.13), (0.1, -1.126), arrowprops=dict(arrowstyle="-|>", color=F.INK2, lw=1.0))
ax.text(0.85, -0.98, "i·i = −1 : e₃ → e₂ → −e₃", color=F.INK2, fontsize=8.6, ha="left")
for v, nom, dx, dy in (((0, 1), "e₃ (piquet)", -0.62, 0.06), ((1, 0), "e₂", 0.05, -0.15),
                       ((0, -1), "−e₃", -0.3, -0.16), ((-1, 0), "−e₂", -0.2, -0.15)):
    ax.plot([v[0]], [v[1]], "o", ms=9, color=ROUGE if nom == "e₂" else F.INK, mec=F.SURF, zorder=7)
    ax.text(v[0] + dx, v[1] + dy, nom, fontsize=10, fontweight="bold")
ax.text(0, -0.2, "disque inscrit :\nla moitié de l'aire", color=VIOLET, fontsize=8.4, ha="center", va="top")
schema(ax, (-1.55, 2.0), (-1.3, 1.35))
ax.set_title("d)  Le croisement : toutes les chèvres avant e₂")
legende(ax, "Le plan de Σ_x, vu de face. Piquet en e₃ : la chèvre de dimension n broute jusqu'à l'angle α_n. En"
        "\ntournant vers le plan de Σ_z, le sommet passe tous ces bords ; seule la chèvre infinie (corde √2, l'arête"
        "\ne₃e₂) a son bord sur le croisement. Les coins de la boîte sont sur le cercle inscrit (tirets violets).")

# e) l'échange √3 ↔ √7
ax = fig.add_subplot(gs[1, 1])
ph = np.linspace(0, 180, 721)
for th, c, nom in ((45, F.AQUA, "coin (½, ½)"), (135, F.BLEU, "coin (−½, ½)"), (225, ROUGE, "coin (−½, −½)"),
                   (315, F.ORANGE, "coin (½, −½)")):
    ax.plot(ph, 5 - 2 * R2 * np.sin(np.radians(ph + th)), color=c, lw=2.2, label=nom)
for y_, c in ((3, F.AQUA), (7, ROUGE)):
    ax.axhline(y_, color=c, lw=0.9, alpha=0.6)
for y_ in (5 - 2 * R2, 5 + 2 * R2):
    ax.axhline(y_, color=F.MUTED, lw=0.9, ls="--")
for n in NS:
    ax.axvline(ALPHA[n], color=COUL[n], lw=1.0, alpha=0.8)
ax.axvline(90, color=ROUGE, lw=2.0)
ax.text(91.5, 7.95, "le croisement (e₂)", color=ROUGE, fontsize=9, fontweight="bold")
ax.text(ALPHA[2] - 1.5, 7.95, "bords des chèvres →", color=F.INK2, fontsize=8.4, ha="right")
ax.set_yticks([5 - 2 * R2, 3, 5, 7, 5 + 2 * R2])
ax.set_yticklabels(["5 − 2√2", "3 : √3", "5", "7 : √7", "5 + 2√2"])
ax.set_xticks([0, 45, 90, 135, 180])
ax.set_xticklabels(["0° : e₃", "45°", "90° : e₂", "135°", "180° : −e₃"])
ax.set_xlim(0, 180)
ax.set_ylim(0.75, 8.45)
ax.set_xlabel("angle φ du sommet mobile, de e₃ vers −e₃")
ax.set_ylabel("d² (unité 1/√2)")
ax.legend(loc="lower center", fontsize=8.2, frameon=True, facecolor=F.SURF, edgecolor="none", ncol=4,
          title="les quatre coins de la section (y, z), vus du sommet mobile", title_fontsize=8.2)
ax.text(46, 5 - 2 * R2 - 0.08, "2 + (√2 − 1)²", color=F.MUTED, fontsize=8.4, va="top")
ax.text(150, 5 + 2 * R2 + 0.08, "2 + (√2 + 1)²", color=F.MUTED, fontsize=8.4, va="bottom")
ax.set_title("e)  √3 ↔ √7 : l'échange au croisement")
legende(ax, "La distance du sommet mobile aux coins de la boîte : d² = 5 − 2√2·sin(φ + θ)."
        "\nÀ mi-chemin, le sommet est aligné avec un coin : extrêmes 2 + (√2 ∓ 1)², les nombres"
        "\nd'argent. Au croisement, la moitié des coins ont échangé √3 et √7 ; en −e₃, tous."
        "\nTraits fins : les bords des chèvres du panneau d.", y=-0.13)

# f) au croisement, les tritons se manquent d'un comma
ax = fig.add_subplot(gs[1, 2])
ax.axvline(600, color=F.INK, lw=2.0)
ax.text(600.5, 0.42, "√2 = 600 cents : la gamme à 12 notes", fontsize=8.8, color=F.INK, va="bottom")
COUL_F = [F.BLEU, F.AQUA, ROUGE]
for i, (fam, lo, hi, nom) in enumerate(TRITONS):
    y_ = 3 - i
    cl, ch = cents(float(lo)), cents(float(hi))
    c = COUL_F[i]
    ax.plot([cl, ch], [y_, y_], color=c, lw=4, alpha=0.35, solid_capstyle="butt")
    for x_, fr_ in ((cl, lo), (ch, hi)):
        ax.plot([x_], [y_], "o", ms=11, color=c, mec=F.SURF, mew=1.6, zorder=5)
        ax.text(x_, y_ - 0.17, f"{fr_}\n{fr(x_, '{:.2f}')}", ha="center", va="top", fontsize=8.4, color=c)
    ax.text(600, y_ + 0.13, f"{fam} : {hi / lo} = {fr(cents(float(hi / lo)), '{:.2f}')} cents, {nom}", ha="center",
            va="bottom", fontsize=8.8, color=c, fontweight="bold", bbox=dict(fc=F.SURF, ec="none", alpha=0.9, pad=1))
ax.annotate("", (cents(729 / 512), 3.65), (600, 3.65), arrowprops=dict(arrowstyle="<->", color=F.BLEU, lw=1.0))
ax.text((600 + cents(729 / 512)) / 2, 3.7, "½ comma", ha="center", va="bottom", fontsize=8.2, color=F.BLEU)
ax.text(cents(1024 / 729), 3.62, "Sol♭ : 6 quintes\nvers le bas", ha="center", va="bottom", fontsize=8.0, color=F.BLEU)
ax.text(cents(729 / 512) + 1.0, 3.25, "Fa♯ : 6 quintes\nvers le haut", ha="left", va="bottom", fontsize=8.0,
        color=F.BLEU)
ax.set_xlim(576, 624)
ax.set_ylim(0.3, 4.15)
ax.set_yticks([])
ax.set_xlabel("cents (1200 = une octave)")
ax.set_title("f)  Au croisement, les tritons se manquent d'un comma")
legende(ax, "x ↦ 2/x retourne l'octave autour de √2 (le triton tempéré, 600 cents)."
        "\nChaque famille de nombres premiers a sa paire de tritons, symétrique autour"
        "\nde √2, et un petit écart : le comma (3), le diaschisma (5), le jubilisma 50/49 (7)."
        "\nLa gamme à 12 notes les efface tous au même point.", y=-0.13)
F.sauver(fig, "v2_racine_sept.png")
