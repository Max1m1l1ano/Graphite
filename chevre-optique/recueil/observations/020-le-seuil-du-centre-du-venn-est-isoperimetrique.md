# 020 — Le seuil des 13 courbes est la constante isopérimétrique, et le polygone donne la quantité de la fiche 003

| champ | valeur |
|---|---|
| type | Analogie ; Fait amusant |
| statut | exact (W_centre/W_reste = √(n/(4π)) ; seuil 4π = 12,566 pour un cercle, π/arctan(1/4) = 12,824 pour un polygone) |
| partie | révision 001 (partie XXX) |
| document | [revision-001.md](../revisions/revision-001.md), § 6 et 7 ; [centre-venn.md](../../centre-venn.md), § 6.4 |
| script | [`scripts/revision_001.py`](../../scripts/revision_001.py), section 4.4 |
| données | [`resultats/revision_001.md`](../../resultats/revision_001.md) |
| image | — |
| dimension | D3 grain, pixels et précision |
| test | identité vérifiée par sympy ; variation du modèle (cercle, puis polygone régulier) |
| arc | 2026-10-07, arc 001 (révision 001) |
| révisé | non |

## Le contexte qui précède

La partie XXX a trouvé que le centre du Venn devient le goulot de la granularité « à partir de 13 courbes » (fiche 011), en comparant la largeur d'image nécessaire au centre et au reste. Le plan de la révision a remarqué que leur rapport est √(n/(4π)) (congruence K10).

## L'observation

Le centre doit loger n croisements à 2 px l'un de l'autre sur un cercle (périmètre 2n) et n régions d'au moins 4 px² (aire 4n). Pour un cercle, périmètre² / aire = 4π, la constante isopérimétrique : le seuil vaut exactement n = 4π = 12,566. Si les croisements sont joints par des segments, le centre est un n-gone régulier, dont la constante vaut 4n·tan(π/n) ; le seuil devient n = π/arctan(1/4) = 12,824. Dans les deux cas : 13 courbes. Et n·tan(π/n) est exactement la quantité de la fiche 003 (34·tan(π/34) ≈ π).

**Le 13 dépend d'un choix** (précision du dossier [grain](../dossiers/grain-pixels-centres.md), refaite ici). Pour des croisements espacés de a et des régions de côté s, le seuil vaut n* = 4π·(s/a)². La partie XXX a pris a = s = 2 px, d'où 4π. Avec a/s = 1,5, il tombe à 5,59 courbes ; avec a/s = 0,5, il monte à 50,27. L'isopérimétrie est la loi ; le 13 est le cadre.

## Ce que le script produit

La section 4.4 de `scripts/revision_001.py` vérifie le rapport par sympy et calcule les deux seuils.

## Liens et pistes

Fiche 011 (le centre à sa limite), fiche 003 (le polygone circonscrit des éventails de Perron), partie XVIII (les pixels et le cercle). Piste : le même calcul pour le centre de l'ombre Σωⁱ du cube (partie XXIX, § 5.4).

Dimensions voisines, à confirmer à la révision : D6 sphères, cubes, Venn et symétries (le centre du Venn) ; D1 la chèvre et les cordes (l'isopérimétrie).
