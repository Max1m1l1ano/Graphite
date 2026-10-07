"""
Le recueil : vérification des remarques calculables de l'auteur (message qui fonde la section « Hasard, coïncidences,
faits amusants, analogies, corrélation et causalité » de CLAUDE.md).

    python3 scripts/recueil_verifications.py        # ≈ 5 s

Écrit resultats/recueil_verifications.md. Chaque section nourrit une fiche du recueil (recueil/observations/).

1. Les congruences de i : bases 10, 2 et 3 (et l'extension F₉ = F₃[i]).
2. Les puissances sous 10 : 2 en a quatre, 3 en a trois.
3. Les exposants 1/2 et 3/2 de ±1, ±2, ±3 et leurs fractions continues (réelles et imaginaires).
4. Les racines digitales : DR(a·b) = DR(DR(a)·DR(b)), les orbites de ×2 et ×5 modulo 9, la période de 1/7.
5. Midy et Midy étendu.
6. Les premiers par position : le chiffre des unités, et chaque dizaine comme sommet du cube {0, 1}⁴.
7. L'inversion 2 ↔ 5 de part et d'autre de la virgule, et le croisement en 7/2.
"""

import os
import random
import time
from fractions import Fraction

import mpmath as mp

ICI = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
md = []
mp.mp.dps = 40


def ligne(t=""):
    print(t)
    md.append(t)


def fr(x, f="{:.4f}"):
    return f.format(x).replace(".", ",").replace("-", "−")


def ent(n):
    return f"{n:,}".replace(",", " ")


ligne("# Le recueil : vérification des remarques de l'auteur\n")
ligne("Recalculé par `scripts/recueil_verifications.py`. Chaque section nourrit une fiche de `recueil/observations/`.\n")

# ===========================================================================
# 1. Les congruences de i
# ===========================================================================
ligne("## 1. Les congruences de i\n")
racines10 = [x for x in range(10) if (x * x) % 10 == 9]
puis3 = [pow(3, k, 10) for k in range(1, 5)]
ligne(f"- Base 10 : 9 ≡ −1 ; les racines de −1 sont {racines10} (3 ≡ i, 7 ≡ −i). Les puissances de 3 modulo 10 :"
      f" {puis3}, soit i, −1, −i, 1 : 27 ≡ 7 ≡ −i, comme tu l'écris (9^(3/2) = 27).")
racines2 = [x for x in range(2) if (x * x) % 2 == (-1) % 2]
ligne(f"- Base 2 : −1 ≡ 1, et les racines de −1 sont {racines2} : 1, −1, i et −i sont le même élément.")
racines3 = [x for x in range(3) if (x * x) % 3 == 2]
# F₉ = F₃[i] : éléments a + b·i, i² = −1 = 2
F9 = [(a, b) for a in range(3) for b in range(3)]


def mul9(u, v):
    return ((u[0] * v[0] - u[1] * v[1]) % 3, (u[0] * v[1] + u[1] * v[0]) % 3)


rac2_F9 = [u for u in F9 if mul9(u, u) == (2, 0)]
ligne(f"- Base 3 : 2 ≡ −1. Dans ℤ/3, 2 n'a pas de racine carrée ({racines3 or 'aucune'}). Dans F₉ = F₃[i] (on ajoute i,"
      f" avec i² = −1 = 2), les racines de 2 sont {['i' if u == (0, 1) else '2i' for u in rac2_F9]} : √2 = ±i, et"
      f" 2√2 = 2i = −i. Ta lecture (√2 ≡ i, 2√2 ≡ −i) est exacte dans F₉, pas dans ℤ/3.")
avec_i = [b for b in range(2, 41) if any((x * x + 1) % b == 0 for x in range(b))]
ligne(f"- Les bases b ≤ 40 où −1 a une racine carrée : {avec_i}. Il faut qu'aucun facteur premier ne soit ≡ 3 (mod 4) et que"
      f" 4 ne divise pas b (partie XIX : i n'existe ni modulo 12, ni modulo 24, ni modulo 60).\n")

# ===========================================================================
# 2. Les puissances sous 10
# ===========================================================================
ligne("## 2. Les puissances sous 10\n")
PS = {}
for b in range(2, 10):
    PS[b] = [b ** k for k in range(0, 10) if b ** k < 10]
ligne("| chiffre | puissances sous 10 | combien |")
ligne("|---:|---|---:|")
ligne("| 0 | 1 (0⁰), puis 0 à l'infini | ∞ |")
ligne("| 1 | 1 à l'infini | ∞ |")
for b in range(2, 10):
    ligne(f"| {b} | {', '.join(map(str, PS[b]))} | {len(PS[b])} |")
