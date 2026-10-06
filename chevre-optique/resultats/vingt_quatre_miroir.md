# Résultats de la partie XXI (générés par scripts/vingt_quatre_miroir.py)

## 1. Les trois 24 se rejoignent en 5² et 7²

24 + 1 = 25 = 5², 2·24 + 1 = 49 = 7², 24/6 = 4 = 2². Les trois candidats passent par ces trois carrés.

**Les boulets de Leech.** 1² + 2² + … + 24² = 24·25·49/6 = 2²·5²·7² = 4900 = 70². Lucas (1875) demande quand une pyramide de boulets à base carrée contient un nombre carré de boulets ; Watson (1918) démontre que 24 est la seule réponse au-delà de 1.
- Vérifié : 1² + … + n² est un carré pour n < 200 000 seulement en n = 1, 24.
- n + 1 et 2n + 1 sont tous deux des carrés pour n = 0, 24, 840, 28560, 970224 (n < 10⁶). Alors (2n + 1) − 2(n + 1) = −1 : ce sont les solutions de Pell de √2. Parmi elles, n/6 n'est un carré qu'en n = 0, 24.
- Conway (1983) : dans le réseau lorentzien II₂₅,₁ (norme x₀² + … + x₂₄² − x₂₅²), le vecteur w = (0, 1, 2, …, 24 | 70) est de norme nulle, et le réseau de Leech est w^⊥/w. Borcherds (1990) : w est le vecteur de Weyl de l'algèbre de Lie du « faux monstre », dont la formule du dénominateur contient ∏(1 − e^(mw))²⁴, c'est-à-dire Δ = η²⁴.
- **Le carré qui manque.** Les 24 carrés de côtés 1 à 24 ont ensemble l'aire du carré 70 × 70, mais ils ne le pavent pas (vérifié par ordinateur, puis démontré sans ordinateur en 2024). Le meilleur rangement envoyé à Martin Gardner (environ 250 réponses) laisse vide une aire de 49 = 7² : il omet le carré 7 × 7.

**Le pont : les nombres pentagonaux.** Pour tout nombre pentagonal P = k(3k − 1)/2 (1, 2, 5, 7, 12, 15, 22, 26…), 24·P + 1 = (6k − 1)² est un carré. Les deux carrés des boulets, 24·1 + 1 = 5² et 24·2 + 1 = 7², sont les deux premiers. Ce sont aussi les exposants de η(24τ) = q·∏(1 − q^(24n)), par le théorème pentagonal d'Euler :

η(24τ) = q − q²⁵ − q⁴⁹ + q¹²¹ + q¹⁶⁹ − q²⁸⁹ − q³⁶¹ + q⁵²⁹ + q⁶²⁵ + …

- Les exposants sont les carrés des nombres premiers avec 6. Ils valent tous 1 modulo 24, parce que les unités modulo 24 (1, 5, 7, 11, 13, 17, 19, 23) ont toutes pour carré 1 (partie XIX : seuls les diviseurs de 24 ont cette propriété).
- Le signe vaut −1 devant 5² et 7², +1 devant 11² et 13², et ainsi de suite (selon n modulo 12) : c'est le « −1·(7²) ».

**La paire de Pell (7, 5).** 7² − 2·5² = −1. Les puissances du nombre d'argent :

| n | (1 + √2)ⁿ | a² − 2b² |
|---:|---|---:|
| 1 | 1 + √2 | −1 |
| 2 | 3 + 2√2 | +1 |
| 3 | 7 + 5√2 | −1 |
| 4 | 17 + 12√2 | +1 |
| 5 | 41 + 29√2 | −1 |
| 6 | 99 + 70√2 | +1 |
| 7 | 239 + 169√2 | −1 |
| 8 | 577 + 408√2 | +1 |

