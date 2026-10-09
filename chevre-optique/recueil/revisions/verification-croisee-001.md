# Vérification croisée de la révision 001 : le recouvrement v2, les doublons et les contradictions

Le plan ([`plan-001.md`](plan-001.md), § 5) confiait cette vérification à un neuvième agent. Deux redémarrages du conteneur et une limite d'usage l'en ont empêché ; je l'ai faite moi-même. Je me suis servi des sorties structurées des agents de dossier (leurs corrections du recouvrement, leurs verdicts sur les fiches, leurs congruences, leurs erreurs trouvées et leurs fiches proposées) et de la lecture des dossiers. La synthèse est [`revision-001.md`](revision-001.md). Le nerf v2 est recalculé par [`scripts/revision_001.py`](../../scripts/revision_001.py), qui lit le bloc JSON du § 1.

## En bref

- **Le recouvrement v2.** Chaque agent a ajouté des parties à son dossier, sept y ont ajouté des fiches, et un seul a retiré quelque chose (ombres : la fiche 010). Les huit dossiers passent de 87 à 126 appartenances de parties, et de 34 à 41 appartenances de fiches (§ 1).
- **Six résultats ont été trouvés deux ou trois fois, chacun par son propre calcul.** Ce sont des confirmations (§ 5.1).
- **La fiche 003 est la plus partagée du recueil** : 6 dossiers sur 8 la contiennent dans le recouvrement v2.
- **Le nerf v2** (§ 3) : les 4 trous du corpus de v1 sont refermés ; au niveau des fiches, il reste 11 triangles vides, autant que le hasard, dont 9 passent par le dossier bases. C'est là que de nouvelles fiches compteraient le plus.
- **Trois désaccords entre agents, qui deviennent des précisions :** le « 2,8 » de Perron (une pente, pas une constante), la palette du Venn (mesurée ou de conception) et la fiche 005 (§ 5.2).
- **Le plan lui-même avait sept erreurs,** trouvées par les agents et par les tests (§ 5.3).
- **64 fiches proposées**, dont 13 déjà faites par la révision (un test du script ou une des fiches 016 à 021) ; elles sont classées par dimension au § 7.

## 1. Le recouvrement v2

