"""
Partie XX : deux chèvres au même endroit. Les faisceaux des n-sphères, le losange de √2 et la figure de diffraction.

    python3 scripts/sphere_faisceaux.py        # ≈ 40 s

Écrit resultats/sphere_faisceaux.md, figures/u1_chevres_faisceaux.png et figures/u2_cartes_losange.png.

1. La chèvre de dimension n, piquet sur la clôture. Dans le plan méridien, la division d'intégrales complexes d'Ullisch
   donne la corde de toutes les dimensions ; cordes certifiées à 50 chiffres par arithmétique d'intervalles.
2. Pair et impair : la récurrence h_n = (n − 1)/n · h_{n−2} de la partie IV, les seuils 3, 6 et 8, la part de clôture.
3. Les faisceaux : n + 1 chèvres placées sur un simplexe couvrent la clôture S^{n−1}, et leur nerf calcule la
   cohomologie de la sphère ; les deux cartes stéréographiques et l'inversion de rayon √2 ; pair et impair (χ, i).
4. Le losange de √2 dans la figure de diffraction : réseau inversé, polytope croisé, retournement de l'aiguille.
5. 3, 8, 24 : le trou profond √n/2, E8 et D4.
6. La musique (2 et 3 donnent 12) et l'IA (√2 en grande dimension).
7. 10⁻⁵⁰ : une précision, et une échelle physique.
"""

import itertools
import logging
import math
import os
import sys
from decimal import ROUND_CEILING, ROUND_FLOOR, Decimal, getcontext
from fractions import Fraction

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from mpmath import iv
from matplotlib.patches import Polygon
from scipy.optimize import brentq
from scipy.special import betainc

sys.path.insert(0, os.path.dirname(__file__))
import figures as F  # noqa: E402  (style et palette des parties précédentes)

logging.getLogger("matplotlib").setLevel(logging.ERROR)
np.seterr(all="ignore")
ICI = os.path.dirname(os.path.abspath(__file__))
ROUGE, VIOLET = "#d0342c", "#7d4fc4"
R2 = math.sqrt(2)
md = []
getcontext().prec = 140


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


def mpfr(x, k):
    """mp.nstr à la française (virgule décimale)."""
    return mp.nstr(x, k).replace(".", ",").replace("-", "−")


def borne(x, sens, chiffres):
    """Borne décimale sûre d'un intervalle : arrondie vers le bas (sens = −1) ou vers le haut (sens = +1)."""
    bas_, haut_ = str(x).strip("[]").split(",")
    v = Decimal(bas_.strip() if sens < 0 else haut_.strip())
    return v.quantize(Decimal(1).scaleb(-chiffres), rounding=ROUND_FLOOR if sens < 0 else ROUND_CEILING)


# ---------------------------------------------------------------------------
# L'équation de la chèvre de dimension n dans le plan méridien
# ---------------------------------------------------------------------------
# Pré : boule unité de dimension n ; piquet P sur la clôture ; corde ρ. Dans le plan qui contient O et P, la corde
# touche la clôture sous l'angle α vu du centre : ρ = 2 sin(α/2). La moitié du pré est broutée quand
#   I_n(α) + ρⁿ·I_n(π/2 − α/2) = ½·I_n(π),   avec I_n(θ) = ∫₀^θ sinⁿ t dt
# (une calotte du pré et une calotte de la boule de la chèvre). En β = π − α, c'est la fonction d'Ullisch pour n = 2.


def I_n(n, th, ctx):
    """I_n(θ) = ∫₀^θ sinⁿ t dt, par la formule de réduction (valable pour θ complexe et en intervalles)."""
    if n == 0:
        return th
    if n == 1:
        return 1 - ctx.cos(th)
    return -ctx.sin(th) ** (n - 1) * ctx.cos(th) / n + ctx.mpf(n - 1) / n * I_n(n - 2, th, ctx)


def G(n, b, ctx=mp):
    """L'équation en β = π − α : zéro réel β_n, corde ρ_n = 2 cos(β_n/2). Pour n = 2, G = f/2 (Ullisch)."""
    a = ctx.pi - b
    return -(I_n(n, a, ctx) + (2 * ctx.sin(a / 2)) ** n * I_n(n, ctx.pi / 2 - a / 2, ctx) - I_n(n, ctx.pi, ctx) / 2)


class NP:  # le même calcul en nombres complexes rapides (numpy), pour compter les zéros
    pi, sin, cos = np.pi, staticmethod(np.sin), staticmethod(np.cos)
    mpf = staticmethod(float)


def enroulement(n, c, R, K=40000, precis=False):
    """Nombre de zéros de G_n dans le disque |β − c| < R (principe de l'argument). En double précision par défaut ;
    precis=True évalue G_n en mpmath (30 chiffres), indispensable près de la racine réelle quand n est grand."""
    t = np.linspace(0, 2 * np.pi, K + 1)
    if precis:
        v = [complex(G(n, mp.mpc(c) + R * mp.e ** (1j * mp.mpf(float(s))))) for s in t]
    else:
        v = G(n, c + R * np.exp(1j * t), NP)
    ang = np.unwrap(np.angle(v))
    assert np.max(np.abs(np.diff(ang))) < 1.0, f"échantillonnage trop lâche (n = {n}, K = {K}, précis = {precis})"
    return int(round((ang[-1] - ang[0]) / (2 * np.pi)))


def zeros_complexes(n, c, R, grille=25):
    """Zéros de G_n dans le disque, par Newton depuis une grille de départs."""
    out = []
    for x0 in np.linspace(c - R, c + R, grille):
        for y0 in np.linspace(-R, R, grille):
            z = complex(x0, y0)
            for _ in range(60):
                d = (G(n, z + 1e-7, NP) - G(n, z - 1e-7, NP)) / 2e-7
                if not np.isfinite(d) or d == 0:
                    break
                pas = G(n, z, NP) / d
                z -= pas
                if not np.isfinite(z) or abs(pas) < 1e-14:
                    break
            if np.isfinite(z) and abs(z - c) < R and abs(G(n, z, NP)) < 1e-9 and all(abs(z - w) > 1e-6 for w in out):
                out.append(complex(z.real, z.imag if abs(z.imag) > 1e-9 else 0.0))
    return sorted(out, key=lambda w: (w.imag, w.real))


def division(gfun, c, R, N=128):
    """La division d'Ullisch par la règle des trapèzes sur le cercle (convergence exponentielle, partie I § 3.3) :
    β = ∮ z/g ÷ ∮ 1/g, les deux intégrales calculées sur les mêmes N points."""
    num = den = mp.mpc(0)
    for k in range(N):
        w = mp.e ** (2j * mp.pi * k / N)
        z = c + R * w
        gz = gfun(z)
        num += z * w / gz
        den += w / gz
    return num / den


def division_sure(gfun, c, R, Nmax=256, tol=mp.mpf(10) ** -24):
    """Double le nombre de points jusqu'à ce que deux divisions successives coïncident à tol près (None sinon)."""
    prec, N = division(gfun, c, R, 32), 64
    while N <= Nmax:
        b = division(gfun, c, R, N)
        if abs(b - prec) < tol:
            return b, N
        prec, N = b, 2 * N
    return None, None


# ---------------------------------------------------------------------------
# 1. Deux chèvres au même endroit
# ---------------------------------------------------------------------------
ligne("## 1. Deux chèvres au même endroit : la division d'intégrales complexes, dimension par dimension\n")
mp.mp.dps = 30
UC, UR = 3 * mp.pi / 4, mp.pi / 4  # le cercle d'Ullisch (erratum 2023)
f_u = lambda z: mp.sin(z) - z * mp.cos(z) - mp.pi / 2
b_u, N_u = division_sure(f_u, UC, UR)
ligne("**La formule d'Ullisch (2020), calculée directement.** β = ∮ z/f(z) dz ÷ ∮ 1/f(z) dz sur le cercle"
      " |z − 3π/4| = π/4, avec f(z) = sin z − z cos z − π/2, puis r = 2 cos(β/2) :")
ligne(f"- β = {mpfr(b_u.real, 25)} (partie imaginaire {mpfr(abs(b_u.imag), 2)}, {N_u} points) ;")
ligne(f"- r = {mpfr(2 * mp.cos(b_u.real / 2), 25)}.")
ecart_G2 = max(abs(2 * G(2, z) - f_u(z)) for z in (mp.mpf("1.2"), mp.mpf("1.9"), mp.mpc("1.5", "0.3")))
ligne(f"\nDans le plan méridien, l'équation de la dimension n est G_n(β) = 0, et G_2 = f/2 (écart vérifié"
      f" {mpfr(ecart_G2, 2)}). Le même procédé (diviser deux intégrales de contour) donne la corde de chaque"
      " dimension :\n")
