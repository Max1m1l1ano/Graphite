# 007 — Mon premier centre était faux de 2,36 px : le biais venait du point de départ

| champ | valeur |
|---|---|
| type | Causalité |
| statut | exact (refait : la recherche s'arrête au bord de ses deux fenêtres) |
| partie | XXX |
| document | [centre-venn.md](../../centre-venn.md), § 1.3 |
| script | [`scripts/centre_venn.py`](../../scripts/centre_venn.py), fonction `centre_grossier` |
| données | [`resultats/centre_venn.md`](../../resultats/centre_venn.md) |
| image | [`ae3_grains_hasard.png`](../../figures/ae3_grains_hasard.png), panneaux b (encart) et c (étoile rouge) |
| dimension | D7 hasard et méthode ; puis, à la révision 001 : D3 grain, pixels et précision |
| test | refaire l'essai tel quel, puis la recherche fine sur le même masque (0,004 px) |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | 001 (2026-10-09) |

## Le contexte qui précède

Ma phrase « le vrai centre ne se trouve qu'à 2 px du trou central » minimisait un écart ; l'auteur l'a relevé.

## L'observation

L'essai grossier partait du barycentre biaisé (13,6 px) et cherchait à ±8 px puis ±2 px : il s'est arrêté au bord de ses deux fenêtres. Le biais du barycentre s'était propagé à la recherche de la symétrie. Autour de ce centre, l'empilement des 17 copies perd 76,2 % de son information commune.

## Ce que le script produit

`centre_grossier` refait l'essai à l'identique ; `incoherence` mesure l'empilement autour de chaque centre.

## Liens et pistes

Fiche 006. Leçon : un point de départ biaisé et une fenêtre trop étroite fabriquent un faux résultat qui a l'air précis.

## Révision 001

Synthèse : [revision-001.md](../revisions/revision-001.md).
- Une autre erreur de chaîne de mesure est trouvée par la révision : le seuil (fiche 018).
- Dossier [grain](../dossiers/grain-pixels-centres.md) : lien fort, de méthode : la fiche est le premier cas d'une famille de douze chaînes (trois encore ouvertes).
