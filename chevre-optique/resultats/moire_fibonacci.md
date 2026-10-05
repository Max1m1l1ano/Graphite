# Résultats de la partie IX (générés par scripts/moire_fibonacci.py)

## 1. Où apparaissent les nouveaux centres

Une composante cos(2πu·r²/R²) des anneaux, échantillonnée sur la grille des pixels, prend aux pixels exactement les mêmes valeurs qu'un motif identique centré en (m, n)·R²/(2u) pixels : u·(x² − (x − x_m)²)/R² diffère d'un entier quand x est entier. En unités du rayon a du disque : x_m/a = m·R/(2u).
Contrôle de l'identité sur 801 pixels : écart maximal 8.1e-12.

Diaphragme de Fibonacci à 55 anneaux : composantes principales u₁ = 21,0840 et u₂ = 33,9160 (ses deux foyers, partie VIII), rapport 1,608612. Lame de Fresnel ordinaire à 55 zones : u = 27,5.

| rayon R (pixels) | famille u₂ (axes) | famille u₁ (axes) | u₂, diagonales | u₁, diagonales | Fresnel (axes) |
|---:|---|---|---|---|---|
| 30 | 0,442 a | 0,711 a | 0,625 a | 1,006 a (dehors) | 0,545 a |
| 36 | 0,531 a | 0,854 a | 0,751 a | 1,207 a (dehors) | 0,655 a |
| 45 | 0,663 a | 1,067 a (dehors) | 0,938 a | 1,509 a (dehors) | 0,818 a |
| 60 | 0,885 a | 1,423 a (dehors) | 1,251 a (dehors) | 2,012 a (dehors) | 1,091 a (dehors) |
| 80 | 1,179 a (dehors) | 1,897 a (dehors) | 1,668 a (dehors) | 2,683 a (dehors) | 1,455 a (dehors) |
| 100 | 1,474 a (dehors) | 2,371 a (dehors) | 2,085 a (dehors) | 3,354 a (dehors) | 1,818 a (dehors) |

Une famille sort du disque quand R dépasse 2u (axes) ou √2·u (diagonales) : u₂ sort à R = 67,8 px, u₁ à R = 42,2 px. Le rapport des deux seuils vaut u₂/u₁ → φ.
Les deux familles vérifient l'équation des lentilles : 1/x₁ + 1/x₂ = 2(u₁ + u₂)/R = 2N/R = 2/x_F, où x_F = R/N est la famille de la lame de Fresnel ordinaire.

## 2. Mesure des centres sur les images échantillonnées

Filtre adapté le long de l'axe (image adoucie par un flou gaussien d'un pixel) ; on garde le centre détecté le plus proche de chaque prédiction, à 1,5 pixel près.

| anneaux | R (px) | famille | centre prédit (px) | centre mesuré (px) | écart (px) |
|---:|---:|---|---:|---:|---:|
| 55 | 30 | u₂ | 13,3 | 13,7 | +0,4 |
| 55 | 30 | u₁ | 21,3 | 21,5 | +0,2 |
| 55 | 36 | u₂ | 19,1 | non trouvé |  |
| 55 | 36 | u₁ | 30,7 | 30,2 | −0,5 |
| 55 | 40 | u₂ | 23,6 | 23,3 | −0,3 |
| 55 | 40 | u₁ | 37,9 | 36,9 | −1,0 |
| 55 | 44 | u₂ | 28,5 | non trouvé |  |
| 55 | 50 | u₂ | 36,9 | non trouvé |  |
| 55 | 56 | u₂ | 46,2 | 46,3 | +0,1 |
| 55 | 60 | u₂ | 53,1 | 54,0 | +0,9 |
| 55 | 64 | u₂ | 60,4 | non trouvé |  |
| 144 | 90 | u₂ | 45,5 | 45,6 | +0,1 |
| 144 | 90 | u₁ | 73,6 | 73,5 | −0,1 |
| 144 | 100 | u₂ | 56,2 | 56,4 | +0,2 |
| 144 | 100 | u₁ | 90,9 | 91,1 | +0,2 |
| 144 | 110 | u₂ | 68,0 | 67,9 | −0,1 |
| 144 | 120 | u₂ | 80,9 | 80,9 | −0,0 |
| 144 | 130 | u₂ | 95,0 | 95,0 | +0,0 |

14 centres retrouvés ; écart moyen 0,30 px, écart maximal 1,04 px.

## 3. L'équation d'optique, φ et Fermat

Distances focales de la lentille de Fibonacci, en unités de z_N = a²/(2λN), la moitié du foyer de la lame de Fresnel ordinaire :

| anneaux N | z₁ (foyer lointain) | z₂ (foyer proche) | 1/z₁ + 1/z₂ | grandissement −z₁/z₂ |
|---:|---|---|---|---|
| 55 | 2,608612 | 1,621654 | 1,000000 | −1,608612 |
| 89 | 2,618211 | 1,617966 | 1,000000 | −1,618211 |
| 144 | 2,616647 | 1,618564 | 1,000000 | −1,616647 |
| 233 | 2,618057 | 1,618025 | 1,000000 | −1,618057 |
| 377 | 2,617832 | 1,618111 | 1,000000 | −1,617832 |
| 610 | 2,618037 | 1,618033 | 1,000000 | −1,618037 |

Limites : φ² = 2,618034 et φ = 1,618034 ; 1/φ² + 1/φ = 1,000000000000.
Une lentille de focale 1 forme l'image d'un objet placé à φ à la distance φ², retournée et agrandie φ fois.

Solutions entières de 1/aⁿ + 1/bⁿ = 1/cⁿ (a ≤ b ≤ 300) :
- n = 1 : 397 solutions, dont 63 primitives ; premières : [(2, 2, 1), (3, 6, 2), (4, 12, 3), (5, 20, 4), (6, 30, 5)]
- n = 2 : 17 solutions, dont 3 primitives ; premières : [(15, 20, 12), (65, 156, 60), (136, 255, 120)]
- n = 3 : 0 solutions, dont 0 primitives ; premières : []

## 4. Les racines de l'unité, le pentagone et la chèvre

(−1)^(1/5) = e^(iπ/5) = (1 + √5)/4 + i·√(5/8 − √5/8) : écart 0.0e+00.
Racines dixièmes de l'unité autres que ±1 (huit) : parties réelles ±φ/2 = ±0,8090 et ±1/(2φ) = ±0,3090.

| corde | r | α = arccos(r/2) | β = 2α | part broutée |
|---|---|---|---|---|
| triangle (simplexe) | 1,154701 | 54,7356° | 109,4712° | 49,717 % |
| chèvre | 1,158728 | 54,5942° | 109,1883° | 50,000 % |
| pentagone | 1,175571 | 54,0000° | 108,0000° | 51,186 % |

Pentagone : r² = 4 sin²36° = 3 − φ = 1,381966 ; part broutée exacte (13 − 3φ)/10 − sin 72°/π = 51,186 %.

## 5. φ, le nombre le plus mal approché par des fractions (Hurwitz)

| fraction p/q | q²·|x − p/q| |
|---|---|
| φ ≈ 8/5 | 0,450850 |
| φ ≈ 34/21 | 0,447011 |
| φ ≈ 144/89 | 0,447225 |
| φ ≈ 987/610 | 0,447214 |
| π ≈ 22/7 | 0,061960 |
| π ≈ 333/106 | 0,935056 |
| π ≈ 355/113 | 0,003406 |

Pour φ, la valeur tend vers 1/√5 = 0,447214 : aucune fraction ne fait mieux à long terme (théorème de Hurwitz, 1891).
