"""
Partie XIII : les Perron tournés de 90°, les branchages et le déphasage cos/sin.

    python3 scripts/perron_dephasage.py        # ≈ 10 s

Écrit resultats/perron_dephasage.md et figures/m1_perron_dephasage.png.

1. Les branchages entourés en rouge (spectre local de la partie XI) : des nœuds où les aiguilles repliées se croisent,
   placés exactement aux centres fantômes des sommes et des différences de composantes.
2. Le déphasage de 90° (cos → sin) sur la lame de zones : relatif, commun, et d'une rangée de pixels à l'autre.
3. L'arbre de Perron tourné de 90° : ses aiguilles deviennent des fréquences qui glissent. Même déphasage, même loi.
4. Tourner de 90° le plan position–fréquence, c'est prendre la transformée de Fourier (vérification exacte).
5. La bande 2,44–2,56 : la chèvre face à Fibonacci, aux bases 2, 10, 12 et 60 et aux constantes déjà rencontrées.
"""

import logging
import os
import sys
from fractions import Fraction

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon
from matplotlib.path import Path
from scipy.optimize import brentq
from scipy.special import betainc, gamma

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


def periode(s):
    """Période dominante d'une courbe échantillonnée de 0 à 360° (0 si elle est constante à 2 % près)."""
    h = 2 * np.abs(np.fft.rfft(s[:-1])) / (len(s) - 1)
    if max(h[1], h[2]) < 0.02 * h[0] / 2:
        return 0
    return 360 if h[1] >= h[2] else 180


def txt_periode(p):
    return "aucune (constant)" if p == 0 else f"{p}°"


repli = lambda v: np.abs(v - np.round(v))  # fréquence vue par la grille de pixels (le « miroir » de 0,5 cycle par pixel)


