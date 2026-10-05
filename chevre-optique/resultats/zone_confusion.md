# Résultats de la partie VI (générés par scripts/zone_confusion.py)

## 1. La zone entre les deux cercles, dans le pré (R = 1)

- corde de la chèvre r₂ = 1,15872847301812 ; côté du triangle 2/√3 = 1,15470053837925 ; écart 0,00402793 (0,3476 %)
- aire de la zone (dans le pré, entre les deux cercles) = π/2 − lentille(2/√3) = 0,00889046020350627
- forme close : (2√2 − arccos(1/3))/3 − π/6 = 0,00889046020350627
- part du pré : 0,28299214 % ; part de la moitié visée : 0,56598428 %
- corde commune avec la corde 2/√3 : x = 1/3 (centre de gravité du triangle), longueur 4√2/3 = 1,885618083
- corde commune de la chèvre : x = 1 − r₂²/2 = 0,3286741629

## 2. Déplacer le cercle du triangle vers O

- déplacement qui donne exactement la moitié : δ = 0,00471211065508 R (premier ordre : aire / corde = 0,0047148785)
- les deux cercles se croisent en (0,00887887 ; ±0,600275), dans le pré
- croissant gagné (au milieu) = 0,00057284909 ; croissants perdus (aux deux bouts) = 0,00057284895 ; écart 1.4e-10 (précision de l'intégration)
- épaisseur maximale : +0,000684176 au milieu ; −0,00402793 sans déplacement

## 3. En dimension n : le simplexe régulier de sommet P et de hauteur R

| n | arête du simplexe √(2n/(n+1)) | corde de la chèvre r_n | écart | n²(r_n² − arête²) | part manquante | déplacement δ_n |
|---:|---|---|---|---|---|---|
| 2 | 1,1547005 | 1,1587285 | 0,004028 | 0,03727 | 0,283 % | 0,00471211 |
| 3 | 1,2247449 | 1,2285449 | 0,0038 | 0,0839 | 0,3316 % | 0,00471216 |
| 4 | 1,2649111 | 1,2680793 | 0,003168 | 0,1284 | 0,3237 % | 0,00404961 |
| 5 | 1,2909944 | 1,293598 | 0,002604 | 0,1682 | 0,3007 % | 0,00339046 |
| 6 | 1,3093073 | 1,3114618 | 0,002154 | 0,2033 | 0,2751 % | 0,00284139 |
| 7 | 1,3228757 | 1,3246796 | 0,001804 | 0,234 | 0,2507 % | 0,00240109 |
| 8 | 1,3333333 | 1,3348624 | 0,001529 | 0,2611 | 0,2286 % | 0,00204947 |
| 9 | 1,3416408 | 1,3429518 | 0,001311 | 0,2851 | 0,209 % | 0,00176686 |
| 10 | 1,3483997 | 1,3495354 | 0,001136 | 0,3064 | 0,1917 % | 0,00153743 |
| 11 | 1,3540064 | 1,3549994 | 0,000993 | 0,3255 | 0,1764 % | 0,00134917 |
| 12 | 1,3587324 | 1,3596078 | 0,0008754 | 0,3427 | 0,163 % | 0,00119305 |
| 15 | 1,3693064 | 1,3699313 | 0,0006249 | 0,3851 | 0,1311 % | 0,000857559 |
| 20 | 1,3801311 | 1,3805255 | 0,0003944 | 0,4355 | 0,0964 % | 0,000545125 |

n = 100 : n²(r_n² − 2n/(n+1)) = 0,606485 (limite 2/3)

n = 400 : n²(r_n² − 2n/(n+1)) = 0,650679 (limite 2/3)

3D exact : part manquante = (59 − 24√6)/64 = 0,00331634645631
δ₂ = 0,00471211065508 ; δ₃ = 0,00471215705085 (écart relatif 9.8e-6)
Avec la corde du simplexe, les deux sphères se coupent sur l'hyperplan x = 1 − n/(n+1) = 1/(n+1), qui passe par le centre de gravité du simplexe.

## 3 bis. En dimension réelle n (fonction bêta incomplète)

Contrôle contre la formule des dimensions entières : écart max 0.0
En dimension 1 : corde de la chèvre = arête = 1 (moitié d'un segment), donc tous les écarts sont nuls.

| n | écart des cordes | déplacement δ | part manquante |
|---:|---|---|---|
| 1,25 | 0,00213278 | 0,0022637 | 0,00118301 |
| 1,5 | 0,00323904 | 0,00358552 | 0,00196418 |
| 2 | 0,00402793 | 0,00471211 | 0,00282992 |
| 2,25 | 0,00408674 | 0,00487303 | 0,00305517 |
| 2,5 | 0,0040417 | 0,00489464 | 0,0031963 |
| 3 | 0,00379999 | 0,00471216 | 0,00331635 |
| 4 | 0,00316819 | 0,00404961 | 0,00323651 |
| 6 | 0,00215448 | 0,00284139 | 0,00275124 |
| 10 | 0,00113572 | 0,00153743 | 0,00191679 |
- sommet de « écart des cordes r − arête » en n = 2,24381, valeur 0,00408677
- sommet de « déplacement δ » en n = 2,42216, valeur 0,0048992
- sommet de « part manquante » en n = 3,19953, valeur 0,00332457
- la courbe δ(n) repasse au niveau de δ₂ en n = 3,0000853 : à 8.5e-5 de la dimension 3

## 4. π − 3

- Nilakantha avec les cônes c_n = 1/n : 4(c₂c₃c₄ − c₄c₅c₆ + …) = 0,14159265358979323846
- retenues de l'hexagone (partie IV) : 1/8 + 9/640 + 15/7168 + … = 0,14159265358979323846
- π − 3 = 0,14159265358979323846

Test : formules p·C/q (p ≤ 10, q ≤ 1000, 12 constantes C) à moins de 0,1 % de la cible

| cible | valeur | formules à moins de 0,1 % | les trois meilleures | avec π − 3 |
|---|---|---:|---|---|
| part manquante (0,283 %) | 0,00282992 | 16 | √3/612 (0,008 %) ; γ/204 (0,015 %) ; √5/790 (0,019 %) | (π − 3)/50 (0,068 %) |
| écart des cordes | 0,00402793 | 26 | √3/430 (0,002 %) ; π/780 (0,006 %) ; 4/993 (0,007 %) | 7·(π − 3)/246 (0,028 %) ; 6·(π − 3)/211 (0,040 %) |
| déplacement δ | 0,00471211 | 23 | 2·γ/245 (0,003 %) ; 2·√5/949 (0,008 %) ; 4/849 (0,015 %) | aucune |
| aire de la zone | 0,00889046 | 33 | φ/182 (0,002 %) ; ρ/149 (0,003 %) ; 2·√5/503 (0,005 %) | aucune |

## 5. La lunule d'Hippocrate

- grand cercle de rayon 1, petit cercle de rayon 1/√2 (rapport √2) : aire de la lunule = 0,5 = aire du triangle (1/2)
