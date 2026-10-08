"""
Partie XIX : les bases 2 et 10 sont deux objets. i modulo 10, l'aiguille qui tourne, le trait, le cône et Thalès.

    python3 scripts/bases_objets.py        # ≈ 10 s

Écrit resultats/bases_objets.md, figures/t1_bases_modulaires.png et figures/t2_trait_cone_thales.png.

1. i modulo b : x² ≡ −1 a une solution exactement quand b = a² + c² (a, c premiers entre eux) ; alors i ≡ a/c,
   la pente de l'aiguille (a, c) de la grille. Base 2 : i ≡ 1 (la diagonale 1x, 1y). Base 10 : i ≡ 3, −i ≡ 7.
2. Les subdivisions harmoniques 1/n : finies ou périodiques, la période étant le nombre de pas de l'aiguille « × b ».
3. Deux échelles qui ne se recalent jamais : log10 2 irrationnel, Benford, les quasi-retours 2^10 ≈ 10^3, la virgule
   flottante.
4. Le point, le trait, le cône : pochoirs à trois points (gauche, droite, centre), erreur du point en dimension n,
   cylindre + cône = hyperboloïde (faisceau gaussien), Archimède (la demi-sphère et son cône conjugué se croisent à
   angle droit à la latitude 45°, au-dessus du demi-disque de rayon 1/√2).
5. Le cône des échelles de Thalès.
6. Les deux couches : 2 et 3 (bases 12, 24, 60, 360) puis 10 ; les retenues de bⁿ ; l'escalier des chiffres.
"""

import logging
import math
import os
import sys
from fractions import Fraction

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle, Wedge

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
ICI = os.path.dirname(os.path.abspath(__file__))
ROUGE, VIOLET = "#d0342c", "#7d4fc4"
R2 = math.sqrt(2)
LOG2 = math.log10(2)
md = []


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


def poids_derivee(pts):
    """Poids exacts w_k de f'(0) ≈ Σ w_k f(k·h) / h : dérivées en 0 des polynômes de Lagrange sur les points pts."""
    w = []
    for k, xk in enumerate(pts):
        s = Fraction(0)
        for m, xm in enumerate(pts):
            if m == k:
                continue
            prod = Fraction(1, xk - xm)
            for j, xj in enumerate(pts):
                if j not in (k, m):
                    prod *= Fraction(0 - xj, xk - xj)
            s += prod
        w.append(s)
    return w


def erreur_txt(c, p):
    """Terme d'erreur c·h^(p−1)·f^(p) écrit comme « −11h²·f‴/6 »."""
    signe = "+" if c > 0 else "−"
    num, den = abs(c.numerator), c.denominator
    hp = "h" if p == 2 else "h²"
    prime = {2: "″", 3: "‴"}[p]
    return f"{signe}{num if num != 1 else ''}{hp}·f{prime}" + (f"/{den}" if den != 1 else "")


# ---------------------------------------------------------------------------
# 1. i modulo b
# ---------------------------------------------------------------------------
def racines_i(b):
    return [x for x in range(b) if (x * x + 1) % b == 0]


def aiguilles(b):
    return [(a, c) for a in range(1, int(b ** 0.5) + 1) for c in range(1, a + 1)
            if a * a + c * c == b and math.gcd(a, c) == 1]


ligne("## 1. i modulo b : quand la base a une racine carrée de −1\n")
ligne("x² ≡ −1 (mod b) a une solution exactement quand b est une somme de deux carrés premiers entre eux, b = a² + c²"
      " (aucun facteur premier ≡ 3 mod 4, pas divisible par 4). Alors a² ≡ −c², donc i ≡ a/c (mod b) : la pente de"
      " l'aiguille (a, c) de la grille, modulo le carré de sa longueur.\n")
ligne("| base b | x avec x² ≡ −1 | aiguille (a, c), a² + c² = b | pente a/c mod b |")
ligne("|---:|---|---|---|")
BASES_I = []
for b in range(2, 41):
    r = racines_i(b)
    aig = aiguilles(b)
    if bool(r) != bool(aig):
        raise SystemExit(f"le théorème échoue en b = {b}")
    if r:
        pentes = [(a * pow(c, -1, b)) % b for a, c in aig]
        BASES_I.append((b, r, aig, pentes))
        ligne(f"| {b} | {', '.join(map(str, r))} | {', '.join(f'({a}, {c})' for a, c in aig)} | {', '.join(map(str, pentes))} |")
SANS = [b for b in range(2, 41) if not racines_i(b)]
ligne(f"\nBases de 2 à 40 sans i : {', '.join(map(str, SANS))}. Le théorème est vérifié pour toutes les bases de 2 à 40.")
ligne("\nLes deux horloges de la base 10 :")
ligne(f"- multiplicative : 3¹, 3², 3³, 3⁴ ≡ {', '.join(str(pow(3, k, 10)) for k in range(1, 5))} (mod 10), comme i, −1, −i, 1."
      " Les unités {1, 3, 9, 7} sont les quatre quarts de tour de l'aiguille ;")
ligne("- additive : 27 = 2 × 10 + 7, sur le troisième tour de l'hélice des dizaines. 27 = 3³ est aussi trois quarts de"
      " tour multiplicatifs : −i.")
ligne("- Base 2 : 1 ≡ −1 (mod 2), et 1² = 1 ≡ −1 : i ≡ −i ≡ 1. L'aiguille ne tourne pas.")
ligne("- Base 10 = base 2 × base 5 (restes chinois) : le dernier chiffre décimal porte la parité (mod 2) et un"
      " chiffre de base 5 ; i vit dans la partie mod 5 (2² ≡ −1 mod 5).")

# ---------------------------------------------------------------------------
# 2. Les subdivisions harmoniques 1/n
# ---------------------------------------------------------------------------
def periode(b, n):
    m = n
    for p in range(2, n + 1):
        if b % p == 0:
            while m % p == 0:
                m //= p
    if m == 1:
        return 0
    k, x = 1, b % m
    while x != 1:
        x = x * b % m
        k += 1
    return k


