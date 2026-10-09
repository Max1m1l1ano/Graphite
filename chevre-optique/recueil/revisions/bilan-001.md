# Bilan de la révision 001 : ce qu'elle a rapporté, ce qu'elle a coûté, et la forme à lui donner

> « Ok, avant ça, on va regarder si l'exercice de synthèse et de compilation c'est bien déroulé et donne des commentaires sur ce qui est rapporté, les connexions entre les sujets, regarde les hasards, coïncidences, etc... et fait des commentaires sur le workflow, les agents pour qu'on puisse déterminer une forme concrète à cet exercice et l'améliorer pour les agents sonnet, opus, toi la quantité de données et l'organisation des données et aussi établir une liste des problématiques ainsi qu'une liste de liste de tâches pour toi, qui travaille directement avec moi, l'utilisateur. »
>
> (ton message du 9 octobre 2026, après la révision 001)

Les mesures viennent des transcriptions des agents (lues par [`outils-001/stats_agents.py`](outils-001/stats_agents.py)), de la taille des fichiers du dépôt et des sorties structurées des agents ([`sorties-agents-001.json`](sorties-agents-001.json)). Les résultats cités sont ceux de [`resultats/revision_001.md`](../../resultats/revision_001.md). Les outils de la révision sont archivés dans [`outils-001/`](outils-001/). Ce bilan ajoute deux fiches au recueil, [022](../observations/022-quatre-derives-croisent-une-constante.md) et [023](../observations/023-quatre-liens-vrais-par-construction.md).

## En bref

- **L'exercice a marché, mais il coûte cher et il est fragile** (§ 1 et 2).
  - Il a produit 8 dossiers, 12 corrections du corpus, 26 erreurs signalées, 12 tests nouveaux, 8 fiches et une intervention qui établit une cause.
  - Il a demandé 15 h d'agents, 49 h de calendrier (dont 40 h d'attente) et 1,4 Mo de texte, 1,7 fois le corpus qu'il révise.
- **Ce qui vaut le plus, ce sont les corrections et les tests** (§ 3).
  - Les résultats neufs portent sur la chaîne de production du corpus : le seuil, la palette, le banc d'essai, le « 93 % ». C'est ton sujet d'étude, la restriction du cadre.
  - Les connexions sont surtout des classiques retrouvés, et quatre sont vraies par construction (fiche 023).
- **Les connexions solides passent par un procédé commun** (§ 4) : le barycentre pesé, le premier 3, le i modulo n.
  - Le dossier bases paraît isolé dans le nerf. Pourtant, son meilleur lien le relie exactement aux aiguilles : 10 et 7 sont les carrés de la même aiguille (3, 1), sur la grille carrée et sur la grille hexagonale.
  - Le nerf ne voit que les fiches partagées, pas les liens écrits.
- **Deux familles de hasards, deux questions** (§ 5) :
  - les dérives qui croisent une constante (fiche 022) : « et au N suivant ? » ;
  - les liens vrais par construction (fiche 023) : « aurait-il pu être faux ? ».
- **Le recueil se regarde lui-même** (§ 5).
  - Les fiches de méthode (D7) passent à 30 %, parce que la révision et ce bilan parlent de méthode.
  - La diagonale √2 plafonne à 6,9 % avec 8 dimensions : il faudra les diviser.
- **Les agents et les données** (§ 6 et 7).
  - Le plan Opus est trop long et n'a pas de budgets.
  - Les dossiers concis rendent autant que les longs, en deux fois moins de temps.
  - La mémoire est le point faible.
  - Les mêmes nombres sont recopiés dans 11 ou 12 fichiers. Je propose un registre des résultats.
- **La suite** : une forme en huit étapes avec des budgets (§ 8), onze problématiques (§ 9), mes listes de tâches et sept questions pour toi (§ 10).

## 1. Ce que la révision a coûté, et ce qu'elle a produit

**Le coût.** Le contexte cumulé additionne, appel après appel, le contexte que l'agent relit (surtout depuis le cache). Il mesure la longueur du travail plus qu'un prix.

| étape | agent | durée | appels d'outils | contexte cumulé |
|---|---|---:|---:|---:|
| le plan | Opus | 71 min | 101 | 36 M |
| 4 dossiers longs (corde, moitiés, bases, grain) | Sonnet | 110 à 143 min chacun | 1 372 | 483 M |
| 4 dossiers concis (lumière, aiguilles, ombres, méthode) | Sonnet | 56 à 74 min chacun | 760 | 244 M |
| perdus (2 redémarrages, 1 reprise ratée) | Opus, Sonnet | 55 min | 280 | 67 M |
| la fin d'arc 001 | Sonnet | 29 min | 94 | 26 M |
| **total des agents** | | **906 min ≈ 15 h** | **2 607** | **856 M** |
| la session principale (moi) | | | 477, dont 420 Bash | une compaction |

