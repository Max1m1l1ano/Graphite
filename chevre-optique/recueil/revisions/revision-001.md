<!-- arcs: 1 -->
# Révision 001 : la diagonale √2 mise en équation, le cadre qui fabrique des liens, et huit dossiers

> « … réviser, lorsqu'il y a plus de 10 de ces observations et moins que 16, tous les scripts, leurs contexte, l'information qu'elles produisent et le cadre de l'observation pour les regrouper en dossiers sur les sujets englobant tout le corpus de recherche et qui permettent de synthétiser et regrouper ces information en Perron avec le triangle du bas, formé des différentes branches qui se rejoignent, comme projection du groupe qui rejoint ces informations et ce triangle placé dans un des disques. Essentiellement un Venn multidimensionnel qu'on sait va finir par donner la diagonale sqrt(2)… »
>
> (le message qui fonde le recueil, 7 octobre 2026 ; la révision est due : 15 fiches non révisées)

Les tests sont recalculés par [`scripts/revision_001.py`](../../scripts/revision_001.py) (≈ 4 min, il demande la copie locale du dépôt de Dzoba pour les § 4.8 et 4.12). Les tableaux complets sont dans [`resultats/revision_001.md`](../../resultats/revision_001.md). Le plan de l'agent Opus est dans [`plan-001.md`](plan-001.md), la vérification croisée dans [`verification-croisee-001.md`](verification-croisee-001.md), les huit dossiers dans [`../dossiers/`](../dossiers/).

## En bref

- **La diagonale √2 devient mesurable.**
  - Une classification naïve à parts égales, une fois centrée, est un simplexe régulier. Son arête √(2K/(K − 1)) rejoint √2 par en dessus quand le nombre K de dimensions grandit.
  - Sa corde vers l'antipode la rejoint par en dessous, et Thalès les lie : d² + c² = 4.
  - La corde de la chèvre de dimension n est exactement une de ces cordes, pour K = n + 2 + le tiers de dimension de la partie XXIV.
  - « Plus les révisions augmentent, plus la diagonale √2 s'affirme » devient un énoncé mesurable. Après cette révision, K = 7 et l'arête à parts égales vaut 1,5275, plus près de √2 ; mais les parts restent inégales, et le cadre fabrique 6 faux liens au lieu de 3 (§ 2).
  - *Précision du [bilan](bilan-001.md) (fiche 023)* : le lien avec la chèvre est un dictionnaire, car K est choisi pour que les deux cordes coïncident. Ce qui se calcule, c'est K − n → 7/3, hérité de la partie XXIV. Et avec huit dimensions, l'arête ne descend pas sous 1,512, 6,9 % au-dessus de √2 : pour que la diagonale s'affirme, il faudra diviser les dimensions.
- **Le cadre fabrique des liens, des déplacements et des nombres.** Trois résultats touchent ton sujet d'étude, la restriction du cadre :
  - **Les liens.** Avec des parts inégales, deux dimensions rares paraissent liées sans rien partager, exactement quand p_a + p_b < Σp². Le partage équitable des aires empêche ce faux lien. Mais leur nombre dépend aussi du classement : de 0 à 21 selon la dimension choisie pour chaque fiche (dossier méthode).
  - **Les déplacements.** Dans l'image du Venn à 17 courbes, monter le seuil d'un masque binaire déplace le centre de 0,044 px à 27 px, sans toucher à la moitié de l'aire. Un effet de seuil prouve que la grandeur seuillée varie d'une courbe à l'autre (§ 3).
  - **Les nombres.** Le seuil de 13 courbes du centre du Venn vaut 4π·(s/a)² : la loi est la constante isopérimétrique, le 13 vient du choix de 2 px.
- **La cause du centre de la lumière est établie par une intervention.** L'agent méthode a repeint un Venn à 13 courbes de palette connue avec son propre rendu. Le photocentre G·H₁ des poids y prédit le déplacement sans paramètre libre (2,08 px prédits, 2,05 à 2,20 observés), et l'ordre de dessin ne compte pas (§ 3).
- **Huit dossiers couvrent les 30 parties.** Les corrections des agents referment les 4 trous du corpus de v1. Il reste 11 trous du recueil, autant que le hasard, dont 9 passent par le dossier bases : c'est là que les prochaines fiches compteraient le plus (§ 4).
- **Des liens nouveaux entre dossiers** (§ 6) :
  - il n'existe pas de Venn simple antipodal à 17 courbes, parce que i existe modulo 17 (une obstruction de parité, dossier ombres). « Antipodal » veut dire qu'une involution sans point fixe garde chaque courbe et envoie chaque région sur son complément. *Précision du bilan (§ 3)* : la symétrie « polaire » de la littérature est un demi-tour, que la parité n'exclut pas ;
  - la face que choisit a modulo 3 dans la fiche 015 et la limite 2 de la fiche 021 sont le même nombre 3 ;
  - les périodes de Gauss du 17-gone sont des ombres du cube.
- **Douze nouveaux tests**, la plupart en faisant varier un paramètre :
  - **Kakeya fini.** La moitié vient de Bonferroni, pas de l'involution. La piste XIV–XX se ferme.
  - **1/7 et la base 10.** C'est la famille q² + 1, et 7 × 13 = Φ₆(10).
  - **Les dizaines de premiers.** Leur rapport dérive, et croise π puis 2√2.
  - **Midy.** Sa tour de périodes se divise par deux à chaque étage (1/3, 1/3, 1/6, 1/12) : la forme binaire d'un arbre de Perron, pas sa loi.
  - **Les trois 4/3.** C'est une coïncidence de petits entiers.
  - **L'arbre de Perron.** Il descend à 43/108, sous les 2/5 des arbres télescopiques ; la partie V l'avait trouvé en nombres.
  - **Le « 93 % » de la défocalisation.** C'est le taux de base : un prédicteur constant fait 70 rayons sur 76, contre 71 (§ 7).
- **La méthode relue.** Le banc d'essai de la partie XXX est en partie construit : la précision ne dit jamais « hasard », et trois verdicts de la variation sont posés à la main. Les erreurs des chaînes de production tombent en cinq classes ; la plus fréquente, le cadre, est la seule qu'aucun test ne voit (dossier méthode).
- **La révision a corrigé douze erreurs**, après vérification : dans les parties XI, XIV, XVIII, XIX, XXIII, XXVII, XXVIII, XXIX et XXX, et dans CLAUDE.md. Les autres sont listées avec leur statut (§ 8).
- **Où chercher les prochaines données** : § 9.

## 1. Comment la révision s'est faite

La chaîne de production de cette révision, dans l'ordre :
1. **Le plan.** Un agent Opus a lu le recueil, le README et les parties, et a écrit [`plan-001.md`](plan-001.md). Il y a mis :
   - 8 dossiers, avec leur recouvrement exact en JSON ;
   - 8 arbres « en Perron » ;
   - 10 congruences à tester (K1 à K10) et 8 tests (T1 à T8) ;
   - le rapport de lancement du workflow, soit 9 agents Sonnet.
