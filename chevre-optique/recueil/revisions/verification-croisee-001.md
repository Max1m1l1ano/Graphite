# Vérification croisée de la révision 001 : le recouvrement v2, les doublons et les contradictions

Le plan ([`plan-001.md`](plan-001.md), § 5) confiait cette vérification à un neuvième agent. Deux redémarrages du conteneur et une limite d'usage l'en ont empêché ; je l'ai faite moi-même. Je me suis servi des sorties structurées des agents de dossier (leurs corrections du recouvrement, leurs verdicts sur les fiches, leurs congruences, leurs erreurs trouvées et leurs fiches proposées) et de la lecture des dossiers. La synthèse est [`revision-001.md`](revision-001.md). Le nerf v2 est recalculé par [`scripts/revision_001.py`](../../scripts/revision_001.py), qui lit le bloc JSON du § 1.

*Dossiers encore en cours d'écriture : ombres, méthode. Leurs lignes seront ajoutées.*

## En bref

- **Le recouvrement v2.** Chaque agent a ajouté des parties et des fiches à son dossier ; aucun n'a rien retiré. Les huit dossiers passent de 87 à 118 appartenances de parties, et de 34 à 41 appartenances de fiches (§ 1).
- **Cinq résultats ont été trouvés deux ou trois fois, chacun par son propre calcul.** Ce sont des confirmations (§ 5.1).
- **La fiche 003 est la plus partagée du recueil** : 6 dossiers sur 8 la contiennent dans le recouvrement v2.
- **Trois désaccords entre agents, qui deviennent des précisions :** le « 2,8 » de Perron (une pente, pas une constante), la palette du Venn (mesurée ou de conception) et la fiche 005 (§ 5.2).
- **Le plan lui-même avait cinq erreurs,** trouvées par les agents et par les tests (§ 5.3).
- **50 fiches proposées**, dont 13 déjà faites par la révision (un test du script ou une des fiches 016 à 021) ; elles sont classées par dimension au § 7.

## 1. Le recouvrement v2

| dossier | parties ajoutées | fiches ajoutées | la raison principale |
|---|---|---|---|
| [corde](../dossiers/corde-et-dimensions.md) | II, X, XVII, XIX, XXVII | 003, 011 | la corde dans un polygone (II § 9), la corde de Ptolémée de 70,81° (X § 5), la récursion d'argent (XVII), le cône à sommet imaginaire (XIX § 6), le tiers de dimension (XXVII § 6) ; les fiches de K1 et K10 |
| [moitiés](../dossiers/moities-et-crans.md) | VI, X, XV, XVI, XIX, XXIII, XXV, XXVIII | 012 | la lunule d'Hippocrate (VI), la grille (XV), le plateau 2^(−1/n) (XVI § 3), le tableau du grain (XXIII § 4), Borel–Padé (XXV), Perron à k = 2 (XXVIII) ; Bonferroni (fiche 012) |
| [bases](../dossiers/bases-congruences-premiers.md) | VI, XV, XVIII, XX, XXII, XXIV | 002 | 10 − 1 = 3² (VI § 3 ter), l'aiguille (3, 1) sur la grille décalée (XV § 5), le cercle de Gauss (XVIII), le comma et 19/12 (XX § 6), 3ⁿ modulo 10 (XXII), le 4/3 de 1/x₀ (XXIV) ; le diésis (fiche 002) |
| [grain](../dossiers/grain-pixels-centres.md) | XXIV, XXV, XXVI, XXVII | 003 | le grain lu en longueur ou en aire (XXIV), la série coupée au mieux (XXV), Kakeya au grain δ (XXVI), l'échelle des taux de change (XXVII § 3) ; n·tan(π/n) (fiche 003) |
| [lumière](../dossiers/lumiere-et-physique.md) | XXI, XXIX | 003 | Self (1983) et le doublement de l'aire (XXI § 3), l'ombre Σωⁱ et son 34-gone (XXIX § 5.4) ; le polygone circonscrit (fiche 003). Corrections relevées dans son § 8 (sa sortie structurée est perdue) |
| [aiguilles](../dossiers/aiguilles-kakeya-perron.md) | VIII, XI, XV, XXI, XXIX, XXX | 009 | les trois façons de retourner l'aiguille (VIII), les trois distances (XI), la demi-case de l'hexagone (XV § 5), l'aiguille de 50 (XXI), un bit par pas (XXIX), la fiche 011 sans sa partie (XXX § 6.4) ; les aigrettes (fiche 009) |
| [ombres](../dossiers/ombres-cube-venn.md) | *(en cours)* | | |
| [méthode](../dossiers/hasard-et-methode.md) | *(en cours)* | | |

