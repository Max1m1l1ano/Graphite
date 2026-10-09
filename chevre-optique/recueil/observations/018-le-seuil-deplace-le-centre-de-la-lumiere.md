# 018 — Le seuil déplace le centre de la lumière, mais pas la moitié : la couleur agit par le poids et par la largeur visible

| champ | valeur |
|---|---|
| type | Causalité ; Corrélation ; Analogie |
| statut | calculé (mesure : le centre de symétrie est connu à 0,003 px ; sans seuil, l'encre est centrée à 0,044 px ; avec le seuil t, l'écart monte de 0,1 à 27,4 px ; la moitié reste entre 49,3 et 49,7 %) |
| partie | révision 001 (partie XXX) |
| document | [revision-001.md](../revisions/revision-001.md), § 3 et 7 ; [centre-venn.md](../../centre-venn.md), § 1 et 2 |
| script | [`scripts/revision_001.py`](../../scripts/revision_001.py), sections 4.8 et 4.9 ; [`scripts/centre_venn.py`](../../scripts/centre_venn.py), section 1 (liste `POIDS`) et fonction `mesure_moitie` |
| données | [`resultats/revision_001.md`](../../resultats/revision_001.md), § 4.8 et 4.9 |
| image | [`rev001_diagonale_cadre.png`](../../figures/rev001_diagonale_cadre.png), panneau c ; l'image mesurée est `venn17-pressure-dark-2000.png` du dépôt de Dzoba (copie locale) |
| dimension | D3 grain, pixels et précision |
| test | mesure contre le budget de grain, puis variation du seuil (0,001 à 0,40) ; l'ordre de dessin est écarté par un nul de permutations (meilleure montée cyclique des aires visibles : p = 0,64) ; un repli signé/non signé est écarté par l'histogramme des canaux (lisse entre 127 et 128) |
| arc | 2026-10-07, arc 001 (révision 001) |
| révisé | non |

## Le contexte qui précède

La partie XXX a mesuré six centres de la lumière pour la même image du Venn à 17 courbes, de 0,61 px (luminance) à 46 px (énergie linéaire). Elle les a attribués au premier harmonique des poids des 17 couleurs (fiche 006). Le plan de la révision 001 a remarqué que l'ordre des écarts ne suit pas celui des harmoniques (congruence K6), et a proposé une seconde cause : l'ordre de dessin des courbes.

Puis l'auteur a demandé : quel est ce masque binaire ? Un seuil de quoi, dans quel chapitre, quel script, quelle image ? Que vaut 0,37 px ? Serait-ce un passage signé/non signé (−128 … 127, où le 0 déséquilibre les deux côtés), ou les canaux RGB, « 1/3 + 10/3 » ?

## L'observation

- **Le masque.** C'est l'ensemble des pixels dont la clarté perçue OKLab dépasse celle du fond de t (fond : la couleur exacte RGB (6, 6, 10), L = 0,1246). Chaque pixel du masque pèse 1. Il ne voit ni la palette ni l'ordre de dessin, et pourtant son centre bouge avec t.
- **0,37 px.** C'est l'écart à t = 0,02, un point du balayage et pas une constante. Sans aucun seuil, l'encre est centrée à 0,044 px ; jusqu'à t = 0,01, l'écart reste au niveau du bruit (0,06 à 0,12 px) ; ensuite, il monte jusqu'à 27,4 px à t = 0,40, toujours vers −100° à −136°.
- **Ce n'est pas un passage signé/non signé.** L'image est en octets non signés (0 à 255), l'histogramme des canaux est lisse entre 127 et 128, et le calcul ne passe jamais par des entiers signés.
- **Le zéro qui déséquilibre existe pourtant dans l'image.** Un axe de 2 000 pixels a son milieu entre deux pixels (999,5), comme −128 … 127 a le sien en −0,5. Prendre 1 000 pour centre donnerait un biais fixe de √2/2 = 0,707 px vers +135°. Le dessin respecte la bonne convention (centre mesuré en 999,497 ; 999,499), et le masque ne suit pas ce biais : sa direction est opposée en hauteur et sa taille varie. Il passe par 0,71 px à t = 0,05, une dérive qui croise une constante (comme la fiche 021).
- **Le 10/3.** Le fond n'est pas un zéro neutre : sa moyenne RGB vaut 22/3, dont 10/3 viennent du bleu. Uniforme, ce décalage n'a pas de dipôle ; il n'agit qu'aux bords anticrénelés, où chaque courbe se mélange au fond bleuté, donc à travers le seuil.
- **La seconde cause est le seuil.** Il change la couleur en largeur visible. La couleur déplace donc le centre par deux canaux : le poids et le seuil.
- **Et la moitié ne bouge pas.** Avec le même masque, la part de l'encre dans le contour réduit de 1/√2 reste entre 49,3 et 49,7 % pour t = 0,005 à 0,3, alors que la quantité d'encre passe de 81 à 19 %. Le seuil touche le premier harmonique (le centre), pas l'harmonique zéro (la distance au centre, protégée par la rotation d'ordre 17). Le résultat de la partie XXX sur la moitié est robuste au cadre ; ses centres de la lumière ne le sont pas.

## Ce que le script produit

Les sections 4.8 et 4.9 de `scripts/revision_001.py` :
- classent les pixels par teinte (les 17 teintes de la palette du traceur, lue sans l'exécuter), mesurent l'aire et le moment de chaque courbe et testent une montée cyclique des aires contre 2 000 permutations ;
- lisent le fond exact et les histogrammes des canaux ;
- balaient le seuil du masque de 0,001 à 0,40 ;
- refont la mesure de la moitié de la partie XXX à six seuils.

## Liens et pistes

- Les fiches liées :
  - la fiche 006 : son analogie tient, sa causalité gagne un canal ;
  - la fiche 007 : une autre erreur de chaîne de mesure ;
  - la fiche 017 : le cadre fabrique des liens ; ici, il fabrique un déplacement ;
  - la fiche 021 : une dérive qui croise des constantes.
- En astrométrie, on retrouve la même différence entre un centroïde isophote (au-dessus d'un seuil) et un centroïde pondéré (Bertin et Arnouts, SExtractor, 1996). C'est aussi la raison des corrections de chromaticité des catalogues (Gaia ; référence exacte à vérifier).
- Les pistes :
  - refaire la mesure sur le rendu « rose » du dépôt (`venn17-rose-dark-2000.png`), à seuil variable ;
  - faire un rendu sur un fond neutre, pour séparer l'effet du fond bleuté.

Dimensions voisines, à confirmer à la révision : D7 hasard et méthode (une erreur de chaîne de mesure) ; D8 physique (le photocentre).