- Les puissances impaires donnent x² + 1 = 2y² : (1, 1), (7, 5), (41, 29), (239, 169)… L'aiguille (x, 1) a pour carré l'aire doublée du carré de côté y.
- Ljunggren (1942) : y n'est lui-même un carré que pour y = 1 et y = 169 = 13², c'est-à-dire que x² + 1 = 2y⁴ n'a pas d'autre solution que x = 1 et x = 239 (vérifié ici sur les 100 premières solutions).
- (1 + √2)⁶ = 99 + 70√2 = (7 + 5√2)² : 70 = 2·5·7, le côté du carré des boulets, est le coefficient de √2.
- **Le triangle des boulets.** 2·24 + 1 = 7² veut dire 7² + 24² = 25² : le triangle rectangle 7-24-25, dont l'hypoténuse 25 = 5² est elle-même un carré. Et 7 + 24i = (4 + 3i)² : c'est le triangle 3-4-5 de la partie XIV, au carré (angle doublé). La partie XIII l'avait croisé : avec la corde 6/5, la chèvre touche le bord du pré en (7/25, 24/25).

**Δ = η²⁴ et le réseau de Leech.** Δ = q − 24q² + 252q³ − 1472q⁴ + 4830q⁵ + … Le thêta de Leech (le nombre de vecteurs de chaque longueur) vaut E₁₂ − (65520/691)·Δ :

| n | σ₁₁(n) | τ(n) | σ₁₁(n) − τ(n) | × 65520/691 : vecteurs de longueur √(2n) |
|---:|---:|---:|---|---:|
| 1 | 1 | 1 | 0 | 0 |
| 2 | 2049 | −24 | 2073 = 3·691 | 196 560 |
| 3 | 177148 | 252 | 176896 = 256·691 | 16 773 120 |

