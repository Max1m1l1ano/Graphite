"""
Bibliothèque de la partie II : Archimède, le cube qui tourne, le ménisque,
et les chèvres dans des solides et des polygones.

Conventions : rayon de la sphère R = 1 sauf mention contraire.
"""

from math import acos, atan2, cos, pi, sin, sqrt

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.spatial import ConvexHull

# ---------------------------------------------------------------------------
# 1. Aires exactes dans le plan
# ---------------------------------------------------------------------------


def lentille(R, r, d):
    """Aire commune de deux disques (rayons R et r, centres à distance d)."""
    if r <= 0 or R <= 0 or d >= R + r:
        return 0.0
    if d <= abs(R - r):
        return pi * min(R, r) ** 2
    a1 = acos((d * d + R * R - r * r) / (2 * d * R))
    a2 = acos((d * d + r * r - R * R) / (2 * d * r))
    return R * R * a1 + r * r * a2 - 0.5 * sqrt(max(0.0, (-d + r + R) * (d + r - R) * (d - r + R) * (d + r + R)))


def _triangle_disque(a, b, r):
    """Aire signée de triangle(0, a, b) ∩ disque(0, r) : le segment ab est coupé aux
    points où il traverse le cercle ; chaque morceau compte comme un triangle (dedans)
    ou comme un secteur (dehors)."""
    d = b - a
    A, B, C = d @ d, 2 * (a @ d), a @ a - r * r
    ts = [0.0]
    disc = B * B - 4 * A * C
    if A > 0 and disc > 0:
        q = sqrt(disc)
        ts += [t for t in sorted(((-B - q) / (2 * A), (-B + q) / (2 * A))) if 0 < t < 1]
    ts.append(1.0)
    total = 0.0
    for t0, t1 in zip(ts[:-1], ts[1:]):
        p, s, m = a + t0 * d, a + t1 * d, a + 0.5 * (t0 + t1) * d
        croix = p[0] * s[1] - p[1] * s[0]
        total += 0.5 * croix if m @ m <= r * r else 0.5 * r * r * atan2(croix, p @ s)
    return total


def aire_polygone_disque(poly, centre, r):
    """Aire exacte de (polygone convexe) ∩ (disque de centre `centre` et de rayon r)."""
    if r <= 0:
        return 0.0
    P = np.asarray(poly, float) - np.asarray(centre, float)
    return abs(sum(_triangle_disque(P[i], P[(i + 1) % len(P)], r) for i in range(len(P))))


def aire_polygone(poly):
    P = np.asarray(poly, float)
    x, y = P[:, 0], P[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))


def polygone_regulier(n, R=1.0, phase=0.0):
    return [(R * cos(phase + 2 * pi * j / n), R * sin(phase + 2 * pi * j / n)) for j in range(n)]


def corde_moitie_polygone(poly, piquet, rmax=4.0):
    """Corde qui broute la moitié du polygone depuis `piquet`."""
    cible = aire_polygone(poly) / 2
    return brentq(lambda r: aire_polygone_disque(poly, piquet, r) - cible, 1e-6, rmax, xtol=1e-14)


# ---------------------------------------------------------------------------
# 2. Polyèdres inscrits dans la sphère unité, découpés en tranches
# ---------------------------------------------------------------------------

PHI = (1 + sqrt(5)) / 2


def icosaedre():
    V = []
    for a in (-1, 1):
        for b in (-PHI, PHI):
            V += [(0, a, b), (a, b, 0), (b, 0, a)]
    V = np.array(V, float)
    return V / np.linalg.norm(V[0])


def polyedre(nom):
    """Sommets (sur la sphère unité) d'un solide de Platon ou d'une sphère géodésique 'geoN'."""
    if nom.startswith("geo"):
        nu = int(nom[3:])
        V0 = icosaedre()
        pts = []
        for f in ConvexHull(V0).simplices:
            A, B, C = V0[f]
            for i in range(nu + 1):
                for j in range(nu + 1 - i):
                    p = (i * A + j * B + (nu - i - j) * C) / nu
                    pts.append(p / np.linalg.norm(p))
        return np.unique(np.round(np.array(pts), 12), axis=0)
    if nom == "tetra":
        V = np.array([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)], float)
    elif nom == "octa":
        V = np.array([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)], float)
    elif nom == "cube":
        V = np.array([(i, j, k) for i in (-1, 1) for j in (-1, 1) for k in (-1, 1)], float)
    elif nom == "icosa":
        return icosaedre()
    elif nom == "dodeca":
        V = [(i, j, k) for i in (-1, 1) for j in (-1, 1) for k in (-1, 1)]
        for a in (-1, 1):
            for b in (-1, 1):
                V += [(0, a / PHI, b * PHI), (a / PHI, b * PHI, 0), (b * PHI, 0, a / PHI)]
        V = np.array(V, float)
    else:
        raise ValueError(nom)
    return V / np.linalg.norm(V, axis=1, keepdims=True)