**Le calendrier.** La révision a duré 49 h, du 7 octobre à 18 h 39 au 9 octobre à 20 h 06 (UTC). Elle a attendu 40 h : la limite d'usage hebdomadaire (du 8 à 1 h 36 au 9 à 6 h), puis ton « Réessayer ».

**Ce qu'elle a écrit.**

| couche | fichiers | taille |
|---|---|---:|
| le plan | `plan-001.md` | 150 Ko |
| les dossiers | 8 | 670 Ko |
| les sorties structurées | `sorties-agents-001.json` | 248 Ko |
| la vérification croisée | 1 | 39 Ko |
| la synthèse | `revision-001.md` | 57 Ko |
| les tests | `scripts/revision_001.py` et ses résultats | 146 Ko, plus 0,75 Mo de figures |
| la fin d'arc | `arc-001.md` et `.csv` | 75 Ko |
| **total (texte)** | | **1,38 Mo** |
| pour comparer : le corpus | 29 documents, README et CLAUDE.md | 0,83 Mo |

**Le rendement des dossiers** (d'après leurs sorties structurées ; celle de lumière est perdue).

| dossier | taille | durée | erreurs trouvées | fiches proposées | congruences | références (dont à vérifier) |
|---|---:|---:|---:|---:|---:|---:|
| corde | 95 Ko | 110 min | 8 | 9 | 11 | 31 (9) |
| moitiés | 105 Ko | 116 min | 5 | 10 | 13 | 26 (8) |
| bases | 144 Ko | 143 min | 3 | 10 | 13 | 21 (10) |
| grain | 146 Ko | 132 min | 7 | 6 | 9 | 32 (8) |
| lumière | 47 Ko | 56 min | — | 9 | — | — |
| aiguilles | 40 Ko | 57 min | 6 | 6 | 7 | 23 (4) |
| ombres | 46 Ko | 74 min | 9 | 7 | 8 | 16 (7) |
| méthode | 46 Ko | 64 min | 7 | 7 | 11 | 28 (10) |

**Ce que le tableau dit.**
- Les dossiers concis trouvent 6,8 erreurs par heure, contre 2,8 pour les longs. Par 100 Ko de texte, c'est 17 contre 5. La longueur n'achète donc pas le rendement.
- *Prudence* : la comparaison mêle trois effets, le gabarit, le sujet et l'ordre. Les dossiers concis venaient après, et méthode lisait les dossiers déjà écrits.

**Le compte des erreurs.** Les sorties structurées en rapportent 45, et lumière en a signalé d'autres dans son dossier. La synthèse en retient 38 : 12 corrigées et 26 signalées. L'écart vient des doublons entre dossiers et des erreurs que je n'ai pas retenues. Je n'en ai pas gardé le compte détaillé, et c'est une des choses que le registre (§ 7) doit tracer.

## 2. Étape par étape : ce qui a marché, ce qui a cassé

1. **Le plan (Opus).**
   - *Ce qui a marché.* Il a fait 8 dossiers qui couvrent les 30 parties, leur recouvrement en JSON, 10 congruences, 8 tests et les consignes des agents.
   - *Ce qui n'a pas marché.* Il fait 150 Ko, trois fois la plus longue des parties. Il contient sept erreurs, trouvées ensuite (vérification croisée, § 5.3), et ne fixe aucun budget aux agents.
   - *Un recouvrement trop étroit.* Les agents y ont ajouté 45 % d'appartenances (de 87 à 126), et les 4 trous du corpus du nerf v1 se sont refermés. *Ma lecture* : c'étaient des trous de la lecture du plan, pas du corpus.
2. **Le workflow (Sonnet).** Les 8 dossiers sont écrits, mais en trois lancements et une reprise ratée, sur deux jours.
   - Un redémarrage du conteneur a arrêté le premier plan Opus après 3 min.
   - Un second redémarrage, la nuit, a arrêté lumière et aiguilles après 26 et 20 min. Les quatre dossiers déjà écrits n'ont été commités qu'après lui (commit 2792d42).
   - Ma reprise avait modifié le texte de tous les prompts. Le cache ne servait plus, et les dossiers déjà écrits repartaient de zéro. Je l'ai arrêtée au bout de 3 min, avant qu'elle écrase quoi que ce soit.
   - La limite d'usage hebdomadaire a coupé lumière juste avant sa sortie structurée, et bloqué ombres et méthode pendant 40 h.
   - Au total, 55 min d'agents perdues (6 %). Le vrai coût, c'est la sortie perdue et l'attente. Le neuvième agent, celui de la vérification croisée, n'a jamais tourné.
3. **Les tests (moi).** C'est la partie la plus solide : `scripts/revision_001.py` refait tout en 4 min, avec des assertions.
   - Le test de reproductibilité a trouvé une faiblesse : le nul du nerf dépendait de l'ordre d'un ensemble de chaînes, qui change à chaque exécution. Trier les éléments l'a corrigé.
   - Le code de l'intervention de l'agent méthode n'était que dans le dossier temporaire. Je l'ai réécrit (§ 4.12) et j'ai retrouvé ses nombres.
4. **La vérification croisée (moi).**
   - Elle a été faite par un générateur, maintenant archivé (`outils-001/croisee.py`).
   - Elle a trouvé 6 confirmations, 3 désaccords et les 7 erreurs du plan.
   - La moitié de ce travail est mécanique (le v2, les doublons, le classement des fiches) : un script peut la faire.
5. **La synthèse (moi).** Elle est complète, avec une étiquette par énoncé : 29 « (A) », 27 « vérifié », 16 « à vérifier ». Mais elle fait 57 Ko, elle répète les dossiers, et j'y ai fait cinq excès, corrigés depuis :
   - « la diagonale démontrée » est devenu « mise en équation » ;
   - « Midy est un arbre de Perron » est devenu « la forme binaire, pas la loi » ;
   - « chaque test fait varier un paramètre » est devenu « presque chaque » ;
   - le manque de 24 % de la palette tournée, que j'expliquais, est « pas expliqué » ;
   - « aucun agent n'a rien retiré » était faux : ombres a retiré la fiche 010.

   Ce sont des erreurs de la classe que la révision chasse dans le corpus : une lecture qui devient un fait.
6. **Les fiches.** Elles sont bonnes, et `maj_fiches.py` a marqué les 15 premières. Mais il a fallu traduire à la main la voix des agents (« ajoutée par moi »).
7. **La fin d'arc (Sonnet).**
   - *Utile* : l'agent a relevé trois « ouverts » de la partie XXX oubliés par la synthèse.
   - *Lourde pour un seul arc* : 29 min, 94 appels, 49 Ko et 141 lignes de CSV, qui se déduisent de git.

## 3. Ce que la révision rapporte, en cinq classes

**A. Nouveau et vérifié : le cœur.**
- Un seuil ne déplace le centre que si la grandeur seuillée varie d'une courbe à l'autre (fiche 018).
- Le photocentre G·H₁ des poids prédit le déplacement sans paramètre libre : 2,08 px prédits, 2,05 à 2,20 observés sur le Venn à 13 courbes repeint (§ 4.12).
- Le « 93 % » de la partie XXX est le taux de base : 71 rayons sur 76, contre 70 pour un prédicteur constant.
- Le banc d'essai de la partie XXX est en partie construit : trois verdicts y sont écrits à la main.
- L'aire 43/108 de l'arbre de Perron optimal à 8 branches : la partie V l'avait en nombres, la révision en donne les fractions.
- La loi 4π·(s/a)² du seuil des 13 courbes.
- Les 12 corrections du corpus.

Presque tous parlent de la chaîne de production (images, seuils, tests) : le cadre fixe le nombre qu'on observe.

**B. Des classiques retrouvés.**
- Bonferroni (fiche 019) et le minimum de Kakeya fini (Blokhuis et Mazzocca, à vérifier).
- Hardy–Littlewood (fiche 021) et l'isopérimétrie (fiche 020).
- Les fausses corrélations de Pearson et les doubles zéros (fiche 017).
- Le théorème du nerf, la tour 2-adique de Midy, et le photocentre des étoiles doubles.

Un lien vers un théorème connu est un résultat (CLAUDE.md, § 1) : il dit où lire la suite. C'est aussi un contrôle, puisqu'un agent qui retrouve un classique n'invente pas.

**C. Vrai par construction (fiche 023).** La corde de la chèvre comme corde du simplexe, les périodes de Gauss comme ombres, les identités du banc d'essai, et T2. Ce sont des dictionnaires : utiles s'ils transportent un calcul.

**D. Des effets de cadre, mesurés.**
- De 0 à 21 faux liens selon le classement des fiches.
- Les trous du nerf v1, qui venaient de la lecture du plan.
- La fiche 003 dans 6 dossiers sur 8 : π et les polygones servent partout, et une fiche générique devient un carrefour sans être plus importante.
- Le 13 du seuil, qui vient du choix de 2 px.
- La dérive du recueil vers D7 (§ 5).

**E. Ouvert et prometteur.**
- **L'obstruction de parité** (dossier ombres, (A)).
  - *Ce qu'elle dit.* Un Venn simple « antipodal » serait muni d'une involution sans point fixe, qui garde chaque courbe, en échange les côtés et envoie chaque région sur son complément. Il exige que C(n, 2) soit impair, donc n ≡ 2 ou 3 (mod 4). Il est exclu à 5, 13 et 17 courbes, et permis à 7, 11, 19 et 23.
  - *Ma relecture.* Le quotient est un plan projectif. Deux courbes unilatères s'y coupent un nombre impair de fois, et il a 2ⁿ⁻¹ − 1 croisements, un nombre impair. L'argument tient ; seule l'étape « on peut prendre l'involution » reste à justifier.
  - *Le cas de 3 courbes.* Il existe : ce sont les trois grands cercles des plans de coordonnées, c'est-à-dire l'octaèdre de la partie XXVIII projeté sur la sphère. L'antipode envoie chaque octant sur l'octant opposé, son complément.
  - *La littérature* (lue dans des résumés de recherche, le réseau de la session bloquant les articles : à vérifier).
    - La « symétrie polaire » de Ruskey et de ses coauteurs est voisine : le diagramme retourné comme un gant redonne le même diagramme. Mais elle se fait par un demi-tour, qui peut échanger les courbes et a deux points fixes. C'est le candidat « miroir + complément » du dossier, que la parité n'exclut pas.
    - Il existe des Venn polaires à 3, 5 et 7 courbes, et aucun ne serait connu à 11 (Mamakani et Ruskey, 2012).
    - Le cas antipodal, plus fort, ne semble pas étudié. C'est une piste, pas encore une découverte.
- **δ₂ ≈ δ₃** (1,7·10⁻⁴ pour une racine au hasard) : ouvert.
- **Le manque de 24 % de la palette tournée** : pas expliqué.
- **K7, la cause commune du logarithme** : ouverte.
- **La cavité du nerf v2** (b₂ = 1, p = 0,047), à prendre avec prudence. Sur une vingtaine de tests indépendants, un p aussi petit arrive au moins une fois six fois sur dix par le seul hasard (1 − 0,953²⁰ = 0,62). Il faut la refaire avec un classement fixé d'avance.

## 4. Les connexions entre les sujets

Une connexion compte quand on peut dire ce qui est partagé exactement, ce qui est transporté et ce qui reste ouvert (CLAUDE.md, § 1). Voici celles qui passent ce test, de la plus solide à la plus fragile.

1. **Le barycentre pesé** (grain, lumière, méthode).
   - *Partagé* : la formule du photocentre, G·H₁(poids).
   - *Transporté* : la littérature des étoiles doubles non résolues, appliquée aux images de Venn.
   - *Ouvert* : la vraie palette de l'image à 17 courbes.
   - *Et l'ombre* (ma lecture). Le dipôle H₁ = Σ wᵢωⁱ est l'ombre Σωⁱ des poids, par définition : un dictionnaire, mais qui transporte un fait exact. Pour des poids rationnels, comme la moyenne RGB d'une palette 8 bits, le dipôle ne s'annule que si les 17 poids sont égaux.
   - *Pourquoi.* Le polynôme minimal de ω sur ℚ est 1 + x + … + x¹⁶. Dans le modèle G·H₁, une palette inégale déplace donc toujours le centre en moyenne RGB.
2. **Le i modulo n** (bases, ombres, aiguilles).
   - *Avec ombres* : i existe modulo 17, et c'est ce qui exclut le Venn antipodal à 17 courbes. Pour n premier, −1 est un carré exactement quand n ≡ 1 (mod 4).
   - *Avec aiguilles* : 10 = N(3 + i) est le carré de l'aiguille (3, 1) sur la grille carrée, et 7 = N(3 + ω) son carré sur la grille hexagonale. Le même 3 est un i modulo 10 et une racine sixième primitive de l'unité modulo 7. C'est la raison géométrique du lemme des chiffres de 1/7 (dossier bases, § 3.2, (A)).
3. **Le cercle R/√2** (moitiés, corde, ombres).
   - Trois gestes le désignent : le miroir d'aire u ↦ 1 − u, l'inversion des jumeaux d·d′ = ½ et la dilatation d'un cran. Archimède le posait déjà (partie II).
   - Sa fiche comblerait le triangle vide corde · moitiés · ombres, ouvert quand ombres a retiré la fiche 010.
4. **Bonferroni** (aiguilles, méthode). La moitié de Kakeya fini et la correction de la fiche 012 tronquent la même inclusion–exclusion.
5. **L'isopérimétrie.** Elle réunit le seuil des 13 courbes, le polygone de la fiche 003 et la limite à 2 000 px (fiches 003, 011 et 020).
6. **Le premier 3** (fiches 015 et 021). Il divise 6 = 7 − 1 = 9 − 3, et il donne le facteur 2 de Hardy–Littlewood (dossier ombres, (A)).
7. **Les dérives** (fiches 002, 004, 018 et 021), réunies dans la fiche 022.
8. **Le logarithme commun** (K7) : ouvert.

**Ce qui reste isolé.**
- *Le dossier bases.* 9 des 11 triangles vides passent par lui, et il ne partage aucune fiche avec aiguilles, alors que le lien 2 les relie exactement.
- *D8, la physique.* Aucune fiche n'y est classée d'abord.
- *Pourquoi.* Le nerf compte les fiches partagées : il voit la comptabilité du recueil, pas les liens écrits.

**Une mise en garde.** Écrire des fiches pour remplir les triangles vides ferait baisser le compte sans rien apprendre. Quand une mesure devient un objectif, elle cesse d'être une bonne mesure : c'est la loi de Goodhart. Une fiche ne doit combler un trou que si c'est une vraie observation ; les liens 2 et 3 en sont, parce qu'ils se démontrent.

## 5. Les hasards et les coïncidences

- **Le tri des coïncidences.** Cinq avaient été testées avant ce bilan.
  - Deux sont devenues une structure : les fiches 003 et 013.
  - Trois sont devenues un hasard testé : les fiches 002, 004 et 021.

  Un hasard testé est un résultat : il dit que la grandeur dérive.
- **Une chaîne qui a marché**, de la fiche 006 à l'intervention.
  - Le centre de la lumière bouge selon la pesée (fiche 006).
  - Mon premier centre était faux de 2,36 px à cause du point de départ (fiche 007).
  - Le seuil déplace le centre, mais pas la moitié (fiche 018).
  - L'intervention établit la cause (§ 4.12).

  C'est le recueil tel que tu l'as voulu : chaque moment s'enchaîne au suivant, jusqu'à une causalité.
- **Trouvé deux fois.** Six résultats ont été trouvés par deux ou trois dossiers, chacun par son propre calcul. Mais les agents sont du même modèle et suivent le même gabarit, donc leurs erreurs peuvent être corrélées. Ici, « trouvé deux fois » vaut moins que deux laboratoires indépendants.
- **Deux familles nouvelles.**
  - *Les dérives qui croisent une constante* (fiche 022) : π puis 2√2, √2/2, les 35,10 % de l'octaèdre, et 1 en N = 16,70. À une seule valeur du paramètre, chacune ressemble à une découverte.
  - *Les liens vrais par construction* (fiche 023). Ils passent tous les tests, même la variation du paramètre.
- **Le recueil se regarde lui-même.**
  - Avant ce bilan, D7 tenait 5 fiches sur 21 (24 %). Il en tient 7 sur 23 (30 %), parce que le bilan, qui parle de méthode, a écrit deux fiches de méthode.
  - Le nombre effectif de dimensions, 1/Σp², est passé de 5,19 à 4,85. Les six paires que le cadre seul fait paraître liées restent D1, D4, D5 et D6 entre elles.
  - Le sujet de la session déforme le Venn des observations : c'est ton effet de cadre, appliqué au recueil.
  - Deux remèdes possibles : pondérer également les dimensions dans les indicateurs, ou diviser D7.
- **La diagonale a un plafond** (fiche 023). L'écart de l'arête à √2 décroît comme 1/(2K) : 8,0 % pour K = 7, 6,9 % pour 8, 3,3 % pour 16, et 1 % seulement pour 51. Avec D1 à D8, on reste donc à 6,9 % au mieux. Pour que la diagonale s'affirme, il faut que les dimensions se divisent, pas seulement que les fiches s'accumulent.

## 6. Les agents : ce qui change pour chacun

**L'agent Opus (le plan).**
- Lui donner un paquet de lecture préparé par script, de 60 Ko au plus, plutôt que le corpus. Le paquet réunit l'index, le registre, les En bref des synthèses, les CSV des arcs et le graphe des fichiers (script → résultats → figures → document).
- Lui imposer 30 Ko de texte au plus, plus un `plan-NNN.json`, et lui faire fixer un budget par agent (taille, durée, appels).
- Tirer les listes de lecture du graphe, par script. Le plan 001 en avait oublié six fichiers pour l'agent corde.
- Pour chaque congruence, lui faire dire si elle aurait pu être fausse, et quel paramètre faire varier.
- Lui faire proposer une division des dimensions.

**Les agents Sonnet (les dossiers).**
- Fixer des limites : 30 Ko, 60 min et 150 appels au plus. Les dossiers concis montrent que c'est possible sans perte.
- Écrire la sortie structurée sur disque, section par section : c'est ce qui a manqué pour lumière.
- Garder le code dans le dépôt (`recueil/revisions/NNN/code/<dossier>/`) : c'est ce qui a obligé à refaire l'intervention de méthode.
- Pas de première personne. Chaque nombre (A) donne son fichier de code.
- **Ajouter un contradicteur** : un agent avec d'autres consignes, ou un autre modèle, qui refait seulement les trois énoncés les plus forts de chaque dossier.

**Moi (la session principale).**
- Un commit après chaque étape, et un journal d'état dans le dépôt (`recueil/revisions/NNN/journal.md`). Les compactions et les redémarrages effacent la mémoire de la session, pas le dépôt.
- Les générateurs dans le dépôt dès le départ.
- Relire mes En bref avant de les publier, verbe par verbe : démontré, établi, toujours, jamais. Mes cinq excès y seraient tombés.
- Aucun énoncé (A) dans un En bref.
- Garder mes questions pour toi dans une liste, et te les poser avant la révision suivante.

**L'agent de fin d'arc.**
- Un script déduit le CSV de git à chaque arc.
- Le récit Sonnet, de 10 Ko au plus, seulement aux révisions ou tous les N arcs (question 3 du § 10.7).

## 7. Les données : la quantité et l'organisation

- **Trop de texte pour être relu.** Personne ne relira 670 Ko de dossiers, ni toi, ni l'agent Opus de la révision 002. Il faut deux couches :
  - une couche courte, que tout le monde lit : les En bref, le registre, les JSON ;
  - une couche longue, les dossiers, qu'on ne lit que pour vérifier.
- **Les mêmes nombres en dix exemplaires.** « 0,044 » est dans 11 fichiers et « 43/108 » dans 12, donc une correction doit être reportée partout à la main. La phrase « 222,5° est un arrondi », restée dans la partie XI après sa correction, montre ce mécanisme ; la révision le reproduit à plus grande échelle.
- **Le registre des résultats, proposé.** Un fichier `recueil/registre.csv`, avec une ligne par résultat et ces colonnes : `id`, `énoncé`, `valeur`, `statut` (exact, calculé, (A) ou à vérifier), `source` (le script et sa section), `fiches`, `cité_dans`.
  - Les documents citent l'id à côté du nombre, par exemple « 43/108 [R017] ».
  - Un script vérifie que chaque nombre cité est celui du registre.
  - Une correction devient une ligne, et le script dit où la reporter.
  - C'est le principe FAIR : des données qu'on retrouve par un identifiant et qu'on réutilise.
- **Les sorties structurées** (248 Ko) sont la bonne couche pour la révision suivante, parce qu'elles se lisent par script. Les dossiers devraient les citer, pas les recopier.
- **Les outils** sont archivés avec les chemins de cette session ; ils sont à réunir en `scripts/revision_outils.py`.

## 8. Une forme concrète pour la révision, à valider

| étape | qui | ce qu'elle produit | budget |
|---|---|---|---|
| 0. préparer | script | `revisions/NNN/paquet.md` : index, registre, fiches nouvelles, arcs, graphe des fichiers, ouverts | 60 Ko |
| 1. planifier | Opus | `plan-NNN.md` et `plan-NNN.json` : dossiers, lectures, questions, congruences, tests, budgets | 30 Ko, 45 min |
| 2. écrire les dossiers | Sonnet, 8 au plus, 2 à la fois, puis un contradicteur | le dossier, son JSON écrit au fil des sections, son code dans `revisions/NNN/code/` | 30 Ko, 60 min, 150 appels chacun |
| 3. croiser | script, puis moi | `verification-croisee-NNN.md` : v2, doublons, contradictions, erreurs du plan ; ma lecture | 10 Ko de lecture |
| 4. tester | moi | `scripts/revision_NNN.py` : tout ce qui entre dans l'En bref, refait et reproductible | ≈ 5 min |
| 5. synthétiser | moi | `revision-NNN.md`, chaque nombre avec son id du registre | 25 Ko |
| 6. mettre à jour | script | les fiches, le registre, l'index, la vérification des nombres cités | — |
| 7. clore | script, puis Sonnet | le CSV de l'arc ; le récit, seulement à la révision | 10 Ko |

**Deux règles en plus.**
- Un commit et un push après chaque étape : un redémarrage ou une limite ne coûte alors qu'une étape.
- À chaque révision, l'agent Opus propose de diviser la dimension la plus chargée (aujourd'hui D7).