ligne("| n | zéros de G_n dans le cercle d'Ullisch | cercle utilisé (trapèzes) | β_n (division) | angle α_n = π − β_n | corde ρ_n |")
ligne("|---:|---|---|---|---|---|")
DIMS = (2, 3, 4, 5, 6, 8, 9, 10, 12, 24, 100)
mp.mp.dps = 50  # en grande dimension, G_n se calcule avec des compensations : on garde de la marge
CHEVRE = {}
for n in DIMS:
    b0 = mp.findroot(lambda b: G(n, b), mp.mpf("1.8") if n < 10 else mp.mpf("1.62"))
    k = enroulement(n, float(UC), float(UR), K=50000) if n <= 40 else None  # au-delà, la double précision ne suffit plus
    beta = None
    if k == 1:  # le cercle d'Ullisch, si la règle des trapèzes y converge en moins de 256 points
        c, R = UC, UR
        beta, Np = division_sure(lambda z: G(n, z), c, R)
        nom = f"Ullisch ({Np} points)" if beta is not None else None
    if beta is None:  # sinon un cercle resserré autour de la racine réelle, qui n'entoure qu'un zéro
        c, R = b0, mp.mpf("0.25") if n <= 24 else mp.mpf("0.1")
        assert enroulement(n, float(c), float(R), K=360, precis=True) == 1
        beta, Np = division_sure(lambda z: G(n, z), c, R)
        nom = f"\\|β − β_n\\| < {fr(float(R), '{:g}')} ({Np} points)"
    assert abs(beta - b0) < mp.mpf(10) ** -20
    CHEVRE[n] = (float(b0), float(2 * mp.cos(b0 / 2)), k, nom)
    ligne(f"| {n} | {k if k is not None else '—'} | {nom} | {mpfr(beta.real, 20)} |"
          f" {fr(math.degrees(math.pi - float(b0)), '{:.3f}')}° |"
          f" {mpfr(2 * mp.cos(b0 / 2), 15)} |")
ligne("| ∞ | — | — | π/2 | 90° | √2 = 1,41421356237310 |")
mp.mp.dps = 30
SEUILS_U = []
prec_k = None
for n in range(2, 41):
    k = enroulement(n, float(UC), float(UR), K=50000)
    if k != prec_k:
        SEUILS_U.append((n, k))
        prec_k = k
assert SEUILS_U[1][0] == 10
Z10 = mp.findroot(lambda b: G(10, b), mp.mpc("2.4238", "0.7808"))  # la paire qui entre en dimension 10, en 30 chiffres
assert abs(Z10 - UC) < UR
ligne("\n- Le cercle d'Ullisch, tel quel, isole la seule racine réelle jusqu'à la dimension 9. Ensuite, des paires de"
      " zéros complexes y entrent : " + ", ".join(f"n = {n} : {k} zéros" for n, k in SEUILS_U[1:]) + "… La première"
      f" paire, {mpfr(Z10.real, 8)} ± {mpfr(Z10.imag, 8)}i, est à {mpfr(abs(Z10 - UC), 8)} du centre, à peine"
      f" sous le rayon π/4 = {mpfr(UR, 8)}. Il suffit alors de resserrer le cercle autour de la racine réelle.")
N_ULL = max(n for n in CHEVRE if CHEVRE[n][3].startswith("Ullisch"))
ligne("- Même avant la dimension 10, la paire qui approche du bord ralentit la règle des trapèzes sur le cercle d'Ullisch"
      " (la convergence dépend de la distance au zéro le plus proche, dedans ou dehors). Avec 256 points au plus, le"
      f" cercle d'Ullisch suffit jusqu'à la dimension {N_ULL} ; au-delà, un cercle resserré est plus rapide.")
ZC = {n: zeros_complexes(n, float(UC), float(UR)) for n in (2, 9, 10, 24)}
for n in (10, 24):
    ligne(f"- Zéros de G_{n} dans le cercle d'Ullisch : "
          + ", ".join(f"{fr(z.real, '{:.4f}')} {'+' if z.imag >= 0 else '−'} {fr(abs(z.imag), '{:.4f}')}i" for z in ZC[n])
          + ".")

# --- certification à 50 chiffres
ligne("\n**Les cordes certifiées à 50 chiffres** (arithmétique d'intervalles : G_n change de signe sur un intervalle de"
      " largeur 2·10⁻⁵⁸ autour de la racine) :\n")
ligne("| n | corde ρ_n, encadrée à 10⁻⁵⁰ près |")
ligne("|---:|---|")
CERT = {}
for n in (2, 3, 4, 8, 24):
    mp.mp.dps = 100
    iv.dps = 100
    b0 = mp.findroot(lambda b: G(n, b), mp.mpf("1.8"))
    eps = mp.mpf(10) ** -58
    lo, hi = b0 - eps, b0 + eps
    glo, ghi = G(n, iv.mpf(lo), iv), G(n, iv.mpf(hi), iv)
    assert (glo.b < 0 < ghi.a) or (glo.a > 0 > ghi.b), n
    rho = 2 * iv.cos(iv.mpf([lo, hi]) / 2)
    CERT[n] = (borne(rho, -1, 50), borne(rho, +1, 50))
    ligne(f"| {n} | {str(CERT[n][0]).replace('.', ',')} ≤ ρ ≤ …{str(CERT[n][1])[-3:]} |")
mp.mp.dps = 60
ligne(f"| ∞ | √2 = {mp.nstr(mp.sqrt(2), 51).replace('.', ',')}… |")
r3 = mp.findroot(lambda r: 3 * r ** 4 - 8 * r ** 3 + 8, 1.2)
assert Decimal(mp.nstr(r3, 55)) > CERT[3][0] and Decimal(mp.nstr(r3, 55)) < CERT[3][1]
ligne(f"\n- En dimension 3 (le « problème de l'oiseau »), la corde est la racine de 3r⁴ − 8r³ + 8 = 0 :"
      f" {mpfr(r3, 30)}… L'encadrement certifié la contient. Les dimensions impaires donnent un polynôme (la"
      " corde est algébrique), les paires gardent l'angle et π (partie VII).")
mp.mp.dps = 30
ligne("\n**Vers √2.** n·(2 − ρ_n²) tend vers 2, et l'angle α_n suit arccos(1/(n + 1)) à un petit ménisque près :\n")
ligne("| n | ρ_n | n·(2 − ρ_n²) | α_n | arccos(1/(n + 1)) |")
ligne("|---:|---|---|---|---|")
for n in (2, 3, 4, 8, 24, 100):
    b0, rho = CHEVRE[n][:2]
    ligne(f"| {n} | {fr(rho, '{:.6f}')} | {fr(n * (2 - rho * rho), '{:.4f}')} | {fr(math.degrees(math.pi - b0), '{:.3f}')}°"
          f" | {fr(math.degrees(math.acos(1 / (n + 1))), '{:.3f}')}° |")


# --- la famille ρ_n(d) (partie XVI)
def calotte(n, h):
    if h <= 0:
        return 0.0
    if h >= 2:
        return 1.0
    v = 0.5 * betainc((n + 1) / 2, 0.5, h * (2 - h))
    return v if h <= 1 else 1 - v


def recouvre(n, d, rho):
    if d + rho <= 1:
        return rho ** n
    if d + 1 <= rho:
        return 1.0
    if d >= 1 + rho:
        return 0.0
    x = (d * d + 1 - rho * rho) / (2 * d)
    return calotte(n, 1 - x) + rho ** n * calotte(n, (rho - d + x) / rho)


def rho_moitie(n, d):
    r0 = 2 ** (-1 / n)
    if d <= 1 - r0:
        return r0
    return brentq(lambda r: recouvre(n, d, r) - 0.5, max(r0, abs(d - 1)), d + 1, xtol=1e-13)


# ---------------------------------------------------------------------------
# 2. Pair et impair
# ---------------------------------------------------------------------------
ligne("\n## 2. Pair et impair : la récurrence de la partie IV\n")
ligne("h_n = (hémisphère)/(cylindre) en dimension n ; h_n = (n − 1)/n · h_{n−2}, avec h_1 = 1 et h_0 = π/2. Les"
      " dimensions impaires divisent par 3, 5, 7… ; les paires, à partir du disque (h_2 = π/4), par 4, 6, 8…\n")
H = {0: Fraction(1, 2), 1: Fraction(1)}
for n in range(2, 25):
    H[n] = H[n - 2] * Fraction(n - 1, n)
hval = lambda n: float(H[n]) * (math.pi if n % 2 == 0 else 1.0)
ligne("| n | h_n | valeur | facteur depuis n − 2 | h_n > ½ (volume croît) | h_n > ½·(1 − 1/n) (aire croît) |")
ligne("|---:|---|---|---|---|---|")
for n in range(1, 13):
    exact = (f"π·{H[n]}" if n % 2 == 0 else str(H[n]))
    fac = f"× {n - 1}/{n}" if n >= 2 else "—"
    ligne(f"| {n} | {exact} | {fr(hval(n), '{:.5f}')} | {fac} | {'oui' if hval(n) > 0.5 else 'non'} |"
          f" {'oui' if hval(n) > 0.5 * (1 - 1 / n) else 'non'} |")
for n in range(2, 25):
    assert abs(hval(n - 1) * hval(n) - math.pi / (2 * n)) < 1e-12
ligne("\n- Réciprocité : h_{n−1}·h_n = π/(2n) pour tout n (vérifié jusqu'à 24) : chaque impaire est l'inverse de sa"
      " voisine paire, à π/(2n) près.")
ligne("- Seuils (partie IV) : l'hémisphère remplit moins de la moitié de son cylindre à partir de la dimension 6 (pic du"
      " volume en 5), et moins de la moitié de l'anneau d'Archimède à partir de la dimension 8 (pic de l'aire en 7).")
