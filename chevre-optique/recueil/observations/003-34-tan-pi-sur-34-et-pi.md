# 003 — 34·tan(π/34) ≈ π, à 2 856 ppm : un lien de structure

| champ | valeur |
|---|---|
| type | Coïncidence ; Corrélation |
| statut | structure (loi de l'écart : π³/(12N²)) |
| partie | XXIX et XXX |
| document | [venn-ppm.md](../../venn-ppm.md), § 5.5 ; [centre-venn.md](../../centre-venn.md), § 7 |
| script | [`scripts/venn_ppm.py`](../../scripts/venn_ppm.py), section 7 ; [`scripts/centre_venn.py`](../../scripts/centre_venn.py), section 7 |
| données | [`resultats/centre_venn.md`](../../resultats/centre_venn.md) |
| image | [`ae3_grains_hasard.png`](../../figures/ae3_grains_hasard.png), panneau f |
| dimension | D6 sphères, cubes, Venn et symétries ; puis, à la révision 001 : D7 hasard et méthode, D3 grain, pixels et précision, D4 optique et diffraction, D5 Kakeya, Perron et aiguilles |
| test | variation du paramètre : l'écart fois N² tend vers π³/12 = 2,5839 (2,5927 pour N = 17, puis 2,5839 pour N = 170 et 1 700) |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | 001 (2026-10-09) |

## Le contexte qui précède

Même test que la fiche 002 : le 34-gone circonscrit des 17 éventails de Perron (partie XXVIII) a un périmètre de 34·tan(π/34), à comparer à π.

## L'observation

Trois des quatre tests à tolérance (Bonferroni, catalogue brouillé, longueur de description) le déclarent « hasard », alors que c'est le polygone qui tend vers le cercle.

## Ce que le script produit

Le banc d'essai de la partie XXX calcule les verdicts des six techniques, puis la loi de l'écart pour N = 17, 170 et 1 700.

## Liens et pistes

Fiche 012 (la leçon de méthode) ; partie XXVIII (N éventails donnent le polygone circonscrit à 2N côtés).

## Révision 001

Synthèse : [revision-001.md](../revisions/revision-001.md).
- Test 4.4 (K10) : n·tan(π/n) est la constante isopérimétrique du n-gone régulier ; le seuil du centre du Venn en dépend (fiche 020).
- Dossier [corde](../dossiers/corde-et-dimensions.md) : ajoutée au dossier par son agent : c'est exactement la deuxième série de T3 (polygone circonscrit) ; recollement à l'ordre 2, obstruction à l'ordre 4.
- Dossier [grain](../dossiers/grain-pixels-centres.md) : À ajouter au dossier grain-pixels-centres (avec la 011).
- Dossier [aiguilles](../dossiers/aiguilles-kakeya-perron.md) : juste, à garder (structure), et ajoutée à ce dossier : 34·tan(π/34) est le coefficient 2N·tan(π/2N) de la fenêtre de Kakeya à N = 17 éventails (aire du 34-gone circonscrit). Place dans les arbres : P1 (branche Perron : le 34-gone est le contour de l'ombre Σωⁱ du cube) et P3 (branche du polygone circonscrit : forme x³/3 de tan contre x³/6 de sin pour la fiche 002 ; lecture de l'agent). Rôle dans ce dossier : le prix du nombre d'éventails, 0,29 % de π, contre une fenêtre large de 56 % à 10⁻⁵⁰.
- Dossier [lumière](../dossiers/lumiere-et-physique.md) : à ajouter au dossier : le 34-gone circonscrit est le pendant de la lumière du polygone inscrit de la fiche 002 (arbre P3).
