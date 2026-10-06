# Résultats de la partie XXII (générés par scripts/carre_neuf_points.py)

## 1. Les pas de 10 se précipitent vers √2

La corde ρ_n est calculée pour toute dimension par une intégrale exacte sur le rayon : un point X de la boule s'écrit X = r·U, avec rⁿ uniforme et U uniforme sur la sphère, et la chèvre broute X quand U₁ ≥ (r² + 1 − ρ²)/(2r). Contrôle : on retrouve les cordes certifiées de la partie XX (dimensions 2, 3, 4, 8 et 24) à 10⁻¹³ près.

| n | ρ_n | ρ_n² (aire du disque de la corde / aire du pré) | 2 − ρ_n² | n·(2 − ρ_n²) | α_n |
|---:|---|---|---|---|---|
| 1 | 1,0000000000 | 1,0000000000 | 1,000e+00 | 1,000000 | 60,0000° |
| 2 | 1,1587284730 | 1,3426516742 | 6,573e−01 | 1,314697 | 70,8117° |
| 3 | 1,2285448637 | 1,5093224822 | 4,907e−01 | 1,472033 | 75,7981° |
| 4 | 1,2680792567 | 1,6080250012 | 3,920e−01 | 1,567900 | 78,6976° |
| 8 | 1,3348624292 | 1,7818577048 | 2,181e−01 | 1,745138 | 83,7382° |
| 10 | 1,3495354400 | 1,8212459038 | 1,788e−01 | 1,787541 | 84,8722° |
| 24 | 1,3859315750 | 1,9208063306 | 7,919e−02 | 1,900648 | 87,7307° |
| 100 | 1,4072166387 | 1,9802586683 | 1,974e−02 | 1,974133 | 89,4344° |

**Les décades de dimension.**

| n | ρ_n² | 2 − ρ_n² | n·(2 − ρ_n²) |
|---:|---|---|---|
| 10¹ | 1,821245903811747 | 1,7875e−01 | 1,7875409619 |
| 10² | 1,980258668277163 | 1,9741e−02 | 1,9741331723 |
| 10³ | 1,998002658191559 | 1,9973e−03 | 1,9973418084 |
| 10⁴ | 1,999800026658139 | 1,9997e−04 | 1,9997334186 |
| 10⁵ | 1,999980000266658 | 2,0000e−05 | 1,9999733342 |
| 10⁶ | 1,999998000002667 | 2,0000e−06 | 1,9999973334 |
| 10⁷ | 1,999999800000027 | 2,0000e−07 | 1,9999997336 |