| dossier | parties ajoutées | fiches ajoutées | la raison principale |
|---|---|---|---|
| [corde](../dossiers/corde-et-dimensions.md) | II, X, XVII, XIX, XXVII | 003, 011 | la corde dans un polygone (II § 9), la corde de Ptolémée de 70,81° (X § 5), la récursion d'argent (XVII), le cône à sommet imaginaire (XIX § 6), le tiers de dimension (XXVII § 6) ; les fiches de K1 et K10 |
| [moitiés](../dossiers/moities-et-crans.md) | VI, X, XV, XVI, XIX, XXIII, XXV, XXVIII | 012 | la lunule d'Hippocrate (VI), la grille (XV), le plateau 2^(−1/n) (XVI § 3), le tableau du grain (XXIII § 4), Borel–Padé (XXV), Perron à k = 2 (XXVIII) ; Bonferroni (fiche 012) |
| [bases](../dossiers/bases-congruences-premiers.md) | VI, XV, XVIII, XX, XXII, XXIV | 002 | 10 − 1 = 3² (VI § 3 ter), l'aiguille (3, 1) sur la grille décalée (XV § 5), le cercle de Gauss (XVIII), le comma et 19/12 (XX § 6), 3ⁿ modulo 10 (XXII), le 4/3 de 1/x₀ (XXIV) ; le diésis (fiche 002) |
| [grain](../dossiers/grain-pixels-centres.md) | XXIV, XXV, XXVI, XXVII | 003 | le grain lu en longueur ou en aire (XXIV), la série coupée au mieux (XXV), Kakeya au grain δ (XXVI), l'échelle des taux de change (XXVII § 3) ; n·tan(π/n) (fiche 003) |
| [lumière](../dossiers/lumiere-et-physique.md) | XXI, XXIX | 003 | Self (1983) et le doublement de l'aire (XXI § 3), l'ombre Σωⁱ et son 34-gone (XXIX § 5.4) ; le polygone circonscrit (fiche 003). Corrections relevées dans son § 8 (sa sortie structurée est perdue) |
| [aiguilles](../dossiers/aiguilles-kakeya-perron.md) | VIII, XI, XV, XXI, XXIX, XXX | 009 | les trois façons de retourner l'aiguille (VIII), les trois distances (XI), la demi-case de l'hexagone (XV § 5), l'aiguille de 50 (XXI), un bit par pas (XXIX), la fiche 011 sans sa partie (XXX § 6.4) ; les aigrettes (fiche 009) |
| [ombres](../dossiers/ombres-cube-venn.md) | V | — | la branche Perron de l'arbre P1 part de la partie V ; la fiche 010 est retirée : le plan la range dans P2, et elle n'a de cube que le dessin |
| [méthode](../dossiers/hasard-et-methode.md) | I, V, X, XIV, XXII, XXIII, XXV | 006 | les cas d'erreur de chaîne qu'il a lus ou vérifiés : l'erratum d'Ullisch et Fraser corrigé par Meyerson (I), la « quasi-coïncidence » (V), le trou qui suit le point P (X), le « 2,8 » et T5 (XIV), les trois phrases corrigées (XXII, XXIII), Borel–Padé contre la troncature (XXV) ; la fiche 006 (une causalité établie sur l'analyse). Les quatorze autres fiches sont des cas d'audit, pas des membres |

**Une précaution.** Chaque agent a estimé l'effet de ses propres corrections sur le nerf (corde : 9 → 14 triangles vides au niveau des fiches ; grain : 9 → 6 ; aiguilles : 11 → 13 ; moitiés : 20 → 17 au niveau des fiches et des parties ; ombres : 10 → 11 en retirant la fiche 010). Ces estimations ne s'additionnent pas : chacune change un seul dossier. Le nerf v2, avec toutes les corrections ensemble, est au § 3.

Le bloc lu par le script, au format du § 1.9 du plan :

```json
{
  "revision": "001",
  "version": "v2",
  "dossiers": {
    "corde-et-dimensions": {
      "parties": ["I", "II", "III", "IV", "VI", "VII", "X", "XV", "XVI", "XVII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVII"],
      "fiches": ["003", "010", "011", "014"]
    },
    "moities-et-crans": {
      "parties": ["I", "II", "IV", "V", "VI", "VIII", "X", "XIV", "XV", "XVI", "XVII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVII", "XXVIII", "XXIX", "XXX"],
      "fiches": ["005", "010", "012"]
    },
    "bases-congruences-premiers": {
      "parties": ["III", "VI", "VII", "IX", "XI", "XII", "XIV", "XV", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIV", "XXV", "XXVI", "XXVIII"],
      "fiches": ["001", "002", "005", "013", "014", "015"]
    },
    "grain-pixels-centres": {
      "parties": ["X", "XIV", "XV", "XVIII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXIX", "XXX"],
      "fiches": ["001", "003", "006", "007", "008", "011"]
    },
    "lumiere-et-physique": {
      "parties": ["I", "II", "VIII", "IX", "X", "XI", "XII", "XIII", "XVII", "XVIII", "XIX", "XX", "XXI", "XXVIII", "XXIX", "XXX"],
      "fiches": ["002", "003", "006", "009"]
    },
    "aiguilles-kakeya-perron": {
      "parties": ["V", "VIII", "X", "XI", "XIII", "XIV", "XV", "XVII", "XIX", "XXI", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"],
      "fiches": ["003", "009", "011"]
    },
    "ombres-cube-venn": {
      "parties": ["II", "V", "XV", "XX", "XXI", "XXII", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"],
      "fiches": ["003", "004", "005", "006", "008", "009", "015"]
    },
    "hasard-et-methode": {
      "parties": ["I", "III", "V", "VI", "X", "XIII", "XIV", "XVIII", "XXII", "XXIII", "XXIV", "XXV", "XXVII", "XXIX", "XXX"],
      "fiches": ["002", "003", "004", "005", "006", "007", "012", "015"]
    }
  }
}
```

## 2. Les congruences, vues par plusieurs dossiers

Une congruence est vérifiée quand deux sections locales se recollent sur ce qu'elles partagent (revision-001.md, § 6). Ici, on regarde si les dossiers qui l'ont traitée sont d'accord.

| | dossiers et tests | ce qu'ils trouvent | accord |
|---|---|---|---|
| K1 | corde ; T3 | se recolle aux ordres 2 et 3 avec le décalage n → n + 49/10 ; obstruction à l'ordre 4 | accord. Le plan disait « dès l'ordre 3 », vrai seulement sans décalage |
| K2 | lumière, aiguilles, moitiés, ombres | les trois 34 (aigrettes, ombre Σωⁱ, éventails) sont un seul fait pour N impair ; calculé pour N = 3 à 20 par deux agents (A) | accord à quatre. Moitiés ajoute l'obstruction en Kakeya fini (en caractéristique 2, x ↦ −x est l'identité) ; lumière ajoute la réserve de la phase (une ouverture complexe casse la symétrie de Friedel) |
| K3 | bases ; § 4.3 | se recolle par la famille q² + 1 et le lemme des chiffres, démontré pour tout q ≥ 2 | accord |
| K4 | moitiés, aiguilles, méthode ; T5 | obstruction : deux procédés, Bonferroni pour Kakeya fini et l'involution pour les hémisphères | accord à quatre. La piste XIV–XX se ferme. Méthode ajoute que les deux troncatures de Bonferroni bornent en sens opposés : l'ordre 1 majore (le p corrigé), l'ordre 2 minore (la taille de Kakeya) |
| K5 | bases, ombres | bases : obstruction, aucune transformation connue entre le 17 de Henderson et le 17 de i | **ombres trouve une implication** : si i existe modulo n (n ≡ 1 mod 4), aucun Venn simple et symétrique n'a le complément pour symétrie. Un tel Venn serait antipodal, et la parité des croisements dans le plan projectif exige C(n, 2) impair. Impossible à 17 ; à 19 et 23, ni exclu ni construit. K5 se recolle donc en partie, par une implication, pas par une transformation |
| K6 | grain, lumière, méthode ; T4 | le centre de la lumière suit la palette ; la seconde cause est le seuil, pas l'ordre de dessin | **désaccord partiel** (§ 5.2), tranché sur un système modèle : méthode refait l'expérience sur un Venn à 13 courbes de palette connue, et G·H₁ prédit l'écart sans paramètre libre (vérifié, § 4.12). La palette réelle de l'image à 17 courbes reste ouverte |
| K7 | moitiés, grain, aiguilles | se recolle pour la pente : un cran, soit un facteur 2 sur l'exposant | accord sur la pente. Deux obstructions nouvelles : le « 2,8 » n'est pas une constante (aiguilles) ; l'aire ½ de Perron à 4 branches n'est pas un effet de cran (moitiés). La cause commune du logarithme reste ouverte (grain) |
| K8 | corde, bases, méthode ; T7 | une coïncidence de petits entiers | accord à trois. Ce qui se recolle passe par log₂ 3 et le comma (19/12) |
| K9 | bases, méthode ; T6 | se recolle en une tour 2-adique, à aires inégales | bases ajoute l'enchevêtrement fixé par la réciprocité quadratique (A). **Méthode : « se recolle trivialement »** : la division par deux est la loi de toute valuation 2-adique, et aucun invariant de Perron (l'aire 2/(k + 2)) n'y passe. La synthèse est corrigée |
| K10 | corde, grain ; § 4.4 | exact : c'est l'isopérimétrie | accord, avec une précision du dossier grain : le seuil vaut 4π·(s/a)² pour des croisements espacés de a et des régions de côté s. Le 13 vient du choix a = s = 2 px (§ 5.2) |

