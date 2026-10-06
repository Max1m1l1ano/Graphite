# Résultats de la partie XVIII (générés par scripts/pixels_longitudes.py)

## 1. Les huit octants du cercle de pixels

L'algorithme du point milieu ne calcule qu'un huitième du cercle, de 90° à 45°, puis le reflète huit fois. Les frontières sont à 45°, 135°, 225° et 315° (et aux axes). Dans un octant, une coordonnée avance d'un pixel à chaque pas ; l'autre avance de 0 ou de 1 selon le signe d'une variable de décision : c'est un arrondi, un « mod 1 ».

| R (pixels) | pixels du 1er octant | pixels du cercle entier | pas « en diagonale » dans l'octant |
|---:|---|---|---|
| 5 | 4 | 28 | 1 |
| 10 | 8 | 56 | 3 |
| 20 | 15 | 112 | 6 |
| 50 | 36 | 284 | 14 |
| 100 | 71 | 564 | 29 |

Nombre de pixels par unité de longueur d'une courbe de direction θ : |cos θ| + |sin θ|. Il vaut 1 le long des axes et √2 = 1,4142 à 45°, 135°, 225° et 315° : la diagonale 1x, 1y coûte 1 + 1 = 2 pixels pour une longueur √2. En moyenne sur le cercle : 4/π = 1,2732.

## 2. Le contact vu à travers l'épaisseur du trait, puis à travers les pixels

Deux traits d'épaisseur w se confondent là où leurs axes sont à moins de w l'un de l'autre. Près de P, l'écart vaut y²(√2 ∓ 1)/2 : la zone de contact apparent a pour demi-longueur √(2w/(√2 ∓ 1)).

| w (en rayons du pré) | demi-longueur, contact intérieur | contact extérieur | rapport | arc apparent intérieur | extérieur |
|---:|---|---|---|---|---|
| 0,05 | 0,43478 | 0,20184 | 2,1541 | 51,5° | 23,3° |
| 0,021 | 0,30172 | 0,13144 | 2,2955 | 35,1° | 15,1° |
| 0,01 | 0,21406 | 0,09087 | 2,3557 | 24,7° | 10,4° |
| 0,001 | 0,06930 | 0,02878 | 2,4082 | 7,9° | 3,3° |
| 0,0001 | 0,02197 | 0,00910 | 2,4136 | 2,5° | 1,0° |

Le rapport tend vers √2 + 1 = 2,4142 quand le trait s'affine. Sur la figure q1 de la partie XVII, les traits font environ w ≈ 0,021 rayon : le contact intérieur semble couvrir un arc d'environ 35°, l'extérieur d'environ 15°.

