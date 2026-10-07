# Le recueil : vérification des remarques de l'auteur

Recalculé par `scripts/recueil_verifications.py`. Chaque section nourrit une fiche de `recueil/observations/`.

## 1. Les congruences de i

- Base 10 : 9 ≡ −1 ; les racines de −1 sont [3, 7] (3 ≡ i, 7 ≡ −i). Les puissances de 3 modulo 10 : [3, 9, 7, 1], soit i, −1, −i, 1 : 27 ≡ 7 ≡ −i, comme tu l'écris (9^(3/2) = 27).
- Base 2 : −1 ≡ 1, et les racines de −1 sont [1] : 1, −1, i et −i sont le même élément.
- Base 3 : 2 ≡ −1. Dans ℤ/3, 2 n'a pas de racine carrée (aucune). Dans F₉ = F₃[i] (on ajoute i, avec i² = −1 = 2), les racines de 2 sont ['i', '2i'] : √2 = ±i, et 2√2 = 2i = −i. Ta lecture (√2 ≡ i, 2√2 ≡ −i) est exacte dans F₉, pas dans ℤ/3.
- Les bases b ≤ 40 où −1 a une racine carrée : [2, 5, 10, 13, 17, 25, 26, 29, 34, 37]. Il faut qu'aucun facteur premier ne soit ≡ 3 (mod 4) et que 4 ne divise pas b (partie XIX : i n'existe ni modulo 12, ni modulo 24, ni modulo 60).

## 2. Les puissances sous 10

| chiffre | puissances sous 10 | combien |
|---:|---|---:|
| 0 | 1 (0⁰), puis 0 à l'infini | ∞ |
| 1 | 1 à l'infini | ∞ |
| 2 | 1, 2, 4, 8 | 4 |
| 3 | 1, 3, 9 | 3 |
| 4 | 1, 4 | 2 |
| 5 | 1, 5 | 2 |
| 6 | 1, 6 | 2 |
| 7 | 1, 7 | 2 |
| 8 | 1, 8 | 2 |
| 9 | 1, 9 | 2 |

- 2 en a quatre (1, 2, 4, 8), 3 en a trois (1, 3, 9) : le rapport 4/3. Ce sont les seuls chiffres à en avoir plus de deux, hors 0 et 1. Le rapprochement avec le 4/3 des boules et de la partie XXIV (1/x₀ = n + 4/3 − …) est une lecture, pas un calcul : je l'inscris au recueil comme analogie à tester.

## 3. Les exposants 1/2 et 3/2, et leurs fractions continues

| z | z^(1/2) (valeur principale) | z^(3/2) |
|---:|---|---|
| 1 | 1,000000 | 1,000000 |
| −1 | 1,000000·i | −1,000000·i |
| 2 | 1,414214 | 2,828427 |
| −2 | 1,414214·i | −2,828427·i |
| 3 | 1,732051 | 5,196152 |
| −3 | 1,732051·i | −5,196152·i |

**Fractions continues réelles** (algorithme usuel) :

- √2 = [1; 2, 2, 2, 2, 2, 2, 2, 2, …]
- 2√2 = 2^(3/2) = [2; 1, 4, 1, 4, 1, 4, 1, 4, …]
- √3 = [1; 1, 2, 1, 2, 1, 2, 1, 2, …]
- 3√3 = 3^(3/2) = [5; 5, 10, 5, 10, 5, 10, 5, 10, …]

**Tes fractions continues imaginaires**, évaluées sur 61 étages et comparées à la valeur exacte :

| nombre | ta fraction continue | écart à la valeur exacte |
|---|---|---|
| (−2)^(1/2) = i√2 | [i; −2i, 2i, −2i, 2i, −2i, …] | moins de 10⁻³⁰ |
| (−2)^(3/2) = −2√2·i | [−3i; −6i, −6i, −6i, −6i, −6i, …] | moins de 10⁻³⁰ |
| (−3)^(1/2) = i√3 | [2i; 4i, 4i, 4i, 4i, 4i, …] | moins de 10⁻³⁰ |
| (−3)^(3/2) = −3√3·i | [−5i; 5i, −10i, 5i, −10i, 5i, …] | moins de 10⁻³⁰ |

- Les quatre sont justes. Elles viennent de deux écritures :
  - multiplier par i la fraction régulière alterne ±i d'un étage à l'autre, car 1/(i·y) = −i/y : i√2 = [i; −2i, 2i, −2i, …] vient de √2 = [1; 2, 2, …], et −3√3·i = [−5i; 5i, −10i, …] de 3√3 = [5; 5, 10, …] ;
  - l'autre arrondit à l'entier le plus proche, ce qui donne une fraction « par défaut » : √3 = 2 − 1/(4 − 1/(4 − …)) et 2√2 = 3 − 1/(6 − 1/(6 − …)) ; multipliées par i, elles deviennent [2i; 4i, 4i, …] et [−3i; −6i, −6i, …].
- Dans ta liste, le dernier terme de (−3)^(1/2) est écrit « 4 » sans i : c'est une coquille de troncature.