**Les congruences nouvelles des agents** (la plus forte de chaque dossier ; chacun a sa table au § 5) :
- *Corde.* Le triangle de Thalès de la partie XXIV (§ 5) est le triangle du simplexe de la classification : (PQ, QP′) = (c_K, d_K), avec K − 1 = 1/x₀ (exact). Et la part de la clôture broutée vaut 2α_n/360°, avec cos α_n = x₀ : 39,34 % en est le cas n = 2.
- *Moitiés.* Le cercle R/√2 est fixé par trois gestes (le miroir d'aire, l'inversion des jumeaux, la dilatation d'un cran), en toute dimension (exact). Les écarts à la moitié sont des miroirs : ½ − 1/√(2πn) sur la clôture, ½ + 1/√(2πn) sur le volume (calculé).
- *Bases.* Le dernier chiffre d'un premier dit si le nombre d'or existe modulo p ; le cocycle se ferme sur 3, 9, 7 (démontré).
- *Grain.* La loi des 8R de la partie XVIII et le budget de la moitié du Venn de la partie XXX se recollent exactement (8⌊R + ½⌋ et 8⌊r⌋ + 4).
- *Aiguilles.* i ≡ a/c (mod b) de la partie XIX et l'aiguille primitive (a, c) de norme b = a² + c² de la partie XIV se recollent entièrement. Les coupes de Perron et les niveaux du Venn se recollent sur le cube {0, 1}ⁿ, avec une obstruction : binaire contre binomial.
- *Lumière.* Tout masque de N zones égales a ses foyers par paires, I(N − u) = I(u) (vérifié sur 2 000 masques) : la symétrie de la partie VIII ne vient pas de Fibonacci.
- *Ombres.* La face que choisit a modulo 3 dans la fiche 015 est une restriction du cube (la fibre au-dessus de 0), pas une ombre. Et 3 est le seul premier impair, étranger à 10, qui divise une différence de deux chiffres des unités (6 = 7 − 1 = 9 − 3) : c'est le facteur 2 de Hardy et Littlewood pour l'écart 6, la limite de la dérive de la fiche 021. La face de la fiche 015 et le 2 de la fiche 021 sont le même 3.
- *Ombres.* Les périodes de Gauss du 17-gone sont les ombres Σωⁱ des régions fixées par un sous-groupe de (ℤ/17)* ; 4 ≡ i engendre celui d'ordre 4 (calculé à 10⁻¹⁵).
- *Méthode.* Les quatre tests à tolérance sont des seuils sur le seul écart d (128 < 186 < 806 < 259 000 ppm) : ils sont totalement ordonnés, et leur cocycle est trivial. Or l'étiquette « structure » ou « hasard » n'est pas une fonction de d : rangés par écart, les six cas non triviaux du banc alternent S C S S S C. Aucun seuil ne peut les séparer.

## 3. Les triangles vides : v1 contre v2

Résultats : [`resultats/revision_001.md`](../../resultats/revision_001.md), § 3. Mêmes trois niveaux que pour v1 : (1) les fiches ; (2) les fiches sans les deux hasards testés 002 et 004 ; (3) les fiches et les parties.

| recouvrement | niveau | sommets, arêtes, triangles, tétraèdres | Betti b₀, b₁, b₂ | triangles vides | triangles remplis : éléments communs en moyenne | nul : b₁ moyen | nul : b₂ moyen | nul : triangles vides en moyenne | p (nul ≥ observé) |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| v1 | brute | 65 | 1,3162 | 40 | 1,6427 | 5 % | 0,3264 | 0,928 |
| v1 | aires égales | 65 | 1,3224 | 40 | 1,5645 | 10 % | 0,2421 | 0,966 |
| v1 | 1 | 8, 18, 7, 1 | 1, 5, 0 | 9 | 1,1 | 3,08 | 0,00 | 5,7 | 0,162 |
| v1 | 2 | 8, 17, 7, 1 | 1, 4, 0 | 7 | 1,1 | 2,66 | 0,00 | 4,8 | 0,238 |
| v1 | 3 | 8, 28, 36, 11 | 1, 0, 5 | 20 | 1,5 | 0,21 | 5,59 | 18,6 | 0,387 |
| v2 | 1 | 8, 24, 25, 16 | 1, 3, 0 | 11 | 1,3 | 1,71 | 0,10 | 10,1 | 0,436 |
| v2 | 2 | 8, 23, 24, 16 | 1, 3, 0 | 8 | 1,3 | 1,78 | 0,05 | 9,6 | 0,638 |
| v2 | 3 | 8, 28, 56, 60 | 1, 0, 1 | 0 | 4,8 | 0,00 | 0,05 | 0,2 | 1,000 |

**v2 : les triangles vides au niveau des fiches** (11) :
- bases-congruences-premiers · corde-et-dimensions · grain-pixels-centres : trou du recueil (une partie les réunit, la fiche manque).
- bases-congruences-premiers · corde-et-dimensions · hasard-et-methode : trou du recueil (une partie les réunit, la fiche manque).
- bases-congruences-premiers · corde-et-dimensions · lumiere-et-physique : trou du recueil (une partie les réunit, la fiche manque).
- bases-congruences-premiers · corde-et-dimensions · moities-et-crans : trou du recueil (une partie les réunit, la fiche manque).
- bases-congruences-premiers · corde-et-dimensions · ombres-cube-venn : trou du recueil (une partie les réunit, la fiche manque).
- bases-congruences-premiers · grain-pixels-centres · hasard-et-methode : trou du recueil (une partie les réunit, la fiche manque).
- bases-congruences-premiers · grain-pixels-centres · lumiere-et-physique : trou du recueil (une partie les réunit, la fiche manque).
- bases-congruences-premiers · grain-pixels-centres · ombres-cube-venn : trou du recueil (une partie les réunit, la fiche manque).
- bases-congruences-premiers · lumiere-et-physique · ombres-cube-venn : trou du recueil (une partie les réunit, la fiche manque).
- corde-et-dimensions · hasard-et-methode · moities-et-crans : trou du recueil (une partie les réunit, la fiche manque).
- corde-et-dimensions · moities-et-crans · ombres-cube-venn : trou du recueil (une partie les réunit, la fiche manque).
- Bilan v2 : 11 trous du recueil, 0 trous du corpus.
- Les fiches laissent 11 triangles vides, contre 10,1 en moyenne pour des dossiers de mêmes tailles tirés au hasard (p = 0,44) : autant que le hasard. Les trous se lisent donc un par un, comme des pistes, pas comme une preuve.
- **Avec les parties (niveau 3), les boucles se remplissent** (b₁ = 0), mais il reste b₂ = 1 cavité (nul : 0,05 en moyenne, p = 0,047). Une cavité, ce sont quatre dossiers dont les quatre triplets se recollent, sans élément commun aux quatre : un trou d'un étage plus haut. Les 10 tétraèdres creux :
  - aiguilles-kakeya-perron · bases-congruences-premiers · grain-pixels-centres · lumiere-et-physique
  - aiguilles-kakeya-perron · bases-congruences-premiers · hasard-et-methode · lumiere-et-physique
  - aiguilles-kakeya-perron · bases-congruences-premiers · hasard-et-methode · ombres-cube-venn
  - bases-congruences-premiers · corde-et-dimensions · grain-pixels-centres · lumiere-et-physique
  - bases-congruences-premiers · corde-et-dimensions · hasard-et-methode · lumiere-et-physique
  - bases-congruences-premiers · grain-pixels-centres · hasard-et-methode · ombres-cube-venn
  - bases-congruences-premiers · grain-pixels-centres · lumiere-et-physique · moities-et-crans
  - bases-congruences-premiers · grain-pixels-centres · lumiere-et-physique · ombres-cube-venn
  - bases-congruences-premiers · hasard-et-methode · lumiere-et-physique · moities-et-crans
  - bases-congruences-premiers · hasard-et-methode · lumiere-et-physique · ombres-cube-venn

**Ce que les corrections ont changé** (ma lecture des tableaux ci-dessus).
- *Les 4 trous du corpus de v1 sont refermés.* Ils passaient tous par le grain. Les parties ajoutées par les agents (XXIV à XXVII pour le grain, XIV et XXV pour méthode, XXIX et XXX pour aiguilles, XV et XVIII pour bases) donnent une partie commune à ces triplets. C'étaient des trous de la lecture du plan, pas du corpus.
- *Au niveau des fiches, v2 laisse 11 triangles vides*, autant que des dossiers de mêmes tailles tirés au hasard (10,1 en moyenne, p = 0,44). Tous sont des trous du recueil : une partie réunit les trois dossiers, la fiche manque.
- *Le dossier bases est dans 9 des 11 triangles vides, et dans les 10 tétraèdres creux.* Ses six fiches touchent peu les autres dossiers : une seule fiche commune avec corde (014), grain (001), lumière (002) ou moitiés (005), aucune avec aiguilles. C'est le sujet que le recueil relie le moins au reste, et c'est là que de nouvelles fiches compteraient le plus. Par exemple, celle que propose le dossier corde : les facteurs 2 des polynômes de la chèvre comptent les retenues de la base 2 (Kummer).
- *Un trou ouvert par une correction.* En retirant la fiche 010, ombres ouvre le triangle corde · moitiés · ombres : la 010 le cachait. Il demande une fiche du cercle R/√2, celle des trois gestes que propose le dossier moitiés.
- *Avec les parties (niveau 3)*, plus aucun triangle vide (20 en v1), et une seule cavité, b₂ = 1 (0,05 en moyenne pour le nul, p = 0,047). C'est le seul indicateur du nerf qui sorte du hasard, de justesse, et c'est un test parmi une dizaine : à surveiller, pas une découverte. Le dossier ombres rappelle que le nerf n'est pas la réunion (36 intersections non contractiles sur 166, dans la v2 à six corrections qu'il a lue) : cette cavité est une propriété du classement, pas du corpus.
- *Ce que ça dit des révisions suivantes.* Une correction d'agent referme des trous du corpus (on lit mieux le corpus) et en déplace vers le recueil (il manque des fiches). Le nerf sert donc à dire où écrire les prochaines fiches : entre bases et les autres dossiers, et sur le cercle R/√2.

