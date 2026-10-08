# Le grain, les pixels et les centres : ce que peut trancher un grain fini

*Dossier de la révision 001, agent `grain` (phase 1). Écrit le 2026-10-08. Le plan est dans `recueil/revisions/plan-001.md` (§ 1.4 et § 5.2.4).*

## Pour lire ce dossier

- **Statuts.** *Démontré* : la preuve est dans le corpus, ou je l'ai refaite. *Calculé* : un script donne le nombre, exact ou numérique. *Mesuré* : lu sur une donnée, avec un grain. *Classique* : résultat publié. *Ma lecture* : une interprétation de l'agent. *Ouvert* : on ne sait pas.
- **Marques.** **(R)** : résultat du dépôt, avec son fichier de `resultats/` et sa section. **(A)** : calculé par l'agent, hors dépôt, dans un dossier temporaire ; à refaire dans `scripts/revision_001.py` (le code du § 7 le fait pour T4). **(P)** : lu dans une publication ou sur un site (références au § 6.3).
- **Ce que je n'ai pas fait.** Je n'ai lancé aucun script du dépôt. Je n'ai exécuté aucun code de Dzoba : dans `/home/user/dzoba/venn17`, j'ai lu `README.md`, `plotter/plotter_svg.py` (fonctions `palette`, `write_svg`, l'export PNG et `raster_png`) et un commentaire de `paper/venn17-19.tex` ; j'ai lu les images PNG et les SVG comme des données (Pillow, numpy, scipy). Mes calculs sont dans un dossier temporaire. Le seul fichier que j'écris dans le dépôt est celui-ci.
- **Fichiers lus en plus de la liste du plan.** `bases-objets.md` § 5 (les retenues, XIX), `tiers-dimension.md` § 2 et § 5 (XXIV : la série, la lecture en longueur ou en aire), `tranche-aiguilles.md` § 1 (XXV : la troncature, Borel–Padé), `kakeya-miroir.md` § 1 (XXVI : Kakeya au grain δ), `octaedre-perron-venn.md` § 2.5 (XXVIII : la constante de Kakeya, par recherche de mots), `carte-connexions.md` § 3 (XXVII : l'échelle des taux de change), `menisque-projection.md` (XVI), la fiche 003, `resultats/revision_001.md` § 4.4, § 4.8, § 4.9 et § 5, et `scripts/revision_001.py` aux mêmes sections. Côté données externes : `plotter/venn-13-color.svg` et les PNG de `plotter/`, `images/venn13-spread.png`, `images/venn17-rose-dark-2000.png`. J'ai regardé les neuf figures de la liste du plan (j1, n2, o1, r1, r2, x1, ad1, ae1, ae3).
- **Un fait arrivé pendant mon travail.** La consigne de session disait que `scripts/revision_001.py` avait les sections 1, 2.1, 4.1 et 4.2. Il a aujourd'hui 1 366 lignes et contient aussi 4.3 à 4.9 (derniers commits : « le masque binaire, son seuil et ce que vaut 0,37 px », puis « la ligne du test T4 résume tout le balayage du seuil »). Son § 4.4 fait déjà le cas K10 (la constante isopérimétrique, 4π et π/arctan(¼)) et son § 4.8–4.9 fait déjà une première partie de T4 (classes de teinte, montée cyclique, balayage du seuil). Je ne les refais pas : je les lis, je les contrôle et je les complète (§ 3.4, § 3.5 et § 7).
- **Ce que je n'ai pas pu faire.** Je n'ai pas fait de recherche en ligne : aucun article du § 6.3 n'a été lu. Chaque référence y est marquée « sûre » (je connais l'auteur, la revue, l'année) ou « à vérifier ». Je n'ai pas non plus le code qui a rendu l'image à 17 courbes : il n'est pas dans le dépôt de Dzoba (§ 3.5).

## En bref

- **Un seul objet : le grain.** Les sept parties du plan et les cinq fiches demandent toutes ce qu'un pas fini (un pixel, un ppm, un chiffre décimal, une case de grille) laisse décider. Deux parties (XXIX, XXX) et quatre fiches (006, 007, 008, 011) reposent sur une seule image, `venn17-pressure-dark-2000.png`.
- **Trois liens forts.**
  1. *Le seuil de 13 courbes est l'inégalité isopérimétrique.* W_centre/W_reste = (a/s)·√(n/4π) exactement, avec a le pas d'arc et s le côté d'un croisement (XXX prend a = s = 2 px). Le seuil n* = 4π·(s/a)² est le point où L²/A = 4π, la constante du cercle, pour n arcs de longueur a qui enferment n cases de côté s. Le 2/π de W_centre est le rayon de confusion n/π d'une étoile de Siemens (XVIII § 6). Ce qui n'est pas une constante, c'est le choix a = s (§ 3.4).
  2. *L'ordre de dessin est écarté, et la « seconde cause » n'en est pas une.* Les PNG du traceur (13 et 11 courbes, dessinés de 0 à n − 1) donnent un contraste d'ordre C = +14,8 ± 0,7 % et +8,6 ± 0,4 % ; l'image à 17 courbes donne −6,0 ± 1,5 %, comme les témoins sans ordre (−6,4 % et −8,0 %), loin des témoins dessinés de 0 à 16 (+13,8 % à +15,9 %). Une palette presque isoluminante (Y₀ ≈ 0,30 à 0,36) redonne l'ordre des quatre pesées continues (RMS 1,4 à 2,0 px) avec un seul facteur géométrique, et fait croître l'écart des masques avec le seuil. Une palette à clarté constante prédit l'inverse pour Y (9 à 12 px au lieu de 0,61 px). K6 n'est plus une obstruction (ma lecture, § 3.5).
  3. *Le budget d'une mesure est une loi déjà démontrée.* La loi des 8R de XVIII § 4 donne le budget de la moitié du Venn : ±1 830 ppm = 4/(π·695,6)·10⁶. Les taux de change de XXIII § 4 (ε⁻², ε⁻¹, ε^(−1/2)) et du logarithme (XXVII § 3) tiennent dans un seul tableau avec les lois du Venn (1 bit par courbe), de Perron (1 bit par étage, mais seulement 2,8/log₂ n d'aire sur une grille) et des pixels (un chiffre par décade). Entre la lecture en longueur et la lecture en aire, il y a un cran : × 2 sur le plan, × √2 sur le ménisque (572,5 contre 811,6 dimensions à 1 ppm, § 3.3).
- **Trois trous.**
  1. *L'image de référence a quatre variables cachées* : le certificat qu'elle dessine, sa mise en page (le TeX de Dzoba oppose « pressure » et « Tutte »), sa palette (mesurée à L ≥ 0,63 ; le traceur a L = 0,58 par défaut) et son ordre de dessin. Le code qui a rendu les PNG à 17 courbes n'est pas publié. XXIX § 1.2 et § 5.2 et XXX § 1.1 en traitent plusieurs comme connues.
  2. *Le logarithme n'a pas de cause commune.* La série de la chèvre le doit à la singularité en −ln √2 (une troncature) ; Perron, le Venn et les pixels le doivent à un grain fini. K7 les recolle « modulo un cran » ; la raison commune est ouverte.
  3. *Les constantes des plafonds sont ouvertes* : Perron sur une grille n × n atteint 2,8/log₂ n sans constante dérivée ; Kakeya au grain δ reste entre π/2 et π·ln 2 (XXVIII § 2.5).
- **Corrections au recouvrement** : ajouter les parties XXIV, XXV, XXVI et XXVII (elles portent les lignes « logarithme » et la lecture longueur/aire du tableau) et la fiche 003 (la quantité n·tan(π/n) de K10) ; ne rien retirer (§ 8).

---

## 1. La question directrice et la projection sur D1–D8

### 1.1 La question

*Que peut trancher un grain fini (un pixel, un ppm, un chiffre, une case de grille) ? À quel taux le grain s'échange-t-il contre des dimensions, des courbes ou des étages ?* (plan, § 1.4)

Je la reformule en deux temps. Une mesure a un grain, et ce qu'on veut décider a une taille : un ménisque de 0,35 %, une moitié à ±1 830 ppm, un ordre de dessin, un lien de structure à 2 856 ppm. La décision tient au rapport entre les deux. Et chaque objet du corpus (la boule, la série, Perron, le Venn) a sa loi pour dire combien de pas il faut pour passer sous un grain donné.

### 1.2 La réponse en bref (ma lecture, appuyée sur XVIII § 4, XXIII § 4, XXVII § 3 et XXX § 6.4)

1. **Un grain tranche ce qui est plus grand que lui.** En dessous, il ne laisse voir que des moments : la lumière, puis l'étalement (ρ²/4 pour un disque), puis la forme au quatrième ordre (X § 2). Un point et un disque s'écartent comme (ρ/σ)², un carré de côté √3·ρ et un disque comme (ρ/σ)⁴.
2. **Il fait deux exceptions : l'aire et la moitié.** Les pixels entièrement dedans et ceux qui touchent enferment le disque, avec un écart de 8R exactement (XVIII § 4). La moitié, elle, ne bouge pas quand le centre ou le seuil bougent : 49,3 à 49,7 % de l'encre dans le contour réduit de 1/√2 pour t = 0,005 à 0,3, alors que l'encre passe de 81 à 19 % (R : `revision_001.md` § 4.9). La longueur n'est jamais certaine : l'escalier mesure 8R − 4, pas 2πR (« π = 4 »).
3. **Il s'échange contre les pas par deux familles de lois.** Pour les objets de *concentration* (les boules, XXIII § 4), des puissances de 1/ε : ε⁻², ε⁻¹, ε^(−1/2). Pour les objets de *doublement* (le Venn, Perron, la série de la chèvre, Kakeya), un logarithme : un bit par courbe ou par étage, un demi-bit en longueur (XXVII § 3, XXIX § 4).
4. **Entre longueur et aire, il y a un cran.** Un même grain lu en aire vaut deux fois le grain lu en longueur : le tableau de XXIX § 4 mêle les deux lectures (plan en longueur, ménisque en aire) et la partie XXIV § 5 dit que les deux sont vraies à la fois (§ 3.3).
5. **Pour une image, le grain a deux parts : le pixel et la pesée.** Le centre de symétrie est connu à 0,003 px. Le centre de la lumière dépend de la pesée, de 0,61 à 46 px : de 200 à 15 000 fois le grain du centre. Le pixel fixe la précision, la pesée décide du résultat (fiche 006).
6. **Une chaîne qui part d'un point biaisé ou d'une fenêtre trop étroite fabrique un résultat précis et faux** (fiche 007). Elle se retrouve dans douze chaînes du corpus, dont trois sont encore ouvertes (§ 3.6).

### 1.3 La projection sur D1–D8 (ma lecture)

Le plan donne D3 0,7 ; D4 0,1 ; D5 0,1 ; D7 0,1 (§ 1.10). Après lecture, je baisse D3 et je lui retire du poids au profit de D7 (la moitié du travail du dossier porte sur la chaîne de production d'une image), de D1 (les taux de change sont des lois de la chèvre) et de trois dimensions que le plan laissait vides.

| dimension | plan | ma lecture | ce qui la porte |
|---|---:|---:|---|
| D1 la chèvre et les cordes | 0 | 0,07 | les boules et leurs taux de change (XXIII § 4), le ménisque de 0,35 % vu par la grille (XV § 3), le cran de la corde |
| D2 bases, chiffres, congruences | 0 | 0,03 | un chiffre certain par décade (XVIII § 4), 2⁻ⁿ = 5ⁿ/10ⁿ (fiche 001), le ménisque qui entre au chiffre 2k + 1 (XXIII § 3) |
| **D3 grain, pixels, précision** | 0,7 | **0,50** | le budget (px, ppm, chiffres), le centre (fiches 006, 008, 011), la loi des 8R, la grille (XV, XVIII) |
| D4 optique et diffraction | 0,1 | 0,10 | ce que le flou laisse voir (X § 2), le rayon de confusion n/π d'une étoile de Siemens (XVIII § 6, XXX § 6.3), le pixel qui intègre (XVIII § 7), le diaphragme (XXX § 2.2) |
| D5 Kakeya, Perron, aiguilles | 0,1 | 0,08 | Perron sur une grille n × n (XIV § 6), Kakeya au grain δ (XXVI § 1, XXIX § 4) |
| D6 sphères, cubes, Venn, symétries | 0 | 0,05 | les comptes du Venn au ppm (XXIX § 2), la moitié des 18 certificats (XXX § 2.5), les polygones de K10 |
| **D7 hasard et méthode** | 0,1 | **0,14** | le biais propagé (fiche 007), la chaîne de production de l'image (XXIX § 1.2, XXX § 1.1), le test T4, les 1 240 comparaisons (XXIX § 5.5) |
| D8 physique | 0 | 0,03 | le photocentre des étoiles doubles et HD (fiche 006), le drizzle de Hubble (XXX § 6.1) |

Les poids font 1 (0,07 + 0,03 + 0,50 + 0,10 + 0,08 + 0,05 + 0,14 + 0,03). Pour le bloc JSON du § 1.10 du plan : `"grain-pixels-centres": {"D3": 0.50, "D7": 0.14, "D4": 0.10, "D5": 0.08, "D1": 0.07, "D6": 0.05, "D2": 0.03, "D8": 0.03}`.

### 1.4 Les notations qui se heurtent

Le dossier croise sept parties écrites à des moments différents. Les mêmes lettres y désignent des objets différents. Je les sépare ici, et je les garde séparées dans la suite.

| lettre | sens dans le corpus | sens que j'ajoute ou que je retiens |
|---|---|---|
| n | la dimension (I à XXIV) ; le nombre de courbes (XXIX, XXX) ; le côté de la grille n × n (XIV § 6) | n = nombre de courbes dans les formules du Venn ; « n × n » pour une grille |
| N | le rayon du pré en mailles (XV § 3) ; le nombre de rayons d'une étoile (XVIII § 6) ; le nombre de côtés ou de lames (XXVIII, XXIX § 4) | N garde ces sens ; je l'écris avec sa partie |
| R, r | R : rayon du pré (R = 1 pour la chèvre), rayon d'un cercle en pixels (XVIII), rayon de l'image (984 px) ; r : la corde, ou un rayon | R en pixels dans XVIII et dans les budgets ; r pour la corde |
| ε, δ | ε : le grain en longueur (XXIII § 4) ; δ : le grain de Kakeya (XXVI) ; « le grain » en pixels (XXIX § 3) | ε en longueur, « grain » en pixels |
| μ | le ménisque r² − (1 + g²) : une quantité en aire (XVI, XXIII) | μ/2 : la même quantité en longueur (le plan x₀ = 1/(n + 1) − μ/2) |
| s | l'arête du simplexe s(n) (XV) | s = côté d'un croisement (K10) ; je note l'arête du simplexe « arête » |
| a | — | a = pas d'arc entre deux croisements centraux (K10) |
| W | largeur d'image en pixels (XXX § 6.4) | W_reste, W_centre |
| G, h, C | — | G : facteur géométrique complexe (bras de levier) ; h : dipôle d'un jeu de poids ; C : contraste d'ordre (T4, § 7) |
| ρ | le rayon du disque (X § 2) ; le rayon normalisé de l'image (XXX § 2) ; un coefficient de Spearman (revision_001) | ρ dans le sens de la partie citée ; « coefficient de Spearman » écrit en toutes lettres |

---

## 2. Les chaînes de production (script → résultats → figures → document)

### 2.1 Les sept chaînes, partie par partie et dans l'ordre (question 1)

Chaque ligne est un maillon : le script (section et fonction), la section de `resultats/`, le panneau de figure, la section du document, et le statut. Pour chaque partie, je dis ce que la chaîne produit et où elle est la plus fragile. Sauf mention, les chemins sont `scripts/<nom>.py`, `resultats/<nom>.md`, `figures/<fichier>.png` et le document `<nom>.md` à la racine.

#### Partie X, § 2–3 — ce qu'un flou laisse voir, et d'où viennent les centres fantômes

| maillon | script `carre_ptolemee.py` | résultats `carre_ptolemee.md` | figure `j1_carre_ptolemee` | document `carre-ptolemee.md` | statut |
|---|---|---|---|---|---|
| M1. Image floue (tache gaussienne σ) d'un point, d'un disque et d'un carré, à lumière égale ; écart maximal rapporté au maximum de l'image du disque | § 2 : `tf_disque(rho)`, `tf_carre(s)`, `image(tf)` | § 2 : six tailles, ρ/σ = 0,05 à 1,6 | panneau b | § 2 | calculé |
| M2. Pentes aux petites tailles : 2,00 (point/disque), 2,00 (carré de même aire/disque), 4,00 (carré de côté √3·ρ/disque) ; rapports π/3 = 1,0472 et 3/π = 0,9549 ; terme des coins −s⁴/120 | § 2 (régressions) | § 2 (dernières lignes) | panneau b | § 2 | démontré (moments), calculé (pentes) |
| M3. Lame de Fresnel à 55 zones, R = 36 px, sur grille carrée et hexagonale : 8 centres sur un carré de demi-côté 0,655 a, 6 sur un hexagone de rayon 0,756 a (2/√3 = 1,1547 fois plus loin) ; identité du réseau réciproque vérifiée à 3,6·10⁻¹⁴ | § 3 : `zones(x, y, R, N=55)` | § 3 | panneau c | § 3 | calculé |

- **Ce que la chaîne produit.** Une loi de visibilité : sous le flou, un petit objet ne montre que sa lumière, son étalement (moment d'ordre 2) puis sa forme (ordre 4). XVIII § 7 la reprend (« un pixel carré de côté p devient indiscernable d'un disque de rayon p/√3 ») et XXIII § 4 la cite.
- **Maillon fragile.** L'écart est une norme sup, rapportée au maximum de l'image du disque : il dépend de l'échelle de l'image. La partie ne le relie pas à la quantification à 8 bits d'un PNG (1/255 = 3 900 ppm). C'est la fiche proposée N1 (§ 6.1).
- **Un cas de biais hors de ma plage.** X § 1 (le « trou » : le seuil « cercle de rayon > 3 » et le point P tiré au hasard) est le premier maillon biaisé du corpus (§ 3.6, ligne 1).

#### Partie XIV, § 6 — l'arbre de Perron sur une grille

| maillon | script `aiguille_grille.py` | résultats `aiguille_grille.md` | figure `n2_perron_grille` | document `aiguille-grille.md` | statut |
|---|---|---|---|---|---|
| M1. Arbre à 2^k branches (aire exacte 2/(k + 2) du triangle) et cases n × n touchées, pour n = 16, 64, 256, 1024 et k = 1 à 14 | § 6 : `arbre(k_, alphas, base, ax0)`, `cases(l, r, ax, n, garder)` | § 6 (premier tableau) | panneaux a, b, c | § 6 | calculé |
| M2. Meilleur arbre par grille : k = 2, 4, 5, 7 (4, 16, 32, 128 branches) ; part minimale 0,622 ; 0,463 ; 0,353 ; 0,275 ; produit par log₂ n : 2,49 ; 2,78 ; 2,83 ; 2,75 | § 6 | § 6 (second tableau) | panneau c (cercles) | § 6 | calculé |
| M3. L'ordre 1/log n ne peut pas être battu (Córdoba, 1977) et il est atteint (Keich, 1999) | — | — | — | § 6 | classique |

- **Ce que la chaîne produit.** Un plafond : au-delà du meilleur arbre, l'aire remonte (1 024 branches sur la grille 64 × 64 couvrent 0,61 du triangle, contre 0,17 sans grille ; panneau b). C'est le « grain plafonne la profondeur » de l'arbre P5.
- **Maillon fragile.** Une seule famille d'arbres (les rapports télescopiques de la partie V), une grille alignée sur la base du triangle, quatre points pour dire que le produit « reste vers 2,8 ». Le meilleur nombre de branches est une puissance de 2 : n/4, n/4, n/8, n/8 (A). Aucune constante n'est dérivée.

#### Partie XV, § 3 — la chèvre comptée sur une grille

| maillon | script `grille_decalee.py` | résultats `grille_decalee.md` | figure `o1_grille_decalee` | document `grille-decalee.md` | statut |
|---|---|---|---|---|---|
| M1. Pré de rayon N mailles, piquet sur un point de la grille à la distance N ; corde = distance au piquet du point de rang médian, ramenée à N ; N = 3 à 300 (2D), 2 à 60 (3D) | § 3 : `chevre_comptee(pts, N, P)`, `g_carree`, `g_hex`, `g_cub`, `g_cfc` | § 3 | panneau c (nuage de points) | § 3 | calculé |
| M2. « La grille voit le ménisque » quand la corde comptée est plus près de r(n) que de l'arête du simplexe : 95 % (carrée), 98 % (décalée), 83 % (cubique), 97 % (couches décalées) des tailles ; toujours à partir de N = 41, 38, 18, 14, soit 5 261, 5 239, 24 405 et 16 295 points | § 3 (boucle `CAS`) | § 3 (tableau) | panneau c (pointillés : 0,35 % et 0,31 %) | § 3 | calculé |

- **Ce que la chaîne produit.** Le seuil d'une grille : quelques milliers de points en 2D, quelques dizaines de milliers en 3D. Le gain de la grille décalée est dans la distance offerte (§ 2 : −0,35 % de la corde, contre −13,7 % et +22,0 % pour la grille carrée), pas dans le comptage.
- **Maillon fragile.** « Toujours à partir de N » est le dernier N qui échoue, plus un : c'est un pire cas. Le nuage du panneau c s'étale sur trois décades d'écart à nombre de points égal. Un seul piquet par grille. Ma régression (A, N = 3 à 300, au-delà de 300 points) donne une pente de −0,70 (carrée) et −0,71 (décalée) pour l'erreur en fonction du nombre de points, soit R^−1,4 en rayon : la même loi que le comptage par les centres de XVIII § 5.

#### Partie XVIII, en entier — les pixels, le mod et les longitudes

| maillon | script `pixels_longitudes.py` | résultats `pixels_longitudes.md` | figure | document `pixels-longitudes.md` | statut |
|---|---|---|---|---|---|
| M1. Les huit octants du point milieu (564 pixels pour R = 100) ; coût \|cos θ\| + \|sin θ\|, moyenne 4/π | § 1 : `point_milieu(R)` | § 1 | `r1_pixels_contacts` d | § 1 | calculé |
| M2. Contact vu par l'épaisseur du trait (w = 0,021 : ±17,6° et ±7,6°) puis par les pixels (colonne verticale 2⌊√(N/√2 + 1/4)⌋ + 1) | § 2 : `anneau(cx, R, L, x0, demi)` | § 2 | `r1` a, b, c | § 2 | calculé |
| M3. Gauss : N(10⁶) = 3 141 592 649 625 ; bits de N(2^k) ; E = T + S + 2, T/√R → −1,17598 = 4√2 ζ(−1/2) | § 3 : `gauss(R)`, `communs(a, b)` | § 3 | `r1` f | § 3 | calculé, démontré (décomposition) |
| M4. Dedans/dehors : écart exactement 8R (80 à 80 000 pour R = 10 à 10⁴) ; escalier 8R − 4 ; corde par les centres (≈ R^−1,5, sans garantie) et corde certaine (largeur 4,57/R) | § 4 : `demi_largeurs`, `compte(R, mode, rho)`, `corde_centres`, `corde_certaine` | § 4 | `r1` e | § 4–5 | démontré (8R), calculé |
| M5. Latitudes et longitudes : repliement des anneaux hors de r = s²/2, des rayons en deçà de r = N/π (22,9 px pour 72 rayons) ; centres fantômes ; produit s²N/(2π) constant | §§ 5–6 : `motif(f, mode, sigma)`, `globe(x, y)` | § 5 | `r2_longitudes_lumiere` a à f | § 6 | calculé |

- **Ce que la chaîne produit.** Le budget certain d'un comptage de pixels (un chiffre par décade de R) et la loi de l'aire (exacte) contre la longueur (jamais). C'est la seule partie du dossier où une précision est *garantie*.
- **Maillon fragile.** La loi des 8R est exacte pour R entier et un centre au milieu d'un pixel (argument modulo 4 : un coin de pixel a des coordonnées demi-entières). XXX § 2.4 l'emploie pour un rayon non entier (695,6 px) et un centre au coin de quatre pixels, et trouve 5 564, « 8r à 0,6 près ». La loi exacte pour ce cas est 8⌊r⌋ + 4 = 5 564 (A, fiche proposée N2). Les « chiffres communs » de la table de Gauss sont des entiers (2, 4, 5, 6, 7, 8) : la pente de 1,3 à 1,4 chiffre par décade du texte vient de l'exposant de E(R), pas de cette colonne.

#### Partie XXIII, § 3–4 — les décimales en deux couches et les taux de change

| maillon | script `lentilles_boules_grain.py` | résultats `lentilles_boules_grain.md` | figure `x1_lentilles_boules_grain` | document `lentilles-boules-grain.md` | statut |
|---|---|---|---|---|---|
| M1. Corde exacte et ménisque : `rho2(n)`, `broute`, `part_calotte` ; cordes certifiées (`CERTIF`, n = 2, 3, 24) ; μ_n = ρ² − 2n/(n + 1) | début du script | § 1 | — | § 1 | calculé |
| M2. Projection (10ᵏ − 1)/(10ᵏ + 1) : ses décimales répètent (10ᵏ − 1)² ; le ménisque commence au chiffre 2k + 1 et entre par une retenue | § 3 (`REPET`, `ADD`) | § 3 | panneau c | § 3 | calculé |
| M3. Quatre taux de change : `n_equateur(ε)` (constante `C_EQ = 2·erfinv(0,5)²` = 0,4549), `n_coquille(ε)` (ln 2/ε), plan 1/ε − 1, `n_menisque(ε)` (1/√(3ε)) | § 4 | § 4 (tableau : ε = 10⁻¹ à 10⁻⁶ et 10⁻⁵⁰) | panneaux d, e | § 4 | démontré (lois), calculé (valeurs) |

- **Ce que la chaîne produit.** Les taux ε⁻², ε⁻¹, ε^(−1/2), avec leurs constantes, et la lecture du ménisque en chiffres : à n = 10ᵏ il faut 2k + 1 chiffres pour le voir, c'est-à-dire ε ∝ n⁻².
- **Maillon fragile.** Le ménisque est le terme principal 2/(3n²) (prouvé dans XXIV pour n ≥ 100). À 1 ppm, les trois termes suivants de XXIV déplacent n de 816,5 à 811,6 en lecture « aire » et de 577,4 à 572,5 en lecture « longueur » (A). « Le grain est une longueur » est posé comme choix, et signalé ouvert au § 7 de la partie.

#### Partie XXIX, § 1–4 — le Venn à 17 au ppm

| maillon | script `venn_ppm.py` | résultats `venn_ppm.md` | figure `ad1_venn_ppm` / `ad2_deux_ombres` | document `venn-ppm.md` | statut |
|---|---|---|---|---|---|
| M1. L'image : `ALLUME = LUM > FOND + 25` (moyenne RGB, fond 22/3) ; centre = plus grand disque vide centré sur un pixel entier, dans ±15 px autour du milieu de la boîte des pixels allumés (`TROU`) ; contour (`RMAX`, 3 600 angles) : harmoniques 17, 34, 51, 68, rayon 984 px, aire 2 956 870 px ; trou 14,4 px ; encre 60,8 % | § 1 | § 1 | ad1 a | § 1 | mesuré |
| M2. Les comptes : `STATS` par certificat (2ⁿ − 2 croisements, 2ⁿ régions, coins) ; `TEXTURE` ; niveaux (`CUM17`, `RAYON_NIV`) ; part des croisements de niveau ≥ 9 (`DEMI`) | § 2 | § 2 | ad1 b, d | § 2 | calculé |
| M3. La granularité : `remplissage(masque, tailles)` (1 à 12 px) ; veines (`VEINES`, `dim_locale(res, 3, 32)`) ; pixels par croisement (`PXC`) | § 3 | § 3 | ad1 e, f | § 3 | mesuré |
| M4. L'analyse dimensionnelle : `kakeya_haut`, `N_SERIE` (31), `PRIX` (neuf lignes) | § 4 | § 4 | ad2 a | § 4 | calculé, classique |

- **Ce que la chaîne produit.** L'unité commune : un croisement = 1/131 070 de l'aire = 7,63 ppm = 22,56 px² (côté 4,75 px) ; le remplissage (99,2 % à 3 px, 99,9 % à 4 px) ; le tableau « ce que coûte 1 ppm ».
- **Maillon fragile (quatre).** (i) « Le certificat de l'image » est c3-s2, choisi parce qu'il est vérifié en Lean (§ 6 de la partie : « je ne sais pas lequel des quatre certificats il dessine »). (ii) § 1.2 attribue à l'image les trois étapes du traceur (Tutte, orbites, anneaux à aire égale), alors que XXX § 2.3 appelle « rose » le dessin de Tutte (§ 6.2, E2). (iii) Le centre est quantifié au pixel (à 0,70 px du centre de symétrie). (iv) Le tableau du § 4 mêle la lecture en longueur (plan, équateur) et la lecture en aire (ménisque, diaphragme, Venn en aire) : § 3.3.

#### Partie XXX, § 1, 2.4 et 6 — les centres, le budget de la moitié, le goulot

| maillon | script `centre_venn.py` | résultats `centre_venn.md` | figure `ae1_centre_moitie` / `ae3_grains_hasard` | document `centre-venn.md` | statut |
|---|---|---|---|---|---|
| M1. Centre de symétrie d'ordre 17 : corrélation de la clarté OKLab avec ses rotations, pas 2 → 0,5 → 0,125 px, paraboloïde ; k = 1, 4, 8 (et 2) : (999,497 ; 999,499) à 0,003 px | § 0 : `charger`, `centre_symetrie(Lc, depart, ks, pas, sub, r0, r1)` ; § 1 | § 1 | ae1 a | § 1.1 | calculé |
| M2. Six pesées : liste `POIDS`, barycentres (`BARY`) : 0,61 ; 1,26 ; 4,51 ; 13,58 ; 33,07 ; 46,07 px ; couleurs des 17 courbes (`COUL` : les 5 % de pixels les plus clairs de chaque teinte, parmi `SAT = (Cc > 0,08) & (L > 0,3)`) et dipôles (`dipole`) : 1,6 ; 4,1 ; 9,8 ; 17,7 % | § 1 | § 1 | ae1 b | § 1.2 | mesuré |
| M3. Premier essai à 2,36 px : `centre_grossier(M, depart)` part du barycentre du masque RGB (13,6 px) | § 1 | § 1 (puce « mon premier essai ») | ae3 b (encart), c | § 1.3 | exact (refait) |
| M4. La moitié en pixels : `mesure_moitie(L, Lb, c, seuil=0,1, masque=None)` ; `N_IN`, `N_TOUCH`, `BUD_PIX`, `BUD_CROIS` : ±1 830 ppm certain, ±3 510 ppm au grain d'un croisement | § 2 | § 2 | ae1 f (bandes) | § 2.4 | calculé |
| M5. Empiler les 17 copies (`drizzle`, `incoherence`) ; harmonique 17 défocalisé (`harmo_cercle`) ; largeurs nécessaires `W_reste`, `W_centre` (`n_max`) | § 6 | § 6 | ae3 a à e | § 6.1 à 6.4 | calculé |

- **Ce que la chaîne produit.** Le centre à 0,003 px ; l'écart des pesées (200 à 15 000 fois le grain du centre) ; le budget de la moitié ; le goulot du centre (18,99 courbes à 2 000 px) ; la limite du drizzle (facteur 2 au plus).
- **Maillon fragile (quatre).** (i) Les poids des pesées sont les couleurs de pixels choisis par leur clarté : une sélection qui peut biaiser selon la teinte (§ 3.5). (ii) § 1.1 suppose la palette du traceur à L = 0,58, et § 1.2 dit en même temps qu'elle est « presque équilibrée » pour l'œil : les deux phrases ne vont pas ensemble (clarté constante n'est pas luminance constante, § 6.2). (iii) Les deux masques binaires dépendent du seuil (revision_001 § 4.8–4.9). (iv) Le modèle de W_centre suppose une orbite circulaire, des anneaux à aire égale et un critère de 2 px (§ 3.4).

### 2.2 Ce que chaque script produit

| script | durée annoncée | produit | fichier de résultats |
|---|---:|---|---|
| `carre_ptolemee.py` | ≈ 5 s | lois du flou (ρ², ρ⁴), réseau réciproque carré et hexagonal, Ptolémée, plan hyperbolique | `carre_ptolemee.md` |
| `aiguille_grille.py` | ≈ 20 s | directions de l'aiguille sur la grille, aiguilles de Fibonacci, Kakeya dans F_q, Perron sur n × n | `aiguille_grille.md` |
| `grille_decalee.py` | ≈ 20 s | la grille décalée, la corde et la maille, la chèvre comptée, les dimensions d'or | `grille_decalee.md` |
| `pixels_longitudes.py` | ≈ 15 s | octants, contacts, Gauss, 8R, corde par les centres et certaine, centres fantômes | `pixels_longitudes.md` |
| `lentilles_boules_grain.py` | ≈ 5 s | plan de la lentille, deux couches décimales, quatre taux de change, cran | `lentilles_boules_grain.md` |
| `venn_ppm.py` | ≈ 40 s (34 s lues) | image, comptes au ppm, granularité, prix de 1 ppm, ombres du cube, gelé/liquide, 1 240 comparaisons | `venn_ppm.md` |
| `centre_venn.py` | ≈ 55 s (50 s lues) | centres, six pesées, moitié, sphère, diaphragmes, diffraction, drizzle, W_centre, banc d'essai | `centre_venn.md` |
| `revision_001.py` (sections 4.4, 4.8, 4.9) | ≈ 80 s au total | K10 (4π), classes de teinte, balayage du seuil, 0,37 px | `revision_001.md` |

### 2.3 Les points faibles communs aux sept chaînes

1. **Tout passe par une image que personne n'a rendue ici.** Le PNG `venn17-pressure-dark-2000.png` est une donnée de Dzoba. Sa palette, son ordre de dessin, sa mise en page et son certificat ne sont pas documentés (§ 3.5.1). Les parties XXIX et XXX et les fiches 006, 007, 008 et 011 en héritent.
2. **Les budgets sont donnés en deux unités qui ne se comparent pas sans règle** : le ppm de l'aire (XXIX), les pixels (XXX), les chiffres (XVIII), les dimensions (XXIII). Le § 3.2 les range en un tableau.
3. **Le grain de la physique est un choix.** XXIII § 7 le laisse ouvert (longueur ou aire) et XXIV § 5 le ferme en disant que les deux lectures sont vraies. Le tableau de XXIX § 4 prend l'une ou l'autre selon la ligne (§ 3.3).
4. **Peu de lignes ont leur propre « variation du paramètre ».** Les lois de XVIII et de XXIII sont vérifiées sur plusieurs tailles. Le plafond de Perron sur grille (quatre grilles) et la chèvre comptée (un piquet par grille) n'ont qu'un échantillon étroit. Le budget du centre est exact en n, mais son modèle (orbite circulaire, 2 px) n'est comparé à aucun dessin.

---

## 3. Ce que le dossier établit, et ce qui reste ouvert

### 3.1 Ce qui est établi

- **Démontré (dans le corpus).**
  - Sous un flou, un petit objet ne montre que ses moments d'ordre 0, 2 et 4 (X § 2).
  - Entre les pixels entièrement dedans et ceux qui touchent un disque, l'écart est exactement 8R, et l'escalier mesure 8R − 4 (XVIII § 4).
  - L'écart de Gauss se coupe en E = T + S + 2 (XVIII § 3).
  - Le plan de la lentille est à x₀ = 1/(n + 1) − μ/2 (XXIII § 2).
  - Les lois de concentration ε⁻², ε⁻¹, ε^(−1/2) (XXIII § 4 ; la dernière par la preuve de XXIV).
  - Un Venn simple a 2ⁿ − 2 croisements (Euler) (XXIX § 2).
  - W_centre/W_reste = (a/s)·√(n/4π) : une identité (§ 3.4).
- **Calculé, ou dérivé et vérifié.** Les tableaux de XIV § 6, XV § 3, XVIII §§ 3 à 5, XXIII, XXIX §§ 3 et 4, XXX §§ 1, 2 et 6, et ceux de `revision_001.md` § 4.4, § 4.8 et § 4.9. Les anneaux de l'image suivent la binomiale à 17 % près (N_l/C(17, l) de 0,825 à 1,045). La série de la chèvre coupée au mieux donne 1,03·2^(−n/2)/n (XXV § 1.1 : dérivée par la méthode de Darboux, vérifiée à 10⁻⁵ près sur 40 coefficients exacts). Mes calculs (A) : K10 à 40 chiffres, le contraste d'ordre de T4, l'ajustement de la palette, la pente de la chèvre comptée, le nerf.
- **Mesuré.** Le centre de symétrie à 0,003 px ; les six pesées ; le remplissage selon le grain ; la dimension des veines ; la moitié des 18 certificats.
- **Classique.** Córdoba (1977) et Keich (1999) pour 1/log n ; Gauss, Hardy, Huxley pour l'écart du cercle ; le drizzle (Fruchter et Hook, 2002) ; l'étoile de Siemens et le critère de Nyquist ; l'inégalité isopérimétrique ; le photocentre (Wielen, 1996).
- **Analogies de structure (même procédé), donc des résultats.**
  - *Le photocentre* (K6, fiche 006). Partagé exactement : un barycentre pesé ; si les poids changent, le barycentre bouge, et sans poids inégaux il reste au centre de symétrie. Transporté : le déplacement entre deux pesées révèle une inégalité cachée des poids, sans séparer les sources. Ouvert : la palette de l'image (§ 3.5).
  - *Le plafond* (K7, arbre P5). Partagé exactement : la forme n ≈ c·log₂(1/ε), à c près. Transporté : les bits par pas du tableau du § 3.3. Ouvert : une cause commune (§ 5.1).
  - *Le seuil de 13 courbes* (K10, fiche 011). Partagé exactement : L²/A pour n arcs et n cases. Transporté : un seuil n* = 4π·(s/a)² pour tout critère de résolution. Ouvert : rien dans le modèle ; le dessin réel (§ 3.4).

### 3.2 Le budget de décision (question 2)

Un seul tableau. Chaque ligne donne la précision accessible (en pixels, en ppm, en chiffres), ce qu'elle tranche, ce qu'elle ne tranche pas, et la source. Les nombres sans marque viennent du fichier cité ; **(A)** : calculé par moi.

| # | partie | mesure | précision accessible | ce qu'elle tranche | ce qu'elle ne tranche pas | source |
|---:|---|---|---|---|---|---|
| 1 | X § 2 | image floue : point contre disque | écart (ρ/σ)²/4 de l'image du disque : 6,25·10⁻⁴ à ρ/σ = 0,05 ; 2,5·10⁻³ à 0,10 | un disque se distingue d'un point si le bruit est sous ce niveau | la forme du disque | R `carre_ptolemee.md` § 2 |
| 2 | X § 2 | image floue : carré de côté √3·ρ contre disque (même étalement) | (ρ/σ)⁴/480 (A, lu sur la table) : 2,1·10⁻⁷ à 0,10 ; 7,8·10⁻⁴ à 0,8 ; 1,07·10⁻² à 1,6. Un PNG à 8 bits (1/255 = 3 900 ppm) voit les coins pour ρ/σ ≳ 1,2, c'est-à-dire p/σ ≳ 2 (p = côté du pixel) | les coins d'un pixel, si le flou reste sous p/2 | les coins sous un flou plus large | R § 2 ; A |
| 3 | XIV § 6 | part du triangle couverte par l'arbre de Perron sur n × n | 0,622 (n = 16), 0,463 (64), 0,353 (256), 0,275 (1 024), contre 2/(k + 2) = 0,222 pour k = 7 | le meilleur nombre de branches (k = 2, 4, 5, 7) | l'aire sans grille : la grille ajoute 24 % à n = 1 024 | R `aiguille_grille.md` § 6 |
| 4 | XIV § 5 | minimum de Kakeya dans F_q | exact (entiers) pour q = 3, 5, 7 : 7, 17, 31 points | la moitié du plan, plus (q − 1)/2 | q pair, q > 7 (c'est T5) | R `aiguille_grille.md` § 5 |
| 5 | XV § 3 | chèvre comptée sur une grille | erreur ∝ points^(−0,7) (A) ; le ménisque (0,35 % de la corde) est vu dès 5 239 points (2D décalée), 5 261 (2D carrée), 16 295 (3D décalée), 24 405 (3D cubique) | chèvre ou simplexe | rien sous quelques milliers de points | R `grille_decalee.md` § 3 ; A |
| 6 | XVIII § 4 | encadrement certain de πR² par les pixels | écart 8R : ±4/(πR) = ±127 ppm à R = 10⁴ (π entre 3,141194 et 3,141994) ; un chiffre de plus par décade de R | 4 chiffres de π à R = 10⁴ | la longueur (8R − 4 contre 2πR) | R `pixels_longitudes.md` § 4 |
| 7 | XVIII § 4–5 | encadrement certain de la corde | demi-largeur 2,285/R (A) : ±15 ppm à R = 2¹⁷ ([1,15871103 ; 1,15874591]) ; exclut l'arête du simplexe (1,154701) dès R ≈ 567, soit ≈ 10⁶ pixels (A) | chèvre ≠ simplexe, avec garantie | — | R § 4 ; A |
| 8 | XVIII § 5 | corde par les centres des pixels | 8 chiffres à R = 10⁵ (écart 6,9·10⁻⁹) ; loi R^−1,5 ; 4,6 ppm à R = 10³ et 0,13 ppm à R = 10⁴ | la valeur, quand on la connaît déjà | rien de certain | R § 4 |
| 9 | XVIII § 3 | écart de Gauss | E(10⁶) = −3 964,79 ; 8 chiffres communs avec πR² ; borne O(R^0,6298) (Huxley) | les premiers chiffres de π par le comptage | une meilleure borne que R^0,63 | R § 3 |
| 10 | XXIII § 1 | n²·μ_n | 2/3 à 10⁻⁴ près jusqu'à n = 10⁶ ; la double précision ne suffit plus à 10⁷ (0,6661) | la loi 2/(3n²) | n ≥ 10⁷ sans précision étendue | R `lentilles_boules_grain.md` § 1 |
| 11 | XXIII § 6 | chèvre de dimension 24 | corde certifiée 1,3859315750 (10 chiffres) ; μ₂₄ = 8,063·10⁻⁴ | le ménisque en 24D | — | R § 6 |
| 12 | XXIX § 2 | un croisement du Venn à 17 courbes | 1/131 070 de l'aire = 7,63 ppm = 22,56 px² (côté 4,75 px) | le grain naturel de l'image | tout ce qui est plus petit qu'une région | R `venn_ppm.md` § 2 |
| 13 | XXIX § 3 | remplissage de l'image selon le grain | 60,3 % à 1 px ; 91,7 % à 2 px ; 99,2 % à 3 px ; 99,9 % à 4 px | dimension 2 au-dessus de 5 px (7,6 ppm), des lignes en dessous (veines : 0,97 à 1,31) | — | R § 3 |
| 14 | XXIX § 5.5 | rapprochements numériques (1 240 comparaisons) | observés/attendus : 1/0,41 à 1 000 ppm ; 0/0,038 à 100 ppm ; 0/0,004 à 10 ppm | qu'aucun rapprochement ne tombe sous 100 ppm | la nature d'un écart de 845 ou de 2 856 ppm | R § 7 |
| 15 | XXX § 1.1 | centre de symétrie d'ordre 17 | ±0,003 px (k = 1, 2, 4, 8) ; 0,004 px du centre de l'image ; 3 ppm du rayon (984 px) | quelle pesée est fausse : les écarts valent 200 à 15 000 fois ce grain | — | R `centre_venn.md` § 1 |
| 16 | XXX § 1.2 | centre de la lumière, six pesées | 0,61 ; 1,26 ; 4,51 ; 13,58 ; 33,07 ; 46,07 px | qu'il existe un dipôle de couleurs | sa cause, sans modèle de palette | R § 1 |
| 17 | revision § 4.9 | masque binaire L > fond + t | sans seuil 0,044 px ; t ≤ 0,01 : 0,06 à 0,12 px ; t = 0,02 : 0,37 px (380 ppm du rayon) ; t = 0,40 : 27,4 px | qu'au-dessus de t = 0,01 le seuil déplace le centre | — | R `revision_001.md` § 4.9 |
| 18 | XXX § 2.4 | moitié de l'aire en pixels | ±1 830 ppm certain (1 517 135 dedans, 1 522 699 touchés, écart 5 564 = 8⌊r⌋ + 4 exactement, A) ; +21 ppm par les centres ; au grain d'un croisement ±3 510 ppm (≈ 920 croisements frôlés) | la moitié (49,4 % à 50,6 % de l'encre) | les quatre certificats à 17 courbes (−649, +2 853, −3 761, −1 816 ppm) | R `centre_venn.md` § 1–2 |
| 19 | XXX § 2.5 | moitié des croisements, dans un certificat | exacte (entiers d'orbites de n) | 262 143 de chaque côté pour `venn19-ramp12h-s192102` | — | R § 2 |
| 20 | XXX § 6.2 | empilement des 17 copies | incohérence 2,1 % (0 px), 4,0 % (0,125), 9,0 % (0,25), 24,9 % (0,5), 50,2 % (1 px), 99,5 % (8 px) | le centre doit être connu à ≈ 0,1 px | un centre à 1 px | R § 6 |
| 21 | XXX § 6.3 | défocalisation de l'harmonique 17 | signes de 2J₁(x)/x justes sur 93 % de 76 rayons ; inversion mesurée de 16 à 21 px, prévue de 9,7 à 17,7 px | le signe du contraste | la position du premier zéro (décalage de 4 à 6 px) | R § 6 |
| 22 | XXX § 2.2 | crans du diaphragme dans l'image | un cran garde la moitié à 6 % près jusqu'au 6e (0,0148 pour 0,0156) ; nul au 13e | la loi 2⁻ʲ jusqu'à f/8 | au-delà : le trou central (14,6 px) | R § 2 |
| 23 | XXX § 6.4 | largeurs d'image nécessaires | W_reste(17) = 817 px, W_centre(17) = 950 px ; à 2 000 px : 19,58 et 18,99 courbes ; à 4 000 px (grains repositionnés) : 21,58 et 20,85 ; à 8 000 px : 23,58 et 22,73 | quels Venn l'image montre : 19 à la limite, 23 non | un autre critère que 2 px | R § 6 ; A |
| 24 | XXX § 6.4, XXIX § 1.3 | trou central de l'image | règle d'aire égale : 11,05 px (A ; 11,2 px avec R = 984) ; minimum pour que l'arc égale le côté d'un croisement : 12,85 px (A) ; mesuré : 14,57 px | le dessin a 13 % de marge au centre (arc 5,39 px, côté 4,75 px) | — | R § 1, § 6 ; A |
| 25 | fiche 001 | 2⁻¹⁷ et 5¹⁷ | 12 chiffres exacts (762 939 453 125) | 2⁻ʲ = 5ʲ·10⁻ʲ pour tout j | — | R `venn_ppm.md` § 2 |
| 26 | fiche 007 | fenêtre d'une recherche de centre | ±8 puis ±2 px pour un biais de 13,6 px : centre faux de 2,36 px | une fenêtre doit dépasser le biais attendu d'au moins un facteur 3 (ici ±41 px) | — | R `centre_venn.md` § 1 |

**Trois régimes.** (i) *Exact* : les entiers et les identités (lignes 4, 19, 25) n'ont pas de grain. (ii) *Certifié* : un encadrement dont la largeur est connue (lignes 6, 7, 18) ; c'est la seule précision garantie du dossier, et elle gagne un chiffre par décade de R. (iii) *Mesuré* : une image et sa pesée (lignes 12, 13, 15 à 17 et 20 à 22) ; la précision du pixel est très bonne (3 ppm sur le centre), celle de la pesée ne l'est pas (jusqu'à 15 000 fois plus). Une mesure d'image ne dépasse donc jamais le grain de la pesée.

**Deux comparaisons qui décident.**
- *Image contre certificat.* L'image tranche la moitié à ±1 830 ppm de façon certaine, et à ±3 510 ppm au grain d'un croisement. Les quatre certificats à 17 courbes sont à −3 761, −1 816, −649 et +2 853 ppm de la moitié (R : `centre_venn.md` § 2) : deux tombent dans la bande certaine (−1 816 et −649), trois dans la bande d'un croisement (avec +2 853), un seul en sort (−3 761). De plus, l'encre de l'image est à 49,43 % dans le contour réduit de 1/√2 : 5 700 ppm sous la moitié, plus que l'écart de n'importe quel certificat. La moitié de l'image ne peut donc pas désigner son certificat. Le certificat, lui, compte des entiers.
- *Garantie contre rapidité.* Pour voir le ménisque de la chèvre par le comptage des centres, 5 000 points suffisent (ligne 5). Pour le *certifier* par l'encadrement dedans/dehors, il faut R ≈ 567 px, soit un million de pixels (ligne 7). Le rapport est de 200.

### 3.3 Les taux de change entre grain et pas (question 3)

Un seul tableau. « Pas » est ce qu'on augmente (dimensions, courbes, étages, pixels) ; « grain » est ce qu'on tolère. **(A)** : calculé par moi, avec mpmath, pour compléter les valeurs du fichier cité.

| # | objet | pas | grain et lecture | loi | pour ε = 1 ppm | pour ε = 10⁻⁵⁰ | source ; statut |
|---:|---|---|---|---|---:|---:|---|
| 1 | boule, équateur | dimension | tranche \|x₁\| < ε qui contient la moitié (longueur) | n ≈ 0,455/ε² (= 2·erfinv(½)²/ε²) | 4,55·10¹¹ | 4,55·10⁹⁹ | R `lentilles_boules_grain.md` § 4 ; XXVII § 3 ; démontré |
| 2 | boule, coquille | dimension | épaisseur ε qui contient la moitié (longueur) | n ≈ ln 2/ε | 6,93·10⁵ | 6,93·10⁴⁹ | idem ; démontré |
| 3 | lentille, plan x₀ | dimension | x₀ < ε (longueur) | n ≈ 1/ε − 1 (XXIV : 1/ε − 4/3, avec le ménisque) | 10⁶ − 1 | 10⁵⁰ − 1 | R § 2 et § 4 ; calculé, à μ/2 près |
| 4 | ménisque, lecture en longueur | dimension | μ/2 < ε | n ≈ 1/√(3ε) | 577,4 ; 572,5 avec les termes suivants (A) | 5,77·10²⁴ | R § 4 ; calculé (terme principal : XXIV) |
| 5 | ménisque, lecture en aire | dimension | μ < ε | n ≈ √(2/(3ε)) | 816,5 ; 811,6 (A) | 8,17·10²⁴ | R `venn_ppm.md` § 4 (817) ; idem |
| 6 | diaphragme à N lames | lames | déficit de lumière 2π²/(3N²) < ε (aire) | N ≈ π√(2/(3ε)) | 2 565 (le texte : 2 566) | 2,57·10²⁵ | R `venn_ppm.md` § 4 ; calculé |
| 7 | série de la chèvre, coupée au mieux | dimension | erreur 1,03·2^(−n/2)/n < ε | n ≈ 2 log₂(1/ε) − 2 log₂ n ; ½ bit par dimension, 6,644 par décade | 31 (30,1) | 316 (315,7) | R `tranche_aiguilles.md` § 1 ; XXVII § 3 ; démontré (XXV) |
| 8 | Kakeya au grain δ | tubes | aire ≥ π/(1 + 2γ + 2 ln(2/δ)) | 1/aire ≤ (1 + 2γ + 2 ln(2/δ))/π : + 1,466 par décade, + 0,441 par bit | 9,92 (aire ≥ 0,1008) | 74,4 (aire ≥ 0,01344) | R `kakeya_miroir.md` § 1 ; `venn_ppm.md` § 4 ; démontré (borne) |
| 9 | Perron, branches de largeur 2⁻ᵏ | étages | largeur | 1 bit par étage ; aire exacte 2/(k + 2) | 20 étages (aire 0,091) | 166 étages (aire 0,0119) | R `venn_ppm.md` § 4 ; `aiguille_grille.md` § 6 ; démontré |
| 10 | Perron sur une grille n × n | côté n | cases | aire minimale ≈ 2,8/log₂ n ; meilleur arbre à n/4 ou n/8 branches (A) ; pour diviser l'aire par 2, élever n au carré | — | — | R `aiguille_grille.md` § 6 ; calculé (ordre : Córdoba, Keich) |
| 11 | Venn, grain en aire | courbes | aire d'une région 2⁻ⁿ | 1 bit par courbe | 20 (19,93) | 166,1 | R `venn_ppm.md` § 4 ; démontré |
| 12 | Venn, grain en longueur | courbes | côté d'une région 2^(−n/2) | ½ bit par courbe : √2 de largeur d'image par courbe | 40 (39,86) | 332,2 | R `venn_ppm.md` § 3 et § 4 ; démontré |
| 13 | Venn dessiné sur W px | courbes | 2 px par côté de croisement (reste) ; 2 px d'arc (centre) | n_reste = 2 log₂ W − 2,35 ; centre : n + log₂ n = 2 log₂ W + 1,30 (A) | W = 2 000 px : 19,58 (reste), 18,99 (centre) | — | R `centre_venn.md` § 6 ; exact dans le modèle |
| 14 | pixels, encadrement d'un disque | rayon R | demi-largeur 4/(πR) en relatif | un chiffre par décade de R, un bit par doublement | R ≈ 1,3·10⁶ (A) | — | R `pixels_longitudes.md` § 4 ; démontré |
| 15 | pixels, encadrement de la corde | rayon R | demi-largeur 2,285/R | un chiffre par décade de R | R ≈ 2·10⁶ (A) | — | R § 4 ; calculé |
| 16 | pixels, corde par les centres | rayon R | écart | ≈ R^−1,5, sans garantie | R ≈ 2·10³ à 3·10³ (lu : 4,6 ppm à 10³, 0,13 ppm à 10⁴) | — | R § 4 ; calculé |
| 17 | pixels, écart de Gauss | rayon R | E(R)/(πR²) | O(R^−1,37) (Huxley) ; conjecture R^−1,5 | 1,3·10⁻⁹ à R = 10⁶ | — | R § 3 ; classique |
| 18 | grille, chèvre comptée | points du pré | erreur de la corde | ≈ points^(−0,7), mesuré sur N ≤ 300 (A) | à calculer (extrapoler quatre décades serait hasardeux) | — | A ; à tester |
| 19 | flou, point contre disque | ρ/σ | écart de l'image | (ρ/σ)²/4 | ρ/σ ≈ 2·10⁻³ | — | R `carre_ptolemee.md` § 2 ; démontré |
| 20 | flou, carré (côté √3·ρ) contre disque | ρ/σ | écart de l'image | (ρ/σ)⁴/480 (A) | ρ/σ ≈ 0,15 | — | R § 2 ; A |
| 21 | bits et chiffres | courbes | décimales de 2⁻ⁿ | 2⁻ⁿ = 5ⁿ/10ⁿ a exactement n décimales ; un bit de grain vaut log₁₀ 2 = 0,301 chiffre significatif | n = 20 : 2⁻²⁰ = 9,5367431640625·10⁻⁷ | n = 166 | fiche 001 ; XXVI ; exact |

**Ce que le tableau montre.**
- *Deux familles.* Les lignes 1 à 6 sont des puissances de 1/ε (exposants 2, 1, 1, ½, ½, ½ : le carré, le nombre, la racine). Les lignes 19 et 20 sont des puissances de ε dans l'autre sens : la plus petite taille visible croît comme ε^(1/2), puis ε^(1/4). Les lignes 7 à 13 et 21 sont des logarithmes : un nombre fixe de bits par pas. Les lignes 14 à 18 (les pixels) sont entre les deux : un chiffre décimal par décade de R, donc deux par décade du nombre de pixels.
- *Le logarithme est la marche 0* (XXVII § 3) : ln(1/ε) = lim (ε^(−s) − 1)/s quand s → 0. À 10⁻⁵⁰, ce rapport vaut 10⁵⁰ pour s = 1, 2·10²⁵ pour s = ½ et tend vers 115,1.
- *Ce que gagne un pas.* Un bit en aire (Venn, ligne 11 ; Perron en largeur, ligne 9) ; un demi-bit en longueur (Venn, ligne 12 ; la série, ligne 7) ; 0,441 en 1/aire (Kakeya, ligne 8). Une décade de grain coûte 3,32 pas dans le premier cas, 6,64 dans le second, 1,466 dans le dernier.

**La règle de lecture : le « cran » apparaît deux fois, avec deux causes.**
1. *Une quantité lue en aire ou en longueur* (lignes 3, 4, 5, 6). r² − (1 + g²) = μ est un écart d'aires et μ/2 est le même écart en longueur, parce que 2 − r² = 2x₀ (le diamètre d'Euclide, XXIV § 5). Pour un même nombre de ppm, la lecture en aire est la lecture en longueur à ε/2. Pour une loi n ∝ ε^(−α), le nombre de pas est multiplié par 2^α : × 2 sur le plan (α = 1), × √2 sur le ménisque (α = ½) ; ce serait × 4 sur l'équateur (α = 2), que le corpus ne lit pas en aire. C'est ce qui sépare 572,5 de 811,6, ou 577,4 de 816,5. **Le corpus a déjà la table de ces lectures** : XXIV § 5 et XXV § 1.5 donnent n ≈ κ/ε avec κ = ½ (corde relative), 1/√2, ln 2 (coquille), **1 (plan)**, 1/ln 2 (crans), √2, **2 (aire)** et 4 (aire en unité du disque central), le plan étant la moyenne géométrique de chaque paire de produit 1. Le « cran de lecture » est le rapport 2 entre les lignes « aire » et « plan ». **Le tableau de XXIX § 4 mêle les deux lectures** : le plan (10⁶) est en longueur, le ménisque (817) et le diaphragme (2 566) sont en aire. Il faut le dire à la ligne.
2. *La taille d'une cellule lue en côté ou en aire* (lignes 9, 11, 12). Le Venn compte un bit par courbe sur l'aire d'une région, donc un demi-bit sur son côté ; Perron compte un bit par étage sur la largeur d'une branche. Ces deux lois sont congrues « modulo un cran » (K7) : un facteur 2 sur le nombre de pas, √2 sur la largeur d'image par courbe. XXIX § 4 écrit que le Venn et Perron « sont sur la même marche, un bit par pas » : c'est vrai en comparant l'aire du Venn à la largeur de Perron, pas en comparant deux largeurs.
3. *Pour la série* (ligne 7), le √2 par dimension est celui de la corde limite : ln √2 = ln(sin 90°/sin 45°), la distance entre le bord de la lentille et le sommet du sinus (XXIV § 2, XXV § 1). Le lien avec le cran du diaphragme existait donc déjà ; ce qui n'existe pas, c'est un lien avec le doublement du Venn (§ 5.1).

---

### 3.4 K10 : la constante isopérimétrique, ou une rencontre de constantes ? (question 5)

**Réponse courte.** C'est la constante isopérimétrique, exactement, dans le modèle de XXX § 6.4 (calculé et démontré, A). La seule « rencontre » est un choix : le critère de 2 px est le même pour l'arc et pour le côté. Le seuil général est n* = 4π·(s/a)².

**Les deux largeurs** (XXX § 6.4). On impose 2 px par côté de croisement (s) pour le reste de l'image, et 2 px d'arc (a) entre les n croisements de l'orbite centrale.
- Le reste : l'aire πR² porte 2ⁿ − 2 croisements de côté s, donc s² = πR²/(2ⁿ − 2) et W_reste = 2R = 2s·√((2ⁿ − 2)/π). Pour s = 2 : 4√((2ⁿ − 2)/π).
- Le centre : l'orbite centrale a le rayon ρ = R√(n/(2ⁿ − 2)) dans un dessin à aire égale. Ses n croisements sont à la distance a l'un de l'autre : 2πρ = n·a. D'où W_centre = 2R = (a/π)·√(n(2ⁿ − 2)). Pour a = 2 : (2/π)√(n(2ⁿ − 2)).
- Leur rapport : W_centre/W_reste = (a/s)·√(n/(4π)). Pour a = s, c'est √(n/(4π)), et il vaut 1 pour n = 4π = 12,566 ; il vaut √2 pour n = 8π = 25,13, un cran de plus.

**Vérification (A).** J'ai refait le tableau de XXX § 6.4 avec mpmath (40 chiffres). Le rapport est égal à √(n/(4π)) aux 8 chiffres imprimés, pour tous les n de 11 à 25 :

| n | 11 | 13 | 15 | 17 | 19 | 21 | 23 | 25 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| W_reste (px) | 102,08 | 204,23 | 408,50 | 817,03 | 1 634,06 | 3 268,13 | 6 536,27 | 13 072,5 |
| W_centre (px) | 95,51 | 207,73 | 446,31 | 950,29 | 2 009,28 | 4 224,78 | 8 842,78 | 18 438,5 |
| W_centre/W_reste | 0,93560258 | 1,0171072 | 1,0925484 | 1,1631066 | 1,2296227 | 1,2927207 | 1,3528791 | 1,4104740 |
| √(n/4π) | 0,93560258 | 1,0171072 | 1,0925484 | 1,1631066 | 1,2296227 | 1,2927207 | 1,3528791 | 1,4104740 |

Les valeurs arrondies sont celles du fichier (204/208 à n = 13, 817/950 à n = 17, 1 634/2 009 à n = 19). À 2 000 px, on retrouve 19,583 (reste) et 18,988 (centre) courbes, et 21,58 et 20,85 avec les grains repositionnés (largeurs divisées par 2, soit 4 000 px).

**Pourquoi c'est l'isopérimétrie.**
- L'orbite centrale a le périmètre L = n·a. Elle enferme n cases de côté s, d'aire A = n·s² (c'est la règle du dessin à aire égale : n croisements, n parts d'aire). Donc L²/A = n·(a/s)².
- Pour un cercle, L²/A = 4π, la constante isopérimétrique. Le seuil est l'égalité : n·(a/s)² = 4π.
- L'inégalité L² ≥ 4π·A dit que le cercle est la forme la plus avare en périmètre. Pour n < 4π·(s/a)², n cases de côté s ne tiennent dans aucune courbe de périmètre n·a : l'arc n'est pas contraignant, le goulot est le reste (n = 11 : 102 px pour le reste, 96 pour le centre). Pour n > 4π·(s/a)², c'est le centre qui demande plus (n = 13 : 208 contre 204).
- Le 2/π de W_centre est le rayon de confusion d'une étoile de Siemens à n rayons : 2πρ = 2n, soit ρ = n/π (critère de Nyquist : une période d'au moins 2 px). XVIII § 6 le donne pour N = 72 : 72/π = 22,9 px. XXX § 6.3 dit d'ailleurs « le centre de ton Venn est une étoile de Siemens à 17 rayons », sans relier cette phrase à W_centre. Le 4/√π de W_reste vient de l'aire d'un disque. Ce n'est pas une rencontre de deux constantes indépendantes : 4π = (2π)²/π, le périmètre d'un cercle au carré sur son aire.

**Le seuil général (A).**

| a/s (critère d'arc / critère de côté) | 0,5 | 0,75 | 1 (XXX) | 1,5 | 2 |
|---|---:|---:|---:|---:|---:|
| n* = 4π·(s/a)² | 50,3 | 22,3 | 12,57 | 5,59 | 3,14 |

**Les polygones : deux modèles, deux seuils, un même entier.**
- Le plan (K10) écrit : si les croisements centraux sont joints par des cordes, le seuil est « multiplié par (π/n)/sin(π/n) ». C'est W_centre qui est multiplié (le polygone est *inscrit* dans le cercle d'aire n·s², ses côtés sont plus courts que les arcs), donc le seuil descend : n* = 12,295 (A).
- `revision_001.py` § 4.4 prend un n-gone régulier *de même aire* n·s², de côté a : l'aire n·a²/(4·tan(π/n)) vaut n·s², donc a² = 4·s²·tan(π/n) ; avec a = s, tan(π/n) = ¼ et n* = π/arctan(¼) = 12,824. C'est W_centre qui diminue, et le seuil monte.
- Les deux sont des polygones différents. Les trois valeurs (12,295 ; 12,566 ; 12,824) donnent la même chose : 13 courbes. Le cercle est la forme qui demande le plus de pixels au centre, donc celle dont le seuil est le plus bas parmi les formes de même aire. Une forme plus allongée le repousse : une ellipse de rapport 2:1 donne L²/A = 14,94 (A, intégrale elliptique), donc n* = 14,9.
- La quantité n·tan(π/n) est celle de la fiche 003 : 34·tan(π/34)/π − 1 = 2 856 ppm (2 855,66 ppm). Ces 2 856 ppm sont le **défaut isopérimétrique du 34-gone circonscrit** : L²/A = 4π·(1 + 0,002856).

**Ce que le corpus avait déjà** (CLAUDE.md, § 6 bis). XVIII § 6 (N/π pour l'étoile de Siemens) ; XXVIII (les éventails de Perron font le polygone circonscrit à 2N côtés, contour de l'ombre du cube : le 34-gone) ; la fiche 003 (n·tan(π/n)). Je n'écris donc pas « coïncidence » : le lien est établi dans XVIII et dans la fiche 003.

**Le dessin réel a de la marge.** Pour 17 courbes, la règle d'aire égale donne un trou de 11,05 px, des arcs de 4,09 px et a/s = 0,860 : le centre serait le goulot. Dzoba élargit le trou à 14,57 px (R : `centre_venn.md` § 1) : les arcs font 5,39 px, a/s = 1,134. Le trou minimal pour a = s est 12,85 px. Le dessin a 13 % de marge. Pour 19 courbes, la règle d'aire égale donne a/s = 0,813 et il faudrait élargir le trou de 23 % pour revenir à a = s.

**La variation qui trancherait** (par ordre de coût).
1. *Faire varier a/s.* Si le seuil est isopérimétrique, il suit 4π·(s/a)² (50,3 ; 22,3 ; 12,57 ; 5,59). Si 13 était un nombre rond sans lien avec la forme, il ne bougerait pas. Le calcul est fait ci-dessus (exact dans le modèle). Ce que le calcul ne dit pas : si un dessin réel choisit son critère.
2. *Faire varier la forme.* Cercle 12,566 ; polygones 12,295 et 12,824 ; ellipse 2:1 : 14,94. À refaire dans le script de révision pour que les quatre soient dans `resultats/revision_001.md`.
3. *Mesurer un dessin réel.* Le dépôt de Dzoba contient les SVG des dessins à 11 et 13 courbes (`plotter/venn-11-color.svg`, `plotter/venn-13-color.svg`). Il faut, pour la région centrale de chacun, son périmètre L, son aire A, le pas d'arc moyen a et le côté moyen s d'une région. Le modèle prédit n·(a/s)² = (L²/A)·(κ/n), avec κ = A/s² le nombre de régions moyennes que contient la région centrale : κ = n pour la règle d'aire égale, κ = 29,6 pour l'image à 17 courbes (π·14,57²/22,56). Et L²/A ≥ 4π est garanti. Le calcul demande l'intersection des courbes : **à calculer**, je ne l'ai pas fait.

### 3.5 Test T4 : la palette ou l'ordre de dessin ? (question 4)

#### 3.5.1 Ce que dit le code du traceur (lu, non exécuté)

- **`palette(n, L=0.58, Cmax=0.22, h0=25.0)`** (`plotter_svg.py`, lignes 695 à 709). Pour la courbe i, la teinte OKLCH est h_i = 25° + 360°·i/n, la clarté L est la même pour toutes, et le chroma est le plus grand qui reste dans la gamme sRGB (28 pas de bissection, plafond 0,22). **Je l'ai recopiée : elle redonne à l'identique les 13 couleurs de `plotter/venn-13-color.svg`** (#df202e, #bb5c00, …, #d5217b ; A). Pour 17 courbes, 6 teintes sur 17 sont au plafond de 0,22 et les autres au bord de la gamme.
- **`write_svg(path, paths, colors, page, stroke=0.35)`** (lignes 717 à 725). Un `<path id="curve-i">` par courbe, dans l'ordre i = 0 … n − 1, `fill="none"`, trait plein de 0,35 mm sur une page de 512 mm, `stroke-linecap="round"`, aucun `opacity`, pas de fond. Dans un SVG, un élément écrit après est peint par-dessus (W3C, SVG 1.1, § 3.3) : à chaque croisement, la courbe de plus grand indice recouvre l'autre. C'est l'hypothèse de K6.
- **L'export PNG** (lignes 963 à 979). Soit `rsvg-convert -w px -h px -b white` (fond blanc), soit `qlmanage`, soit `raster_png` (lignes 989 à 1004) : une polyligne opaque par courbe, dans l'ordre de la liste, à 2× puis réduite par `Image.LANCZOS`. Dans les trois cas, l'ordre est 0 → n − 1.
- **Les PNG publiés** (A, lecture des chunks). Ceux de `plotter/` (11 et 13 courbes, et `images/venn13-spread.png`) ont un fond blanc et deux chunks : `sRGB` et `eXIf` (une table EXIF en gros-boutiste avec seulement PixelXDimension et PixelYDimension, 2 000 × 2 000), ce qui ressemble à l'écriture PNG d'Apple (ImageIO) : ils viennent sans doute de `qlmanage`, le repli du code, ou d'un outil de macOS (les chemins du code sont ceux de Homebrew) ; **à vérifier**. Les deux images à 17 courbes (`pressure` et `rose`) sont en RGB, 2 000 × 2 000, fond (6, 6, 10), **sans aucun chunk** (IHDR, IDAT, IEND). Elles n'ont donc pas la signature des PNG du traceur.
- **Ce que dit le README** (lu en entier). L'image est « drawn at uniform crossing density » ; `plotter/` est « pen-plotter SVG exporter, plus rendered 11- and 13-curve drawings » ; `images/` est « the two drawings shown in this README, plus the earlier rose rendering ». Il ne donne ni palette, ni ordre, ni programme pour les images à 17 courbes. Le mot « pressure » est dans le nom du fichier ; le TeX (`paper/venn17-19.tex`, lignes 395 et 396) l'oppose aux « Tutte layouts » (« only Tutte layouts and the pressure-layout log existed »). L'historique git du dépôt est un seul commit (`e89d6f6`) : rien à y lire.
- **Réponse à la question** : l'ordre d'écriture du SVG est 0 → n − 1 (code). Pour les PNG du traceur, c'est aussi l'ordre de l'image (§ 3.5.3 : je le retrouve dans les pixels). Pour l'image à 17 courbes, **à vérifier** : le code qui l'a rendue n'est dans aucun fichier du dépôt.

#### 3.5.2 Le classement des pixels par teinte, et son erreur

- **Ce que fait `revision_001.py` § 4.8** (lu). Pour chaque pixel : OKLab (a, b), teinte = atan2(b, a), classe = la plus proche des 17 teintes h_i. On garde le pixel si L > fond + 0,1, si le chroma dépasse 0,04 puis 0,06, et si la distance de teinte est inférieure à 6°. Cela classe 1 162 689 puis 845 436 pixels. Pour chaque classe : l'aire visible A_i et le moment M_i = Σ(z − c). Les phases des 17 M_i, rotation retirée, s'étalent de 6,2° et 7,4° : la classe i est bien la courbe i. La montée cyclique des A_i est jugée par un coefficient de Spearman contre 2 000 permutations des A_i : 0,38 (p = 0,64) et 0,53 (p = 0,19) (R : `revision_001.md` § 4.8).
- **Son erreur.** Le nul permute les 17 aires, ce qui suppose les classes échangeables. Le texte note lui-même que le profil des A_i change avec le chroma minimal (le premier harmonique des aires passe de 1,9 % à 7,7 %) : il mesure « l'efficacité du classement ». Le test n'a pas de témoin dans le script.
- **Ce que j'ai contrôlé (A).** (1) *Le test de 4.8 a de la puissance.* Sur des témoins dont l'ordre est connu (une courbe du dessin à 13 courbes, tournée 17 fois, trait de 1 px, rendue en opaque de 0 à 16, de 16 à 0, ou en somme sans ordre, avec deux palettes), il donne un coefficient de 0,66 à 0,82 et p ≤ 0,04 pour 0 → 16, 0,61 à 0,73 et p de 0,01 à 0,10 pour 16 → 0, et 0,35 à 0,53 avec p de 0,22 à 0,74 sans ordre. L'image réelle (0,38 ; 0,53) tombe avec les témoins sans ordre. Le verdict de 4.8 est donc bon. (2) *L'erreur du classement lui-même.* Sur le témoin sans ordre, où l'on connaît la courbe qui a fait chaque pixel, la classe de teinte retrouve la courbe dominante pour 67 à 70 % des pixels « purs » (une courbe fait plus de 90 % de l'intensité) et pour 20 % des pixels mélangés (trait de 1 px, deux palettes). La teinte d'un pixel anticrénelé dérive de plusieurs degrés (de −10,6° pour la classe 8 à +5,2° pour la classe 2, médiane par classe ; écart-type global 17°) : le classement par la teinte la plus proche est bruité.
- **Mon complément : un contraste différentiel.** Pour chaque rotation de k crans, je compare la classe d'un pixel et celle de son image tournée. Sans ordre de dessin, la part de désaccords m_k(i) d'une classe i vers i + k est égale à celle de la classe i + k vers i + k + (n − k), c'est-à-dire la même paire de teintes. Un ordre 0 → n − 1 ajoute un écart positif pour les classes qui passent le « bord du tour » (i ≥ n − k) et négatif pour les autres. Le contraste C est la moyenne de cet écart sur les k. Il annule au premier ordre la dépendance à la palette. L'erreur est celle du rééchantillonnage des 17 secteurs angulaires (±1,1 à ±1,5 points). Le code est au § 7.

#### 3.5.3 L'ordre d'écriture, dans les pixels

| image | ordre connu | C (contraste d'ordre, %) |
|---|---|---:|
| `venn17-pressure-dark-2000.png`, 17 courbes, fond sombre | inconnu | **−5,97 ± 1,46** (chroma > 0,04) ; −5,81 ± 1,60 (> 0,06) |
| `plotter/venn-13-color.svg.png`, rendu du SVG, fond blanc | 0 → 12 | **+14,78 ± 0,72** ; +16,55 ± 0,53 (> 0,06) |
| `plotter/venn-11-color.svg.png`, rendu du SVG, fond blanc | 0 → 10 | **+8,55 ± 0,40** ; +8,59 ± 0,41 |
| `images/venn13-spread.png` (README), fond blanc, chunks `sRGB` et `eXIf` | inconnu | +13,03 ± 0,55 ; +14,32 ± 0,54 |
| témoin, palette Y₀ = 0,30, trait 1 px, sans ordre | aucun | −6,41 ± 1,11 |
| témoin, palette Y₀ = 0,30, opaque 0 → 16 | 0 → 16 | +15,87 ± 1,28 |
| témoin, palette Y₀ = 0,30, opaque 16 → 0 | 16 → 0 | −22,89 ± 1,05 |
| témoin, palette L = 0,70, sans ordre / 0 → 16 / 16 → 0 | — | −8,00 ± 1,16 / +13,82 ± 1,33 / −24,13 ± 1,05 |

- **Verdict (A).** L'image à 17 courbes est au niveau des témoins sans ordre (−6,0 contre −6,4 et −8,0) ; l'écart à un ordre 0 → 16 est de 20 points, soit plus de 10 écarts-types ; l'écart à l'ordre inverse est de 17 points. **Les trois PNG du traceur, dont l'ordre est le même que celui du code, montrent la signature positive** (+8,6 à +16,6 %), avec le même contraste. Le test voit donc bien un ordre quand il y en a un dans une vraie image rendue depuis un SVG. L'image à 17 courbes n'en a pas.
- **Ce que le test ne couvre pas.** Si l'image a été rendue sans recouvrement (transparence, mélange additif), aucun ordre ne serait visible dès le départ. Avec un trait plus fin que 0,5 px, la discrimination s'affaiblit (témoin Y₀ = 0,30 à 0,5 px : −10,5 sans ordre, +2,2 pour 0 → 16 ; à 1,5 px : −6,0 et +27,2). La largeur effective du trait de l'image est d'environ 2 px (A : l'encre couvre 61 % de l'intérieur, avec 0,42 px de trait par px² : 1 − exp(−0,42·w) = 0,61, soit w ≈ 2,2 px, franges comprises). L'image rose donne +2,0 ± 2,3 % (chroma > 0,04) et +7,3 ± 1,7 % (> 0,06) : je ne l'interprète pas, faute d'un témoin à sa géométrie.
- **La sensibilité au centre.** Avec un centre faux de 0,5, 1, 2 et 2,36 px, C passe de −6,0 à −4,8, −3,5, −3,0 et −3,1 % : le verdict ne dépend pas du centre. (Le biais de la fiche 007 n'aurait pas faussé T4.)

#### 3.5.4 La palette : presque isoluminante

**Le modèle (ma lecture).** Si seule la couleur de chaque courbe comptait, le centre de la lumière serait déplacé de G·h, où h est le premier harmonique des poids w_i = F(c_i) − F(fond) (F : la grandeur pesée) et G un facteur géométrique complexe (un bras de levier : le centroïde de l'encre d'une courbe). Comme h se calcule à partir des couleurs de conception, on peut comparer deux palettes avec un seul nombre complexe G ajusté sur quatre pesées. Les deux pesées binaires (les masques) sont traitées au § 3.5.5.

| pesée (R : `centre_venn.md` § 1) | écart observé | h, palette L = 0,70 (clarté constante) | h, palette Y₀ = 0,30 (luminance constante) | prédit, Y₀ = 0,30 (G = 181 px à −99,7°) | prédit, Y₀ = 0,34 (G = 190 px à −100,8°) |
|---|---|---:|---:|---|---|
| luminance Y | 0,61 px à −173° | 5,06 % | 0,081 % | 0,15 px à −149° | 0,10 px |
| clarté L | 4,51 px à −134° | 0,01 % | 2,12 % | 3,82 px à −135° | 3,65 px à −136° |
| moyenne RGB | 33,07 px à −163° | 15,97 % | 18,05 % | 32,61 px à −169° | 33,39 px à −168° |
| énergie R + G + B | 46,07 px à −170° | 21,20 % | 25,62 % | 46,29 px à −167° | 45,80 px à −167° |
| résidu RMS | | | | 2,03 px | 1,64 px (1,42 px à Y₀ = 0,36) |

- **Une palette à clarté constante prédit l'inverse de l'observé.** Les dipôles de L et de Y sont ceux du tableau, et avec G ≈ 207 px (ajusté sur la moyenne RGB) elle donne 9 à 12 px sur Y (observé : 0,61) et 0,02 à 0,08 px sur L (observé : 4,51), pour L de 0,58 à 0,75.
- **Le test le plus net est le rapport Y/E.** La luminance Y et l'énergie E sont toutes deux des quantités en lumière linéaire : leur facteur G est le même au premier ordre. Leurs écarts sont dans le rapport 0,61/46,07 = 0,013. Pour une clarté constante, les dipôles sont dans le rapport 0,24 ; pour une luminance constante, 0,003. L'observé est à un facteur 4 de la seconde (0,5 px d'écart) et à un facteur 18 de la première.
- **Les phases suivent.** Avec un seul G, les trois grandes pesées sont retrouvées à 6° près (−135° contre −134° ; −169° contre −163° ; −167° contre −170° ; à 4° près avec Y₀ = 0,34).
- **Le modèle à deux causes du plan n'a pas besoin de son second terme.** Ajusté avec une palette à clarté constante (L de 0,58 à 0,75), obs = G·h + X donne un second terme stable, X ≈ 7 à 8 px à −135° ± 2° (la direction des masques de clarté), et un RMS de 2,2 à 2,8 px (la cause unique G·h seule : 6,0 à 6,6 px). Avec la palette isoluminante, la cause unique fait 1,4 à 2,0 px : X n'est pas nécessaire. Le « second terme » du plan est ce qu'une palette à clarté constante doit emprunter à la largeur visible pour compenser sa luminance.
- **Le bras de levier est mesurable.** Les 17 centroïdes des pixels classés, rapportés à la rotation de 2πi/17, donnent un bras de 379 px à −96° (chroma > 0,04 ; dispersion des 17 bras : 363 à 401 px et ± 12°). La phase retrouve celle de G (−100°). Le module vaut le double du G ajusté (181 à 194 px). Je le lis comme une dilution du dipôle par le mélange des teintes aux croisements ; je ne l'ai pas testé.
- **Ce que les couleurs mesurées ne disent pas.** Dans `centre_venn.md` § 1, les poids sont les couleurs des « 5 % de pixels les plus clairs de chaque teinte » : L de 0,60 à 0,71, premier harmonique 1,6 % en clarté et 4,1 % en luminance. Avec ces poids, l'ordre est inversé, c'est K6. Mais ces couleurs ne départagent pas les deux palettes : leur Y a un écart-type relatif de 6,3 % et leur L de 2,2 %, soit l'ordre de grandeur de ce que donnerait chacune des deux (corrélation avec la clarté de conception de la palette isoluminante : +0,52 ; avec la luminance de conception de la palette à clarté constante : +0,46). La sélection par la clarté peut biaiser selon la teinte. **L'inversion de K6 vient de ce choix de poids, pas de la physique.**
- **La palette de l'image n'est pas celle par défaut du traceur.** Le chroma le plus saturé de chaque classe donne L de 0,627 à 0,682 (A), au-dessus du 0,58 de `palette()`. Le profil d'énergie par classe de teinte corrèle à +0,45 avec `palette(17, L = 0,58)`, +0,99 avec `palette(17, L = 0,70)` et +0,99 avec une palette à Y₀ = 0,30 (écart quadratique 0,49 % et 0,41 %) : le profil ne départage pas ces deux dernières, les pesées Y et L le font.
- **Un accord interne.** XXX § 1.2 conclut « la palette a été faite pour l'œil, et c'est pour l'œil qu'elle est presque équilibrée » ; XXX § 1.1 écrit que les 17 courbes ont la même clarté OKLab (L = 0,58). Les deux ne vont pas ensemble : une clarté constante donne une luminance qui varie de 24 % (0,301 à 0,373). C'est la phrase de § 1.2 qui est la bonne.

#### 3.5.5 Le seuil : le même dipôle, vu par la largeur

Les masques binaires (L > fond + t et moyenne RGB > fond + 25) donnent le même poids à tout pixel d'encre, mais le seuil change la largeur visible d'une courbe selon sa couleur. J'ai ajusté un modèle de largeur à un paramètre : un trait gaussien (σ = 0,5 px, couverture maximale 0,8), mélangé au fond dans l'espace sRGB, et la largeur où L dépasse fond + t. Avec le même G :

| seuil t | 0,02 | 0,05 | 0,10 | 0,15 | 0,20 | 0,25 | 0,30 | 0,40 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| observé (R : `revision_001.md` § 4.8) | 0,38 px | 0,71 | 1,26 | 2,45 | 4,67 | 12,03 | 13,75 | 27,38 |
| modèle, palette Y₀ = 0,30 | 1,03 | 1,20 | 1,62 | 2,00 | 2,64 | 3,60 | 5,14 | 17,12 |
| modèle, palette L = 0,70 | 0,39 | 0,46 | 0,34 | 0,31 | 0,25 | 0,38 | 0,28 | 0,22 |

Le modèle isoluminant reproduit le sens et l'ordre de grandeur de la croissance (de 1 à 17 px, contre 0,4 à 27 px), avec des directions de −137° à −148° (observé : −99° à −136°). La palette à clarté constante ne produit rien (≤ 0,5 px à tous les seuils) : si les 17 courbes avaient la même clarté, le masque de clarté verrait des traits de même largeur. **L'existence de l'effet de seuil est donc elle-même une preuve que la clarté varie d'une courbe à l'autre.** Le seuil n'est pas une cause indépendante de la palette : il la révèle. (Ma lecture ; trois paramètres, un profil de trait inventé, à confirmer par un rendu à palette connue.)

#### 3.5.6 Verdict sur K6 et sur les fiches 006 et 007

1. **L'ordre de dessin est écarté** (témoins réels et construits, § 3.5.3). Si l'image avait été dessinée de 0 à 16 en traits opaques, comme les PNG du traceur, on verrait +14 %.
2. **La « seconde cause » du plan et celle de la session (le seuil) sont la même cause que la première** : la palette, vue par les poids (pesées continues) ou par les largeurs (masques).
3. **K6 n'est plus une obstruction** si la palette de conception est presque isoluminante (Y₀ ≈ 0,30 à 0,36). Les quatre pesées continues sont retrouvées avec un seul G, à 1,4 à 2,0 px près, et leurs phases à 6° près.
4. **Ce qui reste ouvert** : le module du bras de levier (×2) ; la palette réelle de l'image (à demander à l'auteur, ou à lire dans le code de rendu) ; un rendu de contrôle, avec une palette connue, pour valider le modèle de largeur.
5. **Fiche 006** : l'analogie du photocentre tient (partagé exactement : le barycentre pesé) et sa causalité se précise : le dipôle de *conception* explique les écarts, pas le dipôle *mesuré* sur les pixels. **Fiche 007** : T4 ne dépend pas du centre (§ 3.5.3), la fiche reste une leçon de méthode (§ 3.6).

---

### 3.6 Le biais propagé : où d'autres chaînes partent d'un point biaisé ou d'une fenêtre trop étroite (question 6)

La fiche 007 est le modèle : un barycentre biaisé de 13,6 px sert de départ à une recherche à ±8 px puis ±2 px ; elle s'arrête au bord de ses deux fenêtres, à 2,36 px du vrai centre, et le résultat a l'air précis. J'ai cherché le même défaut dans les sept parties et dans les scripts de la révision. Voici douze chaînes (la treizième est un contrôle).

| # | chaîne | point de départ, ou fenêtre | effet | état |
|---:|---|---|---|---|
| 1 | X § 1 (hors de ma plage) | seuil « cercle de rayon > 3 » et point P tiré au hasard | le « trou » de ±24,18° autour de 29,05° suit le point P, pas un angle fixe (R : `carre_ptolemee.md` § 1) | corrigé (« ce qui vient de moi, pas de la géométrie ») |
| 2 | XXIX § 1 | centre = plus grand disque vide centré sur un pixel entier, dans ±15 px autour du milieu de la boîte des pixels allumés | centre à 0,70 px du centre de symétrie ; négligeable pour la densité par anneau (7·10⁻⁴ du rayon), mais fatal pour un empilement (0,5 px : 24,9 % d'incohérence, 1 px : 50,2 %) | signalé en XXX § 1.3 ; XXIX non refait |
| 3 | XXX § 1.3, fiche 007 | barycentre du masque RGB (13,6 px), fenêtres ±8 puis ±2 px | centre faux de 2,36 px | corrigé (recherche fine : 0,004 px) |
| 4 | XXX § 2.1 | le cercle R/√2 centré sur le barycentre de XXIX | 51,93 % au lieu de 50,61 % (le contour réduit de 1/√2 résiste : 49,40 % contre 49,43 %) | documenté |
| 5 | XXX § 1.1 et § 1.2 | palette supposée à L = 0,58 (le défaut du traceur) ; poids mesurés sur les 5 % de pixels les plus clairs de chaque teinte | K6 : l'ordre des pesées paraît inversé (§ 3.5.4) | **ouvert** |
| 6 | XXIX § 2.3 et § 5.2, XXX § 2.5 | « le certificat de l'image » est c3-s2, parce qu'il est vérifié en Lean (XXIX § 6 : « je ne sais pas lequel des quatre il dessine ») | « 49,935 % des croisements dedans, à 649 ppm » est une propriété d'un des quatre certificats, pas de l'image | **ouvert** |
| 7 | XXIX § 1.2 | les trois étapes de `plotter_svg.py` (Tutte, orbites, anneaux à aire égale) attribuées à l'image « pressure » ; XXX § 2.3 appelle « rose » le dessin de Tutte ; le TeX de Dzoba oppose « pressure » et « Tutte » | la chaîne de production de l'image n'est pas celle qu'on a décrite | **ouvert** |
| 8 | XV § 3 (et XXIII § 4) | grille grossière : sous quelques milliers de points, la chèvre comptée se confond avec son simplexe ; la grille cubique retombe pile sur l'arête √(3/2) à N = 2, 4, 6, 12, 14 | conclure « pas de ménisque » serait faux : la fenêtre est trop étroite | corrigé (« quand la grille voit le ménisque ») |
| 9 | XXIV § 2, XXV § 1.2 | série en 1/n coupée au plus petit terme | à n = 2, la meilleure troncature est 0,32 (0,12 à n = 3 ; 0,03 à 5 ; 3·10⁻³ à 10 ; 10⁻⁵ à 24), alors que Borel–Padé donne 6·10⁻¹⁰ (R : `tranche_aiguilles.md` § 1) | corrigé (resommation) |
| 10 | XXIII § 1 | n²·μ_n en double précision | 0,6661 à n = 10⁷ au lieu de 2/3 | signalé dans le résultat |
| 11 | XXIX § 5.5, XXX § 7 | catalogue de 31 constantes et nul brouillé de ±20 % | le nul déclare « hasard » des liens de structure : 6 verdicts justes sur 10 | documenté (fiche 012) |
| 12 | XIV § 5 (hors de ma plage) | minimum de Kakeya calculé pour q = 3, 5, 7 seulement | « la moitié » est vue sur trois premiers impairs | refait par T5 (q = 2 à 9) |
| 13 | `revision_001.py` § 4.8–4.9 | `C_SYM = (999,497 ; 999,499)` écrit en dur | contrôle (A) : avec un centre faux de 2,36 px, C passe de −6,0 à −3,1 % ; le verdict ne bouge pas | pas de biais |

**Ce que montre la liste.**
- Trois chaînes sont ouvertes (5, 6, 7), et elles ont la même racine : *l'image de référence n'est pas documentée*. Un point de départ supposé (palette par défaut, certificat vérifié, procédure du traceur) se propage dans tout ce qu'on en tire.
- Les chaînes corrigées l'ont été de la même façon : on a refait la recherche depuis un autre départ (3), élargi la fenêtre (8), changé de méthode (9 : Borel–Padé) ou varié le paramètre (12).
- **La règle qui en sort** : avant d'écrire « pas de ménisque », « pas de lien » ou « pas d'ordre », vérifier que la fenêtre dépasse le seuil du phénomène d'au moins un facteur 3, refaire la recherche depuis un autre départ, et garder un témoin positif. T4 le fait (§ 7) : le test de 4.8 et mon contraste sont passés sur des témoins qui ont un ordre.

### 3.7 Ce qui reste ouvert

1. **La chaîne de production de l'image de référence** : certificat, mise en page, palette, ordre de dessin. Le seul moyen de la fermer est le code de rendu de Dzoba, ou un rendu de contrôle dont on connaît la palette (§ 6.3).
2. **Le module du bras de levier** (379 px mesurés contre 181 à 194 px ajustés, § 3.5.4).
3. **Une cause commune au logarithme.** La série de la chèvre le doit à une singularité (−ln √2), Perron et le Venn au doublement, les pixels à la quantification. K7 les recolle « modulo un cran » sans dire pourquoi.
4. **Les constantes des plafonds** : 2,8 pour Perron sur grille (quatre points) ; entre π/2 et π·ln 2 pour Kakeya au grain δ (XXVIII § 2.5).
5. **La loi de la chèvre comptée** : pente −0,7 mesurée sur N ≤ 300, contre −0,75 attendue de R^−1,5. À faire varier (grille, piquet, dimension).
6. **Le grain de la physique** : longueur ou aire (XXIII § 7). XXIV § 5 dit que les deux lectures sont vraies ; le choix décide d'un facteur 2^α sur n (§ 3.3).
7. **Un dessin du Venn où la structure de Perron apparaîtrait en deux dimensions** (XXIX § 5.1) ; **le drizzle au-delà du facteur 2 avec les 17 couleurs** (XXX § 6.1, non tenté) ; **la région centrale des dessins à 11 et 13 courbes**, L²/A et κ (§ 3.4).

---

## 4. Les fiches du dossier : verdict, test, et la partie qui portait déjà le lien

Le plan donne cinq fiches au dossier : 001, 006, 007, 008 et 011. Je les juge une à une, puis je propose d'y ajouter la 003 (§ 4.6). Le § 4.7 dit ce que mes résultats changent aux brouillons 018 et 020 de l'agent de session.

| fiche | dimensions (principale d'abord) | verdict | test | la partie qui portait déjà le lien |
|---|---|---|---|---|
| 001 · 2⁻¹⁷ et 5¹⁷ | D2, D3 | lien exact ; garder, partagée avec `bases` | précision poussée (identité pour tout j, 1 à 59) | XXVI § 2 (la virgule : 10⁶/2²⁰ et 5²⁰) |
| 006 · le centre selon la pesée | D3, D8, D7 | lien fort ; la causalité se précise (T4) | mesure : 4 462 fois le grain du centre ; contraste d'ordre ; ajustement des pesées | X § 2 et XVIII § 7 (ce qu'une mesure voit dépend de son noyau) |
| 007 · le premier centre faux | D7, D3 | lien fort (méthode) ; une famille de douze chaînes | refaire l'essai, puis la recherche fine ; T4 insensible au centre | X § 1 (« ce qui vient de moi, pas de la géométrie ») |
| 008 · centré au millième de pixel | D3, D6 | lien fort et exact | quatre rotations indépendantes à 0,003 px | XVIII § 4 (un coin de pixel est demi-entier) |
| 011 · 19 courbes à la limite | D3, D5, D6 | lien fort ; c'est le cas n = 19 de K10 | W_centre(19) = 2 009 px ; identité à 8 chiffres (A) | XVIII § 6 (l'étoile de Siemens, N/π) ; XIV § 6 (le plafond) |
| 003 · 34·tan(π/34) ≈ π *(à ajouter)* | D6, D3 | la quantité de K10 : le défaut isopérimétrique du 34-gone | variation de N : écart × N² → π³/12 | XXVIII (le 34-gone des éventails) |

### 4.1 Fiche 001 — 2⁻¹⁷ s'écrit avec les chiffres de 5¹⁷

`recueil/observations/001-2-moins-17-chiffres-de-5-puissance-17.md` · Fait amusant · exact · partie XXIX · dimension D2.

- **Verdict : lien exact, fort par l'unité, faible par le calcul. Elle reste dans le dossier.** 2⁻¹⁷ = 7,62939453125·10⁻⁶ et 5¹⁷ = 762 939 453 125 : douze chiffres exacts. Pour le grain, elle dit une chose : 2⁻ⁿ = 5ⁿ/10ⁿ s'écrit avec exactement n décimales. Chaque courbe ajoute une décimale à l'écriture exacte du grain, alors qu'elle ne fait gagner que log₁₀ 2 = 0,301 chiffre significatif de finesse. C'est la ligne 21 du tableau du § 3.3.
- **La partie qui portait déjà le lien** : XXVI § 2, la virgule (10⁶/2²⁰ = 0,95367431640625 a les chiffres de 5²⁰ ; un disque de « 1 To » affiche 931 Go, les chiffres de 5³⁰), et CLAUDE.md § 10 (« 2 et 5, de part et d'autre de la virgule : 2⁻ʲ = 5ʲ·10⁻ʲ »). XXIX § 2.1 le dit pour j = 17 et XXIX § 4 pour j = 20.
- **Test.** Précision poussée : l'identité est vraie pour tout j (XXX § 7, E2 : j de 1 à 59). Rien d'autre à faire : c'est une identité.
- **Un trou du nerf.** Le grain de la fiche est celui du Venn (« une région moyenne »), mais elle n'est pas dans le dossier `ombres-cube-venn`. L'y mettre comble le triangle vide (bases, grain, ombres) du niveau des fiches (§ 8).

### 4.2 Fiche 006 — Le centre de la lumière bouge selon la façon de la peser

`recueil/observations/006-centre-de-la-lumiere-selon-la-pesee.md` · Analogie ; Causalité · structure · partie XXX · dimension D3.

- **Verdict : lien fort. La causalité se précise.** La fiche dit que l'écart vient du dipôle des couleurs. C'est vrai, et T4 y met trois choses. (1) L'ordre de dessin n'y est pour rien (C = −6,0 ± 1,5 %, § 3.5.3). (2) Les écarts des quatre pesées continues sont ceux du dipôle de *conception* d'une palette presque isoluminante (RMS 1,4 à 2,0 px, § 3.5.4), pas ceux du dipôle *mesuré* sur les pixels les plus clairs, qui donne l'ordre inversé de K6. (3) Les écarts des masques sont le même dipôle vu par la largeur visible (§ 3.5.5).
- **La partie qui portait déjà le lien.** X § 2 : un petit objet vu à travers un flou ne montre que sa lumière, son étalement puis sa forme, c'est-à-dire des moments, chacun avec sa pesée ; le centre est le moment d'ordre 1 de la pesée choisie. XVIII § 7 : un pixel qui intègre la lumière sur son carré est une pesée. XXIII § 2 : le plan de la lentille passe par le centre de gravité du simplexe, un barycentre à poids égaux. L'analogie avec le photocentre des étoiles doubles (Wielen, 1996) est nouvelle en XXX.
- **L'analogie, en trois temps** (CLAUDE.md § 1). Partagé exactement : un barycentre pesé, qui coïncide avec le centre de symétrie quand les poids sont égaux (rotation d'ordre 17). Transporté : le déplacement entre deux pesées révèle une inégalité cachée des poids. Ouvert : la palette de l'image.
- **Test.** Mesure contre le grain du centre : l'écart du masque RGB vaut 4 462 fois les 0,003 px. T4 bis ajoute un contraste d'ordre calibré et un ajustement des pesées (§ 7).
- **Une phrase à changer.** « Tout écart vient des poids » (XXX § 1.2) devient, après `revision_001.md` § 4.9, « tout écart vient de la couleur, par le poids et par le seuil », et, après T4 bis, « de la palette, par le poids ou par la largeur visible ». XXX § 1.1 dit que les 17 courbes ont la même clarté L = 0,58 : l'image n'a pas cette palette (L mesuré de 0,627 à 0,682).

### 4.3 Fiche 007 — Mon premier centre était faux de 2,36 px : le biais venait du point de départ

`recueil/observations/007-premier-centre-faux-point-de-depart.md` · Causalité · exact · partie XXX · dimension D7.

- **Verdict : lien fort, de méthode. La fiche est le premier cas d'une famille de douze chaînes (§ 3.6).** Trois sont encore ouvertes, et elles viennent de l'image elle-même.
- **La partie qui portait déjà le lien.** X § 1 : le « trou » des rayons de l'œil de poisson venait du seuil « cercle de rayon > 3 » et d'un point P tiré au hasard. La partie le dit en toutes lettres (« ce qui vient de moi, pas de la géométrie ») et la partie XI le précise. C'est exactement la leçon de 007, dans une autre chaîne.
- **Test.** Refaire l'essai tel quel (il s'arrête au bord de ses deux fenêtres), puis la recherche fine sur le même masque (0,004 px). J'y ajoute un contrôle : le contraste d'ordre de T4 est presque insensible au centre (C de −6,0 à −3,1 % pour un centre faux de 0 à 2,36 px) ; le biais de la fiche n'aurait pas faussé T4.
- **Ce que la fiche devrait dire en plus.** Une fenêtre doit dépasser le biais attendu d'au moins un facteur 3 (ici : ±40 px pour 13,6 px). Un résultat qui s'arrête au bord de sa fenêtre est un signal d'alarme.

### 4.4 Fiche 008 — Le dessin de Dzoba est centré au millième de pixel

`recueil/observations/008-dessin-centre-au-millieme-de-pixel.md` · Fait amusant · calculé · partie XXX · dimension D3.

- **Verdict : lien fort et exact.** Le centre de symétrie est en (999,497 ; 999,499), à 0,004 px du centre exact de l'image, (999,5 ; 999,5). C'est 4 ppm du rayon de 984 px. Quatre rotations indépendantes (k = 1, 2, 4, 8) le redonnent à 0,003 px. Il est au coin de quatre pixels : le plus grand disque vide centré sur un pixel ne s'en approche qu'à 0,70 px.
- **La partie qui portait déjà le lien.** La fiche cite IV (le point au centre de la case). J'ajoute XVIII § 4 : le cercle ne passe jamais par un coin de pixel, parce qu'un coin a des coordonnées demi-entières (somme de deux carrés impairs ≡ 2 modulo 4) ; et `revision_001.md` § 4.9 : le milieu d'un axe de 2 000 pixels est 999,5, et prendre 1 000 pour centre donnerait un biais de √2/2 = 0,7071 px. Le dessin respecte la bonne convention.
- **Test.** Quatre rotations indépendantes. Le test est bon, mais il mesure la *symétrie*, une propriété de la géométrie. Il ne dit rien sur le centre de la lumière (fiche 006).
- **Un lien avec le budget.** C'est aussi le cas où XXX § 2.4 applique la loi des 8R de XVIII : 5 564 pixels d'écart entre les pixels qui touchent le cercle de demi-aire et ceux qui sont entièrement dedans. Pour un centre au coin de quatre pixels et un rayon réel r, cet écart vaut exactement 8⌊r⌋ + 4 = 5 564 (A, fiche proposée N2).

### 4.5 Fiche 011 — À 2 000 px, le centre du Venn à 19 courbes est pile à la limite

`recueil/observations/011-centre-du-venn-19-a-la-limite-a-2000-px.md` · Fait amusant ; Corrélation · calculé · partie XXX · dimension D3.

- **Verdict : lien fort et exact. C'est le cas n = 19 de K10.** W_centre(19) = 2 009 px ; W_reste(19) = 1 634 px ; à 2 000 px le centre résout 18,99 courbes. Avec la règle d'aire égale, le trou central d'un Venn à 19 courbes mesurerait 5,84 px et ses arcs 1,93 px, juste sous les 2 px (A). La « limite » est le seuil du critère de 2 px, pas une limite mathématique ; la proximité de 2 000 et de 2 009 (0,45 %) est une coïncidence de taille d'image.
- **La partie qui portait déjà le lien.** La fiche cite XIV (le plafond de Perron sur une grille) et XVIII (l'étoile de Siemens). Les deux sont bons : XVIII § 6 donne le rayon de confusion N/π, qui est exactement le rayon n/π de l'orbite centrale, et XIV § 6 le plafond en 2,8/log₂ n. XXIX § 3.3 donne les pixels par croisement (5,64 pour 19 courbes à 2 000 px).
- **Test.** La loi W_centre(n) = (2/π)·√(n(2ⁿ − 2)) contre W_reste(n). Je l'ai refaite à 40 chiffres : le rapport vaut √(n/(4π)) pour tout n de 11 à 25 (§ 3.4).
- **Ce qu'il manque.** Le critère « 2 px d'arc » est celui de Nyquist pour une étoile à n rayons ; la fiche ne le dit pas. Et le seuil général est n* = 4π·(s/a)² : 13 courbes valent pour a = s.

### 4.6 Fiche 003 — 34·tan(π/34) ≈ π, à 2 856 ppm : à ajouter au dossier

`recueil/observations/003-34-tan-pi-sur-34-et-pi.md` · Coïncidence ; Corrélation · structure · parties XXIX et XXX · dimension D6.

- **Verdict : à ajouter, avec la 011.** C'est la quantité de K10 : n·tan(π/n) est le quart du rapport L²/A d'un n-gone circonscrit. Les 2 856 ppm sont le **défaut isopérimétrique du 34-gone** : L²/A = 4π·(1 + 0,002856). Le seuil de 13 courbes (K10) et le polygone circonscrit des éventails de Perron (fiche 003) sont donc la même constante, et la fiche donne la loi de l'écart qui manque à K10 : l'écart × N² tend vers π³/12.
- **La partie qui portait déjà le lien.** XXVIII, § 3 : N éventails donnent le polygone circonscrit à 2N côtés (le 34-gone pour 17), contour de l'ombre du cube de dimension 17 (XXIX § 5.4).
- **Test.** Variation du paramètre, déjà dans la fiche (2,5927 pour N = 17, puis 2,5839 pour N = 170 et 1 700). L'ajouter au dossier remplit trois triangles vides du nerf au niveau des fiches (§ 8).

### 4.7 Ce que mes résultats changent aux brouillons 018 et 020 de l'agent de session

- **Brouillon 018 (le seuil déplace le centre de la lumière).** Il est confirmé et se précise. L'ordre de dessin est écarté avec des témoins positifs réels (C = +14,8 ± 0,7 % et +8,6 ± 0,4 % sur les PNG du traceur), pas seulement par un nul de permutations (le test de 4.8 a de la puissance, A). Le seuil n'est pas une cause indépendante : avec une palette à clarté constante, il ne produirait rien (≤ 0,5 px) ; il lit la même palette que les pesées (§ 3.5.5). Son champ « test » peut citer le § 7.
- **Brouillon 020 (le seuil des 13 courbes est la constante isopérimétrique).** Il est confirmé et peut gagner trois lignes : le seuil général n* = 4π·(s/a)² (a = pas d'arc, s = côté d'un croisement) ; le rayon n/π, qui est celui de l'étoile de Siemens (XVIII § 6) ; les deux polygones (même aire : 12,824 ; inscrit dans le cercle d'aire n·s² : 12,295). Il peut citer la fiche 003 comme le défaut isopérimétrique du 34-gone.

---

## 5. Les congruences et les obstructions

Une congruence recolle deux sections locales (une partie, un script, une précision) sur ce qu'elles partagent, à une transformation connue près. Une obstruction est ce qui ne se recolle pas : elle désigne une donnée qui manque. Le plan en donne trois pour ce dossier : K6, K7 et K10.

### 5.1 Celles du plan, côté grain

#### K6 — Le dipôle de la pesée et le photocentre (P8, P5) : l'obstruction est levée, sous une condition

- **Ce qui se recolle.** Qualitativement (XXX § 1.2) : un barycentre pesé est à égalité de poids au centre de symétrie, et il bouge avec les poids. **Quantitativement (A)** : pour les quatre pesées continues (Y, L, moyenne RGB, énergie), l'écart observé est G·h, avec h le premier harmonique des poids de conception (fond retranché) d'une palette presque isoluminante (Y₀ = 0,30 à 0,36) et G un facteur complexe (181 à 194 px à −100°). Le résidu est de 1,4 à 2,0 px pour des écarts de 0,6 à 46 px, et les phases tombent à 6° près.
- **La transformation.** Le premier harmonique complexe des poids, multiplié par le bras de levier G de l'encre d'une courbe. Les masques binaires passent par une largeur visible W(t) au lieu d'un poids (§ 3.5.5).
- **L'obstruction du plan.** « Les écarts ne suivent pas les premiers harmoniques des poids » (clarté L 1,6 % → 4,51 px ; luminance Y 4,1 % → 0,61 px). Elle tient pour les poids *mesurés* sur les « 5 % de pixels les plus clairs de chaque teinte ». Elle disparaît pour les poids de *conception* (L 2,1 %, Y 0,08 %).
- **Ce qui ne se recolle pas encore.** (i) Le module du bras de levier : 379 px mesurés contre 181 à 194 px ajustés. (ii) L'amplitude des masques : le modèle de largeur donne 1 à 17 px là où l'on mesure 0,4 à 27 px, avec des directions décalées de 10° à 40°.
- **Le trou désigné.** La chaîne de rendu de l'image (palette, mélange des couleurs, anticrénelage) : un rendu de contrôle dont on connaît la palette.
- **Verdict.** Congruence établie sur les quatre pesées continues (ma lecture, avec trois pièces à l'appui : les phases, le rapport Y/E, la croissance du seuil). Les deux composantes du plan (couleur, ordre de dessin) se réduisent à une seule : la couleur. L'ordre de dessin est écarté (§ 3.5.3).

#### K7 — Le grain plafonne la profondeur, à un cran près : confirmée, avec deux précisions

- **Ce qui se recolle.** La forme n ≈ c·log₂(1/ε) dans cinq chaînes : Perron sur une grille (aire minimale 2,8/log₂ n ; XIV § 6), Kakeya au grain δ (1/borne = 1,127 + 1,466·k à δ = 10⁻ᵏ ; XXVI § 1.2), le Venn sur W pixels (n_max = 2·log₂ W − 2,35 ; XXX § 6.4), les pixels (un chiffre certain par décade de R ; XVIII § 4), la série de la chèvre (316 dimensions à 10⁻⁵⁰ ; XXV § 1.1).
- **La transformation.** Les bits par pas : 1 (Perron en largeur, Venn en aire), ½ (Venn en largeur, série), 0,441 sur 1/aire (Kakeya). Un facteur 2 sur l'exposant : un cran (√2 de largeur d'image par courbe).
- **Première précision : le cran apparaît deux fois** (§ 3.3). Il y a la quantité lue en aire ou en longueur (ménisque : 811,6 contre 572,5 ; plan : × 2), et la cellule lue en aire ou en côté (Venn : 20 contre 40 courbes à 1 ppm). Le plan écrit « un facteur 2 dans l'exposant : un cran (établi) » : c'est le second.
- **Seconde précision : Perron compte la largeur, pas l'aire.** La largeur des branches vaut 2⁻ᵏ, mais l'aire de l'arbre vaut 2/(k + 2) : le bit par étage ne se traduit pas en bit d'aire (20 étages donnent 0,091 du triangle, 166 donnent 0,0119). XXIX § 4 écrit que le Venn et Perron sont « sur la même marche, un bit par pas » ; c'est vrai de l'aire du Venn et de la largeur de Perron.
- **L'obstruction.** Les causes diffèrent : un grain fini (Perron, Venn, pixels) contre la troncature d'une série (la singularité en −ln √2, XXV § 1). Le √2 par dimension de la série est celui de la corde limite (45° contre 90°, XXIV § 2) ; le √2 par courbe du Venn est un doublement de croisements. Ce sont le même nombre par deux voies ; rien dans le corpus ne les relie.
- **Le trou désigné.** Une cause commune, ou la preuve qu'il n'y en a pas. Et les constantes : 2,8 pour Perron sur grille, entre π/2 et π·ln 2 pour Kakeya.
- **Verdict.** Analogie de structure confirmée (partagé exactement : la forme logarithmique ; transporté : les bits par pas ; ouvert : la cause commune).

#### K10 — Le seuil du centre et l'isopérimétrie : exacte, avec un choix à nommer

- **Ce qui se recolle** (§ 3.4). W_centre/W_reste = (a/s)·√(n/(4π)) : identité à 8 chiffres pour n de 11 à 25 (A). Le seuil 4π·(s/a)² est L²/A = 4π pour n arcs et n cases. Le rayon de confusion n/π est celui de l'étoile de Siemens (XVIII § 6). Le polygone circonscrit de la fiche 003 est la même quantité (4n·tan(π/n)).
- **L'obstruction.** Aucune dans le modèle. Le plan dit que « la correction polygonale est le x²/6 de K1 » : (π/n)/sin(π/n) = 1 + π²/(6n²) + … ; c'est vrai pour W_centre, et je trouve 12,295 pour le seuil du polygone inscrit.
- **Ce qui est un choix, pas une constante.** a = s = 2 px. Pour a/s = 1,5, le seuil tombe à 5,6 courbes.
- **Le trou désigné.** La région centrale des dessins réels (L²/A, κ = A/s²), à mesurer sur les SVG de 11 et de 13 courbes.
- **Verdict.** Exacte (démontré dans le modèle, calculé à 40 chiffres). Ce n'est pas une rencontre de constantes.

### 5.2 Les miennes

| # | éléments | transformation | se recolle jusqu'où | obstruction | verdict |
|---|---|---|---|---|---|
| C1 | la palette de conception, les six pesées (XXX § 1.2), le balayage du seuil (`revision_001.md` § 4.8) | poids : G·h ; largeur : G·W(t) | quatre pesées à 1,4 à 2,0 px ; croissance du seuil en sens et en ordre de grandeur | bras de levier × 2 ; amplitude des masques | recollée en sens, pas en valeur |
| C2 | W_centre (XXX § 6.4) et le rayon de confusion de l'étoile de Siemens (XVIII § 6) | 2πρ = 2n, ρ = n/π | entièrement (même équation) | aucune | section globale |
| C3 | la loi des 8R (XVIII § 4) et le budget de la moitié (XXX § 2.4) | 8⌊R + ½⌋ au milieu d'un pixel ; 8⌊r⌋ + 4 au coin de quatre pixels (A) | exactement : 5 564 = 8·695 + 4 | aucune (le texte dit « 8r à 0,6 près ») | recollée exactement |
| C4 | la grille de XV § 3 (chèvre comptée) et le comptage par les centres de XVIII § 5 | erreur ∝ R^−1,4 (A) contre R^−1,5 | l'exposant, à 0,1 près | la pente mesurée (−0,70, −0,71 en points) contre −0,75 attendue ; trois décades de dispersion | congrue, à confirmer |
| C5 | la série de la chèvre (XXV) et le cran du diaphragme (I § 6.4, XXVII § 3) | ln √2 = ln(sin 90°/sin 45°) | le √2 par dimension est le cran de la corde limite | le Venn (doublement) n'est pas relié à la singularité | lien existant (XXIV § 2, XXV § 1, XXVII § 3) |
| C6 | le « cran de lecture » du § 3.3 et la table des lectures κ de XXIV § 5 | n(aire) = 2^α·n(longueur) | κ = 1 (plan), 2 (aire) : exactement | XXIX § 4 mêle les lectures | recollée ; une ligne à corriger |

### 5.3 Les obstructions et les trous qu'elles désignent

| éléments | le trou | où chercher |
|---|---|---|
| palette, ordre, mise en page et certificat de `venn17-pressure-dark-2000.png` (K6, fiches 006 à 008, 011) | le code de rendu de l'image à 17 courbes n'est pas publié | le dépôt `dzoba/venn17` (une demande à l'auteur) ; la version Zenodo 1.3 (doi 10.5281/zenodo.23189412, d'après le README) ; l'article arXiv:2609.26546 (ses figures) |
| bras de levier × 2 ; amplitude des masques (K6) | un modèle de rendu : mélange sRGB ou linéaire, anticrénelage, noyau Lanczos | un rendu de contrôle avec une palette connue (`palette(17, L = 0,58)`, puis une palette isoluminante) |
| cause commune du logarithme (K7) | la série et le Venn ont le même √2 par deux voies | les chaînes XXIV § 2 et XXIX § 2 : exprimer le doublement des croisements par un angle, comme le 45° du bord de la lentille |
| constante de Perron sur grille ; constante de Kakeya (K7) | 2,8/log₂ n est mesuré sur quatre grilles ; π/2 à π·ln 2 est une fenêtre | calculer le meilleur arbre sur n = 16 à 4 096 ; XXVIII § 2.5 |
| région centrale des dessins réels (K10) | L²/A et κ ne sont mesurés sur aucun dessin | `plotter/venn-11-color.svg` et `plotter/venn-13-color.svg` (intersection des courbes) |
| certificat de l'image (XXIX § 5.2) | la moitié de l'image ne le désigne pas (49,43 % de l'encre, 5 700 ppm sous la moitié) | une mesure indépendante de la moitié (croisements par niveau) sur chacun des quatre certificats, comparée à l'image par niveau |
| chèvre comptée (C4) | l'exposant de l'erreur sur trois grilles | `scripts/grille_decalee.py` § 3 : ajouter la pente en points, et la dimension 3 |

---

## 6. Les trous

### 6.1 Les trous du recueil : six fiches nouvelles proposées (question 7)

Le recueil a quinze fiches. Douze viennent de XXIX et de XXX ; aucune ne vient de X, XIV, XV, XVIII ou XXIII (plan, § 6.1). Les six fiches ci-dessous complètent le dossier. Trois (N1, N2, N3) viennent de X, XVIII et XV et sont en D3 ; deux (N4, N5) sont nées de T4 ; une (N6) est la fiche de K7. Elles ne répètent pas les brouillons 016 à 021 de l'agent de session (la classification naïve, le cadre, le seuil, Kakeya fini et Bonferroni, l'isopérimétrie, les dizaines de premiers). Les numéros sont ceux de ce dossier ; l'agent de fin d'arc leur donnera les siens.

| fiche | titre | type | statut | partie | dimension | à partager avec |
|---|---|---|---|---|---|---|
| N1 | À 8 bits, les coins d'un pixel ne se voient que si le flou est plus étroit que la moitié du pixel | Fait amusant | exact (lois), calculé (seuils) | X § 2 | D3 (D4) | `lumiere` |
| N2 | La loi des 8R devient 8⌊R + ½⌋ et 8⌊r⌋ + 4 : c'est exactement le budget de la moitié du Venn | Causalité | exact | XVIII § 4 | D3 | `ombres`, `moities` |
| N3 | La chèvre comptée sur une grille converge comme (points)^(−0,7), sur la grille carrée comme sur la décalée | Corrélation | à tester | XV § 3 | D3 | `corde` |
| N4 | La palette du Venn à 17 courbes est presque isoluminante : l'œil déplace le centre de 0,61 px, l'énergie de 46 px | Causalité | structure | XXX § 1.2 | D3 (D8) | `lumiere`, `methode` |
| N5 | L'image de référence a quatre variables cachées : certificat, mise en page, palette, ordre de dessin | Causalité | ouvert | XXIX § 1.2 et XXX § 1 | D7 (D3) | `lumiere`, `methode`, `ombres` |
| N6 | Une grille de W pixels ne résout que 2·log₂ W − 2,35 courbes ; Perron sur n × n ne couvre que 2,8/log₂ n : la même marche, à un cran près | Analogie | structure | XIV § 6, XXIX § 4, XXX § 6.4 | D3 (D5) | `aiguilles`, `corde`, `methode` |

#### N1 — À 8 bits, les coins d'un pixel ne se voient que si le flou est plus étroit que la moitié du pixel

Fait amusant · exact (lois), calculé (seuils) · partie X · `carre-ptolemee.md` § 2 · `scripts/carre_ptolemee.py`, section 2 (`tf_disque`, `tf_carre`, `image`) · `figures/j1_carre_ptolemee.png`, panneau b · D3, D4.

- **Contexte.** X § 2 montre que, sous un flou de largeur σ, un point, un disque et un carré se confondent : l'écart décroît comme (ρ/σ)², puis comme (ρ/σ)⁴ si le carré a le côté √3·ρ. XVIII § 7 en tire que « le cercle de pixels n'existe que parce que la lumière, passée par l'œil, arrondit les carrés ». Aucune des deux parties ne dit à partir de quand l'écart passe sous la précision d'une image.
- **Observation.** L'écart maximal, rapporté au maximum de l'image du disque, vaut (ρ/σ)²/4 (point contre disque), 0,0118·(ρ/σ)² (carré de même aire contre disque) et (ρ/σ)⁴/480 (carré de côté √3·ρ contre disque ; coefficient lu sur la table, A). Un PNG à 8 bits n'a qu'un niveau de gris sur 255, soit 3 900 ppm. L'écart passe sous ce niveau pour ρ/σ < 0,125, < 0,58 et < 1,2. Pour le dernier cas, le côté du pixel est p = √3·ρ : **les coins d'un pixel ne se voient que pour p/σ > 2**, c'est-à-dire un flou plus étroit que la moitié du pixel. À 16 bits (1,5·10⁻⁵), les seuils sont ρ/σ = 0,0078 ; 0,036 ; 0,29 (p/σ = 0,5). Le flou de σ = 0,7 px de XVIII § 7 donne p/σ = 1,4 : à 8 bits, il efface les coins, ce que la partie observe (« le centre devient un disque gris uniforme »).
- **Test.** Variation du paramètre : la loi tient de ρ/σ = 0,05 à 0,8 (pentes 2,00 ; 2,00 ; 4,00). À 1,6, elle surestime de 28 % (0,0137 pour 0,0107 sur la table) : le seuil du dernier cas est interpolé sur la table (1,2), et il est à 1,2 ± 0,1.
- **Liens et pistes.** XVIII § 7 (le filtre passe-bas optique, le Nikon D800E) ; la quantification à 8 bits est le grain de toute mesure sur un PNG (§ 3.2, lignes 15 à 17). Piste : refaire le calcul avec un flou de la forme du pixel lui-même.

#### N2 — La loi des 8R devient 8⌊R + ½⌋ et 8⌊r⌋ + 4 : c'est exactement le budget de la moitié du Venn

Causalité · exact · partie XVIII · `pixels-longitudes.md` § 4 · `scripts/pixels_longitudes.py`, section 4 (`demi_largeurs`, `compte`) et `scripts/centre_venn.py`, section 2 (`N_IN`, `N_TOUCH`, `BUD_PIX`) · `figures/r1_pixels_contacts.png`, panneau e ; `figures/ae1_centre_moitie.png`, panneau f · D3.

- **Contexte.** XVIII § 4 démontre, pour un rayon R entier et un centre au milieu d'un pixel, que les pixels qui touchent un disque et ceux qui sont entièrement dedans diffèrent de 8R. XXX § 2.4 l'emploie pour le cercle de demi-aire (r = 695,6 px, centre au coin de quatre pixels) et lit : 1 517 135 dedans, 1 522 699 touchés, écart 5 564, « 8r à 0,6 près ».
- **Observation.** Chaque pixel que le cercle coupe correspond à un croisement d'une ligne de grille (une courbe fermée entre dans un pixel nouveau à chaque croisement). Au milieu d'un pixel, les lignes sont aux demi-entiers : 2⌊R + ½⌋ lignes verticales, coupées deux fois, plus autant d'horizontales, soit **8⌊R + ½⌋**. Au coin de quatre pixels, les lignes sont aux entiers, la ligne x = 0 comprise : 4⌊r⌋ + 2 croisements verticaux et autant d'horizontaux, soit **8⌊r⌋ + 4**. Pour r = 695,6 : 8·695 + 4 = 5 564, exactement. Le budget de la moitié est donc ±(8⌊r⌋ + 4)/(2πr²) = ±1 830 ppm, sans « à 0,6 près ».
- **Test.** Comptage direct (A, numpy) : 300 rayons réels tirés dans [5 ; 600], centre au milieu d'un pixel : l'écart est 8⌊R + ½⌋ dans les 300 cas ; 400 rayons réels tirés dans [5 ; 800], centre au coin : 8⌊r⌋ + 4 dans les 400 cas. Les rayons entiers au coin font exception (10 et 100 : 68 et 780 au lieu de 84 et 804), parce que le cercle passe alors par des points du réseau, c'est-à-dire par des coins de pixels.
- **Liens et pistes.** Fiche 008 (le centre au coin de quatre pixels) ; XVIII § 8 (« la raison est un argument modulo 4 ») ; `revision_001.md` § 4.9 (le milieu d'un axe de 2 000 pixels). Piste : l'équivalent pour le périmètre de l'escalier (8R − 4) avec un centre au coin.

#### N3 — La chèvre comptée sur une grille converge comme (points)^(−0,7)

Corrélation · à tester · partie XV · `grille-decalee.md` § 3 · `scripts/grille_decalee.py`, section 3 (`chevre_comptee`) · `figures/o1_grille_decalee.png`, panneau c · D3.

- **Contexte.** XV § 3 dit que la grille voit le ménisque (0,35 % de la corde en 2D) « toujours à partir de » 5 261 points (carrée) et 5 239 (décalée). XVIII § 5 dit que la corde comptée par les centres converge comme R^−1,5.
- **Observation (A).** Sur les deux grilles 2D, pour N de 3 à 300 et plus de 300 points, l'erreur de la corde comptée suit une loi de puissance en nombre de points, de pente −0,70 (carrée) et −0,71 (décalée) ; sur les médianes par tranche, −0,73 et −0,64. Avec des points ∝ R², cela fait R^−1,4, à 0,1 de l'R^−1,5 de XVIII. La médiane passe sous la moitié du ménisque (2,0·10⁻³) vers 1 700 points ; le « toujours à partir de 5 000 » est le pire cas, trois fois plus loin. Les deux grilles ont la même pente : le gain de la grille décalée n'est pas dans le comptage (c'est ce que dit XV § 3).
- **Test.** À tester : faire varier la grille (cubique, couches décalées, dimension 3), le piquet et le rayon ; comparer la pente au R^−1,5 conjecturé (Hardy, R^(1/2 + ε) pour le cercle de Gauss). Trois décades de dispersion : prendre des médianes.
- **Liens et pistes.** XVIII § 3 (le cercle de Gauss) et XXIII § 4 (« le grain voit le ménisque au-dessous de n ≈ 0,58/√ε »).

#### N4 — La palette du Venn à 17 courbes est presque isoluminante

Causalité · structure · partie XXX · `centre-venn.md` § 1.2 · `scripts/revision_001.py`, section 4.8 (et le code du § 7 de ce dossier) · `figures/ae1_centre_moitie.png`, panneau b · D3, D8.

- **Contexte.** XXX § 1.2 mesure six centres de la lumière (0,61 à 46,07 px) et les attribue au dipôle des couleurs. Le plan (K6) note que l'ordre des écarts ne suit pas l'ordre des dipôles mesurés (Y : 4,1 % pour 0,61 px ; L : 1,6 % pour 4,51 px).
- **Observation.** Avec les couleurs de *conception* d'une palette à luminance relative constante Y₀ = 0,30 à 0,36 (chroma plafonné à 0,22), un seul facteur G (181 à 194 px à −100°) donne les quatre pesées continues à 1,4 à 2,0 px (RMS), et leurs phases à 6° près. Une palette à clarté constante prédit 9 à 12 px sur Y et 0,02 à 0,08 px sur L. Le rapport des écarts Y/E vaut 0,013 ; il vaudrait 0,24 pour une clarté constante et 0,003 pour une luminance constante. La palette « faite pour l'œil » de XXX § 1.2 est donc celle de l'image ; la phrase de XXX § 1.1 (L = 0,58) ne l'est pas.
- **Test.** Ajustement de quatre pesées par un seul nombre complexe (A) ; rapport Y/E ; croissance de l'écart des masques avec le seuil (modèle de largeur à un paramètre) ; le modèle à deux causes du plan, ajusté avec une clarté constante, donne un second terme de 7 à 8 px qui disparaît avec la palette isoluminante. **À tester** : un rendu de contrôle avec une palette connue.
- **Liens et pistes.** Fiches 006 et 018 (brouillon) ; Wielen (1996) ; le bras de levier mesuré (379 px) vaut le double de G.

#### N5 — L'image de référence a quatre variables cachées

Causalité · ouvert · parties XXIX et XXX · `venn-ppm.md` § 1.2 et § 5.2 ; `centre-venn.md` § 1.1 et § 2.3 · `scripts/venn_ppm.py`, section 1 ; `scripts/centre_venn.py`, section 1 · `figures/ad1_venn_ppm.png`, panneau a · D7, D3.

- **Contexte.** Toutes les mesures de XXIX et de XXX portent sur `venn17-pressure-dark-2000.png`. Le README de Dzoba la décrit en une ligne (« drawn at uniform crossing density ») et ne donne aucun programme. Le dépôt n'a que le traceur SVG (`plotter_svg.py`), dont les PNG ont un fond blanc et des chunks `sRGB` et `eXIf` ; l'image n'a ni l'un ni l'autre.
- **Observation.** Quatre variables sont supposées connues et ne le sont pas. (1) *Le certificat* : XXIX prend c3-s2 parce qu'il est vérifié en Lean ; la moitié de l'image (49,43 % de l'encre, 5 700 ppm sous la moitié) ne le désigne pas, car les quatre certificats sont de −3 761 à +2 853 ppm. (2) *La mise en page* : XXIX § 1.2 décrit les trois étapes du traceur (Tutte, orbites, anneaux à aire égale) ; XXX § 2.3 appelle « rose » le dessin de Tutte ; le TeX de Dzoba oppose « pressure » et « Tutte ». (3) *La palette* : mesurée à L de 0,627 à 0,682, donc pas la valeur par défaut (0,58) ; presque isoluminante (fiche N4). (4) *L'ordre de dessin* : écarté dans les pixels (C = −6,0 ± 1,5 %, contre +14,8 % pour les PNG du traceur).
- **Test.** À tester : le code de rendu de l'auteur, ou un rendu de contrôle du certificat c3-s2 par `plotter_svg.py` avec `palette(17, L = 0,58)` puis une palette isoluminante, comparé aux six pesées.
- **Liens et pistes.** Fiche 007 (le biais propagé : trois des douze chaînes ouvertes sont celles-ci, § 3.6) ; fiche 006.

#### N6 — Une grille de W pixels ne résout que 2·log₂ W − 2,35 courbes : la même marche que Perron, à un cran près

Analogie · structure · parties XIV, XXIX et XXX · `aiguille-grille.md` § 6 ; `venn-ppm.md` § 4 ; `centre-venn.md` § 6.4 · `scripts/aiguille_grille.py`, section 6 ; `scripts/centre_venn.py`, section 6 · `figures/n2_perron_grille.png`, panneau c ; `figures/ae3_grains_hasard.png`, panneau e · D3, D5.

- **Contexte.** XXX § 6.4 écrit que le Venn ne peut dépasser « de l'ordre de 2·log₂ de la largeur de l'image en courbes », comme Perron sur une grille. K7 du plan recolle les deux « modulo un cran ».
- **Observation.** *Partagé exactement* : la forme n ≈ c·log₂(1/ε). Pour le Venn à 2 px par côté de croisement, n_reste = 2·log₂ W − 2,35 (19,58 à 2 000 px) ; pour Perron sur une grille n × n, l'aire minimale est 2,8/log₂ n (0,275 à n = 1 024), et pour la mettre sous la moitié il faut élever n au carré. *Transporté* : les bits par pas du § 3.3 (1 bit par étage de Perron en largeur, ½ bit par courbe du Venn en largeur). *Ouvert* : une cause commune ; la série de la chèvre a le même √2 par une troncature (XXV).
- **Test.** Variation du paramètre : quatre grilles pour Perron (n = 16 à 1 024), quinze valeurs de n pour le Venn (11 à 25). **À faire** : Perron sur n = 16 à 4 096, pour que « 2,8 » ait plus de quatre points.
- **Liens et pistes.** Fiche 011 (le cas n = 19) ; XXIX § 4 ; XXVII § 3.

---

### 6.2 Les trous du corpus : erreurs et imprécisions trouvées

Sept points, tous contrôlés par un calcul ou par la lecture du code de Dzoba. Aucun ne casse un résultat ; deux (E1, E3) changent une phrase de conclusion.

| # | fichier | ce qu'il affirme | le problème, et la proposition |
|---|---|---|---|
| E1 | `centre-venn.md` § 1.1 | « La palette du traceur de Dzoba donne aux 17 courbes la même clarté OKLab (L = 0,58) […] C'est le canal où les courbes pèsent le plus également. » | L = 0,58 est la valeur par défaut de `palette()` (vérifié : elle redonne les 13 couleurs du SVG à 13 courbes). Mais l'image à 17 courbes n'a pas été rendue par ce code (pas de chunk, fond sombre) et ses couleurs les plus saturées ont L de 0,627 à 0,682. Le § 1.2 conclut en même temps que la palette est « presque équilibrée » pour l'œil, ce qu'une clarté constante ne donne pas (la luminance varierait de 24 %). Les pesées vont dans le sens d'une luminance presque constante. À écrire : « palette inconnue ; luminance presque constante, inférée ». |
| E2 | `venn-ppm.md` § 1.2 (et `resultats/venn_ppm.md` § 1, « le rendu "pressure" du dépôt ») | l'image est dessinée par les trois étapes de `plotter_svg.py` : un dessin de Tutte, 7 710 inconnues par orbite, des anneaux à aire égale ; « le contour à 17 côtés est un choix de dessin » | `centre-venn.md` § 2.3 appelle « rose » le dessin de Tutte. Le README ne dit pas que `plotter_svg.py` a rendu l'image, et le TeX de Dzoba oppose « pressure » et « Tutte » (`paper/venn17-19.tex`, lignes 395 et 396). Ce que le § 1.2 décrit est le *traceur* ; pour l'image, on ne mesure que le contour à 17 côtés et la densité (60,8 % d'encre, de 56 à 63 % par anneau). À écrire : « le traceur du dépôt fait trois choses ; le programme de l'image « pressure » n'est pas publié ». |
| E3 | `venn-ppm.md` § 2.3 et § 5.2 ; `resultats/venn_ppm.md` § 2 ; `centre-venn.md` § 2.5 | « le certificat de l'image » met 49,935 % des croisements dedans, « à 649 ppm de la moitié » (« dont l'image : −649 ppm ») | XXIX § 6 écrit : « je ne sais pas lequel des quatre certificats il dessine ; j'ai pris celui qui a été vérifié en Lean (c3-s2) ». Un choix devient un fait dans les §§ 2.3 et 5.2 et dans XXX § 2.5. La moitié de l'image (49,43 % de l'encre, 5 700 ppm sous la moitié) ne désigne aucun des quatre (de −3 761 à +2 853 ppm). À écrire : « un des quatre certificats (c3-s2, vérifié en Lean) ». |
| E4 | `venn-ppm.md` § 4 (tableau « ce que coûte 1 ppm ») | le plan (10⁶ dimensions), l'équateur (10¹²), le ménisque (817) et le diaphragme (2 566) sont rangés dans la même colonne | Les deux premiers sont en longueur (x₀ < ε ; tranche \|x₁\| < ε), les deux autres en aire (μ < ε ; déficit de lumière). Pour le même ppm, le ménisque est 577,4 en longueur (572,5 avec les termes suivants, XXIII § 4) et 816,5 en aire (811,6 ; A : l'écart au terme principal reste voisin de −4,9 dans la table de `lentilles_boules_grain.md`). Le 817 est le terme principal. L'équateur a perdu sa constante (4,55·10¹¹). À ajouter : une colonne « lecture ». |
| E5 | `venn-ppm.md` § 4 | « le Venn et Perron sont sur la même marche : un bit par pas. […] tous deux en 2ⁿ morceaux de 2⁻ⁿ » | Perron : largeur 2⁻ᵏ, aire 2/(k + 2). Venn : aire 2⁻ⁿ, largeur 2^(−n/2). Le bit par pas est un bit de largeur pour Perron et d'aire pour le Venn : c'est le « modulo un cran » de K7, que XXIX § 4 ne dit pas (§ 3.3, règle de lecture 2). |
| E6 | `pixels-longitudes.md` § 4 ; `centre-venn.md` § 2.4 | l'écart dedans/dehors vaut « exactement 8R » ; au cercle de demi-aire, « 8r à 0,6 près » | La loi est exacte pour un rayon réel : 8⌊R + ½⌋ au milieu d'un pixel, 8⌊r⌋ + 4 au coin de quatre pixels (fiche N2). 5 564 = 8·695 + 4, sans reste. |
| E7 | `lentilles-boules-grain.md` § 4 ; `tiers-dimension.md` § 5 | le plan de la lentille : n = 1/ε − 1 (XXIII) ; n + 4/3 = 1/ε (XXIV, XXV) | Les deux sont justes à leur ordre : le tiers de dimension est le ménisque (1 + 1/3). À écrire une fois : « 1/ε − 1 au premier ordre, 1/ε − 4/3 avec le ménisque ». |

### 6.3 Les trous des données publiées (question 7)

Je n'ai fait aucune recherche en ligne. Chaque référence est marquée **sûre** (je connais l'auteur, la revue et l'année) ou **à vérifier**. Celles qui viennent du corpus sont marquées (corpus).

**a. Le rendu de l'image à 17 courbes (fiches 006, 007, 008, 011 ; K6 ; fiche N5).**
- *Ce qui manque.* Le programme, la palette et l'ordre de dessin des deux images à 17 courbes ne sont ni dans le dépôt, ni dans le README, ni dans le TeX. `plotter/` ne publie que les dessins à 11 et 13 courbes. L'historique git est un seul commit.
- *Où chercher.* Une demande à l'auteur ; l'archive Zenodo de la version 1.3 (`https://doi.org/10.5281/zenodo.23189412`, d'après le README) ; les figures de l'article.
- *Références.* C. Dzoba, arXiv:2609.26546 (2026), math.CO (README ; **sûre**, telle que donnée par le dépôt) ; les DOI Zenodo du README : 10.5281/zenodo.23189412 (v1.3), 10.5281/zenodo.22896682 (v1.2), 10.5281/zenodo.22885650 (v1.1), 10.5281/zenodo.22885649 (tous) (**sûre**).

**b. La provenance des images matricielles tirées de dessins vectoriels.**
- *L'observation.* L'ordre de dessin et le mélange des couleurs d'un PNG dépendent du programme de rendu ; ni l'un ni l'autre n'est dans le fichier (les PNG de Dzoba à 17 courbes n'ont aucun chunk).
- *Ce qui manque.* Une règle de publication : donner l'ordre, la palette et le mélange (espace sRGB ou linéaire). Je ne sais pas si `rsvg-convert` (ou le moteur d'Apple) mélange en sRGB ou en lumière linéaire (**à vérifier**).
- *Références.* W3C, *Scalable Vector Graphics (SVG) 1.1 (Second Edition)*, 2011, § 3.3, l'ordre de rendu (**sûre**) ; *Portable Network Graphics (PNG) Specification*, ISO/IEC 15948:2004, les chunks `sRGB` et `gAMA` (**sûre**) ; le chunk `eXIf` (**à vérifier** : sa spécification) ; B. Ottosson, « A perceptual color space for image processing », 2020, `https://bottosson.github.io/posts/oklab/` (**sûre**) ; IEC 61966-2-1:1999, sRGB (**sûre**) ; C. E. Duchon, « Lanczos filtering in one and two dimensions », *Journal of Applied Meteorology* 18, 1016–1022 (1979) (**sûre**).

**c. Le déplacement de photocentre par la couleur, pour N sources symétriques.**
- *Ce qui manque.* Les méthodes publiées traitent des paires d'étoiles et des étoiles isolées. Je ne connais aucune étude de N sources colorées en symétrie d'ordre N, ni de l'écart entre un centroïde pesé et un centroïde au-dessus d'un seuil dans ce cas (**à vérifier**).
- *Références.* R. Wielen (1996), le « color-induced displacement » (corpus, XXX § 1.2 ; titre et revue **à vérifier**) ; E. Bertin et S. Arnouts, « SExtractor: Software for source extraction », *Astronomy & Astrophysics Supplement Series* 117, 393–404 (1996) (**sûre**) ; L. Lindegren et al., « Gaia Early Data Release 3: The astrometric solution », *Astronomy & Astrophysics* 649, A2 (2021), pour la calibration chromatique (**sûre** pour la référence, la pertinence est **à vérifier**).

**d. Les comptages de pixels d'un disque : la loi des 8R pour un rayon réel et les exposants du cercle de Gauss.**
- *Ce qui manque.* Je ne connais pas d'énoncé publié de 8⌊R + ½⌋ et de 8⌊r⌋ + 4 (**à vérifier** : la littérature des cercles discrets). Pour le cercle de Gauss, les exposants de la partie XVIII sont des préprints ou des résultats anciens : à relire avant de les citer.
- *Références.* M. N. Huxley, « Exponential sums and lattice points III », *Proceedings of the London Mathematical Society* (3) 87, 591–609 (2003), exposant 131/208 (**sûre**) ; J. Bourgain et N. Watt, « Mean square of zeta function, circle problem and divisor problem revisited », arXiv:1709.04340 (2017), exposant 517/824 (corpus, **sûre**) ; X. Li et X. Yang, « An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem », arXiv:2308.14859 (2023), exposant 0,6289 (corpus ; l'exposant est **à vérifier**) ; G. H. Hardy, « On the expression of a number as the sum of two squares », *Quarterly Journal of Mathematics* 46, 263–283 (1915) (**à vérifier** : les pages) ; J. E. Bresenham, « Algorithm for computer control of a digital plotter », *IBM Systems Journal* 4, 25–30 (1965) (**sûre**) ; OEIS A068785, les points entiers dans x² + y² ≤ 10ⁿ (corpus, **sûre**).

**e. Perron sur une grille n × n : les minima en cases et la constante.**
- *Ce qui manque.* Je ne connais pas de table publiée du meilleur nombre de branches par taille de grille, ni de la constante de 2,8/log₂ n (**à vérifier**). XXVIII § 2.5 la borne entre π/2 et π·ln 2.
- *Références.* A. Córdoba, « The Kakeya maximal function and the spherical summation multipliers », *American Journal of Mathematics* 99, 1–22 (1977) (**sûre**) ; U. Keich, « On L^p bounds for Kakeya maximal functions and the Minkowski dimension in R² », *Bulletin of the London Mathematical Society* 31, 213–221 (1999) (**sûre**) ; C. Fefferman, « The multiplier problem for the ball », *Annals of Mathematics* 94, 330–336 (1971) (corpus, **sûre**).

**f. Le seuil du centre d'un diagramme de Venn dessiné sur des pixels.**
- *Ce qui manque.* Aucune analyse publiée du nombre de pixels nécessaires à un Venn simple et symétrique à n courbes, ni de son goulot au centre (**à vérifier**). Le seuil n* = 4π·(s/a)² est une inégalité isopérimétrique ; son application aux dessins de Venn est, à ma connaissance, nouvelle.
- *Références.* F. Ruskey et M. Weston, « A survey of Venn diagrams », *Electronic Journal of Combinatorics*, Dynamic Survey DS5 (corpus, **sûre**) ; B. Grünbaum, « Venn diagrams and independent families of sets », *Mathematics Magazine* 48, 12–23 (1975) (**sûre**) ; J. Griggs, C. E. Killian et C. D. Savage, « Venn diagrams and symmetric chain decompositions in the Boolean lattice », *Electronic Journal of Combinatorics* 11, R2 (2004) (corpus, **sûre**) ; R. Osserman, « The isoperimetric inequality », *Bulletin of the American Mathematical Society* 84, 1182–1238 (1978) (**sûre**).

**g. L'étoile de Siemens, le critère de Nyquist et la défocalisation.**
- *Ce qui manque.* Les normes d'image emploient l'étoile pour mesurer une résolution ; elles ne la lient pas au nombre de rayons d'un dessin. L'usage de l'étoile dans ISO 12233 est cité par la partie XVIII d'après un article d'Imatest (**à vérifier** à la source).
- *Références.* C. E. Shannon, « Communication in the presence of noise », *Proceedings of the IRE* 37, 10–21 (1949) (**sûre**) ; H. H. Hopkins, « The frequency response of a defocused optical system », *Proceedings of the Royal Society of London A* 231, 91–103 (1955) (**sûre**) ; ISO 12233:2017 (l'existence est **sûre**, le contenu sur l'étoile **à vérifier**).

**h. Le drizzle avec des sources de couleurs inégales.**
- *Ce qui manque.* XXX § 6.1 laisse ouvert l'usage des 17 copies pesées différemment comme 17 éclairages structurés. Je ne connais pas de travail qui le fasse (**à vérifier**).
- *Références.* A. S. Fruchter et R. N. Hook, « Drizzle: A Method for the Linear Reconstruction of Undersampled Images », *Publications of the Astronomical Society of the Pacific* 114, 144–152 (2002) (**sûre**) ; M. G. L. Gustafsson, « Surpassing the lateral resolution limit by a factor of two using structured illumination microscopy », *Journal of Microscopy* 198, 82–87 (2000) (**sûre**).

---

## 7. Le code minimal du test T4 (K6)

### 7.1 Ce qui existe déjà, et ce que j'ajoute

`scripts/revision_001.py` a déjà, aux sections 4.8 et 4.9 : le classement des pixels par teinte (17 teintes de la palette du traceur, clarté L > fond + 0,1, chroma > 0,04 puis 0,06, distance de teinte < 6°), l'aire visible A_i et le moment M_i de chaque classe, le test de montée cyclique (coefficient de Spearman contre 2 000 permutations des A_i), le balayage du seuil de 0,001 à 0,40, la valeur de 0,37 px, le test signé/non signé et la moitié refaite à six seuils. Je ne le refais pas. Je l'ai contrôlé : sur des témoins dont l'ordre est connu, son test a de la puissance (§ 3.5.2). Rien à y changer.

Ce que le code ci-dessous ajoute, et que 4.8 n'a pas :

1. **Un contraste différentiel** : pour chaque rotation de k crans, la part des pixels dont l'image tournée n'est pas de la classe attendue, comparée à celle de la rotation de n − k crans. Il annule au premier ordre la dépendance à la palette. Son erreur vient du rééchantillonnage des n secteurs angulaires.
2. **Des témoins** : des PNG réels dont l'ordre est connu (les dessins à 13 et 11 courbes du traceur, rendus depuis le SVG dans l'ordre 0 → n − 1), et des témoins construits (une courbe du dessin à 13 courbes tournée 17 fois, rendue comme `raster_png` dans trois ordres avec deux palettes).
3. **Une palette à luminance constante** (`palette(Y0=…)`) à côté de la palette à clarté constante du traceur (`palette(L=…)`).
4. **Un verdict calibré** : la distance de l'image au témoin sans ordre et au témoin dessiné de 0 à 16, en écarts-types.
5. **L'ajustement des quatre pesées** par un seul facteur complexe G (§ 7.4).

Il ne lance aucun code de Dzoba : le PNG et le SVG sont lus comme des données. Il demande numpy, scipy et Pillow, et tourne en 30 s environ. Le script de révision dure déjà ≈ 80 s ; T4 bis s'y ajoute. Pour le raccourcir, on peut ne garder que la palette Y₀ = 0,30 et mettre `rep=60` pour l'image.

### 7.2 Ce que j'ai obtenu en l'exécutant (A, hors dépôt)

```text
image à 17 courbes : C = -5.97 % ± 1.46 %
témoin réel venn-13-color.svg.png (0 -> 12) : C = +14.78 % ± 0.72 %
témoin réel venn-11-color.svg.png (0 -> 10) : C = +8.55 % ± 0.40 %
témoin construit, palette L = 0,70, sans ordre : C = -8.00 % ± 1.16 %
témoin construit, palette L = 0,70, opaque 0->16 : C = +13.82 % ± 1.33 %
témoin construit, palette L = 0,70, opaque 16->0 : C = -24.13 % ± 1.05 %
témoin construit, palette Y0 = 0,30, sans ordre : C = -6.41 % ± 1.11 %
témoin construit, palette Y0 = 0,30, opaque 0->16 : C = +15.87 % ± 1.28 %
témoin construit, palette Y0 = 0,30, opaque 16->0 : C = -22.89 % ± 1.05 %
écart de l'image au témoin sans ordre : 0.2 écarts-types ; au témoin 0 -> 16 : 10.0
verdict : pas de signature d'ordre de dessin
```

Et pour l'ajustement du § 7.4 :

```text
palette Y0 = 0,30 : G = 180.7 px à -99.7° ; RMS = 2.03 px ; prédit Y 0.15, L 3.82, MO 32.61, E 46.29 px ; observé Y 0.61, L 4.51, MO 33.07, E 46.07
palette Y0 = 0,34 : G = 189.6 px à -100.8° ; RMS = 1.64 px ; prédit Y 0.10, L 3.65, MO 33.39, E 45.80 px ; observé Y 0.61, L 4.51, MO 33.07, E 46.07
palette L = 0,70 : G = 205.4 px à -94.3° ; RMS = 6.23 px ; prédit Y 10.39, L 0.03, MO 32.81, E 43.56 px ; observé Y 0.61, L 4.51, MO 33.07, E 46.07
```

Ce sont mes sorties, produites hors du dépôt. Ce dossier ne les donne pas comme des résultats du dépôt : le script de révision les recalculera et `resultats/revision_001.md` les portera.

### 7.3 Le code de T4 (le contraste d'ordre et ses témoins)

```python
# T4 bis : l'ordre de dessin des courbes, par un contraste calibré sur des témoins.
# Dépendances : numpy, scipy, PIL. Aucun code de Dzoba n'est lancé : le PNG et le SVG sont lus comme des données.
import math
import re
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

PNG17 = "/home/user/dzoba/venn17/images/venn17-pressure-dark-2000.png"
SVG13 = "/home/user/dzoba/venn17/plotter/venn-13-color.svg"
C_SYM = (999.497, 999.499)                  # centre de symétrie, resultats/centre_venn.md, § 1
FOND, N = (6, 6, 10), 17                     # fond exact de l'image (revision_001.py, § 4.9)
TEINTES = (25 + 360 * np.arange(N) / N) % 360   # plotter_svg.py, palette() : h_i = 25° + 360°·i/n


# --- couleur ---------------------------------------------------------------------------------------------------------
def oklab_ab(S):
    """sRGB 0-255 (tableau ... x 3) -> (a, b) OKLab."""
    lin = S / 255.0
    lin = np.where(lin <= 0.04045, lin / 12.92, ((lin + 0.055) / 1.055) ** 2.4)
    l_ = np.cbrt(0.4122214708 * lin[..., 0] + 0.5363325363 * lin[..., 1] + 0.0514459929 * lin[..., 2])
    m_ = np.cbrt(0.2119034982 * lin[..., 0] + 0.6806995451 * lin[..., 1] + 0.1073969566 * lin[..., 2])
    s_ = np.cbrt(0.0883024619 * lin[..., 0] + 0.2817188376 * lin[..., 1] + 0.6299787005 * lin[..., 2])
    return (1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
            0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_)


def champ_teinte(S, fond):
    """Champ complexe a + i b (OKLab), fond retranché, lissé de 1 px."""
    A, B = oklab_ab(S)
    fa, fb = [float(v[0, 0]) for v in oklab_ab(np.array(fond, float)[None, None, :])]
    return ndimage.gaussian_filter(A - fa, 1.0) + 1j * ndimage.gaussian_filter(B - fb, 1.0)


def oklch_lin(L, C, h):
    h = math.radians(h)
    a, b = C * math.cos(h), C * math.sin(h)
    l_, m_, s_ = L + 0.3963377774 * a + 0.2158037573 * b, L - 0.1055613458 * a - 0.0638541728 * b, L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
            -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)


def palette(n=N, L=0.58, Y0=None, Cmax=0.22, h0=25.0):
    """Reprise de palette() de plotter_svg.py (L constant). Avec Y0 : la clarté L est cherchée, teinte par teinte, pour que
    la luminance relative Y vaille Y0 (palette « à luminance constante »)."""
    def chroma(L_, h):
        lo, hi = 0.0, Cmax
        for _ in range(28):
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if all(-1e-6 <= c <= 1 + 1e-6 for c in oklch_lin(L_, mid, h)) else (lo, mid)
        return lo
    g = lambda c: 12.92 * c if c <= 0.0031308 else 1.055 * max(c, 0) ** (1 / 2.4) - 0.055
    out = []
    for i in range(n):
        h = h0 + 360.0 * i / n
        if Y0 is not None:
            lo, hi = 0.2, 0.98
            for _ in range(40):
                L = 0.5 * (lo + hi)
                r, v, b = oklch_lin(L, chroma(L, h), h)
                lo, hi = (L, hi) if 0.2126 * r + 0.7152 * v + 0.0722 * b < Y0 else (lo, L)
            L = 0.5 * (lo + hi)
        out.append(tuple(int(round(255 * min(1, max(0, g(c))))) for c in oklch_lin(L, chroma(L, h), h)))
    return out


# --- la statistique --------------------------------------------------------------------------------------------------
def contraste_ordre(V, centre, n=N, chroma=0.04, rmin=0.04, rmax=0.93, rep=200, graine=0):
    """m_k(i) : part des pixels de classe de teinte i dont l'image tournée de k crans n'est pas de classe i + k.
    Sans ordre de dessin, m_k(i) = m_(n-k)(i + k) (la même paire de teintes).  Un ordre 0 -> n-1 ajoute un écart d_k(i) > 0
    pour les classes i >= n - k (les paires qui passent le bord du tour) et < 0 sinon.
    C = moyenne_k [ moyenne_(i >= n-k) d_k(i) - moyenne_(i < n-k) d_k(i) ] ; erreur : rééchantillonnage des n secteurs."""
    H, W = V.shape
    yy, xx = np.mgrid[0:H, 0:W].astype(float)
    x, y = xx - centre[0], centre[1] - yy
    R = 0.5 * min(H, W)
    r = np.hypot(x, y)
    teintes = (25 + 360 * np.arange(n) / n) % 360                 # plotter_svg.py, palette() : h_i = 25° + 360°·i/n
    valide = (r > rmin * R) & (r < rmax * R) & (np.abs(V) > chroma)
    classe = np.argmin(np.abs(((np.degrees(np.angle(V)) % 360)[..., None] - teintes + 180) % 360 - 180), -1)
    secteur = (((np.arctan2(y, x) + np.pi) / (2 * np.pi) * n).astype(int)) % n
    tot, mauv = np.zeros((n, n, n)), np.zeros((n, n, n))         # [k][classe][secteur]
    for k in range(1, n):
        th = 2 * math.pi * k / n
        c, s = math.cos(th), math.sin(th)
        col = np.rint(x * c - y * s + centre[0]).astype(int)
        lig = np.rint(centre[1] - (x * s + y * c)).astype(int)
        ok = (lig >= 0) & (lig < H) & (col >= 0) & (col < W)
        lig, col = np.clip(lig, 0, H - 1), np.clip(col, 0, W - 1)
        deux = valide & ok & valide[lig, col]
        mal = deux & (classe[lig, col] != (classe + k) % n)
        tot[k] = np.bincount((classe[deux] * n + secteur[deux]).astype(int), minlength=n * n).reshape(n, n)
        mauv[k] = np.bincount((classe[mal] * n + secteur[mal]).astype(int), minlength=n * n).reshape(n, n)

    def stat(w):
        m = {k: (mauv[k] @ w) / np.maximum(tot[k] @ w, 1) for k in range(1, n)}
        par_k = []
        for k in range(1, n):
            d = np.array([m[k][i] - m[n - k][(i + k) % n] for i in range(n)])
            par_k.append(d[n - k:].mean() - d[:n - k].mean())
        return float(np.mean(par_k))

    rng = np.random.default_rng(graine)
    boot = [stat(np.bincount(rng.integers(0, n, n), minlength=n).astype(float)) for _ in range(rep)]
    return stat(np.ones(n)), float(np.std(boot))


# --- les témoins : une courbe du dessin à 13 courbes du dépôt (SVG lu comme donnée), tournée 17 fois ---------------------
def courbe_svg(chemin, i=0, m=6):
    d = re.findall(r'<path id="curve-%d"[^>]*d="([^"]*)"' % i, open(chemin).read())[0]
    jet = re.findall(r"[MC]|-?[0-9.]+", d)
    pts, cur, k = [], None, 0
    while k < len(jet):
        if jet[k] == "M":
            cur = np.array([float(jet[k + 1]), float(jet[k + 2])]); k += 3
        elif jet[k] == "C":
            k += 1
            while k < len(jet) and jet[k] not in "MC":
                p = [cur] + [np.array([float(jet[k + 2 * j]), float(jet[k + 2 * j + 1])]) for j in range(3)]
                t = np.linspace(0, 1, m, endpoint=False)[:, None]
                pts.append((1 - t) ** 3 * p[0] + 3 * (1 - t) ** 2 * t * p[1] + 3 * (1 - t) * t ** 2 * p[2] + t ** 3 * p[3])
                cur = p[3]; k += 6
        else:
            k += 1
    P = np.vstack(pts + [pts[0][:1]])
    z = (P[:, 0] - 256.0) + 1j * (256.0 - P[:, 1])
    return [np.c_[(z * np.exp(2j * math.pi * j / N)).real + 256, 256 - (z * np.exp(2j * math.pi * j / N)).imag] for j in range(N)]


def temoin(courbes, couleurs, ordre, mode, wpx=600, larg=1.0):
    """Rendu à 2x puis réduction LANCZOS, comme raster_png (lu dans plotter_svg.py).  mode « ordonne » : polylignes opaques
    dans l'ordre donné ; mode « somme » : somme des écarts au fond, qui ne dépend pas de l'ordre."""
    ss, sc = 2, 2 * wpx / 512.0
    fond = np.array(FOND, float)
    def une(i):
        im = Image.new("RGB", (ss * wpx, ss * wpx), FOND)
        ImageDraw.Draw(im).line([(float(x * sc), float(y * sc)) for x, y in courbes[i]], fill=couleurs[i], width=max(1, round(larg * ss)))
        return im
    if mode == "ordonne":
        im = Image.new("RGB", (ss * wpx, ss * wpx), FOND)
        d = ImageDraw.Draw(im)
        for i in ordre:
            d.line([(float(x * sc), float(y * sc)) for x, y in courbes[i]], fill=couleurs[i], width=max(1, round(larg * ss)))
        return np.asarray(im.resize((wpx, wpx), Image.LANCZOS)).astype(float)
    acc = sum(np.asarray(une(i).resize((wpx, wpx), Image.LANCZOS)).astype(float) - fond for i in ordre)
    return np.clip(np.round(fond + acc), 0, 255)


def charge(chemin):
    """PNG -> RGB flottant ; un canal alpha éventuel est posé sur du blanc (les PNG du traceur sont RGBA, fond blanc)."""
    im = Image.open(chemin)
    if im.mode == "RGBA":
        blanc = Image.new("RGBA", im.size, (255, 255, 255, 255))
        blanc.alpha_composite(im)
        im = blanc
    return np.asarray(im.convert("RGB")).astype(float)


if __name__ == "__main__":
    res = {}
    # 1. l'image à 17 courbes
    res["image à 17 courbes"] = contraste_ordre(champ_teinte(charge(PNG17), FOND), C_SYM)
    # 2. des témoins réels : les PNG du traceur, rendus depuis le SVG dans l'ordre 0 -> n-1 (fond blanc, centre 999,5)
    for nom, n in (("venn-13-color.svg.png", 13), ("venn-11-color.svg.png", 11)):
        Sw = charge("/home/user/dzoba/venn17/plotter/" + nom)
        res[f"témoin réel {nom} (0 -> {n - 1})"] = contraste_ordre(champ_teinte(Sw, (255, 255, 255)), (999.5, 999.5), n=n)
    # 3. des témoins construits : une courbe du dessin à 13 courbes, tournée 17 fois, trois ordres, deux palettes
    CRB = courbe_svg(SVG13)
    for nom, coul in (("L = 0,70", palette(L=0.70)), ("Y0 = 0,30", palette(Y0=0.30))):
        for libelle, ordre, mode in (("sans ordre", range(N), "somme"), ("opaque 0->16", range(N), "ordonne"),
                                     ("opaque 16->0", range(N - 1, -1, -1), "ordonne")):
            Ws = temoin(CRB, coul, list(ordre), mode)
            res[f"témoin construit, palette {nom}, {libelle}"] = contraste_ordre(champ_teinte(Ws, FOND), (300.0, 300.0), rep=60)
    for nom, (C, e) in res.items():
        print(f"{nom} : C = {100 * C:+.2f} % ± {100 * e:.2f} %")
    # 4. verdict : l'image est-elle plus proche d'un témoin sans ordre que d'un témoin dessiné de 0 à 16 ?
    Ci, ei = res["image à 17 courbes"]
    ecart = lambda fin: min(abs(Ci - C) / math.hypot(ei, e) for nom, (C, e) in res.items() if nom.endswith(fin))
    d_sans, d_haut = ecart("sans ordre"), ecart("opaque 0->16")
    print(f"écart de l'image au témoin sans ordre : {d_sans:.1f} écarts-types ; au témoin 0 -> 16 : {d_haut:.1f}")
    print("verdict :", "pas de signature d'ordre de dessin" if d_sans < 3 < d_haut else "à examiner")
```

### 7.4 Le code de l'ajustement de la palette (suite du même fichier)

Il donne, pour une palette de conception, les dipôles h des quatre pesées continues (fond retranché), le facteur complexe G qui ajuste les écarts observés (copiés de `resultats/centre_venn.md`, § 1) et le résidu RMS. Pour la clarté constante, il prédit l'inverse de l'observé sur Y et sur L ; pour la luminance constante, il les retrouve.

```python
import cmath

# --- l'ajustement de la palette (suite du même fichier : math, np, palette, C_SYM et FOND sont définis plus haut) ---
OM = np.exp(2j * np.pi * np.arange(17) / 17)
BARY = {"Y": (998.89, 999.58), "L": (996.35, 1002.73), "MO": (967.83, 1009.04), "E": (954.20, 1007.88)}   # centre_venn.md, § 1
OBS = {k: (x - C_SYM[0]) + 1j * (C_SYM[1] - y) for k, (x, y) in BARY.items()}                          # écart en px, y vers le haut


def grandeurs(rgb):
    """Pour une couleur sRGB 0-255 (ou un tableau n x 3) : Y, clarté OKLab L, moyenne des canaux, énergie linéaire."""
    rgb = np.asarray(rgb, float)
    lin = np.where(rgb / 255 <= 0.04045, rgb / 255 / 12.92, ((rgb / 255 + 0.055) / 1.055) ** 2.4)
    lms = np.cbrt(lin @ np.array([[0.4122214708, 0.2119034982, 0.0883024619], [0.5363325363, 0.6806995451, 0.2817188376],
                                  [0.0514459929, 0.1073969566, 0.6299787005]]))
    return {"Y": lin @ np.array([0.2126, 0.7152, 0.0722]), "L": lms @ np.array([0.2104542553, 0.7936177850, -0.0040720468]),
            "MO": rgb.mean(-1), "E": lin.sum(-1)}


def ajuste(couleurs):
    """Écart prédit = G·h, avec h le premier harmonique des poids de conception (fond retranché) et G complexe (moindres carrés)."""
    f, f0 = grandeurs(couleurs), grandeurs(FOND)
    ks = list(OBS)
    h = np.array([((f[k] - f0[k]) @ OM) / (f[k] - f0[k]).sum() for k in ks])
    o = np.array([OBS[k] for k in ks])
    G = (np.conj(h) @ o) / (np.conj(h) @ h)
    return G, dict(zip(ks, h)), float(np.sqrt(np.mean(np.abs(o - G * h) ** 2)))


def affiche_ajustement():
    for nom, coul in (("Y0 = 0,30", palette(Y0=0.30)), ("Y0 = 0,34", palette(Y0=0.34)), ("L = 0,70", palette(L=0.70))):
        G, h, rms = ajuste(coul)
        print(f"palette {nom} : G = {abs(G):.1f} px à {math.degrees(cmath.phase(G)):.1f}° ; RMS = {rms:.2f} px ; prédit " +
              ", ".join(f"{k} {abs(G * h[k]):.2f}" for k in h) + " px ; observé " + ", ".join(f"{k} {abs(OBS[k]):.2f}" for k in h))
```

### 7.5 Comment le brancher dans `scripts/revision_001.py`

- **Où.** Entre les sections 4.8 et 4.9 (une « 4.8 bis »), sous le `else:` qui teste l'existence de `IMG_P`. Réutiliser `IMG_P`, `C_SYM`, `ligne`, `fr` et `ent` du script (le fond (6, 6, 10) n'est calculé qu'en 4.9 : l'écrire en dur ici) ; ne garder des constantes ci-dessus que `SVG13` et le dossier des PNG du traceur, avec un `os.path.exists` pour chacun (le dépôt de Dzoba peut être absent, comme pour 4.8).
- **Les assertions, dans le style du script** : `assert d_sans < 3 < d_haut` (l'image est du côté du témoin sans ordre) ; `assert res["témoin réel venn-13-color.svg.png (0 -> 12)"][0] > 0.10` (le test voit l'ordre d'un vrai rendu) ; `assert ajuste(palette(Y0=0.30))[2] < 3.0 < ajuste(palette(L=0.70))[2]` (la luminance constante ajuste les quatre pesées, la clarté constante non).
- **La ligne du tableau `TESTS`** : `("006 et 007 (T4 bis)", "contraste d'ordre calibré par des témoins réels et construits ; palette isoluminante", f"image {fr(100*Ci, '{:+.1f}')} % ; PNG du traceur +14,8 et +8,6 % ; pas d'ordre de dessin")`.
- **Ce qu'on ne doit pas en conclure.** Que l'image n'a pas été rendue avec des recouvrements : le test dit seulement qu'il n'y a pas de recouvrement *opaque et ordonné* de la forme de `raster_png`. Que la palette de l'image est exactement isoluminante : le modèle ajuste quatre nombres complexes avec un seul, il ne prouve pas la palette. Que le modèle de largeur du § 3.5.5 est validé : il a trois paramètres et un trait inventé.
- **Les limites connues.** Un trait plus fin que 0,5 px affaiblit la discrimination (§ 3.5.3). Le classement par la teinte la plus proche retrouve la bonne courbe pour 67 à 70 % des pixels purs (§ 3.5.2). Le rendu des témoins construits (polylignes opaques à 2× puis `LANCZOS`) est celui de `raster_png`, pas celui du moteur qui a rendu les PNG du traceur (inconnu : `rsvg-convert` ou `qlmanage`) ; les PNG du traceur sont les témoins réels.

---

## 8. Les corrections au recouvrement (bloc JSON du § 1.9 du plan)

### 8.1 La proposition

```json
"grain-pixels-centres": {
  "parties": ["X", "XIV", "XV", "XVIII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXIX", "XXX"],
  "fiches": ["001", "003", "006", "007", "008", "011"]
}
```

- **À ajouter, parties** : XXIV, XXV, XXVI, XXVII.
- **À ajouter, fiches** : 003.
- **À retirer** : rien.
- **Projection (§ 1.10 du plan)** : `"grain-pixels-centres": {"D3": 0.50, "D7": 0.14, "D4": 0.10, "D5": 0.08, "D1": 0.07, "D6": 0.05, "D2": 0.03, "D8": 0.03}` (§ 1.3).

### 8.2 Les raisons

| ajout | sections lues | raison |
|---|---|---|
| **XXIV** | § 2 et § 5 | la lecture du grain en longueur ou en aire : le diamètre d'Euclide (2 − r² = 2x₀), la table des lectures κ, et la divergence en 1/ln √2. Sans elle, le « cran de lecture » du § 3.3 n'a pas de source ; le plan l'écrit pour XXIII § 7 (« ouvert »), XXIV § 5 le ferme |
| **XXV** | § 1.1, § 1.2 et § 1.5 | la série coupée au mieux (1,03·2^(−n/2)/n, ligne 7 du tableau des taux de change), Borel–Padé (6·10⁻¹⁰ à n = 2 contre 0,32 : un cas de fenêtre trop étroite, § 3.6, ligne 9) et l'unité du grain comme angle |
| **XXVI** | § 1.2 et § 1.3 | Kakeya au grain δ : la borne de Córdoba avec sa constante (1,127 + 1,466·k) et les constructions (ligne 8). La question 3 du plan demande « le logarithme » : sa ligne vient de XXV et de XXVI |
| **XXVII** | § 3 | l'échelle des taux de change, que le § 3.3 complète : « le logarithme est la marche 0 ». Le plan la cite dans « Ce qui les réunit » (§ 1.4 : « partie XXVII, § 3 ») et ne la met pas dans le JSON |
| **fiche 003** | — | la quantité n·tan(π/n) de K10 ; 2 856 ppm est le défaut isopérimétrique du 34-gone (§ 4.6) |

**Rien à retirer.** Chaque partie de la liste du plan porte un maillon de § 2.1 (X : M1 à M3 ; XIV : M1 à M3 ; XV : M1 et M2 ; XVIII : M1 à M5 ; XXIII : M1 à M3 ; XXIX : M1 à M4 ; XXX : M1 à M5), et chaque fiche est jugée au § 4. La fiche 001 reste : elle donne le grain naturel du Venn et l'échange bit/chiffre (ligne 21).

### 8.3 Ce que ça change dans le nerf (calculé par l'agent, hors dépôt, à refaire par T1)

J'ai recalculé le nerf du JSON v1 (les huit dossiers) avec les définitions du plan : une paire est sécante si elle partage une partie ou une fiche ; un triangle est vide si les trois paires sont sécantes et qu'aucun élément n'est commun aux trois. Je retrouve les nombres de l'agent `corde` pour la v1 (18 paires et 9 triangles vides au niveau des fiches ; 28 et 20 au niveau « fiches + parties »).

| recouvrement de `grain` | niveau « fiches » : paires sécantes sur 28, triangles vides | niveau « fiches + parties » : paires, triangles vides |
|---|---|---|
| v1 du plan | 18, 9 | 28, 20 |
| + XXVII | 18, 9 | 28, 18 |
| + XXV, XXVI, XXVII | 18, 9 | 28, 15 |
| + XXIV, XXV, XXVI, XXVII | 18, 9 | 28, 13 |
| + fiche 003 seule | 18, 6 | 28, 18 |
| **+ XXIV à XXVII et fiche 003 (proposition)** | **18, 6** | **28, 13** |
| proposition, plus 001 dans `ombres` | 18, 5 | 28, 13 |
| proposition, plus 001 dans `ombres` et dans `methode` | 18, 4 | 28, 12 |
| idem, plus N5 partagée par `grain`, `lumiere`, `methode` | 18, 3 | 28, 12 |
| sans la fiche 001 (pour mémoire) | 17, 7 | 28, 20 |

- **Les quatre parties sont un gain net** : 20 triangles vides tombent à 13 au niveau « fiches + parties », sans rien changer au niveau des fiches.
- **La fiche 003 remplit trois triangles du niveau des fiches** : (grain, aiguilles, ombres), (grain, aiguilles, méthode) et (grain, ombres, méthode). Elle n'en crée aucun et ne crée aucune paire nouvelle. Contrairement à l'ajout de 003 et de 011 au dossier `corde` (qui crée cinq triangles vides), ici l'ajout est gratuit.
- **Les trois triangles du niveau des fiches qui contiennent encore `grain`** (avec la proposition) sont (bases, grain, ombres), (bases, grain, méthode) et (grain, lumière, méthode). Ce sont, par construction, des fiches qui manquent. Trois réponses simples, hors de mon JSON : la fiche 001 dans `ombres-cube-venn` (son grain est celui du Venn, XXIX § 2.1) et dans `hasard-et-methode` (c'est le cas E2 du banc d'essai de XXX § 7 : une identité exacte) ; la fiche proposée N5 (les variables cachées de l'image) dans `grain`, `lumiere` et `methode`. Avec les trois, il ne reste que trois triangles sans `grain` : (corde, moities, bases), (corde, bases, ombres) et (lumiere, ombres, methode).
- **Réserve (le plan la fait déjà pour T8).** Le recouvrement a été fait en lisant des résumés qui contiennent les renvois : ces nombres ne sont pas indépendants des parties. Partager d'autres fiches nouvelles entre plusieurs dossiers crée aussi des paires sécantes, donc des triangles vides : j'ai essayé (N1 à N6 partagées comme au § 6.1) et le niveau des fiches monte à 22 paires et 13 triangles vides. C'est une information sur ce qui manque, pas un défaut ; je laisse le choix à l'agent `croisement`.

---

## Annexe : les chemins cités

J'ai vérifié par `ls` l'existence de chaque document, script, fichier de résultats, figure et fiche cités dans ce dossier (script de contrôle hors dépôt) ; les fichiers de `/home/user/dzoba/venn17` (README, `plotter/plotter_svg.py`, `plotter/venn-13-color.svg`, `plotter/venn-13-color.svg.png`, `plotter/venn-11-color.svg.png`, `images/venn13-spread.png`, `images/venn17-pressure-dark-2000.png`, `images/venn17-rose-dark-2000.png`, `paper/venn17-19.tex`) existent aussi. Aucun fichier n'a été écrit dans le dépôt, hormis celui-ci.
