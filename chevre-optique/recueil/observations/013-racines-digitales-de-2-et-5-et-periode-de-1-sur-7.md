# 013 — Les racines digitales de 2ⁿ et 5ⁿ parcourent les chiffres de la période de 1/7

| champ | valeur |
|---|---|
| type | Fait amusant ; Coïncidence |
| statut | exact pour 7 ; la variation échoue pour 13 (l'autre période 6) : propre à 7, mécanisme à trouver |
| partie | recueil |
| document | [resultats/recueil_verifications.md](../../resultats/recueil_verifications.md), § 4 |
| script | [`scripts/recueil_verifications.py`](../../scripts/recueil_verifications.py), section 4 |
| données | [`resultats/recueil_verifications.md`](../../resultats/recueil_verifications.md) |
| image | — |
| dimension | D2 bases, chiffres et congruences ; puis, à la révision 001 : D5 Kakeya, Perron et aiguilles, D7 hasard et méthode |
| test | variation du paramètre : 1/13 a la période 076923, d'autres chiffres |
| arc | 2026-10-07, arc 001 (le recueil : message fondateur du § 10 de CLAUDE.md) |
| révisé | 001 (2026-10-09) |

## Le contexte qui précède

Remarque de l'auteur (7 octobre 2026), dans le message qui fonde la section 10 de CLAUDE.md : « DR 2 et 5 donnent les mêmes chiffres que la période de 1/7 mais pas dans le même ordre, et DR 3 donne 3 et 6 alterné ».

## L'observation

DR(2ⁿ) = 1, 2, 4, 8, 7, 5 et DR(5ⁿ) = 1, 5, 7, 8, 4, 2 parcourent les unités modulo 9. La période de 1/7 est 142857 : le même ensemble, dans un autre ordre. Sous ×2 ou ×5, les racines digitales se rangent en trois orbites : {1, 2, 4, 8, 7, 5}, {3, 6} (en alternance) et {9}.

## Ce que le script produit

Le script vérifie DR(a·b) = DR(DR(a)·DR(b)) sur 100 000 paires, calcule les orbites et compare les périodes de 1/7 et 1/13.

## Liens et pistes

Parties XXVIII (Midy pour 1/17) et XIX (les horloges des derniers chiffres). Piste : les chiffres de 1/7 sont ⌊10r/7⌋ pour r = 1 à 6, ce qui saute justement 3 et 6.

## Révision 001

Synthèse : [revision-001.md](../revisions/revision-001.md).
- Tests 4.1, 4.3 et 4.10 : le lien est propre à la base 10, expliqué par la famille q² + 1 et le lemme des chiffres ; Φ₆(10) = 7 × 13 explique la fausse piste de 1/13.
- Dossier [bases](../dossiers/bases-congruences-premiers.md) : exact, propre à la base 10, et expliqué : le mécanisme est trouvé (K3) et démontré pour toute base q² + 1.