**Le coût estimé** (une estimation, pas une mesure) : ≈ 10 h d'agents au lieu de 15, et ≈ 0,5 Mo de texte au lieu de 1,4.

## 9. Les problématiques

| # | problématique | ce qui la montre | le levier |
|---|---|---|---|
| 1 | robustesse | 2 redémarrages, 1 limite d'usage, une sortie et du code perdus | le disque d'abord ; un commit par étape |
| 2 | volume | 1,4 Mo pour un corpus de 0,83 Mo | des budgets ; une couche courte |
| 3 | cohérence | des nombres recopiés dans 11 ou 12 fichiers ; 26 erreurs en attente | le registre, vérifié par script |
| 4 | reproductibilité | 29 énoncés (A) non refaits ; un nul qui changeait d'une exécution à l'autre | le code dans le dépôt ; pas de (A) dans les En bref |
| 5 | validité | liens vrais par construction ; dérives ; erreurs corrélées entre agents ; 0 à 21 faux liens selon le classement ; p = 0,047 parmi beaucoup de tests | les deux questions ; un classement fixé avant le calcul ; le contradicteur |
| 6 | coût | 15 h d'agents pour 12 corrections et 8 fiches | des budgets ; le rendement par erreur trouvée |
| 7 | gouvernance | mes lectures de tes images (la diagonale par le simplexe, la cohomologie par le nerf, les disques placés à la main) ne sont pas validées | tes réponses au § 10.7 |
| 8 | taxonomie | 8 dimensions plafonnent la diagonale ; D8 est vide ; D7 tient 30 % ; 18 fiches sur 23 ont deux ou trois types | diviser, pondérer |
| 9 | références | 16 « à vérifier » dans la synthèse ; ni les agents ni ce bilan ne lisent les articles (arXiv et combinatorics.org sont bloqués par le réseau de la session) | une passe de vérification ; « sûre » seulement avec un DOI relu |
| 10 | sécurité et licences | le dépôt de Dzoba (CC BY 4.0) est lu, jamais exécuté ; des chemins de session restent dans les outils archivés | garder la règle ; citer Dzoba sous chaque figure dérivée |
| 11 | dimensions | le cadre du recueil fabrique 6 faux liens, et la session déplace les parts | en faire une donnée de ton sujet d'étude |

