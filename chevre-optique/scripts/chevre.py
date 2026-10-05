"""
Bibliothèque commune : problème de la chèvre, intégrales de contour, n dimensions.

Conventions (partout) :
  - le champ est la boule unité de R^n (rayon R = 1), centre O ;
  - le piquet P est à la distance `delta` de O (delta = 1 : piquet sur le bord) ;
  - la corde a la longueur `k` (on note aussi r quand delta = 1) ;
  - "fraction broutée" = vol(B(O,1) ∩ B(P,k)) / vol(B(O,1)).

Deux familles de fonctions :
  - versions mpmath (précision arbitraire) pour les tableaux de valeurs ;
  - versions numpy/scipy (vectorisées) pour les figures.
"""

import math

import mpmath as mp
import numpy as np
from scipy.special import betainc, gammaln

# ---------------------------------------------------------------------------
# 1. Intégrales de contour : le quotient d'Ullisch et le principe de l'argument
# ---------------------------------------------------------------------------


def racine_par_quotient(f, centre, rayon, N=128):
    """Racine simple z0 de f à l'intérieur du cercle |z - centre| = rayon.

    z0 = ∮ z/f(z) dz / ∮ 1/f(z) dz  (théorème des résidus : le facteur
    inconnu 1/f'(z0) apparaît en haut et en bas, la division l'élimine).
    Les deux intégrales sont évaluées par la règle des trapèzes sur le cercle,
    qui converge exponentiellement vite pour un intégrande analytique périodique.
    """
    num = mp.mpc(0)
    den = mp.mpc(0)
    for j in range(N):
        w = mp.expjpi(2 * mp.mpf(j) / N)  # e^{2iπ j/N} ; dz = i·rayon·w dθ
        z = centre + rayon * w
        fz = f(z)
        num += z * w / fz
        den += w / fz
    return num / den  # les facteurs i·rayon·2π/N se simplifient


def nombre_de_zeros(f, centre, rayon, N=800):
    """Nombre de zéros de f dans le disque (principe de l'argument).

    (1/2π) × variation totale de arg f le long du cercle ; doit valoir 1
    pour que le quotient ci-dessus soit légitime.
    """
    total = mp.mpf(0)
    precedent = None
    for j in range(N + 1):
        a = mp.arg(f(centre + rayon * mp.expjpi(2 * mp.mpf(j) / N)))
        if precedent is not None:
            d = a - precedent
            while d > mp.pi:
                d -= 2 * mp.pi
            while d < -mp.pi:
                d += 2 * mp.pi
            total += d
        precedent = a
    return total / (2 * mp.pi)


# ---------------------------------------------------------------------------
# 2. Calottes sphériques en dimension n
# ---------------------------------------------------------------------------


def W(n, t):
    """W_n(t) = ∫_0^t sin^n(φ) dφ, fonction entière (t complexe accepté).

    Récurrence : W_n = -sin^{n-1} t cos t / n + (n-1)/n · W_{n-2},
    W_0 = t, W_1 = 1 - cos t.  La fraction de volume d'une calotte de la
    boule unité de R^n d'angle au centre t (0 ≤ t ≤ π) vaut W_n(t)/W_n(π).
    """
    if n == 0:
        return t
    if n == 1:
        return 1 - mp.cos(t)
    return -mp.sin(t) ** (n - 1) * mp.cos(t) / n + mp.mpf(n - 1) / n * W(n - 2, t)


def W_pi(n):
    """W_n(π) = √π Γ((n+1)/2) / Γ(n/2 + 1)  (intégrale de Wallis)."""
    n = mp.mpf(n)
    return mp.sqrt(mp.pi) * mp.gamma((n + 1) / 2) / mp.gamma(n / 2 + 1)


def equation_chevre(n):
    """F_n(α) = W_n(2α) - (2 cos α)^n W_n(α) - W_n(π)/2, entière en α.

    La corde vaut r = 2 cos α, où α est l'angle en P entre PO et le point
    d'intersection des deux sphères.  Pour n = 2 on retrouve exactement
    (sin β - β cos β - π/2)/2 avec β = 2α : l'équation d'Ullisch.
    """
    demi = W_pi(n) / 2
    return lambda a: W(n, 2 * a) - (2 * mp.cos(a)) ** n * W(n, a) - demi


def fraction_calotte_mp(n, theta):
    """Fraction de volume de la calotte d'angle au centre theta (0..π), mpmath."""
    a = (mp.mpf(n) + 1) / 2
    I = mp.betainc(a, mp.mpf(1) / 2, 0, mp.sin(theta) ** 2, regularized=True)
    return I / 2 if theta <= mp.pi / 2 else 1 - I / 2


def fraction_broutee_mp(n, k, delta=1):
    """vol(B(O,1) ∩ B(P,k)) / vol(B(O,1)) avec |OP| = delta, en mpmath."""
    k = mp.mpf(k)
    delta = mp.mpf(delta)
    if delta >= 1 + k:
        return mp.mpf(0)  # disjoints (au plus tangents extérieurement)
    if delta <= k - 1:
        return mp.mpf(1)  # le champ est dans le cercle de corde
    if delta <= 1 - k:
        return k ** n  # la corde ne sort pas du champ (cercle inscrit à la limite)
    x0 = (1 + delta**2 - k**2) / (2 * delta)  # hyperplan radical (plan des intersections)
    th1 = mp.acos(x0)  # calotte du champ, vue de O
    th2 = mp.acos((delta - x0) / k)  # calotte de la boule de corde, vue de P
    return fraction_calotte_mp(n, th1) + k**n * fraction_calotte_mp(n, th2)