**Avec des pixels** (anneau numérique : pixels dont le centre est à moins d'un demi-pixel du cercle). Pré de N pixels de rayon, petits cercles de N/√2 :

| N | pixels partagés, contact intérieur | contact extérieur | colonne verticale du petit cercle 2⌊√(N/√2 + 1/4)⌋ + 1 | (4/3)√(2(√2 + 1)N) |
|---:|---|---|---|---|
| 8 | 9 | 5 | 5 | 8,3 |
| 16 | 13 | 7 | 7 | 11,7 |
| 32 | 17 | 9 | 9 | 16,6 |
| 64 | 23 | 13 | 13 | 23,4 |
| 128 | 33 | 19 | 19 | 33,1 |
| 256 | 49 | 27 | 27 | 46,9 |
| 512 | 65 | 39 | 39 | 66,3 |
| 1024 | 93 | 53 | 53 | 93,8 |
| 2048 | 131 | 77 | 77 | 132,6 |

Au contact extérieur, les pixels partagés sont exactement la colonne verticale du petit cercle au point de tangence. Au contact intérieur, les deux anneaux restent ensemble bien au-delà de cette colonne.

Colonne verticale au point le plus à droite d'un cercle de N pixels : 2⌊√(N + 1/4)⌋ + 1 pixels.

| N | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|
| pixels | 3 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 7 | 7 | 7 | 7 |

Trois pixels pour les cercles de rayon 1, 2 et 3 : la plus petite tangente verticale.

## 3. Compter les pixels : le cercle de Gauss, en décimal et en binaire

N(R) = nombre de pixels (points entiers) dans le disque de rayon R. Gauss a donné N(10) = 317 et N(100) = 31 417.

| R | N(R) | πR² | écart E = N − πR² | chiffres communs avec π·R² |
|---:|---|---|---|---|
| 10^0 | 5 | 3,141592653589793 | +1,86 | 0 |
| 10^1 | 317 | 314,1592653589793 | +2,84 | 2 |
| 10^2 | 31417 | 31415,92653589793 | +1,07 | 4 |
| 10^3 | 3141549 | 3141592,653589793 | −43,65 | 5 |
| 10^4 | 314159053 | 314159265,3589793 | −212,36 | 6 |
| 10^5 | 31415925457 | 31415926535,89793 | −1078,90 | 7 |
| 10^6 | 3141592649625 | 3141592653589,793 | −3964,79 | 8 |

En binaire (R = 2^k), N(R) écrit en base 2 reproduit les premiers bits de π = 11,0010010000111111011010101…

| R | N(R) en binaire | bits communs avec π·R² |
|---:|---|---|
| 2^0 | 101 | 1 |
| 2^4 | 1100011101 | 4 |
| 2^8 | 110010010000100101 | 13 |
| 2^12 | 11001001000011111001101001 | 17 |
| 2^16 | 1100100100001111110110010010001001 | 22 |
| 2^20 | 110010010000111111011010100111111010100101 | 26 |

**L'écart se coupe en deux, exactement.** Avec ⌊y⌋ = y − ½ − ψ(y), où ψ(y) = (y mod 1) − ½ est la dent de scie :
E(R) = T(R) + S(R) + 2, où T(R) = Σ 2√(R² − x²) − πR² (l'erreur des trapèzes) et S(R) = −2 Σ_{|x|<R} ψ(√(R² − x²)) (la somme des dents de scie : le « mod 1 » de chaque colonne).
Le terme lisse vient des deux tangentes verticales (x = ±R) : T(R) ≈ 4√2 ζ(−1/2) √R = −1,175982 √R.

| R | E(R) | T(R) | T/√R | S(R) | T + S + 2 |
|---:|---|---|---|---|---|
| 10 | +2,84 | −3,71 | −1,17239 | +4,55 | +2,84 |
| 100 | +1,07 | −11,76 | −1,17562 | +10,83 | +1,07 |
| 1000 | −43,65 | −37,19 | −1,17595 | −8,47 | −43,65 |
| 10000 | −212,36 | −117,60 | −1,17598 | −96,76 | −212,36 |
| 100000 | −1078,90 | −371,88 | −1,17598 | −709,02 | −1078,90 |
| 1000000 | −3964,79 | −1175,98 | −1,17598 | −2790,81 | −3964,79 |

Bornes connues : E(R) = O(R^(131/208)) ≈ R^0,6298 (Huxley, 2003), amélioré en R^0,6289 (Li et Yang, prépublication 2023) ; une prépublication de Bourgain et Watt (2017) annonce R^(517/824) ≈ R^0,6274. Conjecture de Hardy : R^(1/2 + ε).

## 4. L'espace entre les nombres : pixels intérieurs et extérieurs

| R | pixels entièrement dedans | πR² | pixels touchés | écart | 8R | π certain entre |
|---:|---|---|---|---|---|---|
| 10 | 277 | 314,2 | 357 | 80 | 80 | 2,770000 et 3,570000 |
| 100 | 31029 | 31415,9 | 31829 | 800 | 800 | 3,102900 et 3,182900 |
| 1000 | 3137677 | 3141592,7 | 3145677 | 8000 | 8000 | 3,137677 et 3,145677 |
| 10000 | 314119389 | 314159265,4 | 314199389 | 80000 | 80000 | 3,141194 et 3,141994 |

L'écart vaut exactement 8R : chaque quart de cercle traverse R lignes verticales et R horizontales de la grille (2R + 1 pixels), et le cercle ne passe jamais par un coin de pixel, parce qu'un coin a des coordonnées demi-entières : (2x)² + (2y)² serait la somme de deux carrés impairs, ≡ 2 modulo 4, alors que 4R² ≡ 0 modulo 4.
- R = 10 : périmètre de l'escalier intérieur = 76 = 8R − 4 ; rapport au cercle 1,2096 → 4/π = 1,2732.
- R = 100 : périmètre de l'escalier intérieur = 796 = 8R − 4 ; rapport au cercle 1,2669 → 4/π = 1,2732.
- R = 1000 : périmètre de l'escalier intérieur = 7996 = 8R − 4 ; rapport au cercle 1,2726 → 4/π = 1,2732.

**La chèvre en pixels.** Deux façons de la compter, sur un pré de R pixels de rayon :
- par les centres des pixels (rapide, mais sans garantie) ;
- par les pixels entièrement dedans et ceux qui touchent (lent, mais certain : la vraie corde est forcément dans l'intervalle).

| R | corde par les centres | écart à r | encadrement certain | largeur | r dedans ? |
|---:|---|---|---|---|---|
| 10^1 | 1,1401754251 | −1,86e−02 | [1,00000000 ; 1,39463257] | 3,95e−01 | oui |
| 10^2 | 1,1588356225 | +1,07e−04 | [1,13589172 ; 1,18163023] | 4,57e−02 | oui |
| 10^3 | 1,1587337917 | +5,32e−06 | [1,15644996 ; 1,16103079] | 4,58e−03 | oui |
| 10^4 | 1,1587283245 | −1,49e−07 | [1,15849989 ; 1,15895702] | 4,57e−04 | oui |
| 10^5 | 1,1587284799 | +6,87e−09 | [1,15870562 ; 1,15875133] | 4,57e−05 | oui |
| 2^3 | 1,1524430572 | −6,29e−03 | [1,00000000 ; 1,44967669] | 4,50e−01 | oui |
| 2^5 | 1,1566722202 | −2,06e−03 | [1,08815533 ; 1,23526471] | 1,47e−01 | oui |
| 2^7 | 1,1583859073 | −3,43e−04 | [1,14090589 ; 1,17677362] | 3,59e−02 | oui |
| 2^9 | 1,1587234023 | −5,07e−06 | [1,15428613 ; 1,16320441] | 8,92e−03 | oui |
| 2^11 | 1,1587239167 | −4,56e−06 | [1,15761182 ; 1,15984739] | 2,24e−03 | oui |
| 2^13 | 1,1587275818 | −8,91e−07 | [1,15844984 ; 1,15900724] | 5,57e−04 | oui |
| 2^15 | 1,1587283960 | −7,70e−08 | [1,15865868 ; 1,15879830] | 1,40e−04 | oui |
| 2^17 | 1,1587284701 | −2,97e−09 | [1,15871103 ; 1,15874591] | 3,49e−05 | oui |

L'encadrement certain gagne exactement un chiffre par niveau décimal (×10) et un bit par niveau binaire (×2) : sa largeur vaut environ 4,6/R. Le comptage par les centres va plus vite (environ R^−1,5), mais sans garantie.

La corde en décimal : 1,15872847301812151782823350993… ; en binaire : 1,001010001010001001101101111000001000111010001101…

## 5. Les longitudes qui manquaient

- Lame de zones (les latitudes vues du pôle) : phase π r²/s² avec s² = 100 pixels² ; fréquence locale r/s², repliement au-delà de r = s²/2 = 50 pixels.
- Étoile de Siemens (les longitudes) : 72 périodes sur le tour ; période locale 2πr/72, repliement en deçà de r = 72/π = 22,9 pixels.

**Où se recréent les centres.** Aux points entiers, cos φ(x) = cos(φ(x) − 2π m·x) pour tout vecteur entier m : un nouveau centre apparaît là où ∇φ = 2π m.
- Lame de zones, φ = π r²/s² : ∇φ = 2π x/s², donc les centres fantômes sont aux points s²·m du réseau (à 100, 141,4, 200 pixels…), hors du disque de Nyquist.
- Étoile, φ = Nθ : ∇φ = N(−y, x)/r², donc les centres fantômes sont aux points (N/2π)·(m₂, −m₁)/|m|² : le réseau inversé (x ↦ x/|x|²), tourné de 90°, à 11,46, 8,10, 5,73 pixels… du centre, dans le disque de Nyquist.
- Pour un même m, distance du fantôme des anneaux × distance du fantôme des rayons = s²N/(2π) = 1145,9 : la forme de Newton x·x' = f² (partie XVII).
- Globe vu du pôle, parallèles et méridiens tous les 5° : les méridiens se replient près du pôle (rayon 2/(5° en radians) = 22,9 pixels), les parallèles près du bord.

## 6. La lumière

- 300 pixels par pouce vus à 30 cm : un pixel sous-tend 0,97 minute d'arc (l'acuité « 10/10 » vaut environ 1 minute).
- Pupille de 3 mm, lumière à 550 nm : limite de diffraction 1,22 λ/D = 0,77 minute d'arc.
- Sous un flou plus large que le pixel, un pixel carré de côté p devient indiscernable d'un disque de rayon p/√3 (même étalement), l'écart décroissant comme (p/σ)⁴ (partie X).
