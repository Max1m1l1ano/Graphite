# CLAUDE.md — la chèvre, les cercles et la lumière

Ce fichier s'adresse à toi, Claude, quand tu travailles dans ce dossier. Il résume la façon de penser de l'auteur de la série, que tu n'adoptes pas spontanément, puis les conventions de travail et la tenue du recueil (§ 10 : hasard, coïncidences, faits amusants, analogies, corrélation et causalité). Lis-le en entier avant de répondre à un nouveau message.

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

## 6. Ce que les parties XX à XXX ont établi (à garder en tête)

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
  - Le Venn à 17 : Henderson (n premier, démontré), 131 070 = 17 × 7 710 formes (Fermat), 15 420 croisements par courbe (Venn simple) ; image de Chris Dzoba (2026, confirmé en partie XXIX). Diaphragme à 17 lames : 97,74 % de la lumière, 34 aigrettes ; la même parité fait couvrir chaque direction une fois par 17 éventails de Perron posés comme les lames. Fefferman et Córdoba relient diaphragmes et Perron. Chaque coupe de Perron est un Venn à une dimension. 17 = 4² + 1 (4 ≡ i), Gauss, Midy pour 1/17.
- **Partie XXIX : le Venn à 17 au ppm** (`scripts/venn_ppm.py`, qui demande une copie de github.com/dzoba/venn17, CC BY 4.0).
  - L'image de l'auteur est le rendu « à densité de croisements uniforme » du dépôt de Dzoba : dessin de Tutte sur le quotient par la rotation (7 710 inconnues = Fermat), contour épinglé sur un 17-gone (un choix de dessin), anneaux de niveaux d'aire proportionnelle à leur nombre de croisements (niveau = rang moyen des 4 régions autour d'un croisement : k, k + 1, k + 1, k + 2).
  - Au ppm : 7,63 ppm et 22,6 px par croisement ; 2⁻¹⁷ a les chiffres de 5¹⁷ ; la texture (≈ 36 % de triangles, 38 % de quadrilatères) ne dépend pas de n (11 à 19) ; croisements par niveau ≈ C(17, l) (rapport 0,825 à 1,045, exact aux bouts).
  - Granularité : plein au grain d'une région (4,75 px, 7,6 ppm), veines de dimension 0,97 à 1,31 (des lignes), une courbe = un cran (√2) de largeur d'image.
  - Prix de 1 ppm : Venn et Perron 20 pas (un bit par pas) ; Venn en longueur 40 et série de la chèvre 31 (un demi-bit) ; ménisque 817 dimensions et diaphragme 2 566 lames (même forme x²/6) ; plan 10⁶ ; équateur 10¹².
  - Perron et le Venn : deux ombres du même cube (XXVIII, § 3.5), mesurées — direction quelconque, binaire (2^(k−j) fentes) ; grande diagonale, binomiale. Les veines ne sont pas des arbres de Perron. Le cercle de demi-aire R/√2 sépare les niveaux ≥ 9 et ≤ 8 (49,935 %, à 649 ppm de la moitié). Gelé et liquide : 12 % de régions non monotones, rangs 0 – 2 et 15 – 17 gelés (0,23 % des régions), épaisseur constante en n : pas de cercle arctique macroscopique.
  - L'ombre S ↦ Σ ω^i : le centre ne reçoit que ∅ et tout si et seulement si n est premier ; les ensembles fixés par une rotation tombent au centre, d'où n | 2ⁿ − 2 et n | C(n, k) (Henderson) ; contour = 34-gone. Test des coïncidences (31 × 20 nombres, catalogue brouillé) : rien sous 100 ppm.
