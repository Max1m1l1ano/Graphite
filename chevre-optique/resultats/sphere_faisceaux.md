# Résultats de la partie XX (générés par scripts/sphere_faisceaux.py)

## 1. Deux chèvres au même endroit : la division d'intégrales complexes, dimension par dimension

**La formule d'Ullisch (2020), calculée directement.** β = ∮ z/f(z) dz ÷ ∮ 1/f(z) dz sur le cercle |z − 3π/4| = π/4, avec f(z) = sin z − z cos z − π/2, puis r = 2 cos(β/2) :
- β = 1,905695729309883894882666 (partie imaginaire 3,2e−33, 256 points) ;
- r = 1,158728473018121517828234.

Dans le plan méridien, l'équation de la dimension n est G_n(β) = 0, et G_2 = f/2 (écart vérifié 2,0e−31). Le même procédé (diviser deux intégrales de contour) donne la corde de chaque dimension :

| n | zéros de G_n dans le cercle d'Ullisch | cercle utilisé (trapèzes) | β_n (division) | angle α_n = π − β_n | corde ρ_n |
|---:|---|---|---|---|---|
| 2 | 1 | Ullisch (256 points) | 1,9056957293098838949 | 70,812° | 1,15872847301812 |
| 3 | 1 | Ullisch (256 points) | 1,8186654425307943381 | 75,798° | 1,22854486373522 |
| 4 | 1 | Ullisch (256 points) | 1,7680607051346728152 | 78,698° | 1,26807925667342 |
| 5 | 1 | \|β − β_n\| < 0,25 (64 points) | 1,7348331015781602522 | 80,601° | 1,29359799636023 |
| 6 | 1 | \|β − β_n\| < 0,25 (64 points) | 1,7112920278732134363 | 81,950° | 1,31146181902716 |
| 8 | 1 | \|β − β_n\| < 0,25 (128 points) | 1,6800849015054563879 | 83,738° | 1,33486242915791 |
| 9 | 1 | \|β − β_n\| < 0,25 (128 points) | 1,6691952722239202429 | 84,362° | 1,34295179853544 |
| 10 | 3 | \|β − β_n\| < 0,25 (128 points) | 1,6602927991529253732 | 84,872° | 1,34953543999843 |
| 12 | 3 | \|β − β_n\| < 0,25 (128 points) | 1,6466022012175802252 | 85,657° | 1,35960781711644 |
| 24 | 5 | \|β − β_n\| < 0,25 (128 points) | 1,6104035161842535578 | 87,731° | 1,38593157500109 |
| 100 | — | \|β − β_n\| < 0,1 (128 points) | 1,5806671529465787936 | 89,434° | 1,40721663871529 |
| ∞ | — | — | π/2 | 90° | √2 = 1,41421356237310 |

- Le cercle d'Ullisch, tel quel, isole la seule racine réelle jusqu'à la dimension 9. Ensuite, des paires de zéros complexes y entrent : n = 10 : 3 zéros, n = 19 : 5 zéros, n = 28 : 7 zéros, n = 36 : 9 zéros… La première paire, 2,4237587 ± 0,78080506i, est à 0,78372281 du centre, à peine sous le rayon π/4 = 0,78539816. Il suffit alors de resserrer le cercle autour de la racine réelle.
- Même avant la dimension 10, la paire qui approche du bord ralentit la règle des trapèzes sur le cercle d'Ullisch (la convergence dépend de la distance au zéro le plus proche, dedans ou dehors). Avec 256 points au plus, le cercle d'Ullisch suffit jusqu'à la dimension 4 ; au-delà, un cercle resserré est plus rapide.
- Zéros de G_10 dans le cercle d'Ullisch : 2,4238 − 0,7808i, 1,6603 + 0,0000i, 2,4238 + 0,7808i.
- Zéros de G_24 dans le cercle d'Ullisch : 2,3372 − 0,7053i, 2,0592 − 0,5321i, 1,6104 + 0,0000i, 2,0592 + 0,5321i, 2,3372 + 0,7053i.