2. **Le workflow.** Les agents Sonnet ont écrit un dossier chacun.
   - Le conteneur a redémarré deux fois pendant la révision. Quatre dossiers ont survécu (corde, moitiés, bases, grain). Les quatre autres (lumière, aiguilles, ombres, méthode) ont été relancés dans un second workflow, avec la consigne d'être plus concis.
   - Une limite d'usage hebdomadaire a encore arrêté trois agents. Lumière avait fini d'écrire son dossier (sa sortie structurée est perdue : j'en ai relevé les corrections à la main). Ombres et méthode ont été relancés une troisième fois, après ton « Réessayer ».
   - La vérification croisée prévue pour un neuvième agent, je l'ai faite moi-même à partir des corrections de chaque agent ([`verification-croisee-001.md`](verification-croisee-001.md)).
3. **Les tests.** J'ai calculé les tests du plan dans `scripts/revision_001.py`, sauf T8 (le nerf contre la carte), que l'agent méthode a fait hors du dépôt (A). J'y ai ajouté cinq tests nés en route (§ 4.1, 4.2, 4.9, 4.11, 4.12). Six énoncés des dossiers y sont refaits avant d'être cités (§ 4.10).
4. **La synthèse.** C'est ce document, avec les nouvelles fiches 016 à 021, les fiches 001 à 015 marquées « révisé : 001 », et les corrections du corpus.

**Une étiquette pour chaque énoncé**, comme dans « Le tri » :
- *vérifié* : refait par `scripts/revision_001.py` ;
- *(A)* : calculé par un agent, hors du dépôt, avec son code dans le § 7 de son dossier, à refaire ;
- *ma lecture* : un rapprochement proposé ;
- *à vérifier* : une référence ou un détail non confirmé.

## 2. La diagonale √2 : ce que veut dire « elle s'affirme »

Résultats : [`resultats/revision_001.md`](../../resultats/revision_001.md), § 1 et 2.1. Figure : [`rev001_diagonale_cadre.png`](../../figures/rev001_diagonale_cadre.png), panneaux a et b.

**La classification naïve est un simplexe** (vérifié).
- On range des fiches à parts égales dans K dimensions, puis on retire la fiche moyenne. Les K classes deviennent les sommets du simplexe régulier inscrit dans la sphère : le cosinus entre deux sommets vaut −1/(K − 1).
- Deux fiches de dimensions différentes sont alors à l'arête d_K = √(2K/(K − 1)). Elle vaut 1,512 pour 8 dimensions, 1,458 pour 17 et 1,421 pour 100 : toujours plus que √2.
- Sans retirer la moyenne, elles seraient exactement à √2, la diagonale d'une face du cube {0, 1}^K du Venn. En retirant ce que toutes les fiches ont en commun, le √2 devient une **limite**. Il s'affirme quand le nombre de dimensions grandit.

**Thalès relie cette diagonale à la chèvre** (vérifié ; fiche 016).
- Pour deux vecteurs unités u et w, prends l'arête d = |u − w| et la corde c = |u + w|, de u à l'antipode de w. On a toujours d² + c² = 4 : le triangle (w, u, −w) est rectangle en u, d'hypoténuse le diamètre.
- La corde du simplexe vaut c_K = √(2(K − 2)/(K − 1)). Elle tend vers √2 par en dessous, pendant que l'arête y tend par en dessus.
- **La corde de la chèvre de dimension n est exactement une corde de ce simplexe**, pour K = 1 + 1/x₀(n), où x₀ est le plan de la lentille de la partie XXIV.
  - K − n monte de 2 (en 1D) vers 7/3 : c'est 2, plus le tiers de dimension de la partie XXIV.
  - À n = 1 000, K − n = 2,33086, comme le développement 7/3 − 112/(45n) + 3856/(189n²).
- Le dossier corde relie ce K = N + 2 à quatre parties qui portaient déjà le tiers de dimension : XV § 4, XXIII § 2, XXIV § 3 et XXVII § 6. Il ajoute la formule exacte N − n = (n + 1)·μ/(2x₀) (A).
- La diagonale √2 du Venn des révisions et la corde √2 de la chèvre infinie sont donc les deux côtés du même angle droit.

**Ce qu'on suit d'une révision à l'autre.**
- L'index du recueil calcule à chaque passage :
  - le nombre K de dimensions principales occupées ;
  - leur nombre effectif 1/Σp² ;
  - l'arête du simplexe à parts égales ;
  - les paires de dimensions que le seul cadre fait paraître liées.
- Pour les 15 premières fiches : K = 6, 1/Σp² = 4,79, une arête à parts égales de 1,5492, et 3 faux liens.
- Après la révision (21 fiches, avec les six nouvelles) : K = 7, car D5 est occupée par la fiche 019 ; 1/Σp² = 5,19 ; une arête à parts égales de 1,5275, plus près de √2. Mais il y a 6 faux liens au lieu de 3, tous entre les quatre dimensions rares (D1, D4, D5 et D6, une ou deux fiches chacune ; D1–D6 passe de justesse, 0,1905 contre 0,1927).
- La diagonale s'affirme quand K grandit, et le cadre fabrique plus de liens tant que les parts restent inégales : c'est la règle de la fiche 017, vue d'une révision à l'autre. Elle s'affirme vraiment quand K grandit **et** que les parts s'égalisent.

## 3. Le cadre fabrique des liens, et des déplacements

Résultats : § 2.1, 4.8 et 4.9. Figure : panneaux b et c. Fiches 017 et 018.

**Des liens** (vérifié).
- Les 15 fiches occupent 6 dimensions, à parts inégales : D2 et D7 en ont 4, D1 et D4 une seule.
- Les fiches de D1 et de D4, qui ne partagent rien, sont à 1,364 l'une de l'autre, sous √2 : elles *paraissent* liées. Celles de D2 et D7 sont repoussées à 1,721.
- La règle est exacte : deux classes a et b passent sous √2 exactement quand p_a + p_b < Σp². Elle est vérifiée sur les 15 paires.
- Avec des parts égales, p_a + p_b = 2/K reste toujours plus grand que Σp² = 1/K : aucun faux lien. **Le partage équitable des aires est la condition qui empêche le cadre de fabriquer des corrélations.**
- En statistique, c'est le « problème des doubles zéros » de l'écologie numérique, de la même famille que les corrélations parasites des données à somme constante.
- **Le « 3 » dépend du classement** (dossier méthode, (A)). Si chaque fiche peut aussi tomber sur une des dimensions voisines qu'elle déclare, il y a 27 648 classements plausibles : le nombre de faux liens va de 0 à 21 (3,2 en moyenne), et 17,7 % des classements n'en ont aucun. Le 3 du recueil est une réalisation, pas une mesure. Le partage égal des aires supprime le faux lien, pas le choix du classement : c'est le « jardin des chemins qui bifurquent » (Gelman et Loken, 2014). Pour le fermer, on fixe le classement avant de calculer, ou on calcule sur toutes les variantes.

**Des déplacements** (vérifié ; ta question sur le masque binaire).
- Le masque binaire est l'ensemble des pixels dont la clarté perçue OKLab dépasse celle du fond, une couleur exacte (6, 6, 10), de t.
  - Sans seuil, l'encre est centrée à 0,044 px du centre de symétrie, qui est connu à 0,003 px.
  - Quand t monte, le centre s'écarte jusqu'à 27,4 px.
- Ce n'est ni un passage signé/non signé (l'histogramme des canaux est lisse entre 127 et 128), ni l'ordre de dessin (pas de montée des aires visibles le long d'un tour : p = 0,64).
- **C'est le seuil.** Il change la couleur en largeur visible, par l'anticrénelage des bords.
- **La moitié, elle, ne bouge pas.** La part de l'encre dans le contour réduit de 1/√2 reste entre 49,3 et 49,7 % pour t = 0,005 à 0,3, alors que la quantité d'encre passe de 81 à 19 %.
  - Le seuil touche le premier harmonique (le dipôle, donc le centre).
  - La moitié ne dépend que de l'harmonique zéro, que la rotation d'ordre 17 protège.
  - Le résultat de la partie XXX sur la moitié est robuste au cadre ; ses centres de la lumière ne le sont pas.
- **Ce qu'ajoute le dossier grain** (§ 3.5, (A)) :
  - Le « contraste d'ordre » des PNG du traceur, dessinés de 0 à n − 1, vaut +14,8 % et +8,6 %. Celui de l'image à 17 courbes vaut −6,0 %, comme les témoins sans ordre : l'ordre de dessin est écarté une seconde fois, par une autre méthode.
  - Une palette presque isoluminante en luminance Y (Y₀ ≈ 0,30 à 0,36) redonne les quatre pesées continues avec un seul facteur géométrique. C'est pourquoi la luminance donne le plus petit écart (0,61 px).