ligne("- La dimension 3 est le premier barreau : h_3 = 2/3 (Archimède). C'est aussi la seule dimension où l'ombre de la"
      " sphère sur un axe est uniforme : la densité de la projection de S^{n−1} est ∝ (1 − t²)^((n−3)/2), plate pour"
      " n = 3, massée aux bords pour n = 2, à l'équateur pour n ≥ 4.")
ligne("\n**Aire et volume pour la chèvre.** Elle broute toujours la moitié du volume du pré, mais pas la moitié de sa"
      " clôture. Part de la clôture S^{n−1} broutée (calotte d'angle α_n) :\n")


def part_cloture(n, a):
    """Part de la sphère S^{n−1} dans une calotte de demi-angle a ≤ 90° : ½·I_{sin² a}((n − 1)/2, ½)."""
    return 0.5 * betainc((n - 1) / 2, 0.5, math.sin(a) ** 2)


assert abs(part_cloture(2, 1.0) - 1 / math.pi) < 1e-12 and abs(part_cloture(3, 1.0) - (1 - math.cos(1)) / 2) < 1e-12
PARTS = {}
for n in (2, 3, 4, 5, 6, 8, 12, 24, 100, 300):
    rho = CHEVRE[n][1] if n in CHEVRE else rho_moitie(n, 1.0)
    PARTS[n] = part_cloture(n, 2 * math.asin(rho / 2))
ligne("| n | " + " | ".join(str(n) for n in PARTS) + " |")
ligne("|---|" + "---|" * len(PARTS))
ligne("| part de la clôture | " + " | ".join(fr(v, "{:.4f}") for v in PARTS.values()) + " |")
NMIN = min((n for n in PARTS if n <= 24), key=lambda n: PARTS[n])
ligne(f"\n- Minimum en dimension {NMIN} ({fr(PARTS[NMIN], '{:.4f}')}), puis la part monte vers ½ : en dimension infinie,"
      " aire et volume se rejoignent (la chèvre broute un hémisphère).")

# ---------------------------------------------------------------------------
# 3. Les faisceaux des sphères
# ---------------------------------------------------------------------------
ligne("\n## 3. Les faisceaux des n-sphères\n")


def simplexe(n):
    """n + 1 sommets unitaires dans R^n, deux à deux à produit scalaire −1/n."""
    E = np.eye(n + 1) - 1.0 / (n + 1)
    U, S, _ = np.linalg.svd(E)
    B = U[:, :n] * S[:n]
    return B / np.linalg.norm(B, axis=1, keepdims=True)


rng = np.random.default_rng(20)
ligne("**n + 1 chèvres couvrent la clôture.** On place une chèvre de dimension n sur chaque sommet du simplexe régulier"
      " inscrit dans la clôture S^{n−1} ; chacune broute la calotte d'angle α_n. Pour former un bon recouvrement"
      " (nerf = bord du simplexe), il faut arccos(1/n) < α_n < 90° :\n")
ligne("| n | sphère couverte | α_n | seuil arccos(1/n) | multiplicité observée (2·10⁵ points) | jamais n + 1 chèvres à la fois |")
ligne("|---:|---|---|---|---|---|")
COUV = {}
for n in (2, 3, 4, 8, 24):
    b0, rho = CHEVRE[n][:2]
    a = math.pi - b0
    V_ = simplexe(n)
    assert np.allclose(V_ @ V_.T, np.eye(n + 1) * (1 + 1 / n) - 1 / n)
    X = rng.normal(size=(200000, n))
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    mult = ((X @ V_.T) > math.cos(a)).sum(axis=1)
    assert math.acos(1 / n) < a < math.pi / 2 and mult.min() >= 1 and mult.max() <= n
    COUV[n] = (mult.min(), mult.max())
    ligne(f"| {n} | S^{n - 1} | {fr(math.degrees(a), '{:.3f}')}° | {fr(math.degrees(math.acos(1 / n)), '{:.3f}')}° |"
          f" {mult.min()} à {mult.max()} | oui |")
ligne("\n- Toute la clôture est broutée (multiplicité ≥ 1), deux chèvres voisines se recouvrent, et aucun point n'est"
      " brouté par les n + 1 à la fois (ils ne peuvent pas être à moins de 90° de tous les sommets). Les intersections"
      " de calottes de moins de 90° sont convexes : c'est un bon recouvrement.")
ligne("- La chèvre broute toujours un peu plus que arccos(1/(n + 1)), au-dessus du seuil arccos(1/n) : le recouvrement"
      " marche dans toutes les dimensions. En dimension infinie, α → 90° : chaque chèvre broute un hémisphère.")


def rang_mod(M, p=1_000_000_007):
    M = [list(r) for r in M]
    if not M:
        return 0
    rows, cols, r = len(M), len(M[0]), 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c] % p, p - 2, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % p:
                fct = M[i][c] % p
                M[i] = [(x - fct * y) % p for x, y in zip(M[i], M[r])]
        r += 1
        if r == rows:
            break
    return r


def cech(nb):
    """Cohomologie de Čech du nerf « bord du simplexe à nb sommets » (toutes les parties propres non vides)."""
    faces = {k: list(itertools.combinations(range(nb), k + 1)) for k in range(nb - 1)}
    idx = {k: {f: i for i, f in enumerate(faces[k])} for k in faces}
    rangs = {}
    for k in range(nb - 2):
        M = [[0] * len(faces[k]) for _ in faces[k + 1]]
        for j, g in enumerate(faces[k + 1]):
            for t in range(len(g)):
                M[j][idx[k][g[:t] + g[t + 1:]]] = (-1) ** t
        rangs[k] = rang_mod(M)
    betti = [len(faces[k]) - rangs.get(k, 0) - rangs.get(k - 1, 0) for k in range(nb - 1)]
    return betti, [len(faces[k]) for k in range(nb - 1)]


ligne("\n**La cohomologie de Čech du nerf** (le faisceau constant ℤ ; le nerf de n + 1 chèvres est le bord du simplexe à"
      " n + 1 sommets) :\n")
ligne("| clôture | chèvres | cochaînes par degré | Betti b₀ … b_{n−1} | χ |")
ligne("|---|---:|---|---|---:|")
BETTI = {}
for n in range(2, 10):
    b, c = cech(n + 1)
    chi = sum((-1) ** k * x for k, x in enumerate(c))
    BETTI[n - 1] = b
    assert b == [1] + [0] * (n - 2) + [1] and chi == 1 + (-1) ** (n - 1)
    ligne(f"| S^{n - 1} | {n + 1} | {', '.join(map(str, c))} | {', '.join(map(str, b))} | {chi} |")
ligne("\n- On retrouve H⁰ = H^{n−1} = ℤ et rien entre les deux : la cohomologie de la sphère, calculée avec des chèvres.")
ligne("- χ(S^k) = 1 + (−1)^k : 2 pour les sphères paires, 0 pour les impaires.")

ligne("\n**Les deux cartes de la sphère.** Projeter S^n depuis le pôle nord N sur le plan de l'équateur, c'est"
      " l'inversion de centre N et de rayon √2 : elle fixe l'équateur (à distance √2 de N). Vérifications (1000 points"
      " au hasard par dimension) :\n")
ligne("| n | carte sud ∘ (carte nord)⁻¹ = inversion y ↦ y/\\|y\\|² | inversion de rayon √2 = carte nord | hémisphère sud → dedans, nord → dehors |")
ligne("|---:|---|---|---|")
for n in (1, 2, 3, 8, 24):
    X = rng.normal(size=(1000, n + 1))
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    Np = np.zeros(n + 1)
    Np[-1] = 1
    sN = X[:, :-1] / (1 - X[:, -1:])
    sS = X[:, :-1] / (1 + X[:, -1:])
    Y = Np + 2 * (X - Np) / ((X - Np) ** 2).sum(axis=1, keepdims=True)
    sud = X[:, -1] < 0
    ok1 = np.allclose(sS, sN / (sN ** 2).sum(axis=1, keepdims=True))
    ok2 = np.allclose(Y[:, -1], 0) and np.allclose(Y[:, :-1], sN)
    ok3 = bool(np.all(np.linalg.norm(sN[sud], axis=1) < 1) and np.all(np.linalg.norm(sN[~sud], axis=1) > 1))
    assert ok1 and ok2 and ok3
    ligne(f"| {n} | oui | oui | oui |")
ligne("\n- Chaque carte manque un seul point ; les deux se recouvrent sur ℝⁿ privé de 0, et on passe de l'une à l'autre"
      " par l'inversion. Les deux hémisphères ont chacun la moitié de l'aire : l'un tombe dans le disque unité,"
      " l'autre dehors.")
ligne("- Mayer–Vietoris sur ces deux cartes donne H^k(S^n) = H^{k−1}(S^{n−1}) : la cohomologie monte d'une dimension"
      " à la suivante en partant de S⁰, deux points.")


def champs(k):
    """Nombre maximal de champs de vecteurs indépendants sur S^k (Radon–Hurwitz, Adams 1962)."""
    m = k + 1
    b = 0
    while m % 2 == 0:
        m //= 2
        b += 1
    c, d = b % 4, b // 4
    return 2 ** c + 8 * d - 1


ligne("\n**Pair et impair : où vit i.** Une rotation J de ℝ^m avec J² = −1 (un « i ») n'existe que si m est pair"
      " (det J² = (−1)^m). Sur une sphère impaire S^(m−1), x ↦ J·x est un champ tangent qui ne s'annule jamais ; sur"
      " une sphère paire, tout champ s'annule quelque part (χ = 2, la boule chevelue).\n")
