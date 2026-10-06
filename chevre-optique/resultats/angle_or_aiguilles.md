# Résultats de la partie XI (générés par scripts/angle_or_aiguilles.py)

## 1. L'angle d'or partage le tour comme les deux foyers partagent la puissance

Angle d'or : 360°/φ² = 137,507764° ; complément : 360°/φ = 222,492236°.
En tours : 1/φ² = 0,381966 et 1/φ = 0,618034 ; somme = 1,000000000000.
Les deux foyers de la lentille de Fibonacci (partie IX) : 1/z₁ + 1/z₂ = 1/z_N avec z₁ → φ², z₂ → φ (en unités de z_N). Le foyer proche porte 1/φ de la puissance 1/z_N, le foyer lointain 1/φ² : le même partage.
222,5° est un arrondi : la valeur exacte 222,4922…° est irrationnelle (φ l'est) et n'a pas d'écriture décimale finie.

## 2. Les trous laissés par l'angle d'or (théorème des trois distances)

| directions N | longueurs des trous (degrés) | rapports | la plus grande = somme des deux autres ? |
|---:|---|---|---|
| 2 | 137,508 ; 222,492 | 1,618034 | — |
| 3 | 84,984 ; 137,508 | 1,618034 | — |
| 4 | 52,523 ; 84,984 ; 137,508 | 1,618034, 1,618034 | oui |
| 5 | 52,523 ; 84,984 | 1,618034 | — |
| 8 | 32,461 ; 52,523 | 1,618034 | — |
| 10 | 20,062 ; 32,461 ; 52,523 | 1,618034, 1,618034 | oui |
| 13 | 20,062 ; 32,461 | 1,618034 | — |
| 20 | 12,399 ; 20,062 ; 32,461 | 1,618034, 1,618034 | oui |
| 21 | 12,399 ; 20,062 | 1,618034 | — |
| 34 | 7,663 ; 12,399 | 1,618034 | — |
| 55 | 4,736 ; 7,663 | 1,618034 | — |

Deux longueurs seulement pour N = 2, 3, 5, 8, 13, 21, 34, 55 : exactement les nombres de Fibonacci.
Toutes les longueurs sont des 360°/φ^k : 137,51° ; 84,98° ; 52,52° ; 32,46° ; 20,06° ; 12,40° ; …

## 3. Le spectre du diaphragme de Fibonacci (55 anneaux)

| rang | composante u | amplitude | nature |
|---:|---:|---|---|
| 1 | 21 | 0,2306 | nombre de Fibonacci |
| 2 | 34 | 0,1424 | nombre de Fibonacci |
| 3 | 13 | 0,0982 | nombre de Fibonacci |
| 4 | 76 | 0,0637 | nombre de Lucas, réplique 21 + 1×55 |
| 5 | 89 | 0,0544 | nombre de Fibonacci, réplique 34 + 1×55 |
| 6 | 26 | 0,0537 | somme ou différence de nombres de Fibonacci |
| 7 | 29 | 0,0481 | nombre de Lucas |
| 8 | 8 | 0,0454 | nombre de Fibonacci |
| 9 | 16 | 0,0371 | somme ou différence de nombres de Fibonacci |
| 10 | 131 | 0,0370 | réplique 21 + 2×55 |
| 11 | 144 | 0,0336 | nombre de Fibonacci, réplique 34 + 2×55 |
| 12 | 18 | 0,0333 | nombre de Lucas |
| 13 | 42 | 0,0304 | somme ou différence de nombres de Fibonacci |
| 14 | 186 | 0,0260 | réplique 21 + 3×55 |
| 15 | 24 | 0,0259 | somme ou différence de nombres de Fibonacci |
| 16 | 199 | 0,0243 | nombre de Lucas, réplique 34 + 3×55 |

Multiples de 55 : amplitude exactement nulle (2,4e−17 pour 55, 2,4e−17 pour 220).
u = 11 : 0,0170 ; u = 66 = 11 + 55 : 0,0028 ; u = 121 = 11 + 2×55 : 0,0015 ; rapport 121/11 : 0,090909 = 11/121 = 1/11.
Les répliques u + 55k viennent des marches des anneaux, comme les ordres d'un réseau : leur amplitude décroît en 1/(u + 55k).

## 4. Les petites aiguilles du spectre local (rayon 60 px, le long de l'axe)

On reconstruit la rangée de pixels avec les K composantes les plus fortes, et on compare son spectre local au spectre mesuré.

| composantes gardées K | composantes ajoutées | ressemblance des spectres (corrélation) |
|---:|---|---|
| 1 | 21 | 0,607 |
| 2 | 34 | 0,709 |
| 3 | 13 | 0,767 |
| 4 | 76 | 0,802 |
| 6 | 89, 26 | 0,855 |
| 8 | 29, 8 | 0,885 |
| 12 | 16, 131, 144, 18 | 0,928 |
| 16 | 42, 186, 24, 199 | 0,940 |
| 24 | … | 0,950 |
| 40 | … | 0,971 |
| 80 | … | 0,986 |
| 200 | … | 0,997 |
| 600 | … | 0,998 |

Avec les deux seules composantes de la partie IX (21 et 34), la ressemblance n'est que de 0,71 : les autres aiguilles manquaient.