ligne(f"\n- 2 en a quatre (1, 2, 4, 8), 3 en a trois (1, 3, 9) : le rapport {Fraction(len(PS[2]), len(PS[3]))}. Ce sont les"
      " seuls chiffres à en avoir plus de deux, hors 0 et 1. Le rapprochement avec le 4/3 des boules et de la partie XXIV"
      " (1/x₀ = n + 4/3 − …) est une lecture, pas un calcul : je l'inscris au recueil comme analogie à tester.\n")

# ===========================================================================
# 3. Exposants 1/2 et 3/2, fractions continues
# ===========================================================================
ligne("## 3. Les exposants 1/2 et 3/2, et leurs fractions continues\n")
ligne("| z | z^(1/2) (valeur principale) | z^(3/2) |")
ligne("|---:|---|---|")
for z in (1, -1, 2, -2, 3, -3):
    a, b = mp.power(z, mp.mpf(1) / 2), mp.power(z, mp.mpf(3) / 2)

    def txt(w):
        re_, im_ = float(mp.re(w)), float(mp.im(w))
        if abs(im_) < 1e-30:
            return fr(re_, '{:.6f}')
        if abs(re_) < 1e-30:
            return fr(im_, '{:.6f}') + "·i"
        return f"{fr(re_, '{:.6f}')} + {fr(im_, '{:.6f}')}·i"
    ligne(f"| {str(z).replace('-', '−')} | {txt(a)} | {txt(b)} |")


def fc_reelle(x, n=12):
    out = []
    for _ in range(n):
        a = int(mp.floor(x))
        out.append(a)
        x = 1 / (x - a)
    return out


def evalue(termes):
    v = termes[-1]
    for t in reversed(termes[:-1]):
        v = t + 1 / v
    return v


ligne("\n**Fractions continues réelles** (algorithme usuel) :\n")
for nom, x in (("√2", mp.sqrt(2)), ("2√2 = 2^(3/2)", 2 * mp.sqrt(2)), ("√3", mp.sqrt(3)), ("3√3 = 3^(3/2)", 3 * mp.sqrt(3))):
    ligne(f"- {nom} = [{fc_reelle(x)[0]}; {', '.join(map(str, fc_reelle(x)[1:9]))}, …]")
I = mp.mpc(0, 1)
CAS_FC = [
    ("(−2)^(1/2) = i√2", I * mp.sqrt(2), [I] + [(-2 * I) if k % 2 == 0 else (2 * I) for k in range(60)]),
    ("(−2)^(3/2) = −2√2·i", -2 * mp.sqrt(2) * I, [-3 * I] + [-6 * I] * 60),
    ("(−3)^(1/2) = i√3", I * mp.sqrt(3), [2 * I] + [4 * I] * 60),
    ("(−3)^(3/2) = −3√3·i", -3 * mp.sqrt(3) * I, [-5 * I] + [(5 * I) if k % 2 == 0 else (-10 * I) for k in range(60)]),
]
ligne("\n**Tes fractions continues imaginaires**, évaluées sur 61 étages et comparées à la valeur exacte :\n")
ligne("| nombre | ta fraction continue | écart à la valeur exacte |")
ligne("|---|---|---|")
def terme(t):
    k = int(mp.nint(mp.im(t)))
    return {1: "i", -1: "−i"}.get(k, f"{k}i".replace("-", "−"))


for nom, x, termes in CAS_FC:
    e = abs(evalue(termes) - x)
    etxt = "moins de 10⁻³⁰" if e < mp.mpf(10) ** -30 else mp.nstr(e, 3)
    ligne(f"| {nom} | [{terme(termes[0])}; {', '.join(terme(t) for t in termes[1:6])}, …] | {etxt} |")
ligne("\n- Les quatre sont justes. Elles viennent de deux écritures :")
ligne("  - multiplier par i la fraction régulière alterne ±i d'un étage à l'autre, car 1/(i·y) = −i/y : i√2 = [i; −2i, 2i,"
      " −2i, …] vient de √2 = [1; 2, 2, …], et −3√3·i = [−5i; 5i, −10i, …] de 3√3 = [5; 5, 10, …] ;")