La ligne 7 mérite un mot. Une lecture non validée qui devient un fait, c'est encore la classe d'erreur que la révision chasse : elle est ici au niveau du protocole lui-même.

## 10. Les listes de tâches (les miennes)

**10.1 Consolider, avant la révision 002.**
- [x] Archiver les outils (`outils-001/`, avec leur README).
- [ ] Écrire `scripts/revision_outils.py`, avec des chemins relatifs : préparer, extraire, construire le v2, croiser, classer, réunir les sorties, mettre à jour les fiches.
- [ ] Créer `recueil/registre.csv` et le script qui vérifie les nombres cités.
- [ ] Refaire dans le script de la révision les énoncés (A) de l'En bref de la synthèse, ou les en retirer.

**10.2 Corriger le corpus.** Il s'agit des 26 erreurs signalées, une à une, avec la preuve du dossier.
- Les plus simples d'abord :
  - le README, § 7, contre CLAUDE.md, § 1 ;
  - les parties V § 3, VIII § 7, XIV § 6, XVI § 2, et XXIX § 2.2 et § 5.3 ;
  - les deux « Córdoba (1977) » ;
  - les deux sens de α_n et de β ;
  - la figure x1.
- Puis la fiche 010, avec le certificat.

**10.3 Vérifier les références** :
- Wielen (1996) sur ADS ;
- la revue de Fraser en 1984 ;
- Miles (1964) ;
- Ruskey et Weston, et Mamakani et Ruskey (la symétrie polaire) ;
- Blokhuis et Mazzocca (2008) ;
- les corrections de chromaticité de Gaia ;
- le Nikon D800E ;
- Lipsitch (2010) et Strona (2014) ;
- les identifiants arXiv et Zenodo de Dzoba.