def corde_moitie_mp(n, delta=1):
    """Longueur de corde k telle que la chèvre broute la moitié du champ."""
    delta = mp.mpf(delta)
    k_interieur = mp.mpf(2) ** (-mp.mpf(1) / n)  # boule de demi-volume
    if delta + k_interieur <= 1:
        return k_interieur  # la boule de corde tient dans le champ
    gauche = max(k_interieur, abs(1 - delta))
    droite = 1 + delta
    return mp.findroot(lambda k: fraction_broutee_mp(n, k, delta) - mp.mpf(1) / 2,
                       (gauche, droite), solver="anderson")


# --- versions numpy (vectorisées) pour les figures --------------------------


def fraction_calotte(n, theta):
    theta = np.asarray(theta, dtype=float)
    I = betainc((n + 1) / 2, 0.5, np.sin(theta) ** 2)
    return np.where(theta <= np.pi / 2, I / 2, 1 - I / 2)


def fraction_broutee(n, k, delta=1.0):
    """Version numpy de fraction_broutee_mp (k et delta peuvent être des tableaux)."""
    k, delta = np.broadcast_arrays(np.asarray(k, dtype=float), np.asarray(delta, dtype=float))
    out = np.empty(k.shape)
    disjoint = delta >= 1 + k
    englouti = delta <= k - 1
    dedans = delta <= 1 - k
    partiel = ~(disjoint | englouti | dedans)
    out[disjoint] = 0.0
    out[englouti] = 1.0
    out[dedans] = k[dedans] ** n
    kp, dp = k[partiel], delta[partiel]
    x0 = (1 + dp**2 - kp**2) / (2 * dp)
    th1 = np.arccos(np.clip(x0, -1, 1))
    th2 = np.arccos(np.clip((dp - x0) / kp, -1, 1))
    # k^n · fraction : en log pour éviter les débordements quand n est grand
    with np.errstate(divide="ignore"):
        terme2 = np.exp(n * np.log(kp) + np.log(fraction_calotte(n, th2)))
    out[partiel] = fraction_calotte(n, th1) + terme2
    return out


def corde_moitie(n, delta=1.0):
    """Version flottante (bissection) de corde_moitie_mp."""
    k_int = 2.0 ** (-1.0 / n)
    if delta + k_int <= 1:
        return k_int
    lo, hi = max(k_int, abs(1 - delta)), 1 + delta
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if fraction_broutee(n, mid, delta) < 0.5:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# 3. Boules en dimension n : volume, surface
# ---------------------------------------------------------------------------


def volume_boule(n):
    """V_n = π^{n/2} / Γ(n/2 + 1) (boule unité)."""
    return math.exp(0.5 * n * math.log(math.pi) - gammaln(n / 2 + 1))


def surface_sphere(n):
    """S_{n-1} = dV_n/dR = n V_n = 2 π^{n/2} / Γ(n/2) (sphère unité de R^n)."""
    return n * volume_boule(n)


# ---------------------------------------------------------------------------
# 4. Cas plan : aire de la lentille (intersection de deux disques)
# ---------------------------------------------------------------------------


def aire_lentille(R, r, d):
    """Aire de l'intersection de deux disques (rayons R, r, centres à distance d).

    C'est la même fonction qui donne : l'herbe broutée, l'obscuration d'une
    éclipse, la lumière transmise en vignettage mécanique, et (pour R = r)
    la FTM d'un objectif limité par la diffraction.
    """
    R, r, d = (np.asarray(v, dtype=float) for v in (R, r, d))
    R, r, d = np.broadcast_arrays(R, r, d)
    out = np.zeros(R.shape)
    inclus = d <= np.abs(R - r)
    out[inclus] = np.pi * np.minimum(R, r)[inclus] ** 2
    p = (d < R + r) & ~inclus
    Rp, rp, dp = R[p], r[p], d[p]
    a1 = np.arccos(np.clip((dp**2 + Rp**2 - rp**2) / (2 * dp * Rp), -1, 1))
    a2 = np.arccos(np.clip((dp**2 + rp**2 - Rp**2) / (2 * dp * rp), -1, 1))
    k = np.sqrt(np.clip((-dp + rp + Rp) * (dp + rp - Rp) * (dp - rp + Rp) * (dp + rp + Rp), 0, None))
    out[p] = Rp**2 * a1 + rp**2 * a2 - 0.5 * k
    return out


def ftm_diffraction(s):
    """FTM d'une pupille circulaire sans aberration, s = ν/ν_c (ν_c = 1/(λN)).

    = recouvrement normalisé de deux disques identiques décalés de 2s rayons.
    """
    s = np.clip(np.asarray(s, dtype=float), 0, 1)
    return (2 / np.pi) * (np.arccos(s) - s * np.sqrt(1 - s**2))