- **L'intervention qui manquait, faite sur un système modèle** (dossier méthode, § 3.6 ; refaite par le script, § 4.12 : vérifié). Le Venn à 13 courbes du traceur de Dzoba a une palette et un ordre de dessin connus. L'agent en a lu la géométrie dans le SVG, l'a repeinte avec son propre rendu (aucun code de Dzoba exécuté), puis a changé une seule chose à la fois.
  - *La palette* : le centre se déplace de G·H₁(poids), **sans paramètre libre** (le bras de levier G est lu dans le SVG) : 2,08 px prédits, 2,05 à 2,20 px observés selon le rendu, phases à 11° près. Décalée de 4 courbes, la palette fait tourner l'écart de −109,5° (prédit : −110,8°), mais son module tombe à 1,58 px, 24 % sous la prédiction : un écart que le modèle n'explique pas. Avec une palette à luminance égale, l'écart en luminance tombe à 0,13 px, et ceux de la moyenne RGB et de l'énergie restent à 2,3 et 1,6 px : c'est le motif de l'image à 17 courbes.
  - *L'ordre de dessin* : quatre autres ordres déplacent le centre de 0,26 px au plus, contre 2,20 px pour la palette.
  - *Un témoin du seuil* : sur le PNG à 13 courbes, dont toutes les courbes ont la même clarté OKLab (0,58), un seuil sur la clarté ne déplace le centre que de 0,07 à 0,29 px ; un seuil sur la moyenne RGB, qui varie d'une courbe à l'autre, de 1,1 à 11,7 px. **Un effet de seuil prouve donc que la grandeur seuillée varie d'une courbe à l'autre** : dans l'image à 17 courbes, la clarté va de 0,60 à 0,71 (correction de la partie XXX, § 1.1). C'est la cause du balayage de la fiche 018.
  - La causalité « palette → centre » est donc établie par intervention, sur un système modèle. Pour l'image à 17 courbes elle-même, la palette reste inconnue.
- **Le dossier grain nomme aussi les quatre variables cachées de l'image de référence** : le certificat, la mise en page, la palette et l'ordre de dessin. Son code de rendu n'est pas publié. C'est un trou de la chaîne de production des parties XXIX et XXX (§ 8).

## 4. Les huit dossiers et leur nerf

**Les dossiers.** Chacun réunit les parties qui partagent un même procédé :

| dossier | question directrice (résumée) | parties (v1 → v2) | fiches (v1 → v2) |
|---|---|---|---|
| [corde-et-dimensions](../dossiers/corde-et-dimensions.md) | quel procédé fait passer la corde de 1,1587 à √2, et que transporte-t-il d'une dimension à l'autre ? | 13 → 18 | 2 → 4 |
| [moities-et-crans](../dossiers/moities-et-crans.md) | toutes les moitiés viennent-elles de quelques procédés seulement ? | 14 → 22 | 2 → 3 |
| [bases-congruences-premiers](../dossiers/bases-congruences-premiers.md) | quelles congruences relient bases, puissances, périodes et premiers ? | 11 → 17 | 5 → 6 |
| [grain-pixels-centres](../dossiers/grain-pixels-centres.md) | que peut trancher un grain fini, et à quel taux s'échange-t-il ? | 7 → 11 | 5 → 6 |
| [lumiere-et-physique](../dossiers/lumiere-et-physique.md) | quelles lois optiques suivent le même procédé que la chèvre et le Venn ? | 14 → 16 | 3 → 4 |
| [aiguilles-kakeya-perron](../dossiers/aiguilles-kakeya-perron.md) | comment le grain plafonne-t-il Perron et Kakeya ? | 10 → 16 | 2 → 3 |
| [ombres-cube-venn](../dossiers/ombres-cube-venn.md) | le cube {0, 1}ⁿ et ses ombres sont-ils le groupe commun ? | 10 → 11 | 8 → 7 |
| [hasard-et-methode](../dossiers/hasard-et-methode.md) | quel test pour quelle observation, et où les chaînes de données ont-elles dérapé ? | 8 → 15 | 7 → 8 |

Aucun agent n'a retiré de partie ; un seul a retiré une fiche (ombres : la 010, qui relève de la moitié, pas du cube). Les raisons de chaque correction sont dans la [vérification croisée](verification-croisee-001.md), § 1.

**Le nerf** (vérifié ; § 3 des résultats ; figure [`rev001_perron_venn.png`](../../figures/rev001_perron_venn.png), panneau a).
- On met un sommet par dossier, une arête quand deux dossiers partagent une fiche, et un triangle quand trois en partagent une.
- **Au niveau des fiches (v1)**, b₀ = 1 et b₁ = 5, avec 9 triangles vides. Des dossiers de mêmes tailles tirés au hasard en laissent 5,7 en moyenne (p = 0,16) : un peu plus que le hasard, sans plus. Les trous se lisent un par un, comme des pistes.
- **5 trous du recueil.** Une partie réunit les trois dossiers ; il manque la fiche.
  - bases · corde · moitiés ;
  - bases · corde · ombres ;
  - grain · méthode · lumière ;
  - grain · méthode · ombres ;
  - méthode · lumière · ombres.
- **4 trous du corpus.** Aucune partie ne réunit les trois dossiers.
  - aiguilles · grain · méthode ;
  - aiguilles · grain · ombres ;
  - bases · grain · méthode ;
  - bases · grain · ombres.
  - **Tous passent par le grain.** Le corpus mesure le grain avec chacun de ces sujets, mais jamais avec deux à la fois. Par exemple, aucune partie ne teste le hasard sur une construction de Perron limitée par le grain.
- **Avec les parties**, toutes les boucles se remplissent (b₁ = 0). Il reste b₂ = 5 cavités, comme pour des dossiers tirés au hasard (p = 0,71) : un effet de la taille des dossiers, pas une donnée.

**Le nerf v2, après les corrections des huit agents** (vérifié ; figure, panneau a ; la lecture détaillée est au § 3 de la [vérification croisée](verification-croisee-001.md)).
- **Les 4 trous du corpus de v1 sont refermés.** Les parties que les agents ont ajoutées donnent une partie commune à ces quatre triplets (XXIV à XXVII pour le grain, XIV et XXV pour méthode, XXIX et XXX pour aiguilles, XV et XVIII pour bases). C'étaient des trous de la lecture du plan, pas du corpus.
- **Au niveau des fiches, 11 triangles vides**, autant que des dossiers de mêmes tailles tirés au hasard (10,1 en moyenne, p = 0,44). Tous sont des trous du recueil.
- **Le dossier bases est dans 9 des 11, et dans les 10 tétraèdres creux.** Ses fiches touchent peu les autres dossiers (une seule fiche commune avec corde, grain, lumière ou moitiés, aucune avec aiguilles). C'est là que de nouvelles fiches compteraient le plus.
- **Un trou ouvert par une correction.** En retirant la fiche 010, ombres ouvre le triangle corde · moitiés · ombres, que la 010 cachait. Il demande une fiche du cercle R/√2.
- **Avec les parties**, plus aucun triangle vide (20 en v1) et une seule cavité, b₂ = 1 (p = 0,047 contre le nul). C'est un test parmi une dizaine, de justesse, et le nerf n'est pas la réunion (§ 6) : à surveiller, pas une découverte.
- **Ce que le nerf apprend d'une révision à l'autre** : une correction d'agent referme des trous du corpus (on lit mieux le corpus) et en déplace vers le recueil (il manque des fiches). Le nerf dit donc où écrire les prochaines fiches.

## 5. La synthèse en Perron : les huit arbres

Figure : [`rev001_perron_venn.png`](../../figures/rev001_perron_venn.png), panneau b. Chaque arbre a des branches, qui sont des chaînes de parties et de fiches. Elles se rejoignent dans un triangle du bas, posé dans le disque de sa dimension. Le plan les a proposés (§ 2.2) ; les dossiers les corrigent.