ligne("| sphère | χ | champs indépendants (Radon–Hurwitz) | parallélisable |")
ligne("|---|---:|---:|---|")
for k in (1, 2, 3, 4, 5, 6, 7, 8, 15, 23, 24):
    ligne(f"| S^{k} | {1 + (-1) ** k} | {champs(k)} | {'oui' if champs(k) == k else 'non'} |")
ligne("\n- Les seules sphères parallélisables sont S¹, S³ et S⁷ : celles des nombres complexes, des quaternions et des"
      " octonions (dimensions 2, 4 et 8). La formule a une période 8 (Bott).")

# ---------------------------------------------------------------------------
# 4. Le losange de √2 et la figure de diffraction
# ---------------------------------------------------------------------------
ligne("\n## 4. Le losange de √2 dans la figure de diffraction\n")
N_RAYONS = 72
RG = N_RAYONS / (2 * math.pi)
ligne(f"Étoile de Siemens de la partie XVIII ({N_RAYONS} rayons) : les fantômes sont au réseau inversé"
      " (N/2π)·(m₂, −m₁)/|m|².")
ligne(f"- Couche |m| = 1 : 4 fantômes sur les axes, à {fr(RG, '{:.3f}')} pixels du centre : les sommets d'un losange.")
ligne(f"- Couche |m| = √2 : 4 fantômes sur les diagonales, à {fr(RG / R2, '{:.3f}')} pixels : exactement les milieux"
      " des côtés du losange, sur son cercle inscrit.")
ligne("- Rayon inscrit / rayon circonscrit = 1/√2 : le disque inscrit a exactement la moitié de l'aire du disque"
      " circonscrit.")
ligne("- À l'échelle d'un pixel tourné de 45°, ce losange a une hauteur √2 et un côté 1. À l'échelle du pré (sommets"
      " sur le cercle unité), son côté vaut √2 : la corde de la chèvre de dimension infinie.")
ligne("\n**Le retournement.** Avant inversion, la couche √2 du réseau (±1, ±1) forme un carré dont les milieux des côtés"
      " sont la couche 1. Après inversion, c'est l'inverse : la couche 1 donne les sommets, la couche √2 les milieux."
      " L'inversion échange sommets et milieux.\n")
ligne("**En dimension n**, la couche 1 de ℤⁿ inversée donne les 2n sommets du polytope croisé (arêtes √2), et la"
      " couche √2 inversée donne exactement les milieux de ses arêtes, à 1/√2 du centre :\n")
ligne("| n | sommets ±e_i | arêtes (= couche √2 inversée) | toutes les arêtes valent √2 | milieux à 1/√2 |")
ligne("|---:|---:|---:|---|---|")
for n in (2, 3, 4, 8):
    c1 = [v for v in itertools.product(range(-1, 2), repeat=n) if sum(x * x for x in v) == 1]
    c2 = [v for v in itertools.product(range(-1, 2), repeat=n) if sum(x * x for x in v) == 2]
    inv2 = {tuple(Fraction(x, 2) for x in v) for v in c2}
    mil = {tuple(Fraction(x + y, 2) for x, y in zip(a, b)) for a, b in itertools.combinations(c1, 2)
           if sum(x * y for x, y in zip(a, b)) == 0}
    assert inv2 == mil
    ligne(f"| {n} | {len(c1)} | {len(mil)} | oui | oui |")
ligne("\n- 24 arêtes en dimension 4 et 112 en dimension 8 : ce sont les racines des réseaux D₄ et D₈ (§ 5).")
ligne("\n**Le retournement de l'aiguille.** Retourner une aiguille, c'est −1 = i·i : deux quarts de tour, en passant par"
      " une direction perpendiculaire (un sommet voisin du losange, à distance √2). En dimension 2, il y a deux chemins"
      " (par i ou par −i, comme 3 et 7 modulo 10). En dimension n, toute direction de la sphère S^(n−2) perpendiculaire"
      " convient : un cercle en 3D, une infinité de chemins en dimension infinie.")

# ---------------------------------------------------------------------------
# 5. 3, 8, 24
# ---------------------------------------------------------------------------
ligne("\n## 5. 3, 8, 24 : le trou profond √n/2\n")
ligne("Le centre d'un cube de ℤⁿ (le centre du pixel vu de ses coins) est à √n/2 des coins.\n")
ligne("| n | 2 | 3 | 4 | 8 | 16 | 24 |")
ligne("|---|---|---|---|---|---|---|")
ligne("| √n/2 | " + " | ".join(fr(math.sqrt(n) / 2, "{:.4f}") for n in (2, 3, 4, 8, 16, 24)) + " |")
nD8 = sum(1 for v in itertools.product(range(-1, 2), repeat=8) if sum(x * x for x in v) == 2 and sum(v) % 2 == 0)
nH = sum(1 for s in itertools.product((-1, 1), repeat=8) if s.count(-1) % 2 == 0)
nD4 = sum(1 for v in itertools.product(range(-1, 2), repeat=4) if sum(x * x for x in v) == 2)
assert (nD8, nH, nD4) == (112, 128, 24)
ligne("\n- n = 2 : 1/√2 (le rayon du demi-disque). n = 4 : 1. n = 8 : √2, la diagonale 1x, 1y.")
ligne(f"- En dimension 8, le centre du cube est donc aussi loin que les voisins les plus proches de D₈ (les vecteurs"
      f" ±e_i ± e_j, de longueur √2). On peut l'ajouter : E₈ = D₈ ∪ (D₈ + ½·(1, …, 1)), la grille décalée d'une demi-maille"
      f" (partie XV). Ses vecteurs les plus courts : {nD8} + {nH} = {nD8 + nH}, le nombre de sphères qui touchent une"
      " sphère dans le meilleur empilement de dimension 8.")
ligne(f"- En dimension 4, les racines de D₄ sont {nD4} : 24 sphères touchent une sphère (Musin, 2003).")
ligne("- Le meilleur empilement de sphères n'est démontré qu'en dimensions 1, 2, 3, 8 et 24 (Hales en 3, Viazovska en 8,"
      " Cohn, Kumar, Miller, Radchenko et Viazovska en 24).")

# ---------------------------------------------------------------------------
# 6. Musique et IA
# ---------------------------------------------------------------------------
ligne("\n## 6. La géométrie dans la musique et dans l'IA\n")
L3 = math.log2(3)
cf, y = [], L3
for _ in range(10):
    a_ = int(y)
    cf.append(a_)
    y = 1 / (y - a_)
red = []
h0, h1, k0, k1 = 0, 1, 1, 0
for a_ in cf:
    h0, h1 = h1, a_ * h1 + h0
    k0, k1 = k1, a_ * k1 + k0
    red.append((h1, k1))
comma = Fraction(3 ** 12, 2 ** 19)
ligne(f"**2 et 3 donnent 12.** log₂ 3 = {fr(L3, '{:.9f}')} = [{cf[0]} ; {', '.join(map(str, cf[1:]))}, …]. Réduites :"
      f" {', '.join(f'{p}/{q}' for p, q in red[:8])}…")
ligne(f"- 19/12 : 3¹² ≈ 2¹⁹, douze quintes ≈ sept octaves. L'écart est le comma pythagoricien {comma} ="
      f" {fr(float(comma), '{:.6f}')}, soit {fr(1200 * math.log2(float(comma)), '{:.2f}')} cents.")
ligne(f"- La quinte tempérée 2^(7/12) = {fr(2 ** (7 / 12), '{:.6f}')} est trop basse de"
      f" {fr(1200 * (math.log2(1.5) - 7 / 12), '{:.3f}')} cent. Les réduites suivantes donnent les gammes à 41 et 53 notes.")
ligne("- Le cercle des quintes est une rotation irrationnelle, comme le cercle des décades (partie XIX). Théorème des"
      " trois distances, pour N quintes ramenées dans l'octave :\n")
ligne("| N notes | longueurs de pas (en cents) |")
ligne("|---:|---|")
PAS = {}
for Nq in (5, 6, 7, 8, 12, 41, 53):
    pts = sorted((k * math.log2(1.5)) % 1 for k in range(Nq))
    g = np.diff(pts + [pts[0] + 1])
    PAS[Nq] = sorted(set(np.round(1200 * g, 6)))
    ligne(f"| {Nq} | {' ; '.join(fr(v, '{:.2f}') for v in PAS[Nq])} |")
ligne("\n- 5 (pentatonique), 7 (diatonique) et 12 (chromatique) n'ont que deux tailles de pas ; 6 et 8 en ont trois.")
ligne("\n**L'IA et √2.** Deux vecteurs unitaires tirés au hasard en dimension d sont à distance √(2 − 2t), où t = u·v suit"
      " la densité ∝ (1 − t²)^((d−3)/2), celle de l'ombre de la sphère (§ 2). Mesures (2·10⁴ paires par dimension) :\n")
