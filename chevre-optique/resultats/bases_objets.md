# Résultats de la partie XIX (générés par scripts/bases_objets.py)

## 1. i modulo b : quand la base a une racine carrée de −1

x² ≡ −1 (mod b) a une solution exactement quand b est une somme de deux carrés premiers entre eux, b = a² + c² (aucun facteur premier ≡ 3 mod 4, pas divisible par 4). Alors a² ≡ −c², donc i ≡ a/c (mod b) : la pente de l'aiguille (a, c) de la grille, modulo le carré de sa longueur.

| base b | x avec x² ≡ −1 | aiguille (a, c), a² + c² = b | pente a/c mod b |
|---:|---|---|---|
| 2 | 1 | (1, 1) | 1 |
| 5 | 2, 3 | (2, 1) | 2 |
| 10 | 3, 7 | (3, 1) | 3 |
| 13 | 5, 8 | (3, 2) | 8 |
| 17 | 4, 13 | (4, 1) | 4 |
| 25 | 7, 18 | (4, 3) | 18 |
| 26 | 5, 21 | (5, 1) | 5 |
| 29 | 12, 17 | (5, 2) | 17 |
| 34 | 13, 21 | (5, 3) | 13 |
| 37 | 6, 31 | (6, 1) | 6 |

Bases de 2 à 40 sans i : 3, 4, 6, 7, 8, 9, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 27, 28, 30, 31, 32, 33, 35, 36, 38, 39, 40. Le théorème est vérifié pour toutes les bases de 2 à 40.

Les deux horloges de la base 10 :
- multiplicative : 3¹, 3², 3³, 3⁴ ≡ 3, 9, 7, 1 (mod 10), comme i, −1, −i, 1. Les unités {1, 3, 9, 7} sont les quatre quarts de tour de l'aiguille ;
- additive : 27 = 2 × 10 + 7, sur le troisième tour de l'hélice des dizaines. 27 = 3³ est aussi trois quarts de tour multiplicatifs : −i.
- Base 2 : 1 ≡ −1 (mod 2), et 1² = 1 ≡ −1 : i ≡ −i ≡ 1. L'aiguille ne tourne pas.
- Base 10 = base 2 × base 5 (restes chinois) : le dernier chiffre décimal porte la parité (mod 2) et un chiffre de base 5 ; i vit dans la partie mod 5 (2² ≡ −1 mod 5).

## 2. Les subdivisions harmoniques entre deux chiffres

1/n s'écrit avec un nombre fini de chiffres en base b quand tous les facteurs premiers de n divisent b ; sinon il est périodique, de période égale au nombre de pas de l'aiguille « × b » sur le cercle des restes modulo n avant de revenir à son départ.

| n | 1/n en base 2 | période | 1/n en base 10 | période |
|---:|---|---|---|---|
| 2 | 0,1000000000000000… | fini | 0,500000000000… | fini |
| 3 | 0,0101010101010101… | 2 | 0,333333333333… | 1 |
| 4 | 0,0100000000000000… | fini | 0,250000000000… | fini |
| 5 | 0,0011001100110011… | 4 | 0,200000000000… | fini |
| 6 | 0,0010101010101010… | 2 | 0,166666666666… | 1 |
| 7 | 0,0010010010010010… | 3 | 0,142857142857… | 6 |
| 8 | 0,0010000000000000… | fini | 0,125000000000… | fini |
| 9 | 0,0001110001110001… | 6 | 0,111111111111… | 1 |
| 10 | 0,0001100110011001… | 4 | 0,100000000000… | fini |
| 11 | 0,0001011101000101… | 10 | 0,090909090909… | 2 |
| 12 | 0,0001010101010101… | 2 | 0,083333333333… | 1 |
| 13 | 0,0001001110110001… | 12 | 0,076923076923… | 6 |
| 17 | 0,0000111100001111… | 8 | 0,058823529411… | 16 |
| 101 | 0,0000001010001000… | 100 | 0,009900990099… | 4 |

- 1/5 en binaire : 0,0011 0011… (période 4) parce que 2 ≡ i (mod 5) : quatre quarts de tour.
- 1/3 en binaire : 0,01 01… (période 2) parce que 2 ≡ −1 (mod 3) : un demi-tour. 1/11 en décimal : période 2, 10 ≡ −1 (mod 11). 1/101 en décimal : période 4, 10 ≡ i (mod 101).
- Sur un ordinateur (binaire), 0,1 + 0,2 = 0,30000000000000004 : 1/10 n'a pas d'écriture finie en base 2.

## 3. Deux échelles qui ne se recalent jamais

log₁₀ 2 est irrationnel : si log₁₀ 2 = p/q, alors 2^q = 10^p = 2^p 5^p, impossible pour p ≥ 1. Sur le cercle des décades (log₁₀ x mod 1), multiplier par 2 fait tourner l'aiguille de log₁₀ 2 = 0,301030 tour (108,37°), sans jamais retomber exactement au même endroit.

Fraction continue : log₁₀ 2 = [0 ; 3, 3, 9, 2, 2, 4, 6, 2, 1, 1, …]. Quasi-retours (réduites p/q) :