## 4. Les arbres corrigés

Figure : [`rev001_perron_venn.png`](../../figures/rev001_perron_venn.png), panneau b. Le tableau complet est au § 5 de la synthèse ; ici, ce qui change, et qui le dit.

| arbre | disque | ce qui change | dossiers et tests |
|---|---|---|---|
| P1 l'ombre du cube {0, 1}ⁿ | D6 | une branche de la parité, les trois 34 (K2) ; un cube et huit regards, tous déjà écrits dans le corpus ; la fiche 015 y entre par une restriction, pas par une ombre ; les périodes de Gauss sont des ombres ; la branche Perron part de la partie V | lumière, aiguilles, moitiés, ombres |
| P2 la moitié | D1 | un seul cercle R/√2, fixé par trois gestes ; la branche « Kakeya fini » se détache (Bonferroni) | moitiés ; T5 |
| P3 le terme x²/6 | D1 | même 1/6, obstruction à l'ordre 4 ; le « dernier 2 » du ménisque compte les dérangements de 3 | corde ; T3 ; § 4.10 |
| P4 le quart de tour i modulo b | D2 | la famille q² + 1, le lemme des chiffres, Φ₆(10) = 7 × 13, le dernier chiffre et le nombre d'or | bases ; § 4.3 et 4.10 |
| P5 le budget en bits | D3 | le seuil isopérimétrique, la loi des 8R ; K7 tient pour la pente seulement | grain, aiguilles ; § 4.4 |
| P6 les réduites et les trois distances | D2 | le diésis et le comma, deux écarts du même théorème ; la demi-case (Pick) pour l'or, l'argent, Farey et l'hexagone | bases, aiguilles |
| P7 la loi de l'écart | D7 | sa réserve : une dérive peut croiser une constante (π, 2√2) | § 4.2 et 4.9 |
| P8 le cône à sommet imaginaire | D8 | la branche « photocentre » se détache : il n'a ni col ni distance de Rayleigh ; la forme de Newton x·x′ = c revient cinq fois | lumière |
| **P9 (nouveau)** le barycentre pesé | D8, contre D3 et D7 | le centre de la lumière est le premier harmonique des poids, G·H₁ ; le seuil en est un second canal ; établi par intervention sur un Venn à 13 courbes de palette connue | lumière, grain, méthode ; T4 ; fiche 018 |

