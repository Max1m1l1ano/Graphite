# 011 — À 2 000 px, le centre du Venn à 19 courbes est pile à la limite

| champ | valeur |
|---|---|
| type | Fait amusant ; Corrélation |
| statut | calculé (le centre résout jusqu'à n = 18,99 ; il faut 2 009 px pour 19) |
| partie | XXX |
| document | [centre-venn.md](../../centre-venn.md), § 6.4 |
| script | [`scripts/centre_venn.py`](../../scripts/centre_venn.py), section 6 (granularité) |
| données | [`resultats/centre_venn.md`](../../resultats/centre_venn.md) |
| image | [`ae3_grains_hasard.png`](../../figures/ae3_grains_hasard.png), panneau e |
| dimension | D3 grain, pixels et précision |
| test | loi : W_centre(n) = (2/π)·√(n(2ⁿ − 2)) contre W_reste(n) = 4·√((2ⁿ − 2)/π) |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | non |

## Le contexte qui précède

L'auteur demande d'aller « encore plus près du centre », en tenant compte des limites de granularité.

## L'observation

Le centre devient le goulot dès 13 courbes, et de plus en plus : l'écart croît comme √n. Le dessin de Dzoba élargit son trou (14,6 px au lieu de 11,2) pour garder 5,4 px entre les croisements centraux.

## Ce que le script produit

Le script calcule les deux largeurs nécessaires de n = 11 à 25, et la limite à 2 000 et 8 000 px, avec et sans repositionnement des grains.

## Liens et pistes

Partie XIV (Perron sur une grille ne descend plus à zéro) ; partie XVIII (le disque de confusion de l'étoile de Siemens).

Dimensions voisines, à confirmer à la révision : D5 Perron (le même plafond que Perron sur une grille).
