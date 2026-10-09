# 008 — Le dessin de Dzoba est centré au millième de pixel

| champ | valeur |
|---|---|
| type | Fait amusant |
| statut | calculé (0,004 px ; rotations k = 1, 2, 4, 8 à 0,003 px) |
| partie | XXX |
| document | [centre-venn.md](../../centre-venn.md), § 1.1 |
| script | [`scripts/centre_venn.py`](../../scripts/centre_venn.py), fonction `centre_symetrie` |
| données | [`resultats/centre_venn.md`](../../resultats/centre_venn.md) |
| image | [`ae1_centre_moitie.png`](../../figures/ae1_centre_moitie.png), panneau a |
| dimension | D3 grain, pixels et précision ; puis, à la révision 001 : D6 sphères, cubes, Venn et symétries |
| test | quatre rotations indépendantes donnent le même point |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | 001 (2026-10-09) |

## Le contexte qui précède

On cherche le vrai centre de symétrie d'ordre 17 pour mesurer la moitié et empiler les copies.

## L'observation

Le centre de symétrie est en (999,497 ; 999,499), et le centre exact de l'image en (999,5 ; 999,5). Le vrai centre est au coin de quatre pixels : le plus grand disque vide centré sur un pixel ne peut que s'en approcher à 0,70 px.

## Ce que le script produit

La corrélation de l'image (clarté OKLab) avec ses rotations, cherchée au pas de 2, 0,5 et 0,125 px, puis affinée par un paraboloïde.

## Liens et pistes

Fiches 006 et 007 ; partie IV (le point au centre de la case).

## Révision 001

Synthèse : [revision-001.md](../revisions/revision-001.md).
- Dossier [grain](../dossiers/grain-pixels-centres.md) : lien fort et exact.
- Dossier [méthode](../dossiers/hasard-et-methode.md) : bon test avec réserve ; le verdict tient.
- Dossier [ombres](../dossiers/ombres-cube-venn.md) : calculé.
