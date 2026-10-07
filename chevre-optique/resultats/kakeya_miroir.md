# Résultats de la partie XXVI (générés par scripts/kakeya_miroir.py)

## 1. La surface minimale de Kakeya au grain δ

Le problème au grain δ : N tubes 1 × δ (des parallélogrammes d'aire δ et de largeur δ), un dans chacune des directions jπ/N, espacées de δ au plus. Quelle est l'aire minimale de leur union ?

### 1.1 La somme des croisements

Deux tubes dont les directions font l'angle θ se recouvrent au plus de δ²/sin θ (deux bandes de largeur δ se croisent sur un parallélogramme de cette aire). Pour N directions, la somme vaut :

| N | Σ csc(jπ/N), j = 1 … N − 1 | (2N/π)(ln(2N/π) + γ) | (écart) × N |
|---:|---|---|---|
| 10 | 15,449800 | 15,458516 | −0,08717 |
| 100 | 301,171410 | 301,172282 | −0,08727 |
| 1000 | 4477,593932 | 4477,594019 | −0,08727 |
| 10000 | 59434,652163 | 59434,652172 | −0,08730 |

L'écart vaut −π/(36N) = −0,08727/N : la formule est exacte au terme près, ce qui permet de l'évaluer pour N = π·10⁵⁰.

### 1.2 La borne du bas (Córdoba)

Cauchy–Schwarz donne |∪T| ≥ (Σ|T|)²/‖Σχ_T‖², et ‖Σχ_T‖² = Σ |T ∩ T'| ≤ N·(δ + δ²·Σ csc) ≈ π·(1 + 2γ + 2 ln(2/δ)). D'où, avec Σ|T| = Nδ = π :

    |∪T| ≥ π / (1 + 2γ + 2 ln(2/δ)),   donc   1/|∪T| ≤ 1,1270 + 1,4659·k  pour δ = 10⁻ᵏ.

(constante : (1 + 2γ + 2 ln 2)/π = 1,12705 ; pente : 2 ln 10/π = 1,46587 par décade)

### 1.3 Les constructions : arbres de Perron en tubes

Trois éventails de 60° (tournés de 60°) couvrent toutes les directions ; chacun est un arbre de Perron à 2^k branches (rapports télescopiques de la partie V), et chaque direction reçoit un tube dans sa branche. On calcule l'aire exacte de l'union (1 000 tranches) et on garde le meilleur k.

| δ | N directions | meilleur arbre | aire de l'union (3 éventails) | × ln(1/δ) | borne de Córdoba | construction ÷ borne |
|---|---:|---|---|---|---|---|
| 10⁻¹ | 33 | k = 3 (8 branches) | 1,1791 | 2,715 | 0,3880 | 3,04 |
| 3,2·10⁻² | 102 | k = 4 (16 branches) | 0,8296 | 2,865 | 0,3014 | 2,75 |
| 10⁻² | 315 | k = 5 (32 branches) | 0,6425 | 2,959 | 0,2464 | 2,61 |
| 3,2·10⁻³ | 996 | k = 6 (64 branches) | 0,5166 | 2,974 | 0,2087 | 2,47 |
| 10⁻³ | 3144 | k = 7 (128 branches) | 0,4298 | 2,969 | 0,1810 | 2,37 |
| 3,2·10⁻⁴ | 9936 | k = 9 (512 branches) | 0,3672 | 2,959 | 0,1598 | 2,30 |
| 10⁻⁴ | 31416 | k = 10 (1024 branches) | 0,3180 | 2,928 | 0,1431 | 2,22 |
| 3,2·10⁻⁵ | 99348 | k = 11 (2048 branches) | 0,2813 | 2,915 | 0,1295 | 2,17 |
| 10⁻⁵ | 314160 | k = 13 (8192 branches) | 0,2503 | 2,882 | 0,1183 | 2,12 |

(calcul : 27 s)

Le produit aire × ln(1/δ) reste vers 2,91 de 10⁻² à 10⁻⁵ : l'aire suit 1/ln(1/δ). Si la formule 2/(k + 2) de la partie V tient pour tout k, la famille tend lentement vers 2√3·ln 2 = 2,401 (le débord des tubes devient négligeable).

À δ = 10⁻³, un éventail couvre 0,248 du triangle (la grille de la partie XIV donnait 0,28 pour n = 1024).
Les arbres battent le deltoïde (π/8 = 0,3927) à partir de δ = 3,2·10⁻⁴ seulement.

### 1.4 La tranche 10⁻⁴⁹ – 10⁻⁵⁵

| δ | borne de Córdoba (démontrée) | 1/borne | construction extrapolée (2,40 à 2,91 sur ln(1/δ)) | part du deltoïde |
|---|---|---|---|---|
| 10⁻⁴⁹ | 0,013707 | 72,9547 | 0,0213 – 0,0258 | 3,49 – 6,56 % |
| 10⁻⁵⁰ | 0,013437 | 74,4206 | 0,0209 – 0,0253 | 3,42 – 6,43 % |
| 10⁻⁵¹ | 0,013178 | 75,8865 | 0,0204 – 0,0248 | 3,36 – 6,31 % |
| 10⁻⁵² | 0,012928 | 77,3524 | 0,0201 – 0,0243 | 3,29 – 6,19 % |
| 10⁻⁵³ | 0,012687 | 78,8182 | 0,0197 – 0,0238 | 3,23 – 6,07 % |
| 10⁻⁵⁴ | 0,012456 | 80,2841 | 0,0193 – 0,0234 | 3,17 – 5,96 % |
| 10⁻⁵⁵ | 0,012232 | 81,7500 | 0,0190 – 0,0230 | 3,11 – 5,85 % |

- Miroir harmonique : 1/L(49) + 1/L(51) − 2/L(50) = 0 (exactement : 1/L est affine en k).
- Sur la tranche, la borne ne baisse que de 10,76 % (L(49)/L(55) = 1,1206 ; 55/49 = 1,1224), quand le grain est divisé par 10⁶.
- Pour une aiguille de longueur √3 (la grande diagonale du cube), l'aire se multiplie par 3 : au moins 0,0401 à 10⁻⁵⁰, contre 3π/8 = 1,1781 pour le deltoïde et 3π/4 = 2,3562 pour le disque qu'elle balaie en tournant sur son milieu.

## 2. La virgule du kibi et son miroir

### 2.1 Les nombres exacts

- virgule : c = 2²⁰/10⁶ − 1 = 0,048576 ; 2¹⁰/10³ = 128/125 (le diesis), 2²⁰/10⁶ = (128/125)² = 16384/15625
- miroir : 10⁶/2²⁰ = 5⁶/2¹⁴ = 15625/16384 = 0,95367431640625 (les chiffres de 5²⁰ = 95367431640625)
- 1 − miroir = c/(1 + c) = 0,04632568359375
- écart entre le cran et son miroir : (1 + c) − 1/(1 + c) = 0,09490168359375
- double linéaire : 2c = 0,097152 (les chiffres de 2²¹ = 2097152)
- carré : (1 + c)² − 1 = 2c + c² = 0,099511627776 (2⁴⁰ = 1099511627776, le téra contre le tébi)
- les deux retenues : 2c − écart = c²/(1 + c) = 0,00225031640625 ; carré − 2c = c² = 0,002359627776
- milieu de l'écart et du carré : 0,097206655684875 = 2c + c³/(2(1 + c)) ; le double est au milieu à 0,000054655684875 près
- en logarithme : log₁₀(1 + c) = 0,020599913280 ; le miroir est à −0,020599913280 ; l'écart, le double et le carré valent tous 2·log₁₀(1 + c) = 0,041199826559 décade.

### 2.2 Les retenues du doublement

| chiffre (de droite à gauche) | 2 × chiffre + retenue | écrit | retenue |
|---|---|---|---|
| 6 | 12 | 2 | 1 |
| 7 | 15 | 5 | 1 |
| 5 | 11 | 1 | 1 |
| 8 | 17 | 7 | 1 |
| 4 | 9 | 9 | 0 |
| 0 | 0 | 0 | 0 |

2 × 048576 = 097152 : quatre retenues de suite, que le 4 absorbe en devenant 9. Arrondi : 4,86 × 2 = 9,72.

### 2.3 Les paliers des octets et leurs miroirs

| palier | 2^(10j)/10^(3j) | virgule | miroir 10^(3j)/2^(10j) | chiffres de | ce qu'affiche un disque |
|---|---|---|---|---|---|
| kilo/kibi | 1,024 | +2,4000 % | 0,9765625 | 5^10 | 1 ko → 0,977 Kio |
| méga/mébi | 1,048576 | +4,8576 % | 0,95367431640625 | 5^20 | 1 Mo → 0,954 Mio |
| giga/gibi | 1,073741824 | +7,3742 % | 0,931322574615478515625 | 5^30 | 1 To → 931 Gio |
| téra/tébi | 1,099511627776 | +9,9512 % | 0,9094947017729282379150390625 | 5^40 | 1 To → 0,909 Tio |

### 2.4 Les trois écarts sur le cercle des décades

On place les crans 2⁰, 2¹, …, 2^(N−1) sur un cercle dont un tour vaut une décade (la position de 2ʲ est la partie fractionnaire de j·log₁₀ 2). Le théorème des trois distances (conjecturé par Steinhaus, démontré en 1958 par Sós, Surányi et Świerczkowski ; partie XI) dit qu'il n'y a jamais plus de trois écarts différents. Chaque écart est un rapport 2^a/10^b, donc 2^x·5^y.

| crans | écarts (en décade) | rapports exacts | combien |
|---:|---|---|---|
| 4 | 0,096910 ; 0,301030 | 5/4 ; 2/1 | 1 ; 3 |
| 11 | 0,010300 ; 0,096910 ; 0,107210 | 128/125 ; 5/4 ; 32/25 | 1 ; 8 ; 2 |
| 21 | 0,010300 ; 0,086610 ; 0,096910 | 128/125 ; 625/512 ; 5/4 | 11 ; 8 ; 2 |
| 94 | 0,004210 ; 0,010300 ; 0,014510 | 5²⁸/2⁶⁵ ; 128/125 ; 5²⁵/2⁵⁸ | 1 ; 84 ; 9 |

Pour 21 crans (2⁰ à 2²⁰) : 11 diesis 128/125, 8 écarts 625/512 = (5/4)⁴/2 et 2 tierces 5/4 ; le grand est le produit des deux petits. Les puissances de 5 occupent les positions symétriques (log₁₀ 5ʲ = j − log₁₀ 2ʲ) : mêmes écarts, dans l'ordre inverse.

### 2.5 Les crans les plus proches des décades, et leurs reflets

Fraction continue de log₁₀ 2 : [0; 3, 3, 9, 2, 2, 4, 6, 2, 1, …]. Ses réduites donnent les crans qui tombent le plus près d'une décade, alternativement au-dessus et au-dessous.

| j | 2ʲ ≈ 10ᵇ | écart de 2ʲ | 5ʲ ≈ 10^(j−b) | écart de 5ʲ | (1 + écart)(1 + écart miroir) |
|---:|---|---|---|---|---|
| 3 | 10¹ | −20,0000 % | 10² | +25,0000 % | 1 (exact) |
| 10 | 10³ | +2,4000 % | 10⁷ | −2,3438 % | 1 (exact) |
| 93 | 10²⁸ | −0,9648 % | 10⁶⁵ | +0,9742 % | 1 (exact) |
| 196 | 10⁵⁹ | +0,4336 % | 10¹³⁷ | −0,4318 % | 1 (exact) |
| 485 | 10¹⁴⁶ | −0,1040 % | 10³³⁹ | +0,1042 % | 1 (exact) |
| 2136 | 10⁶⁴³ | +0,0163 % | 10¹⁴⁹³ | −0,0163 % | 1 (exact) |

### 2.6 La tranche en crans

| décade | cran le plus proche | 2⁻ᵐ ÷ 10⁻ᵏ | chiffres de 5ᵐ (les mêmes que 2⁻ᵐ) |
|---|---|---|---|
| 10⁻⁴⁹ | 2⁻¹⁶³ | 0,8553 | 855284707229… |
| 10⁻⁵⁰ | 2⁻¹⁶⁶ | 1,0691 | 106910588403… |
| 10⁻⁵¹ | 2⁻¹⁶⁹ | 1,3364 | 133638235504… |
| 10⁻⁵² | 2⁻¹⁷³ | 0,8352 | 835238971903… |
| 10⁻⁵³ | 2⁻¹⁷⁶ | 1,0440 | 104404871487… |
| 10⁻⁵⁴ | 2⁻¹⁷⁹ | 1,3051 | 130506089359… |
| 10⁻⁵⁵ | 2⁻¹⁸³ | 0,8157 | 815663058499… |

Miroir autour de 50 : 2⁻¹⁶³ × 2⁻¹⁶⁹ = (2⁻¹⁶⁶)², comme 10⁻⁴⁹ × 10⁻⁵¹ = (10⁻⁵⁰)² ; les écarts suivent : 1,142987 = 1,142987.

## 3. Le cube qui tourne : de deux carrés à l'hexagone

- L'ombre du cube unité dans la direction u vaut |u₁| + |u₂| + |u₃| (2 000 directions au hasard, écart max 1.1e-15). C'est √3·cos(angle avec la grande diagonale la plus proche).
- Vues spéciales : face (carré) 1 ; diagonale de face (rectangle coupé en deux) √2 ; grande diagonale (hexagone) √3.
- Moyenne sur toutes les directions : 3/2 (Cauchy : un quart de la surface 6 ; ou 3 × ½ par la boîte à chapeau d'Archimède, u₁ étant uniforme sur [−1, 1]). Monte-Carlo : 1,4998.

### 3.1 Le mouvement complet autour d'un axe d'ordre 2

On tourne autour de l'axe (1, −1, 0)/√2, qui passe par les milieux de deux arêtes opposées ; la direction de vue est u(t) = cos t·(1, 1, 0)/√2 + sin t·(0, 0, 1). C'est le seul type d'axe dont le tour passe par les trois vues spéciales.

    ombre(t) = √2·|cos t| + |sin t|

| t | vue | ombre |
|---|---|---|
| 0,00° | rectangle (diagonale de face) | 1,414214 |
| 35,26° | hexagone (grande diagonale) | 1,732051 |
| 90,00° | carré (face) | 1,000000 |
| 144,74° | hexagone | 1,732051 |
| 180,00° | rectangle | 1,414214 |

- Hexagones à ±35,26° et 180° ± 35,26° : quatre par tour, séparés tour à tour par 70,53° (autour du rectangle) et 109,47° (autour du carré), cos = ±1/3 : les angles du losange de la partie II.
- Moyenne sur le tour : 1,536936 = (2/π)(1 + √2) = 1,536936.
- Autres axes : d'ordre 4 (une face) 4/π = 1,2732 ; d'ordre 3 (la grande diagonale, le tour de la partie II vu de côté) (2/π)√6 = 1,5594, le plus grand possible.

### 3.2 Les deux carrés

- Les faces avant et arrière (z = ±½) se projettent en deux parallélogrammes d'aire |u₃| décalés de l'ombre de l'arête verticale. Leur partie commune vaut (|u₃| − |u₁|)(|u₃| − |u₂|)/|u₃| tant que |u₁|, |u₂| ≤ |u₃|, et 0 ensuite (1 000 directions, écart max 3.9e-16).
- Sur le mouvement, de la face (t = 90°) à l'hexagone (t = 35,26°), elle passe de 1 à 0 : les deux carrés se quittent exactement à l'hexagone, où ils ne se touchent plus qu'au centre (les sommets (½, ½, ½) et (−½, −½, −½) s'y projettent tous les deux).
- À l'hexagone, les trois paires de faces sont dans ce cas en même temps : six losanges de 60°/120°, d'aire 1/√3 = 0,57735 chacun ; trois devant (un pavage de l'hexagone), trois derrière (l'autre pavage). Le dessin en fil de fer superpose les deux : les six rayons.

### 3.3 Le carré passe dans l'hexagone (Prince Rupert)

- Le long de la grande diagonale (l'hexagone, Wallis 1693) : côté 1,03527623 ; √6 − √2 = 1,03527618.
- Le long de (2, 2, 1)/3 (Nieuwland, publié en 1816) : côté 1,06066022 ; 3√2/4 = 1,06066017 ; ombre 5/3 ; aire du carré 9/8.
- Aucune des 54 directions de la grille ne fait mieux (meilleure : 1,06066), ni les 6 voisines de (2, 2, 1)/3 (meilleure : 1,060652).
- (2, 2, 1) est le plus petit quadruplet de Pythagore : 1² + 2² + 2² = 3².
- (2, 2, 1)/3 est sur le mouvement complet du § 3.1 : t = arcsin(1/3) = 19,47°, entre le rectangle (0°) et l'hexagone (35,26°), à 15,79° de l'hexagone ; ombre √2·cos t + sin t = 4/3 + 1/3 = 5/3. (calcul : 5 s)