ligne("| d | distance moyenne | écart-type | 1/√(2d) |")
ligne("|---:|---|---|---|")
IA = {}
for d in (2, 3, 10, 100, 1000, 4096):
    U = rng.normal(size=(20000, d))
    U /= np.linalg.norm(U, axis=1, keepdims=True)
    W = rng.normal(size=(20000, d))
    W /= np.linalg.norm(W, axis=1, keepdims=True)
    dist = np.linalg.norm(U - W, axis=1)
    IA[d] = dist
    ligne(f"| {d} | {fr(dist.mean(), '{:.4f}')} | {fr(dist.std(), '{:.4f}')} | {fr(1 / math.sqrt(2 * d), '{:.4f}')} |")
ligne("\n- En grande dimension, deux directions sans rapport sont presque perpendiculaires, à distance √2 : la corde de"
      " la chèvre de dimension infinie. C'est ce qui permet à un réseau de neurones de ranger beaucoup plus de notions"
      " que de dimensions (la « superposition »).")

# ---------------------------------------------------------------------------
# 7. 10⁻⁵⁰
# ---------------------------------------------------------------------------
ligne("\n## 7. 10⁻⁵⁰ : une précision, et une échelle physique\n")
Gc, hbar, cl, hP = 6.67430e-11, 1.054571817e-34, 299792458.0, 6.62607015e-34
LP = math.sqrt(hbar * Gc / cl ** 3)
E50 = hP * cl / 1e-50
RS50 = 2 * Gc * E50 / cl ** 4
LCRIT = math.sqrt(2 * Gc * hP / cl ** 3)
ligne("**Comme précision.** Les cordes du § 1 sont encadrées à 10⁻⁵⁰ près. Un grain de 10⁻⁵⁰ sur un pré de rayon 1"
      " demande :")
ligne("- " + " ; ".join(f"{fr(50 / math.log10(b), '{:.1f}')} chiffres en base {b}" for b in (2, 10, 12, 60)) + ".")
ligne(f"\n**Comme échelle physique** (CODATA 2018). La longueur de Planck vaut {fr(LP * 1e35, '{:.4f}')}·10⁻³⁵ m ;"
      f" 10⁻⁵⁰ m en est {fr(1e-50 / LP * 1e16, '{:.2f}')}·10⁻¹⁶.")
ligne(f"- Pour sonder 10⁻⁵⁰ m, il faut une onde de cette longueur : un photon de {fr(E50 / 1e25, '{:.2f}')}·10²⁵ J."
      f" Son rayon de Schwarzschild serait {fr(RS50 * 1e19, '{:.2f}')}·10⁻¹⁹ m, {fr(RS50 / 1e-50 / 1e31, '{:.1f}')}·10³¹"
      " fois la région sondée : la mesure créerait un trou noir qui la cache.")
ligne(f"- Ce rayon égale la longueur d'onde vers {fr(LCRIT * 1e35, '{:.2f}')}·10⁻³⁵ m, soit"
      f" {fr(LCRIT / LP, '{:.2f}')} longueurs de Planck (√(4π)) : en dessous, aucune mesure de position n'est possible"
      " dans la physique connue.")

with open(os.path.join(ICI, "..", "resultats", "sphere_faisceaux.md"), "w") as fh:
    fh.write("# Résultats de la partie XX (générés par scripts/sphere_faisceaux.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure 1 : deux chèvres au même endroit, et les faisceaux des sphères
# ===========================================================================
NS_EV = (2, 3, 4, 8, 24, 100)
COUL = {2: F.ORANGE, 3: F.JAUNE, 4: F.AQUA, 8: F.SEQ[7], 24: F.SEQ[10], 100: F.SEQ[13]}
TT = np.linspace(0, 2 * np.pi, 400)


def cercle(ax, r, cx=0.0, cy=0.0, **kw):
    ax.plot(cx + r * np.cos(TT), cy + r * np.sin(TT), **kw)


def schema(ax, lim, lim_y=None):
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-(lim_y or lim), lim_y or lim)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)


fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.18, hspace=0.3)

# a) le losange de √2 au centre de la figure de diffraction
ax = fig.add_subplot(gs[0, 0])
W = 20
yy, xx = np.mgrid[-W:W + 1, -W:W + 1]
etoile = 0.5 + 0.5 * np.cos(N_RAYONS * np.arctan2(yy, xx))
ax.imshow(etoile, cmap="gray", vmin=0, vmax=1, extent=(-W - 0.5, W + 0.5, -W - 0.5, W + 0.5), origin="lower",
          interpolation="nearest", alpha=0.55)
cercle(ax, RG, color=ROUGE, lw=1.4, ls="--")
cercle(ax, RG / R2, color=VIOLET, lw=1.4, ls=":")
ax.add_patch(Polygon([(RG, 0), (0, RG), (-RG, 0), (0, -RG)], closed=True, fill=False, ec=ROUGE, lw=2.2))
for m1 in range(-2, 3):
    for m2 in range(-2, 3):
        n2 = m1 * m1 + m2 * m2
        if 0 < n2 <= 5:
            k_ = RG / n2
            st = dict(ms=15, mew=2.2, mec=ROUGE) if n2 == 1 else (dict(ms=13, mew=2.0, mec=VIOLET) if n2 == 2 else
                                                                   dict(ms=7, mew=1.2, mec=F.ORANGE))
            ax.plot([k_ * m2], [-k_ * m1], "o", mfc=F.SURF, zorder=6, **st)
ax.text(RG + 0.8, 1.0, "|m| = 1 : sommets", color=ROUGE, fontsize=8.8, fontweight="bold", zorder=7,
        bbox=dict(fc=F.SURF, ec="none", alpha=0.85, pad=1))
ax.text(RG / 2 + 1.0, RG / 2 + 1.6, "|m| = √2 : milieux des côtés", color=VIOLET, fontsize=8.8, fontweight="bold",
        zorder=7, bbox=dict(fc=F.SURF, ec="none", alpha=0.85, pad=1))
ax.text(-W + 0.5, -W + 0.6, "|m|² = 4, 5 : la couronne\nsuivante (orange)", color=F.ORANGE, fontsize=8.3, zorder=7,
        bbox=dict(fc=F.SURF, ec="none", alpha=0.85, pad=1))
schema(ax, W + 0.5)
ax.set_title("a)  Le losange de √2 dans la figure de diffraction")
ax.text(0.5, -0.02, f"L'étoile de Siemens de la partie XVIII ({N_RAYONS} rayons), au centre des pixels. Les fantômes"
        " |m| = 1\nsont les sommets d'un losange (cercle rouge), les fantômes |m| = √2 les milieux de ses côtés\n"
        "(cercle violet, rayon × 1/√2, aire × 1/2). À l'échelle d'un pixel tourné de 45°, hauteur √2.",
        transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)

# b) deux chèvres au même endroit
ax = fig.add_subplot(gs[0, 1])
ax.add_patch(plt.Circle((0, 0), 1, fc=F.SEQ[1], ec=F.INK, lw=1.4))
ax.add_patch(Polygon([(1, 0), (0, 1), (-1, 0), (0, -1)], closed=True, fill=False, ec=ROUGE, lw=1.6, ls="--"))
cercle(ax, 1 / R2, color=VIOLET, lw=1.2, ls=":")
P = np.array([1.0, 0.0])
for n in NS_EV:
    b0, rho = CHEVRE[n][:2]
    a = math.pi - b0
    for sg in (1, -1):
        Q = np.array([math.cos(a), sg * math.sin(a)])
        ax.plot([P[0], Q[0]], [P[1], Q[1]], color=COUL[n], lw=1.6 if n in (2, 100) else 1.1)
        ax.plot([Q[0]], [Q[1]], "o", ms=6, color=COUL[n], mec=F.SURF, zorder=6)
for sg in (1, -1):
    ax.plot([1, 0], [0, sg], color=F.INK, lw=2.2)
    ax.plot([0], [sg], "o", ms=8, color=F.INK, mec=F.SURF, zorder=7)
tt = np.linspace(math.pi / 2, 3 * math.pi / 2, 200)
for rho, c in ((CHEVRE[2][1], F.ORANGE), (R2, F.INK)):
    arc = np.array([1 + rho * np.cos(tt), rho * np.sin(tt)])
    dedans = arc[0] ** 2 + arc[1] ** 2 <= 1.0001
    ax.plot(arc[0][dedans], arc[1][dedans], color=c, lw=2.2, alpha=0.9)
ax.plot([1], [0], "o", ms=11, color=ROUGE, mec=F.SURF, zorder=8)
ax.text(1.07, -0.09, "piquet", color=ROUGE, fontsize=9, fontweight="bold")
ax.text(-1.28, 1.13, "∞ : corde √2, angle 90° : le côté du losange", color=F.INK, fontsize=8.8, fontweight="bold")
ax.text(-1.28, -1.24, "2D : corde 1,1587…, angle 70,8° (Ullisch)", color=F.ORANGE, fontsize=8.8, fontweight="bold")
ax.text(-0.35, -0.2, "cercle 1/√2 :\nla moitié du pré", color=VIOLET, fontsize=8.2, ha="center")
for i, n in enumerate(NS_EV):
    ax.text(1.12, 0.92 - 0.11 * i, f"n = {n} : {fr(math.degrees(math.pi - CHEVRE[n][0]), '{:.1f}')}°", color=COUL[n],
            fontsize=8.6, fontweight="bold")
