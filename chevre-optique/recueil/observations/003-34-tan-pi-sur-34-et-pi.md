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
| dimension | D6 sphères, cubes, Venn et symétries |
| test | variation du paramètre : l'écart fois N² tend vers π³/12 = 2,5839 (2,5927 pour N = 17, puis 2,5839 pour N = 170 et 1 700) |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | non |

## Le contexte qui précède

Même test que la fiche 002 : le 34-gone circonscrit des 17 éventails de Perron (partie XXVIII) a un périmètre de 34·tan(π/34), à comparer à π.

## L'observation

Trois des quatre tests à tolérance (Bonferroni, catalogue brouillé, longueur de description) le déclarent « hasard », alors que c'est le polygone qui tend vers le cercle.

## Ce que le script produit

Le banc d'essai de la partie XXX calcule les verdicts des six techniques, puis la loi de l'écart pour N = 17, 170 et 1 700.

## Liens et pistes

Fiche 012 (la leçon de méthode) ; partie XXVIII (N éventails donnent le polygone circonscrit à 2N côtés).

Dimensions voisines, à confirmer à la révision : D7 hasard et méthode.