def tourner_vers_le_haut(V, v):
    """Rotation qui envoie le vecteur unitaire v sur (0, 0, 1)."""
    z = np.array([0.0, 0.0, 1.0])
    v = v / np.linalg.norm(v)
    c = v @ z
    if abs(c - 1) < 1e-14:
        return V
    if abs(c + 1) < 1e-14:
        return V * np.array([1, -1, -1])
    k = np.cross(v, z)
    s = np.linalg.norm(k)
    k /= s
    K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    return V @ (np.eye(3) + s * K + (1 - c) * K @ K).T


class Tranches:
    """Polyèdre convexe découpé par les plans z = cste (le piquet est en (0, 0, 1))."""

    def __init__(self, V):
        H = ConvexHull(V)
        aretes = set()
        for f in H.simplices:
            for a, b in ((f[0], f[1]), (f[1], f[2]), (f[0], f[2])):
                aretes.add((min(a, b), max(a, b)))
        E = np.array(sorted(aretes))
        self.A, self.B = V[E[:, 0]], V[E[:, 1]]
        self.volume = H.volume
        self.faces = len(H.simplices)
        self.hauteurs = np.unique(np.round(V[:, 2], 12))

    def polygone(self, z):
        za, zb = self.A[:, 2], self.B[:, 2]
        m = (np.minimum(za, zb) <= z) & (np.maximum(za, zb) >= z) & (za != zb)
        t = (z - za[m]) / (zb[m] - za[m])
        P = self.A[m, :2] + t[:, None] * (self.B[m, :2] - self.A[m, :2])
        if len(P) < 3:
            return None
        try:
            return P[ConvexHull(P).vertices]
        except Exception:
            return None

    def volume_dans_boule(self, r):
        """Volume du polyèdre à moins de r du piquet (0, 0, 1)."""
        def aire(z):
            P = self.polygone(z)
            rho = sqrt(max(0.0, r * r - (1 - z) ** 2))
            return 0.0 if P is None else aire_polygone_disque(P, (0, 0), rho)
        bas = max(self.hauteurs[0], 1 - r)
        pts = [z for z in self.hauteurs if bas < z < 1]
        return quad(aire, bas, 1.0, points=pts or None, limit=max(200, 4 * len(pts)),
                    epsabs=1e-12, epsrel=1e-11)[0]


def corde_moitie_polyedre(nom):
    V = polyedre(nom)
    if nom.startswith("geo"):  # piquet sur un sommet d'origine de l'icosaèdre (5 voisins)
        haut = V[np.argmin(np.linalg.norm(V - icosaedre()[0], axis=1))]
    else:
        haut = V[np.argmax(V[:, 2])]
    T = Tranches(tourner_vers_le_haut(V, haut))
    r = brentq(lambda r: T.volume_dans_boule(r) - T.volume / 2, 0.3, 2.0, xtol=1e-11)
    return r, len(V), T.faces, T.volume


# ---------------------------------------------------------------------------
# 3. Chèvres dans les solides d'Archimède (piquet T = (1, 0, 0), au contact
#    de la sphère, du cylindre et du cube ; tranches z = cste)
# ---------------------------------------------------------------------------

CARRE = [(-1, -1), (1, -1), (1, 1), (-1, 1)]


def volume_brouté(solide, r):
    """Volume à moins de r de T = (1, 0, 0) dans : 'boule', 'cylindre' (rayon 1, |z| ≤ 1),
    'anneau' (cylindre moins double cône, |z| ≤ ρ ≤ 1 : même volume que la boule),
    'cube' ([-1, 1]^3)."""
    def tranche(z):
        k = sqrt(max(0.0, r * r - z * z))
        if solide == "boule":
            return lentille(sqrt(max(0.0, 1 - z * z)), k, 1.0)
        if solide == "cylindre":
            return lentille(1.0, k, 1.0)
        if solide == "anneau":
            return lentille(1.0, k, 1.0) - (lentille(abs(z), k, 1.0) if z != 0 else 0.0)
        if solide == "cube":
            return aire_polygone_disque(CARRE, (1, 0), k)
        raise ValueError(solide)
    zm = min(r, 1.0)
    return quad(tranche, -zm, zm, limit=200, epsabs=1e-12, epsrel=1e-11)[0]


VOLUMES = {"boule": 4 * pi / 3, "cylindre": 2 * pi, "anneau": 4 * pi / 3, "cube": 8.0}


def corde_moitie_solide(solide):
    return brentq(lambda r: volume_brouté(solide, r) - VOLUMES[solide] / 2, 0.5, 3.4, xtol=1e-12)


# ---------------------------------------------------------------------------
# 4. Le cube qui tourne autour de sa grande diagonale (arête 1)
# ---------------------------------------------------------------------------

_U = np.ones(3) / sqrt(3)
_SOMMETS = np.array([[i, j, k] for i in (0, 1) for j in (0, 1) for k in (0, 1)], float)
_ARETES = [(a, b) for a in range(8) for b in range(a + 1, 8)
           if np.sum(np.abs(_SOMMETS[a] - _SOMMETS[b])) == 1]