ligne("  - l'autre arrondit à l'entier le plus proche, ce qui donne une fraction « par défaut » : √3 = 2 − 1/(4 − 1/(4 − …)) et"
      " 2√2 = 3 − 1/(6 − 1/(6 − …)) ; multipliées par i, elles deviennent [2i; 4i, 4i, …] et [−3i; −6i, −6i, …].")
ligne("- Dans ta liste, le dernier terme de (−3)^(1/2) est écrit « 4 » sans i : c'est une coquille de troncature.\n")

# ===========================================================================
# 4. Racines digitales
# ===========================================================================
ligne("## 4. Les racines digitales\n")


def dr(n):
    return 0 if n == 0 else 1 + (n - 1) % 9


random.seed(31)
ok = all(dr(a * b) == dr(dr(a) * dr(b)) for a, b in ((random.randrange(1, 10 ** 12), random.randrange(1, 10 ** 12))
                                                         for _ in range(100000)))
ligne(f"- DR(a·b) = DR(DR(a)·DR(b)) : {'vrai' if ok else 'faux'} sur 100 000 paires au hasard (jusqu'à 10¹²). La raison :"
      " DR(n) ≡ n (mod 9), car 10 ≡ 1 (mod 9). C'est la « base 9 » que tu décris : 0 et 9 se superposent.")


def orbite(m, s):
    o, x = [], s
    while x not in o:
        o.append(x)
        x = dr(x * m)
    return o


for m in (2, 5):
    orbs, vus = [], set()
    for s in range(1, 10):
        if s not in vus:
            o = orbite(m, s)
            orbs.append(o)
            vus |= set(o)
    ligne(f"- Multiplier par {m}, en racines digitales : orbites {' ; '.join('{' + ', '.join(map(str, o)) + '}' for o in orbs)}.")
