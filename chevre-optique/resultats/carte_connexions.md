# Résultats de la partie XXVII (générés par scripts/carte_connexions.py)

## 1. Le graphe des parties I à XXVI

- 178 paires reliées sur 325 (54,8 %) ; 932 renvois au total.
- La partie I (le README) porte l'index de la série : elle est reliée à 25 parties sur 25. On ne prédit donc pas de liens avec elle.

| partie | sujet | voisins | renvois reçus |
|---|---|---:|---:|
| I | la chèvre (README) | 25 | 98 |
| XXIII | la relecture : lentilles, boules, grain | 24 | 31 |
| XIV | l'aiguille sur une grille | 20 | 30 |
| VI | le ménisque de 0,35 % | 17 | 68 |
| XV | la grille décalée | 16 | 26 |
| V | Kakeya, Perron | 15 | 43 |
| XX | deux chèvres au même endroit | 15 | 46 |
| XVII | deux foyers, récursion d'argent | 14 | 32 |
| XIX | les bases sont des objets | 14 | 47 |
| XXI | les trois 24, le miroir 49-50-51 | 14 | 43 |
| XXIV | un tiers de dimension | 14 | 31 |
| IV | les trois solides | 13 | 37 |
| VIII | foyer, diaphragme, Fibonacci | 13 | 38 |
| IX | le moiré de Fibonacci | 13 | 35 |
| XIII | Perron tournés, cos/sin | 13 | 16 |
| XI | l'angle d'or, trois distances | 12 | 35 |
| XVI | ménisque et projection | 12 | 47 |
| VII | les polynômes | 11 | 38 |
| XVIII | faire des ronds avec des carrés | 11 | 33 |
| XXVI | Kakeya à 10⁻⁵⁰, kibi, cube | 11 | 9 |
| II | Archimède, le cube qui tourne | 10 | 37 |
| III | π, √2 et les dimensions | 10 | 18 |
| X | le point et le carré, Ptolémée | 10 | 33 |
| XXII | le carré de neuf points | 10 | 17 |
| XXV | les ouverts, la tranche 49 – 55 | 10 | 22 |
| XII | 144, la douzième lentille | 9 | 22 |

### 1.1 Les liens que le graphe prédit

