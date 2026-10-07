# 009 — Ton Venn diffracte comme un diaphragme à 17 lames : 34 + 34 aigrettes

| champ | valeur |
|---|---|
| type | Analogie |
| statut | structure (le contour seul donne les 34 aigrettes de sa famille ; Friedel double l'ordre) |
| partie | XXX |
| document | [centre-venn.md](../../centre-venn.md), § 5 |
| script | [`scripts/centre_venn.py`](../../scripts/centre_venn.py), section 5 |
| données | [`resultats/centre_venn.md`](../../resultats/centre_venn.md) |
| image | [`ae2_diaphragmes_diffraction.png`](../../figures/ae2_diaphragmes_diffraction.png), panneaux e et f |
| dimension | D4 optique et diffraction |
| test | séparer les sources : le masque du contour seul (34 aigrettes, 100 % dans la famille du contour), le cœur seul (85 % dans la seconde) |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | non |

## Le contexte qui précède

L'auteur a vu mes deux images du spectre en noir et blanc : « tes deux images en noir et blanc l'ont capturé ».

## L'observation

Le spectre a 70 aigrettes. 34 viennent du contour à 17 côtés, exactement celles d'une étoile vue à travers un diaphragme à 17 lames (partie XXVIII). Les 36 autres viennent des veines intérieures (34 attendues, plus deux pics de bruit) et sont tournées de 4,0°.

## Ce que le script produit

La transformée de Fourier de l'image, la recherche des pics angulaires et leurs résidus modulo 180°/17, les spectres du contour seul et du cœur seul, et les harmoniques angulaires.

## Liens et pistes

Partie XXVIII (34 aigrettes) ; partie XX (le losange de √2 dans la diffraction) ; partie X (l'ordre 4 des pixels).

Dimensions voisines, à confirmer à la révision : D6 symétries.
