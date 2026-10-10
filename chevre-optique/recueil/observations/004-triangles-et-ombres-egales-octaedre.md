# 004 — La part des triangles (35,8 %) frôle les 35,10 % de l'octaèdre

| champ | valeur |
|---|---|
| type | Coïncidence ; Hasard |
| statut | hasard (testé) |
| partie | XXIX et XXX |
| document | [venn-ppm.md](../../venn-ppm.md), § 2.2 et § 5.5 ; [centre-venn.md](../../centre-venn.md), § 7 |
| script | [`scripts/venn_ppm.py`](../../scripts/venn_ppm.py), section 2 (texture) ; [`scripts/centre_venn.py`](../../scripts/centre_venn.py), section 7 |
| données | [`resultats/venn_ppm.md`](../../resultats/venn_ppm.md) |
| image | [`ad1_venn_ppm.png`](../../figures/ad1_venn_ppm.png), panneau d ; [`ae3_grains_hasard.png`](../../figures/ae3_grains_hasard.png), panneau f |
| dimension | D7 hasard et méthode ; puis, à la révision 001 : D6 sphères, cubes, Venn et symétries |
| test | variation du paramètre : 36,0, 37,3, 35,8 et 35,7 % pour 11, 13, 17 et 19 courbes, un certificat par n (à 17 courbes, les quatre certificats vont de 35,3 à 36,7 % : dossiers ombres et méthode, (A)) ; rien ne suit 35,10 % |
| arc | 2026-10-07, parties XXIX et XXX (avant le recueil) |
| révisé | 001 (2026-10-09) |

## Le contexte qui précède

La texture des Venn de Dzoba (la part des régions à 3, 4, 5… coins) ne dépend presque pas du nombre de courbes. La partie XXVIII avait trouvé que l'ombre de l'octaèdre égale celle du cube sur 35,10 % des directions.

## L'observation

Les deux pourcentages sont à 1,9 % l'un de l'autre.

## Ce que le script produit

La texture vient des certificats (partie XXIX), et le verdict du banc d'essai et de la variation (partie XXX).

## Liens et pistes

Fiche 002 (même test).

## Révision 001

Synthèse : [revision-001.md](../revisions/revision-001.md).
- La part des triangles dérive avec n : 35,95 ; 35,76 ; 35,12 % à 17, 19 et 23 courbes (dossier ombres ; à 23, les cinq comptes publiés par Dzoba). Elle passe par les 35,10 % de l'octaèdre vers 23 courbes : une dérive qui croise une constante, comme la fiche 021. Les droites tirées au hasard en donnent 2 − π²/6 = 35,51 % (Miles, 1964, à vérifier) : un étalon possible (dossiers ombres et méthode).
- Dossier [méthode](../dossiers/hasard-et-methode.md) : bon test (variation sur n), mais sans le point n = 23 ; le verdict tient, à suivre.
- Dossier [ombres](../dossiers/ombres-cube-venn.md) : hasard (testé), maintenu.