Pour deux parties qui ne se citent pas, on additionne 1/ln(degré) sur leurs voisins communs (indice d'Adamic–Adar) : deux chapitres qui fréquentent les mêmes chapitres, surtout des chapitres peu cités, devraient se parler.

| rang | paire | voisins communs | indice | dans cette partie |
|---:|---|---:|---|---|
| 1 | XXIII – XXVI | 11 | 4,23 | § 3 : l'échelle des taux de change |
| 2 | XIV – XX | 11 | 4,21 | — |
| 3 | VI – VIII | 11 | 4,15 | — |
| 4 | XIV – XVII | 11 | 4,11 | § 7 : les aiguilles d'argent |
| 5 | VI – XX | 10 | 3,80 | § 6 : les deux bouts du ménisque |
| 6 | XIV – XXIV | 10 | 3,80 | — |
| 7 | VI – XXI | 10 | 3,75 | — |
| 8 | V – IX | 10 | 3,69 | — |
| 9 | VI – XIX | 9 | 3,41 | — |
| 10 | V – XXI | 9 | 3,39 | — |
| 11 | VII – XIV | 9 | 3,33 | — |
| 12 | XV – XVIII | 9 | 3,29 | § 2 : les cercles arctiques |
| 13 | IV – XV | 9 | 3,26 | — |
| 14 | XVI – XXII | 9 | 3,22 | — |
| 15 | V – XX | 8 | 3,02 | — |

Les pistes (prédites, pas encore établies) et leurs voisins communs :

- XIV – XX : I, IV, XI, XV, XVI, XVIII, XIX, XXI, XXIII, XXV, XXVI
- VI – VIII : I, II, V, VII, IX, XII, XIII, XIV, XV, XVII, XXIII
- XIV – XXIV : I, IV, VI, XVI, XVIII, XIX, XXI, XXIII, XXV, XXVI
- VI – XXI : I, IV, VII, XIII, XIV, XVI, XVII, XXII, XXIII, XXIV
- V – IX : I, IV, VI, VII, VIII, X, XIII, XIV, XV, XXIII
- VI – XIX : I, II, XIV, XVI, XVII, XVIII, XXII, XXIII, XXIV
- V – XXI : I, IV, VII, XIII, XIV, XVII, XXII, XXIII, XXVI
- VII – XIV : I, III, IV, V, VI, VIII, IX, XXI, XXIII
- IV – XV : I, III, V, VI, IX, XIII, XIV, XX, XXIII
- XVI – XXII : I, VI, XV, XVII, XIX, XX, XXI, XXIII, XXIV
- V – XX : I, IV, VII, XV, XVII, XXII, XXIII, XXVI

Rangs des autres paires établies ici : IV – XXVI : 17e ; XXII – XXVI : 60e ; II – XV : 41e ; XV – XXVI : 56e ; XVIII – XXVI : 102e ; II – XVIII : 123e ; VI – XXVI : 54e.

## 2. Les cercles arctiques

### 2.1 Les comptes exacts

| ordre n | pavages du diamant aztèque (comptés) | 2^(n(n+1)/2) | | côté a | partitions planes a × a × a (comptées) | MacMahon |
|---:|---|---|---|---:|---|---|
| 1 | 2 | 2^1 | | 1 | 2 | 2 |
| 2 | 8 | 2^3 | | 2 | 20 | 20 |
| 3 | 64 | 2^6 | | 3 | 980 | 980 |
| 4 | 1024 | 2^10 | | 4 | 232848 | 232848 |
| 5 | 32768 | 2^15 | | 5 | — | 267227532 |
| 6 | 2097152 | 2^21 | | 6 | — | 1478619421136 |

- L'ordre 4 a 2¹⁰ = 1 024 pavages (le kibi) et l'ordre 6 en a 2²¹ = 2 097 152 (les chiffres du 9,72 de la partie XXVI) : chaque étage n multiplie le compte par 2ⁿ, il compte en crans.
- L'hexagone de côté 1 a 2 pavages : les deux lectures du cube de Necker (partie XXVI).

### 2.2 Le losange : un diamant aztèque d'ordre 48 (2352 dominos, 40000 balayages)

Part des dominos verticaux au fil des balayages (½ attendu par symétrie) : 0 : 0,012, 5000 : 0,495, 10000 : 0,465, 15000 : 0,475, 20000 : 0,484, 25000 : 0,516, 30000 : 0,491, 35000 : 0,471, 40000 : 0,509.

| distance au centre (en rayons du cercle inscrit) | part du type majoritaire de chaque secteur |
|---|---|
| 0,00 – 0,25 | 0,345 |
| 0,25 – 0,50 | 0,374 |
| 0,50 – 0,75 | 0,357 |
| 0,75 – 0,90 | 0,528 |
| 0,90 – 1,00 | 0,685 |
| 1,00 – 1,10 | 0,996 |
| 1,10 – 1,25 | 1,000 |
| 1,25 – 1,42 | 1,000 |

Dans le cercle, les quatre sortes de dominos se mélangent ; dehors, chaque coin n'en garde qu'une (gelé).

### 2.3 L'hexagone : cubes empilés dans une boîte 40 × 40 × 40 (4800 losanges, 24000 balayages)

Hauteur moyenne ÷ côté au fil des balayages (½ attendu par symétrie) : 0 : 0,001, 4000 : 0,493, 8000 : 0,504, 12000 : 0,534, 16000 : 0,513, 20000 : 0,493, 24000 : 0,498.

| distance au centre (en rayons du cercle inscrit) | part du type majoritaire de chaque secteur |
|---|---|
| 0,00 – 0,25 | 0,404 |
| 0,25 – 0,50 | 0,381 |
| 0,50 – 0,75 | 0,412 |
| 0,75 – 0,90 | 0,427 |
| 0,90 – 1,00 | 0,684 |
| 1,00 – 1,06 | 0,977 |
| 1,06 – 1,12 | 1,000 |
| 1,12 – 1,16 | 1,000 |

(échantillonnage : 13 s)

### 2.4 Les deux cercles

- Losange de sommets (±1, 0), (0, ±1) : cercle inscrit de rayon 1/√2 = 0,707107, d'aire π/2 = la moitié du disque circonscrit ; il couvre π/4 = 0,7854 du losange.
- Hexagone du cube (ombre le long de la grande diagonale, côté √(2/3)) : cercle inscrit de rayon √2/2, l'ombre de la sphère médiane (partie II) ; il couvre π/(2√3) = 0,9069 de l'hexagone, la densité de l'empilement hexagonal des disques.

## 3. L'échelle des taux de change du grain (XXIII – XXV – XXVI)

| lecture | loi | à 10⁻⁵⁰ | par décade de grain |
|---|---|---|---|
| l'équateur (la tranche de demi-largeur ε contient la moitié de la boule) | ε⁻² | 4,55·10⁹⁹ | × 100 |
| la coquille (épaisseur ε, la moitié du volume) | ε⁻¹ | 6,93·10⁴⁹ | × 10 |
| le plan de la lentille | ε⁻¹ | 1,00·10⁵⁰ | × 10 |
| le ménisque (la chèvre et son simplexe) | ε^(−1/2) | 5,77·10²⁴ | × 3,162 |
| la série en 1/n, tronquée au mieux | ≈ 2·log₂(1/ε) | 315,7 | + 6,584 |
| Kakeya : l'inverse de l'aire minimale | ≈ (2/π)·ln(1/ε) | 74,4 | + 1,466 |

- La série gagne un facteur √2 par dimension (2^(−n/2)) : un cran de la partie XXI. Une décade de grain coûte donc 2·log₂ 10 = 6,6439 dimensions, autant de crans qu'il y en a dans une décade.
- Les exposants 2, 1, ½ se divisent par deux à chaque marche ; le logarithme est la marche 0 : ln(1/ε) = lim (ε^(−s) − 1)/s quand s → 0.
  - s = 1 : (ε^(−s) − 1)/s à 10⁻⁵⁰ = 1,00·10⁵⁰
  - s = 0,5 : (ε^(−s) − 1)/s à 10⁻⁵⁰ = 2,00·10²⁵
  - s = 0,1 : (ε^(−s) − 1)/s à 10⁻⁵⁰ = 999990,0
  - s = 0,01 : (ε^(−s) − 1)/s à 10⁻⁵⁰ = 216,2
  - s = 0,001 : (ε^(−s) − 1)/s à 10⁻⁵⁰ = 122,0
  - limite : ln(10⁵⁰) = 115,1293

## 4. L'ombre du cube et les 2n chèvres (XXII – XXVI)

- Pour u unitaire : ombre(u) × cos(angle au piquet le plus proche) = ‖u‖₁·‖u‖∞ ≥ ‖u‖₂² = 1 (sur 20 000 directions au hasard, l'excès minimal au-dessus de 1 vaut 5,7e−03).
- Égalité exactement quand toutes les composantes non nulles ont la même taille : les 26 directions du cube de 27 points {−1, 0, 1}³ (partie XXII en 3D).
  - 6 centres de faces : le carré, ombre 1 ; 12 milieux d'arêtes : le rectangle, ombre √2 ; 8 sommets : l'hexagone, ombre √3. L'ombre vaut la distance du point au centre.
- Les 2n chèvres de la partie XXII couvrent la clôture quand cos α_n < 1/√n, c'est-à-dire quand 1/cos α_n dépasse la plus grande ombre du cube de dimension n, √n.

| n | α_n | 1/cos α_n = 1/x₀ | n + 4/3 − 112/(45n) | plus grande ombre √n | seuil arccos(1/√n) |
|---:|---|---|---|---|---|
| 2 | 70,81° | 3,0425 | 2,0889 | 1,4142 | 45,00° |
| 3 | 75,80° | 4,0760 | 3,5037 | 1,7321 | 54,74° |
| 4 | 78,70° | 5,1024 | 4,7111 | 2,0000 | 60,00° |
| 5 | 80,60° | 6,1236 | 5,8356 | 2,2361 | 63,43° |
| 8 | 83,74° | 9,1683 | 9,0222 | 2,8284 | 69,30° |
| 10 | 84,87° | 11,1886 | 11,0844 | 3,1623 | 71,57° |
| 24 | 87,73° | 25,2545 | 25,2296 | 4,8990 | 78,22° |
| 50 | 88,88° | 51,2903 | 51,2836 | 7,0711 | 81,87° |
| 100 | 89,43° | 101,3103 | 101,3084 | 10,0000 | 84,26° |

## 5. Archimède dans l'ombre du cube (III, IV – XXVI)

Ombres (aires) du cube d'arête 1 et de sa sphère médiane (rayon √2/2, qui passe par les milieux des arêtes) :

- plus petite ombre du cube : 1 (le carré) ; ombre moyenne : 3/2 (Cauchy : surface 6 ÷ 4) ;
- ombre de la sphère médiane : π/2 = 1,570796 (dans toutes les directions) ;
- plus grande ombre du cube : √3 = 1,732051 (l'hexagone, dont le cercle inscrit est l'ombre de la sphère médiane, partie II).
- Donc 3/2 < π/2 < √3, c'est-à-dire 3 < π < 2√3 : les premières bornes d'Archimède, celles de l'hexagone.
  - À droite, c'est la même figure qu'Archimède : un cercle dans l'hexagone circonscrit.
  - À gauche, c'est Cauchy : l'ombre moyenne vaut le quart de la surface, et la sphère médiane (2π) a plus de surface que le cube (6), parce que π > 3.
- L'écart π/2 − 3/2 = (π − 3)/2 = 0,070796 : la moitié des « retenues de l'hexagone » 1/8 + 9/640 + … de la partie IV.

## 6. Les deux chèvres au même endroit sont les deux bouts du ménisque (VI – XX – XXIV)

- L'écart relatif (corde − arête du simplexe) ÷ arête vaut 0 en dimension 1, culmine à 0,3495 % en dimension 2,083 (dimension réelle), et tend vers 0 à l'infini. L'écart absolu (corde − arête) culmine en dimension 2,244, le « n ≈ 2,24 » de la partie VI.
- La chèvre plane (n = 2) est à 0,3488 % : à 0,19 % près du maximum. La chèvre infinie (corde √2) est à 0.
- En unités de dimension, le même ménisque grandit au contraire de 0 à 1/3 : N − n = 0,0425 en dimension 2, 0,1886 en 10, 0,3103 en 100, 0,3309 en 1 000 (partie XXIV : un tiers de dimension).

## 7. Les aiguilles d'argent (XIV – XVII)

Deux familles d'aiguilles de la grille, (x, y) = (F_k, F_(k+1)) et (P_k, P_(k+1)) :

| k | Fibonacci | angle | écart à la direction d'or | Pell | angle | écart à la direction d'argent |
|---:|---|---|---|---|---|---|
| 1 | (1, 1) | 45,000° | −0,32492 | (1, 2) | 63,435° | −0,158513 |
| 2 | (1, 2) | 63,435° | +0,20081 | (2, 5) | 68,199° | +0,065658 |
| 3 | (2, 3) | 56,310° | −0,12411 | (5, 12) | 67,380° | −0,027196 |
| 4 | (3, 5) | 59,036° | +0,07670 | (12, 29) | 67,521° | +0,011265 |
| 5 | (5, 8) | 57,995° | −0,04741 | (29, 70) | 67,496° | −0,004666 |
| 6 | (8, 13) | 58,392° | +0,02930 | (70, 169) | 67,501° | +0,001933 |
| 7 | (13, 21) | 58,241° | −0,01811 | (169, 408) | 67,500° | −0,000801 |
| 8 | (21, 34) | 58,299° | +0,01119 | (408, 985) | 67,500° | +0,000332 |

- Direction d'or : arctan φ = 58,283° ; direction d'argent : arctan(1 + √2) = 67,500° = 67,5° exactement.
- Deux voisines ont toujours un déterminant ±1 (Cassini pour Fibonacci, son analogue pour Pell) : le triangle entre elles a l'aire ½, la demi-case minimale de la partie XIV. Les écarts changent de signe à chaque pas et se divisent par φ (or) ou par 1 + √2 (argent).
- La récursion d'argent de la partie XVII, T(d) = 2 − 1/(2d), part de 1 et donne 1, 3/2, 5/3, 17/10, 29/17, 99/58, 169/99… : des rapports de nombres de Pell, vers le contact d = 1 + 1/√2 = 1,707107.
- Ce contact, multiplié par √2, est la pente d'argent : (1 + 1/√2)·√2 = 1 + √2 = tan 67,5°. Et T'(d) = 1/(2d²) = 0,171573 = (√2 − 1)² au contact : la récursion avance de deux aiguilles de Pell par pas.

## 8. arccos(1/3) : la zone de confusion et le tétraèdre dans le cube (VI – XXVI)

- Les quatre grandes diagonales du cube font entre elles des angles de cosinus ±0,333333 = ±1/3 : ce sont les axes du tétraèdre régulier inscrit (un sommet sur deux). D'où les écarts 70,53° et 109,47° entre les hexagones du mouvement complet (partie XXVI).
- Dans la partie VI, la corde du triangle (2/√3) coupe la clôture à x = 1/3, donc sous l'angle arccos(1/3) : c'est l'angle qui entre dans l'aire exacte de la zone de confusion.
- En dimension n, le plan de la lentille du simplexe est à 1/(n + 1) du centre (partie I) ; et −1/(n + 1) est le cosinus de l'angle au centre du simplexe régulier de dimension n + 1. La vraie chèvre a cos α_n = x₀, un peu moins : l'écart d'angle est le ménisque.

| n | arccos(1/(n + 1)) | simplexe de dimension n + 1 (angle au centre) | α_n de la chèvre | écart (le ménisque) |
|---:|---|---|---|---|
| 2 | 70,529° | 109,471° | 70,812° | 0,283° |
| 3 | 75,522° | 104,478° | 75,798° | 0,276° |
| 4 | 78,463° | 101,537° | 78,698° | 0,235° |
| 5 | 80,406° | 99,594° | 80,601° | 0,195° |
| 10 | 84,784° | 95,216° | 84,872° | 0,088° |
