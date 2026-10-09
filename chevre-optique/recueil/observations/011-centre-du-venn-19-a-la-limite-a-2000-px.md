# 011 — À 2 000 px et 2 px par croisement, le centre du Venn à 19 courbes est à la limite

| champ | valeur |
|---|---|
| type | Fait amusant ; Corrélation |
| statut | calculé (le centre résout jusqu'à n = 18,99 ; il faut 2 009 px pour 19) |
| partie | XXX |
| document | [centre-venn.md](../../centre-venn.md), § 6.4 |
| script | [`scripts/centre_venn.py`](../../scripts/centre_venn.py), section 6 (granularité) |
| données | [`resultats/centre_venn.md`](../../resultats/centre_venn.md) |
| image | [`ae3_grains_hasard.png`](../../figures/ae3_grains_hasard.png), panneau e |
| dimension | D3 grain, pixels et précision ; puis, à la révision 001 : D5 Kakeya, Perron et aiguilles, D6 sphères, cubes, Venn et symétries |
| test | loi : W_centre(n) = (2/π)·√(n(2ⁿ − 2)) contre W_reste(n) = 4·√((2ⁿ − 2)/π) |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | 001 (2026-10-09) |

## Le contexte qui précède

L'auteur demande d'aller « encore plus près du centre », en tenant compte des limites de granularité.

## L'observation

Le centre devient le goulot dès 13 courbes, et de plus en plus : l'écart croît comme √n. Le dessin de Dzoba élargit son trou (14,6 px au lieu de 11,2) pour garder 5,4 px entre les croisements centraux.

## Ce que le script produit

Le script calcule les deux largeurs nécessaires de n = 11 à 25, et la limite à 2 000 et 8 000 px, avec et sans repositionnement des grains.

## Liens et pistes

Partie XIV (Perron sur une grille ne descend plus à zéro) ; partie XVIII (le disque de confusion de l'étoile de Siemens).

## Révision 001

Synthèse : [revision-001.md](../revisions/revision-001.md).
- Test 4.4 (K10) : le seuil des 13 courbes est la constante isopérimétrique 4π (fiche 020). Il vaut 4π·(s/a)² et dépend du choix a = s = 2 px (dossier grain). De même, les 18,99 courbes à 2 000 px dépendent des 2 px d'arc par croisement : 19,76 courbes à 1,5 px, 17,90 à 3 px (revision_001.py, § 4.10 ; dossier méthode). « Pile à la limite » ne tient qu'avec ce critère : le titre est précisé.
- Dossier [corde](../dossiers/corde-et-dimensions.md) : ajoutée au dossier par son agent : K10 exact ; troisième série de T3 (cordes) ; obstruction à l'ordre 4.
- Dossier [grain](../dossiers/grain-pixels-centres.md) : lien fort et exact : c'est le cas n = 19 de K10.
- Dossier [aiguilles](../dossiers/aiguilles-kakeya-perron.md) : calculé, juste ; place dans les arbres : P5 (branche du Venn : XXIX § 4, XXX § 6.4, fiche 011) et P3 par K10 (seuil √(n/4π)) ; pas dans P1. K7 précise le lien « à un cran près » : +2,6 % par courbe au centre à n = 19.
- Dossier [méthode](../dossiers/hasard-et-methode.md) : bon test ; la loi tient, « pile à la limite » dépasse le test.