ax.text(1.12, 0.92 - 0.11 * len(NS_EV), "n = ∞ : 90°", color=F.INK, fontsize=8.6, fontweight="bold")
schema(ax, 1.55, 1.32)
ax.set_xlim(-1.3, 1.8)
ax.set_title("b)  Deux chèvres au même endroit")
ax.text(0.5, -0.02, "Le même piquet, le même pré. La chèvre plane s'arrête à 70,8° du piquet (vu du centre) ; celle de\n"
        "dimension infinie atteint 90°, les sommets voisins du losange : sa corde √2 en est le côté. Entre les\n"
        "deux, toutes les dimensions, chacune avec sa division d'intégrales complexes (panneau c).",
        transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)

# c) la division d'intégrales complexes, dimension par dimension
ax = fig.add_subplot(gs[0, 2])
cercle(ax, float(UR), float(UC), 0, color=F.INK, lw=1.8)
ax.axhline(0, color=F.BASE, lw=0.8)
for n in NS_EV:
    b0 = CHEVRE[n][0]
    ax.plot([b0], [0], "o", ms=9, color=COUL[n], mec=F.SURF, zorder=6)
for n in (2, 100):
    ax.annotate(f"n = {n}", (CHEVRE[n][0], 0), (CHEVRE[n][0] + 0.02, 0.12) if n == 2 else (1.47, -0.17), fontsize=8.6,
                color=COUL[n], fontweight="bold", ha="center")
ax.plot([math.pi / 2], [0], "x", ms=10, mew=2, color=F.INK)
ax.annotate("∞ : π/2", (math.pi / 2, 0), (1.36, 0.22), fontsize=8.6, arrowprops=dict(arrowstyle="-", color=F.INK2,
            lw=0.8))
for n, mk, c in ((10, "^", F.SEQ[8]), (24, "s", F.SEQ[10])):
    zs = [z for z in ZC[n] if abs(z.imag) > 1e-6]
    ax.plot([z.real for z in zs], [z.imag for z in zs], mk, ms=8, color=c, mec=F.SURF, zorder=6,
            label=f"zéros complexes de G_{n} dans le cercle")
cercle(ax, 0.25, CHEVRE[24][0], 0, color=F.SEQ[10], lw=1.2, ls="--")
ax.text(3.22, -0.95, "cercle d'Ullisch : |β − 3π/4| = π/4", ha="right", va="bottom", fontsize=8.8, color=F.INK)
liste = "\n".join(f"{n} : {fr(CHEVRE[n][0], '{:.4f}')} → {fr(CHEVRE[n][1], '{:.4f}')}" for n in NS_EV)
ax.text(1.23, -0.95, "β = ∮ z/G ÷ ∮ 1/G\nρ = 2 cos(β/2)\n\nn : β_n → ρ_n\n" + liste + "\n∞ : π/2 → √2",
        fontsize=7.8, color=F.INK, va="bottom", bbox=dict(fc=F.SURF, ec=F.BASE, pad=3), zorder=8)