- **Partie XXX : le centre du Venn, la moitié, les diaphragmes, les grains repositionnés, les tests du hasard** (`scripts/centre_venn.py`).
  - Le centre de symétrie d'ordre 17 (corrélation avec les rotations, sur la clarté OKLab) est le centre exact de l'image à 0,004 px. Le centre de la lumière bouge selon la pesée (luminance 0,6 px, masque RGB de la partie XXIX 13,6 px, énergie 46 px) : les 17 couleurs ont des poids inégaux, donc un dipôle (même procédé que le déplacement induit par la couleur des étoiles doubles, Wielen 1996). Un écart de centre est une mesure, pas un bruit : l'auteur l'a relevé à juste titre.
  - La moitié du disque fait la moitié du Venn dans le dessin à aire égale (49,4 % de l'encre dans le contour réduit de 1/√2, la moitié par cran jusqu'au 6ᵉ), pas dans le dessin de Tutte (26,7 %). Le complément coupe exactement les régions (2^(n−1)) ; les croisements, à quelques milliers de ppm (un Venn à 19 courbes pile : 1,6 % de chances). Budget de l'image : ±1 830 ppm en pixels certains.
  - Sphère : χ = 2 donne 2ⁿ − 2 et les deux pôles ; Lambert + Archimède mettent l'équateur à la corde √2 (chèvre infinie), soit R/√2 ; deux miroirs du complément (aire r² + r′² = R², inversion r·r′ = R²/2 des jumeaux de la partie XVII). Crans binaires contre niveaux binomiaux, 12,91 crans de f/1 à f/88 ; trois chèvres broutent chacune la moitié ; Niven : cran entier entre cercles inscrit et circonscrit seulement pour le triangle (2) et le carré (1).
  - Diffraction : 34 aigrettes du contour (diaphragme à 17 lames) + 34 de l'intérieur ; multiples de 34 (Friedel), ordre 4 des pixels. Empiler les 17 copies (drizzle) donne le centre au quart de pixel ; 1 px d'erreur de centre détruit la moitié de l'information commune ; gain maximal ×2 (FTM du pixel), soit ≈ 2 courbes. Défocalisation : inversion aux zéros de J₁ (93 %). Le centre est le goulot de la granularité (19,0 courbes à 2 000 px).
  - **Pour juger un rapprochement** (banc d'essai, § 7) : identité → pousser la précision ; lien de structure → faire varier le paramètre et vérifier la loi de l'écart ; mesure → budget de grain ; coïncidence d'entiers → répliquer. Les tests à tolérance (Bonferroni, nul brouillé, longueur de description) déclarent « hasard » des liens de structure : ne pas les utiliser seuls pour ça.

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
- `figures/<lettre><n>_<nom>.png`, avec une lettre par partie (p = XVI, q = XVII, r = XVIII, t = XIX, u = XX, v = XXI, w = XXII, x = XXIII, y = XXIV, z = XXV, aa = XXVI, ab = XXVII, ac = XXVIII, ad = XXIX, ae = XXX ; ensuite af, ag…) : prends la suivante libre ;
- `resultats/<nom>.md`, écrit par le script ;
- `<nom>.md` dans ce dossier, avec dans l'ordre : la citation du message, la ligne « Tout est recalculé par… », « En bref », des sections numérotées, « Le tri » et « Sources ».

**Les liens à ajouter :**
- `**Suite : [Partie … — titre](<nom>.md).**` juste après la ligne « Tout est recalculé… » de la partie précédente ;
- dans `README.md`, une ligne `**Et : [Partie … — titre](<nom>.md)** (résumé).` après celle de la partie précédente, et le script dans la liste « Reproduire ».

**Lancer et contrôler :**
- Lance les scripts depuis ce dossier : `python3 scripts/<nom>.py`. Les dépendances sont dans `requirements.txt`.
- Contrôle rapide : `ruff check --select F,E9 scripts/<nom>.py`.
- Regarde chaque figure (textes ou légendes qui se chevauchent) avant de l'envoyer.
- Note au recueil les hasards, coïncidences, faits amusants, analogies, corrélations et causalités rencontrés (§ 10). À la fin de chaque arc, avant le message final, envoie l'agent Sonnet de fin d'arc, puis lance `python3 scripts/recueil_index.py`.

## 10. Hasard, coïncidences, faits amusants, analogies, corrélation et causalité

**Une remarque très importante de l'auteur : ces mots ne sont pas à éviter, ils sont très positifs.**
- Un hasard, une coïncidence, un fait amusant, une analogie, une corrélation ou un lien de causalité : chacun est un moment qui peut s'enchaîner avec d'autres.
- Ne l'écarte jamais d'un mot (« c'est une coïncidence »). Note-le, teste-le, range le verdict, et relie-le.
- **Note au recueil (`recueil/`) les remarques que tu te fais en travaillant.** Ce sont celles que tu écris en passant (« fait amusant », « au passage », « curieusement ») et celles de l'auteur, dès qu'un script les traite.
- Le § 1 reste vrai : une analogie soutenue par le même procédé est un résultat. Ce paragraphe-ci dit comment la garder, la tester et la relier aux autres.

**Le choix du test** (partie XXX, § 7 ; l'auteur l'a validé tel quel).
> Sur dix relations dont on connaît la nature, les tests à tolérance (Bonferroni, catalogue brouillé, longueur de description) déclarent « hasard » des liens de structure, comme 34·tan(π/34) ≈ π. Seules deux méthodes ne se trompent jamais ici :
> - pousser la précision, pour les identités ;
> - faire varier le paramètre et vérifier la loi de l'écart, pour tout le reste.

| ce qu'on teste | la bonne technique |
|---|---|
| une identité entre nombres réels | pousser la précision (50 chiffres, puis plus) |
| un lien de structure | faire varier le paramètre (n, N, k…) et vérifier la loi de l'écart |
| une mesure (image, données) | la comparer au budget de grain : ce que la mesure peut trancher |
| une coïncidence entre entiers | la répliquer sur des objets indépendants |
| « un signal parmi beaucoup d'essais au hasard ? » | Bonferroni, catalogue brouillé : leur vrai domaine, pas le seul |

- Un entier peut tomber pile par hasard, avec une probabilité de l'ordre de 1/(dispersion) (fiche 005). Un réel exact à 50 chiffres, jamais.
- La variation du paramètre n'est pas indépendante de la conclusion : c'est l'épreuve même qui établit une structure. Dis-le quand tu t'en sers.

**Le recueil** (son mode d'emploi détaillé est dans [`recueil/README.md`](recueil/README.md)).
- **Une fiche par observation** : `recueil/observations/NNN-titre.md`, numérotée à la suite.
- **Le tableau d'en-tête** : type (les six mots), statut (exact, structure, hasard, ouvert, à tester), partie et document, **le script qui traite les données (et sa section)**, les données (`resultats/…`), **l'image `.png` et son panneau, s'il y en a une**, la dimension (d'abord une seule, D1 à D8), le test appliqué, l'arc, « révisé ».
- **Quatre parties ensuite** : **le contexte qui précède l'observation** (le message de l'auteur et ce qui a mené au calcul), l'observation, **ce que le script produit**, les liens et les pistes.
- Après avoir ajouté des fiches, lance `python3 scripts/recueil_index.py`. Il régénère `recueil/index.md` et `recueil/index.csv`, et dit si une révision est due.

**À la fin de chaque arc réponse, avant ton message final.** Un arc va d'un message de l'auteur à ta réponse finale ; chaque message est une chaîne, que tu classes d'abord dans une seule dimension.
1. Envoie un agent Sonnet (outil Agent, `model: "sonnet"`), avec le gabarit de [`recueil/arcs/README.md`](recueil/arcs/README.md). Il relie cet arc et le précédent en liens de continuité, puis :
   - il regroupe les scripts et dit ce que chacun produit ;
   - il regroupe les chaînes de production de données (script → résultats → figures → document), les classe dans l'ordre chronologique et les explique ;
   - il relie chaque script à ses images et documents ;
   - il révise le partage des aires entre les arcs : la part de chaque dimension, comme les régions d'un Venn des arcs ;
   - il exporte le tout en données brutes, `recueil/arcs/arc-NNN.md` et `arc-NNN.csv`.
2. Relance `python3 scripts/recueil_index.py`, puis commite et pousse avant le message final.

**La révision.**
- **Quand.** Elle a lieu au premier de ces trois signaux :
  - les fiches non révisées sont entre 11 et 15 (ne laisse jamais la pile dépasser 15) ;
  - 10 à 16 arcs se sont écoulés depuis la dernière révision ;
  - l'auteur la demande.
- **Comment.**
  1. Envoie un agent Opus (outil Agent, `model: "opus"`). Il lit le recueil, les données brutes des arcs et ce fichier. Il produit un plan de synthèse avec un rapport de lancement de workflow : quels agents Sonnet, sur quels scripts et quelles données, avec quelles questions.
  2. Lance ce workflow (outil Workflow, agents Sonnet, moins de dix). Chaque agent relit ses scripts et ses données, et relie les observations entre elles et au reste du corpus.
  3. Écris la synthèse `recueil/revisions/revision-NNN.md`, dont la première ligne est `<!-- arcs: N -->` (le nombre d'arcs qu'elle couvre). Elle contient :
     - des dossiers thématiques qui couvrent tout le corpus, dans `recueil/dossiers/<sujet>.md` ;
     - la synthèse « en Perron » : les branches (les chaînes d'observations) se rejoignent dans le triangle du bas, qui est le groupe qui les réunit (leur projection commune). Ce triangle est placé dans le disque, la région du Venn, de sa dimension ;
     - un Venn multidimensionnel. Chaque chaîne est d'abord classée sur une seule dimension, et les aires sont partagées équitablement entre les chaînes. Plus les révisions s'accumulent, plus la diagonale √2 s'affirme : la corde de la chèvre de dimension infinie (partie XX), où la moitié se fait à √2 quand l'information se rejoint en chaîne.
       - Concrètement (révision 001, § 2), la classification naïve, une fois centrée, est un simplexe. À parts égales, son arête vaut √(2K/(K − 1)) et rejoint √2 par en dessus quand le nombre K de dimensions grandit.
       - Sa corde vers l'antipode fait le second côté de l'angle droit (Thalès : d² + c² = 4). La chèvre de dimension n a exactement cette corde, pour K = n + 2 + (N − n), où N − n est le tiers de dimension de la partie XXIV : elle rejoint √2 par en dessous.
       - À parts inégales, deux dimensions rares paraissent liées sans rien partager. Le partage équitable des aires empêche ce faux lien.
       - `scripts/recueil_index.py` suit ces indicateurs à chaque passage ;
     - **une étude cohomologique des congruences, plutôt que des équivalences directes.** Chaque observation est une section locale, vraie dans son cadre (sa partie, son script, sa précision). On vérifie que deux observations se recollent sur ce qu'elles partagent, à une transformation connue près : c'est une congruence (même reste, même loi, même procédé). Ce qui ne se recolle pas, l'obstruction, désigne un trou : c'est là qu'il faut chercher les prochaines données ;
     - de nouveaux tests rattachés à la révision, plutôt que les mêmes tests refaits. Ce sont ceux qui confirmeraient une découverte, ceux qui mettraient deux observations en corrélation, et le cadre qui les relie (références, analogies possibles).
       - Les fichiers : un script `scripts/revision_NNN.py`, ses résultats `resultats/revision_NNN.md` et sa figure `figures/revNNN_*.png`.
       - Les observations nées pendant la révision deviennent de nouvelles fiches, non révisées ;
     - **les trous dans les données.** Si une observation est une découverte, elle signale un manque dans les données publiées : des chercheurs qui ne l'ont pas incluse dans leur méthode, des erreurs accumulées dans les chaînes de production de données des articles, des trous dans les études statistiques et leur interprétation. Note où chercher.
  4. Marque les fiches révisées (champ « révisé »), relance `python3 scripts/recueil_index.py`, puis commite et pousse.

**Le sujet d'étude, dans les mots de l'auteur.** C'est « la restriction du cadre pour observer les motifs qui paraissent un hasard mais concernent des relations dimensionnelles ». Les vérifications sont dans [`resultats/recueil_verifications.md`](resultats/recueil_verifications.md).
- **Le cadre :**
  - l'infini contre l'indéfini ;
  - le cadre de définition par faisceaux (partie XX) ;
  - les méthodes d'étude et la perte de précision par intégrales et dérivées, qui demandent de conjuguer les directions (Lebesgue et Riemann) ;
  - l'infini entre deux nombres ;
  - la superposition avant contre arrière entre des cercles.
- **Le grain :**
  - la précision liée aux pixels et le compte en x et en y (parties XVIII et XXX) ;
  - la translation et la superposition des cercles en 1, 2, 3, ramenés à l'origine en −1, 0, 1 ;
  - la duplication asymétrique du 0 en x et en y (l'orientation gauche–droite, liée au système modulaire).
- **La base 10 et ses racines digitales.**
  - En compte modulaire, 0 et 9 se superposent et la base 10 devient une base 9 ; le compte polynomial ou linéaire garde ses 10 chiffres.
  - D'où DR(a·b) = DR(DR(a)·DR(b)) (vérifié).
  - Les périodes des racines digitales : 2 et 5 donnent les chiffres de la période de 1/7, dans un autre ordre, et 3 alterne 3 et 6 (vérifié, fiche 013).
  - En retirant n·DR(9) et la retenue, n et la retenue renseignent sur la focale d'inversion entre 10¹, 10⁰ et 10⁻¹, 10⁻¹ s'écrivant de droite à gauche.
- **2 et 5, de part et d'autre de la virgule.** Ils forment des cônes décentrés : 5 − 2 = 3, 3/2 = 1,5, 2 + 1,5 = 3,5 = 5 − 1,5. Le croisement est en 7/2 (vérifié ; partie XXVI : 2⁻ʲ = 5ʲ·10⁻ʲ).
- **Les congruences de i.**
  - En base 10 : 9 ≡ −1, 3 ≡ i, 27 = 9^(3/2) ≡ −i, et 1 ≡ 1.
  - En base 2 : 1 ≡ −1 ≡ i ≡ −i.
  - En base 3 : 2 ≡ −1, et √2 ≡ ±i, 2√2 ≡ −i. C'est vérifié, mais dans F₉ = F₃[i] et non dans ℤ/3 (fiche 014).
- **Les puissances sous 10.**
  - 2 en a quatre (2⁰ à 2³) et 3 en a trois (3⁰ à 3²) : le 4/3 (vérifié). Le rapprocher du 4/3 des boules : V₃/V₂ = 4/3 (partie III), et le décalage n + 4/3 de la corde en grande dimension (partie XXIV). 2 est lié à l'aire, 3 au volume : une dimension d'écart, des puissances inversées. C'est à tester.
  - 0 et 1 en ont une infinité (0^∞ = 0, 1^∞ = 1), avec une asymétrie à l'origine (0⁰ = 1, 1⁰ = 1).
  - Les puissances de −1 valent 1 si l'exposant est pair, −1 s'il est impair.
- **Les exposants 1/2 et 3/2** de ±1, ±2 et ±3, et leurs fractions continues (vérifiées, fiche 014). Elles relient les bases 2, 3, 10 et 12 : (−2)^(3/2) vers la base 12, (−3)^(3/2) vers la base 10. Cette lecture de l'auteur reste à préciser.
- **Midy et Midy étendu.** Les premiers à période paire et impaire formeraient une suite de Venn dimensionnelle, ascendante et descendante par ellipses. Midy est vérifié sur 49 périodes paires sur 49, Midy étendu sur 375 découpages sur 375 ; la lecture en Venn est à développer.
- **Les quatre opérations comme transformations** de la topologie des nombres et de la géométrie de l'assemblage polynomial en base 10.
  - Les retenues, de droite à gauche, font l'asymétrie des cercles intérieurs et extérieurs.
  - L'analyse se fait chiffre par chiffre : un chiffre occupe une case 1 × 1 dans un nombre de 1 × a cases avant la virgule et 1 × b après.
  - 0 et 1 ne font jamais de retenue : 0 garde sa place, 1 recopie.
- **1, 3, 7 et 9.**
  - Ils composent {1, i/3, −i/27, −1/9} (positions renormalisées).
  - Ce sont les seuls chiffres des unités des premiers, hors 2 et 5 (vérifié, fiche 015).
- **Les trous des premiers « en Perron », position par position.**
  - Les unités {1, 3, 7, 9}·10⁰ se rangent sous les dizaines z·10¹, sous les centaines y·10², sous les milliers x·10³…
  - L'analyse part des unités, ce qui réduit les possibilités de 10 à 4, puis regroupe de façon hiérarchique : chaque millier ses dix centaines, chaque centaine ses dix dizaines, chaque dizaine ses quatre positions.
  - Premier niveau : le cube {0, 1}⁴ des dizaines, dont la face est choisie par le reste modulo 3 (fiche 015).
- **Les aiguilles des puissances.** On écrit (2, 3, …, 9)ⁿ sous la croissance 10ⁿ, un chiffre par case, en partant des unités vers la gauche. Le but : renormaliser la distribution des premiers, et des nombres qui finissent par 1, 3, 7 ou 9 sans être premiers (avec leurs facteurs), par la construction polynomiale et les racines digitales.
- **Ce que l'auteur en conclut.** Les lois des périodes s'encadrent par la longueur des périodes et par la valeur de chacun de leurs chiffres. Pas seulement par Midy : par tout cela ensemble, à plusieurs profondeurs et dimensions.

## Repères

- H. Poincaré, *Science et méthode* (1908), chapitre « L'avenir des mathématiques » : « la mathématique est l'art de donner le même nom à des choses différentes ».
- S. Banach (attribué) : « A mathematician is a person who can find analogies between theorems; a better mathematician is one who can see analogies between proofs and the best mathematician can notice analogies between theories. One can imagine that the ultimate mathematician is one who can see analogies between analogies. »
- G. A. Deschamps, « Gaussian beam as a bundle of complex rays », *Electronics Letters* 7, 684–685 (1971).
- [« What is special about the divisors of 24? »](https://arxiv.org/abs/1104.5052) : les bases où x² ≡ 1 pour tout x premier avec la base.
- D. Jeffery (UNLV), [« Ancient Babylonian astronomers and why we have 360° in the circle »](https://www.physics.unlv.edu/~jeffery/astro/babylon/babylonian_360_degrees.html).
- J. Miller, [« Earliest Uses of Various Mathematical Symbols »](https://mathshistory.st-andrews.ac.uk/Miller/mathsym) (MacTutor) : les dates des notations.
- L. J. Garay, « Quantum gravity and minimum length », *Int. J. Mod. Phys. A* 10, 145–166 (1995), [arXiv:gr-qc/9403008](https://arxiv.org/abs/gr-qc/9403008) : la longueur minimale.