| p/q | 2^q / 10^p | écart |
|---|---|---|
| 1/3 | 0,800000 | −20,000 % |
| 3/10 | 1,024000 | +2,400 % |
| 28/93 | 0,990352 | −0,965 % |
| 59/196 | 1,004336 | +0,434 % |
| 146/485 | 0,998960 | −0,104 % |
| 643/2136 | 1,000163 | +0,016 % |
| 4004/13301 | 0,999936 | −0,006 % |

Décibels : doubler une puissance ajoute 10 log₁₀ 2 = 3,0103 dB, presque 3 dB, à cause de 2^10 ≈ 10^3.

Les préfixes : kilo = 10³ mais kibi = 2¹⁰. L'écart se cumule à chaque palier :

| palier | 2^(10k) / 10^(3k) | écart |
|---|---|---|
| kibi / kilo | 1,0240 | +2,40 % |
| mébi / méga | 1,0486 | +4,86 % |
| gibi / giga | 1,0737 | +7,37 % |
| tébi / téra | 1,0995 | +9,95 % |
| pébi / péta | 1,1259 | +12,59 % |

Un disque vendu « 1 To » (10¹² octets, compté en base 10) contient 931,3 Gio : c'est le « 931 Go » d'un système qui compte en base 2.

Premier chiffre des puissances de 2 (n = 1 à 10000) contre la loi de Benford log₁₀(1 + 1/d) :

| d | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| 2^n | 0,3010 | 0,1761 | 0,1249 | 0,0970 | 0,0791 | 0,0670 | 0,0579 | 0,0512 | 0,0458 |
| Benford | 0,3010 | 0,1761 | 0,1249 | 0,0969 | 0,0792 | 0,0669 | 0,0580 | 0,0512 | 0,0458 |

En base 2, le premier chiffre d'un nombre non nul est toujours 1 : la loi de Benford y est triviale.

Théorème des trois distances (partie XI) pour les points n·log₁₀ 2 mod 1 : 10 points : 2 longueurs ; 30 points : 3 longueurs ; 93 points : 2 longueurs ; 100 points : 3 longueurs. Deux longueurs seulement aux dénominateurs des réduites (10, 93).

**L'atlas de la virgule flottante.** Un nombre flottant = mantisse × base^exposant : chaque exposant est une carte (une décade, ou une « binade » de 1 à 2), découpée en un nombre fixe de pas. L'écart entre deux nombres voisins grandit avec le nombre (un cône sur deux échelles logarithmiques), et l'écart relatif oscille d'un facteur égal à la base dans chaque carte : 2 en binaire, 10 en décimal.

## 4. Le point, le trait, le cône

**Trois points : à gauche, à droite ou au centre.** On mesure la pente en 0 avec des points espacés de h. Les segments {−1, 0, 1}, {0, 1, 2} et {1, 2, 3} donnent trois formules : les dérivées en 0 des polynômes de Lagrange. Erreur de troncature, et sensibilité au bruit des points (écart-type σ chacun, indépendants) :

| points (en h) | où est 0 | poids | erreur de troncature | bruit (× σ/h) |
|---|---|---|---|---|
| {−1, 0} | points à gauche | −1, 1 | −h·f″/2 | 1,414 |
| {0, 1} | points à droite | −1, 1 | +h·f″/2 | 1,414 |
| {−1, 0, 1} | au centre | −1/2, 0, 1/2 | +h²·f‴/6 | 0,707 |
| {0, 1, 2} | au bord | −3/2, 2, −1/2 | −h²·f‴/3 | 2,550 |
| {1, 2, 3} | dehors | −5/2, 4, −3/2 | −11h²·f‴/6 | 4,950 |

- À gauche et à droite (deux points), les erreurs sont **opposées** : ±h·f″/2. Le centre est leur moyenne, et elles s'y annulent : l'erreur tombe à h²·f‴/6.
- Pour les trois segments de trois points, les erreurs sont dans le rapport 1 : 2 : 11 et le bruit dans le rapport 1 : 3,61 : 7,00 (soit 1 : √13 : 7). Le centre gagne sur les deux tableaux.

Sur le cercle de R pixels, près de sa tangente verticale (x(y) = √(R² − y²), vraie pente 0), la tangente mesurée penche de (en degrés) :

| R | h | droite {0, h} | gauche {−h, 0} | centre {−h, 0, h} | bord {0, h, 2h} | dehors {h, 2h, 3h} |
|---:|---:|---|---|---|---|---|
| 10 | 1 | −2,87 | +2,87 | 0 (exact) | +0,04 | +0,46 |
| 12 | 3 | −7,24 | +7,24 | 0 (exact) | +0,80 | +11,60 |
| 50 | 1 | −0,57 | +0,57 | 0 (exact) | +0,00034 | +0,00345 |
| 50 | 3 | −1,72 | +1,72 | 0 (exact) | +0,00937 | +0,10 |

La droite et la gauche penchent d'environ ∓h/(2R) radian, en sens contraires ; le centre est exact par symétrie.

