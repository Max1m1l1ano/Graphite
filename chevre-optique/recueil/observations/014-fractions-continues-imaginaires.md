# 014 — Les fractions continues imaginaires : multiplier par i alterne ±i à chaque étage

| champ | valeur |
|---|---|
| type | Fait amusant ; Analogie |
| statut | exact (1/(i·y) = −i/y) ; deux écritures vérifiées à 10⁻³⁰ |
| partie | recueil |
| document | [resultats/recueil_verifications.md](../../resultats/recueil_verifications.md), § 3 |
| script | [`scripts/recueil_verifications.py`](../../scripts/recueil_verifications.py), section 3 |
| données | [`resultats/recueil_verifications.md`](../../resultats/recueil_verifications.md) |
| image | — |
| dimension | D2 bases, chiffres et congruences ; puis, à la révision 001 : D1 la chèvre et les cordes, D5 Kakeya, Perron et aiguilles |
| test | précision poussée : 61 étages, écart à la valeur exacte de moins de 10⁻³⁰ |
| arc | 2026-10-07, arc 001 (le recueil : message fondateur du § 10 de CLAUDE.md) |
| révisé | 001 (2026-10-09) |

## Le contexte qui précède

L'auteur donne les fractions continues de (±2)^(1/2), (±2)^(3/2), (±3)^(1/2) et (±3)^(3/2), pour relier les bases 2, 3, 10 et 12.

## L'observation

Les quatre fractions imaginaires de l'auteur sont justes. Deux viennent de la fraction régulière multipliée par i : les signes alternent, i√2 = [i; −2i, 2i, …]. Les deux autres arrondissent à l'entier le plus proche : i√3 = [2i; 4i, 4i, …], comme √3 = 2 − 1/(4 − 1/(4 − …)).

## Ce que le script produit

Le script évalue les fractions sur 61 étages en précision 40 chiffres, et donne les fractions réelles de √2, 2√2, √3 et 3√3.

## Liens et pistes

Partie XIX (i modulo 10) ; le lien « (−2)^(3/2) ≡ −i modulo 3 » de l'auteur reste à préciser : dans F₉, √2 = ±i, mais (−2)^(3/2) y donne ±1.

## Révision 001

Synthèse : [revision-001.md](../revisions/revision-001.md).
- Le dossier bases sépare 2^(3/2) (≡ −i dans F₉) et (−2)^(3/2) (= ±1 dans F₉) : la phrase de l'auteur est à préciser avec lui.
- Dossier [corde](../dossiers/corde-et-dimensions.md) : lien faible, par les nombres (√2, 2/√3, √(3/2)) : gardée dans le dossier avec cette étiquette.
- Dossier [bases](../dossiers/bases-congruences-premiers.md) : exact (quatre fractions justes à moins de 10⁻³⁰ sur 61 étages) ; le lien avec F₉ est exact pour 2^(3/2) (2√2 = −i), non pour (−2)^(3/2) (= ±1) ; les 10 et 12 des fractions continues sont des termes de clôture.