def developpement(num, den, b, k):
    out, r = [], num
    for _ in range(k):
        r *= b
        out.append(r // den)
        r %= den
    return "".join(map(str, out))


ligne("\n## 2. Les subdivisions harmoniques entre deux chiffres\n")
ligne("1/n s'écrit avec un nombre fini de chiffres en base b quand tous les facteurs premiers de n divisent b ;"
      " sinon il est périodique, de période égale au nombre de pas de l'aiguille « × b » sur le cercle des restes"
      " modulo n avant de revenir à son départ.\n")
ligne("| n | 1/n en base 2 | période | 1/n en base 10 | période |")
ligne("|---:|---|---|---|---|")
PER = []
for n in list(range(2, 14)) + [17, 101]:
    p2, p10 = periode(2, n), periode(10, n)
    PER.append((n, p2, p10))
    ligne(f"| {n} | 0,{developpement(1, n, 2, 16)}… | {p2 if p2 else 'fini'} | 0,{developpement(1, n, 10, 12)}… |"
          f" {p10 if p10 else 'fini'} |")
ligne("\n- 1/5 en binaire : 0,0011 0011… (période 4) parce que 2 ≡ i (mod 5) : quatre quarts de tour.")
ligne("- 1/3 en binaire : 0,01 01… (période 2) parce que 2 ≡ −1 (mod 3) : un demi-tour. 1/11 en décimal : période 2,"
      " 10 ≡ −1 (mod 11). 1/101 en décimal : période 4, 10 ≡ i (mod 101).")
ligne(f"- Sur un ordinateur (binaire), 0,1 + 0,2 = {repr(0.1 + 0.2).replace('.', ',')} : 1/10 n'a pas d'écriture finie en"
      " base 2.")

# ---------------------------------------------------------------------------
# 3. Deux échelles qui ne se recalent jamais
# ---------------------------------------------------------------------------
ligne("\n## 3. Deux échelles qui ne se recalent jamais\n")
ligne("log₁₀ 2 est irrationnel : si log₁₀ 2 = p/q, alors 2^q = 10^p = 2^p 5^p, impossible pour p ≥ 1. Sur le cercle"
      f" des décades (log₁₀ x mod 1), multiplier par 2 fait tourner l'aiguille de log₁₀ 2 = {fr(LOG2, '{:.6f}')} tour"
      f" ({fr(360 * LOG2, '{:.2f}')}°), sans jamais retomber exactement au même endroit.\n")
x = LOG2
cf, y = [], x
for _ in range(11):
    a = int(y)
    cf.append(a)
    if y - a < 1e-14:
        break
    y = 1 / (y - a)
ligne(f"Fraction continue : log₁₀ 2 = [0 ; {', '.join(map(str, cf[1:]))}, …]. Quasi-retours (réduites p/q) :\n")
ligne("| p/q | 2^q / 10^p | écart |")
ligne("|---|---|---|")
h0, h1, k0, k1 = 0, 1, 1, 0
CONV = []
for a in cf:
    h0, h1 = h1, a * h1 + h0
    k0, k1 = k1, a * k1 + k0
    CONV.append((h1, k1))
for p, q in CONV[1:8]:
    rap = Fraction(2 ** q, 10 ** p)
    ligne(f"| {p}/{q} | {fr(float(rap), '{:.6f}')} | {fr(100 * (float(rap) - 1), '{:+.3f}')} % |")
ligne(f"\nDécibels : doubler une puissance ajoute 10 log₁₀ 2 = {fr(10 * LOG2, '{:.4f}')} dB, presque 3 dB, à cause de"
      " 2^10 ≈ 10^3.")
ligne("\nLes préfixes : kilo = 10³ mais kibi = 2¹⁰. L'écart se cumule à chaque palier :\n")
ligne("| palier | 2^(10k) / 10^(3k) | écart |")
ligne("|---|---|---|")
for k, nom in enumerate(("kibi / kilo", "mébi / méga", "gibi / giga", "tébi / téra", "pébi / péta"), 1):
    rap = 2 ** (10 * k) / 10 ** (3 * k)
    ligne(f"| {nom} | {fr(rap, '{:.4f}')} | +{fr(100 * (rap - 1), '{:.2f}')} % |")
ligne(f"\nUn disque vendu « 1 To » (10¹² octets, compté en base 10) contient {fr(1e12 / 2 ** 30, '{:.1f}')} Gio : c'est"
      " le « 931 Go » d'un système qui compte en base 2.")
NB = 10000
premiers = [int(str(2 ** n)[0]) for n in range(1, NB + 1)]
freq = [premiers.count(d) / NB for d in range(1, 10)]
ligne(f"\nPremier chiffre des puissances de 2 (n = 1 à {NB}) contre la loi de Benford log₁₀(1 + 1/d) :\n")
ligne("| d | " + " | ".join(str(d) for d in range(1, 10)) + " |")
ligne("|---|" + "---|" * 9)
ligne("| 2^n | " + " | ".join(fr(f, "{:.4f}") for f in freq) + " |")
ligne("| Benford | " + " | ".join(fr(math.log10(1 + 1 / d), "{:.4f}") for d in range(1, 10)) + " |")
ligne("\nEn base 2, le premier chiffre d'un nombre non nul est toujours 1 : la loi de Benford y est triviale.")
GAPS = {}
for M in (10, 30, 93, 100):
    pts = sorted((n * LOG2) % 1 for n in range(M))
    g = np.diff(pts + [pts[0] + 1])
    GAPS[M] = sorted(set(np.round(g, 9)))
ligne("\nThéorème des trois distances (partie XI) pour les points n·log₁₀ 2 mod 1 : "
      + " ; ".join(f"{M} points : {len(v)} longueurs" for M, v in GAPS.items())
      + ". Deux longueurs aux dénominateurs des réduites (10, 93), et plus généralement pour N = m·q_k + q_(k−1) :"
      " 2, 3, 4, 7, 10, 13, 23, 33, …, 93, 103 (correction de la révision 001).")
ligne("\n**L'atlas de la virgule flottante.** Un nombre flottant = mantisse × base^exposant : chaque exposant est une"
      " carte (une décade, ou une « binade » de 1 à 2), découpée en un nombre fixe de pas. L'écart entre deux nombres"
      " voisins grandit avec le nombre (un cône sur deux échelles logarithmiques), et l'écart relatif oscille d'un"
      " facteur égal à la base dans chaque carte : 2 en binaire, 10 en décimal.")

# ---------------------------------------------------------------------------
# 4. Le point, le trait, le cône
# ---------------------------------------------------------------------------
ligne("\n## 4. Le point, le trait, le cône\n")
ligne("**Trois points : à gauche, à droite ou au centre.** On mesure la pente en 0 avec des points espacés de h. Les"
      " segments {−1, 0, 1}, {0, 1, 2} et {1, 2, 3} donnent trois formules : les dérivées en 0 des polynômes de"
      " Lagrange. Erreur de troncature, et sensibilité au bruit des points (écart-type σ chacun, indépendants) :\n")
ligne("| points (en h) | où est 0 | poids | erreur de troncature | bruit (× σ/h) |")
ligne("|---|---|---|---|---|")
POCH = {}
for pts, nom in (((-1, 0), "points à gauche"), ((0, 1), "points à droite"), ((-1, 0, 1), "au centre"),
                 ((0, 1, 2), "au bord"), ((1, 2, 3), "dehors")):
    w = poids_derivee(pts)
    p = len(pts)
    c = sum(wk * Fraction(xk) ** p for wk, xk in zip(w, pts)) / math.factorial(p)
    bruit = math.sqrt(sum(float(wk) ** 2 for wk in w))
    POCH[pts] = (w, c, bruit)
    ligne("| {" + ", ".join(fr(x, "{:d}") for x in pts) + "} | " + nom + " | "
          + ", ".join(str(wk).replace("-", "−") for wk in w) + f" | {erreur_txt(c, p)} | {fr(bruit, '{:.3f}')} |")
b0, b1, b2 = (POCH[k][2] for k in ((-1, 0, 1), (0, 1, 2), (1, 2, 3)))
ligne("\n- À gauche et à droite (deux points), les erreurs sont **opposées** : ±h·f″/2. Le centre est leur moyenne,"
      " et elles s'y annulent : l'erreur tombe à h²·f‴/6.")
ligne(f"- Pour les trois segments de trois points, les erreurs sont dans le rapport 1 : 2 : 11 et le bruit dans le"
      f" rapport 1 : {fr(b1 / b0, '{:.2f}')} : {fr(b2 / b0, '{:.2f}')} (soit 1 : √13 : 7). Le centre gagne sur les deux"
      " tableaux.")
ligne("\nSur le cercle de R pixels, près de sa tangente verticale (x(y) = √(R² − y²), vraie pente 0), la tangente"
      " mesurée penche de (en degrés) :\n")
ligne("| R | h | droite {0, h} | gauche {−h, 0} | centre {−h, 0, h} | bord {0, h, 2h} | dehors {h, 2h, 3h} |")
ligne("|---:|---:|---|---|---|---|---|")


def penche(R, h, pts):
    w = poids_derivee(pts)
    d = sum(float(wk) * math.sqrt(R * R - (xk * h) ** 2) for wk, xk in zip(w, pts)) / h
    return math.degrees(math.atan(d))


for R, h in ((10, 1), (12, 3), (50, 1), (50, 3)):
    cases = [penche(R, h, pts) for pts in ((0, 1), (-1, 0), (-1, 0, 1), (0, 1, 2), (1, 2, 3))]
    ligne(f"| {R} | {h} | " + " | ".join("0 (exact)" if abs(v) < 1e-12 else fr(v, "{:+.2f}" if abs(v) >= 0.01
                                          else "{:+.5f}") for v in cases) + " |")
ligne("\nLa droite et la gauche penchent d'environ ∓h/(2R) radian, en sens contraires ; le centre est exact par"
      " symétrie.")
RF, HF = 12, 3
COL = [y for y in range(-RF, RF + 1) if round(math.sqrt(RF * RF - y * y)) == RF]
x3 = math.sqrt(RF * RF - HF * HF)
ligne(f"\n**La figure t2 a en nombres exacts** (R = {RF}, h = {HF}). La colonne de la tangente compte {len(COL)} pixels"
      f" (|y| ≤ √(R − 1/4) = {fr(math.sqrt(RF - 0.25), '{:.3f}')}) : 4 en haut et 4 en bas, le pixel du centre compté"
      f" dans les deux. Le point du centre est au centre de sa case ; les points en ±h sont en x = √{RF * RF - HF * HF} ="
      f" {fr(x3, '{:.4f}')}, à {fr(x3 - RF, '{:.4f}')} du centre de leur case et à {fr(x3 - RF + 0.5, '{:.4f}')} de sa"
      f" face gauche (la face est à −1/2), soit {fr((RF - x3) * math.sqrt(12), '{:.2f}')} σ. Le seuil du bruit 0,84·√R"
      f" vaut {fr(2 ** -0.25 * math.sqrt(RF), '{:.2f}')}, juste sous h = {HF} ; et √R·σ = √12/√12 = 1 exactement.")
SIG = 1 / math.sqrt(12)
ligne(f"\n**L'erreur du point.** Un pixel arrondit la position : erreur uniforme d'écart-type σ = 1/√12 ="
      f" {fr(SIG, '{:.4f}')} pixel. Avec trois points espacés de h, la courbure (y(−h) − 2y(0) + y(h))/h² a un bruit"
      " √6·σ/h². Elle n'émerge du bruit (1/R > √6·σ/h²) que pour h > (√6·σ·R)^(1/2) ≈ 0,84 √R : il faut environ √R"
      " pixels de chaque côté pour voir qu'un arc est courbé, la longueur de la colonne verticale de la partie XVIII.\n")
ligne("| R | √6·σ·R : h minimal | √R |")
ligne("|---:|---|---|")
for R in (10, 100, 1000):
    ligne(f"| {R} | {fr(math.sqrt(math.sqrt(6) * SIG * R), '{:.2f}')} | {fr(math.sqrt(R), '{:.2f}')} |")
ligne("\n**L'erreur du point en dimension n.** Arrondir un point à la grille, c'est le ramener au centre de sa case :"
      " l'erreur est uniforme dans le cube [−1/2, 1/2]^n. Sa longueur moyenne quadratique vaut √(n/12) ; elle se"
      " concentre de plus en plus autour de cette valeur, et la boule inscrite (rayon 1/2) n'en contient presque plus"
      " rien : en grande dimension, l'erreur vit sur une sphère mince de rayon √(n/12), dans les coins du cube.\n")
ligne("| n | √(n/12) | part du cube dans la boule inscrite | dispersion relative de la longueur |")
ligne("|---:|---|---|---|")
rng = np.random.default_rng(19)
for n in (1, 2, 3, 10, 100):
    e = rng.uniform(-0.5, 0.5, size=(100000, n))
    lon = np.sqrt((e ** 2).sum(axis=1))
    vol = math.exp((n / 2) * math.log(math.pi) - math.lgamma(n / 2 + 1) - n * math.log(2))
    vol_txt = fr(vol, "{:.4f}") if vol > 1e-3 else fr(vol, "{:.1e}").replace("e", " × 10^")
    ligne(f"| {n} | {fr(math.sqrt(n / 12), '{:.4f}')} | {vol_txt} | {fr(lon.std() / lon.mean(), '{:.3f}')} |")
ligne("\nEn dimension 3, l'erreur moyenne quadratique vaut exactement 1/2 voxel (√(3/12) = 1/2).")
ligne("\n**Cylindre + cône = hyperboloïde.** Un point d'erreur w₀ (le trait d'épaisseur 2w₀, un cylindre) et une"
      " direction d'erreur θ (un cône) donnent ensemble l'enveloppe r² = w₀² + θ²z² : un hyperboloïde. C'est le profil"
      " d'un faisceau laser gaussien, où la lumière impose w₀·θ = λ/π : plus le trait est fin, plus le cône s'ouvre.")
for lam, w0 in ((550e-9, 1e-3), (550e-9, 85e-6), (550e-9, 5e-6)):
    th = lam / (math.pi * w0)
    zr = math.pi * w0 ** 2 / lam
    zr_txt = f"{fr(zr, '{:.2f}')} m" if zr > 1 else f"{fr(zr * 1e3, '{:.3g}')} mm"
    ligne(f"- λ = 550 nm, demi-épaisseur w₀ = {fr(w0 * 1e6, '{:g}')} µm : cône θ = {fr(th * 1e3, '{:.3g}')} mrad,"
          f" longueur où le trait reste fin z_R = πw₀²/λ = {zr_txt}.")
ligne("\n**Le même procédé : un cône dont le sommet est déplacé dans l'imaginaire.** r² = w₀² + θ²z² = θ²·|z + i·z_R|²,"
      " avec z_R = w₀/θ. Pour le faisceau laser, c'est la source ponctuelle à distance imaginaire de Deschamps (1971).\n")
ligne("| hyperboloïde | col w₀ | pente θ | w₀·θ | z_R = w₀/θ | forme |")
ligne("|---|---|---|---|---|---|")
for nom, w0, th, forme in (("chèvre de dimension infinie (partie XVI)", 1.0, 1.0, "ρ = \\|d + i\\|"),
                           ("cube qui tourne (partie II)", 1 / R2, R2, "r = √2·\\|z + i/2\\|")):
    zs = np.linspace(0, 5, 11)
    assert np.allclose(np.sqrt(w0 ** 2 + (th * zs) ** 2), th * np.abs(zs + 1j * w0 / th))
    ligne(f"| {nom} | {fr(w0, '{:.4f}')} | {fr(th, '{:.4f}')} | {fr(w0 * th, '{:.0f}')} | {fr(w0 / th, '{:g}')} |"
          f" {forme} |")
ligne("| faisceau laser | w₀ | λ/(π·w₀) | λ/π | π·w₀²/λ | source en z = −i·z_R |")
ligne("\n- Le cube et la chèvre ont w₀·θ = 1 : deux faisceaux de même « longueur d'onde » λ = π (en unités du rayon),"
      " l'un plus serré (z_R = 1/2) que l'autre (z_R = 1).")
ligne(f"- En z = z_R, la largeur vaut √2·w₀ et la phase de Gouy arctan(z/z_R) vaut 45°. Pour la chèvre, d = 1 (le piquet"
      f" sur la clôture) est exactement sa distance de Rayleigh : ρ = |1 + i| = {fr(abs(1 + 1j), '{:.6f}')}, la diagonale"
      " 1x, 1y.")
ligne("\n**Archimède : la demi-sphère et son cône conjugué.** Dans le cylindre de rayon 1 et de hauteur 1, à la hauteur z,"
      " la demi-sphère a pour rayon √(1 − z²) et le cône (sommet au centre) a pour rayon z : (1 − z²) + z² = 1, les deux"
      " tranches remplissent la tranche du cylindre (1/3 + 2/3 du volume).")
ligne("- Les deux surfaces se croisent sur le cercle z = r = 1/√2 (la latitude 45°), et à angle droit : chaque"
      " génératrice du cône est un rayon de la sphère.")
ligne("- Vu de dessus, ce cercle entoure exactement la moitié du disque (π/2) : c'est le demi-disque des parties XVII et"
      " XVIII, et le plateau de la chèvre en dimension 2 (partie XVI).")
ligne("- À l'écran (projection vue de dessus), une surface de pente φ est comprimée d'un facteur cos φ : le cône d'un"
      f" facteur uniforme 1/√2 = {fr(1 / R2, '{:.4f}')}, la demi-sphère d'un facteur √(1 − r²) qui tend vers 0 au bord,"
      " le cylindre complètement (vu par la tranche). C'est pourquoi les parallèles du globe se serrent au bord et s'y"
      " replient (partie XVIII).")
ligne("- Le cône et le cylindre se déroulent à plat sans déformation (courbure de Gauss nulle) ; la demi-sphère non"
      " (theorema egregium de Gauss). Projeter la sphère horizontalement sur le cylindre garde les aires (Archimède,"
      " projection de Lambert) mais déforme les formes ; projeter verticalement sur l'écran comprime par cos φ. Aucune"
      " carte plate ne garde tout.")

# ---------------------------------------------------------------------------
# 5. Thalès
# ---------------------------------------------------------------------------
ligne("\n## 5. Le cône des échelles et Thalès\n")
LUNE_D, LUNE_L = 3474.8e3, 384400e3
SOU = 19.05e-3
ligne(f"Thalès : un objet de taille L à la distance D sous-tend L/D radian. La Lune : {fr(LUNE_D / 1e3, '{:.1f}')} km à"
      f" {fr(LUNE_L / 1e3, '{:.0f}')} km, soit {fr(math.degrees(LUNE_D / LUNE_L), '{:.3f}')}° ; rapport"
      f" D/L = {fr(LUNE_L / LUNE_D, '{:.1f}')}.")
ligne(f"- Un sou (pièce d'un cent, {fr(SOU * 1e3, '{:.2f}')} mm) cache la Lune à {fr(SOU * LUNE_L / LUNE_D, '{:.2f}')} m de l'œil.")
ligne(f"- Une minute d'arc (l'acuité de l'œil) : {fr(0.3 * math.radians(1 / 60) * 1e6, '{:.0f}')} µm à 30 cm (un pixel"
      f" « Retina »), {fr(LUNE_L * math.radians(1 / 60) / 1e3, '{:.0f}')} km sur la Lune.")
ligne(f"- Une décade = log₂ 10 = {fr(math.log2(10), '{:.4f}')} octaves.")

# ---------------------------------------------------------------------------
# 6. Les deux couches : 2 et 3, puis 10
# ---------------------------------------------------------------------------
ligne("\n## 6. Les deux couches : 2 et 3 (12, 24, 60, 360), puis 10\n")


def ordre_mod(x, b):
    k, y = 1, x % b
    while y != 1:
        y, k = y * x % b, k + 1
    return k


def facteurs(b):
    f, p, out = b, 2, []
    while p * p <= f:
        e = 0
        while f % p == 0:
            f, e = f // p, e + 1
        if e:
            out.append(f"{p}{'⁰¹²³⁴⁵⁶⁷⁸⁹'[e] if e > 1 else ''}")
        p += 1
    if f > 1:
        out.append(str(f))
    return " × ".join(out)


ligne("| base | facteurs | racines de −1 | ordres des unités | toute unité est un reflet (x² ≡ 1) |")
ligne("|---:|---|---|---|---|")
COUCHES = {}
for b in (2, 10, 12, 24, 60, 360):
    U = [x for x in range(1, b) if math.gcd(x, b) == 1]
    rac = [x for x in range(b) if (x * x + 1) % b == 0]
    ords = sorted({ordre_mod(x, b) for x in U})
    refl = all(x * x % b == 1 for x in U)
    COUCHES[b] = (rac, ords, refl)
    ligne(f"| {b} | {facteurs(b)} | {', '.join(map(str, rac)) or 'aucune'} | {', '.join(map(str, ords))} |"
          f" {'oui' if refl else 'non'} |")
ASSERT_24 = [b for b in range(2, 200) if all(x * x % b == 1 for x in range(1, b) if math.gcd(x, b) == 1)]
assert ASSERT_24 == [2, 3, 4, 6, 8, 12, 24]
ligne("\n- Les bases où toute unité est son propre inverse (que des reflets, aucun quart de tour) sont exactement les"
      f" diviseurs de 24 : {', '.join(map(str, ASSERT_24))} (vérifié jusqu'à 200).")
ligne("- −1 n'a de racine carrée ni modulo 12, ni 24, ni 60, ni 360 (tous divisibles par 4) ; il en a une modulo 10"
      " (3 ≡ i). Les bases du cercle et de l'heure se coupent bien en 2, 3, 4, 6 ; la base 10 porte le quart de tour.")
ligne("\nDernier chiffre de bⁿ (n = 1, 2, 3, …) :\n")
ligne("| b | base 10 | base 12 |")
ligne("|---:|---|---|")


def cycle_txt(b, B):
    seq = [pow(b, n, B) for n in range(1, 2 * B + 3)]
    for debut in range(len(seq)):
        for per in range(1, B + 1):
            if all(seq[k] == seq[k + per] for k in range(debut, len(seq) - per)):
                avant, boucle = seq[:debut], seq[debut:debut + per]
                nom = {1: "fixe", 2: "demi-tour", 4: "quart de tour"}.get(per, f"période {per}")
                txt = ", ".join(map(str, boucle))
                return (", ".join(map(str, avant)) + " → " if avant else "") + f"{txt} ({nom})"
    return "?"


for b in range(12):
    ligne(f"| {b} | {cycle_txt(b, 10) if b < 10 else '—'} | {cycle_txt(b, 12)} |")
ligne(f"\n- Chiffres fixes (idempotents, e² ≡ e) : base 10 : {', '.join(str(e) for e in range(10) if e * e % 10 == e)} ;"
      f" base 12 : {', '.join(str(e) for e in range(12) if e * e % 12 == e)}. 0 et 1 restent statiques dans toute base ;"
      " 5 et 6 sont les deux interrupteurs de 10 = 2 × 5 (5 ≡ (1 mod 2, 0 mod 5), 6 ≡ (0 mod 2, 1 mod 5)), 4 et 9 ceux"
      " de 12 = 4 × 3.")
ligne("- En base 10, 2, 3, 7 et 8 tournent par quarts de tour ; en base 12, rien ne tourne plus vite qu'un demi-tour.")
ligne("\n**L'escalier des chiffres.** En base 10, bⁿ s'écrit avec ⌊n·log₁₀ b⌋ + 1 chiffres : le bord droit d'une table"
      " des puissances est une droite tracée en pixels, de pente log₁₀ b.\n")
ligne("| b | pente log₁₀ b | rangs n où la marche est haute (un chiffre de plus ; deux pour 12) |")
ligne("|---:|---|---|")
for b in (2, 3, 12):
    lon = [len(str(b ** n)) for n in range(0, 80)]
    assert all(lon[n] == math.floor(n * math.log10(b)) + 1 for n in range(80))
    haut = 2 if b > 10 else 1
    rangs = [n for n in range(1, 80) if lon[n] - lon[n - 1] == haut]
    ligne(f"| {b} | {fr(math.log10(b), '{:.5f}')} | {', '.join(map(str, rangs[:12]))}… |")
lon2 = [len(str(2 ** n)) for n in range(0, 200)]
rangs2 = [n for n in range(1, 200) if lon2[n] > lon2[n - 1]]
ecarts2 = [b_ - a_ for a_, b_ in zip(rangs2, rangs2[1:])]
ligne(f"\n- Pour 2ⁿ, les marches font {', '.join(map(str, ecarts2[:12]))}… : 3 chiffres tous les 10 rangs (2¹⁰ ≈ 10³),"
      " jusqu'à ce que le petit écart de 2,4 % s'accumule et décale le motif (la réduite suivante, 28/93). C'est la"
      " même mécanique que la droite en pixels de la partie XVIII.")
ligne("- 12 = 2² × 3 : log₁₀ 12 = 2·log₁₀ 2 + log₁₀ 3 ; la base 10 transforme les produits de la première couche"
      " (2 et 3) en sommes de pentes.")

with open(os.path.join(ICI, "..", "resultats", "bases_objets.md"), "w") as fh:
    fh.write("# Résultats de la partie XIX (générés par scripts/bases_objets.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure 1 : l'arithmétique des bases
# ===========================================================================
BOITE = dict(fc=F.SURF, ec="none", alpha=0.88, pad=0.4)
fig = plt.figure(figsize=(21, 14.2))
gs = fig.add_gridspec(2, 3, wspace=0.18, hspace=0.22)


def schema(ax, lim):
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.axis("off")


# a) la droite des nombres enroulée en spirale (l'hélice des dizaines vue de dessus)
ax = fig.add_subplot(gs[0, 0])
for n in range(0, 40):
    tour, pos = divmod(n, 10)
    ang = math.radians(90 - 36 * pos)
    rr = 1.0 + 0.42 * tour
    col = {1: F.BLEU, 3: F.ORANGE, 9: ROUGE, 7: VIOLET}.get(pos, F.MUTED)
    gros = n in (1, 3, 9, 27)
    if gros:
        ax.plot([rr * math.cos(ang)], [rr * math.sin(ang)], "o", ms=16, color=col, mec=F.SURF, mew=1.2, zorder=5)
    ax.text(rr * math.cos(ang), rr * math.sin(ang), str(n), fontsize=9 if gros else 8.2, ha="center", va="center",
            color="white" if gros else col, zorder=6, fontweight="bold",
            bbox=None if gros else dict(fc=F.SURF, ec="none", alpha=0.9, pad=0.15))
t = np.linspace(0, 4 * 2 * np.pi, 800)
rr = 1.0 + 0.42 * t / (2 * np.pi)
ax.plot(rr * np.cos(np.pi / 2 - t), rr * np.sin(np.pi / 2 - t), color=F.GRID, lw=1, zorder=1)
for pos, col in ((1, F.BLEU), (3, F.ORANGE), (9, ROUGE), (7, VIOLET)):
    ang = math.radians(90 - 36 * pos)
    ax.plot([0, 2.5 * math.cos(ang)], [0, 2.5 * math.sin(ang)], color=col, lw=0.8, ls=":", zorder=0)
for a_, b_ in ((3, 9), (9, 27)):
    pa = [(1 + 0.42 * (n // 10)) * f(math.radians(90 - 36 * (n % 10))) for n in (a_,) for f in (math.cos, math.sin)]
    pb = [(1 + 0.42 * (n // 10)) * f(math.radians(90 - 36 * (n % 10))) for n in (b_,) for f in (math.cos, math.sin)]
    ax.add_patch(FancyArrowPatch(pa, pb, arrowstyle="-|>", mutation_scale=14, color=F.INK, lw=1.4,
                                 connectionstyle="arc3,rad=0.25", zorder=4))
ax.text(-2.75, -2.55, "La droite des nombres enroulée : un tour = 10. L'angle est n mod 10, le tour est ⌊n/10⌋.\n"
        "Flèches : ×3. 3 → 9 → 27 : 27 = 2 tours + 7. Les rayons 1, 3, 9, 7 sont les unités.", fontsize=8.5,
        color=F.INK2, va="top")
schema(ax, 2.8)
ax.set_ylim(-3.15, 2.8)
ax.set_title("a)  La droite des nombres enroulée (dizaines)")

# b) les horloges multiplicatives
ax = fig.add_subplot(gs[0, 1])
HORL = [(-1.35, 1.35, 10, [1, 3, 9, 7], "mod 10 : ×3", "i ≡ 3, −1 ≡ 9, −i ≡ 7"),
        (1.35, 1.35, 5, [1, 2, 4, 3], "mod 5 : ×2", "i ≡ 2, −1 ≡ 4, −i ≡ 3"),
        (-1.35, -1.75, 13, [1, 8, 12, 5], "mod 13 : ×8", "i ≡ 8, −1 ≡ 12, −i ≡ 5"),
        (1.35, -1.75, 2, [1, 1, 1, 1], "mod 2", "1 ≡ −1 ≡ i ≡ −i")]
for cx, cy, b, cyc, tit, sous in HORL:
    tt = np.linspace(0, 2 * np.pi, 200)
    ax.plot(cx + 0.85 * np.cos(tt), cy + 0.85 * np.sin(tt), color=F.BASE, lw=1.2)
    noms = ["1", "i", "−1", "−i"]
    for k, v in enumerate(cyc):
        ang = math.radians(90 - 90 * k) if b != 2 else math.radians(90)
        px, py = cx + 0.85 * math.cos(ang), cy + 0.85 * math.sin(ang)
        ax.plot([px], [py], "o", ms=17, color=[F.BLEU, F.ORANGE, ROUGE, VIOLET][k] if b != 2 else F.BLEU,
                mec=F.SURF, mew=1.2, zorder=5)
        ax.text(px, py, str(v), ha="center", va="center", color="white", fontsize=9.5, fontweight="bold", zorder=6)
        if b != 2:
            if k in (1, 3):
                ax.text(cx + 1.13 * math.cos(ang), cy + 1.13 * math.sin(ang), noms[k], ha="center", va="center",
                        fontsize=9, color=F.INK2)
    if b != 2:
        for k in range(4):
            a1, a2 = math.radians(90 - 90 * k - 12), math.radians(90 - 90 * (k + 1) + 12)
            ax.add_patch(FancyArrowPatch((cx + 0.6 * math.cos(a1), cy + 0.6 * math.sin(a1)),
                                         (cx + 0.6 * math.cos(a2), cy + 0.6 * math.sin(a2)), arrowstyle="-|>",
                                         mutation_scale=10, color=F.INK2, lw=1.0, connectionstyle="arc3,rad=-0.4"))
    ax.text(cx, cy + 1.12, tit, ha="center", fontsize=9.5, fontweight="bold")
    ax.text(cx, cy - 1.22, sous, ha="center", fontsize=8.5, color=F.INK2, va="top")
ax.text(0, -3.45, "En haut, 1 ; en bas, −1 ; à droite, i ; à gauche, −i. Chaque flèche multiplie par la racine de −1.",
        ha="center", fontsize=8.3, color=F.INK2)
schema(ax, 2.8)
ax.set_ylim(-3.6, 2.7)
ax.set_title("b)  L'aiguille qui tourne d'un quart de tour")

# c) les aiguilles de la grille qui portent un i
ax = fig.add_subplot(gs[0, 2])
for gx in range(0, 7):
    ax.plot([gx, gx], [0, 6.3], color=F.GRID, lw=0.7, zorder=0)
for gy in range(0, 7):
    ax.plot([0, 6.3], [gy, gy], color=F.GRID, lw=0.7, zorder=0)
COUL_A = [F.BLEU, F.AQUA, F.ORANGE, VIOLET, F.JAUNE, ROUGE, F.SEQ[10], F.INK2, F.SEQ[6], F.MUTED]
for k, (b, r, aig, pentes) in enumerate(BASES_I):
    for (a, c), pe in zip(aig, pentes):
        col = COUL_A[k % len(COUL_A)]
        ax.add_patch(FancyArrowPatch((0, 0), (a, c), arrowstyle="-|>", mutation_scale=12, color=col, lw=1.8 if b in (2, 10) else 1.2,
                                     zorder=3))
        ax.text(a + 0.08, c + 0.06, f"{b}: i ≡ {pe}", fontsize=8.3 if b in (2, 10) else 7.6, color=col,
                fontweight="bold" if b in (2, 10) else "normal", zorder=4, bbox=dict(fc=F.SURF, ec="none", alpha=0.8,
                                                                                          pad=0.2))
ax.text(0.15, 5.95, "Aiguille (a, c) : base b = a² + c², i ≡ a/c (mod b).\n(1, 1) : ta diagonale 1x, 1y, base 2, i ≡ 1."
        "\n(3, 1) : base 10, i ≡ 3.", fontsize=8.5, va="top", bbox=dict(fc=F.SURF, ec="none", alpha=0.92, pad=2))
ax.text(0.15, -0.35, "Sans i : 3, 4, 6, 7, 8, 9, 11, 12, 14, 15, 16… (un facteur 4, ou un premier ≡ 3 mod 4)",
        fontsize=8.3, color=F.INK2, va="top")
ax.set_xlim(-0.2, 6.6)
ax.set_ylim(-0.9, 6.5)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("c)  Les bases qui ont un i : les aiguilles de la grille")

# d) les périodes des subdivisions 1/n
ax = fig.add_subplot(gs[1, 0])
ns = np.arange(2, 31)
p2 = np.array([periode(2, n) for n in ns])
p10 = np.array([periode(10, n) for n in ns])
ax.bar(ns - 0.2, p2, width=0.4, color=F.BLEU, label="base 2")
ax.bar(ns + 0.2, p10, width=0.4, color=F.ORANGE, label="base 10")
for n, a, b in zip(ns, p2, p10):
    if a == 0:
        ax.plot([n - 0.2], [0.4], "o", ms=4, color=F.BLEU)
    if b == 0:
        ax.plot([n + 0.2], [0.4], "o", ms=4, color=F.ORANGE)
for n, txt in ((5, "1/5 : 2 ≡ i (mod 5)\n4 quarts de tour"), (3, "1/3 : 2 ≡ −1\ndemi-tour"),
               (11, "1/11 : 10 ≡ −1\ndemi-tour")):
    ax.annotate(txt, (n, periode(2, n) if n != 11 else periode(10, n)), (n + 1.2, 20 if n == 5 else (15 if n == 3 else 25)),
                fontsize=8.3, arrowprops=dict(arrowstyle="-", color=F.INK2, lw=0.8))
ax.set_xlabel("n (subdivision 1/n de l'espace entre deux chiffres)")
ax.set_ylabel("période des chiffres de 1/n (0 = écriture finie, point)")
ax.legend(loc="upper left", fontsize=8.6, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("d)  Les subdivisions 1/n : finies ou périodiques")

# e) le cercle des décades : ×2 = 108,37°, et Benford
ax = fig.add_subplot(gs[1, 1])
for d in range(1, 10):
    a1, a2 = 90 - 360 * math.log10(d + 1), 90 - 360 * math.log10(d)
    ax.add_patch(Wedge((0, 0), 1.0, a1, a2, width=0.22, fc=F.SEQ[2 + d], ec=F.SURF, lw=1.2, alpha=0.9))
    am = math.radians((a1 + a2) / 2)
    ax.text(0.89 * math.cos(am), 0.89 * math.sin(am), str(d), ha="center", va="center", fontsize=9, color="white",
            fontweight="bold")
for n in range(0, 21):
    ang = math.radians(90 - 360 * ((n * LOG2) % 1))
    col = F.ORANGE if n in (0, 10) else F.INK
    ax.plot([0.66 * math.cos(ang)], [0.66 * math.sin(ang)], "o", ms=7 if n in (0, 10) else 5, color=col, zorder=5)
    if n <= 10:
        decal = {0: math.radians(11), 10: math.radians(-11)}.get(n, 0)
        ax.text(0.5 * math.cos(ang + decal), 0.5 * math.sin(ang + decal), f"$2^{{{n}}}$", fontsize=8.6,
                ha="center", va="center", color=col)
ax.text(0.5, -0.02, "Cercle des décades : l'angle est log₁₀ x mod 1. ×2 = un pas de 108,37° (0,30103 tour),\n"
        "jamais exactement périodique. 2¹⁰ = 1024 revient presque au départ (orange) : 2¹⁰ ≈ 10³.\n"
        "Secteurs : les premiers chiffres 1 à 9, de tailles log₁₀(1 + 1/d) (Benford).", fontsize=8.4, ha="center",
        va="top", color=F.INK2, transform=ax.transAxes)
ins = ax.inset_axes([1.32, -0.42, 0.88, 0.8], transform=ax.transData)
ins.bar(range(1, 10), freq, color=F.SEQ[8])
ins.plot(range(1, 10), [math.log10(1 + 1 / d) for d in range(1, 10)], "o", ms=3, color=F.ORANGE)
ins.set_title("1er chiffre de 2ⁿ, n ≤ 10⁴\n(points : Benford)", fontsize=7.5, fontweight="normal")
ins.tick_params(labelsize=6.5)
schema(ax, 1.25)
ax.set_xlim(-1.12, 2.3)
ax.set_ylim(-1.08, 1.12)
ax.set_title("e)  Deux échelles qui ne se recalent jamais")

# f) la virgule flottante : un cône sur deux échelles logarithmiques
ax = fig.add_subplot(gs[1, 2])
xs = np.geomspace(1, 1000, 4000)
ulp2 = 2.0 ** (np.floor(np.log2(xs)) - 4)        # 5 bits significatifs
ulp10 = 10.0 ** (np.floor(np.log10(xs)) - 1)     # 2 chiffres significatifs
ax.loglog(xs, ulp2, color=F.BLEU, lw=1.8, label="base 2, 5 bits : écart entre voisins")
ax.loglog(xs, ulp10, color=F.ORANGE, lw=1.8, label="base 10, 2 chiffres : écart entre voisins")
ax.loglog(xs, xs / 16, color=F.BLEU, lw=0.8, ls=":")
ax.loglog(xs, xs / 10, color=F.ORANGE, lw=0.8, ls=":")
ax.plot([], [], color=F.INK2, lw=0.8, ls=":", label="pointillés : le cône x/16 et x/10")
ax.set_xlabel("le nombre x (échelle log)")
ax.set_ylabel("écart au nombre voisin (échelle log)")
ax.legend(loc="upper left", fontsize=8.3, frameon=True, facecolor=F.SURF, edgecolor="none")
ins = ax.inset_axes([0.08, 0.5, 0.36, 0.24])
ins.semilogx(xs, ulp2 / xs, color=F.BLEU, lw=1.2)
ins.semilogx(xs, ulp10 / xs, color=F.ORANGE, lw=1.2)
ins.set_title("écart relatif : oscille d'un facteur 2\n(binaire) ou 10 (décimal) dans chaque carte", fontsize=7.5,
              fontweight="normal")
ins.tick_params(labelsize=6.5)
ax.set_title("f)  L'atlas des nombres flottants : un cône en marches")
F.sauver(fig, "t1_bases_modulaires.png")

# ===========================================================================
# Figure 2 : le trait, le cône et Thalès
# ===========================================================================
fig = plt.figure(figsize=(21, 14.2))
gs = fig.add_gridspec(2, 3, wspace=0.2, hspace=0.32)

# a) trois points : à gauche, à droite, au centre, au bord
ax = fig.add_subplot(gs[0, 0])
RP = 12
for yy in range(-7, 8):
    xx = round(math.sqrt(RP * RP - yy * yy))
    ax.add_patch(Rectangle((xx - 0.5, yy - 0.5), 1, 1, fc=F.SEQ[3], ec="white", lw=0.8))
ty = np.linspace(-7.5, 7.5, 200)
ax.plot(np.sqrt(RP * RP - ty * ty), ty, color=F.INK, lw=1.4)
h = 3
xc = lambda yv: math.sqrt(RP * RP - yv * yv)  # noqa: E731
yy_ = np.array([-7.5, 7.5])
for pts, c, ls, nom in (((0, 1), ROUGE, "-", "droite (+) {0, h}"), ((-1, 0), VIOLET, "-", "gauche (−) {−h, 0}"),
                        ((-1, 0, 1), F.AQUA, "-", "centre {−h, 0, h}"), ((0, 1, 2), F.ORANGE, "--", "bord {0, h, 2h}")):
    w = poids_derivee(pts)
    d = sum(float(wk) * xc(xk * h) for wk, xk in zip(w, pts)) / h
    ang = math.degrees(math.atan(d))
    ang_txt = "0° exact" if abs(ang) < 1e-9 else f"{fr(ang, '{:+.1f}')}°"
    ax.plot(RP + d * yy_, yy_, color=c, lw=2 if ls == "-" else 1.8, ls=ls, label=f"{nom} : {ang_txt}")
for yv, c in ((0, F.INK), (h, ROUGE), (-h, VIOLET), (2 * h, F.ORANGE)):
    ax.plot([xc(yv)], [yv], "o", ms=7, color=c, mec=F.SURF, zorder=6)
ax.set_xlim(RP - 6.5, RP + 3)
ax.set_ylim(-7.5, 7.5)
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.01), fontsize=8.3, frameon=False, ncol=2)
ax.text(0.5, -0.135, f"Cercle de {RP} pixels près de sa tangente verticale, h = {h} (carrés : les pixels). Le segment est"
        " vertical :\nla droite (+) est en haut. La droite et la gauche penchent en sens contraires d'environ h/(2R) ;"
        "\nle centre est leur moyenne, exacte. Le bord (ordre 2) penche peu, mais amplifie le bruit 3,6 fois plus.",
        fontsize=8.4,
        va="top", ha="center", transform=ax.transAxes, color=F.INK2)
ax.set_title("a)  Trois points : à gauche, à droite ou au centre")

# b) l'erreur du point amplifiée par la dérivée
ax = fig.add_subplot(gs[0, 1])
hs = np.geomspace(1, 300, 200)
for R, c in ((10, F.SEQ[6]), (100, F.SEQ[9]), (1000, F.SEQ[12])):
    ax.loglog(hs, np.full_like(hs, 1 / R), color=c, lw=1.2, ls="--")
    ax.text(1.05, 1.12 / R, f"courbure vraie 1/R, R = {R}", fontsize=8, color=c)
    hm = math.sqrt(math.sqrt(6) * SIG * R)
    ax.plot([hm], [1 / R], "o", ms=7, color=c, zorder=5)
ax.loglog(hs, math.sqrt(6) * SIG / hs ** 2, color=ROUGE, lw=2, label="bruit de la courbure : √6·σ/h²")
ax.loglog(hs, SIG / (R2 * hs), color=F.AQUA, lw=1.6, label="bruit de la pente (centre) : σ/(√2·h)")
ax.loglog(hs, POCH[(0, 1, 2)][2] * SIG / hs, color=F.ORANGE, lw=1.4, ls="--", label="bruit de la pente (bord) : 2,55·σ/h")
ax.set_xlabel("écart h entre les trois points (pixels)")
ax.set_ylabel("erreur (pente : sans unité ; courbure : 1/pixel)")
ax.legend(loc="upper right", fontsize=8.3, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.text(1.1, 2e-5, "● : la courbure sort du bruit en h ≈ 0,84 √R.\nIl faut ~√R pixels pour voir qu'un arc est courbé\n"
        "(la colonne verticale de la partie XVIII).", fontsize=8.4, color=F.INK2)
ax.set_ylim(1e-5, 2)
ax.set_title("b)  L'erreur du point (σ = 1/√12) amplifiée par la dérivée")

# c) cylindre + cône = hyperboloïde
ax = fig.add_subplot(gs[0, 2])
z = np.linspace(-3, 3, 400)
for w0, th, c, nom in ((1.0, 1.0, F.INK, "chèvre en dimension ∞ : ρ² = 1 + d² (col 1, 45°)"),
                       (1 / R2, R2, F.AQUA, "cube qui tourne (II) : r² = 1/2 + 2z² (col √2/2, pente √2)"),
                       (0.5, 2.0, F.BLEU, "trait fin : col 0,5, pente 2"),
                       (2.0, 0.5, F.ORANGE, "trait épais : col 2, pente 0,5")):
    r = np.sqrt(w0 ** 2 + (th * z) ** 2)
    ax.plot(z, r, color=c, lw=2 if c in (F.INK, F.AQUA) else 1.6, label=nom)
    ax.plot(z, -r, color=c, lw=2 if c in (F.INK, F.AQUA) else 1.6)
ax.plot(z, np.abs(z), color=F.MUTED, lw=0.8, ls=":")
ax.plot(z, -np.abs(z), color=F.MUTED, lw=0.8, ls=":")
ax.axhline(1, color=F.MUTED, lw=0.8, ls="--")
ax.axhline(-1, color=F.MUTED, lw=0.8, ls="--")
ax.text(-2.95, 1.08, "cylindre (le trait)", fontsize=8.2, color=F.MUTED)
ax.text(2.5, 1.15, "cône\n(la direction)", fontsize=8.2, color=F.MUTED, ha="center", va="bottom")
ax.set_xlabel("z (le long du trait)")
ax.set_ylabel("rayon r")
ax.set_ylim(-4.2, 4.2)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=7.9, frameon=False, ncol=2)
ax.text(0, 4.05, "r² = w₀² + θ²z² : cylindre² + cône²\nfaisceau laser : w₀·θ = λ/π\nici w₀·θ = 1 pour les quatre",
        fontsize=8.3, va="top", ha="center", color=F.INK2, bbox=dict(fc=F.SURF, ec="none", alpha=0.85, pad=1))
ax.set_title("c)  Cylindre + cône = hyperboloïde (le trait de lumière)")

# d) Archimède : la demi-sphère et son cône conjugué, de face et de dessus (épure de Monge)
ax = fig.add_subplot(gs[1, 0])
rr_ = np.linspace(0, 1, 300)
YC = -1.32                                         # centre de la vue de dessus
ax.add_patch(Rectangle((-1, 0), 2, 1, fc=F.SEQ[1], ec=F.INK, lw=1.2))
for sg in (1, -1):
    ax.fill_between(sg * rr_, 0, np.sqrt(1 - rr_ ** 2), color=F.BLEU, alpha=0.3, lw=0)
    ax.plot(sg * rr_, np.sqrt(1 - rr_ ** 2), color=F.BLEU, lw=2)
    ax.plot(sg * rr_, rr_, color=F.ORANGE, lw=2)
    ax.plot([sg / R2], [1 / R2], "o", ms=9, color=ROUGE, mec=F.SURF, zorder=6)
    ax.plot([sg / R2, sg / R2], [1 / R2, YC], color=ROUGE, lw=0.9, ls=":", zorder=5)
ax.plot([-1 / R2, 1 / R2], [1 / R2, 1 / R2], color=ROUGE, lw=1, ls="--")
zz = 0.4
ax.annotate("", (-math.sqrt(1 - zz * zz), zz), (0, zz), arrowprops=dict(arrowstyle="<->", color=F.BLEU, lw=1.0))
ax.text(-0.45, zz + 0.03, "√(1 − z²)", fontsize=8.4, color=F.BLEU, ha="center")
ax.annotate("", (zz, zz), (0, zz), arrowprops=dict(arrowstyle="<->", color=F.ORANGE, lw=1.0))
ax.text(zz / 2, zz - 0.11, "z", fontsize=9, color=F.ORANGE, ha="center")
ax.annotate("croisement\nà angle droit\nen z = r = 1/√2\n(latitude 45°)", (1 / R2 + 0.04, 1 / R2), (1.1, 0.62),
            fontsize=8.3, color=ROUGE, va="center", ha="left",
            arrowprops=dict(arrowstyle="->", color=ROUGE, lw=0.9))
ax.text(-1, 1.04, "demi-sphère : √(1 − z²)", fontsize=8.6, color=F.BLEU, ha="left", va="bottom")
ax.text(1, 1.04, "cône : z", fontsize=8.6, color=F.ORANGE, ha="right", va="bottom")
tt = np.linspace(0, 2 * np.pi, 300)
ax.fill(np.cos(tt), YC + np.sin(tt), color=F.SEQ[2], lw=0)
ax.fill(np.cos(tt) / R2, YC + np.sin(tt) / R2, color=F.SEQ[5], lw=0)
ax.plot(np.cos(tt) / R2, YC + np.sin(tt) / R2, color=ROUGE, lw=1.2, ls="--")
ax.plot(np.cos(tt), YC + np.sin(tt), color=F.INK, lw=1.2)
ax.text(0, YC, "π/2\nla moitié", ha="center", va="center", fontsize=9, color="white", fontweight="bold")
ax.text(-1.22, 0.5, "de face", rotation=90, ha="center", va="center", fontsize=9, color=F.INK2)
ax.text(-1.22, YC, "de dessus", rotation=90, ha="center", va="center", fontsize=9, color=F.INK2)
ax.text(0.5, -0.02, "À chaque hauteur z : (1 − z²) + z² = 1, les deux tranches font celle du cylindre.\n"
        "Volumes : demi-sphère 2/3, cône 1/3 du cylindre (Archimède). De dessus (épure de\nMonge, lignes de rappel"
        " en pointillés) : le cercle de 45° enferme la moitié du disque,\nπ/2, et l'anneau l'autre moitié : le"
        " demi-disque des parties XVII et XVIII.", fontsize=8.4, color=F.INK2, ha="center", va="top",
        transform=ax.transAxes)
ax.set_xlim(-1.35, 1.95)
ax.set_ylim(YC - 1.08, 1.22)
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("d)  Archimède : la demi-sphère et son cône, à 45°")

# e) la compression à l'écran
ax = fig.add_subplot(gs[1, 1])
rr2 = np.linspace(0, 0.999, 400)
ax.plot(rr2, np.sqrt(1 - rr2 ** 2), color=F.BLEU, lw=2, label="demi-sphère : cos φ = √(1 − r²)")
ax.plot(rr2, np.full_like(rr2, 1 / R2), color=F.ORANGE, lw=2, label="cône à 45° : 1/√2 partout")
ax.plot([1, 1], [0, 1], color=F.INK, lw=2, label="cylindre : vu par la tranche (0)")
ax.axvline(1 / R2, color=ROUGE, lw=0.9, ls="--")
ax.text(1 / R2 + 0.01, 0.95, "r = 1/√2 :\nles deux se croisent", fontsize=8.3, color=ROUGE, va="top")
ax.fill_between(rr2, 0, np.sqrt(1 - rr2 ** 2), where=np.sqrt(1 - rr2 ** 2) < 0.2, color=ROUGE, alpha=0.15, lw=0)
ax.text(0.83, 0.05, "repli des\nparallèles", fontsize=8.2, color=ROUGE)
ax.set_xlabel("rayon r à l'écran (vue de dessus)")
ax.set_ylabel("compression de la surface à l'écran (cos de la pente)")
ax.set_xlim(0, 1.05)
ax.set_ylim(0, 1.05)
ax.legend(loc="lower left", fontsize=8.3, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("e)  À l'écran : la pente comprime la surface")

# f) le cône des échelles de Thalès
ax = fig.add_subplot(gs[1, 2])
LX = np.linspace(-4, 12, 50)
for ang, nom, c in ((1.0, "1 radian", F.MUTED), (LUNE_D / LUNE_L, "0,52° : Lune, Soleil, sou à 2,1 m", F.ORANGE),
                    (math.radians(1 / 60), "1′ : limite de l'œil", ROUGE)):
    ax.plot(LX, LX + math.log10(ang), color=c, lw=1.4 if c != F.MUTED else 0.9, ls="-" if c != F.MUTED else ":",
            label=nom)
OBJ = [(0.3, 85e-6, "pixel « Retina » à 30 cm", 0.3, 0.55, "left"), (0.3, 70e-6, "cheveu", -0.25, -0.2, "right"),
       (0.6, SOU, "sou à bout de bras", -0.25, 0.4, "right"),
       (SOU * LUNE_L / LUNE_D, SOU, "sou qui cache la Lune (2,1 m)", 0.3, -0.25, "left"),
       (LUNE_L, LUNE_D, "Lune", 0.3, 0.1, "left"), (1.496e11, 1.3927e9, "Soleil", -0.25, 0.35, "right"),
       (LUNE_L, 112e3, "détail le plus fin\nvisible sur la Lune (112 km)", 0.3, -0.2, "left"),
       (1.0, 1.0, "échelle humaine", 0.3, 0.1, "left")]
for d_, l_, nom, dx, dy, ha in OBJ:
    ax.plot([math.log10(d_)], [math.log10(l_)], "o", ms=7, color=F.INK, zorder=5)
    ax.text(math.log10(d_) + dx, math.log10(l_) + dy, nom, fontsize=8, va="center", ha=ha, zorder=6,
            bbox=dict(fc=F.SURF, ec="none", alpha=0.85, pad=0.3))
for k in range(-4, 13):
    for j in range(1, 4):
        ax.axvline(k + j * LOG2, color=F.GRID, lw=0.35, zorder=0)
ax.set_xlim(-1.5, 12)
ax.set_ylim(-5, 10)
ax.set_xlabel("log₁₀ distance (m) — traits fins : les octaves")
ax.set_ylabel("log₁₀ taille (m)")
ax.legend(loc="upper left", fontsize=8.2, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_title("f)  Le cône des échelles : Thalès sur deux échelles log")
F.sauver(fig, "t2_trait_cone_thales.png")