| arbre | triangle du bas | disque | ce que la révision change |
|---|---|---|---|
| P1 | l'ombre du cube {0, 1}ⁿ | D6 | Les trois 34 (aigrettes, ombre Σωⁱ, éventails) sont un seul fait : les N racines de l'unité et leurs opposées font les 2N racines d'ordre 2N quand N est impair (dossiers lumière et aiguilles, N = 3 à 20, (A)). C'est une section globale, à ajouter à l'arbre comme branche de la parité. Le dossier ombres trouve huit regards sur le même cube, tous déjà écrits dans le corpus ; la fiche 015 y entre par une restriction (la fibre au-dessus de 0), pas par une ombre ; les périodes de Gauss du 17-gone sont des ombres Σωⁱ (calculé à 10⁻¹⁵, (A)) ; la branche Perron part de la partie V. « Groupe » est un mot trop fort : l'objet commun est le cube et ses projections ; le groupe géométrique est ℤ/n × ℤ/2 |
| P2 | la moitié | D1 | Un seul cercle, R/√2, est fixé par trois gestes : le miroir d'aire, l'inversion des jumeaux et la dilatation d'un cran (dossier moitiés ; Archimède, II § 1). La branche « Kakeya fini » s'en détache : elle vient de Bonferroni (T5) |
| P3 | le terme x²/6 | D1 | Même 1/6, pas le même ménisque : l'obstruction est à l'ordre 4 (T3). Le « dernier 2 » du ménisque compte les dérangements de 3 (vérifié, § 4.10) |
| P4 | le quart de tour i modulo b | D2 | La famille q² + 1 et le lemme des chiffres (vérifiés) ; 7 × 13 = Φ₆(10) ; (ℤ/10)* est aussi un groupe de Galois, et le dernier chiffre d'un premier dit si le nombre d'or existe modulo p (dossier bases, (A)) |
| P5 | le budget en bits | D3 | Le seuil des 13 courbes est la constante isopérimétrique (vérifié) ; la loi des 8R de la partie XVIII donne le budget de la moitié du Venn (dossier grain, (A)). K7 tient pour la pente, pas pour les valeurs : le « 2,8 » de Perron sur une grille culmine à 2,83 (n = 256) puis baisse à 2,57 (n = 65 536) (dossier aiguilles, (A)) |
| P6 | les réduites et les trois distances | D2 | Le diésis et le comma sont deux écarts du même théorème des trois distances (dossier bases, (A)) ; les deux longueurs ne tombent pas seulement aux dénominateurs des réduites (corrigé). La demi-case (déterminant ±1, aire ½, Pick) est un seul procédé pour Fibonacci, Pell, Farey et l'hexagone ; l'or et l'argent sont les deux premiers points du spectre de Markov (dossier aiguilles) |
| P7 | la loi de l'écart | D7 | Elle tranche 10 tests de cette révision ; elle a sa réserve : la dérive qui croise une constante (4.2, 4.9 ; et la part des triangles, 35,95 puis 35,76 puis 35,12 % à 17, 19 et 23 courbes, qui passe par les 35,10 % de la fiche 004). Le dossier méthode en relit la lignée : la variation du paramètre date de la partie VI, le banc de la partie XXX l'a mise en tableau, et une partie de son « 10/10 » est posée à la main |
| P8 | le cône à sommet imaginaire | D8 | La branche « photocentre » s'en détache (dossier lumière) : le photocentre n'a ni col ni distance de Rayleigh. La forme de Newton x·x′ = c revient cinq fois : lentille, œil de poisson, jumeaux de la chèvre, fantômes des pixels, complément du Venn (dossier lumière) |
| P9 (nouveau) | le barycentre pesé (le dipôle H₁ des poids) | D8 contre D3 | Les étoiles doubles (Wielen), la molécule HD et le Venn : le centre de la lumière est le premier harmonique des poids, et le seuil en est un second canal (fiches 006 et 018 ; dossier lumière). Établi par une intervention sur un Venn à 13 courbes de palette connue, sans paramètre libre (dossier méthode ; vérifié, § 4.12) |

## 6. L'étude cohomologique : ce qui se recolle, et ce qui ne se recolle pas

Chaque fiche, chaque résultat de partie, est une **section locale**, vraie dans son cadre. Deux sections **se recollent** quand elles coïncident sur ce qu'elles partagent, à une transformation connue près : c'est une congruence. Ce qui ne se recolle pas est une **obstruction**, et elle désigne un trou.