def rayon2_balayé(s):
    """Carré du rayon du solide balayé à l'abscisse s le long de la diagonale (0 ≤ s ≤ √3),
    calculé directement sur les arêtes du cube."""
    best = 0.0
    for a, b in _ARETES:
        A, B = _SOMMETS[a], _SOMMETS[b]
        sa, sb = A @ _U, B @ _U
        if sa != sb and (sa - s) * (sb - s) <= 0:
            X = A + (s - sa) / (sb - sa) * (B - A)
            best = max(best, X @ X - s * s)
    return best


def profil_balayé(s):
    """Même chose en formule : cônes r² = 2s² aux bouts, hyperboloïde r² = 1/2 + 2(s − √3/2)² au milieu."""
    s0 = sqrt(3) / 2
    if s <= 1 / sqrt(3):
        return 2 * s * s
    if s >= 2 / sqrt(3):
        return 2 * (sqrt(3) - s) ** 2
    return 0.5 + 2 * (s - s0) ** 2


# ---------------------------------------------------------------------------
# 5. Le ménisque dans un tube (calotte sphérique, régime a ≪ longueur capillaire)
# ---------------------------------------------------------------------------


def anneau_menisque(theta_deg):
    """Volume oublié en lisant au point extrême du ménisque (bas si concave, haut si convexe),
    en unités de π a³ (a = rayon du tube) : (1 − S)(1 + 2S) / (3 C (1 + S)), S = sin θ, C = |cos θ|.
    θ = 0 : hémisphère, l'anneau oublié est le cône d'Archimède, 1/3."""
    t = np.radians(theta_deg)
    S, C = np.sin(t), np.abs(np.cos(t))
    return (1 - S) * (1 + 2 * S) / (3 * C * (1 + S))


def profondeur_menisque(theta_deg):
    """Flèche du ménisque (calotte) en unités de a : (1 − sin θ)/|cos θ|."""
    t = np.radians(theta_deg)
    return (1 - np.sin(t)) / np.abs(np.cos(t))


LIQUIDES = {  # tension (N/m), masse volumique (kg/m³), angle de contact sur verre (°) ; valeurs usuelles à 20 °C
    "eau": (0.0728, 998.2, 0.0),
    "mercure": (0.485, 13534.0, 140.0),
}
G = 9.81


def longueur_capillaire(liquide):
    g_, rho, _ = LIQUIDES[liquide]
    return sqrt(g_ / (rho * G))


def jurin(liquide, a):
    """Hauteur d'ascension (m) dans un tube de rayon a (m) : 2γ cos θ / (ρ g a)."""
    g_, rho, th = LIQUIDES[liquide]
    return 2 * g_ * cos(np.radians(th)) / (rho * G * a)


# ---------------------------------------------------------------------------
# 6. Trois façons de découper l'aire de la chèvre (plan)
# ---------------------------------------------------------------------------


def aire_riemann(r, N):
    """Bandes verticales (somme de Riemann au point milieu) sur [1 − r, 1]."""
    x = 1 - r + (np.arange(N) + 0.5) * r / N
    h = 2 * np.minimum(np.sqrt(np.clip(1 - x * x, 0, None)), np.sqrt(np.clip(r * r - (x - 1) ** 2, 0, None)))
    return h.sum() * r / N


def aire_niveaux(r, N, gauss=False):
    """Par niveaux de distance au piquet (formule de la coaire) : A(r) = ∫ 2ρ arccos(ρ/2) dρ."""
    if gauss:
        x, w = np.polynomial.legendre.leggauss(N)
        rho = r * (x + 1) / 2
        return (r / 2) * np.sum(w * 2 * rho * np.arccos(rho / 2))
    rho = (np.arange(N) + 0.5) * r / N
    return np.sum(2 * rho * np.arccos(rho / 2)) * r / N


# ---------------------------------------------------------------------------
# 7. Dimensions : maxima selon l'unité, projection de la sphère sur un axe
# ---------------------------------------------------------------------------


def dimension_du_maximum(R, quoi="volume"):
    """Dimension entière qui maximise V_n(R) (ou S_{n-1}(R)) : dépend de l'unité R."""
    from scipy.special import gammaln
    n = np.arange(1, 400)
    if quoi == "volume":
        lv = 0.5 * n * np.log(pi) + n * np.log(R) - gammaln(n / 2 + 1)
    else:
        lv = np.log(2) + 0.5 * n * np.log(pi) + (n - 1) * np.log(R) - gammaln(n / 2)
    return int(n[np.argmax(lv)])


def densite_projection(n, z):
    """Densité de la projection de l'aire de la sphère S^{n-1} sur un axe : ∝ (1 − z²)^((n−3)/2)."""
    from scipy.special import beta
    return (1 - z * z) ** ((n - 3) / 2) / beta(0.5, (n - 1) / 2)