(En 10⁸, ρ² = 1,99999998 ; le terme suivant n'est plus lisible en double précision.)

- Chaque facteur 10 sur la dimension ajoute un 9 (et un 0) à ρ² : 1,82…, 1,980…, 1,998 0…, 1,999 800 0…, 1,999 980 000 3… Les décades de dimension sont les décimales de l'approche de 2.
- n·(2 − ρ_n²) → 2 (partie XX), et le calcul donne n·(2 − ρ_n²) = 2 − 8/(3n) + … (n·(t_n − 1) vaut −1,33291, −1,33329, −1,33329 en 10⁴, 10⁵, 10⁶ ; −4/3 = −1,33333). Donc 2 − ρ_n² ≈ 2/n. C'est le développement r_n² = 2n/(n + 1) + 2/(3n²) de la partie I (§ 5.4).
- ρ² est le rapport entre l'aire du disque de la corde et celle du pré (dans le plan méridien, la projection de la partie XX). Le doublement de l'aire, ρ² = 2, n'arrive qu'en dimension infinie.
- Les trois cercles de rayons 1/√2 (la moitié du pré), 1 (le pré) et √2 (la corde infinie) ont des aires ½, 1 et 2 : trois diaphragmes de suite.
- **Ton 10⁻⁵⁰ y a une place précise.** 2 − ρ_n² = 10⁻⁵⁰ en n ≈ 2·10⁵⁰ ; de même 10⁻⁴⁹ en 2·10⁴⁹ et 10⁻⁵¹ en 2·10⁵¹ (correction relative 4/(3n), négligeable). Le miroir 49-50-51 de la partie XXI est une échelle de dimensions : chaque cran de 10 sur la précision est un cran de 10 sur la dimension.
- *Corrigé dans la partie XXIII :* l'accord se fait aussi dans les longueurs. Le plan de la lentille est à R/(n + 1) du centre (parties I et VI) : en dimension 10ᵏ − 1, il est à 10⁻ᵏ R.

## 2. Le carré de neuf points

Le carré [−1, 1]² : quatre sommets (±1, ±1), quatre milieux d'arêtes (±1, 0), (0, ±1), et le centre. Vu du centre : 0, 1 (les milieux) et √2 (les sommets). Le pré est le cercle inscrit, de rayon 1 ; le piquet est le milieu (1, 0).

| distance au piquet (1, 0) | points |
|---|---|
| 1 | (1, 1), (0, 0), (1, −1) |
| √2 | (0, 1), (0, −1) |
| 2 | (−1, 0) |
| √5 | (−1, 1), (−1, −1) |

**Les chèvres remplissent l'écart entre 1 et √2.** Le carré ne donne que deux distances autour du piquet, 1 et √2. Les cordes de toutes les dimensions remplissent l'intervalle entre les deux :
- n = 1 : ρ₁ = 1 exactement. La chèvre de la droite (le pré est le diamètre [−1, 1]) broute la moitié en allant jusqu'au centre ; son cercle passe par le centre et par les deux coins (1, ±1).
- n = 2 : ρ₂ = 1,1587284730…, la division d'intégrales complexes d'Ullisch ; n = 3 : 1,2285448637… ; n = 24 : 1,3859315750…
- n → ∞ : ρ → √2. La corde atteint les deux milieux voisins (0, ±1) : le croisement.
- Les cordes croissent avec la dimension (vérifié de 1 à 30, puis 100 et les décades jusqu'à 10⁸).

**Les 3ⁿ points du cube.** En dimension n, les points à coordonnées dans {−1, 0, 1} sont les centres des faces du cube (le cube lui-même compris) : 3ⁿ points, dont C(n, k)·2ᵏ à la distance √k du centre.

| n | distances 0, 1, √2, √3… | total 3ⁿ | 3ⁿ modulo 10 |
|---:|---|---:|---|
| 1 | 1, 2 | 3 | 3 = i |
| 2 | 1, 4, 4 | 9 | 9 = −1 |
| 3 | 1, 6, 12, 8 | 27 | 7 = −i |
| 4 | 1, 8, 24, 32, 16 | 81 | 1 |
| 5 | 1, 10, 40, 80, 80, 32 | 243 | 3 = i |
| 6 | 1, 12, 60, 160, 240, 192, 64 | 729 | 9 = −1 |
| 7 | 1, 14, 84, 280, 560, 672, 448, 128 | 2187 | 7 = −i |
| 8 | 1, 16, 112, 448, 1120, 1792, 1792, 1024, 256 | 6561 | 1 |

- Le carré de neuf points est la ligne n = 2 : 1 centre, 4 milieux, 4 sommets.
- 3 est i modulo 10 (partie XIX) : 3² = 9 ≡ −1. Chaque dimension multiplie le nombre de points par 3, donc les fait tourner d'un quart de tour modulo 10 : 3, 9, 7, 1.
- Comme empilement : des sphères de rayon 1 centrées aux sommets se touchent aux milieux des arêtes, et le centre est le trou le plus profond, à √2. Le rapport entre le trou et le rayon vaut √2 (§ 4).
- Les quatre petits carrés ont leurs centres (±½, ±½) sur le cercle de rayon 1/√2, celui de la moitié du pré.

## 3. Les faisceaux

**En 2D.** Quatre chèvres, une à chaque milieu. Chacune broute sur la clôture un arc de ±α₂ = ±70,81° autour de son piquet. Comme 70,81° > 45°, les quatre arcs couvrent le cercle. Les arcs voisins se recouvrent autour des directions des sommets ; les arcs opposés ne se touchent jamais. Le nerf (qui recouvre qui) est un carré, un cycle de 4 : il calcule la cohomologie du cercle (H⁰ = H¹ = ℤ).

**En dimension n.** 2n chèvres aux ±e_i, les sommets du polytope croisé (les milieux des faces du cube). C'est un bon recouvrement de la clôture S^(n−1) dès que arccos(1/√n) < α_n < 90° :
- si α_n > arccos(1/√n), un groupe de chèvres sans paire opposée a toujours un point commun, au besoin dans la direction d'un sommet du cube ;
- si α_n < 90°, deux chèvres opposées ne se touchent pas ;
- les calottes de moins de 90° sont convexes, donc leurs intersections sont contractiles.

| n | α_n | seuil arccos(1/√n) | chèvres | nerf : sommets, arêtes, triangles… | nombres de Betti |
|---:|---|---|---:|---|---|
| 2 | 70,81° | 45,00° | 4 | 4, 4 | 1, 1 |
| 3 | 75,80° | 54,74° | 6 | 6, 12, 8 | 1, 0, 1 |
| 4 | 78,70° | 60,00° | 8 | 8, 24, 32, 16 | 1, 0, 0, 1 |
| 5 | 80,60° | 63,43° | 10 | 10, 40, 80, 80, 32 | 1, 0, 0, 0, 1 |
| 8 | 83,74° | 69,30° | 16 | C(n, k)·2ᵏ | sphère S⁷ |
| 24 | 87,73° | 78,22° | 48 | C(n, k)·2ᵏ | sphère S²³ |
| 100 | 89,43° | 84,26° | 200 | C(n, k)·2ᵏ | sphère S⁹⁹ |

- Le nerf est le bord du polytope croisé, une sphère S^(n−1) : la condition est vérifiée pour toutes les dimensions calculées (2 à 30, 100, et les décades jusqu'à 10⁸), car 90° − α_n ≈ 1/(n + 1) radian alors que 90° − arccos(1/√n) ≈ 1/√n.
- Les nombres de Betti sont vérifiés de 2 à 5 (rang des bords modulo un nombre premier) : 1, 0, …, 0, 1, ceux de la sphère.
- **Les sommets du cube sont les endroits où n chèvres se recouvrent** : dans la direction (±1, …, ±1)/√n, les n chèvres d'un même signe broutent ensemble. Sur un piquet, une seule.

| n | chèvres | au moins (sur un piquet) | au plus (vers un sommet du cube) | en moyenne (2·10⁵ points au hasard) | le moins brouté des points tirés |
|---:|---:|---:|---:|---|---:|
| 2 | 4 | 1 | 2 | 1,57 | 1 |
| 3 | 6 | 1 | 3 | 2,27 | 1 |
| 4 | 8 | 1 | 4 | 3,00 | 1 |
| 8 | 16 | 1 | 8 | 6,24 | 1 |
| 24 | 48 | 1 | 24 | 20,42 | 12 |
| 100 | 200 | 1 | 100 | 92,20 | 79 |

- En grande dimension, un point au hasard est loin des piquets : en 24D, aucun des 200 000 points tirés n'est brouté par moins de 12 chèvres.

**À l'infini, le recouvrement cesse d'être bon.** En α = 90°, les arcs sont des demi-cercles fermés et les chèvres opposées se touchent : en 2D, Est et Ouest se rencontrent en 90° et 270°, deux points séparés. Le nerf devient le bord d'un tétraèdre, de nombres de Betti 1, 0, 1, 0 : une sphère S² au lieu du cercle. Le croisement est exactement l'endroit où le calcul des faisceaux casse.

## 4. 24 pour la sphère 24D

**La chèvre 24D.** ρ₂₄ = 1,385931575001… (certifiée à 50 chiffres dans la partie XX), α₂₄ = 87,731°. Ses 48 piquets ±e_i couvrent la clôture S²³ (seuil arccos(1/√24) = 78,22°). Le nerf est le bord du polytope croisé de dimension 24 : 48 sommets, 1104 arêtes, …, 2²⁴ = 16 777 216 facettes, de caractéristique d'Euler 0, celle de S²³. Un point au hasard de la clôture est brouté par 20,4 chèvres en moyenne.
- Les 48 piquets sont aussi les 48 points où une sphère de ℤ²⁴ touche ses voisines (les centres des faces du cube).

**Le réseau de Leech garde le √2 du carré.** Ses sphères ont un rayon de 1 (vecteurs minimaux de norme 4), et le point de l'espace le plus éloigné du réseau est à √2 : le rayon de recouvrement vaut √2 (Conway, Parker et Sloane, 1982). Les trous les plus profonds forment 23 familles, une par réseau de Niemeier. C'est exactement le rapport du carré de neuf points : milieux (contacts) à 1, centre (trou) à √2.

| réseau | dimension | rayon des sphères | trou le plus profond | rapport | contrôle |
|---|---:|---|---|---|---|
| ℤ (la droite) | 1 | ½ | ½ | 1 | exact |
| ℤ² (le carré de neuf points) | 2 | ½ | √2/2 | √2 | trou en (½, ½) ; le plus loin trouvé par tirage : 0,70708 |
| D₃ = cubique à faces centrées (record en 3D) | 3 | √2/2 | 1 | √2 | trou en (1, 0, 0) ; le plus loin trouvé par tirage : 0,99991 |
| D₄ | 4 | √2/2 | 1 | √2 | trou en (1, 0, 0, 0) et (½, ½, ½, ½) ; le plus loin trouvé par tirage : 0,99985 |
| E₈ (record en 8D) | 8 | √2/2 | 1 | √2 | trou en (1, 0, …, 0) ; le plus loin trouvé par tirage : 0,99914 |
| A₂ = hexagonal (record en 2D) | 2 | ½ | 1/√3 = 0,5774 | 2/√3 = 1,1547 | exact |
| Λ₂₄ = Leech (record en 24D) | 24 | 1 | √2 | √2 | Conway, Parker et Sloane (1982) |
| ℤ²⁴ | 24 | ½ | √24/2 | √24 = 4,8990 | exact |

- **En 3, 8 et 24**, trois des cinq dimensions où l'empilement record est démontré (1, 2, 3, 8, 24), le trou le plus profond est à √2 fois le rayon des sphères : le rapport du carré de neuf points. En 2D, le record (hexagonal) a 2/√3 ; le carré, lui, a √2.
- **Dans ℤ²⁴**, le centre du cube est à √24 fois le rayon. Leech ramène ce rapport au √2 du carré, comme E₈ le fait en 8D en remplissant les trous de D₈ (partie XX).
- **Les contacts.** Une sphère de ℤ²⁴ en touche 48 (les piquets des chèvres), une sphère de Leech 196 560 (partie XXI).
- 2/√3 = 1,15470 (l'hexagonal) et ρ₂ = 1,15873 (la chèvre plane) diffèrent de 0,35 %. *Corrigé dans la partie XXIII :* ce n'est pas une coïncidence. 2/√3 est l'arête du triangle de hauteur R, le simplexe de la 2D, terme principal de la corde (parties V et VI) et maille de la grille décalée (partie XV) ; l'écart est le ménisque. En 2D, le rapport trou/rayon de l'hexagonal tombe sur le même 2/√3 (côté/hauteur du triangle équilatéral) ; en 3D les deux se séparent (√2 et √(3/2)).