## 5. Les doublons et les contradictions

### 5.1 Trouvé deux fois : des confirmations

- **La fiche 010.** Corde et moitiés, chacun par son calcul, trouvent que 39,34 % n'est exact que pour le cercle du bord : la part monte quand on rentre (39,57 % pour l'anneau de rayon 0,99 ; 39,52 % au niveau 4 du dessin à aire égale). La fiche est corrigée. Ombres la retire de son dossier : elle n'a de cube que le dessin. En la retirant, il ouvre un triangle vide, corde · moitiés · ombres : la fiche 010 cachait ce trou, qui demande une fiche du cercle R/√2 (celle des trois gestes, proposée par moitiés).
- **K2, les trois 34.** Lumière et aiguilles l'ont calculé chacun pour N = 3 à 20 ; moitiés l'a relié à x ↦ −x.
- **K4, la moitié de Kakeya fini.** Moitiés, aiguilles et le test T5 concluent tous trois à deux procédés.
- **Le minimum 2/(k + 2).** Moitiés (pour k = 2, l'aire vaut ½ sur tout un segment de rapports) et aiguilles (pour k = 3, 43/108 < 2/5, vérifié au § 4.10) trouvent chacun que c'est le minimum de la borne, pas celui de l'aire. La partie V l'avait vu en nombres (0,3981). CLAUDE.md et la partie XXVIII sont précisés.
- **La palette comme cause du centre de la lumière.** Grain et lumière l'ont trouvée tous deux ; ils ne s'accordent pas sur les détails (§ 5.2). Méthode tranche le statut : la cause est établie sur l'analyse (la pesée, le seuil), par des interventions ; sur l'image, ce n'est encore qu'un ajustement.
- **Le « 93 % » et le banc d'essai.** Lumière a montré que le 93 % est le taux de base ; méthode, que le « 10/10 » de la variation est en partie écrit à la main. Deux erreurs de la même partie XXX, trouvées par deux chemins : un score cité sans son témoin.

### 5.2 Les désaccords entre agents

1. **K7 : le « 2,8 » de Perron sur une grille.** Le dossier grain tient l'analogie pour « confirmée » avec cette valeur. Le dossier aiguilles la calcule plus loin : « part × log₂ n » culmine à 2,83 (n = 256), puis baisse à 2,57 (n = 65 536). Les deux ont raison sur la pente ; la valeur n'est pas une constante. Verdict : se recolle pour la pente, pas pour les valeurs.
2. **K6 : quelle palette ?** Les deux dossiers disent que les couleurs mesurées (les 5 % de pixels les plus clairs de chaque teinte) ne suffisent pas : avec elles, les directions relatives des écarts ratent de 55° (luminance) et 47° (clarté) (lumière, (A)).
   - Le dossier grain ajuste une palette de conception presque isoluminante (Y₀ = 0,30 à 0,36) et un facteur G de 181 à 194 px. Il retrouve les quatre pesées continues à 1,4 – 2,0 px près, et leurs phases à 6° près ; il conclut « obstruction levée sous condition ».
   - Mais il note lui-même deux restes : le bras de levier mesuré vaut 379 px, deux fois le G ajusté ; et les masques du modèle vont de 1 à 17 px quand les mesures vont de 0,4 à 27 px, avec des directions décalées de 10° à 40°.
   - Le dossier lumière garde le statut « structure, à tester » : le rapport des pesées Y/E vaut 0,0132, entre 0,003 (palette isoluminante) et 0,23 (couleurs mesurées).
   - **Le dossier méthode a fait le rendu de contrôle** (§ 3.6 ; refait par le script de la révision, § 4.12) : sur le Venn à 13 courbes du traceur, de palette et d'ordre connus, repeint par son propre rendu, G·H₁ prédit l'écart **sans paramètre libre** (2,08 px prédits, 2,05 à 2,20 observés, phases à 11° près), et quatre autres ordres de dessin ne déplacent le centre que de 0,3 px au plus. À luminance égale, l'écart en luminance tombe à 0,13 px quand ceux de la moyenne RGB et de l'énergie restent à 2,3 et 1,6 px : le motif de l'image à 17 courbes.
   - Mon verdict : la loi est établie par intervention sur un système modèle, et la lecture du dossier grain (une palette presque isoluminante) en sort renforcée. Sur l'image à 17 courbes, la palette reste ajustée, faute du code de rendu. Le test T4 a ajouté un second canal, le seuil (fiche 018) ; le témoin du dossier méthode montre qu'un effet de seuil signe une grandeur seuillée qui varie d'une courbe à l'autre.
3. **La fiche 005.** Moitiés trouve « miroir + complément » en tête dans les 18 certificats, à 1,5 à 2,3 fois le hasard, et conclut « hasard testé, cause ouverte » (A). Bases la juge « compatible avec le hasard ». Le calcul de moitiés (son § 7.3) est à refaire avant de trancher.
4. **Pas un désaccord : la fiche 014.** Corde y voit un lien faible, par les nombres (√2, 2/√3, √(3/2)) ; bases, un lien exact avec F₉. Ils parlent de deux parties de la fiche.
5. **Une précision de K10.** Le seuil vaut n* = 4π·(s/a)², pour des croisements espacés de a et des régions de côté s. Avec a = s = 2 px (le choix de la partie XXX), on trouve 4π et 13 courbes ; avec a/s = 1,5, le seuil tombe à 5,6 courbes ; avec a/s = 0,5, il monte à 50,3. L'isopérimétrie est la loi ; le 13 est le cadre. C'est exactement ton sujet d'étude : la restriction du cadre fixe le nombre qu'on observe.

### 5.3 Les erreurs du plan

- *K1* : « obstruction dès l'ordre 3 ». Vrai sans décalage ; avec le décalage s = 49/10, l'ordre 3 se recolle et l'obstruction est à l'ordre 4 (corde, refait par T3).
- *K6* : la seconde cause proposée, l'ordre de dessin, est écartée deux fois (T4 : p = 0,64 ; grain : contraste d'ordre −6,0 %, comme les témoins). La seconde cause est le seuil.
- *K7* : le « 2,8 » pris pour une constante (aiguilles).
- *K10* : le polygone inscrit du plan donne n* = 12,295 ; le n-gone de même aire du script, 12,824 ; le cercle, 12,566. Les trois donnent 13 courbes (grain).
- *La liste de lecture de l'agent corde* oubliait six fichiers, dont carte-connexions.md et archimede.md (corde).
- *T6* : « Midy en Perron ». La division par deux à chaque étage est la loi de toute valuation 2-adique, pas un invariant de Perron (méthode). La synthèse est corrigée.
- *T1 et T8* sont des nuls (la dernière ligne de la table du § 10), pas des variations du paramètre ; et le nul de T1 garde les marges, ce qui le rend conservateur quand la structure est dans les tailles des dossiers (méthode).

