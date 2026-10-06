# Résultats de la partie XXIII (générés par scripts/lentilles_boules_grain.py)

## 1. Ce que la partie XXII avait oublié

Trois phrases de la partie XXII contredisaient des acquis des parties précédentes :

| partie XXII | ce qu'on avait posé | où |
|---|---|---|
| « le terme 8/(3n) est mesuré, pas démontré » | r_n² = 2n/(n + 1) + 2/(3n²) + …, dérivé (esquisse) et vérifié jusqu'à n = 10 000 : il donne exactement n·(2 − r²) = 2 − 8/(3n) + … | partie I, § 5.4 |
| « 2/√3 et ρ₂ : une coïncidence, sans plus » | 2/√3 est l'arête du triangle de hauteur R, le simplexe de la dimension 2 ; l'arête √(2n/(n + 1)) du simplexe est le terme principal de la corde dans toutes les dimensions, et l'écart (0,35 % en 2D) est le ménisque. C'est aussi la maille de la grille décalée. En 2D, le rapport trou/rayon de l'hexagonal tombe sur le même 2/√3 (côté/hauteur du triangle équilatéral) ; en 3D, les deux se séparent (√2 pour le trou du cubique à faces centrées, √(3/2) pour le simplexe). | parties V, VI, XV |
| « l'accord se fait dans les dimensions, pas dans les longueurs » | le plan de la lentille (où se coupent le pré et la sphère de la corde) est à x₀ ≈ R/(n + 1) du centre : ½, ⅓, ¼… Avec la corde du simplexe, il passe exactement par son centre de gravité. Une décade de dimension est une décade de longueur. | parties I (§ 5.4) et VI |

**Contrôle du développement de la partie I** (n²·μ_n doit tendre vers 2/3, avec μ_n = r_n² − 2n/(n + 1)) :

| n | 2 | 3 | 4 | 8 | 10 | 24 | 100 | 10³ | 10⁴ | 10⁵ | 10⁶ | 10⁷ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n²·μ_n | 0,0373 | 0,0839 | 0,1284 | 0,2611 | 0,3064 | 0,4644 | 0,6065 | 0,6602 | 0,6660 | 0,6666 | 0,6668 | 0,6661 |

(En 10⁷, la double précision ne suffit plus pour μ ; jusqu'à 10⁶ la limite 2/3 est atteinte à 10⁻⁴ près.)

## 2. Le plan de la lentille : une décade de dimension, une décade de longueur

La zone broutée est une lentille (partie I, § 2.1 et § 6.2). Le pré et la sphère de la corde se coupent dans un plan, à la distance x₀ = R − r²/(2R) du centre. Avec r² = 1 + (n − 1)/(n + 1) + μ (partie XVI), on a exactement x₀ = 1/(n + 1) − μ/2 (pour R = 1).

| n | x₀ (plan de la lentille) | 1/(n + 1) (centre de gravité du simplexe) | μ/2 |
|---:|---|---|---|
| 1 | 5,000000e−01 | 5,000000e−01 | 0 |
| 2 | 3,286742e−01 | 3,333333e−01 | 4,659e−03 |
| 3 | 2,453388e−01 | 2,500000e−01 | 4,661e−03 |
| 4 | 1,959875e−01 | 2,000000e−01 | 4,013e−03 |
| 8 | 1,090711e−01 | 1,111111e−01 | 2,040e−03 |
| 10 | 8,937705e−02 | 9,090909e−02 | 1,532e−03 |
| 24 | 3,959683e−02 | 4,000000e−02 | 4,032e−04 |
| 100 | 9,870666e−03 | 9,900990e−03 | 3,032e−05 |
| 10³ | 9,986709e−04 | 9,990010e−04 | 3,301e−07 |
| 10⁴ | 9,998667e−05 | 9,999000e−05 | 3,330e−09 |
| 10⁵ | 9,999867e−06 | 9,999900e−06 | 3,333e−11 |
| 10⁶ | 9,999987e−07 | 9,999990e−07 | 3,334e−13 |
| 10⁷ | 9,999999e−08 | 9,999999e−08 | 3,331e−15 |

- **Une décade de dimension est une décade de longueur.** En dimension n = 10ᵏ − 1, le plan de la lentille est à 10⁻ᵏ R du centre, à μ/2 ≈ 1/(3n²) près. La partie XXII l'avait écrit en aire (2 − r² ≈ 2/n) ; c'est la même chose en longueur, puisque 2 − r² = 2x₀.
- **Le miroir 49-50-51 de la partie XXI est un miroir de plans.** En dimensions 10⁴⁹ − 1, 10⁵⁰ − 1 et 10⁵¹ − 1, le plan est à 10⁻⁴⁹, 10⁻⁵⁰ et 10⁻⁵¹ R, et x₀·x₀′ = (10⁻⁵⁰)² : la forme de Newton, sur des longueurs.
- **√2 arrive exactement quand le plan atteint le centre.** Le plan coupe alors le pré en deux moitiés : c'est le partage d'aire. C'est la phrase de la partie I (« ce plan glisse vers le centre, et quand il l'atteint, la corde vaut √2 R »), et c'est la tienne : √2 arrive là où les pas de 10 se précipitent vers la dimension infinie.