## 4. Les racines digitales

- DR(a·b) = DR(DR(a)·DR(b)) : vrai sur 100 000 paires au hasard (jusqu'à 10¹²). La raison : DR(n) ≡ n (mod 9), car 10 ≡ 1 (mod 9). C'est la « base 9 » que tu décris : 0 et 9 se superposent.
- Multiplier par 2, en racines digitales : orbites {1, 2, 4, 8, 7, 5} ; {3, 6} ; {9}.
- Multiplier par 5, en racines digitales : orbites {1, 5, 7, 8, 4, 2} ; {3, 6} ; {9}.
- DR(2ⁿ) = 1, 2, 4, 8, 7, 5, 1, 2, 4, 8, 7, 5… ; DR(5ⁿ) = 1, 5, 7, 8, 4, 2, 1, 5, 7, 8, 4, 2… ; DR(3ⁿ) = 1, 3, 9, 9, 9, 9, 9, 9…
- La période de 1/7 est 142857 : chiffres ['1', '2', '4', '5', '7', '8'], les mêmes que l'orbite de 2 (et de 5), dans un autre ordre. Variation du paramètre : l'autre premier de période 6, 13, a la période 076923 (chiffres ['0', '2', '3', '6', '7', '9']). Le lien est donc propre à 7, pas une loi des périodes de longueur 6.
- « DR 3 donne 3 et 6 alterné » : c'est l'orbite de 3 sous ×2 (ou ×5) : 3, 6, 3, 6… Les puissances de 3, elles, donnent 1, 3, 9, 9, 9… (je lis ta phrase comme l'orbite de 3 sous le doublement).

## 5. Midy et Midy étendu

- Premiers de 7 à 397 : 49 à période paire, 26 à période impaire (31, 37, 41, 43, 53, 67, 71, 79, 83, 107, 151, 163, …).
- Midy (période paire 2h : les deux moitiés font 10ʰ − 1) : vrai pour 49 / 49. Exemple : 1/7 → 142 + 857 = 999 ; 1/17 → 05882352 + 94117647 = 99999999.
- Midy étendu (couper la période en k blocs égaux : leur somme est un multiple de 10^(L/k) − 1) : vrai pour 375 / 375 découpages.

## 6. Les premiers par position

- Premiers sous 10⁶, par chiffre des unités : 1 : 19 617 ; 2 : 1 ; 3 : 19 665 ; 5 : 1 ; 7 : 19 621 ; 9 : 19 593. Hors 2 et 5, tout premier finit par 1, 3, 7 ou 9.
- Chaque dizaine 10a + {1, 3, 7, 9} choisit lesquels sont premiers : un sommet du cube {0, 1}⁴, une région d'un Venn à quatre ensembles. Sur les 100 000 dizaines sous 10⁶ :

| motif (unités premières) | dizaines |
|---|---:|
| {} | 40 636 |
| {3} | 10 709 |
| {7} | 10 681 |
| {1} | 10 660 |
| {9} | 10 644 |
| {3, 9} | 4 216 |
| {1, 7} | 4 208 |
| {1, 3} | 1 515 |
| {7, 9} | 1 493 |
| {3, 7} | 1 484 |
| {1, 9} | 1 457 |
| {1, 7, 9} | 556 |
| {1, 3, 9} | 542 |
| {3, 7, 9} | 520 |
| {1, 3, 7} | 514 |
| {1, 3, 7, 9} | 165 |

- Les dizaines aux quatre premiers (les « quadruplets ») : 165 sous 10⁶ (11, 101, 191, 821, 1481, 1871, …). Toutes ont a ≡ 1 (mod 3) : oui. Sinon, l'un des quatre serait divisible par 3.
- **Le reste de a modulo 3 choisit la face du cube.** Pour a ≡ 0, seuls 1 et 7 peuvent être premiers (unités rencontrées : [1, 7]) ; pour a ≡ 2, seuls 3 et 9 ([3, 9]) ; pour a ≡ 1, les quatre ([1, 3, 7, 9]). La raison : 10a + u ≡ a + u (mod 3). C'est pourquoi les paires {1, 7} et {3, 9} (même reste modulo 3, distance 6) sont près de trois fois plus fréquentes que {1, 3}, {7, 9}, {3, 7} ou {1, 9} : 8 424 contre 3 008 + 2 941 (la série singulière de Hardy et Littlewood, vue sur le cube).

## 7. L'inversion 2 ↔ 5 et le croisement en 7/2

- 1/2 = 5/10 = 0,5 et 1/5 = 2/10 = 0,2 : diviser par 2, c'est multiplier par 5 et déplacer la virgule (partie XXVI : 2⁻ʲ = 5ʲ·10⁻ʲ).
- 5 − 2 = 3, 3/2 = 1,5, 2 + 1,5 = 3,5 = 5 − 1,5 : le croisement est au milieu de 2 et 5, en 7/2 ; et 2 × 5 = 10, la base.

(calculs : 0.3 s)