**Les cordes certifiées à 50 chiffres** (arithmétique d'intervalles : G_n change de signe sur un intervalle de largeur 2·10⁻⁵⁸ autour de la racine) :

| n | corde ρ_n, encadrée à 10⁻⁵⁰ près |
|---:|---|
| 2 | 1,15872847301812151782823350993350914968829226649209 ≤ ρ ≤ …210 |
| 3 | 1,22854486373522090344899449768529346564419164551860 ≤ ρ ≤ …861 |
| 4 | 1,26807925667341823348355415211571793356474343402219 ≤ ρ ≤ …220 |
| 8 | 1,33486242915790962010461237019787330529447771629681 ≤ ρ ≤ …682 |
| 24 | 1,38593157500109279341163629468441198854737501013798 ≤ ρ ≤ …799 |
| ∞ | √2 = 1,41421356237309504880168872420969807856967187537695… |

- En dimension 3 (le « problème de l'oiseau »), la corde est la racine de 3r⁴ − 8r³ + 8 = 0 : 1,22854486373522090344899449769… L'encadrement certifié la contient. Les dimensions impaires donnent un polynôme (la corde est algébrique), les paires gardent l'angle et π (partie VII).

**Vers √2.** n·(2 − ρ_n²) tend vers 2, et l'angle α_n suit arccos(1/(n + 1)) à un petit ménisque près :

| n | ρ_n | n·(2 − ρ_n²) | α_n | arccos(1/(n + 1)) |
|---:|---|---|---|---|
| 2 | 1,158728 | 1,3147 | 70,812° | 70,529° |
| 3 | 1,228545 | 1,4720 | 75,798° | 75,522° |
| 4 | 1,268079 | 1,5679 | 78,698° | 78,463° |
| 8 | 1,334862 | 1,7451 | 83,738° | 83,621° |
| 24 | 1,385932 | 1,9006 | 87,731° | 87,708° |
| 100 | 1,407217 | 1,9741 | 89,434° | 89,433° |

## 2. Pair et impair : la récurrence de la partie IV

h_n = (hémisphère)/(cylindre) en dimension n ; h_n = (n − 1)/n · h_{n−2}, avec h_1 = 1 et h_0 = π/2. Les dimensions impaires divisent par 3, 5, 7… ; les paires, à partir du disque (h_2 = π/4), par 4, 6, 8…

| n | h_n | valeur | facteur depuis n − 2 | h_n > ½ (volume croît) | h_n > ½·(1 − 1/n) (aire croît) |
|---:|---|---|---|---|---|
| 1 | 1 | 1,00000 | — | oui | oui |
| 2 | π·1/4 | 0,78540 | × 1/2 | oui | oui |
| 3 | 2/3 | 0,66667 | × 2/3 | oui | oui |
| 4 | π·3/16 | 0,58905 | × 3/4 | oui | oui |
| 5 | 8/15 | 0,53333 | × 4/5 | oui | oui |
| 6 | π·5/32 | 0,49087 | × 5/6 | non | oui |
| 7 | 16/35 | 0,45714 | × 6/7 | non | oui |
| 8 | π·35/256 | 0,42951 | × 7/8 | non | non |
| 9 | 128/315 | 0,40635 | × 8/9 | non | non |
| 10 | π·63/512 | 0,38656 | × 9/10 | non | non |
| 11 | 256/693 | 0,36941 | × 10/11 | non | non |
| 12 | π·231/2048 | 0,35435 | × 11/12 | non | non |

- Réciprocité : h_{n−1}·h_n = π/(2n) pour tout n (vérifié jusqu'à 24) : chaque impaire est l'inverse de sa voisine paire, à π/(2n) près.
- Seuils (partie IV) : l'hémisphère remplit moins de la moitié de son cylindre à partir de la dimension 6 (pic du volume en 5), et moins de la moitié de l'anneau d'Archimède à partir de la dimension 8 (pic de l'aire en 7).
- La dimension 3 est le premier barreau : h_3 = 2/3 (Archimède). C'est aussi la seule dimension où l'ombre de la sphère sur un axe est uniforme : la densité de la projection de S^{n−1} est ∝ (1 − t²)^((n−3)/2), plate pour n = 3, massée aux bords pour n = 2, à l'équateur pour n ≥ 4.

**Aire et volume pour la chèvre.** Elle broute toujours la moitié du volume du pré, mais pas la moitié de sa clôture. Part de la clôture S^{n−1} broutée (calotte d'angle α_n) :

| n | 2 | 3 | 4 | 5 | 6 | 8 | 12 | 24 | 100 | 300 |
|---|---|---|---|---|---|---|---|---|---|---|
| part de la clôture | 0,3934 | 0,3773 | 0,3760 | 0,3786 | 0,3823 | 0,3900 | 0,4029 | 0,4255 | 0,4610 | 0,4771 |

- Minimum en dimension 4 (0,3760), puis la part monte vers ½ : en dimension infinie, aire et volume se rejoignent (la chèvre broute un hémisphère).

## 3. Les faisceaux des n-sphères

**n + 1 chèvres couvrent la clôture.** On place une chèvre de dimension n sur chaque sommet du simplexe régulier inscrit dans la clôture S^{n−1} ; chacune broute la calotte d'angle α_n. Pour former un bon recouvrement (nerf = bord du simplexe), il faut arccos(1/n) < α_n < 90° :

| n | sphère couverte | α_n | seuil arccos(1/n) | multiplicité observée (2·10⁵ points) | jamais n + 1 chèvres à la fois |
|---:|---|---|---|---|---|
| 2 | S^1 | 70,812° | 60,000° | 1 à 2 | oui |
| 3 | S^2 | 75,798° | 70,529° | 1 à 3 | oui |
| 4 | S^3 | 78,698° | 75,522° | 1 à 4 | oui |
| 8 | S^7 | 83,738° | 82,819° | 1 à 7 | oui |
| 24 | S^23 | 87,731° | 87,612° | 4 à 17 | oui |

- Toute la clôture est broutée (multiplicité ≥ 1), deux chèvres voisines se recouvrent, et aucun point n'est brouté par les n + 1 à la fois (ils ne peuvent pas être à moins de 90° de tous les sommets). Les intersections de calottes de moins de 90° sont convexes : c'est un bon recouvrement.
- La chèvre broute toujours un peu plus que arccos(1/(n + 1)), au-dessus du seuil arccos(1/n) : le recouvrement marche dans toutes les dimensions. En dimension infinie, α → 90° : chaque chèvre broute un hémisphère.

**La cohomologie de Čech du nerf** (le faisceau constant ℤ ; le nerf de n + 1 chèvres est le bord du simplexe à n + 1 sommets) :

| clôture | chèvres | cochaînes par degré | Betti b₀ … b_{n−1} | χ |
|---|---:|---|---|---:|
| S^1 | 3 | 3, 3 | 1, 1 | 0 |
| S^2 | 4 | 4, 6, 4 | 1, 0, 1 | 2 |
| S^3 | 5 | 5, 10, 10, 5 | 1, 0, 0, 1 | 0 |
| S^4 | 6 | 6, 15, 20, 15, 6 | 1, 0, 0, 0, 1 | 2 |
| S^5 | 7 | 7, 21, 35, 35, 21, 7 | 1, 0, 0, 0, 0, 1 | 0 |
| S^6 | 8 | 8, 28, 56, 70, 56, 28, 8 | 1, 0, 0, 0, 0, 0, 1 | 2 |
| S^7 | 9 | 9, 36, 84, 126, 126, 84, 36, 9 | 1, 0, 0, 0, 0, 0, 0, 1 | 0 |
| S^8 | 10 | 10, 45, 120, 210, 252, 210, 120, 45, 10 | 1, 0, 0, 0, 0, 0, 0, 0, 1 | 2 |

- On retrouve H⁰ = H^{n−1} = ℤ et rien entre les deux : la cohomologie de la sphère, calculée avec des chèvres.
- χ(S^k) = 1 + (−1)^k : 2 pour les sphères paires, 0 pour les impaires.

**Les deux cartes de la sphère.** Projeter S^n depuis le pôle nord N sur le plan de l'équateur, c'est l'inversion de centre N et de rayon √2 : elle fixe l'équateur (à distance √2 de N). Vérifications (1000 points au hasard par dimension) :

| n | carte sud ∘ (carte nord)⁻¹ = inversion y ↦ y/\|y\|² | inversion de rayon √2 = carte nord | hémisphère sud → dedans, nord → dehors |
|---:|---|---|---|
| 1 | oui | oui | oui |
| 2 | oui | oui | oui |
| 3 | oui | oui | oui |
| 8 | oui | oui | oui |
| 24 | oui | oui | oui |

- Chaque carte manque un seul point ; les deux se recouvrent sur ℝⁿ privé de 0, et on passe de l'une à l'autre par l'inversion. Les deux hémisphères ont chacun la moitié de l'aire : l'un tombe dans le disque unité, l'autre dehors.
- Mayer–Vietoris sur ces deux cartes donne H^k(S^n) = H^{k−1}(S^{n−1}) : la cohomologie monte d'une dimension à la suivante en partant de S⁰, deux points.

**Pair et impair : où vit i.** Une rotation J de ℝ^m avec J² = −1 (un « i ») n'existe que si m est pair (det J² = (−1)^m). Sur une sphère impaire S^(m−1), x ↦ J·x est un champ tangent qui ne s'annule jamais ; sur une sphère paire, tout champ s'annule quelque part (χ = 2, la boule chevelue).

| sphère | χ | champs indépendants (Radon–Hurwitz) | parallélisable |
|---|---:|---:|---|
| S^1 | 0 | 1 | oui |
| S^2 | 2 | 0 | non |
| S^3 | 0 | 3 | oui |
| S^4 | 2 | 0 | non |
| S^5 | 0 | 1 | non |
| S^6 | 2 | 0 | non |
| S^7 | 0 | 7 | oui |
| S^8 | 2 | 0 | non |
| S^15 | 0 | 8 | non |
| S^23 | 0 | 7 | non |
| S^24 | 2 | 0 | non |

- Les seules sphères parallélisables sont S¹, S³ et S⁷ : celles des nombres complexes, des quaternions et des octonions (dimensions 2, 4 et 8). La formule a une période 8 (Bott).

## 4. Le losange de √2 dans la figure de diffraction

Étoile de Siemens de la partie XVIII (72 rayons) : les fantômes sont au réseau inversé (N/2π)·(m₂, −m₁)/|m|².
- Couche |m| = 1 : 4 fantômes sur les axes, à 11,459 pixels du centre : les sommets d'un losange.
- Couche |m| = √2 : 4 fantômes sur les diagonales, à 8,103 pixels : exactement les milieux des côtés du losange, sur son cercle inscrit.
- Rayon inscrit / rayon circonscrit = 1/√2 : le disque inscrit a exactement la moitié de l'aire du disque circonscrit.
- À l'échelle d'un pixel tourné de 45°, ce losange a une hauteur √2 et un côté 1. À l'échelle du pré (sommets sur le cercle unité), son côté vaut √2 : la corde de la chèvre de dimension infinie.

**Le retournement.** Avant inversion, la couche √2 du réseau (±1, ±1) forme un carré dont les milieux des côtés sont la couche 1. Après inversion, c'est l'inverse : la couche 1 donne les sommets, la couche √2 les milieux. L'inversion échange sommets et milieux.

**En dimension n**, la couche 1 de ℤⁿ inversée donne les 2n sommets du polytope croisé (arêtes √2), et la couche √2 inversée donne exactement les milieux de ses arêtes, à 1/√2 du centre :

| n | sommets ±e_i | arêtes (= couche √2 inversée) | toutes les arêtes valent √2 | milieux à 1/√2 |
|---:|---:|---:|---|---|
| 2 | 4 | 4 | oui | oui |
| 3 | 6 | 12 | oui | oui |
| 4 | 8 | 24 | oui | oui |
| 8 | 16 | 112 | oui | oui |

- 24 arêtes en dimension 4 et 112 en dimension 8 : ce sont les racines des réseaux D₄ et D₈ (§ 5).

**Le retournement de l'aiguille.** Retourner une aiguille, c'est −1 = i·i : deux quarts de tour, en passant par une direction perpendiculaire (un sommet voisin du losange, à distance √2). En dimension 2, il y a deux chemins (par i ou par −i, comme 3 et 7 modulo 10). En dimension n, toute direction de la sphère S^(n−2) perpendiculaire convient : un cercle en 3D, une infinité de chemins en dimension infinie.

## 5. 3, 8, 24 : le trou profond √n/2

Le centre d'un cube de ℤⁿ (le centre du pixel vu de ses coins) est à √n/2 des coins.

| n | 2 | 3 | 4 | 8 | 16 | 24 |
|---|---|---|---|---|---|---|
| √n/2 | 0,7071 | 0,8660 | 1,0000 | 1,4142 | 2,0000 | 2,4495 |

- n = 2 : 1/√2 (le rayon du demi-disque). n = 4 : 1. n = 8 : √2, la diagonale 1x, 1y.
- En dimension 8, le centre du cube est donc aussi loin que les voisins les plus proches de D₈ (les vecteurs ±e_i ± e_j, de longueur √2). On peut l'ajouter : E₈ = D₈ ∪ (D₈ + ½·(1, …, 1)), la grille décalée d'une demi-maille (partie XV). Ses vecteurs les plus courts : 112 + 128 = 240, le nombre de sphères qui touchent une sphère dans le meilleur empilement de dimension 8.
- En dimension 4, les racines de D₄ sont 24 : 24 sphères touchent une sphère (Musin, 2003).
- Le meilleur empilement de sphères n'est démontré qu'en dimensions 1, 2, 3, 8 et 24 (Hales en 3, Viazovska en 8, Cohn, Kumar, Miller, Radchenko et Viazovska en 24).

## 6. La géométrie dans la musique et dans l'IA

**2 et 3 donnent 12.** log₂ 3 = 1,584962501 = [1 ; 1, 1, 2, 2, 3, 1, 5, 2, 23, …]. Réduites : 1/1, 2/1, 3/2, 8/5, 19/12, 65/41, 84/53, 485/306…
- 19/12 : 3¹² ≈ 2¹⁹, douze quintes ≈ sept octaves. L'écart est le comma pythagoricien 531441/524288 = 1,013643, soit 23,46 cents.
- La quinte tempérée 2^(7/12) = 1,498307 est trop basse de 1,955 cent. Les réduites suivantes donnent les gammes à 41 et 53 notes.
- Le cercle des quintes est une rotation irrationnelle, comme le cercle des décades (partie XIX). Théorème des trois distances, pour N quintes ramenées dans l'octave :

| N notes | longueurs de pas (en cents) |
|---:|---|
| 5 | 203,91 ; 294,13 |
| 6 | 90,22 ; 203,91 ; 294,13 |
| 7 | 90,22 ; 203,91 |
| 8 | 90,22 ; 113,69 ; 203,91 |
| 12 | 90,22 ; 113,69 |
| 41 | 23,46 ; 43,30 |
| 53 | 19,84 ; 23,46 |

- 5 (pentatonique), 7 (diatonique) et 12 (chromatique) n'ont que deux tailles de pas ; 6 et 8 en ont trois.

**L'IA et √2.** Deux vecteurs unitaires tirés au hasard en dimension d sont à distance √(2 − 2t), où t = u·v suit la densité ∝ (1 − t²)^((d−3)/2), celle de l'ombre de la sphère (§ 2). Mesures (2·10⁴ paires par dimension) :

| d | distance moyenne | écart-type | 1/√(2d) |
|---:|---|---|---|
| 2 | 1,2745 | 0,6132 | 0,5000 |
| 3 | 1,3274 | 0,4732 | 0,4082 |
| 10 | 1,3969 | 0,2346 | 0,2236 |
| 100 | 1,4125 | 0,0715 | 0,0707 |
| 1000 | 1,4140 | 0,0223 | 0,0224 |
| 4096 | 1,4141 | 0,0110 | 0,0110 |

- En grande dimension, deux directions sans rapport sont presque perpendiculaires, à distance √2 : la corde de la chèvre de dimension infinie. C'est ce qui permet à un réseau de neurones de ranger beaucoup plus de notions que de dimensions (la « superposition »).

## 7. 10⁻⁵⁰ : une précision, et une échelle physique

**Comme précision.** Les cordes du § 1 sont encadrées à 10⁻⁵⁰ près. Un grain de 10⁻⁵⁰ sur un pré de rayon 1 demande :
- 166,1 chiffres en base 2 ; 50,0 chiffres en base 10 ; 46,3 chiffres en base 12 ; 28,1 chiffres en base 60.

**Comme échelle physique** (CODATA 2018). La longueur de Planck vaut 1,6163·10⁻³⁵ m ; 10⁻⁵⁰ m en est 6,19·10⁻¹⁶.
- Pour sonder 10⁻⁵⁰ m, il faut une onde de cette longueur : un photon de 1,99·10²⁵ J. Son rayon de Schwarzschild serait 3,28·10⁻¹⁹ m, 3,3·10³¹ fois la région sondée : la mesure créerait un trou noir qui la cache.
- Ce rayon égale la longueur d'onde vers 5,73·10⁻³⁵ m, soit 3,54 longueurs de Planck (√(4π)) : en dessous, aucune mesure de position n'est possible dans la physique connue.