## 3. Les décimales en deux couches

En dimension n = 10ᵏ, la projection vaut (10ᵏ − 1)/(10ᵏ + 1). Son écriture décimale répète exactement le carré (10ᵏ − 1)², sur 2k chiffres :

| k | n | projection (n − 1)/(n + 1) | se répète | ménisque μ | premier chiffre du ménisque |
|---:|---:|---|---|---|---:|
| 1 | 10¹ | 0,8181… | 81 = 9² | 3,064e−03 | 3 |
| 2 | 10² | 0,98019801… | 9801 = 99² | 6,065e−05 | 5 |
| 3 | 10³ | 0,998001998001… | 998001 = 999² | 6,602e−07 | 7 |
| 4 | 10⁴ | 0,9998000199980001… | 99980001 = 9999² | 6,660e−09 | 9 |
| 5 | 10⁵ | 0,99998000019999800001… | 9999800001 = 99999² | 6,666e−11 | 11 |
| 6 | 10⁶ | 0,999998000001999998000001… | 999998000001 = 999999² | 6,668e−13 | 13 |
| 7 | 10⁷ | 0,9999998000000199999980000001… | 99999980000001 = 9999999² | 6,661e−15 | 15 |
| 8 | 10⁸ | 0,99999998000000019999999800000001… | 9999999800000001 = 99999999² | ≈ 2/(3n²) | 17 |