## 6. Les trous dans les données publiées

La synthèse en fait le tableau (revision-001.md, § 9), et chaque dossier a le sien (§ 6.3). La vérification croisée ajoute ceci : **quatre trous sont désignés par deux dossiers ou plus à la fois**, ce qui les rend plus sûrs.
- *La chaîne de rendu des images de Venn* (grain, lumière) : la palette, l'espace de mélange, l'anticrénelage et l'ordre de dessin des PNG à 17 courbes ne sont pas publiés. C'est aussi ce qui bloque K6.
- *Le déplacement induit par la couleur* (lumière, grain) : pour N sources colorées en symétrie d'ordre N, le centre dépend du poids et du seuil. À répliquer sur les binaires « CID » de SDSS (Pourbaix et al., 2004) : à calculer.
- *Les constantes de Perron et de Kakeya au grain fini* (aiguilles, moitiés, grain) : pas de table publiée des rapports optimaux, ni de la constante entre π/2 et π·ln 2.
- *Ce que le dépôt de Dzoba ne publie pas* (ombres, méthode, grain) : la moitié des croisements et les croisements par niveau, la symétrie par le complément, le profil des défauts par rang, l'histogramme des degrés, l'ordre de dessin et le code de rendu. Les six certificats à 23 courbes sont publiés (Zenodo) mais pas lus : k₁, N_l et la part des triangles s'y liraient.

**Les références à vérifier**, relevées par plusieurs dossiers : le titre de Wielen (1996) ; le nom de la revue de Fraser en 1984 ; les deux articles « Córdoba (1977) » ; le Nikon D800E ; la référence exacte des corrections de chromaticité de Gaia.