**Une précaution.** Chaque agent a estimé l'effet de ses propres corrections sur le nerf (corde : 9 → 14 triangles vides au niveau des fiches ; grain : 9 → 6 ; aiguilles : 11 → 13 ; moitiés : 20 → 17 au niveau des fiches et des parties). Ces estimations ne s'additionnent pas : chacune change un seul dossier. Le nerf v2, avec toutes les corrections ensemble, est au § 3.

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
      "parties": ["II", "XV", "XX", "XXI", "XXII", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"],
      "fiches": ["003", "004", "005", "006", "008", "009", "010", "015"]
    },
    "hasard-et-methode": {
      "parties": ["III", "VI", "XIII", "XVIII", "XXIV", "XXVII", "XXIX", "XXX"],
      "fiches": ["002", "003", "004", "005", "007", "012", "015"]
    }
  }
}
```

## 2. Les congruences, vues par plusieurs dossiers

Une congruence est vérifiée quand deux sections locales se recollent sur ce qu'elles partagent (revision-001.md, § 6). Ici, on regarde si les dossiers qui l'ont traitée sont d'accord.

| | dossiers et tests | ce qu'ils trouvent | accord |
|---|---|---|---|
| K1 | corde ; T3 | se recolle aux ordres 2 et 3 avec le décalage n → n + 49/10 ; obstruction à l'ordre 4 | accord. Le plan disait « dès l'ordre 3 », vrai seulement sans décalage |
| K2 | lumière, aiguilles, moitiés | les trois 34 (aigrettes, ombre Σωⁱ, éventails) sont un seul fait pour N impair ; calculé pour N = 3 à 20 par deux agents (A) | accord à trois. Moitiés ajoute l'obstruction en Kakeya fini (en caractéristique 2, x ↦ −x est l'identité) ; lumière ajoute la réserve de la phase (une ouverture complexe casse la symétrie de Friedel) |
| K3 | bases ; § 4.3 | se recolle par la famille q² + 1 et le lemme des chiffres, démontré pour tout q ≥ 2 | accord |
| K4 | moitiés, aiguilles ; T5 | obstruction : deux procédés, Bonferroni pour Kakeya fini et l'involution pour les hémisphères | accord à trois. La piste XIV–XX se ferme |
| K5 | bases | obstruction établie par la théorie : aucune transformation connue entre le 17 de Henderson et le 17 de i | — |
| K6 | grain, lumière ; T4 | le centre de la lumière suit la palette ; la seconde cause est le seuil, pas l'ordre de dessin | **désaccord partiel** (§ 5.2) |
| K7 | moitiés, grain, aiguilles | se recolle pour la pente : un cran, soit un facteur 2 sur l'exposant | accord sur la pente. Deux obstructions nouvelles : le « 2,8 » n'est pas une constante (aiguilles) ; l'aire ½ de Perron à 4 branches n'est pas un effet de cran (moitiés). La cause commune du logarithme reste ouverte (grain) |
| K8 | corde, bases ; T7 | une coïncidence de petits entiers | accord. Bases : ce qui se recolle passe par log₂ 3 et le comma |
| K9 | bases ; T6 | se recolle en une tour 2-adique, à aires inégales | accord. Bases ajoute l'enchevêtrement fixé par la réciprocité quadratique (A) |
| K10 | corde, grain ; § 4.4 | exact : c'est l'isopérimétrie | accord, avec une précision du dossier grain : le seuil vaut 4π·(s/a)² pour des croisements espacés de a et des régions de côté s. Le 13 vient du choix a = s = 2 px (§ 5.2) |

**Les congruences nouvelles des agents** (la plus forte de chaque dossier ; chacun a sa table au § 5) :
- *Corde.* Le triangle de Thalès de la partie XXIV (§ 5) est le triangle du simplexe de la classification : (PQ, QP′) = (c_K, d_K), avec K − 1 = 1/x₀ (exact). Et la part de la clôture broutée vaut 2α_n/360°, avec cos α_n = x₀ : 39,34 % en est le cas n = 2.
- *Moitiés.* Le cercle R/√2 est fixé par trois gestes (le miroir d'aire, l'inversion des jumeaux, la dilatation d'un cran), en toute dimension (exact). Les écarts à la moitié sont des miroirs : ½ − 1/√(2πn) sur la clôture, ½ + 1/√(2πn) sur le volume (calculé).
- *Bases.* Le dernier chiffre d'un premier dit si le nombre d'or existe modulo p ; le cocycle se ferme sur 3, 9, 7 (démontré).
- *Grain.* La loi des 8R de la partie XVIII et le budget de la moitié du Venn de la partie XXX se recollent exactement (8⌊R + ½⌋ et 8⌊r⌋ + 4).
- *Aiguilles.* i ≡ a/c (mod b) de la partie XIX et l'aiguille primitive (a, c) de norme b = a² + c² de la partie XIV se recollent entièrement. Les coupes de Perron et les niveaux du Venn se recollent sur le cube {0, 1}ⁿ, avec une obstruction : binaire contre binomial.
- *Lumière.* Tout masque de N zones égales a ses foyers par paires, I(N − u) = I(u) (vérifié sur 2 000 masques) : la symétrie de la partie VIII ne vient pas de Fibonacci.

## 3. Les triangles vides : v1 contre v2

Résultats : [`resultats/revision_001.md`](../../resultats/revision_001.md), § 3. Mêmes trois niveaux que pour v1 : (1) les fiches ; (2) les fiches sans les deux hasards testés 002 et 004 ; (3) les fiches et les parties.

| recouvrement | niveau | sommets, arêtes, triangles, tétraèdres | Betti b₀, b₁, b₂ | triangles vides | triangles remplis : éléments communs en moyenne | nul : b₁ moyen | nul : b₂ moyen | nul : triangles vides en moyenne | p (nul ≥ observé) |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| v1 | brute | 65 | 1,3162 | 40 | 1,6427 | 5 % | 0,3264 | 0,928 |
| v1 | aires égales | 65 | 1,3224 | 40 | 1,5645 | 10 % | 0,2421 | 0,966 |
| v1 | 1 | 8, 18, 7, 1 | 1, 5, 0 | 9 | 1,1 | 3,08 | 0,00 | 5,7 | 0,162 |
| v1 | 2 | 8, 17, 7, 1 | 1, 4, 0 | 7 | 1,1 | 2,66 | 0,00 | 4,8 | 0,238 |
| v1 | 3 | 8, 28, 36, 11 | 1, 0, 5 | 20 | 1,5 | 0,21 | 5,59 | 18,6 | 0,387 |
| v2 | 1 | 8, 24, 26, 16 | 1, 2, 0 | 10 | 1,2 | 1,77 | 0,10 | 10,2 | 0,528 |
| v2 | 2 | 8, 23, 25, 16 | 1, 2, 0 | 7 | 1,2 | 1,85 | 0,05 | 9,3 | 0,712 |
| v2 | 3 | 8, 28, 55, 55 | 1, 0, 1 | 1 | 4,1 | 0,00 | 0,17 | 0,5 | 0,372 |

**v2 : les triangles vides au niveau des fiches** (10) :
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
- Bilan v2 : 10 trous du recueil, 0 trous du corpus.
- Les fiches laissent 10 triangles vides, contre 10,2 en moyenne pour des dossiers de mêmes tailles tirés au hasard (p = 0,53) : un peu plus que le hasard, sans plus. Les trous se lisent donc un par un, comme des pistes, pas comme une preuve.
- **Avec les parties (niveau 3), les boucles se remplissent** (b₁ = 0), mais il reste b₂ = 1 cavités (nul : 0,17 en moyenne, p = 0,156). Une cavité, ce sont quatre dossiers dont les quatre triplets se recollent, sans élément commun aux quatre : un trou d'un étage plus haut. Les 10 tétraèdres creux :
  - aiguilles-kakeya-perron · bases-congruences-premiers · grain-pixels-centres · lumiere-et-physique
  - bases-congruences-premiers · corde-et-dimensions · grain-pixels-centres · lumiere-et-physique
  - bases-congruences-premiers · corde-et-dimensions · hasard-et-methode · lumiere-et-physique
  - bases-congruences-premiers · corde-et-dimensions · hasard-et-methode · ombres-cube-venn
  - bases-congruences-premiers · grain-pixels-centres · hasard-et-methode · ombres-cube-venn
  - bases-congruences-premiers · grain-pixels-centres · lumiere-et-physique · moities-et-crans
  - bases-congruences-premiers · grain-pixels-centres · lumiere-et-physique · ombres-cube-venn
  - bases-congruences-premiers · hasard-et-methode · lumiere-et-physique · moities-et-crans
  - bases-congruences-premiers · hasard-et-methode · lumiere-et-physique · ombres-cube-venn
  - corde-et-dimensions · hasard-et-methode · lumiere-et-physique · moities-et-crans


## 4. Les arbres corrigés

Figure : [`rev001_perron_venn.png`](../../figures/rev001_perron_venn.png), panneau b. Le tableau complet est au § 5 de la synthèse ; ici, ce qui change, et qui le dit.

| arbre | disque | ce qui change | dossiers et tests |
|---|---|---|---|
| P1 l'ombre du cube {0, 1}ⁿ | D6 | une branche de la parité : les trois 34 (K2) | lumière, aiguilles, moitiés |
| P2 la moitié | D1 | un seul cercle R/√2, fixé par trois gestes ; la branche « Kakeya fini » se détache (Bonferroni) | moitiés ; T5 |
| P3 le terme x²/6 | D1 | même 1/6, obstruction à l'ordre 4 ; le « dernier 2 » du ménisque compte les dérangements de 3 | corde ; T3 ; § 4.10 |
| P4 le quart de tour i modulo b | D2 | la famille q² + 1, le lemme des chiffres, Φ₆(10) = 7 × 13, le dernier chiffre et le nombre d'or | bases ; § 4.3 et 4.10 |
| P5 le budget en bits | D3 | le seuil isopérimétrique, la loi des 8R ; K7 tient pour la pente seulement | grain, aiguilles ; § 4.4 |
| P6 les réduites et les trois distances | D2 | le diésis et le comma, deux écarts du même théorème ; la demi-case (Pick) pour l'or, l'argent, Farey et l'hexagone | bases, aiguilles |
| P7 la loi de l'écart | D7 | sa réserve : une dérive peut croiser une constante (π, 2√2) | § 4.2 et 4.9 |
| P8 le cône à sommet imaginaire | D8 | la branche « photocentre » se détache : il n'a ni col ni distance de Rayleigh ; la forme de Newton x·x′ = c revient cinq fois | lumière |
| **P9 (nouveau)** le barycentre pesé | D8, contre D3 et D7 | le centre de la lumière est le premier harmonique des poids, G·H₁ ; le seuil en est un second canal | lumière, grain ; T4 ; fiche 018 |

## 5. Les doublons et les contradictions

### 5.1 Trouvé deux fois : des confirmations

- **La fiche 010.** Corde et moitiés, chacun par son calcul, trouvent que 39,34 % n'est exact que pour le cercle du bord : la part monte quand on rentre (39,57 % pour l'anneau de rayon 0,99 ; 39,52 % au niveau 4 du dessin à aire égale). La fiche est corrigée.
- **K2, les trois 34.** Lumière et aiguilles l'ont calculé chacun pour N = 3 à 20 ; moitiés l'a relié à x ↦ −x.
- **K4, la moitié de Kakeya fini.** Moitiés, aiguilles et le test T5 concluent tous trois à deux procédés.
- **Le minimum 2/(k + 2).** Moitiés (pour k = 2, l'aire vaut ½ sur tout un segment de rapports) et aiguilles (pour k = 3, 43/108 < 2/5, vérifié au § 4.10) trouvent chacun que c'est le minimum de la borne, pas celui de l'aire. La partie V l'avait vu en nombres (0,3981). CLAUDE.md et la partie XXVIII sont précisés.
- **La palette comme cause du centre de la lumière.** Grain et lumière l'ont trouvée tous deux ; ils ne s'accordent pas sur les détails (§ 5.2).

### 5.2 Les désaccords entre agents

1. **K7 : le « 2,8 » de Perron sur une grille.** Le dossier grain tient l'analogie pour « confirmée » avec cette valeur. Le dossier aiguilles la calcule plus loin : « part × log₂ n » culmine à 2,83 (n = 256), puis baisse à 2,57 (n = 65 536). Les deux ont raison sur la pente ; la valeur n'est pas une constante. Verdict : se recolle pour la pente, pas pour les valeurs.
2. **K6 : quelle palette ?** Les deux dossiers disent que les couleurs mesurées (les 5 % de pixels les plus clairs de chaque teinte) ne suffisent pas : avec elles, les directions relatives des écarts ratent de 55° (luminance) et 47° (clarté) (lumière, (A)).
   - Le dossier grain ajuste une palette de conception presque isoluminante (Y₀ = 0,30 à 0,36) et un facteur G de 181 à 194 px. Il retrouve les quatre pesées continues à 1,4 – 2,0 px près, et leurs phases à 6° près ; il conclut « obstruction levée sous condition ».
   - Mais il note lui-même deux restes : le bras de levier mesuré vaut 379 px, deux fois le G ajusté ; et les masques du modèle vont de 1 à 17 px quand les mesures vont de 0,4 à 27 px, avec des directions décalées de 10° à 40°.
   - Le dossier lumière garde le statut « structure, à tester » : le rapport des pesées Y/E vaut 0,0132, entre 0,003 (palette isoluminante) et 0,23 (couleurs mesurées).
   - Mon verdict : l'obstruction est levée en partie, avec deux paramètres ajustés. Ce qui la lèverait tout à fait, c'est un rendu de contrôle à palette connue ; le code de rendu de l'image n'est pas publié. Le test T4 a ajouté un second canal, le seuil (fiche 018), qui explique une part des masques.
3. **La fiche 005.** Moitiés trouve « miroir + complément » en tête dans les 18 certificats, à 1,5 à 2,3 fois le hasard, et conclut « hasard testé, cause ouverte » (A). Bases la juge « compatible avec le hasard ». Le calcul de moitiés (son § 7.3) est à refaire avant de trancher.
4. **Pas un désaccord : la fiche 014.** Corde y voit un lien faible, par les nombres (√2, 2/√3, √(3/2)) ; bases, un lien exact avec F₉. Ils parlent de deux parties de la fiche.
5. **Une précision de K10.** Le seuil vaut n* = 4π·(s/a)², pour des croisements espacés de a et des régions de côté s. Avec a = s = 2 px (le choix de la partie XXX), on trouve 4π et 13 courbes ; avec a/s = 1,5, le seuil tombe à 5,6 courbes ; avec a/s = 0,5, il monte à 50,3. L'isopérimétrie est la loi ; le 13 est le cadre. C'est exactement ton sujet d'étude : la restriction du cadre fixe le nombre qu'on observe.

### 5.3 Les erreurs du plan

- *K1* : « obstruction dès l'ordre 3 ». Vrai sans décalage ; avec le décalage s = 49/10, l'ordre 3 se recolle et l'obstruction est à l'ordre 4 (corde, refait par T3).
- *K6* : la seconde cause proposée, l'ordre de dessin, est écartée deux fois (T4 : p = 0,64 ; grain : contraste d'ordre −6,0 %, comme les témoins). La seconde cause est le seuil.
- *K7* : le « 2,8 » pris pour une constante (aiguilles).
- *K10* : le polygone inscrit du plan donne n* = 12,295 ; le n-gone de même aire du script, 12,824 ; le cercle, 12,566. Les trois donnent 13 courbes (grain).
- *La liste de lecture de l'agent corde* oubliait six fichiers, dont carte-connexions.md et archimede.md (corde).

## 6. Les trous dans les données publiées

La synthèse en fait le tableau (revision-001.md, § 9), et chaque dossier a le sien (§ 6.3). La vérification croisée ajoute ceci : **trois trous sont désignés par deux dossiers à la fois**, ce qui les rend plus sûrs.
- *La chaîne de rendu des images de Venn* (grain, lumière) : la palette, l'espace de mélange, l'anticrénelage et l'ordre de dessin des PNG à 17 courbes ne sont pas publiés. C'est aussi ce qui bloque K6.
- *Le déplacement induit par la couleur* (lumière, grain) : pour N sources colorées en symétrie d'ordre N, le centre dépend du poids et du seuil. À répliquer sur les binaires « CID » de SDSS (Pourbaix et al., 2004) : à calculer.
- *Les constantes de Perron et de Kakeya au grain fini* (aiguilles, moitiés, grain) : pas de table publiée des rapports optimaux, ni de la constante entre π/2 et π·ln 2.

**Les références à vérifier**, relevées par plusieurs dossiers : le titre de Wielen (1996) ; le nom de la revue de Fraser en 1984 ; les deux articles « Córdoba (1977) » ; le Nikon D800E ; la référence exacte des corrections de chromaticité de Gaia.

## 7. Les nouvelles fiches, classées par dimension

Chaque dossier propose ses fiches au § 6.1, avec leur type, leur statut, leur script et leur image. Elles ne sont pas écrites dans le recueil : on les écrira quand une partie les reprendra (revision-001.md, § 10). La colonne « puis » donne les dimensions voisines ; « déjà fait » renvoie au test ou à la fiche de la révision qui la recouvre.

50 fiches proposées par 6 dossiers.

| dimension | fiches | dont déjà faites |
|---|---:|---:|
| D1 la chèvre et les cordes | 7 | 1 |
| D2 bases, chiffres et congruences | 9 | 4 |
| D3 grain, pixels et précision | 7 | 1 |
| D4 optique et diffraction | 4 | 0 |
| D5 Kakeya, Perron et aiguilles | 9 | 4 |
| D6 sphères, cubes, Venn et symétries | 4 | 1 |
| D7 hasard et méthode | 5 | 2 |
| D8 physique | 5 | 0 |

**D1 la chèvre et les cordes** (7)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| corde | La chèvre plane est contenue dans la série de la chèvre infinie | structure | — | — |
| corde | Les seuils entiers de IV § 4 ne tiennent pas en dimension réelle | hasard | D7 | — |
| corde | δ₂ ≈ δ₃ à 10⁻⁵ : une proximité nommée trois fois, jamais expliquée | ouvert | D7 | — |
| corde | Les polygones circonscrits à 4 et à 8 côtés ont la même corde (1,165644) | exact | D6 | — |
| moitiés | La corde de la moitié du carré ne change pas quand on coupe ses quatre coins, jusqu'à t = 0,5989 | exact | — | — |
| moitiés | Les écarts à la moitié sont des miroirs : ½ − 1/√(2πn) sur la clôture, ½ + 1/√(2πn) sur le volume | structure | — | — |
| corde | Le « −2 » de la coquille est le nombre de dérangements de 3 : E[(1 − E)^j] = (−1)^j·!j | exact | D7 | § 4.10 (vérifié) |

**D2 bases, chiffres et congruences** (9)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| corde | Les facteurs 2 des polynômes de la chèvre comptent les retenues de la base 2 (Kummer) | exact | D1 | — |
| bases | Midy est un demi-tour, et 10^(L/4) est un i : la tour du 17-gone | exact | D6 | — |
| bases | Le diésis et le comma sont le troisième écart du théorème des trois distances | exact | D5 | — |
| bases | Le dernier chiffre d'un premier dit si le nombre d'or existe modulo p ; la course de Tchebychev | exact pour le lien | D7 | — |
| bases | La famille de Pell des bases à deux écritures : le 7 de Hutton et le 239 de Machin sont des i | exact | D5 | — |
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

**D5 Kakeya, Perron et aiguilles** (9)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| corde | L'aiguille qui se retourne passe le bord de chaque chèvre : cos α_n = x₀, et 39,34 % = 2α₂/360° | exact | D1 | — |
| moitiés | L'arbre de Perron à 4 branches : l'aire ne dépend que du rétrécissement total P = α₀α₁ | à tester | — | — |
| aiguilles | La demi-case (déterminant ±1) est le même procédé pour l'or, l'argent, Farey, Pick et l'hexagone | structure | D2 | — |
| aiguilles | Tous les plus petits ensembles de Kakeya de F_q² (q ≤ 9) ont le même profil de multiplicités | exact | D6 | — |
| aiguilles | Kakeya lit les chiffres du grain : 1/aire gagne entre 1,057 et 1,466 par décade | démontré | D3 | — |
| moitiés | Kakeya sur un corps fini : la moitié vient de l'inclusion–exclusion, l'involution ne compte que l'excès | exact | D6 | fiche 019 |
| bases | La même aiguille (q, 1) a pour norme q² + 1 sur la grille carrée et q² − q + 1 sur la grille décalée | exact | D2 | § 4.3 (vérifié) |
| aiguilles | Les N éventails de Perron, l'ombre Σωⁱ du cube et les aigrettes comptent les mêmes droites | exact | D6, D4 | K2 (deux dossiers) |
| aiguilles | L'arbre de Perron à 8 branches fait mieux que 2/(k + 2) : 43/108 | calculé | — | § 4.10 (vérifié) |

**D6 sphères, cubes, Venn et symétries** (4)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| moitiés | « Miroir + complément » arrive en tête dans 18 certificats sur 18 | ouvert | D7 | — |
| moitiés | Les quatre demi-volumes d'Archimède : trois sont 2^(−1/e), le quatrième est une cubique | exact | D1 | — |
| moitiés | L'involution z² ↔ 1 − z² échange la tranche de l'hémisphère et celle du cône conjugué | exact | — | — |
| lumière | Les trois 34 sont un seul fait : C_N × {±1} est cyclique d'ordre 2N si et seulement si N est impair | exact | D4, D5 | K2 (deux dossiers) |

**D7 hasard et méthode** (5)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| bases | Les rapports de Lemke Oliver et Soundararajan croisent 17/24 et 2/3 à 10⁸ puis s'en vont | hasard | D2 | — |
| grain | L'image de référence a quatre variables cachées : certificat, mise en page, palette, ordre de dessin | ouvert | D3 | — |
| lumière | Le ppm d'un passage par 1 d'une famille continue est uniforme : les 845 ppm de la fiche 002 sont au rang 0,6 | calculé | D4 | — |
| corde | Le « 0,6668 » est du bruit de double précision, pas une valeur | exact | D3 | corrigé (partie XXIII) |
| lumière | Le « 93 % » de la défocalisation du Venn est le taux de base d'un prédicteur constant | calculé | D4 | § 4.11 (vérifié) |

**D8 physique** (5)

| dossier | titre | statut | puis | déjà fait |
|---|---|---|---|---|
| corde | Le col de la chèvre de dimension n est g_n = √((n − 1)/(n + 1)) : un faisceau dont la distance de Rayleigh est g_n | à tester | D1 | — |
| moitiés | Au point de Rayleigh, l'aire du faisceau double et l'intensité au centre est divisée par deux | exact | D4 | — |
| lumière | Le photocentre de N sources symétriques est G·H₁(poids) ; N = 2 redonne le déplacement des étoiles doubles | structure | D3 | — |
| lumière | Deux directions au hasard sont à √2 : exact en isotrope, faux pour les plongements réels | à tester | D1 | — |
| lumière | Friedel et Bijvoet : le doublement 17 → 34 exige une ouverture réelle | à tester | D4, D6 | — |