- **La projection est la couche 1** (partie XIX) : un nombre rationnel, la grille décalée (l'arête du simplexe). Ses décimales sont les carrés de 9, 99, 999… : 9/11 = 0,(81), 99/101 = 0,(9801), 999/1001 = 0,(998001).
- **Le ménisque est la couche 2** : la division d'intégrales complexes (transcendante en dimension paire, partie I § 5.5). Il vaut ≈ 2/(3n²) et commence exactement au chiffre 2k + 1, juste après le premier carré.
- **Il entre par une retenue.** En 100D : 1,9801 9801 98… + 0,0000 6064 85… = 1,9802 5866 83… : le 1 devient 2. En 1000D : 1,998001 998… + 0,000000 660… = 1,998002 658… Les retenues de la partie XIX sont la frontière exacte entre les deux couches.

## 4. Les boules et le grain grossier

**Ce qu'on avait posé.**
- **Partie I, § 5.2.** La coquille d'épaisseur 0,1 R contient 1 − 0,9ⁿ du volume (65 % en 10D) ; la tranche |x₁| < 0,1 R autour d'un équateur en contient 25 % en 10D, 69 % en 100D et 99,8 % en 1000D (recalculé : 25,5 %, 68,5 %, 99,8 %).
- **Partie I, § 5.3.** La corde est la distance médiane ; |X − P|² ≈ 2 parce que |X| ≈ 1 (la coquille) et X·P ≈ 0 (l'équateur). La fraction broutée par √2 converge en 1/√n (l'équateur), la corde en 1/n (la coquille).
- **Partie XV.** Comptée sur une grille grossière, la chèvre se confond avec son simplexe ; il faut quelques milliers de points en 2D pour voir le ménisque.
- **Partie XVIII.** Le grain grossier honnête : chaque niveau décimal du grain donne un chiffre certain de la corde. L'aire converge sous le grain, la longueur jamais (« π = 4 »).
- **Partie X.** Sous le flou, un point, un disque et un carré se confondent ; l'écart décroît comme la taille², puis taille⁴ quand le carré a le bon côté (√3 fois le rayon).

**Quatre taux de change entre le grain ε (une longueur, R = 1) et la dimension.** Ce sont les dimensions à partir desquelles le grain ne distingue plus :

| grain ε | la sphère de son équateur (tranche \|x₁\| < ε : la moitié) | la boule de sa coquille (épaisseur ε : la moitié) | le plan de la lentille du centre (x₀ < ε) | la chèvre de son simplexe (μ/2 < ε) |
|---|---|---|---|---|
| 10⁻¹ | 44,76 | 6,579 | 10¹ − 1 | — |
| 10⁻² | 4549 | 68,97 | 10² − 1 | — |
| 10⁻³ | 4,55·10⁵ | 692,8 | 10³ − 1 | 13,52 |
| 10⁻⁴ | 4,55·10⁷ | 6931 | 10⁴ − 1 | 52,93 |
| 10⁻⁵ | 4,55·10⁹ | 6,93·10⁴ | 10⁵ − 1 | 177,7 |
| 10⁻⁶ | 4,55·10¹¹ | 6,93·10⁵ | 10⁶ − 1 | 572,5 |
| loi | ≈ 0,455/ε² | ≈ ln 2/ε = 0,693/ε | 1/ε − 1 | ≈ 1/√(3ε) = 0,577/√ε |
| **10⁻⁵⁰** | **≈ 0,45·10¹⁰⁰** | **≈ 0,69·10⁵⁰** | **10⁵⁰** | **≈ 0,58·10²⁵** |

- **Les puissances et leurs racines.** À un même grain, l'équateur demande ε⁻², la coquille et le plan ε⁻¹, le ménisque ε^(−1/2). Pour ton 10⁻⁵⁰ : 10¹⁰⁰, 10⁵⁰ et 10²⁵, le carré, le nombre et la racine.
- **Ce qu'on voit de la chèvre à un grain donné** (figure, panneau d) : au-dessous de n ≈ 0,58/√ε, le ménisque (la chèvre diffère de son simplexe) ; entre les deux, le simplexe seul, le plan encore hors du centre ; au-delà de n ≈ 1/ε, le plan est au centre à un grain près, et la chèvre est la chèvre infinie, √2.
- La chèvre suit la coquille, pas l'équateur : sa corde converge en 1/n parce que la médiane ne voit que le décalage moyen de la coquille (1/n), pas les fluctuations symétriques de l'équateur (1/√n) — l'esquisse de la partie I.

## 5. Le carré de neuf points relu

**Il était déjà là, trois fois.**
- **Partie I, § 6.4 : un cran.** « Un cran sépare le cercle tangent aux côtés et le cercle qui passe par les coins » : les cercles inscrit et circonscrit d'un carré ont des aires dans le rapport 2. Les distances 1 et √2 du carré de neuf points sont un cran de diaphragme.
- **Partie X : les centres fantômes.** Des pixels carrés replient les anneaux et font apparaître 8 nouveaux centres : 4 aux points cardinaux, 4 sur les diagonales. Avec le vrai centre, ce sont les neuf points, créés par le grain grossier lui-même. Des pixels hexagonaux en donnent 6, sur un hexagone.
- **Partie XV : la grille carrée et la grille décalée.** La grille carrée n'offre que 1 et √2 autour du piquet (14 % et 22 % de la corde) ; la grille décalée d'une demi-maille offre l'arête du simplexe, 2/√3 en 2D, √(3/2) en 3D (le cubique à faces centrées), √(2n/(n + 1)) en dimension n. C'est le réseau A_n : la grille carrée d'une dimension de plus, coupée en diagonale.

**Toutes les dimensions tiennent dans un seul cran.** De la dimension 1 (corde 1) à l'infini (corde √2), l'aire du disque de la corde passe de 1 à 2 fois celle du pré : exactement un cran. Chaque dimension en parcourt une part, log₂ r_n² :

| n | arête du simplexe √(2n/(n + 1)) | corde r_n | ménisque μ_n | part du cran log₂ r_n² |
|---:|---|---|---|---|
| 1 | 1,000000 | 1,000000 | 0 | 0,000000 |
| 2 | 1,154701 | 1,158728 | 9,32e−03 | 0,425085 |
| 3 | 1,224745 | 1,228545 | 9,32e−03 | 0,593901 |
| 4 | 1,264911 | 1,268079 | 8,03e−03 | 0,685290 |
| 8 | 1,333333 | 1,334862 | 4,08e−03 | 0,833382 |
| 10 | 1,348400 | 1,349535 | 3,06e−03 | 0,864926 |
| 24 | 1,385641 | 1,385932 | 8,06e−04 | 0,941712 |
| 100 | 1,407195 | 1,407217 | 6,06e−05 | 0,985689 |
| 10³ | 1,413507 | 1,413507 | 6,60e−07 | 0,998559 |
| 10⁶ | 1,414213 | 1,414213 | 6,67e−13 | 0,999999 |
| ∞ | √2 | √2 | 0 | 1 |

- La part qui manque au cran vaut ≈ 1/((n + 1)·ln 2) = 1,44/(n + 1) : une décade de dimension divise par 10 ce qui manque au cran.
- Le complément des neuf points se fait donc en deux couches : la grille décalée (l'arête du simplexe, couche 1), puis le ménisque (la division d'intégrales, couche 2).

## 6. 24D relu

- **Le terme principal a le 5² des boulets pour dénominateur** : 2n/(n + 1) = 48/25, donc l'arête du simplexe vaut √48/5 = 4√3/5 = 1,3856406461 (partie XXI : 24 + 1 = 5²).
- La corde certifiée vaut 1,3859315750 : le ménisque est μ₂₄ = 8,063e−04 (n²·μ = 0,464, en route vers 2/3).
- La projection vaut 23/25 ; le plan de la lentille est à 1/25 − μ/2 = 0,03960 R du centre ; et κ₂₄·h₂₅ = 1/25 aussi (parties VII et XXI). Le même 1/(n + 1) : le centre de gravité du simplexe d'un côté, la réciprocité de Wallis de l'autre.
- La 24D a parcouru 0,9417 du cran.