| | ce qui est comparé | verdict de la révision |
|---|---|---|
| K1 | le ménisque de la chèvre et la lumière du polygone | se recolle aux ordres 2 et 3 (décalage s = 49/10), **obstruction à l'ordre 4** (vérifié). Le trou : un diaphragme à rayon distribué, partenaire de l'asymétrie de la coquille |
| K2 | les trois 34 : aigrettes, ombre Σωⁱ, éventails | **section globale** : vérifiée pour N = 3 à 20 par deux dossiers (lumière, aiguilles, (A)) ; la réserve de la phase pour une ouverture complexe est dans le dossier lumière, § 5.1 |
| K3 | 1/7, les racines digitales de 2ⁿ, i modulo 10 | **se recolle** par la famille q² + 1 et le lemme des chiffres (vérifiés) |
| K4 | les moitiés | l'involution et la dilatation se recollent en R/√2 ; **Kakeya fini fait obstruction** (vérifié) |
| K5 | le 17 de Henderson et le 17 de i | **obstruction** pour une transformation (19 et 23 ont des Venn et pas de i), mais **une implication nouvelle** (dossier ombres, démontrée sous l'hypothèse forte, (A)) : si i existe modulo n, aucun Venn simple et symétrique n'a le complément pour symétrie. Un tel Venn serait antipodal ; dans le plan projectif, deux courbes unilatères se coupent un nombre impair de fois, donc C(n, 2) doit être impair, n ≡ 2 ou 3 (mod 4). Impossible à 17 (4² ≡ −1) ; à 19 et 23, ni exclu ni construit |
| K6 | le dipôle de la pesée et le photocentre | la seconde cause est le seuil, pas l'ordre de dessin (vérifié) ; avec une palette presque isoluminante, l'obstruction se lève (dossier grain). **Sur un Venn à 13 courbes de palette connue, la loi G·H₁ prédit l'écart sans paramètre libre, et l'ordre de dessin ne compte pas** (dossier méthode ; vérifié, § 4.12). Pour l'image à 17 courbes, la palette reste inconnue |
| K7 | le grain plafonne la profondeur | se recolle modulo un cran **pour la pente**, pas pour les valeurs (le « 2,8 » n'est pas une constante, dossier aiguilles) ; la cause commune du logarithme reste ouverte |
| K8 | les trois 4/3 | **obstruction** : une coïncidence de petits entiers (vérifié) |
| K9 | Midy, pair et impair | se recolle en une tour binaire (1/3, 1/3, 1/6, 1/12, vérifié), **à aires inégales**. Le dossier bases ajoute l'enchevêtrement par la réciprocité quadratique (A). Le dossier méthode précise : la division par deux est la queue géométrique de toute valuation 2-adique ; c'est la forme d'un arbre de Perron, pas sa loi 2/(k + 2) |
| K10 | le seuil du centre et l'isopérimétrie | **se recolle exactement** : 4π, et n·tan(π/n) pour le polygone (vérifié) |

**Les obstructions nouvelles des dossiers** (une sélection ; chaque dossier a sa table, § 5.3) :
- δ₂ ≈ δ₃ à 10⁻⁵ : une proximité nommée trois fois (VI, XVI, XXIV), jamais expliquée (dossier corde).
- La chèvre n'atteint √2 qu'à l'infini, alors que les réseaux records (D₃, E₈, Leech) ont leur trou le plus profond à √2 fois le rayon en dimension 3, 8 et 24. Aucun lien démontré (dossier corde).
- La fiche 005 : « miroir + complément » arrive en tête dans les 18 certificats, à 1,5 à 2,3 fois le hasard, mais aucun certificat n'est symétrique par le complément. Cause inconnue (dossier moitiés, (A)).
- Le logarithme de K7 vient d'une troncature pour la série de la chèvre, et d'un grain fini pour Perron, le Venn et les pixels : deux causes pour une même loi (dossier grain).
- Le nerf n'est pas la réunion (dossier ombres, (A)). Le théorème du nerf demande des intersections contractiles : c'est vrai des calottes des chèvres (partie XX), pas des dossiers. Dans le graphe des renvois de la partie XXVII, 6 intersections sur 81 ne le sont pas en v1 (36 sur 166 en v2), et les nombres de Betti du nerf diffèrent de ceux de la réunion. Les triangles vides restent des pistes ; les cavités sont des propriétés du classement, pas du corpus.
- L'étiquette « structure » ou « hasard » n'est pas une fonction de l'écart (dossier méthode) : rangés par écart, les six cas non triviaux du banc alternent S C S S S C. Aucun test qui ne regarde que l'écart ne peut les séparer.

**Un recollement nouveau** (dossier ombres, (A)) : la face que choisit a modulo 3 dans la fiche 015 et la limite 2 de la dérive de la fiche 021 sont le même nombre 3. C'est le seul premier impair, étranger à 10, qui divise une différence de deux chiffres des unités (6 = 7 − 1 = 9 − 3) : il interdit deux coordonnées à la fois, et c'est lui qui donne le facteur 2 de Hardy et Littlewood pour l'écart 6. La roue modulo 30 dessine les trois faces.

## 7. Les nouveaux tests de la révision, et leurs verdicts

Presque chaque test fait varier un paramètre, comme le demande le choix du test du § 10 de CLAUDE.md. Le nerf (T1) et sa comparaison à la carte (T8) sont des nuls, la dernière ligne de la table du § 10 (dossier méthode). Résultats : [`resultats/revision_001.md`](../../resultats/revision_001.md), § 4 et 5.

| test | ce qui varie | verdict | ce que ça change |
|---|---|---|---|
| 4.1, fiche 013 | la base (3 à 60), le premier (jusqu'à 400) | seul (10, 7) répond, hors des cas triviaux | le lien 1/7 ↔ racines digitales de 2ⁿ est propre à la base 10 |
| 4.2, fiche 015 | la taille N (10⁴ à 10⁸) | le rapport par motif dérive de 3,90 à 2,53 et croise π puis 2√2 ; les paires larges restent à 2 | deux « constantes » qui n'en sont pas (fiche 021). Le dossier bases prolonge jusqu'à 10⁹ : la prédiction de Hardy et Littlewood à taille finie s'accorde à 0,0005 près (A) |
| 4.3, K3 | la famille b = q² + 1 | seuls q = 2 et 3 remplissent le groupe | le 3 de 1/7 et le i modulo 10 sont le même 3 |
| 4.4, K1 | l'ordre du développement | même 1/6 ; l'ordre 4 ne se recolle pas | même exposant, pas le même ménisque |
| 4.4, K10 | le centre en cercle ou en polygone | 4π = 12,566 et π/arctan(1/4) = 12,824 | le seuil des 13 courbes est isopérimétrique (fiche 020) |
| 4.5, K8 | les bases de 3 à 10⁶ | 4/3 pour b = 10 à 16 et 244 à 256 seulement | une coïncidence de petits entiers. Le dossier bases ajoute la loi des fenêtres : 2 pour 4/3, 81 pour 19/12 (A) |
| 4.6, K9 | la borne et la base | 2/3 de périodes paires (17/24 en base 2) ; tour 1/3, 1/3, 1/6, 1/12 | le « Venn de Midy » a des aires inégales par nature ; sa tour a la forme d'un arbre de Perron, pas sa loi |
| 4.7, K4 | le corps F_q, q = 2 à 9 | q(q + 1)/2 pour q pair ; + (q − 1)/2 points triples pour q impair | la moitié vient de Bonferroni (fiche 019) |
| 4.8 et 4.9, K6 | le seuil du masque (sans seuil, puis 0,001 à 0,40) | pas d'ordre de dessin ni de repli signé ; le centre glisse de 0,044 à 27 px ; la moitié reste à 49,3–49,7 % | la couleur déplace le centre par le poids et par le seuil (fiche 018) |
| 4.10 | six énoncés des dossiers | dérangements, Φ₆(10) = 7 × 13, lemme des chiffres, arbre de Perron 43/108, loi de l'écart des presque-entiers de Heegner, critère du centre de la fiche 011 : vérifiés | ils peuvent être cités sans (A) |
| 4.11 | le score du modèle de défocalisation contre un prédicteur constant | 71 rayons sur 76 contre 70 | le « 93 % » de la partie XXX est le taux de base (dossier lumière) |
| 4.12 | la palette, puis l'ordre de dessin, d'un Venn à 13 courbes repeint ; le seuil sur son PNG | G·H₁ prédit l'écart sans paramètre libre ; l'ordre ne compte presque pas ; un seuil n'agit que sur une grandeur qui varie d'une courbe à l'autre | la cause du centre de la lumière est établie par une intervention (dossier méthode) |
| T8 (dossier méthode, (A)) | le nerf v1 contre la carte des connexions, sur les paires de parties non reliées | ρ(Adamic–Adar, dossiers partagés) = −0,035 (p = 0,65) ; les deux méthodes ne sont pas indépendantes (rapport des chances 1,69, p = 0,024) | pas de signal, ni en v1 ni en v2 (ρ = +0,090, p = 0,23). Et le prédicteur de la partie XXVII n'est validé que par les liens qu'il a fait chercher : sans eux, p = 0,28 |

## 8. Les erreurs trouvées dans les chaînes de production

C'est la partie de ton sujet d'étude qui se mesure le mieux : des erreurs qui s'accumulent d'une partie à l'autre parce qu'une phrase reste après sa correction, ou parce qu'un choix devient un fait.

**Corrigées par la révision, après vérification :**

| où | l'erreur | signalée par | la correction |
|---|---|---|---|
| XXX § 1.1 | la palette du traceur (L = 0,58) attribuée à l'image, dont les courbes vont de 0,60 à 0,71 | dossier grain | l'image garde les teintes, pas la clarté ; son code de rendu n'est pas publié |
| XXIX § 1.2 | « le programme du dépôt » présenté comme celui qui a rendu l'image | dossier grain | c'est une lecture : le README ne le dit pas |
| XI (script et résultats) | « 222,5° est un arrondi », resté après la correction de la partie XII | dossier bases | 222,5° = 89/144 de tour exactement |
| XVIII § 8 | une phrase corrigée par XIX § 1, sans renvoi | dossier bases | renvoi ajouté |
| XIX § 4 (script, résultats, texte) | deux longueurs « aux dénominateurs des réduites » seulement | dossier bases | tous les N = m·q_k + q_(k−1) (recalculé : 2, 3, 4, 7, 10, 13, 23, …, 93, 103) |
| XXIII § 1 | 0,6668 et 0,6661 en 10⁶ et 10⁷ dimensions | dossier corde | du bruit de double précision : la série exacte donne 0,66666 et 0,666666 |
| XIV § 5 et XXVII § 9 | la moitié de Kakeya fini expliquée par les carrés | plan (K4), test T5 | elle vient de l'inclusion–exclusion ; la piste XIV–XX se ferme |
| XXX (En bref et § 6.3), CLAUDE.md § 6 | « 93 % des signes en accord » avec la défocalisation | dossier lumière | c'est le taux de base : 71 rayons sur 76, contre 70 pour un prédicteur constant (§ 4.11) |
| XXVIII, En bref | « la formule 2/(k + 2) … démontrée pour tout k », sans dire laquelle | dossier aiguilles | précisé : c'est l'aire des arbres télescopiques ; l'arbre optimal fait mieux dès 8 branches (§ 2.6 de la partie) |
| XXX, figure ae3 (panneau d) et résultats § 6 | le « 93 % » répété sans son taux de base | dossiers lumière et méthode | la légende et la ligne de résultats donnent le taux de base : « positif partout » fait 92 % (script de la partie XXX relancé) |
| XXX (En bref, § 7.2, figure ae3 panneau f), CLAUDE.md § 10 | « la précision poussée et la variation du paramètre ne se trompent jamais » | dossier méthode | précisé, après lecture du script : la précision ne peut que confirmer ou s'abstenir, et trois verdicts de la variation (C1, C2, E4) sont posés à la main. La table du § 10 reste juste comme pratique |
| CLAUDE.md § 6 (partie XXVIII) | « minimum 2/(k + 2) » lu comme l'aire minimale | dossier aiguilles | c'est le minimum d'une borne ; l'aire exacte descend à 43/108 < 2/5 pour k = 3 (§ 4.10). La partie V l'avait trouvé en nombres (0,3981482) ; le dossier en reconnaît les fractions, 7/9, 25/42 et 43/50 |

**Signalées, pas encore corrigées** (à vérifier une à une à la prochaine révision ; le dossier qui les signale donne la preuve) :
- *Fiche 010.* « Chaque anneau du bord » n'est exact que pour le cercle du bord : la part monte quand on rentre (dossiers corde et moitiés). La fiche est corrigée dans son texte ; les valeurs par niveau sont à refaire avec le certificat.
- *Partie XXIII, figure x1, panneau e.* « Sphère » au lieu de « boule » : les nombres sont ceux de la tranche de la boule (dossier corde).
- *Parties I, XX, XXII et XXV.* α_n désigne deux angles différents, et β a aussi deux sens (dossier corde).
- *Partie XVI, § 2.* « La même proximité » : celle de δ est 46 fois plus étroite que celle de μ (dossier corde, (A)).
- *README, § 9.* En 1984, la revue de Fraser s'appelait *The Two-Year College Mathematics Journal*, et le doi n'est pas confirmé (dossier corde, à vérifier).
- *Partie V, § 3.* L'aire ½ de Perron vaut pour deux rapports égaux. Avec deux rapports indépendants, elle vaut ½ sur tout un segment (dossier moitiés, (A)).
- *Parties XXIX, § 2.3 et § 5.2, et XXX, § 2.5.* « Je ne sais pas lequel des quatre certificats il dessine » devient plus loin un fait : un choix qui devient une donnée (dossier grain).
- *Partie XXIX, § 4.* Le tableau « ce que coûte 1 ppm » mêle des longueurs et des aires (dossier grain). De même, « un bit par pas » est un bit de largeur pour Perron et un bit d'aire pour le Venn.
- *Parties XXIII et XXIV.* Le plan de la lentille s'écrit n = 1/ε − 1 dans l'une et n + 4/3 = 1/ε dans l'autre : les deux sont justes à leur ordre (le 1/3 est le ménisque). À écrire une seule fois (dossier grain).
- *Partie XXVIII, § 3.5.* « 2^(k−j) fentes de largeur 2^j » : pour j = 0, la largeur vaut v et non 1 (dossier aiguilles ; imprécision mineure).
- *Parties X, XVII, XIX et XXVIII.* Les sections des scripts et des résultats ne suivent pas la numérotation du document (XIX § 2 = section 1 des résultats, par exemple). Le champ « script » des fiches doit donner les deux (dossier aiguilles).
- *Partie XVIII, § 4.* La loi des 8R devient exacte en 8⌊R + ½⌋ au milieu d'un pixel et 8⌊r⌋ + 4 au coin de quatre pixels (dossier grain, (A)).
- *Fiche 014.* La phrase « (−2)^(3/2) ≡ −i modulo 3 » réunit 2^(3/2) (≡ −i dans F₉) et (−2)^(3/2) (= ±1 dans F₉). La fiche le signalait déjà ; c'est à te demander (dossier bases).
- *Partie XIV, § 6.* « Son produit par log₂ n reste vers 2,8 » : il culmine à 2,83 puis baisse à 2,57 (dossier aiguilles, (A)).
- *Parties V, X, XIV, XXVI et XXVIII.* « Córdoba (1977) » désigne deux articles différents, la fonction maximale (*Amer. J. Math.*) et le multiplicateur du polygone (*Ann. of Math.*) (dossier aiguilles).
- *Partie XXX, Sources.* Le titre donné pour Wielen (1996) n'est pas celui de l'article de *A&A* 314 (dossier lumière, à vérifier sur ADS).
- *README, § 7.* « Analogies, pas équivalences… ne prouvent rien » contredit le § 1 de CLAUDE.md : à réécrire en trois temps, partagé, transporté, ouvert (dossier lumière).
- *Partie VIII, § 7.* La symétrie des deux foyers vaut pour tout masque ; la récurrence de Fibonacci dit où ils tombent, pas qu'ils sont symétriques (dossier lumière).
- *Partie XVIII, § 7.* Le Nikon D800E n'ôte pas la lame passe-bas, il en annule l'effet par une seconde lame (dossier lumière, à vérifier).
- *Partie VI, § 3 bis, et figure f2 (panneau b).* « δ₂ ≈ δ₃ : c'est le hasard ». Le calcul qui juge la fiche 002 donne ici 1,7·10⁻⁴ pour une racine tirée au hasard (de l'ordre de 10⁻³ avec la marge d'essais), contre 0,61 pour la fiche 002. Le statut juste est « ouvert » (dossiers méthode et corde).
- *Partie XXIX, § 5.5.* « ppm » y désigne la valeur absolue du logarithme du rapport ; ailleurs, c'est l'écart relatif (2 852 contre 2 856 pour la fiche 003) (dossier méthode).
- *Partie XXVII, § 1.3.* Le prédicteur d'Adamic–Adar n'est validé que par les liens qu'il a fait chercher : 4 des 11 liens établis sont dans ses 15 premiers rangs, que l'auteur a cherchés d'abord. Sans eux, les 7 autres ne font pas mieux que le hasard (p = 0,28) (dossier méthode, (A)).
- *Partie XXIX, § 5.3.* « Épaisseur constante » du gel repose sur une ligne par taille, et « pas de cercle arctique macroscopique » compare un poids binomial à une aire : la couche gelée est mince en poids et en dessin, pas en rangs (20 à 33 % des rangs) (dossier ombres).
- *Partie XXIX, § 2.2.* « La texture ne dépend presque pas de n » vaut de 11 à 19 courbes ; à 23, les cinq comptes publiés (35,01 à 35,18 % de triangles) sont sous toutes les valeurs à 17 et 19 (dossier ombres).
- *Partie XXX, § 3 et § 9.* Un Venn simple à 17 courbes, symétrique et symétrique par le complément, n'existe pas au sens fort (l'obstruction de parité, § 6) ; à 19 courbes, la question reste entière (dossier ombres).
- *Le facteur d'essais de Bonferroni* (1 240, parties XXIX et XXX) compte les comparaisons faites, pas les formules possibles (VI § 4 : 10 × 1 000 × 12 par grandeur). C'est un choix de cadre, à écrire (dossier méthode).

## 9. Les trous dans les données publiées, et où chercher

Chaque dossier a son tableau (§ 6.3), avec des références marquées « sûre » ou « à vérifier ». Les pistes les plus nettes :

| piste | ce que le corpus observe | ce qui manque ailleurs | où chercher |
|---|---|---|---|
| le rendu des images de Venn | le centre et la lumière dépendent de la palette, du seuil et de l'anticrénelage | le programme, la palette, l'ordre de dessin et l'espace de mélange des PNG à 17 courbes ne sont pas publiés | une demande à l'auteur ; l'archive Zenodo (v1.3) ; une règle de publication des images de données |
| les centroïdes au-dessus d'un seuil | pour N sources colorées en symétrie d'ordre N, le seuil déplace le centre sans toucher au rayon | aucune étude connue de ce cas (à vérifier) | l'astrométrie des étoiles non résolues, les corrections de chromaticité (Gaia) ; SExtractor |
| les premiers par position | la dérive des 16 motifs de dizaine, le lien entre le dernier chiffre et le nombre d'or, la course à chaque premier | les tables publient π(10ⁿ ; 10, a) et les quadruplets, pas les 16 motifs ni leur loi de dérive (à vérifier) | OEIS A073505 à A073508 ; Lemke Oliver et Soundararajan (2016) ; Hardy et Littlewood (1923) |
| la corde en dimension n | le développement 2n/(n + 1) + 2/(3n²) − 98/(15n³) + …, divergent en 2/ln 2 | aucune source atteinte ne le donne (Fraser et Meyerson, 1984, non relus) | Fraser (1984) ; Meyerson (1984) ; la Mathematical Gazette |
| Kakeya fini, q pair | le minimum q(q + 1)/2, calculé pour q = 2, 4, 8 | la publication qui le démontre (une duale d'hyperovale, d'après des résumés ; à vérifier) | Blokhuis et Mazzocca (2008) ; Blokhuis, De Boeck, Mazzocca et Storme (2014) |
| Midy et la tour 2-adique | les aires 1/3, 1/3, 1/6, 1/12 en base 10 | pas de table de la tour par base, ni de lien explicite avec le i (à vérifier) | Hasse (1966) ; Moree (2005, 2012) |
| les arbres de Perron optimaux | l'aire exacte d'un arbre à 8 branches descend à 43/108, sous la famille télescopique (la partie V l'avait trouvé en nombres, 0,3981 ; minimum local, pas prouvé global) | pas de table publiée des rapports optimaux, ni de la constante de Kakeya au grain δ (entre π/2 et π·ln 2) ; la constante 3D de Wang et Zahl non calculée (à vérifier) | Schoenberg (1962) ; Keich (1999) ; Wang et Zahl (2025) |
| le déplacement induit par la couleur | le centre de N sources colorées en symétrie d'ordre N dépend du poids et du seuil | les catalogues à source unique rangent ce déplacement dans le bruit ou dans le point zéro (à tester) | les solutions astrométriques de Gaia pour les étoiles non résolues |
| un banc d'essai à vérités indépendantes | les presque-entiers de Heegner suivent la loi de l'écart −196 884·e^(−π√d) (rapport 0,9999 à 1 pour d = 19, 43, 67, 163, vérifié) ; e^π − π ≈ 20 (4,5·10⁻⁵) et π⁴ + π⁵ ≈ e⁶ (4,4·10⁻⁸) n'ont pas de mécanisme connu | pas de liste publique de relations de nature démontrée et de presque-entiers sans mécanisme, pour juger les tests eux-mêmes (dossier méthode) | Cox, *Primes of the Form x² + ny²* (1989) ; Diaconis et Mosteller (1989) |
| un Venn antipodal | la parité exclut à 17 courbes un Venn simple dont le complément est une symétrie ; elle ne l'exclut pas à 19 et 23 | aucun texte du dépôt de Dzoba n'en parle. La notion voisine de Venn « à symétrie polaire » est un demi-tour, que la parité n'exclut pas : elle existe à 3, 5 et 7 courbes, et aucun cas ne serait connu à 11 (bilan, § 3, à vérifier). Le cas antipodal ne semble pas étudié | Ruskey et Weston, *A survey of Venn diagrams* (DS5) ; Grünbaum (1975) ; Henderson (1963) |
| les certificats à 23 courbes | la part des triangles dérive (35,95 ; 35,76 ; 35,12 %) ; le premier rang non monotone vaut 2 ou 3 de 11 à 19 courbes | publiés (six fois 889 Mo) mais lus nulle part : k₁, les croisements par niveau, l'histogramme des degrés ; les droites au hasard donnent 2 − π²/6 = 35,51 % de triangles (Miles, à vérifier) | l'archive Zenodo du dépôt de Dzoba ; Miles (1964) |
| les tests de coïncidences | la loi de l'écart tranche ce que les tests à tolérance déclarent « hasard » | on corrige pour le nombre d'essais, on fait rarement varier le paramètre (à vérifier sur quelques analyses publiées) | Gross et Vitells (2010) ; Gelman et Loken (2014) |

**Le cadre qui conceptualise ces liens** (plan, § 6.3) :
- les faisceaux et leurs obstructions (Abramsky et Brandenburger, 2011) : des données locales cohérentes deux à deux, qui ne se recollent pas en une donnée globale ;
- le nerf et sa persistance (Borsuk, 1948 ; Carlsson, 2009) ;
- la cause commune de Reichenbach (1956), qui est le triangle du bas de l'arbre de Perron ;
- l'intervention de Pearl (2009) : refaire l'essai en ne changeant qu'une chose, comme la fiche 007 et le test T4.

## 10. Ce qui change dans le recueil

- **Les fiches 001 à 015** sont marquées « révisé : 001 ». Leur dimension principale reste la même. Les dimensions voisines confirmées par les dossiers y sont ajoutées, avec les verdicts des tests.
- **Les nouvelles fiches, nées pendant la révision** (non révisées) :
  - 016 : la classification naïve est un simplexe, et Thalès la relie à la chèvre ;
  - 017 : le cadre fabrique des liens ;
  - 018 : le seuil déplace le centre de la lumière, pas la moitié ;
  - 019 : la moitié de Kakeya fini vient de Bonferroni ;
  - 020 : le seuil des 13 courbes est isopérimétrique ;
  - 021 : les dizaines de premiers croisent π puis 2√2.
- **Les fiches proposées par les dossiers** : 64, chacune avec son type, son script et sa section ; elles sont classées par dimension dans la vérification croisée (§ 7). Elles restent dans les dossiers (§ 6.1 de chacun). On les écrira quand une partie les reprendra, pour ne pas remplir la pile sans les vérifier. Les plus fortes :
  - les dérangements du ménisque (corde) ;
  - la chèvre plane dans la série de la chèvre infinie (corde) ;
  - les trois gestes qui fixent R/√2 (moitiés) ;
  - le lemme des chiffres et Φ₆(10) (bases) ;
  - le dernier chiffre et le nombre d'or (bases) ;
  - la loi des 8R exacte (grain) ;
  - les quatre variables cachées de l'image (grain) ;
  - la demi-case, un seul procédé pour l'or, l'argent, Farey, Pick et l'hexagone (aiguilles) ;
  - Kakeya lit les chiffres du grain : 1/aire gagne entre 1,057 et 1,466 par décade (aiguilles) ;
  - la forme de Newton x·x′ = c, cinq fois (lumière) ;
  - le ppm d'un passage par 1 est uniforme : les 845 ppm de la fiche 002 sont au rang 0,6 (lumière).
  - pas de Venn antipodal à 17 courbes : l'obstruction de parité (ombres) ;
  - la face de la fiche 015 est une fibre, et 3 est le seul premier qui coupe deux coordonnées (ombres) ;
  - les périodes de Gauss du 17-gone sont des ombres Σωⁱ (ombres) ;
  - le nerf ne lit l'espace que si les intersections sont contractiles (ombres) ;
  - le banc d'essai : six cas non triviaux, et un « 10/10 » en partie posé à la main (méthode) ;
  - le nombre de liens apparents dépend du classement, de 0 à 21 (méthode) ;
  - l'intervention sur un Venn à 13 courbes de palette connue (méthode).

## Le tri

**Exact (vérifié par le script)**
- d² + c² = 4 ; l'arête √(2K/(K − 1)) et la corde √(2(K − 2)/(K − 1)) du simplexe centré ; la corde de la chèvre égale à c_K pour K = 1 + 1/x₀.
- La règle des faux liens p_a + p_b < Σp².
- Le minimum de Kakeya dans F_q pour q = 2 à 9, et l'identité q(q + 1)/2 + Σ C(m_P − 1, 2).
- W_c/W_r = √(n/(4π)) ; les seuils 4π et π/arctan(1/4).
- La famille q² + 1, le lemme des chiffres (q ≤ 30), Φ₆(10) = 7 × 13, E[(1 − E)^j] = (−1)^j·!j.
- L'aire 43/108 de l'arbre de Perron à 8 branches de rapports 7/9, 25/42 et 43/50 (la partie V l'avait trouvée en nombres).
- T3 : l'obstruction à l'ordre 4 ; T7 : les deux fenêtres de bases.

**Calculé (vérifié par le script)**
- La dérive des dizaines (10⁴ à 10⁸) et le rapport 2 des paires larges.
- La tour 2-adique des périodes.
- Le balayage du seuil, la moitié robuste et le test de l'ordre de dessin.
- Le nerf v1 et le nerf v2, leurs triangles vides et leur nul (reproductible : le nul trie ses éléments avant de les mélanger).
- Le « 93 % » de la partie XXX contre un prédicteur constant : 71 rayons sur 76 contre 70.

**Analogie de structure (même procédé), donc un résultat**
- La diagonale √2 des révisions et la corde √2 de la chèvre (Thalès).
- La moitié de Kakeya fini et la correction de Bonferroni de la fiche 012 : tronquer l'inclusion–exclusion.
- Le seuil du centre du Venn et le polygone circonscrit de la fiche 003 : la constante isopérimétrique.
- Le photocentre des étoiles doubles et le centre de la lumière du Venn : le même barycentre pesé, G·H₁(poids). Il est confirmé sans paramètre libre sur un Venn à 13 courbes de palette connue (dossier méthode ; vérifié, § 4.12).
- La face de la fiche 015 et la limite 2 de la fiche 021 : le même premier 3, qui divise 6 = 7 − 1 = 9 − 3 (dossier ombres, (A)).
- Les périodes de Gauss du 17-gone et l'ombre Σωⁱ du cube : la conjugaison de Galois agit sur les ombres (dossier ombres, (A)).
- Midy et un arbre de Perron : ce qui est partagé exactement, c'est la division binaire à chaque étage. Rien de plus ne se transporte : la loi de Perron, 2/(k + 2), n'a pas d'équivalent dans la tour, dont la queue géométrique est celle de toute valuation 2-adique (dossier méthode). Ouvert : ta lecture en Venn ascendant et descendant.

**Mes lectures (corrige-moi si je t'ai mal compris)**
- Mesurer « la diagonale √2 qui s'affirme » par le simplexe centré et par l'arête de la classification naïve. C'est une définition que je propose ; elle colle à ta phrase, mais tu avais peut-être autre chose en tête.
- Lire « l'étude cohomologique de congruences » comme le nerf du recouvrement par les dossiers, avec ses triangles vides comme trous. Le dossier ombres en fixe la limite : sans intersections contractiles, le nerf décrit le classement, pas la forme du corpus.
- Placer chaque arbre « en Perron » dans un disque précis (figure, panneau b) : le placement est fait à la main.

**Ouvert**
- La cavité du nerf v2 avec les parties (b₂ = 1, p = 0,047) : à revoir à la révision 002, avec un classement fixé avant le calcul.
- T8 en v2, et le test prospectif du prédicteur de la partie XXVII : geler son classement et compter, aux révisions suivantes, les liens établis dans ses premiers rangs (dossier méthode).
- La cause de la fiche 005.
- La palette réelle de l'image à 17 courbes. L'intervention est faite sur un système modèle (le Venn à 13 courbes du traceur, dossier méthode) ; sur l'image elle-même, il faudrait le code de rendu de Dzoba.
- Un banc d'essai à vérités indépendantes, avec plus de cas négatifs.
- δ₂ ≈ δ₃ (1,7·10⁻⁴ pour une racine au hasard : ouvert, pas « hasard »).
- Un Venn antipodal à 19 ou 23 courbes. C'est le premier « ouvert » de la partie XXX : la révision le ferme à 17 courbes (au sens fort), pas à 19.
- Trois autres « ouverts » de la partie XXX, qu'aucun dossier n'a testés (relevés par l'agent de fin d'arc) : une théorie exacte de l'inversion par défocalisation pour des arcs courbes ; les 17 couleurs comme 17 motifs structurés, pour dépasser le facteur 2 ; le dessin sphérique « naturel » dont la pression serait la projection de Lambert.
- Le premier rang non monotone à 23 courbes : 2 ou 3 si l'épaisseur du gel est constante, 4 si elle croît avec n.
- La cause commune du logarithme (K7).
- Le lien entre la chèvre et les réseaux records.

**Pas établi**
- Les énoncés marqués (A) : ils sont dans les dossiers, avec leur code, mais pas encore refaits par le script de la révision.
- Le rapprochement des trois 4/3 : c'est une coïncidence de petits entiers.

## Sources

- Les huit dossiers : chacun a ses références, classées « sûre » ou « à vérifier » (§ 6.3).
- K. Pearson, « On a form of spurious correlation which may arise when indices are used in the measurement of organs », *Proc. R. Soc. Lond.* 60, 489–498 (1897).
- F. Chayes, « On correlation between variables of constant sum », *J. Geophys. Res.* 65, 4185–4193 (1960).
- J. Aitchison, *The Statistical Analysis of Compositional Data*, Chapman & Hall (1986).
- P. Legendre, L. Legendre, *Numerical Ecology*, 3e éd., Elsevier (2012) : le problème des doubles zéros.
- E. Bertin, S. Arnouts, « SExtractor: Software for source extraction », *A&AS* 117, 393–404 (1996).
- A. Blokhuis, F. Mazzocca, « The finite field Kakeya problem », dans *Building Bridges*, Bolyai Society Mathematical Studies 19, 205–218 (2008).
- C. E. Bonferroni, « Teoria statistica delle classi e calcolo delle probabilità » (1936) ; J. Galambos, I. Simonelli, *Bonferroni-type Inequalities with Applications*, Springer (1996).
- G. H. Hardy, J. E. Littlewood, « Some problems of “Partitio numerorum” III », *Acta Math.* 44, 1–70 (1923).
- H. Hasse, « Über die Dichte der Primzahlen p, für die eine vorgegebene ganzrationale Zahl a ≠ 0 von gerader bzw. ungerader Ordnung mod. p ist », *Math. Annalen* 166, 19–23 (1966).
- M. Rubinstein, P. Sarnak, « Chebyshev's bias », *Experimental Mathematics* 3, 173–197 (1994) ; R. J. Lemke Oliver, K. Soundararajan, « Unexpected biases in the distribution of consecutive primes », *PNAS* 113, E4446–E4454 (2016).
- E. Gross, O. Vitells, « Trial factors for the look elsewhere effect in high energy physics », *Eur. Phys. J. C* 70, 525–530 (2010).
- S. Abramsky, A. Brandenburger, « The sheaf-theoretic structure of non-locality and contextuality », *New J. Phys.* 13, 113036 (2011).
- G. Carlsson, « Topology and data », *Bull. AMS* 46, 255–308 (2009).
- N. J. Gotelli, « Null model analysis of species co-occurrence patterns », *Ecology* 81, 2606–2621 (2000) ; G. Strona et al., la méthode « curveball », *Nature Communications* 5, 4114 (2014) (à vérifier).
- H. Reichenbach, *The Direction of Time*, University of California Press (1956) ; J. Pearl, *Causality*, 2e éd., Cambridge University Press (2009).
- A. Gelman, E. Loken, « The statistical crisis in science », *American Scientist* 102, 460–465 (2014) : le jardin des chemins qui bifurquent.
- P. Diaconis, F. Mosteller, « Methods for studying coincidences », *J. Amer. Statist. Assoc.* 84, 853–861 (1989) ; D. A. Cox, *Primes of the Form x² + ny²*, Wiley (1989).
- L. A. Adamic, E. Adar, « Friends and neighbors on the Web », *Social Networks* 25, 211–230 (2003).
- K. Borsuk, « On the imbedding of systems of compacta in simplicial complexes », *Fund. Math.* 35, 217–234 (1948) ; A. Hatcher, *Algebraic Topology*, Cambridge University Press (2002), corollaire 4G.3 : le théorème du nerf.
- D. W. Henderson, « Venn diagrams for more than four classes », *Amer. Math. Monthly* 70, 424–426 (1963) ; F. Ruskey, M. Weston, « A survey of Venn diagrams », *Electron. J. Combin.*, Dynamic Survey DS5.
- R. E. Miles, « Random polygons determined by random lines in a plane », *PNAS* 52, 901–907 (1964) (à vérifier).