ax.legend(loc="upper left", fontsize=8.0, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_xlim(1.2, 3.25)
ax.set_ylim(-0.97, 0.97)
ax.set_aspect("equal")
ax.set_xlabel("Re β")
ax.set_ylabel("Im β")
ax.set_title("c)  La division d'intégrales complexes, dimension par dimension")
ax.text(0.5, -0.13, "Jusqu'à la dimension 9, le cercle d'Ullisch n'entoure qu'un zéro : la racine réelle. En dimension"
        " 10,\nune paire de zéros complexes y entre (à 0,0017 du bord) ; on resserre alors le cercle (tirets, n = 24).",
        transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)

# d) pair et impair : les deux chaînes de la partie IV
ax = fig.add_subplot(gs[1, 0])
ns = np.arange(1, 13)
vals = [hval(n) for n in ns]
ax.bar(ns, vals, color=[F.BLEU if n % 2 else F.ORANGE for n in ns], width=0.62, zorder=3)
ax.axhline(0.5, color=F.INK, lw=1.2, ls="--")
for n in range(2, 13):
    ax.plot([n - 0.38, n + 0.38], [0.5 * (1 - 1 / n)] * 2, color=ROUGE, lw=2.2, zorder=4)
    ax.text(n, hval(n) + 0.02, f"×{n - 1}/{n}", ha="center", fontsize=7.8, color=F.BLEU if n % 2 else F.ORANGE,
            fontweight="bold")
ax.text(0.35, 0.51, "½", fontsize=9, ha="left", va="bottom", color=F.INK)
ax.annotate("3 : 2/3 (Archimède)", (3, 2 / 3), (4.3, 0.8), fontsize=8.6, color=F.BLEU,
            arrowprops=dict(arrowstyle="->", color=F.BLEU, lw=0.9))
ax.set_xticks(ns)
ax.set_ylim(0, 1.12)
ax.set_xlabel("dimension n")
ax.set_ylabel("h_n = hémisphère / cylindre")
ax.set_title("d)  Pair et impair : les deux chaînes de la partie IV")
ax.text(0.5, -0.13, "h_n = (n − 1)/n · h_{n−2}. Impaires (bleu) : on divise par 3, 5, 7… depuis h₁ = 1. Paires (orange) :"
        "\npar 4, 6, 8… depuis le disque, h₂ = π/4. Et h_{n−1}·h_n = π/(2n) : les deux chaînes sont réciproques.\n"
        "Tirets noirs, ½ : le volume des boules décroît dès 6. Traits rouges, ½·(1 − 1/n) : leur aire décroît dès 8.",
        transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)

# e) les faisceaux : n + 1 chèvres couvrent la clôture
sub = gs[1, 1].subgridspec(1, 2, wspace=0.05)
ax = fig.add_subplot(sub[0])
a2 = math.pi - CHEVRE[2][0]
for i, c in enumerate((F.ORANGE, F.AQUA, F.BLEU)):
    th0 = math.pi / 2 + 2 * math.pi * i / 3
    t_ = np.linspace(th0 - a2, th0 + a2, 200)
    r_ = 1.0 + 0.07 * i
    ax.plot(r_ * np.cos(t_), r_ * np.sin(t_), color=c, lw=5, alpha=0.85, solid_capstyle="butt")
    ax.plot([math.cos(th0)], [math.sin(th0)], "o", ms=9, color=c, mec=F.INK, zorder=6)
cercle(ax, 1, color=F.INK, lw=1)
tri = [(0.42 * math.cos(math.pi / 2 + 2 * math.pi * i / 3), 0.42 * math.sin(math.pi / 2 + 2 * math.pi * i / 3))
       for i in range(3)]
ax.add_patch(Polygon(tri, closed=True, fill=False, ec=F.INK2, lw=1.2))
for (x_, y_), c in zip(tri, (F.ORANGE, F.AQUA, F.BLEU)):
    ax.plot([x_], [y_], "o", ms=6, color=c)
ax.text(0, -0.5, "nerf : le bord\ndu triangle = S¹", ha="center", va="center", fontsize=7.8, color=F.INK2)
schema(ax, 1.3)
ax.set_title("e)  Les faisceaux : n + 1 chèvres couvrent la clôture", fontsize=11.5)
ax.text(0.5, -0.02, "3 chèvres planes (70,8°) sur un\ntriangle couvrent le cercle ;\njamais les trois à la fois.",
        transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)
ax = fig.add_subplot(sub[1])
a3 = math.pi - CHEVRE[3][0]
V3 = simplexe(3)
rot = np.linalg.qr(np.array([[0.9, 0.3, 0.2], [-0.2, 0.8, 0.5], [0.1, -0.4, 0.9]]))[0]
V3 = V3 @ rot.T
g = np.linspace(-1, 1, 361)
U_, Wv = np.meshgrid(g, g)
dedans = U_ ** 2 + Wv ** 2 <= 1
Z_ = np.sqrt(np.clip(1 - U_ ** 2 - Wv ** 2, 0, 1))
pts = np.stack([U_, Wv, Z_], axis=-1)
mult = (pts @ V3.T > math.cos(a3)).sum(axis=-1).astype(float)
mult[~dedans] = np.nan
ax.imshow(mult, extent=(-1, 1, -1, 1), origin="lower", cmap=plt.matplotlib.colors.ListedColormap(
    [F.SEQ[2], F.SEQ[6], F.SEQ[10]]), vmin=0.5, vmax=3.5, interpolation="nearest")
for v in V3:
    if v[2] > 0:
        ax.plot([v[0]], [v[1]], "o", ms=9, color=F.ORANGE, mec=F.INK, zorder=6)
cercle(ax, 1, color=F.INK, lw=1)
schema(ax, 1.3)
ax.text(0.5, -0.02, "4 chèvres de dimension 3 (75,8°)\nsur un tétraèdre : chaque point de\nS² est brouté 1, 2 ou 3 fois"
        " (clair → foncé).", transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)

# f) la cohomologie des sphères, de dimension en dimension
ax = fig.add_subplot(gs[1, 2])
NMAX = 8
for n in range(0, NMAX + 1):
    for k in range(0, NMAX + 1):
        plein = (k == 0 or k == n)
        ax.add_patch(plt.Rectangle((k - 0.45, n - 0.45), 0.9, 0.9, fc=(F.SEQ[8] if plein else F.SURF),
                                   ec=F.GRID, lw=0.8, zorder=2))
        if plein:
            ax.text(k, n, "ℤ²" if (n == 0) else "ℤ", ha="center", va="center", color="white", fontsize=9,
                    fontweight="bold", zorder=3)
    if n >= 1:
        ax.annotate("", (n - 0.2, n - 0.2), (n - 0.8, n - 0.8), arrowprops=dict(arrowstyle="->", color=ROUGE, lw=1.2),
                    zorder=4)
    chi = 2 if n % 2 == 0 else 0
    ax.text(NMAX + 1.0, n, f"χ = {chi}", va="center", fontsize=8.6, color=F.ORANGE if chi else F.BLEU)
    if n % 2 == 1:
        ax.text(NMAX + 2.25, n, "i : x ↦ ix" + (" ; parallélisable" if n in (1, 3, 7) else ""), va="center",
                fontsize=8.0, color=F.BLEU)
ax.set_xlim(-0.6, NMAX + 5.6)
ax.set_ylim(-0.6, NMAX + 0.6)
ax.set_xticks(range(NMAX + 1))
ax.set_xticklabels([f"$H^{{{k}}}$" for k in range(NMAX + 1)], fontsize=9)
ax.set_yticks(range(NMAX + 1))
ax.set_yticklabels([f"$S^{{{n}}}$" for n in range(NMAX + 1)], fontsize=9.5)
ax.grid(False)
ax.set_title("f)  La cohomologie des sphères, de dimension en dimension")
ax.text(0.5, -0.08, "Calculée par le nerf des chèvres (tableau du § 3) pour S¹ à S⁸. Flèches rouges : Mayer–Vietoris sur"
        "\nles deux cartes (deux hémisphères), H^(n−1)(S^(n−1)) = H^n(S^n), à partir de S⁰ = deux points. Les sphères"
        "\nimpaires portent i (un champ qui ne s'annule pas) ; S¹, S³ et S⁷ : complexes, quaternions, octonions.",
        transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)
F.sauver(fig, "u1_chevres_faisceaux.png")

# ===========================================================================
# Figure 2 : les deux cartes, le losange, 3-8-24, la musique et l'IA
# ===========================================================================
fig = plt.figure(figsize=(21, 14.6))
gs = fig.add_gridspec(2, 3, wspace=0.18, hspace=0.3)

# a) deux cartes et une inversion de rayon √2
ax = fig.add_subplot(gs[0, 0])
t_s = np.linspace(math.pi, 2 * math.pi, 200)
t_n = np.linspace(0, math.pi, 200)
ax.plot(np.cos(t_s), np.sin(t_s), color=F.AQUA, lw=4)
ax.plot(np.cos(t_n), np.sin(t_n), color=F.ORANGE, lw=4)
ax.plot([-1, 1], [0, 0], color=F.AQUA, lw=6, alpha=0.5, solid_capstyle="butt")
for sg in (1, -1):
    ax.plot([sg * 1, sg * 3.1], [0, 0], color=F.ORANGE, lw=6, alpha=0.5, solid_capstyle="butt")
ax.axhline(0, color=F.INK2, lw=0.8)
cercle(ax, R2, 0, 1, color=ROUGE, lw=1.3, ls="--")
Nn = np.array([0.0, 1.0])
for deg in (-25, -60, -95, -140, 35, 70, 115, 150):
    Pp = np.array([math.cos(math.radians(deg)), math.sin(math.radians(deg))])
    x_img = Pp[0] / (1 - Pp[1])
    c = F.AQUA if deg < 0 else F.ORANGE
    ax.plot([Nn[0], x_img], [Nn[1], 0], color=c, lw=0.8, alpha=0.8)
    ax.plot([Pp[0]], [Pp[1]], "o", ms=5, color=c, mec=F.INK, mew=0.5, zorder=6)
    ax.plot([x_img], [0], "|", ms=12, mew=2, color=c, zorder=6)
ax.plot([0], [1], "o", ms=9, color=F.INK, zorder=7)
ax.text(0.1, 1.12, "N", fontsize=10, fontweight="bold")
ax.plot([0], [-1], "o", ms=7, color=F.INK, zorder=7)
ax.text(0.1, -1.22, "S", fontsize=10, fontweight="bold")
ax.text(-2.55, 2.45, "inversion de centre N,\nrayon √2 (tirets) : elle\nenvoie la sphère sur le\nplan"
        " et fixe l'équateur", fontsize=8.6, color=ROUGE, va="top")
ax.text(-2.55, -0.85, "hémisphère sud (aire ½)\n→ dans le disque unité", fontsize=8.8, color=F.AQUA, fontweight="bold")
ax.text(1.12, 2.3, "hémisphère nord\n(aire ½) → dehors", fontsize=8.8, color=F.ORANGE, fontweight="bold")
schema(ax, 2.6, 2.0)
ax.set_ylim(-1.35, 2.5)
ax.set_title("a)  Deux cartes et une inversion de rayon √2")
ax.text(0.5, -0.02, "Projeter depuis N (carte nord) ou depuis S (carte sud) : chaque carte manque un seul point. On passe"
        "\nde l'une à l'autre par y ↦ y/|y|² : l'inversion. Les deux hémisphères ont chacun la moitié de l'aire :"
        "\nl'un tombe dedans, l'autre dehors. Mayer–Vietoris sur ces deux cartes fait monter la cohomologie.",
        transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)

# b) le réseau et le réseau inversé : le retournement
ax = fig.add_subplot(gs[0, 1])
cercle(ax, 1, color=F.INK, lw=1.2)
for m1 in range(-2, 3):
    for m2 in range(-2, 3):
        n2 = m1 * m1 + m2 * m2
        if 0 < n2 <= 5:
            ax.plot([m1], [m2], "o", ms=5, color=F.INK2, zorder=4)
            ax.plot([m1 / n2], [m2 / n2], "o", ms=8 if n2 <= 2 else 6, mfc=F.SURF,
                    mec=ROUGE if n2 == 1 else (VIOLET if n2 == 2 else F.ORANGE), mew=1.8, zorder=5)
ax.add_patch(Polygon([(1, 1), (-1, 1), (-1, -1), (1, -1)], closed=True, fill=False, ec=F.BLEU, lw=1.6, ls="--"))
ax.add_patch(Polygon([(1, 0), (0, 1), (-1, 0), (0, -1)], closed=True, fill=False, ec=ROUGE, lw=2.0))
for (a_, b_) in ((1, 1), (-1, 1), (2, 0), (2, 1)):
    n2 = a_ * a_ + b_ * b_
    ax.annotate("", (a_ / n2 * 1.04, b_ / n2 * 1.04), (a_ * 0.97, b_ * 0.97),
                arrowprops=dict(arrowstyle="->", color=VIOLET if n2 == 2 else F.ORANGE, lw=1.1, alpha=0.9))
ax.text(1.08, 1.1, "avant : carré (±1, ±1),\nmilieux des côtés à 1", color=F.BLEU, fontsize=8.6)
ax.text(-2.3, 1.55, "après : losange (±1, 0), (0, ±1),\nmilieux des côtés à 1/√2", color=ROUGE, fontsize=8.6)
schema(ax, 2.35)
ax.set_title("b)  Le réseau et le réseau inversé : le retournement")
ax.text(0.5, -0.02, "Points : le réseau (les fantômes de la lame de zones). Cercles : le réseau inversé m/|m|² (ceux de"
        "\nl'étoile de Siemens, à un quart de tour près). L'inversion fixe le cercle unité et échange sommets et"
        "\nmilieux : le carré devient le losange. C'est la transition entre les deux cartes du panneau a.",
        transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)

# c) le polytope croisé : l'arête √2 dans toutes les dimensions, et le retournement de l'aiguille
ax = fig.add_subplot(gs[0, 2])
Rv = np.linalg.qr(np.array([[0.85, -0.45, 0.25], [0.35, 0.85, 0.4], [-0.4, -0.2, 0.9]]))[0]
proj = lambda v: (Rv @ np.asarray(v, float))[:2]
prof = lambda v: (Rv @ np.asarray(v, float))[2]
E3 = [np.eye(3)[i] * s for i in range(3) for s in (1, -1)]
cercle(ax, 1 / R2, color=VIOLET, lw=1.0, ls=":")
cercle(ax, 1, color=F.BASE, lw=0.8)
for a_, b_ in itertools.combinations(E3, 2):
    if abs(a_ @ b_) < 1e-9:
        pa, pb = proj(a_), proj(b_)
        derriere = prof(a_) + prof(b_) < 0
        ax.plot([pa[0], pb[0]], [pa[1], pb[1]], color=F.INK2, lw=0.9 if derriere else 1.5,
                ls=":" if derriere else "-", alpha=0.8)
        mid = proj((a_ + b_) / 2)
        ax.plot([mid[0]], [mid[1]], "o", ms=5, mfc=F.SURF, mec=VIOLET, mew=1.2, zorder=5)
for v in E3:
    p_ = proj(v)
    ax.plot([p_[0]], [p_[1]], "o", ms=8, color=F.INK, mec=F.SURF, zorder=6)


def arc3(u, v, n_=60):
    s = np.linspace(0, 1, n_)
    pts_ = np.array([math.cos(x * math.pi / 2) * u + math.sin(x * math.pi / 2) * v for x in s])
    return np.array([proj(q) for q in pts_])


e1, e2, e3 = np.eye(3)
for (u, v, w), c, ls in (((e1, e2, -e1), ROUGE, "-"), ((e1, e3, -e1), F.ORANGE, "--")):
    for a_, b_ in ((u, v), (v, w)):
        A = arc3(a_, b_)
        ax.plot(A[:, 0], A[:, 1], color=c, lw=2.2, ls=ls)
ax.annotate("", proj(e1), (0, 0), arrowprops=dict(arrowstyle="-|>", color=F.INK, lw=2.4))
for v, nom in ((e1, "e₁"), (e2, "e₂"), (e3, "e₃"), (-e1, "−e₁")):
    p_ = proj(v)
    ax.text(p_[0] * 1.13, p_[1] * 1.13 + 0.03, nom, fontsize=10, fontweight="bold", ha="center")
ax.text(-1.48, -1.18, "arêtes √2 (toutes), milieux à 1/√2 (cercle violet) :\nn = 2 : 4 arêtes ; 3 : 12 ; 4 : 24 (D₄) ;"
        " 8 : 112 (D₈)", fontsize=8.4, color=F.INK2)
ax.text(0.45, 1.12, "retourner = deux quarts de tour :\npar e₂ (rouge) ou par e₃ (orange)", fontsize=8.6, color=ROUGE)
schema(ax, 1.5, 1.3)
ax.set_title("c)  Le polytope croisé : l'arête √2 en toute dimension")
ax.text(0.5, -0.02, "L'octaèdre ±e_i (la version 3D du losange). Retourner l'aiguille e₁ en −e₁, c'est i·i = −1 : deux"
        "\nquarts de tour par une direction perpendiculaire. En 2D, deux chemins (i ou −i, comme 3 et 7 modulo 10) ;"
        "\nen 3D, un cercle de chemins ; en dimension infinie, une infinité.", transform=ax.transAxes, ha="center",
        va="top", fontsize=8.4, color=F.INK2)

# d) 3, 8, 24 : le centre du cube vu des coins
ax = fig.add_subplot(gs[1, 0])
nn = np.arange(1, 25)
for d_ in (1, 2, 3, 8, 24):
    ax.axvspan(d_ - 0.4, d_ + 0.4, color=F.JAUNE, alpha=0.18, lw=0)
ax.plot(nn, np.sqrt(nn) / 2, "o-", color=F.BLEU, ms=5, lw=1.2, zorder=4)
for val, nom, c in ((1 / R2, "1/√2 : le demi-disque", VIOLET), (1.0, "1 : les voisins de ℤ⁴", F.INK2),
                    (R2, "√2 : la diagonale 1x, 1y", ROUGE)):
    ax.axhline(val, color=c, lw=1.0, ls="--")
    ax.text(24.6, val + 0.03, nom, color=c, fontsize=8.6, ha="right", va="bottom")
for d_, c in ((2, VIOLET), (4, F.INK), (8, ROUGE)):
    ax.plot([d_], [math.sqrt(d_) / 2], "o", ms=11, color=c, mec=F.SURF, zorder=6)
for d_, kiss in ((1, "2"), (2, "6"), (3, "12"), (4, "24"), (8, "240"), (24, "196 560")):
    ax.text(d_, 2.72, kiss, ha="center", fontsize=8.6, color=F.ORANGE, fontweight="bold")
ax.text(12, 2.88, "sphères qui en touchent une (le meilleur empilement)", ha="center", fontsize=8.4, color=F.ORANGE)
ax.text(4.3, 2.25, "E₈ = D₈ ∪ (D₈ + ½·(1, …, 1)) :\n112 + 128 = 240 voisins", fontsize=8.8, color=ROUGE)
ax.set_xlim(0.3, 24.8)
ax.set_ylim(0, 3.05)
ax.set_xticks([1, 2, 3, 4, 8, 12, 16, 24])
ax.set_xlabel("dimension n")
ax.set_ylabel("distance du centre du cube aux coins : √n/2")
ax.set_title("d)  3, 8, 24 : le centre du pixel vu de ses coins")
ax.text(0.5, -0.13, "Bandes jaunes : les dimensions où le meilleur empilement de sphères est démontré (1, 2, 3, 8, 24)."
        "\nEn 8, le centre du cube est à √2 des coins, comme les plus proches voisins : la grille décalée d'une"
        "\ndemi-maille (partie XV) devient E₈, l'empilement record.", transform=ax.transAxes, ha="center", va="top",
        fontsize=8.4, color=F.INK2)

# e) 2 et 3 donnent 12 : le cercle des quintes
ax = fig.add_subplot(gs[1, 1])
cercle(ax, 1, color=F.BASE, lw=1.2)
Q = math.log2(1.5)
noms = ["Do", "Sol", "Ré", "La", "Mi", "Si", "Fa♯", "Do♯", "Sol♯", "Ré♯", "La♯", "Mi♯", "Si♯"]
pq = []
for k in range(13):
    th = math.pi / 2 - 2 * math.pi * ((k * Q) % 1)
    pq.append((math.cos(th), math.sin(th)))
for k in range(12):
    ax.plot([pq[k][0], pq[k + 1][0]], [pq[k][1], pq[k + 1][1]], color=F.SEQ[6], lw=1.0, alpha=0.8)
for k, (x_, y_) in enumerate(pq):
    c = ROUGE if k == 12 else (F.INK if k == 0 else F.BLEU)
    ax.plot([x_], [y_], "o", ms=8, color=c, mec=F.SURF, zorder=6)
    r_lab = 1.16 if k != 12 else 1.32
    ax.text(x_ * r_lab, y_ * r_lab, noms[k], ha="center", va="center", fontsize=8.8, color=c, fontweight="bold")
th12 = math.pi / 2 - 2 * math.pi * ((12 * Q) % 1)
tt_ = np.linspace(th12, math.pi / 2, 30)
ax.plot(1.05 * np.cos(tt_), 1.05 * np.sin(tt_), color=ROUGE, lw=3)
ax.text(0.0, 0.0, "3¹² ≈ 2¹⁹\n(réduite 19/12 de log₂ 3)\n\ncomma : 23,46 cents\npas : 90,22 et 113,69 cents",
        ha="center", va="center", fontsize=9, color=F.INK, bbox=dict(fc=F.SURF, ec=F.BASE, pad=4))
schema(ax, 1.45)
ax.set_title("e)  2 et 3 donnent 12 : le cercle des quintes")
ax.text(0.5, -0.02, "Chaque quinte (× 3/2) fait tourner de log₂(3/2) = 0,585 octave : une rotation irrationnelle, comme"
        "\nle cercle des décades (partie XIX). Après 12 quintes, on revient presque au départ (arc rouge). Les gammes"
        "\nà 5, 7 et 12 notes n'ont que deux tailles de pas : le théorème des trois distances (partie XI).",
        transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)

# f) Archimède, la chèvre infinie et l'IA : la même loi
ax = fig.add_subplot(gs[1, 2])
ts = np.linspace(-0.999, 0.999, 2001)
for d_, c in ((2, F.ORANGE), (3, F.INK), (4, F.SEQ[5]), (10, F.SEQ[8]), (30, F.SEQ[10]), (100, F.SEQ[13])):
    dens = (1 - ts ** 2) ** ((d_ - 3) / 2)
    dens /= np.trapezoid(dens, ts)
    ax.plot(ts, dens, color=c, lw=2.4 if d_ == 3 else 1.6, label=f"d = {d_}" + (" : plat (Archimède)" if d_ == 3 else ""))
t100 = 1 - IA[100] ** 2 / 2
ax.hist(t100, bins=80, density=True, histtype="step", color=F.SEQ[13], lw=0.8, ls=":")
ax.axvline(0, color=ROUGE, lw=1.0, ls="--")
ax.text(-0.86, 4.45, "t = 0 : distance √2,\nla chèvre de dimension infinie", color=ROUGE, fontsize=8.6, va="top")
ax.text(-0.86, 3.55, "d = 4096 (un plongement d'IA) :\npic à 25, hors du cadre ;\nécart-type 1/√4096 = 0,016", fontsize=8.4,
        color=F.SEQ[13], va="top")
ax.set_ylim(0, 4.6)
ax.set_xlim(-1, 1)
ax.set_xlabel("t = u·v (cosinus entre deux directions au hasard)")
ax.set_ylabel("densité ∝ (1 − t²)^((d − 3)/2)")
ax.legend(loc="upper right", fontsize=8.0, frameon=True, facecolor=F.SURF, edgecolor="none")
top = ax.secondary_xaxis("top", functions=(lambda x: np.sqrt(np.clip(2 - 2 * x, 0, 4)), lambda dd: 1 - dd ** 2 / 2))
top.set_xticks([0.5, 1.0, R2, 1.75, 2.0])
top.set_xticklabels(["0,5", "1", "√2", "1,75", "2"])
top.set_xlabel("distance |u − v|", fontsize=8.6)
ax.set_title("f)  Archimède, la chèvre infinie et l'IA : la même loi", pad=28)
ax.text(0.5, -0.13, "La même densité décrit l'ombre de la sphère sur un axe et l'angle entre deux directions au hasard."
        "\nEn 3D elle est plate (la boîte à chapeau d'Archimède) ; en grande dimension, tout se masse en t = 0 : deux"
        "\ndirections sans rapport sont à √2 l'une de l'autre (pointillés : 2·10⁴ paires en d = 100).",
        transform=ax.transAxes, ha="center", va="top", fontsize=8.4, color=F.INK2)
F.sauver(fig, "u2_cartes_losange.png")