**10.4 Les nouveaux tests.**
- Le Venn antipodal à 7 courbes, le plus petit cas permis après 3 : tester les 23 Venn simples, monotones et symétriques connus (il faut leurs données).
- k₁ à 23 courbes, sur l'archive Zenodo, si le réseau le permet.
- Le manque de 24 % de la palette tournée.
- δ₂ ≈ δ₃.
- La fiche 005, en refaisant le calcul de moitiés.
- T8 prospectif : geler le classement du prédicteur de la partie XXVII, puis compter les liens établis à chaque révision.
- Les trois ouverts de la partie XXX.

**10.5 Les fiches qui combleraient de vrais trous**, à écrire quand un script les traite :
- les trois gestes de R/√2 ;
- l'aiguille (3, 1), avec ses normes 10 et 7 ;
- l'octaèdre comme Venn antipodal à 3 courbes ;
- le dipôle des poids rationnels.

**10.6 Les changements du protocole, à valider par toi** : les budgets du § 8 dans CLAUDE.md, § 10 ; la fin d'arc allégée ; la division des dimensions ; le registre.

**10.7 Mes questions pour toi.**
1. La fiche 014 : quelle lecture de « (−2)^(3/2) ≡ −i modulo 3 » voulais-tu ? Dans F₉, 2^(3/2) est ≡ −i, mais (−2)^(3/2) vaut ±1.
2. Mes trois lectures, la diagonale par le simplexe, la cohomologie par le nerf et les disques placés à la main, sont-elles ce que tu avais en tête ?
3. L'agent de fin d'arc doit-il tourner à chaque arc ? Ou bien un script à chaque arc, et un récit aux révisions ?
4. Les budgets du § 8 te conviennent-ils ?
5. Puis-je proposer à la révision 002 de diviser les dimensions, par exemple D7 en « tests » et « cadre » ?
6. Parmi les 64 fiches proposées, lesquelles veux-tu voir écrites ? Les quatre du § 10.5 d'abord ?
7. Veux-tu écrire à Dzoba pour son code de rendu (la palette, l'ordre de dessin, l'espace de mélange) ? C'est une démarche vers l'extérieur : je peux préparer le message, mais c'est toi qui l'envoies.