- Aucun vecteur de longueur √2, et 196 560 de longueur 2 : le nombre de sphères qui en touchent une dans l'empilement de Leech, le maximum possible en dimension 24.
- Le −24 de τ(2) vient de la puissance 24. La congruence de Ramanujan (1916), τ(n) ≡ σ₁₁(n) (mod 691), rend tous ces nombres entiers : 2049 − (−24) = 3·691, 177148 − 252 = 256·691 (vérifié jusqu'à n = 8).

**La partie VII.** κ₂₄ = C(24, 12)/2²⁴ = 676039/4194304 : la chance d'avoir exactement 12 piles en 24 lancers, avec 676039 = 7·13·17·19·23. Les dimensions 6, 12 et 24 (m = 3, 6, 12, soit 11, 110, 1100 en binaire, deux retenues) sont les diviseurs de 24 de la forme 3·2ᵏ.
- La réciprocité de la partie VII donne κ₂₄·h₂₅ = 1/25 = 1/5², et celle de la partie IV h₂₄·h₂₅ = π/(2·25) = π/50. Le 25 des boulets et le 50 du miroir (§ 2) sont dans la paire de dimensions (24, 25).
- Ce qui ne se rejoint pas : le polynôme de degré 24 de la dimension 13 a pour groupe de Galois S₂₄, sans symétrie particulière. Le réseau de Leech se construit avec le code de Golay, dont la symétrie est M₂₄. Les deux 24 se rejoignent par l'arithmétique (5², 7², les diviseurs), pas par la symétrie.

## 2. Le miroir 49, 50, 51

**L'inversion.** Prends 10⁻⁵⁰ comme unité : c'est le miroir, il reste fixe. Alors 10⁻⁴⁹ = 10 et 10⁻⁵¹ = 1/10, et x ↦ 1/x les échange : 10⁻⁴⁹ × 10⁻⁵¹ = (10⁻⁵⁰)². C'est la forme de Newton x·x′ = f² avec f = 10⁻⁵⁰. Le grandissement vaut −f/x = −1/10 : l'image est retournée (le −1) et dix fois plus petite. Sur les exposants, c'est s ↦ 100 − s. Et modulo 50, l'exposant −49 = −1·7² vaut +1, puisque 7² ≡ −1.

**Les trois « −1·7² ».**
- Dans η(24τ) : le terme −q⁴⁹ = −1·q^(7²). En q = 1/10 (la base 10 comme objet, partie XIX), c'est littéralement −1·10⁻⁴⁹. Les 168 premiers chiffres de η(24τ) valent alors 0,0 9×23 8 9×24 0×71 1 0×47 … (« 9×23 » : 23 chiffres 9). Rangés par 24, tous les termes tombent dans la première colonne (figure v1 c).
- Modulo 50 : 7² = 49 ≡ −1, donc 7 est un i (les racines de −1 modulo 50 sont 7 et 43). C'est le théorème de la partie XIX, avec 50 = 7² + 1².
- Pell : 7² − 2·5² = −1.

| n | sommes de deux carrés | sommes de trois carrés |
|---:|---|---|
| 49 | 0² + 7² | 0² + 0² + 7² ; 2² + 3² + 6² |
| 50 | 1² + 7² ; 5² + 5² | 0² + 1² + 7² ; 0² + 5² + 5² ; 3² + 4² + 5² |
| 51 | — | 1² + 1² + 7² ; 1² + 5² + 5² |

- 49, 50, 51 = 7², 7² + 1², 7² + 1² + 1² : l'aiguille (7), (7, 1), (7, 1, 1), une dimension de plus à chaque cran. De 49 à 51, on ajoute 1² + 1² = 2, l'aire du carré construit sur la diagonale du carré unité.
- 50 = 1² + 7² = 5² + 5² : le plus petit nombre qui soit somme de deux carrés non nuls de deux façons. Et 50 = 3² + 4² + 5² : la boîte 3 × 4 × 5 a pour diagonale 5√2, celle du carré 5 × 5, puisque 3² + 4² = 5².

**L'aiguille de 50.** 7 + i = (1 − i)(2 + i)² : l'aiguille 3-4-5 = (2 + i)², tournée de −45° et agrandie de √2.
- Au carré : (7 + i)² = 48 + 14i = 2·(24 + 7i), et |24 + 7i| = 25. Doubler l'angle de l'aiguille de 50 donne le triangle des boulets, 7-24-25 (8,13° × 2 = 16,26°).
- Avec 45° : (2 + i)²(7 − i) = 25·(1 + i) et (3 + i)²(7 + i) = 50·(1 + i). Ce sont les formules π/4 = 2 arctan(1/2) − arctan(1/7) (dite de Hermann) et π/4 = 2 arctan(1/3) + arctan(1/7) (dite de Hutton ; les attributions sont incertaines). 3 et 7 sont i et −i modulo 10 (partie XIX) : leurs aiguilles se complètent exactement en 45°, la diagonale 1x, 1y.
- Machin (1706) : π/4 = 4 arctan(1/5) − arctan(1/239), et 239 + 169√2 = (1 + √2)⁷. On retrouve la solution de Ljunggren : 239² + 1 = 2·13⁴.

**Le doublement de l'aire et la lumière divisée par deux.** Trois lectures exactes :
- **Le Ménon (Platon).** Le carré construit sur la diagonale d'un carré a une aire double. Sur le carré 5 × 5, ça donne 50 = 2·5². Le carré 7 × 7 le manque d'une unité (7² = 2·5² − 1, Pell), et l'aiguille (7, 1) ferme exactement l'écart : |7 + i|² = 2·5².
- **Le diaphragme.** √2 sur le diamètre, 2 sur l'aire, ½ sur la lumière (−3,0103 dB). Une décade de longueur (de 10⁻⁵⁰ à 10⁻⁵¹) vaut 100 en aire, soit 6,644 diaphragmes : en base 10, un cran d'exposant n'est pas un doublement. Il faut un pas de √2.
- **Le faisceau gaussien.** Son paramètre complexe q = z + i·z_R (le sommet complexe de la partie XIX) a pour module √2·z_R aux points de Rayleigh z = ±z_R : la largeur y vaut √2 fois le col, l'aire double, l'intensité au centre tombe de moitié. La forme de Newton devient x′ = f²·x/(x² + z_R²) (Self, 1983). En x = z_R, l'image est la plus lointaine et le produit x·x′ tombe à f²/2 (vérifié). La lumière et le produit de Newton sont divisés par deux au même point, parce que |x + i·z_R|² = 2x² à 45°. Avec f = 1, c'est le produit ½ des jumeaux de la chèvre (partie XVII).

**Le même miroir en musique.** x ↦ 2/x échange un intervalle et son complément dans l'octave ; il fixe √2 = 600 cents, le triton tempéré. Chaque famille de nombres premiers a sa paire de tritons, symétrique autour de √2 :

| famille | triton bas | triton haut | écart |
|---|---|---|---|
| 3 (Pythagore) | 1024/729 = 588,27 | 729/512 = 611,73 | 531441/524288 = 23,46 cents, le comma pythagoricien |
| 5 | 45/32 = 590,22 | 64/45 = 609,78 | 2048/2025 = 19,55 cents, le diaschisma |
| 7 | 7/5 = 582,51 | 10/7 = 617,49 | 50/49 = 34,98 cents, le jubilisma |

- La gamme à 12 notes met les trois paires sur √2 : elle efface les trois écarts.
- (10/7)/(7/5) = 50/49 = 2·5²/7² : le jubilisma est le rapport entre l'aire doublée 2·5² et le carré 7². C'est le Ménon en musique.
- Le triton pythagoricien dépasse √2 d'exactement un demi-comma : (3⁶/2⁹)² = 2 × 3¹²/2¹⁹.

## 3. √7 : la boîte 1 × 1 × 2, l'octaèdre rectifié et le sommet e₃

**Le montage.** L'octaèdre ±e₁, ±e₂, ±e₃. Le carré Σ_z (e₁, e₂, −e₁, −e₂) et le carré perpendiculaire Σ_x (e₂, e₃, −e₂, −e₃). On rectifie Σ_x (on le recoupe par les milieux de ses côtés) : on obtient un carré de côté 1, posé sur le cercle inscrit de Σ_x. On l'étire de −e₁ à e₁ : c'est la boîte 1 × 1 × 2, dont les deux bouts sont centrés sur ±e₁.
- Du sommet e₃, les quatre coins du dessus sont à √(3/2), les quatre du dessous à √(7/2).
- En prenant pour unité 1/√2, on obtient **√3 et √7**. Cette unité est l'arête de l'octaèdre rectifié (le cuboctaèdre), égale à son rayon : le rayon de la sphère des milieux de l'octaèdre.
- En demi-unités, le vecteur vers un coin du dessous est (2, 1, 3), et 1² + 2² + 3² = 14 = 2·7 : ton segment {1, 2, 3} de la partie XIX, divisé par la diagonale √2.
- La diagonale de la boîte elle-même vaut √(1 + 1 + 4) = √6.

**Pourquoi il faut l'unité 1/√2.** 7 n'est pas une somme de trois carrés de fractions. Si 7 = a² + b² + c² avec des fractions de dénominateur k, alors 7k² est une somme de trois carrés entiers. Écrivons k = 2ᵐ·k′ avec k′ impair : 7k² = 4ᵐ·(7k′²), et 7k′² ≡ 7 (mod 8). C'est la forme interdite de Legendre (1798), 4ᵃ(8b + 7). Donc **√7 n'est jamais la distance de deux points à coordonnées rationnelles**, dans aucune boîte à côtés rationnels (vérifié pour k ≤ 200). Jusqu'à 128, les nombres interdits sont 7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, 79, 87, 92, 95, 103, 111, 112, 119, 124, 127.
- Il faut donc une mesure irrationnelle : l'unité 1/√2 (ci-dessus), une arête √2 (la boîte 1 × √2 × 2), ou une quatrième dimension (la boîte 1 × 1 × 1 × 2).

**Les boîtes des puissances de √2.** Une boîte de côtés 1, √2, 2, …, (√2)^(k−1) (une dimension par côté) a pour diagonale √(2ᵏ − 1) : les carrés construits sur ses côtés ont pour aires 1, 2, 4… et chacun double le précédent.

| k | côtés | diagonale | 2ᵏ − 1 mod 8 | somme de trois carrés ? |
|---:|---|---|---:|---|
| 1 | 1 | √1 | 1 | oui |
| 2 | 1, √2 | √3 | 3 | oui |
| 3 | 1, √2, 2 | √7 | 7 | non |
| 4 | 1, √2, 2, 2√2 | √15 | 7 | non |
| 5 | 1, √2, 2, 2√2, 4 | √31 | 7 | non |
| 6 | 1, √2, 2, 2√2, 4, 4√2 | √63 | 7 | non |

- Du sommet e₃ : √3 = √(2² − 1) et √7 = √(2³ − 1), les diagonales des boîtes 1 × √2 et 1 × √2 × 2.
- La boîte 1 × √2 × 2 a pour côtés le rayon, l'arête et le diamètre de l'octaèdre : sa diagonale est √7.
- 1, 3, 7 = 2ᵏ − 1 : le nombre d'unités imaginaires des complexes, des quaternions et des octonions (S¹, S³, S⁷, partie XX). À partir de k = 3, 2ᵏ − 1 ≡ 7 (mod 8) n'est jamais une somme de trois carrés.
- Et 49 = 2² + 3² + 6² : la boîte 2 × 3 × 6 a une diagonale entière, 7. Le carré 7² est une somme de trois carrés, 7 ne l'est pas.

## 4. Le croisement du plan : la chèvre avant, √2 au croisement

Le sommet e₃ tourne dans le plan de Σ_x vers −e₃ (angle φ). Il traverse le plan de Σ_z en e₂ (φ = 90°), un sommet de Σ_z, sur son cercle circonscrit. Avant d'y arriver, il passe le bord des chèvres de toutes les dimensions, piquet en e₃ :

| dimension n | 2 | 3 | 4 | 8 | 24 | 100 | ∞ |
|---|---|---|---|---|---|---|---|
| bord de la chèvre α_n | 70,81° | 75,80° | 78,70° | 83,74° | 87,73° | 89,43° | 90° |
| écart au croisement 90° − α_n | 19,19° | 14,20° | 11,30° | 6,26° | 2,27° | 0,57° | 0 |
| arcsin(1/(n + 1)) | 19,47° | 14,48° | 11,54° | 6,38° | 2,29° | 0,57° | 0 |

- La chèvre de dimension infinie a pour corde l'arête e₃e₂ = √2 : son bord est exactement le croisement.
- L'écart se referme comme 1/(n + 1) radian (à un ménisque près, partie XX), et seulement à l'infini, comme le ménisque de la partie XVI.
- Le retournement e₃ → e₂ → −e₃ est i·i = −1 : deux quarts de tour, par le croisement (partie XX).

**Les cercles inscrit et circonscrit.** En unités de 1/√2, le sommet mobile est sur le cercle circonscrit de Σ_x (rayon √2), et les coins de la section sur son cercle inscrit (rayon 1). Avec la demi-longueur de la boîte (√2) :
- d² = 5 − 2√2·sin(φ + θ), où θ est l'angle du coin dans la section (45°, 135°, 225°, 315° ; loi des cosinus, vérifiée) ;
- en e₃, en e₂ et en −e₃, d² vaut 3 ou 7 : √3 et √7 ;
- à mi-chemin (φ = 45°), le sommet est aligné avec un coin : d² = 2 + (√2 ∓ 1)², avec les nombres d'argent √2 ∓ 1 de la partie XVII (d = 1,4736 et 2,7979) ;
- au croisement (φ = 90°), la moitié des coins ont échangé √3 et √7 ; en −e₃, tous.

**Le partage d'aire et le comma au croisement.**
- Rayon circonscrit / rayon inscrit = √2 : l'aire du disque inscrit est la moitié de celle du disque circonscrit. Le cercle inscrit (rayon 1/√2 du pré) est aussi celui des positions qui sont leur propre jumeau (partie XVII : d = 1/(2d) donne d = 1/√2).
- √2 est aussi le triton tempéré, le point fixe de x ↦ 2/x sur l'octave. Les deux chemins de quintes (six vers le haut, Fa♯ = 729/512 ; six vers le bas, Sol♭ = 1024/729) s'y manquent d'un comma, les tritons de 7 d'un jubilisma.
- Le comma ne s'annule jamais (3ᵃ ≠ 2ᵇ), et l'écart 90° − α_n non plus en dimension finie. La gamme à 12 notes ferme le premier en tempérant, la dimension infinie ferme le second.