def spectre_local(s, Lw=16, nfft=512):
    w = np.hanning(Lw)
    out = []
    for c0 in range(len(s)):
        seg = np.array([s[j] if 0 <= j < len(s) else 0.0 for j in range(c0 - Lw // 2, c0 - Lw // 2 + Lw)])
        seg = (seg - np.sum(seg * w) / np.sum(w)) * w
        out.append(np.abs(np.fft.rfft(seg, nfft)))
    return np.array(out)


def ecart(S, ref, m=None):
    d = np.abs(S - ref)
    return d.sum() / ref.sum() if m is None else d[m].sum() / ref[m].sum()


FREQ = np.fft.rfftfreq(512)
THETAS = np.radians(np.arange(0, 361, 5))


# ---------------------------------------------------------------------------
# 1. Le spectre local du diaphragme de Fibonacci (mêmes réglages que la partie XI)
# ---------------------------------------------------------------------------
def mot_fibonacci(j):
    S = ["B", "A"]
    for _ in range(2, j + 1):
        S.append(S[-1] + S[-2])
    return S[j]


Q55 = np.array([c == "A" for c in mot_fibonacci(9)], float)
NZ = len(Q55)


def coef(u):
    """Coefficient de Fourier du motif des anneaux, en ζ = (r/a)² (cellules de largeur 1/N)."""
    if u == 0:
        return Q55.mean() + 0j
    k = np.arange(NZ)
    Q = np.sum(Q55 * np.exp(-2j * np.pi * u * k / NZ))
    return Q * (1 - np.exp(-2j * np.pi * u / NZ)) / (2j * np.pi * u)


US = np.arange(1, 601)
C = np.array([coef(u) for u in US])
ORDRE = np.argsort(np.abs(C))[::-1]
AMP = {int(u): abs(c) for u, c in zip(US, C)}
R = 60
II = np.arange(-R, R + 1)
X = II / R
ZE = II * II / R ** 2


def rangee(y0=0.0):
    """La rangée de pixels à la hauteur y0 (en pixels) du diaphragme binaire de rayon R."""
    ze = (II * II + y0 * y0) / R ** 2
    kz = np.floor(NZ * ze).astype(int)
    return np.where(kz < NZ, Q55[np.minimum(kz, NZ - 1)], 0.0)


def reconstruit(K, phases=None, seules=None):
    """Rangée reconstruite avec les K composantes les plus fortes (ou seulement celles de « seules ») ;
    phases = {u: facteur complexe}, 1j fait passer la composante u de cos à sin."""
    r = np.full(len(II), coef(0).real) if seules is None else np.zeros(len(II))
    for t in ORDRE[:K] if seules is None else [int(np.where(US == u)[0][0]) for u in seules]:
        ph = 1.0 if phases is None else phases.get(int(US[t]), 1.0)
        r = r + 2 * np.real(ph * C[t] * np.exp(2j * np.pi * US[t] * ZE))
    return np.where(ZE < 1, r, 0.0)


def valeur(S, x0, f0, xs=X):
    return S[np.argmin(np.abs(xs - x0)), np.argmin(np.abs(FREQ - f0))]


S0 = spectre_local(rangee())
# Les deux zones entourées en rouge sur la capture du panneau d de la partie XI (x/a, cycles par pixel)
ZONES = {"A": [(0.30, 0.20), (0.28, 0.35), (0.32, 0.42), (0.40, 0.40), (0.48, 0.25), (0.70, 0.21), (0.45, 0.15), (0.40, 0.20)],
         "B": [(0.05, 0.0), (0.05, 0.20), (0.32, 0.20), (0.40, 0.17), (0.40, 0.05), (0.43, 0.0)]}
XX, FF = np.meshgrid(X, FREQ, indexing="ij")
MASQUE = {k: Path(p).contains_points(np.c_[XX.ravel(), FF.ravel()]).reshape(XX.shape) for k, p in ZONES.items()}

ligne("## 1. Les branchages entourés en rouge\n")
ligne(f"Zone A (en haut) : {MASQUE['A'].sum()} cases du spectre ; zone B (en bas) : {MASQUE['B'].sum()} cases.\n")
ligne("Ressemblance (corrélation) entre le spectre mesuré et celui de la rangée reconstruite avec K composantes :\n")
ligne("| K | composantes ajoutées | zone A | zone B | tout le spectre |")
ligne("|---:|---|---|---|---|")
CORR = {}
prec = 0
for K in (2, 3, 5, 8, 12, 16, 24, 40, 200):
    SK = spectre_local(reconstruit(K))
    CORR[K] = [np.corrcoef(S0[MASQUE[z]], SK[MASQUE[z]])[0, 1] for z in "AB"] + [np.corrcoef(S0.ravel(), SK.ravel())[0, 1]]
    ajout = ", ".join(str(int(US[t])) for t in ORDRE[prec:K]) if K <= 16 else "…"
    ligne(f"| {K} | {ajout} | {fr(CORR[K][0], '{:.3f}')} | {fr(CORR[K][1], '{:.3f}')} | {fr(CORR[K][2], '{:.3f}')} |")
    prec = K
S12 = spectre_local(reconstruit(12))

# Les nœuds : croisements des aiguilles repliées des 12 premières composantes.
# Une aiguille au-delà de 0,5 cycle par pixel est vue dans le miroir : c'est la moitié e^{−iθ} du cos.
TOP = [int(US[t]) for t in ORDRE[:12]]
xs = np.linspace(0, 1, 40001)
NOEUDS = []
for i_, u in enumerate(TOP):
    for v in TOP[i_ + 1:]:
        d = repli(2 * u * xs / R) - repli(2 * v * xs / R)
        for j in np.where(np.sign(d[:-1]) * np.sign(d[1:]) < 0)[0]:
            x0 = xs[j] - d[j] * (xs[j + 1] - xs[j]) / (d[j + 1] - d[j])
            su, sv = (np.sign(2 * w * x0 / R - np.round(2 * w * x0 / R)) for w in (u, v))
            w = u + v if su != sv else abs(u - v)
            NOEUDS.append(dict(x=x0, f=repli(2 * u * x0 / R), u=u, v=v, type="miroir" if su != sv else "direct", w=w,
                               ordre=2 * w * x0 / R, poids=AMP[u] * AMP[v]))
err = max(abs(n_["ordre"] - round(n_["ordre"])) for n_ in NOEUDS)
ligne(f"\n{len(NOEUDS)} nœuds (croisements) entre les aiguilles repliées des 12 premières composantes, pour 0 ≤ x/a ≤ 1.")
ligne("Nœud miroir : une des deux aiguilles est vue dans le miroir du repliement (au-delà de 0,5 cycle par pixel) ; il bat"
      " à la fréquence u + v. Nœud direct : les deux du même côté ; il bat à |u − v|.")
ligne("Chaque nœud est sur un centre fantôme de la fréquence de battement (u + v ou |u − v|) : 2(u ± v)·x/R y est un entier"
      f" (écart max {err:.1e}).")
ligne("Le premier nœud miroir de u et v est en x/a = R/(2(u+v)), à la fréquence f = u/(u+v) cycle par pixel.\n")
ligne("| paire | x/a du nœud | f = u/(u+v) | en degrés par pixel (360·f) |")
ligne("|---|---|---|---|")
for u, v in ((13, 21), (21, 34), (34, 89), (21, 89)):
    ligne(f"| {u} et {v} | {fr(R / (2 * (u + v)))} | {u}/{u + v} = {fr(u / (u + v), '{:.5f}')} | {fr(360 * u / (u + v), '{:.3f}')}° |")
ligne("\n21/55 de tour = 137,45° et 34/55 = 222,55° : au nœud de 21 et 34, la composante 21 avance d'une approximation de"
      " Fibonacci de l'angle d'or par pixel, et la 34 de son complément (parties XI et XII).\n")
for z in "AB":
    dedans = [n_ for n_ in NOEUDS if Path(ZONES[z]).contains_point((n_["x"], n_["f"]))]
    nm = sum(n_["type"] == "miroir" for n_ in dedans)
    forts = sorted(dedans, key=lambda n_: -n_["poids"])[:6]
    ligne(f"- zone {z} : {len(dedans)} nœuds ({nm} miroirs, {len(dedans) - nm} directs) ; les plus forts : "
          + " ; ".join(f"{n_['u']} × {n_['v']} ({n_['type']}, battement {n_['w']})" for n_ in forts))
    for n_ in dedans:
        n_["zone"] = z

# ---------------------------------------------------------------------------
# 2. Le déphasage de 90° sur la lame de zones
# ---------------------------------------------------------------------------
ligne("\n## 2. Le déphasage de 90° (cos → sin) sur la lame de zones\n")
K = 40
REF = spectre_local(reconstruit(K))
FAMILLES = [("21 et 34", {21, 34}), ("13 et 8", {13, 8}), ("26 et 29", {26, 29}), ("répliques 76, 89, 131, 144", {76, 89, 131, 144}),
            ("toutes sauf 21 et 34", "sauf"), ("toutes (déphasage commun)", "toutes")]
ligne("Chaque composante choisie passe de cos à sin ; écart relatif du spectre local (K = 40 composantes) :\n")
ligne("| composantes décalées de 90° | tout le spectre | zone A | zone B |")
ligne("|---|---|---|---|")
DEPH = {}
for nom, fam in FAMILLES:
    if fam == "sauf":
        ph = {int(US[t]): 1j for t in ORDRE[:K] if int(US[t]) not in (21, 34)}
    elif fam == "toutes":
        ph = {int(US[t]): 1j for t in ORDRE[:K]}
    else:
        ph = {u: 1j for u in fam}
    S = spectre_local(reconstruit(K, ph))
    DEPH[nom] = (ecart(S, REF), ecart(S, REF, MASQUE["A"]), ecart(S, REF, MASQUE["B"]), S)
    ligne(f"| {nom} | {fr(DEPH[nom][0], '{:.3f}')} | {fr(DEPH[nom][1], '{:.3f}')} | {fr(DEPH[nom][2], '{:.3f}')} |")
S180 = spectre_local(reconstruit(K, {int(US[t]): -1 for t in ORDRE[:K]}))
ligne(f"\nDéphasage commun de 180° (tout change de signe) : écart {fr(ecart(S180, REF), '{:.3f}')}.")

ligne("\n### La loi du nœud\n")
ligne("Deux composantes seules ; on ajoute la phase θ à la seconde (relatif), ou aux deux (commun), et on lit le spectre"
      " au nœud. a et b : le spectre au nœud avec chaque composante seule.\n")
ligne("| nœud | type | a | b | relatif : min → max | \\|a − b\\| et a + b | période | commun : min → max | période |")
ligne("|---|---|---|---|---|---|---|---|---|")
LOI = {}
for u, v, genre in ((21, 34, "miroir"), (13, 76, "direct")):
    nd = [n_ for n_ in NOEUDS if {n_["u"], n_["v"]} == {u, v} and n_["type"] == genre][0]
    a = valeur(spectre_local(reconstruit(0, seules=(u,))), nd["x"], nd["f"])
    b = valeur(spectre_local(reconstruit(0, seules=(v,))), nd["x"], nd["f"])
    rel = np.array([valeur(spectre_local(reconstruit(0, {v: np.exp(1j * t)}, seules=(u, v))), nd["x"], nd["f"]) for t in THETAS])
    com = np.array([valeur(spectre_local(reconstruit(0, {u: np.exp(1j * t), v: np.exp(1j * t)}, seules=(u, v))), nd["x"], nd["f"])
                    for t in THETAS])
    th0 = THETAS[np.argmax(com)]  # phase commune de départ où le nœud est le plus clair
    Sx = [spectre_local(reconstruit(0, {u: np.exp(1j * t), v: np.exp(1j * t)}, seules=(u, v))) for t in (th0, th0 + np.pi / 2)]
    LOI[(u, v)] = (nd, rel, com, Sx[0], Sx[1], th0)
    ligne(f"| {u} × {v} en x/a = {fr(nd['x'], '{:.3f}')}, f = {fr(nd['f'], '{:.3f}')} | {genre} (battement {nd['w']}) |"
          f" {fr(a, '{:.2f}')} | {fr(b, '{:.2f}')} | {fr(rel.min(), '{:.2f}')} → {fr(rel.max(), '{:.2f}')} |"
          f" {fr(abs(a - b), '{:.2f}')} et {fr(a + b, '{:.2f}')} | {txt_periode(periode(rel))} |"
          f" {fr(com.min(), '{:.2f}')} → {fr(com.max(), '{:.2f}')} | {txt_periode(periode(com))} |")
nd = LOI[(21, 34)][0]
v_cos, v_sin = (valeur(spectre_local(reconstruit(0, ph, seules=(21, 34))), nd["x"], nd["f"]) for ph in (None, {21: 1j, 34: 1j}))
ligne(f"- 21 × 34 avec les phases de la lame : passer les deux en sin fait passer le nœud de {fr(v_cos, '{:.2f}')} à"
      f" {fr(v_sin, '{:.2f}')} seulement, car il part presque en quadrature (à mi-chemin entre fort et faible).")
for (u, v), (nd, _, _, Sa_, Sb_, th0) in LOI.items():
    ligne(f"- {u} × {v} ({nd['type']}) : en partant de la phase commune {np.degrees(th0):.0f}° (nœud au plus clair), ajouter 90°"
          f" à tout fait passer le nœud de {fr(valeur(Sa_, nd['x'], nd['f']), '{:.2f}')} à {fr(valeur(Sb_, nd['x'], nd['f']), '{:.2f}')}.")
ligne("\nLe nœud suit la loi des interférences : il va de |a − b| (opposition) à a + b (en phase) quand le déphasage"
      " relatif fait un tour. Un cos réel est la somme de deux rotations de sens contraires, cos θ = (e^{iθ} + e^{−iθ})/2, et"
      " l'aiguille vue dans le miroir est la moitié e^{−iθ}. Un déphasage commun de 90° tourne donc les deux aiguilles d'un"
      " nœud miroir de +90° et de −90° : leur déphasage relatif change de 180°, et le nœud passe à l'état opposé (clair ↔"
      " sombre ; un nœud à mi-chemin, en quadrature, reste à mi-chemin). Sur un nœud direct, le même déphasage commun ne"
      " change rien.")

ligne("\n### D'une rangée de pixels à l'autre\n")
ligne("À la hauteur y0, la composante u prend la phase 2πu·y0²/R² : un nœud de u et v se décale de 2π(u ± v)·y0²/R².\n")
ligne("| y0 (pixels) | décalage du nœud miroir 21 × 34 (battement 55) | écart du spectre (tout) | zone A | zone B |")
ligne("|---:|---|---|---|---|")
for y0 in (0, 2, 4, 6, 8, 12):
    Sy = spectre_local(rangee(y0))
    ligne(f"| {y0} | {fr(np.degrees(2 * np.pi * 55 * y0 ** 2 / R ** 2) % 360, '{:.1f}')}° | {fr(ecart(Sy, S0), '{:.3f}')} |"
          f" {fr(ecart(Sy, S0, MASQUE['A']), '{:.3f}')} | {fr(ecart(Sy, S0, MASQUE['B']), '{:.3f}')} |")
ligne(f"\nLe nœud 21 × 34 tourne de 90° dès y0 = R/(2√55) = {fr(R / (2 * 55 ** 0.5), '{:.2f}')} pixels : dans l'image elle-même,"
      " le passage de cos à sin se fait tout seul d'une rangée à l'autre.")

# ---------------------------------------------------------------------------
# 3. L'arbre de Perron tourné de 90°
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
    return l, r, axs_


PL, PR, PA = arbre(3, [4 / 5, 3 / 4, 2 / 3])
LO, HI = min(min(PL), min(PA)), max(max(PR), max(PA))
LP, LWP = 241, 48
NP_ = np.arange(LP)
XP = NP_ / (LP - 1)
BANDES_P = {"sous 0,5 (de 0,02 à 0,48)": (0.02, 0.48), "centré sur 0,5 (de 0,27 à 0,73) : une moitié dans le miroir": (0.27, 0.73)}


def aiguilles(f_lo, f_hi):
    """Tourner de 90° : la base du triangle devient l'axe des fréquences, la hauteur devient la position.
    Chaque branche donne 3 aiguilles (ses deux bords et sa médiane), de la base (x = 0) au sommet (x = 1)."""
    fq = lambda v: f_lo + (f_hi - f_lo) * (v - LO) / (HI - LO)
    return [[(fq(b), fq(PA[i])) for b in (PL[i], (PL[i] + PR[i]) / 2, PR[i])] for i in range(len(PL))]


def signal_perron(ag, dephasage, seules=None, L=LP):
    """Chaque aiguille devient une fréquence qui glisse (« chirp »). Phase de départ à pas d'angle d'or (2π·k/φ²), pour
    qu'elles ne s'alignent jamais toutes ; dephasage[i] s'ajoute à toutes les aiguilles de la branche i."""
    n = np.arange(L)
    s = np.zeros(L)
    k = 0
    for i, tri in enumerate(ag):
        for j, (fb, f1) in enumerate(tri):
            if seules is None or (i, j) in seules:
                s += np.cos(2 * np.pi * (fb * n + (f1 - fb) * n * n / (2 * (L - 1)) + k / PHI ** 2) + dephasage[i])
            k += 1
    return s


def noeuds_perron(ag):
    """Croisements (repliés) d'aiguilles de branches différentes, avec leur type (miroir ou direct)."""
    liste = [(i, j, fb, f1) for i, tri in enumerate(ag) for j, (fb, f1) in enumerate(tri)]
    xx_ = np.linspace(0.1, 0.9, 8001)
    out = []
    for p in range(len(liste)):
        for q in range(p + 1, len(liste)):
            (i1, j1, b1, s1), (i2, j2, b2, s2) = liste[p], liste[q]
            if i1 == i2:
                continue
            f1_, f2_ = b1 + (s1 - b1) * xx_, b2 + (s2 - b2) * xx_
            d = repli(f1_) - repli(f2_)
            for k in np.where(np.sign(d[:-1]) * np.sign(d[1:]) < 0)[0]:
                miroir = np.sign(f1_[k] - np.round(f1_[k])) != np.sign(f2_[k] - np.round(f2_[k]))
                pente = abs((s1 - b1) + (s2 - b2)) if miroir else abs((s1 - b1) - (s2 - b2))
                out.append(dict(x=xx_[k], f=repli(f1_[k]), a=(i1, j1), b=(i2, j2), type="miroir" if miroir else "direct",
                                pente=pente))
    return out


ligne("\n## 3. L'arbre de Perron tourné de 90°\n")
ligne("Arbre à 8 branches de la partie X (α = 4/5, 3/4, 2/3). Chaque branche donne 3 aiguilles (ses deux bords et sa"
      " médiane). Tourné de 90°, la base devient l'axe des fréquences et la hauteur l'axe des positions : chaque aiguille"
      f" devient une fréquence qui glisse de la base (x = 0) au sommet (x = 1). {LP} points, fenêtre de {LWP} points.\n")
ligne("| arbre tourné | branches alternées cos / sin | déphasage commun de 90° | déphasage commun de 180° |")
ligne("|---|---|---|---|")
PERRON = {}
for nom, (f_lo, f_hi) in BANDES_P.items():
    ag = aiguilles(f_lo, f_hi)
    Sc = spectre_local(signal_perron(ag, np.zeros(8)), Lw=LWP)
    Sa = spectre_local(signal_perron(ag, np.array([0, np.pi / 2] * 4)), Lw=LWP)
    Ss = spectre_local(signal_perron(ag, np.full(8, np.pi / 2)), Lw=LWP)
    Sm = spectre_local(signal_perron(ag, np.full(8, np.pi)), Lw=LWP)
    PERRON[nom] = dict(ag=ag, cos=Sc, e_alt=ecart(Sa, Sc), e_com=ecart(Ss, Sc), e_180=ecart(Sm, Sc))
    ligne(f"| {nom} | {fr(PERRON[nom]['e_alt'], '{:.3f}')} | {fr(PERRON[nom]['e_com'], '{:.3f}')} | {fr(PERRON[nom]['e_180'], '{:.3f}')} |")
P_BAS, P_MIR = (PERRON[k] for k in BANDES_P)
ligne("\nTant que l'arbre reste sous 0,5 cycle par pixel, aucune aiguille n'est vue dans le miroir : le spectre ne voit que"
      " les déphasages relatifs, et le déphasage commun ne change presque rien. Centré sur 0,5, la moitié de l'arbre passe"
      " dans le miroir, des nœuds miroirs apparaissent, et le déphasage commun change le spectre, comme dans la lame.")
ligne(f"Lame de zones, pour comparer : déphasage relatif {fr(DEPH['toutes sauf 21 et 34'][0], '{:.3f}')},"
      f" commun {fr(DEPH['toutes (déphasage commun)'][0], '{:.3f}')}.")
ligne("\nLa loi du nœud dans l'arbre centré sur 0,5 (deux aiguilles seules de deux branches différentes) :\n")
ligne("| nœud | type | relatif : min → max | période | commun : min → max | période |")
ligne("|---|---|---|---|---|---|")
LOI_P = {}
ag = P_MIR["ag"]
PRIS = []
for genre in ("miroir", "direct"):
    cands = [n_ for n_ in noeuds_perron(ag) if n_["type"] == genre and 0.06 < n_["f"] < 0.44 and n_["pente"] > 0.08
             and all(abs(n_["x"] - p_["x"]) + abs(n_["f"] - p_["f"]) > 0.08 for p_ in PRIS)]
    nd = min(cands, key=lambda n_: abs(n_["x"] - 0.5))
    PRIS.append(nd)
    seules = {nd["a"], nd["b"]}
    (i1, _), (i2, _) = nd["a"], nd["b"]

    def lire(th1, th2):
        dph = np.zeros(8)
        dph[i1] += th1
        dph[i2] += th2
        return valeur(spectre_local(signal_perron(ag, dph, seules), Lw=LWP), nd["x"], nd["f"], XP)

    rel = np.array([lire(0, t) for t in THETAS])
    com = np.array([lire(t, t) for t in THETAS])
    LOI_P[genre] = (nd, rel, com)
    ligne(f"| branches {i1 + 1} × {i2 + 1} en x = {fr(nd['x'], '{:.3f}')}, f = {fr(nd['f'], '{:.3f}')} | {genre} |"
          f" {fr(rel.min(), '{:.2f}')} → {fr(rel.max(), '{:.2f}')} | {txt_periode(periode(rel))} |"
          f" {fr(com.min(), '{:.2f}')} → {fr(com.max(), '{:.2f}')} | {txt_periode(periode(com))} |")
ligne("\nMême loi que dans la lame : un tour pour le déphasage relatif ; un demi-tour pour le déphasage commun sur un nœud"
      " miroir ; rien sur un nœud direct.")

# ---------------------------------------------------------------------------
# 4. Tourner de 90°, c'est la transformée de Fourier
# ---------------------------------------------------------------------------
L4 = 256
n4 = np.arange(L4)
g4 = sum(np.exp(-np.pi * (n4 - L4 // 2 + k * L4) ** 2 / L4) for k in range(-3, 4))  # gaussienne qui est sa propre TF
inv = np.abs(np.fft.fftshift(np.abs(np.fft.fft(np.fft.ifftshift(g4))) / np.sqrt(L4)) - g4).max()


def stft_complet(s):
    return np.array([np.abs(np.fft.fft(s * np.roll(g4, m - L4 // 2))) for m in range(L4)])


s4 = signal_perron(P_BAS["ag"], np.zeros(8), L=L4)
A4 = stft_complet(s4)
B4 = stft_complet(np.fft.fft(s4) / np.sqrt(L4))
TOURNE = np.array([[A4[(-k) % L4, m] for k in range(L4)] for m in range(L4)])
dev_rot = np.abs(B4 - TOURNE).max() / A4.max()
dev_inv = np.abs(np.fft.fft(np.fft.fft(s4)) / L4 - s4[(-n4) % L4]).max()
ligne("\n## 4. Tourner de 90° le plan position–fréquence, c'est la transformée de Fourier\n")
ligne(f"Fenêtre gaussienne de variance L/(2π) (L = {L4}), qui est sa propre transformée de Fourier (écart {inv:.1e}).")
ligne(f"Spectre local de la transformée de Fourier de l'arbre tourné, comparé au spectre local tourné de 90° : écart max"
      f" {dev_rot:.1e} (relatif). Deux transformées de suite (180°) : s(n) → s(−n), l'image retournée (écart {dev_inv:.1e}).")


# ---------------------------------------------------------------------------
# 5. La bande 2,44–2,56
# ---------------------------------------------------------------------------
def part(n, r):
    """Part de la boule unité de dimension réelle n broutée avec la corde r (bêta incomplète régularisée)."""
    c1 = 1 - r * r / 2
    I1 = betainc((n + 1) / 2, 0.5, 1 - c1 * c1)
    if c1 < 0:
        I1 = 2 - I1
    return (I1 + r ** n * betainc((n + 1) / 2, 0.5, 1 - r * r / 4)) / 2


def corde(n):
    return brentq(lambda r: part(n, r) - 0.5, 1.0, 2 ** 0.5, xtol=1e-15)


def corde_mp(n):
    mp.mp.dps = 30
    n = mp.mpf(n)

    def p(r):
        c1 = 1 - r * r / 2
        I1 = mp.betainc((n + 1) / 2, mp.mpf(1) / 2, 0, 1 - c1 * c1, regularized=True)
        return (I1 + r ** n * mp.betainc((n + 1) / 2, mp.mpf(1) / 2, 0, 1 - r * r / 4, regularized=True)) / 2

    return mp.findroot(lambda r: p(r) - mp.mpf(1) / 2, 1.2)


ctrl = max(abs(float(corde_mp(n)) - corde(float(n))) for n in ("2", "2.5", "3"))
NN = np.round(np.arange(1.10, 4.5001, 0.0025), 5)
RR = np.array([corde(n) for n in NN])
SS = np.sqrt(2 * NN / (NN + 1))
VV = np.pi ** (NN / 2) / gamma(NN / 2 + 1)
RN = RR ** NN
GRANDEURS = {"corde r": RR, "r²": RR ** 2, "rⁿ (boule de la corde, en boules unité)": RN, "corde du simplexe s": SS,
             "écart r − s": RR - SS, "volume de la boule V(n)": VV, "aire de la sphère n·V(n)": NN * VV,
             "hémisphère / cylindre h(n)": np.sqrt(np.pi) / 2 * gamma((NN + 1) / 2) / gamma(NN / 2 + 1)}
ANGLES = {"angle au piquet α (°)": np.degrees(np.arccos(RR / 2)), "arc de la corde γ (°)": 2 * np.degrees(np.arcsin(RR / 2))}

FIB = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
LUC = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199]
fam_fib = {"φ": PHI, "1/φ": 1 / PHI, "φ²": PHI ** 2, "1/φ²": PHI ** -2, "φ³": PHI ** 3, "1/φ³": PHI ** -3, "√φ": PHI ** 0.5,
           "1/√φ": PHI ** -0.5, "φ/2": PHI / 2, "2/φ": 2 / PHI, "2 sin 36°": 2 * np.sin(np.pi / 5), "3 − φ": 3 - PHI}
for k in range(1, 12):
    for a, b in ((FIB[k + 1], FIB[k]), (FIB[k], FIB[k + 1]), (FIB[k + 2], FIB[k]), (FIB[k], FIB[k + 2])):
        fam_fib.setdefault(f"{a}/{b}", a / b)
for v in sorted(set(FIB + LUC)):
    fam_fib.setdefault(str(v), float(v))
ang_fib = {f"360°/φ^{k}": 360 / PHI ** k for k in range(1, 7)}
ang_fib.update({"137,5°": 137.5, "222,5°": 222.5, "36°": 36.0, "54°": 54.0, "72°": 72.0, "108°": 108.0, "144°": 144.0})
fam_bases = {}
for B, pmax in ((2, 6), (10, 2), (12, 2), (60, 1)):
    for p in range(-3, pmax + 1):
        fam_bases.setdefault(f"{B}^{p}", float(B) ** p)
for q in (2, 4, 8, 16, 10, 12, 60):
    for p_ in range(1, 40 * q):
        v = Fraction(p_, q)
        if v.denominator > 1 and 0.01 <= v <= 40:
            fam_bases.setdefault(f"{v.numerator}/{v.denominator}", float(v))
ang_bases = {}
for N_ in (12, 24, 60, 144, 270, 720):
    for m in range(1, N_):
        a = Fraction(360 * m, N_)
        ang_bases.setdefault(f"{float(a):g}°".replace(".", ","), float(a))
fam_autres = {"√2": 2 ** 0.5, "√3": 3 ** 0.5, "√5": 5 ** 0.5, "2/√3": 2 / 3 ** 0.5, "1/√3": 3 ** -0.5, "1/√2": 0.5 ** 0.5,
              "π": np.pi, "π/2": np.pi / 2, "π/3": np.pi / 3, "π/4": np.pi / 4, "π/6": np.pi / 6, "π − 3": np.pi - 3, "e": np.e,
              "ρ (nombre plastique)": 1.324717957244746, "2,5 = 5²×10⁻¹": 2.5, "1/4 = 5²×10⁻²": 0.25, "1/11": 1 / 11,
              "0,6416 (FTO défocalisée)": 0.6416}
ang_autres = {"109,47° (tétraèdre)": np.degrees(np.arccos(-1 / 3)), "70,53°": np.degrees(np.arccos(1 / 3)),
              "54,74° (angle magique)": np.degrees(np.arccos(3 ** -0.5)), "35,26°": np.degrees(np.arcsin(3 ** -0.5))}
FAMILLES_C = {"Fibonacci, Lucas et φ": (fam_fib, ang_fib), "bases 2, 10, 12 et 60": (fam_bases, ang_bases),
              "constantes déjà rencontrées": (fam_autres, ang_autres)}


def croisements(courbe, cible):
    d = courbe - cible
    j = np.where(np.sign(d[:-1]) * np.sign(d[1:]) < 0)[0]
    return NN[j] + (NN[j + 1] - NN[j]) * d[j] / (d[j] - d[j + 1])


def simple(nom):
    """Fractions à un seul chiffre en base 10 ou 12, ou à 3 chiffres binaires au plus (dénominateur 8 au plus, ou 10, 12)."""
    if "/" in nom and nom.split("/")[1].isdigit():
        return int(nom.split("/")[1]) in (2, 3, 4, 5, 6, 8, 10, 12)
    return True


COUPS = {f: [] for f in FAMILLES_C}
for fam, (nombres, angles) in FAMILLES_C.items():
    for qn, qv in GRANDEURS.items():
        for cn, cv in nombres.items():
            COUPS[fam] += [(n_, qn, cn) for n_ in croisements(qv, cv)]
    for qn, qv in ANGLES.items():
        for cn, cv in angles.items():
            COUPS[fam] += [(n_, qn, cn) for n_ in croisements(qv, cv)]
BANDE = (2.44, 2.56)
CENTRES = np.arange(1.26, 4.3401, 0.01)
ligne("\n## 5. La bande 2,44–2,56\n")
ligne(f"Corde calculée par la fonction bêta incomplète (contrôle à 30 chiffres en n = 2 ; 2,5 ; 3 : écart {ctrl:.0e}).\n")
ligne("| grandeur | n = 2,44 | n = 2,50 | n = 2,56 |")
ligne("|---|---|---|---|")
for qn, qv in {**GRANDEURS, **ANGLES}.items():
    ligne(f"| {qn} | " + " | ".join(fr(np.interp(n, NN, qv), '{:.6f}') for n in (2.44, 2.50, 2.56)) + " |")
ligne("\nCroisements exacts dans la bande (la grandeur passe par la valeur exacte) :\n")
CONTROLE = {}
for fam, cps in COUPS.items():
    ns = np.array([c[0] for c in cps])
    dans = sorted(c for c in cps if BANDE[0] <= c[0] <= BANDE[1])
    comptes = np.array([((ns >= c - 0.06) & (ns <= c + 0.06)).sum() for c in CENTRES])
    CONTROLE[fam] = (len(dans), comptes)
    montres = [c for c in dans if fam != "bases 2, 10, 12 et 60" or simple(c[2])]
    reste = len(dans) - len(montres)
    ligne(f"- **{fam}** ({len(dans)}) : " + ("aucun" if not dans else " ; ".join(f"{c[1]} = {c[2]} en n = {fr(c[0])}" for c in montres))
          + (f" ; et {reste} fractions de dénominateur 15, 16, 20, 30 ou 60 (surtout l'aire n·V(n), qui varie vite)" if reste else ""))
n65 = brentq(lambda n: corde(n) - 1.2, 2.4, 2.6, xtol=1e-13)
ligne(f"\nLa corde vaut 6/5 en n = {fr(n65, '{:.5f}')} : alors cos α = r/2 = 3/5 et sin α = 4/5, le triangle piquet–centre–bord"
      " se coupe en deux triangles 3-4-5 (α = 53,13°).")
ligne("\nContrôle : le même compte pour toutes les bandes de largeur 0,12 entre 1,2 et 4,4 :\n")
ligne("| famille | dans 2,44–2,56 | moyenne des bandes | écart-type | bandes plus pauvres | à égalité | plus riches |")
ligne("|---|---|---|---|---|---|---|")
for fam, (k_, comptes) in CONTROLE.items():
    ligne(f"| {fam} | {k_} | {fr(comptes.mean(), '{:.1f}')} | {fr(comptes.std(), '{:.1f}')} | {fr(100 * np.mean(comptes < k_), '{:.0f}')} % |"
          f" {fr(100 * np.mean(comptes == k_), '{:.0f}')} % | {fr(100 * np.mean(comptes > k_), '{:.0f}')} % |")

LIGNE_FIB = []
for k in range(2, 13):
    c = FIB[k + 1] / FIB[k]
    LIGNE_FIB.append((FIB[k + 1], FIB[k], brentq(lambda n: corde(n) ** n - c, 1.5, 4.0, xtol=1e-13)))
N_ETOILE = brentq(lambda n: corde(n) ** n - PHI, 2.0, 3.5, xtol=1e-13)
N_PI2 = brentq(lambda n: corde(n) ** n - np.pi / 2, 2.3, 2.6, xtol=1e-13)
ligne("\n### La ligne de Fibonacci de rⁿ\n")
ligne("| rⁿ = | dimension n |")
ligne("|---|---|")
for a, b, n_ in LIGNE_FIB:
    ligne(f"| {a}/{b} = {fr(a / b, '{:.6f}')} | {fr(n_, '{:.6f}')} |")
ligne(f"| φ = {fr(PHI, '{:.6f}')} | {fr(N_ETOILE, '{:.6f}')} |")
ligne(f"\nLes dimensions convergent vers n* = {fr(N_ETOILE, '{:.5f}')} en alternant, comme les fractions vers φ."
      f" Seule 8/5 (n = {fr(LIGNE_FIB[2][2])}) tombe dans la bande ; la limite est {fr(N_ETOILE - 2.56, '{:.3f}')} au-dessus.")
ligne(f"rⁿ vaut r² = {fr(corde(2.0) ** 2)} en 2D et r³ = {fr(corde(3.0) ** 3)} en 3D, et croît avec n : comme φ = 1,6180"
      " est entre les deux, la limite tombe forcément entre 2D et 3D.")
LIMITES = []
for qn, qv in GRANDEURS.items():
    for cn in ("φ", "1/φ", "φ²", "1/φ²", "φ³", "√φ", "1/√φ", "φ/2", "2/φ"):
        LIMITES += [(n_, qn, cn) for n_ in croisements(qv, fam_fib[cn]) if 1.2 <= n_ <= 4.4]
for qn, qv in ANGLES.items():
    for k in range(1, 7):
        LIMITES += [(n_, qn, f"360°/φ^{k}") for n_ in croisements(qv, 360 / PHI ** k) if 1.2 <= n_ <= 4.4]
LIMITES.sort()
nl = np.array([x[0] for x in LIMITES])
ligne(f"\nToutes les limites de ce genre (une grandeur égale à une puissance de φ) entre 1,2 et 4,4 : {len(LIMITES)}, dont"
      f" {((nl >= BANDE[0]) & (nl <= BANDE[1])).sum()} dans la bande (on en attendrait {fr(len(LIMITES) * 0.12 / 3.2, '{:.2f}')}"
      " si elles étaient réparties au hasard) :")
ligne("; ".join(f"{fr(n_, '{:.3f}')} ({q} = {c})" for n_, q, c in LIMITES))

with open(os.path.join(ICI, "..", "resultats", "perron_dephasage.md"), "w") as fh:
    fh.write("# Résultats de la partie XIII (générés par scripts/perron_dephasage.py)\n\n" + "\n".join(md) + "\n")

# ===========================================================================
# Figure
# ===========================================================================
fig = plt.figure(figsize=(20, 13.5))
gs = fig.add_gridspec(2, 3, wspace=0.2, hspace=0.3)
FOND = dict(fc=F.SURF, ec="none", alpha=0.92, pad=2.5)


def spectre(ax, S, cmap="Greys"):
    ax.imshow(S.T, origin="lower", aspect="auto", extent=(X[0] - 0.5 / R, X[-1] + 0.5 / R, 0, 0.5), cmap=cmap,
              vmax=np.percentile(S, 99.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.5)
    ax.grid(False)


def zones(ax):
    for z, p in ZONES.items():
        ax.add_patch(Polygon(p, closed=True, fill=False, ec=ROUGE, lw=2.2, zorder=6))
        ax.text(*{"A": (0.265, 0.405), "B": (0.035, 0.185)}[z], z, color=ROUGE, fontsize=12, fontweight="bold", ha="right", zorder=7)


def marque_noeuds(ax, plein=True):
    for n_ in NOEUDS:
        if "zone" in n_:
            ax.plot(n_["x"], n_["f"], "o" if n_["type"] == "miroir" else "^", ms=4.5 if plein else 4,
                    mfc=F.JAUNE if plein else "none", mec=F.INK, mew=0.6 if plein else 0.7, zorder=8)


xx = np.linspace(0, 1, 801)

# a) les nœuds dans les zones rouges
ax = fig.add_subplot(gs[0, 0])
spectre(ax, S0)
for u in TOP:
    coul = F.ORANGE if u in (21, 34) else (F.BLEU if u in (13, 76, 89, 131, 144) else F.AQUA)
    ax.plot(xx, repli(2 * u * xx / R), color=coul, lw=0.8, alpha=0.55)
zones(ax)
marque_noeuds(ax)
ax.set_xlabel("position sur l'axe (x/a), R = 60 px")
ax.set_ylabel("fréquence des franges vues (cycles par pixel)")
ax.legend(handles=[Line2D([], [], color=F.ORANGE, lw=1.2, label="21, 34"), Line2D([], [], color=F.BLEU, lw=1.2, label="13, 76, 89, 131, 144"),
                   Line2D([], [], color=F.AQUA, lw=1.2, label="26, 29, 8, 16, 18"),
                   Line2D([], [], marker="o", ls="", mfc=F.JAUNE, mec=F.INK, label="nœud miroir (une aiguille repliée)"),
                   Line2D([], [], marker="^", ls="", mfc=F.JAUNE, mec=F.INK, label="nœud direct")],
          fontsize=8, loc="upper right", frameon=True, facecolor=F.SURF, edgecolor="none", framealpha=0.92)
ax.set_title("a)  Tes zones rouges : des nœuds d'aiguilles")

# b) reconstruction à 12 composantes
ax = fig.add_subplot(gs[0, 1])
spectre(ax, S12)
zones(ax)
ax.set_xlabel("position sur l'axe (x/a)")
ax.set_yticklabels([])
ax.text(0.985, 0.985, f"12 composantes :\nzone A {CORR[12][0]:.2f}, zone B {CORR[12][1]:.2f}\n(2 composantes : {CORR[2][0]:.2f} et {CORR[2][1]:.2f})"
        .replace(".", ","), transform=ax.transAxes, ha="right", va="top", fontsize=9, bbox=FOND)
axi = ax.inset_axes([0.6, 0.07, 0.37, 0.3])
Ks = sorted(CORR)
axi.semilogx(Ks, [CORR[k][0] for k in Ks], "o-", color=ROUGE, ms=3, lw=1, label="zone A")
axi.semilogx(Ks, [CORR[k][1] for k in Ks], "s-", color=F.INK2, ms=3, lw=1, label="zone B")
axi.set_ylim(0.3, 1.0)
axi.set_xlabel("K composantes", fontsize=7.5, labelpad=1)
axi.set_ylabel("ressemblance", fontsize=7.5, labelpad=1)
axi.tick_params(labelsize=7)
axi.legend(fontsize=7, loc="lower right", frameon=True, facecolor=F.SURF, edgecolor="none")
axi.set_facecolor(F.SURF)
ax.set_title("b)  Les branchages reviennent avec 12 composantes")

# c) cos -> sin sur deux nœuds de la lame
axc = fig.add_subplot(gs[0, 2])
axc.axis("off")
axc.set_title("c)  Tout passer en sin : le nœud miroir s'inverse")
for row, (u, v) in enumerate(((21, 34), (13, 76))):
    nd, rel, com, Sc_, Ss_, th0 = LOI[(u, v)]
    vmax = max(Sc_.max(), Ss_.max())
    for col, (Sx, nom) in enumerate(((Sc_, f"θ₀ = {np.degrees(th0):.0f}°"), (Ss_, "θ₀ + 90° partout"))):
        ax = axc.inset_axes([0.0 + 0.53 * col, 0.56 - 0.54 * row, 0.47, 0.37])
        ax.imshow(Sx.T, origin="lower", aspect="auto", extent=(X[0] - 0.5 / R, X[-1] + 0.5 / R, 0, 0.5), cmap="Greys", vmax=vmax)
        ax.plot(nd["x"], nd["f"], "o", ms=17, mfc="none", mec=ROUGE, mew=1.6)
        ax.set_xlim(nd["x"] - 0.3, nd["x"] + 0.3)
        ax.set_ylim(max(nd["f"] - 0.2, 0), min(nd["f"] + 0.2, 0.5))
        ax.grid(False)
        ax.tick_params(labelsize=7.5)
        if col:
            ax.set_yticklabels([])
        ax.set_title((f"{u} + {v} ({nd['type']}), " if col == 0 else "") + nom, fontsize=9, fontweight="normal", loc="left")
        if row == 1:
            ax.set_xlabel("position (x/a)", fontsize=8.5)
        ax.text(0.03, 0.04, f"nœud : {valeur(Sx, nd['x'], nd['f']):.2f}".replace(".", ","), transform=ax.transAxes, fontsize=8,
                bbox=FOND)

# d) Perron tourné de 90°, sous 0,5 puis centré sur 0,5
sub = gs[1, 0].subgridspec(2, 1, hspace=0.12)
for row, P in enumerate((P_BAS, P_MIR)):
    ax = fig.add_subplot(sub[row, 0])
    ax.imshow(P["cos"].T, origin="lower", aspect="auto", extent=(0, 1, 0, 0.5), cmap="Greys", vmax=np.percentile(P["cos"], 99.5))
    for tri in P["ag"]:
        for fb, f1 in tri:
            ax.plot(XP, repli(fb + (f1 - fb) * XP), color=F.AQUA, lw=0.6, alpha=0.45)
    ax.grid(False)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.5)
    ax.set_ylabel("fréquence")
    ax.tick_params(labelsize=8)
    if row == 0:
        ax.set_xticklabels([])
        ax.set_title("d)  L'arbre de Perron tourné de 90°")
        ax.text(0.985, 0.04, "sous 0,5 : rien dans le miroir", transform=ax.transAxes, ha="right", fontsize=8.5, bbox=FOND)
        ax.add_patch(plt.Rectangle((0.006, 0.6), 0.205, 0.39, transform=ax.transAxes, fc=F.SURF, ec=F.BASE, lw=0.6, zorder=4))
        axp = ax.inset_axes([0.01, 0.62, 0.2, 0.36], zorder=5)
        for i in range(len(PL)):
            axp.add_patch(Polygon([[PL[i], 0], [PR[i], 0], [PA[i], 1]], closed=True, fc=F.AQUA, alpha=0.3, ec=F.AQUA, lw=0.6))
        axp.set_xlim(LO - 0.05, HI + 0.05)
        axp.set_ylim(-0.05, 1.05)
        axp.set_aspect("equal", adjustable="datalim")
        axp.axis("off")
    else:
        ax.set_xlabel("position (hauteur de l'arbre, de la base au sommet)")
        ax.text(0.985, 0.04, "centré sur 0,5 : la moitié haute passe dans le miroir", transform=ax.transAxes, ha="right",
                fontsize=8.5, bbox=FOND)

# e) les écarts comparés, et la loi du nœud
sub = gs[1, 1].subgridspec(2, 1, hspace=0.42, height_ratios=[1.25, 1])
ax = fig.add_subplot(sub[0, 0])
cas = [("lame de zones", DEPH["toutes sauf 21 et 34"][0], DEPH["toutes (déphasage commun)"][0]),
       ("Perron tourné,\nsous 0,5", P_BAS["e_alt"], P_BAS["e_com"]), ("Perron tourné,\ncentré sur 0,5", P_MIR["e_alt"], P_MIR["e_com"])]
xb = np.arange(len(cas))
ax.bar(xb - 0.18, [c[1] * 100 for c in cas], 0.34, color=F.BLEU, label="relatif : une partie passe de cos à sin")
ax.bar(xb + 0.18, [c[2] * 100 for c in cas], 0.34, color=F.ORANGE, label="commun : tout passe de cos à sin")
for i, c in enumerate(cas):
    for dx_, v in ((-0.18, c[1]), (0.18, c[2])):
        ax.text(i + dx_, v * 100 + 1.5, f"{100 * v:.0f} %", ha="center", fontsize=9)
ax.set_xticks(xb)
ax.set_xticklabels([c[0] for c in cas], fontsize=9)
ax.set_ylabel("écart du spectre (%)")
ax.set_ylim(0, 92)
ax.legend(fontsize=8, loc="upper left", ncol=1, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.grid(axis="x", visible=False)
ax.set_title("e)  Même loi pour la lame et pour Perron")
ax = fig.add_subplot(sub[1, 0])
for (nd, rel, com, *_), ls in ((LOI[(21, 34)], "-"), (LOI_P["miroir"], "--")):
    ax.plot(np.degrees(THETAS), rel / rel.max(), color=F.BLEU, lw=1.4, ls=ls)
    ax.plot(np.degrees(THETAS), com / com.max(), color=F.ORANGE, lw=1.4, ls=ls)
ax.set_xticks([0, 90, 180, 270, 360])
ax.set_xlim(0, 360)
ax.set_xlabel("déphasage θ ajouté (degrés)", fontsize=9)
ax.set_ylabel("nœud miroir\n(rapporté au max)", fontsize=9)
ax.legend(handles=[Line2D([], [], color=F.BLEU, lw=1.4, label="relatif : un tour"),
                   Line2D([], [], color=F.ORANGE, lw=1.4, label="commun : un demi-tour"),
                   Line2D([], [], color=F.INK2, lw=1.2, label="lame (21 × 34)"),
                   Line2D([], [], color=F.INK2, lw=1.2, ls="--", label="Perron tourné")],
          fontsize=7.5, loc="upper center", ncol=2, frameon=True, facecolor=F.SURF, edgecolor="none")
ax.set_ylim(0, 1.5)
ax.set_yticks([0, 0.5, 1])

# f) la bande 2,44–2,56
ax = fig.add_subplot(gs[1, 2])
m = (NN >= 2.2) & (NN <= 2.9)
ax.plot(NN[m], RN[m], color=F.BLEU, lw=1.8)
ax.text(2.74, 1.765, "rⁿ", color=F.BLEU, fontsize=12, fontweight="bold")
ax.axvspan(*BANDE, color=F.JAUNE, alpha=0.18, lw=0)
ax.text(2.5, 1.448, "ta bande\n2,44–2,56", ha="center", va="bottom", fontsize=8.5, color=F.INK2)
for a, b, n_ in LIGNE_FIB[:6]:
    ax.plot([n_, n_], [1.44, a / b], color=F.MUTED, lw=0.7, ls=":")
    ax.plot(n_, a / b, "o", color=F.ORANGE, ms=5, mec=F.SURF, zorder=5)
    if (a, b) in ((3, 2), (5, 3), (8, 5), (13, 8)):
        ax.annotate(f"{a}/{b}", xy=(n_, a / b), xytext={(13, 8): (4, 3), (8, 5): (5, -12)}.get((a, b), (5, 3)),
                    textcoords="offset points", fontsize=8.5)
ax.plot(N_PI2, np.pi / 2, "s", color=F.INK2, ms=5, mec=F.SURF, zorder=5)
ax.annotate("π/2", xy=(N_PI2, np.pi / 2), xytext=(-20, 4), textcoords="offset points", fontsize=8.5, color=F.INK2)
ax.axhline(PHI, color=F.ORANGE, lw=0.8, ls="--")
ax.text(2.895, PHI - 0.012, f"rⁿ = φ : limite en n* = {N_ETOILE:.4f}".replace(".", ","), ha="right", va="top", fontsize=8.5,
        color=F.ORANGE)
ax.axvline(2.5, color=ROUGE, lw=1, ls=(0, (4, 3)))
ax.text(2.49, 1.84, "5/2 : la borne de Wolff (1995)\npour les ensembles de Kakeya en 3D", ha="right", va="top", fontsize=8.5,
        color=ROUGE)
ax.set_xlim(2.2, 2.9)
ax.set_ylim(1.44, 1.85)
ax.set_xlabel("dimension n")
ax.set_ylabel("rⁿ : la boule de la corde, en boules unité")
axi = ax.inset_axes([0.73, 0.05, 0.25, 0.22])
comptes = sum(c for _, c in CONTROLE.values())
k_tot = sum(k for k, _ in CONTROLE.values())
axi.hist(comptes, bins=18, color=F.BASE)
axi.axvline(k_tot, color=ROUGE, lw=1.4)
axi.set_title("croisements par bande\n(rouge : la tienne)", fontsize=7, fontweight="normal", loc="center")
axi.tick_params(labelsize=6.5)
axi.set_yticks([])
axi.set_facecolor(F.SURF)
ax.set_title("f)  2,44–2,56 : une ligne de Fibonacci passe")
F.sauver(fig, "m1_perron_dephasage.png")