**L'erreur du point.** Un pixel arrondit la position : erreur uniforme d'écart-type σ = 1/√12 = 0,2887 pixel. Avec trois points espacés de h, la courbure (y(−h) − 2y(0) + y(h))/h² a un bruit √6·σ/h². Elle n'émerge du bruit (1/R > √6·σ/h²) que pour h > (√6·σ·R)^(1/2) ≈ 0,84 √R : il faut environ √R pixels de chaque côté pour voir qu'un arc est courbé, la longueur de la colonne verticale de la partie XVIII.

| R | √6·σ·R : h minimal | √R |
|---:|---|---|
| 10 | 2,66 | 3,16 |
| 100 | 8,41 | 10,00 |
| 1000 | 26,59 | 31,62 |

**L'erreur du point en dimension n.** Arrondir un point à la grille, c'est le ramener au centre de sa case : l'erreur est uniforme dans le cube [−1/2, 1/2]^n. Sa longueur moyenne quadratique vaut √(n/12) ; elle se concentre de plus en plus autour de cette valeur, et la boule inscrite (rayon 1/2) n'en contient presque plus rien : en grande dimension, l'erreur vit sur une sphère mince de rayon √(n/12), dans les coins du cube.

| n | √(n/12) | part du cube dans la boule inscrite | dispersion relative de la longueur |
|---:|---|---|---|
| 1 | 0,2887 | 1,0000 | 0,578 |
| 2 | 0,4082 | 0,7854 | 0,372 |
| 3 | 0,5000 | 0,5236 | 0,290 |
| 10 | 0,9129 | 0,0025 | 0,146 |
| 100 | 2,8868 | 1,9 × 10^−70 | 0,045 |

En dimension 3, l'erreur moyenne quadratique vaut exactement 1/2 voxel (√(3/12) = 1/2).

**Cylindre + cône = hyperboloïde.** Un point d'erreur w₀ (le trait d'épaisseur 2w₀, un cylindre) et une direction d'erreur θ (un cône) donnent ensemble l'enveloppe r² = w₀² + θ²z² : un hyperboloïde. C'est le profil d'un faisceau laser gaussien, où la lumière impose w₀·θ = λ/π : plus le trait est fin, plus le cône s'ouvre.
- λ = 550 nm, demi-épaisseur w₀ = 1000 µm : cône θ = 0,175 mrad, longueur où le trait reste fin z_R = πw₀²/λ = 5,71 m.
- λ = 550 nm, demi-épaisseur w₀ = 85 µm : cône θ = 2,06 mrad, longueur où le trait reste fin z_R = πw₀²/λ = 41,3 mm.
- λ = 550 nm, demi-épaisseur w₀ = 5 µm : cône θ = 35 mrad, longueur où le trait reste fin z_R = πw₀²/λ = 0,143 mm.
- Même forme : l'hyperboloïde du cube qui tourne (partie II), r² = 1/2 + 2 z², col √2/2 et cône de pente √2 ; et la chèvre de dimension infinie (partie XVI), ρ² = 1 + d², col 1 et cône à 45°. Les deux ont le même produit col × pente : (√2/2)·√2 = 1·1 = 1, comme deux faisceaux de même longueur d'onde.

**Archimède : la demi-sphère et son cône conjugué.** Dans le cylindre de rayon 1 et de hauteur 1, à la hauteur z, la demi-sphère a pour rayon √(1 − z²) et le cône (sommet au centre) a pour rayon z : (1 − z²) + z² = 1, les deux tranches remplissent la tranche du cylindre (1/3 + 2/3 du volume).
- Les deux surfaces se croisent sur le cercle z = r = 1/√2 (la latitude 45°), et à angle droit : chaque génératrice du cône est un rayon de la sphère.
- Vu de dessus, ce cercle entoure exactement la moitié du disque (π/2) : c'est le demi-disque des parties XVII et XVIII, et le plateau de la chèvre en dimension 2 (partie XVI).
- À l'écran (projection vue de dessus), une surface de pente φ est comprimée d'un facteur cos φ : le cône d'un facteur uniforme 1/√2 = 0,7071, la demi-sphère d'un facteur √(1 − r²) qui tend vers 0 au bord, le cylindre complètement (vu par la tranche). C'est pourquoi les parallèles du globe se serrent au bord et s'y replient (partie XVIII).
- Le cône et le cylindre se déroulent à plat sans déformation (courbure de Gauss nulle) ; la demi-sphère non (theorema egregium de Gauss). Projeter la sphère horizontalement sur le cylindre garde les aires (Archimède, projection de Lambert) mais déforme les formes ; projeter verticalement sur l'écran comprime par cos φ. Aucune carte plate ne garde tout.

## 5. Le cône des échelles et Thalès

Thalès : un objet de taille L à la distance D sous-tend L/D radian. La Lune : 3474,8 km à 384400 km, soit 0,518° ; rapport D/L = 110,6.
- Un sou (pièce d'un cent, 19,05 mm) cache la Lune à 2,11 m de l'œil.
- Une minute d'arc (l'acuité de l'œil) : 87 µm à 30 cm (un pixel « Retina »), 112 km sur la Lune.
- Une décade = log₂ 10 = 3,3219 octaves.