## Le tri

- **Mesuré** : les durées, les appels, le contexte cumulé, les tailles, les nombres recopiés et le rendement des dossiers.
- **Exact**, en une ligne chacun :
  - l'arête √(2K/(K − 1)) et son plafond pour K = 8 ;
  - le dipôle des poids rationnels, nul seulement à poids égaux ;
  - l'octaèdre comme Venn antipodal à 3 courbes ;
  - 10 = N(3 + i) et 7 = N(3 + ω) ;
  - 1 − 0,953²⁰ = 0,62.
- **Relu, pas refait** : la démonstration de parité du dossier ombres, dont une étape reste à justifier.
- **Mes lectures** (corrige-moi) :
  - les cinq classes ;
  - la dérive vers D7 comme effet de cadre ;
  - les trous de v1 comme trous de la lecture du plan ;
  - le diagnostic des agents, qui mêle le gabarit, le sujet et l'ordre.
- **Estimé** : le coût de la forme proposée.
- **À vérifier** : ce que la littérature dit des Venn polaires.

## Sources

- B. A. Nosek, C. R. Ebersole, A. C. DeHaven, D. T. Mellor, « The preregistration revolution », *PNAS* 115, 2600–2606 (2018) : fixer l'analyse avant de voir les données.
- A. Gelman, E. Loken, « The statistical crisis in science », *American Scientist* 102, 460–465 (2014) : le jardin des chemins qui bifurquent.
- M. J. Page et al., « The PRISMA 2020 statement », *BMJ* 372, n71 (2021) : un protocole de synthèse écrit d'avance, avec ses étapes et ses comptes.
- M. D. Wilkinson et al., « The FAIR Guiding Principles for scientific data management and stewardship », *Scientific Data* 3, 160018 (2016).
- M. Strathern, « "Improving ratings": audit in the British University system », *European Review* 5, 305–321 (1997) : la forme courante de la loi de Goodhart.
- K. Borsuk, *Fund. Math.* 35, 217–234 (1948) ; A. Hatcher, *Algebraic Topology* (2002), corollaire 4G.3 : le théorème du nerf.
- E. Gross, O. Vitells, « Trial factors for the look elsewhere effect in high energy physics », *Eur. Phys. J. C* 70, 525–530 (2010).
- F. Ruskey, M. Weston, « A survey of Venn diagrams », *Electron. J. Combin.*, DS5 : [combinatorics.org](https://www.combinatorics.org/files/Surveys/ds5/VennSymmEJC.html).
- K. Mamakani, F. Ruskey, « A New Rose: The First Simple Symmetric 11-Venn Diagram » (2012) : [arXiv:1207.6452](https://arxiv.org/abs/1207.6452).
- T. Cao, K. Mamakani, F. Ruskey, « Symmetric monotone Venn diagrams with seven curves » : [page de F. Ruskey](https://webhome.cs.uvic.ca/~ruskey/Publications/Venn7/Venn7.html) ; et, pour la définition de la symétrie polaire, [les Venn polaires à 6 courbes](https://webhome.cs.uvic.ca/~ruskey/Publications/SixVenn/SixVenn.html).
