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
- Ce que ça transporte : le cube et la chèvre ont w₀·θ = 1, donc une « longueur d'onde » λ = π. La chèvre classique (le piquet sur la clôture, d = 1) est exactement à la distance de Rayleigh de son faisceau : la largeur y vaut √2 fois le col (ρ = |1 + i| = √2, la diagonale 1x, 1y) et la phase de Gouy y vaut 45°.

## 2. Les bases sont des objets, et leur histoire suit des besoins d'organisation

**Une base n'est pas une simple convention d'écriture.**
- Elle fixe la grille qui découpe l'espace entre les nombres : les fractions qui tombent juste, l'horloge des derniers chiffres, l'existence d'un i, la régularité des nombres flottants. La base 2 et la base 10 sont deux objets physiques différents (partie XIX).
- 1, 2, 3, 4, 5, 6 est un compte naïf. Un compte jumelé avec des données est une séquence d'épreuves qui forme un atlas.
  - Chaque chiffre est une épreuve : dans quelle case le nombre tombe-t-il ?
  - Le nombre est la suite emboîtée de ces cases : une suite de points, pas une infinité de chiffres à écrire. C'est l'encadrement certain des parties XVII et XVIII.
- Le compte naïf est comme le modèle de Thomson pour se représenter l'atome : plus simple à comprendre, et c'est exactement pour ça qu'on le garde pour compter. (Nuance proposée à l'auteur en partie XIX : Thomson a été réfuté ; Bohr, faux dans son image mais juste dans ses nombres, serait un parallèle plus proche.)
- **Les échelles.** On part de l'échelle humaine, puis on monte ou on descend sur un cône à deux échelles logarithmiques (−zⁿ, +zⁿ). Thalès relie toute taille à un objet que les humains connaissent : un sou (19,05 mm) cache la Lune à 2,11 m.

**La succession des standards : base 60, base 12, base 10 (la thèse de l'auteur).**
- **Bases 60 (360°) et 12 :** elles servaient à simplifier des problèmes topologiques et géométriques observables (le ciel, le cercle, le jour, l'année).
- **Base 10 :** elle simplifie les analyses conceptuelles déjà simplifiées par la base 60 (360), par les nombres complexes.
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

## 6. Ton et façon de répondre

- **Langue et ton.** Réponds en français, sur un ton simple et conversationnel, et tutoie l'auteur.
- **Explications.** Explique pourquoi et comment, pas seulement quoi. Dis ce qui est sûr et ce qui ne l'est pas, et donne des sources en liens.
- **Partir de ses propositions.** Cherche d'abord le procédé commun qui les soutient (§ 1), calcule-le, puis dis ce qui reste ouvert. N'affaiblis pas une proposition par réflexe.
- **Vérifier.** Vérifie chaque nombre par un calcul, dans un script, avant de l'écrire.

## 7. Conventions de la série

**Chaque message de l'auteur devient en général une nouvelle « Partie », avec :**
- `scripts/<nom>.py`, qui utilise le style commun de `scripts/figures.py` (`import figures as F`, puis `F.sauver`) ;
- `figures/<lettre><n>_<nom>.png`, avec une lettre par partie (p = XVI, q = XVII, r = XVIII, t = XIX) : prends la suivante libre ;
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