dr2 = [dr(2 ** n) for n in range(12)]
dr5 = [dr(5 ** n) for n in range(12)]
dr3 = [dr(3 ** n) for n in range(8)]
p7 = str(10 ** 6 // 7).zfill(6)
p13 = str(10 ** 6 // 13).zfill(6)
ligne(f"- DR(2ⁿ) = {', '.join(map(str, dr2))}… ; DR(5ⁿ) = {', '.join(map(str, dr5))}… ; DR(3ⁿ) = {', '.join(map(str, dr3))}…")
ligne(f"- La période de 1/7 est {p7} : chiffres {sorted(set(p7))}, les mêmes que l'orbite de 2 (et de 5), dans un autre ordre."
      f" Variation du paramètre : l'autre premier de période 6, 13, a la période {p13} (chiffres {sorted(set(p13))}). Le lien"
      " est donc propre à 7, pas une loi des périodes de longueur 6.")
ligne("- « DR 3 donne 3 et 6 alterné » : c'est l'orbite de 3 sous ×2 (ou ×5) : 3, 6, 3, 6… Les puissances de 3, elles, donnent"
      " 1, 3, 9, 9, 9… (je lis ta phrase comme l'orbite de 3 sous le doublement).\n")

# ===========================================================================
# 5. Midy
# ===========================================================================
ligne("## 5. Midy et Midy étendu\n")


def periode(p):
    k, r = 1, 10 % p
    while r != 1:
        r = r * 10 % p
        k += 1
    return k


def chiffres(p, L):
    return str((10 ** L - 1) // p).zfill(L)


PREM = [p for p in range(7, 400) if all(p % q for q in range(2, int(p ** 0.5) + 1)) and p != 5]
pairs, impairs, midy_ok, etendu_ok, etendu_n = [], [], 0, 0, 0
for p in PREM:
    L = periode(p)
    d = chiffres(p, L)
    if L % 2 == 0:
        pairs.append(p)
        h = L // 2
        midy_ok += int(int(d[:h]) + int(d[h:]) == 10 ** h - 1)
    else:
        impairs.append(p)
    for k in range(2, L + 1):
        if L % k == 0 and L // k >= 1:
            b = L // k
            s = sum(int(d[j * b:(j + 1) * b]) for j in range(k))
            etendu_n += 1
            etendu_ok += int(s % (10 ** b - 1) == 0)
ligne(f"- Premiers de 7 à 397 : {len(pairs)} à période paire, {len(impairs)} à période impaire"
      f" ({', '.join(map(str, impairs[:12]))}, …).")
ligne(f"- Midy (période paire 2h : les deux moitiés font 10ʰ − 1) : vrai pour {midy_ok} / {len(pairs)}. Exemple :"
      f" 1/7 → 142 + 857 = 999 ; 1/17 → {chiffres(17, 16)[:8]} + {chiffres(17, 16)[8:]} = 99999999.")
ligne(f"- Midy étendu (couper la période en k blocs égaux : leur somme est un multiple de 10^(L/k) − 1) : vrai pour"
      f" {etendu_ok} / {etendu_n} découpages.\n")

# ===========================================================================
# 6. Les premiers par position
# ===========================================================================
ligne("## 6. Les premiers par position\n")
N = 10 ** 6
crible = bytearray([1]) * N
crible[0:2] = b"\x00\x00"
for i in range(2, int(N ** 0.5) + 1):
    if crible[i]:
        crible[i * i::i] = bytearray(len(range(i * i, N, i)))
unites = {u: sum(crible[u::10]) for u in range(10)}
ligne("- Premiers sous 10⁶, par chiffre des unités : " + " ; ".join(f"{u} : {ent(unites[u])}" for u in range(10) if unites[u])
      + ". Hors 2 et 5, tout premier finit par 1, 3, 7 ou 9.")
MOTIFS = {}
for a in range(N // 10):
    m = tuple(u for u in (1, 3, 7, 9) if crible[10 * a + u])
    MOTIFS[m] = MOTIFS.get(m, 0) + 1
ligne("- Chaque dizaine 10a + {1, 3, 7, 9} choisit lesquels sont premiers : un sommet du cube {0, 1}⁴, une région d'un Venn"
      f" à quatre ensembles. Sur les {ent(N // 10)} dizaines sous 10⁶ :\n")
ligne("| motif (unités premières) | dizaines |")
ligne("|---|---:|")
for m, c in sorted(MOTIFS.items(), key=lambda t: -t[1]):
    ligne(f"| {{{', '.join(map(str, m))}}} | {ent(c)} |")
QUAD = [10 * a for a in range(N // 10) if all(crible[10 * a + u] for u in (1, 3, 7, 9))]
ligne(f"\n- Les dizaines aux quatre premiers (les « quadruplets ») : {len(QUAD)} sous 10⁶ ({', '.join(str(q + 1) for q in QUAD[:6])}, …)."
      f" Toutes ont a ≡ 1 (mod 3) : {'oui' if all((q // 10) % 3 == 1 for q in QUAD) else 'non'}. Sinon, l'un des quatre"
      " serait divisible par 3.")
FACES = {0: set(), 1: set(), 2: set()}
for a in range(1, N // 10):
    m = tuple(u for u in (1, 3, 7, 9) if crible[10 * a + u])
    FACES[a % 3] |= set(m)
ligne(f"- **Le reste de a modulo 3 choisit la face du cube.** Pour a ≡ 0, seuls 1 et 7 peuvent être premiers (unités"
      f" rencontrées : {sorted(FACES[0])}) ; pour a ≡ 2, seuls 3 et 9 ({sorted(FACES[2])}) ; pour a ≡ 1, les quatre"
      f" ({sorted(FACES[1])}). La raison : 10a + u ≡ a + u (mod 3). C'est pourquoi les paires {{1, 7}} et {{3, 9}} (même reste"
      f" modulo 3, distance 6) sont près de trois fois plus fréquentes que {{1, 3}}, {{7, 9}}, {{3, 7}} ou {{1, 9}} :"
      f" {ent(MOTIFS[(1, 7)] + MOTIFS[(3, 9)])} contre {ent(MOTIFS[(1, 3)] + MOTIFS[(7, 9)])} + {ent(MOTIFS[(3, 7)] + MOTIFS[(1, 9)])}"
      " (la série singulière de Hardy et Littlewood, vue sur le cube).\n")

# ===========================================================================
# 7. 2 ↔ 5 et le croisement en 7/2
# ===========================================================================
ligne("## 7. L'inversion 2 ↔ 5 et le croisement en 7/2\n")
ligne("- 1/2 = 5/10 = 0,5 et 1/5 = 2/10 = 0,2 : diviser par 2, c'est multiplier par 5 et déplacer la virgule (partie XXVI :"
      " 2⁻ʲ = 5ʲ·10⁻ʲ).")
ligne(f"- 5 − 2 = 3, 3/2 = 1,5, 2 + 1,5 = 3,5 = 5 − 1,5 : le croisement est au milieu de 2 et 5, en {Fraction(7, 2)} ; et"
      f" 2 × 5 = 10, la base.")
ligne(f"\n(calculs : {time.time() - T0:.1f} s)")
with open(os.path.join(ICI, "..", "resultats", "recueil_verifications.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(md) + "\n")
