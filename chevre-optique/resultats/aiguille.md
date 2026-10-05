# Résultats de la partie V (générés par scripts/aiguille.py)

## 1. Où retourner une aiguille de longueur 1

| ensemble | aire | valeur | contrôle numérique | part du disque |
|---|---|---|---|---|
| disque de diamètre 1 | π/4 | 0,78539816 | 0,78539816 | 1,0 |
| triangle de Reuleaux de largeur 1 | (π − √3)/2 | 0,70477092 | 0,70477091 | 0,897342 |
| triangle équilatéral de hauteur 1 (Pál) | 1/√3 | 0,57735027 | 0,57735027 | 0,735105 |
| deltoïde (Kakeya) | π/8 | 0,39269908 | 0,39269908 | 0,5 |

Deltoïde : longueur des segments tangents (7 positions) = 1.000000000000 … 1.000000000000 (aiguille de longueur 1)
Étoilés : aire ≥ π/108 = 0,029089 (Cunningham 1971), amélioré en π/98 = 0,032057 (2025)

## 2. La chèvre et le triangle équilatéral de hauteur R

- corde de la chèvre : 1,15872847302 R ; côté du triangle équilatéral de hauteur R : 2/√3 = 1,15470053838 R
- écart : 0,004028 R (0,348 %)
- herbe broutée avec la corde 2/√3 : 49,7170 % (au lieu de 50 %)
- angle au centre : chèvre β = 1,905695729 ; triangle 2·arccos(1/√3) = 1,910633236
- triangle de Reuleaux = trois chèvres de corde = côté : chaque paire de disques se recouvre de 39,10 % (vesica piscis, (2π/3 − √3/2)/π)

## 3. L'arbre de Perron (triangle équilatéral de hauteur 1, 2^k branches)

- 2 branches, α = 2/3 : aire = 0,66666666666666666667 (minimum de α² + 2(1 − α)²)
- 4 branches, α = 1/√2 aux deux étages : aire = 0,5 ; près de l'optimum, aire = 1 − 2α² + 2α⁴ = ½ + 2(α² − ½)²
- 4 branches, α = 3/4 puis 2/3 : aire = 0,5

| branches N = 2^k | rapports α (du plus fin au plus grossier) | aire exacte | 2/(k+2) |
|---:|---|---|---|
| 2 | 2/3 | 0,66666666666666666667 | 0,66666666666666666667 |
| 4 | 3/4, 2/3 | 0,5 | 0,5 |
| 8 | 4/5, 3/4, 2/3 | 0,4 | 0,4 |
| 16 | 5/6, 4/5, 3/4, 2/3 | 0,33333333333333333333 | 0,33333333333333333333 |
| 32 | 6/7, 5/6, 4/5, 3/4, 2/3 | 0,28571428571428571429 | 0,28571428571428571429 |
| 64 | 7/8, 6/7, 5/6, 4/5, 3/4, 2/3 | 0,25 | 0,25 |

(calcul exact : 5 s)

Grands arbres (tranches, 3000 niveaux) :
- k = 7 (128 branches) : 0,22222 ; 2/(k+2) = 0,22222
- k = 8 (256 branches) : 0,20000 ; 2/(k+2) = 0,20000
- k = 9 (512 branches) : 0,18182 ; 2/(k+2) = 0,18182
- k = 10 (1024 branches) : 0,16667 ; 2/(k+2) = 0,16667
- k = 11 (2048 branches) : 0,15385 ; 2/(k+2) = 0,15385
- k = 12 (4096 branches) : 0,14286 ; 2/(k+2) = 0,14286
- k = 13 (8192 branches) : 0,13333 ; 2/(k+2) = 0,13333
- k = 14 (16384 branches) : 0,12500 ; 2/(k+2) = 0,12500

Rapports irréguliers trouvés par optimisation (Nelder–Mead, départs aléatoires), aire exacte :
- k = 3 : α = (0.7778, 0.5953, 0.8602) → 0,3981482 contre 2/(k+2) = 0,4 (gain 0,46 %)
- k = 5 : α = (0.8396, 0.7207, 0.9287, 0.598, 0.8449) → 0,28382547 contre 2/(k+2) = 0,28571429 (gain 0,66 %)

## 4. Ménisques d'Archimède contre arbre de Perron

| N | ménisques : 1 − (N/2π)·sin(2π/N) | arbre de Perron : 2/(log₂N + 2) |
|---:|---|---|
| 4 | 3,634e-01 | 0,5000 |
| 16 | 2,550e-02 | 0,3333 |
| 64 | 1,606e-03 | 0,2500 |
| 256 | 1,004e-04 | 0,2000 |
| 1024 | 6,275e-06 | 0,1667 |
| 4096 | 3,922e-07 | 0,1429 |
| 16384 | 2,451e-08 | 0,1250 |

Pour que l'arbre de Perron descende à 1 % du triangle, il faudrait 2^198 ≈ 4·10⁵⁹ branches (2/(k+2) = 0,01 ⇒ k = 198) ; les ménisques d'Archimède passent sous 1 % dès N = 26.