## 7. Les nouvelles fiches, classées par dimension

Chaque dossier propose ses fiches au § 6.1, avec leur type, leur statut, leur script et leur image. Elles ne sont pas écrites dans le recueil : on les écrira quand une partie les reprendra (revision-001.md, § 10). La colonne « puis » donne les dimensions voisines ; « déjà fait » renvoie au test ou à la fiche de la révision qui la recouvre.

64 fiches proposées par 8 dossiers.

| dimension | fiches | dont déjà faites |
|---|---:|---:|
| D1 la chèvre et les cordes | 8 | 1 |
| D2 bases, chiffres et congruences | 10 | 4 |
| D3 grain, pixels et précision | 7 | 1 |
| D4 optique et diffraction | 4 | 0 |
| D5 Kakeya, Perron et aiguilles | 10 | 4 |
| D6 sphères, cubes, Venn et symétries | 9 | 1 |
| D7 hasard et méthode | 10 | 2 |
| D8 physique | 6 | 0 |

**D1 la chèvre et les cordes** (8)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| corde | La chèvre plane est contenue dans la série de la chèvre infinie | structure | — | — |
| corde | Les seuils entiers de IV § 4 ne tiennent pas en dimension réelle | hasard | D7 | — |
| corde | δ₂ ≈ δ₃ à 10⁻⁵ : une proximité nommée trois fois, jamais expliquée | ouvert | D7 | — |
| corde | Les polygones circonscrits à 4 et à 8 côtés ont la même corde (1,165644) | exact | D6 | — |
| moitiés | La corde de la moitié du carré ne change pas quand on coupe ses quatre coins, jusqu'à t = 0,5989 | exact | — | — |
| moitiés | Les écarts à la moitié sont des miroirs : ½ − 1/√(2πn) sur la clôture, ½ + 1/√(2πn) sur le volume | structure | — | — |
| méthode | δ₂ ≈ δ₃ : 2·10⁻⁴, donc « ouvert », pas « hasard » | ouvert | D7 | — |
| corde | Le « −2 » de la coquille est le nombre de dérangements de 3 : E[(1 − E)^j] = (−1)^j·!j | exact | D7 | § 4.10 (vérifié) |

**D2 bases, chiffres et congruences** (10)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| corde | Les facteurs 2 des polynômes de la chèvre comptent les retenues de la base 2 (Kummer) | exact | D1 | — |
| bases | Midy est un demi-tour, et 10^(L/4) est un i : la tour du 17-gone | exact | D6 | — |
| bases | Le diésis et le comma sont le troisième écart du théorème des trois distances | exact | D5 | — |
| bases | Le dernier chiffre d'un premier dit si le nombre d'or existe modulo p ; la course de Tchebychev | exact pour le lien | D7 | — |
| bases | La famille de Pell des bases à deux écritures : le 7 de Hutton et le 239 de Machin sont des i | exact | D5 | — |
| ombres | La face choisie par a mod 3 (fiche 015) est la fibre de l'ombre au-dessus de 0 ; 3 est le seul premier qui coupe deux coordonnées | exact | D6 | — |
| bases | Le 3 de 1/7 est le i de la base 10 : la famille b = q² + 1 | exact | D5 | § 4.3 (vérifié) |
| bases | La tour 2-adique des périodes et son enchevêtrement par la réciprocité quadratique (T6, T6b) | structure | D7 | § 4.6 (vérifié) |
| bases | Les trois 4/3 sont une coïncidence de petits entiers ; la loi du comma est derrière (T7) | hasard | D7, D1 | § 4.5 (vérifié) |
| bases | La dérive des dizaines de premiers est la prédiction de Hardy et Littlewood à taille finie | structure | D7, D6 | fiche 021 |

**D3 grain, pixels et précision** (7)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| moitiés | Les quatre lignes du tableau du grain sont les quatre procédés de la moitié | exact | D1 | — |
| grain | À 8 bits, les coins d'un pixel ne se voient que si le flou est plus étroit que la moitié du pixel | exact | D4 | — |
| grain | La loi des 8R devient 8⌊R + ½⌋ et 8⌊r⌋ + 4 : c'est exactement le budget de la moitié du Venn | exact | — | — |
| grain | La chèvre comptée sur une grille converge comme (points)^(−0,7), sur la grille carrée comme sur la décalée | à tester | — | — |
| grain | Une grille de W pixels ne résout que 2·log₂ W − 2,35 courbes : la même marche que Perron, à un cran près | structure | D5 | — |
| aiguilles | Perron sur une grille : « part × log₂ n » culmine à 2,83 puis baisse (2,57 à n = 65 536) | calculé | D5 | — |
| grain | La palette du Venn à 17 courbes est presque isoluminante : l'œil déplace le centre de 0,61 px, l'énergie de 46 px | structure | D8 | fiche 018 |

**D4 optique et diffraction** (4)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| moitiés | La FTM50 d'une pupille en dimension n est la médiane de |Y₁| (Y uniforme dans la boule) | exact | D3 | — |
| lumière | Tout masque de N zones égales a ses foyers par paires, I(N − u) = I(u) | exact | — | — |
| lumière | Le contraste d'une pupille circulaire défocalisée s'inverse à partir de W₂₀ = 0,6416 λ | calculé | D8 | — |
| lumière | La forme de Newton x·x′ = c revient cinq fois | exact | D1, D6 | — |

