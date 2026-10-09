# 021 — Le rapport des dizaines de premiers croise π à 10⁵ puis 2√2 à 10⁶ : une dérive, pas une constante

| champ | valeur |
|---|---|
| type | Coïncidence ; Hasard |
| statut | hasard (testé : la variation de N montre une dérive de 3,90 à 2,53, vers 2) |
| partie | révision 001 (fiche 015) |
| document | [revision-001.md](../revisions/revision-001.md), § 7 |
| script | [`scripts/revision_001.py`](../../scripts/revision_001.py), section 4.2 |
| données | [`resultats/revision_001.md`](../../resultats/revision_001.md) |
| image | [`rev001_diagonale_cadre.png`](../../figures/rev001_diagonale_cadre.png), panneau d |
| dimension | D2 bases, chiffres et congruences |
| test | variation de la taille N, de 10⁴ à 10⁸ ; la loi (2, Hardy–Littlewood) se lit sur le compte des paires larges |
| arc | 2026-10-07, arc 001 (révision 001) |
| révisé | non |

## Le contexte qui précède

La fiche 015 compte les dizaines de premiers sous 10⁶ : les motifs {1, 7} et {3, 9} (distance 6) sont environ 2,8 fois plus nombreux, motif par motif, que les autres paires. La révision a fait varier N.

## L'observation

Le rapport par motif vaut 3,1448 à 10⁵ (π à 0,10 %) et 2,8321 à 10⁶ (2√2 à 0,13 %), puis 2,63 et 2,53 : il dérive vers 2, en 1/ln N. À une seule taille, chacun des deux passages ressemble à une découverte. Le rapport des paires larges (sans exiger que les deux autres soient composés) reste entre 1,98 et 2,09 de 10⁴ à 10⁸ : c'est la loi, S(6)/S(2) = 2, parce que 3 divise 6.

## Ce que le script produit

La section 4.2 de `scripts/revision_001.py` crible jusqu'à 10⁸ et compte les motifs exacts et les paires larges à chaque taille.

## Liens et pistes

Fiche 015 ; fiche 012 (une grandeur qui dérive passe tous les tests à tolérance à une taille donnée) ; le biais de Tchebychev (Rubinstein et Sarnak, 1994) et le biais des premiers consécutifs (Lemke Oliver et Soundararajan, 2016), deux effets du second ordre longtemps lus comme du bruit ; l'effet de regard ailleurs (Gross et Vitells, 2010). Le dossier [bases](../dossiers/bases-congruences-premiers.md) prolonge le compte jusqu'à 10⁹ : la prédiction de Hardy et Littlewood à taille finie, sans paramètre ajusté, suit la dérive à 0,0005 près (calcul de l'agent, à refaire). Piste : les 16 motifs de la dizaine à 10⁹ et plus, avec leurs termes du second ordre.

Dimensions voisines, à confirmer à la révision : D7 hasard et méthode.
