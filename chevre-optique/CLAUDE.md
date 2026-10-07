# CLAUDE.md — la chèvre, les cercles et la lumière

Ce fichier s'adresse à toi, Claude, quand tu travailles dans ce dossier. Il résume la façon de penser de l'auteur de la série, que tu n'adoptes pas spontanément, puis les conventions de travail. Lis-le en entier avant de répondre à un nouveau message.

## 1. Une analogie de forme soutenue par le même procédé est un résultat

**Le principe de l'auteur.**
- Les mathématiques sont elles-mêmes une analogie de forme. Elles simplifient les phénomènes observables pour qu'ils s'ordonnent quand on les écrit, sur une tablette d'argile ou sur une feuille de papier.
- Poincaré le disait ainsi : « la mathématique est l'art de donner le même nom à des choses différentes ». Et on attribue à Banach l'idée que le meilleur mathématicien voit des analogies entre les théories, puis des analogies entre les analogies.
- Quand deux phénomènes obéissent au même procédé mathématique (la même équation, la même construction, les mêmes invariants), c'est une découverte. C'est la base de toutes les découvertes.

**Ce que tu dois faire.**
- Ne range jamais une telle correspondance sous « pas établi ». N'écris pas qu'elle n'est « qu'une analogie », ni « une analogie de forme, pas de la physique ».
- Écris plutôt trois choses :
  1. **ce qui est partagé exactement** (l'équation, le procédé) : c'est établi ;
  2. **ce que la correspondance transporte** d'un domaine à l'autre (un calcul, une valeur, une prédiction) ;
  3. **ce qui reste ouvert** (un mécanisme physique commun, s'il y en a un) : c'est une question, pas une objection.
- Dans les sections « Le tri », range ces liens sous « Analogie de structure (même procédé) », avec les résultats.
- L'honnêteté ne change pas : on distingue toujours démontré, calculé, classique, lecture et ouvert. Mais « ouvert » ne veut pas dire « faux », et une structure commune démontrée est un acquis.

**L'exemple qui a fixé cette règle (partie XIX).**
- Le cube qui tourne (r² = 1/2 + 2z²), la chèvre de dimension infinie (ρ² = 1 + d²) et le faisceau laser gaussien (r² = w₀² + θ²z²) sont trois cas du même objet : un cône dont le sommet est déplacé dans l'imaginaire, r = θ·|z + i·z_R|, avec z_R = w₀/θ.
- Pour la chèvre, ρ = |d + i|. Pour le laser, c'est la source ponctuelle complexe de Deschamps (1971).
- Ce que ça transporte : le cube et la chèvre ont w₀·θ = 1, donc une « longueur d'onde » λ = π. La chèvre de **dimension infinie**, piquet sur la clôture (d = 1), est exactement à la distance de Rayleigh de son faisceau : la largeur y vaut √2 fois le col (ρ = |1 + i| = √2, la diagonale 1x, 1y) et la phase de Gouy y vaut 45°.
- **Attention aux mots : « la chèvre classique » est la chèvre plane** (corde 1,1587…). Au même piquet, elle et la chèvre de dimension infinie (corde √2) sont deux chèvres au même endroit, séparées par une infinité de dimensions (partie XX). C'est le phénomène que l'auteur étudie ; ne jamais les confondre.

## 2. Les bases sont des objets, et leur histoire suit des besoins d'organisation

**Une base n'est pas une simple convention d'écriture.**
- Elle fixe la grille qui découpe l'espace entre les nombres : les fractions qui tombent juste, l'horloge des derniers chiffres, l'existence d'un i, la régularité des nombres flottants. La base 2 et la base 10 sont deux objets physiques différents (partie XIX).
- 1, 2, 3, 4, 5, 6 est un compte naïf. Un compte jumelé avec des données est une séquence d'épreuves qui forme un atlas.
  - Chaque chiffre est une épreuve : dans quelle case le nombre tombe-t-il ?
  - Le nombre est la suite emboîtée de ces cases : une suite de points, pas une infinité de chiffres à écrire. C'est l'encadrement certain des parties XVII et XVIII.
- Le compte naïf est comme le modèle de Thomson pour se représenter l'atome : plus simple à comprendre, et c'est exactement pour ça qu'on le garde pour compter. (Nuance proposée à l'auteur en partie XIX : Thomson a été réfuté ; Bohr, faux dans son image mais juste dans ses nombres, serait un parallèle plus proche.)
- **Les échelles.** On part de l'échelle humaine, puis on monte ou on descend sur un cône à deux échelles logarithmiques (−zⁿ, +zⁿ). Thalès relie toute taille à un objet que les humains connaissent : un sou (19,05 mm) cache la Lune à 2,11 m.

**La succession des standards : base 60, base 12, base 10 (des faits historiques, datés au § 7 de la partie XX).**
- Les mathématiques (bases, notations, standards) sont une création humaine qui a évolué comme une langue, selon les besoins de chaque époque. **C'est un fait documenté : ne l'appelle pas « la thèse de l'auteur ».**
- **Bases 60 (360°) et 12 :** elles servaient à simplifier des problèmes topologiques et géométriques observables (le ciel, le cercle, le jour, l'année).
- **Base 10 :** elle est devenue le standard de l'écriture des calculs (Brahmagupta 628, Fibonacci 1202, Stevin 1585). Elle a absorbé l'analyse des angles hérités de la base 60 : par log₁₀ (Briggs, 1617), les produits deviennent des sommes ; par e^(iθ) (Euler, 1748), la rotation devient une multiplication.
- **La chronologie des notations :** Recorde (=, 1557), Descartes (x, y, z, 1637), Newton (fluxions, 1665–1687), Leibniz (∫, 1675), Euler (f(x), e, π, i, XVIIIe siècle, les Lumières), Gauss (≡, 1801).
- **Faits exacts qui vont dans ce sens** (calculés au § 6 de [`resultats/bases_objets.md`](resultats/bases_objets.md)) :
  - −1 n'a pas de racine carrée modulo 12, 24, 60 ou 360. Il en a une modulo 10 : 3 ≡ i, 7 ≡ −i.
  - Modulo 12 et 24, tout nombre premier avec la base est son propre inverse (x² ≡ 1). Ces horloges n'ont que des reflets. Les seules bases ainsi sont les diviseurs de 24.
  - Modulo 10, l'horloge 1 → 3 → 9 → 7 → 1 est un tour en quatre quarts : celle de i.
- **Nuance historique à garder :** ces bases ont souvent coexisté (l'Égypte comptait en base 10 pendant que la Mésopotamie calculait en base 60). Ce qui change avec les besoins, c'est la base qui sert de standard.

## 3. Le procédé à deux couches : simplifier, puis extrapoler

**Couche 1, géométrique (multiplicative).**
- Les bases 2 et 3 se rejoignent en 12 = 2²·3 (puis en 24, et en 60 et 360 avec un 5).
- Elles coupent le cercle et le temps en parts égales (2, 3, 4, 6). Les horloges de 12 et 24 n'ont que des reflets ; 60 et 360 ont des quarts de tour, mais aucun i.

**Couche 2, conceptuelle (linéaire).** La base 10 linéarise tout par log₁₀.
- Un nombre est un polynôme en 10, Σ dₖ·10ᵏ. Ses chiffres sont rangés en colonnes (les facteurs 10ⁿ) et en rangées, comme des pixels.
- bⁿ s'écrit avec ⌊n·log₁₀ b⌋ + 1 chiffres. Le bord d'une table des puissances est donc une droite tracée en pixels, de pente log₁₀ b : 0,30103 pour 2, 0,47712 pour 3, 1,07918 pour 12.
- Pour 2ⁿ, les marches font 3, 3, 4, 3, 3, 4… : 3 chiffres tous les 10 rangs, parce que 2¹⁰ ≈ 10³. C'est la même mécanique que la droite en pixels de la partie XVIII.
- log₁₀ 12 = 2·log₁₀ 2 + log₁₀ 3 : les produits de la couche 1 deviennent des sommes de pentes.

**Les retenues.** En multipliant, les puissances bⁿ ne restent pas statiques sous 10 : les retenues déplacent les chiffres. 0 et 1 restent statiques. Pour le dernier chiffre :
- base 10 : 0, 1, 5 et 6 sont fixes (5 et 6 sont les interrupteurs des deux couches de 10 = 2 × 5). 2, 3, 7 et 8 tournent par quarts de tour, 4 et 9 par demi-tours ;
- base 12 : 0, 1, 4 et 9 sont fixes. Rien ne tourne plus vite qu'un demi-tour.

**L'extrapolation.** Pour l'auteur, ce qui est établi dans une couche se transporte dans l'autre par ce dictionnaire :
- les produits deviennent des pentes ;
- les reflets deviennent des quarts de tour ;
- les divisions du cercle deviennent i.

C'est le même geste qu'au § 1 : la structure commune est le résultat.

## 4. Lire la figure des trois points comme l'auteur (partie XIX, figure t2, panneau a)

- Le cercle a un rayon de R = 12 pixels ; on le regarde près de sa tangente verticale. Il y a un point central, un point 3 rangées au-dessus (rouge) et un point 3 rangées au-dessous (vert dans la première version, violet maintenant).
- La colonne de la tangente fait 7 carrés : 4 en haut et 4 en bas, le carré central compté dans les deux. Cinq lignes délimitent chaque groupe de 4.
- √12 joue deux rôles.
  - C'est la demi-longueur de la colonne : √(R − 1/4) = 3,43 ≈ √12.
  - C'est l'inverse du bruit d'un point arrondi : σ = 1/√12. Pour R = 12, √R·σ = 1.
- Les positions deviennent des nombres exacts (des cases), avec une erreur relative au centre de la case.
- Le point central est au centre de sa case. Les points en ±3 sont en x = √135 = 11,619, à −0,381 du centre de leur case. Ils arrivent donc près de la face gauche, à 0,119 de cette face, qui est à −1/2.

## 5. Le cube, la grille et les deux contacts

**La lecture de l'auteur.**
- Le cube est la transformation de la grille carrée en 2D en grille cubique en 2D. Elle inclut les coins des carrés des pixels et les centres de leurs côtés gauches (voir aussi la grille décalée de la partie XV, une grille cubique coupée en diagonale).
- Le côté droit (externe) devient la tangente de reflet externe.
- Le côté interne n'est pas un reflet. C'est la zone de contact, où 1 − √2 et la division d'intégrales complexes s'échangent pour calculer le rayon qui couvre la moitié de l'aire du grand disque.

**Faits exacts liés.**
- 1 − √2 est le conjugué de 1 + √2, et leur produit vaut −1 = i². Ce sont les pentes tan(−22,5°) et tan(67,5°), deux directions perpendiculaires : un quart de tour, pas un reflet.
- Les contacts intérieur et extérieur du disque de rayon 1/√2 ont pour courbures relatives √2 − 1 et √2 + 1 (parties XVII et XVIII).
- **La division d'intégrales complexes d'Ullisch** (README, § 3) :
  - on calcule β = ∮ z/f(z) dz ÷ ∮ 1/f(z) dz, avec f(z) = sin z − z cos z − π/2, sur le cercle |z − 3π/4| = π/4 ;
  - on obtient β = 1,905695729…, puis r = 2 cos(β/2) = 1,158728473018121517828… ;
  - c'est le rayon qui broute la moitié du disque de rayon 1.

## 6. Ce que les parties XX à XXVIII ont établi (à garder en tête)

- **Toutes les dimensions, une seule équation.** Dans le plan méridien (ce que l'auteur appelle « les cordes projetées sur la 2e dimension »), la chèvre de dimension n obéit à G_n(β) = 0, avec G₂ = f/2 (Ullisch). La division ∮ z/G ÷ ∮ 1/G donne la corde de chaque dimension. Le cercle d'Ullisch marche tel quel jusqu'à la dimension 9.
- **Pair et impair = la récurrence de la partie IV.** h_n = (n − 1)/n · h_{n−2} : les impaires divisent par 3, 5, 7…, les paires (depuis le disque) par 4, 6, 8… ; h_{n−1}h_n = π/(2n). Le volume des boules décroît dès 6, leur aire dès 8 ; 3 est le premier barreau et la seule dimension où l'ombre de la sphère est plate.
- **Les faisceaux des sphères, avec des chèvres.** n + 1 chèvres sur un simplexe couvrent la clôture S^(n−1) (un bon recouvrement) ; leur nerf calcule la cohomologie. Toute sphère = deux hémisphères d'aire ½ recollés par l'inversion y ↦ y/|y|² ; la projection stéréographique est l'inversion de rayon √2.
- **Le losange de √2 dans la figure de diffraction.** Fantômes |m| = 1 : sommets ; |m| = √2 : milieux des côtés (rapport d'aires ½). En dimension n : le polytope croisé, arêtes √2. Retourner l'aiguille = i·i = −1.
- **√2 partout.** La chèvre infinie, le centre du cube en 8D (E₈ = D₈ ∪ (D₈ + ½·(1, …, 1))), la distance entre deux directions au hasard en grande dimension (les plongements d'IA).
- **2 et 3 donnent 12 :** 3¹² ≈ 2¹⁹ (réduite 19/12 de log₂ 3), le comma pythagoricien.
- **Partie XXI : les trois 24 sont une seule arithmétique.** 24 + 1 = 5², 2·24 + 1 = 7², 24/6 = 2² : les boulets 1² + … + 24² = 70² (Watson) d'où sort Leech ; les exposants 24·P + 1 = (6k − 1)² de η(24τ) = q − q²⁵ − q⁴⁹ + … (les unités modulo 24 ont pour carré 1) ; Δ = η²⁴ et le thêta de Leech ; κ₂₄·h₂₅ = 1/5², h₂₄·h₂₅ = π/50. La symétrie ne passe pas (S₂₄ pour la chèvre, M₂₄ pour Leech).
- **Le miroir 49-50-51.** 10⁻⁴⁹ × 10⁻⁵¹ = (10⁻⁵⁰)² ; 7² ≡ −1 (mod 50) ; 7² = 2·5² − 1 (Pell) ; (7 + i)² = 2·(24 + 7i) ; (3 + i)²(7 + i) = 50·(1 + i), donc 3 et 7 (i et −i modulo 10) font 45°.
- **Le doublement de l'aire est un pas de √2, pas de 10** : une décade vaut 6,644 diaphragmes. Au point de Rayleigh d'un faisceau gaussien, l'aire double, l'intensité et le produit de Newton sont divisés par deux (Self, 1983).
- **√7 vu de e₃.** Dans la boîte 1 × 1 × 2 (Σ_x rectifié, étiré de −e₁ à e₁), les coins sont à √3 et √7 en unités de 1/√2. √7 n'est jamais une distance entre points rationnels (Legendre) : il faut l'unité 1/√2, une arête √2 (la boîte 1 × √2 × 2) ou une quatrième dimension.
- **Le croisement.** En tournant de e₃ vers e₂, le sommet passe le bord des chèvres de toutes les dimensions (α_n → 90°, seule la chèvre infinie a son bord au croisement). Au croisement : √3 ↔ √7, le disque inscrit a la moitié de l'aire, et les tritons se ratent d'un comma autour de √2.
- **Partie XXII : le pas de 10 et le pas de √2 ne s'opposent pas.** Les décades de dimension sont les décimales de l'approche : 2 − ρ_n² ≈ 2/n (ρ² = 1,82 ; 1,980 ; 1,998 0…). Le doublement de l'aire (ρ² = 2) n'arrive qu'à l'infini, et la précision 10⁻ᵏ correspond à la dimension 2·10ᵏ (10⁻⁵⁰ ↔ 2·10⁵⁰). Sur une longueur physique, un cran de 10 reste × 100 en aire.
- **Le carré de neuf points** (sommets, milieux, centre) : vu d'un milieu, 1 et √2 ; les cordes ρ_n remplissent [1, √2] (ρ₁ = 1, ρ₂ = Ullisch, ρ_∞ = √2). En dimension n : 3ⁿ centres de faces du cube, 3ⁿ ≡ 3, 9, 7, 1 (mod 10).
- **Les faisceaux du polytope croisé.** 2n chèvres aux ±e_i : nerf = bord du polytope croisé = S^(n−1) en toute dimension finie (arccos(1/√n) < α_n < 90°) ; n chèvres à la fois vers les sommets du cube ; à l'infini, le recouvrement n'est plus bon et le nerf se trompe.
- **Leech garde le √2 du carré** : sphères de rayon 1, trou le plus profond à √2 (Conway, Parker, Sloane 1982). Même rapport pour D₃ (cfc), D₄ et E₈ : en 3, 8 et 24 (les dimensions nommées par l'auteur), les records ont leur trou à √2 fois le rayon.
- **Partie XXIII : le plan de la lentille.** Il est à x₀ = 1/(n + 1) − μ/2 du centre, donc une décade de dimension est une décade de longueur. Quatre taux de change grain → dimension : ε⁻² (équateur), ε⁻¹ (coquille et plan), ε^(−1/2) (ménisque).
- **Partie XXIV : le terme 2/(3n²) est démontré.**
  - La borne : |r_n² − 2n/(n + 1) − 2/(3n²)| < 1 800/n³ pour n ≥ 100. Les coefficients suivants sont rationnels : −98/15, 5966/105…
  - 2/3 = 2 × 1/6 × 2 : le double produit, la courbure de l'équateur, l'asymétrie de la coquille.
  - **Le ménisque vaut un tiers de dimension** : la chèvre de dimension n a la corde du simplexe de dimension n + 1/3, et 1/x₀ = n + 4/3 − 112/(45n) + …
  - La série diverge au rythme 1/ln √2. Sa meilleure précision est 2^(−n/2)/n.
  - La loi du piquet à distance d (partie I) et le c_n/ρ² de la partie XVI sont le même terme.
- **Le facteur 2 entre le plan et l'aire est le diamètre.**
  - Euclide VI.8 et Thalès donnent r² = 2R·(R − x₀) : le défaut d'aire est la bande x₀ × 2R.
  - C'est un cran (le cercle des côtés contre celui des coins), et les deux lectures sont vraies en même temps : 10⁵⁰ − 4/3 et 2·10⁵⁰ − 4/3 au grain 10⁻⁵⁰.
  - Le 2 repose sur des triangles semblables, donc sur le postulat des parallèles (Wallis, 1663) : c'est un test de platitude.
  - Ne réécris pas « ton modèle doit choisir ».
- **Partie XXV : les ouverts de la partie XXIV.**
  - L'équation de la chèvre est une intégrale de Laplace : ∫₀^β (cos ψ/cos β)ⁿ dψ = ∫₀^∞ e^(−nu) tan φ(u) du. D'où les grands ordres r²_m ≈ (−1)^m e^(−1/2) √(ln 2/π) Γ(m − ½)(2/ln 2)^m et la meilleure précision 1,03·2^(−n/2)/n.
  - Resommée (Borel–Padé), la série de la dimension infinie redonne la chèvre plane (Ullisch) à 10⁻⁹·⁵ : les deux chèvres de la partie XX sont reliées par un calcul exact.
  - Ordres 2 à 8 démontrés (n ≥ 100) ; c₂ = 4/405 et c₃ = 1/96 démontrés par la lentille exacte.
  - Le grain comme angle : cos α_n = x₀ ; le plan est le miroir des lectures (paires κ·κ′ = 1).
- **La tranche 49 – 55 et les aiguilles.** Sept niveaux, miroir autour de 52 ; l'aiguille (7, 1, …, 1) gagne une dimension par niveau ; carrés minimaux 1, 2, 3, 2, 2, 3, 4 (55 ≡ 7 mod 8, Legendre) ; i n'existe que modulo 50 et 53 ; rotations 3-4-5, 7-24-25, 5-12-13, 28-45-53 ; r₂₄ par le τ de Ramanujan ; (7, 1, 1) n'a aucun arrêt perpendiculaire sur le réseau 3D.
- **Partie XXVI : Kakeya au grain δ, la virgule et son miroir, le cube qui tourne.**
  - Aire minimale de N tubes 1 × δ (une direction chacun) : au moins π/(1 + 2γ + 2 ln(2/δ)) (Córdoba, constante calculée), donc 1/aire ≤ 1,127 + 1,466·k pour δ = 10⁻ᵏ ; arbres de Perron en tubes (calculés jusqu'à 10⁻⁵) : ≈ 2,9/ln(1/δ). À 10⁻⁵⁰ : entre 0,0134 et ≈ 0,025. Kakeya lit l'exposant k, la chèvre lit 10⁻ᵏ ; miroir harmonique 1/L(49) + 1/L(51) = 2/L(50).
  - 2¹⁰/10³ = 128/125 = le diesis (2 et 5, comme le comma pythagoricien pour 2 et 3) ; le miroir 10⁶/2²⁰ = 5⁶/2¹⁴ a les chiffres de 5²⁰ (« 1 To » = 931 Go : 5³⁰). 9,49 / 9,72 / 9,95 % = écart cran–miroir, double 2c, carré : égaux en log (2 × 0,0206 décade), séparés en chiffres par les retenues c²/(1 + c) et c².
  - Les 21 crans 2⁰ … 2²⁰ sur le cercle des décades : trois écarts, 128/125 (×11), 625/512 (×8), 5/4 (×2) ; les 5ʲ sont le reflet exact.
  - Le cube : ombre |u₁| + |u₂| + |u₃| (1, √2, √3) ; le mouvement complet autour d'un axe d'ordre 2 donne √2|cos t| + |sin t|, des hexagones séparés par 109,47° et 70,53° (le losange de la partie II) ; les deux carrés (faces avant et arrière) se recouvrent de (|u₃| − |u₁|)(|u₃| − |u₂|)/|u₃| et se quittent exactement à l'hexagone ; Prince Rupert : Wallis √6 − √2 dans l'hexagone, Nieuwland 3√2/4 le long de (2, 2, 1)/3, sur le même tour (t = arcsin 1/3).
- **Partie XXVII : la carte des connexions.** Le graphe des renvois entre les parties I à XXVI (`scripts/carte_connexions.py`) : 178 paires sur 325 ; carrefours XXIII, XIV, VI ; liens prédits par les voisins communs (Adamic–Adar). **Pour chercher de nouvelles connexions : `python3 scripts/carte_connexions.py N` affiche la carte des parties I à N, les paires prédites et leurs voisins communs, sans réécrire les fichiers de la partie XXVII.** Établis :
  - cercles arctiques : dominos au hasard dans le losange (2^(n(n+1)/2) pavages, 1 024 à l'ordre 4) et cubes empilés dans l'hexagone (MacMahon ; côté 1 = Necker) ne se mélangent que dans le cercle inscrit — pour l'hexagone, l'ombre de la sphère médiane (II) ; pour le losange, le disque de demi-aire (XVII) ;
  - échelle du grain : ε⁻², ε⁻¹, ε^(−1/2) (XXIII), puis la marche 0, le logarithme : la série (XXV, 316 dimensions à 10⁻⁵⁰, un cran de √2 par dimension = 6,644 par décade comme en XXI) et Kakeya (XXVI, 1/aire = 74) ;
  - ‖u‖₁·‖u‖∞ ≥ 1 : ombre du cube × cos(angle au piquet) ≥ 1, égalité sur les 26 directions de {−1, 0, 1}³ ; le seuil des 2n chèvres (XXII) est la plus grande ombre √n ; 1/x₀ = n + 4/3 − … (XXIV) ;
  - 3/2 < π/2 < √3 ⟺ 3 < π < 2√3 (Archimède dans l'ombre du cube) ;
  - la chèvre plane et la chèvre infinie (XX) = sommet (n ≈ 2,08 relatif, 2,24 absolu, VI) et bout de la bosse du ménisque ; en dimensions, N − n → ⅓ ;
  - aiguilles de Pell (1, 2), (2, 5), (5, 12)… vers 67,5° à une demi-case par pas = la récursion d'argent (XVII) ; contact 1 + 1/√2, fois √2 = 1 + √2 ;
  - arccos(1/3) de la zone de confusion (VI) = écart entre hexagones (XXVI) : le tétraèdre inscrit ; cos = −1/(n + 1) pour le simplexe de dimension n + 1.
  - Pistes encore ouvertes : XIV–XX, VI–VIII, XIV–XXIV, VI–XXI, V–IX.
- **Partie XXVIII : l'octaèdre, Perron démontré, le Venn à 17** (`scripts/octaedre_perron_venn.py`).
  - L'octaèdre |x| + |y| + |z| ≤ 1 est le polaire du cube [−½, ½]³ par leur sphère médiane commune (rayon √2/2, 12 milieux d'arêtes communs) : ‖u‖₁ est sa jauge. Même hexagone d'ombre et de coupe le long de (1, 1, 1). Son ombre vaut max(‖u‖₁, 2‖u‖∞) : égale à celle du cube sur 8 triangles sphériques d'angles arccos(1/3) (35,10 % des directions) ; moyenne √3.
  - Les deux cercles arctiques (XXVII) sont l'ombre de la même sphère médiane : axe d'ordre 4 pour les dominos (le losange est l'ombre de l'octaèdre), axe d'ordre 3 pour l'hexagone. Argument direct pour l'hexagone : Kenyon–Okounkov (cité) + cinq tangentes fixent une conique. La récurrence de l'octaèdre compte les deux pavages (Dodgson, Kuo) ; linéarisée, |v| ≤ 1/√2 : le losange est le cône exact, le cercle arctique le cône des vitesses de groupe.
  - Perron démontré pour tout k : borne « cœur + oreilles » F = P_k² + 2Σ(P_j − P_(j+1))² pour tous les rapports ; minimum 2/(k + 2) aux seuls rapports télescopiques (oreilles égales) ; aire exacte par la coupe en plateau 1/(k + 2), prouvée par l'ombre du cube. Kakeya : N éventails donnent le polygone circonscrit à 2N côtés ; à 10⁻⁵⁰, l'aire minimale est démontrée entre 0,01344 et 0,02096 (13 éventails ; 17 : 0,02097) ; constantes asymptotiques π/2 et π·ln 2.
  - Le Venn à 17 : Henderson (n premier, démontré), 131 070 = 17 × 7 710 formes (Fermat), 15 420 croisements par courbe (Venn simple) ; image probablement de Dzoba (2026). Diaphragme à 17 lames : 97,74 % de la lumière, 34 aigrettes ; la même parité fait couvrir chaque direction une fois par 17 éventails de Perron posés comme les lames. Fefferman et Córdoba relient diaphragmes et Perron. Chaque coupe de Perron est un Venn à une dimension. 17 = 4² + 1 (4 ≡ i), Gauss, Midy pour 1/17.

## 6 bis. Les acquis des parties I à XIX : relis-les avant d'écrire

La partie XXIII a corrigé trois phrases de la partie XXII qui contredisaient des acquis. **Avant d'écrire « coïncidence », « mesuré, pas démontré », « pas établi » ou « pas dans les longueurs », cherche dans les parties précédentes** (`grep` sur les `.md` de ce dossier) : le lien y est peut-être déjà.

- **Partie I (README).**
  - L'aire de la lentille F(δ, k) sert pour la chèvre, l'éclipse, le vignettage et la FTM.
  - Le piquet au centre donne k = 1/√2 : un cran.
  - « Un cran sépare le cercle tangent aux côtés et le cercle qui passe par les coins » (§ 6.4).
  - r_n² = 2n/(n + 1) + 2/(3n²), esquissé au § 5.4, démontré dans la partie XXIV (avec tous les termes suivants).
  - Le plan de la lentille est à x₀ ≈ R/(n + 1).
  - La corde est la distance médiane ; la coquille et l'équateur (§ 5.2–5.3).
  - Les cercles k² = δ² + c, avec c = (n − 1)/(n + 1) (démontré dans la partie XXIV, avec la correction + 2/(3n²δ²)).
- **Partie IV.** La suite des trois solides, π = 2 + ⅓(2 + ⅖(…)), part du carré inscrit (aire 2). Seuils 6 et 8.
- **Parties V et VI.**
  - Le triangle de hauteur R, puis le simplexe d'arête √(2n/(n + 1)), terme principal de la corde.
  - L'écart (0,35 % en 2D) est le ménisque, **pas une coïncidence**.
  - Le plan de la lentille passe par le centre de gravité du simplexe.
- **Partie X.**
  - Le point, le disque et le carré se confondent sous le flou (un carré de côté √3·ρ ressemble à un disque de rayon ρ).
  - Des pixels carrés font 8 centres fantômes (4 cardinaux, 4 diagonaux) : avec le centre, le carré de neuf points.
- **Partie XV.**
  - La grille décalée est A_n (la grille carrée d'une dimension de plus, coupée en diagonale) ; sa maille est l'arête du simplexe.
  - La grille carrée n'offre que 1 et √2.
  - Une grille grossière confond la chèvre et son simplexe.
- **Partie XVI.**
  - r² = 1 + (n − 1)/(n + 1) + μ (piquet, projection, ménisque) ; le c_n/ρ² du piquet lointain (§ 6), retrouvé dans la partie XXIV.
  - Le plateau 2^(−1/n) ; les contacts à 45° (Laguerre).
- **Partie XVII.** Le disque de demi-aire 1/√2 ; les jumeaux d·d′ = ½ (la forme de Newton x·x′ = f²) ; la récursion d'argent (Pell).
- **Partie XVIII.** Le grain grossier honnête : un chiffre certain par niveau décimal. L'aire converge sous le grain, la longueur jamais (« π = 4 »).
- **Partie XIX.** Les bases comme objets, i modulo b, les deux couches et les retenues.

## 7. Travailler sur un modèle de l'auteur « comme exact »

- Quand l'auteur demande de traiter son modèle comme une exactitude physique (par exemple à 10⁻⁵⁰ m), **pose-le comme postulat** : suppose-le exact, calcule ce qu'il implique, et dis ce qui permettrait de le tester.
- **Ne le présente pas comme de la physique établie.** Sous la longueur de Planck (1,6·10⁻³⁵ m), la physique connue ne sait plus définir une position (partie XX, § 8).
- **Ne le rejette pas non plus.** Un postulat cohérent dont on tire des conséquences est un travail légitime.

## 8. Ton et façon de répondre

- **Langue et ton.** Réponds en français, sur un ton simple et conversationnel, et tutoie l'auteur.
- **Explications.** Explique pourquoi et comment, pas seulement quoi. Dis ce qui est sûr et ce qui ne l'est pas, et donne des sources en liens.
- **Partir de ses propositions.** Cherche d'abord le procédé commun qui les soutient (§ 1), calcule-le, puis dis ce qui reste ouvert. N'affaiblis pas une proposition par réflexe.
- **Vérifier.** Vérifie chaque nombre par un calcul, dans un script, avant de l'écrire.
- **Relire.** Avant de conclure, relis les acquis du § 6 bis et cite la partie où un lien a déjà été posé.

## 9. Conventions de la série

**Chaque message de l'auteur devient en général une nouvelle « Partie », avec :**
- `scripts/<nom>.py`, qui utilise le style commun de `scripts/figures.py` (`import figures as F`, puis `F.sauver`) ;
- `figures/<lettre><n>_<nom>.png`, avec une lettre par partie (p = XVI, q = XVII, r = XVIII, t = XIX, u = XX, v = XXI, w = XXII, x = XXIII, y = XXIV, z = XXV, aa = XXVI, ab = XXVII, ac = XXVIII ; ensuite ad, ae…) : prends la suivante libre ;
- `resultats/<nom>.md`, écrit par le script ;
- `<nom>.md` dans ce dossier, avec dans l'ordre : la citation du message, la ligne « Tout est recalculé par… », « En bref », des sections numérotées, « Le tri » et « Sources ».

**Les liens à ajouter :**
- `**Suite : [Partie … — titre](<nom>.md).**` juste après la ligne « Tout est recalculé… » de la partie précédente ;
- dans `README.md`, une ligne `**Et : [Partie … — titre](<nom>.md)** (résumé).` après celle de la partie précédente, et le script dans la liste « Reproduire ».

**Lancer et contrôler :**
- Lance les scripts depuis ce dossier : `python3 scripts/<nom>.py`. Les dépendances sont dans `requirements.txt`.
- Contrôle rapide : `ruff check --select F,E9 scripts/<nom>.py`.
- Regarde chaque figure (textes ou légendes qui se chevauchent) avant de l'envoyer.

## Repères

- H. Poincaré, *Science et méthode* (1908), chapitre « L'avenir des mathématiques » : « la mathématique est l'art de donner le même nom à des choses différentes ».
- S. Banach (attribué) : « A mathematician is a person who can find analogies between theorems; a better mathematician is one who can see analogies between proofs and the best mathematician can notice analogies between theories. One can imagine that the ultimate mathematician is one who can see analogies between analogies. »
- G. A. Deschamps, « Gaussian beam as a bundle of complex rays », *Electronics Letters* 7, 684–685 (1971).
- [« What is special about the divisors of 24? »](https://arxiv.org/abs/1104.5052) : les bases où x² ≡ 1 pour tout x premier avec la base.
- D. Jeffery (UNLV), [« Ancient Babylonian astronomers and why we have 360° in the circle »](https://www.physics.unlv.edu/~jeffery/astro/babylon/babylonian_360_degrees.html).
- J. Miller, [« Earliest Uses of Various Mathematical Symbols »](https://mathshistory.st-andrews.ac.uk/Miller/mathsym) (MacTutor) : les dates des notations.
- L. J. Garay, « Quantum gravity and minimum length », *Int. J. Mod. Phys. A* 10, 145–166 (1995), [arXiv:gr-qc/9403008](https://arxiv.org/abs/gr-qc/9403008) : la longueur minimale.