**D5 Kakeya, Perron et aiguilles** (10)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| corde | L'aiguille qui se retourne passe le bord de chaque chèvre : cos α_n = x₀, et 39,34 % = 2α₂/360° | exact | D1 | — |
| moitiés | L'arbre de Perron à 4 branches : l'aire ne dépend que du rétrécissement total P = α₀α₁ | à tester | — | — |
| aiguilles | La demi-case (déterminant ±1) est le même procédé pour l'or, l'argent, Farey, Pick et l'hexagone | structure | D2 | — |
| aiguilles | Tous les plus petits ensembles de Kakeya de F_q² (q ≤ 9) ont le même profil de multiplicités | exact | D6 | — |
| aiguilles | Kakeya lit les chiffres du grain : 1/aire gagne entre 1,057 et 1,466 par décade | démontré | D3 | — |
| méthode | Le 3-4-5 de la bande de XIII est une rotation de la grille | à tester | D2 | — |
| moitiés | Kakeya sur un corps fini : la moitié vient de l'inclusion–exclusion, l'involution ne compte que l'excès | exact | D6 | fiche 019 |
| bases | La même aiguille (q, 1) a pour norme q² + 1 sur la grille carrée et q² − q + 1 sur la grille décalée | exact | D2 | § 4.3 (vérifié) |
| aiguilles | Les N éventails de Perron, l'ombre Σωⁱ du cube et les aigrettes comptent les mêmes droites | exact | D6, D4 | K2 (deux dossiers) |
| aiguilles | L'arbre de Perron à 8 branches fait mieux que 2/(k + 2) : 43/108 | calculé | — | § 4.10 (vérifié) |

**D6 sphères, cubes, Venn et symétries** (9)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| moitiés | « Miroir + complément » arrive en tête dans 18 certificats sur 18 | ouvert | D7 | — |
| moitiés | Les quatre demi-volumes d'Archimède : trois sont 2^(−1/e), le quatrième est une cubique | exact | D1 | — |
| moitiés | L'involution z² ↔ 1 − z² échange la tranche de l'hémisphère et celle du cône conjugué | exact | — | — |
| ombres | Les périodes de Gauss du 17-gone sont les ombres Σωⁱ des régions fixées par un sous-groupe de (ℤ/17)* | exact | D2 | — |
| ombres | Le premier rang non monotone d'un Venn de Dzoba vaut 2 ou 3 de 11 à 19 courbes (au plus 2 ou 3 à 23) | calculé | D7 | — |
| ombres | La part des triangles dérive avec n : 35,95 ; 35,76 ; 35,12 % à 17, 19 et 23 courbes | à tester | D7 | — |
| ombres | Un Venn simple dont le complément est une symétrie est antipodal ; il exige C(n,2) impair, donc n ≡ 2 ou 3 (mod 4) : impossible à 17, non exclu à 19 et 23 | exact | D2 | — |
| ombres | ‖u‖₁·‖u‖∞ ≥ 1 : le seuil des 2n chèvres est la plus grande ombre du cube | exact | D1 | — |
| lumière | Les trois 34 sont un seul fait : C_N × {±1} est cyclique d'ordre 2N si et seulement si N est impair | exact | D4, D5 | K2 (deux dossiers) |

**D7 hasard et méthode** (10)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| bases | Les rapports de Lemke Oliver et Soundararajan croisent 17/24 et 2/3 à 10⁸ puis s'en vont | hasard | D2 | — |
| grain | L'image de référence a quatre variables cachées : certificat, mise en page, palette, ordre de dessin | ouvert | D3 | — |
| lumière | Le ppm d'un passage par 1 d'une famille continue est uniforme : les 845 ppm de la fiche 002 sont au rang 0,6 | calculé | D4 | — |
| ombres | Le nerf d'un recouvrement ne lit l'espace que si les intersections sont contractiles : 75 sur 81 pour les dossiers (v1), 130 sur 166 (v2) | calculé | D6 | — |
| méthode | Les tests à tolérance sont des seuils sur l'écart seul | exact | — | — |
| méthode | Le banc d'essai : six cas non triviaux, et un « 10/10 » en partie écrit en dur | calculé | — | — |
| méthode | Le prédicteur d'Adamic–Adar n'est validé que par les liens qu'il a fait chercher | calculé | — | — |
| méthode | Le nombre de « liens apparents » dépend du classement | calculé | — | — |
| corde | Le « 0,6668 » est du bruit de double précision, pas une valeur | exact | D3 | corrigé (partie XXIII) |
| lumière | Le « 93 % » de la défocalisation du Venn est le taux de base d'un prédicteur constant | calculé | D4 | § 4.11 (vérifié) |

**D8 physique** (6)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| corde | Le col de la chèvre de dimension n est g_n = √((n − 1)/(n + 1)) : un faisceau dont la distance de Rayleigh est g_n | à tester | D1 | — |
| moitiés | Au point de Rayleigh, l'aire du faisceau double et l'intensité au centre est divisée par deux | exact | D4 | — |
| lumière | Le photocentre de N sources symétriques est G·H₁(poids) ; N = 2 redonne le déplacement des étoiles doubles | structure | D3 | — |
| lumière | Deux directions au hasard sont à √2 : exact en isotrope, faux pour les plongements réels | à tester | D1 | — |
| lumière | Friedel et Bijvoet : le doublement 17 → 34 exige une ouverture réelle | à tester | D4, D6 | — |
| méthode | Intervention sur un Venn à 13 courbes : la palette déplace le centre comme G·H₁ le prévoit, l'ordre presque pas | calculé | D3, D7 | — |

