# Résultats de la partie X (générés par scripts/carre_ptolemee.py)

## 1. Le trou des rayons de l'œil de poisson

P = (0,45 ; 0,25), direction 29,05° ; P' = −P/|P|² ; |PP'| = 2,4574.
Le rayon lancé à l'angle θ de la droite PP' est un cercle de rayon |PP'|/(2|sin θ|). Pour θ = 0, c'est la droite P–O–P', le seul rayon droit.
Avec mon seuil « cercle de rayon > 3 », les rayons sautés forment deux secteurs de ±24,18° autour de 29,05° et 209,05° : de 4,88° à 53,23°, et de 184,88° à 233,23°.
Rayon du cercle à 137,5° : 1,295 (tracé) ; à 222,5° : 5,284 (sauté, car il est dans le second secteur).
Pour un autre point, Q = (−0,3 ; 0,4), le trou serait centré sur 126,87° et 306,87° : il suit le point, pas un angle fixe.

## 2. Un point, un disque et un carré rapetissés sous le flou

Images floues (tache gaussienne de largeur σ), à lumière totale égale ; écart maximal rapporté au maximum de l'image du disque.

| rayon du disque ρ/σ | point contre disque | carré de même aire (côté √π·ρ) | carré de côté √3·ρ |
|---:|---|---|---|
| 0,05 | 6,25e−04 | 2,95e−05 | 1,30e−08 |
| 0,10 | 2,50e−03 | 1,18e−04 | 2,08e−07 |
| 0,20 | 1,00e−02 | 4,67e−04 | 3,31e−06 |
| 0,40 | 4,05e−02 | 1,80e−03 | 5,21e−05 |
| 0,80 | 1,69e−01 | 6,27e−03 | 7,84e−04 |
| 1,60 | 7,73e−01 | 1,38e−02 | 1,07e−02 |

Pentes aux petites tailles (log-log) : point/disque 2,00, carré de même aire 2,00, carré de côté √3·ρ 4,00.
Moments d'ordre 2 par axe : disque ρ²/4, carré s²/12. À aire égale (s² = πρ²), le carré est π/3 = 1,0472 fois plus étalé ; à étalement égal (s = √3·ρ), son aire vaut 3/π = 0,9549 fois celle du disque.
La première différence de forme est d'ordre 4 : pour le carré, ⟨x⁴⟩ − 3⟨x²y²⟩ = s⁴(1/80 − 1/48) = −s⁴/120 (le disque donne 0).

## 3. Le carré des centres fantômes est le réseau réciproque de la grille

Grille hexagonale (pas 1 pixel) : u·|x|²/R² et u·|x − x_g|²/R² − u·|x_g|²/R² diffèrent d'un entier en chaque point du réseau quand g est un vecteur du réseau réciproque ; écart maximal à un entier : 3.6e-14.
Lame de Fresnel à 55 zones, R = 36 px : grille carrée → 8 centres sur le carré de demi-côté 0,655 a (4 aux milieux des côtés, 4 aux coins, à √2 près) ; grille hexagonale → 6 centres sur l'hexagone de rayon 0,756 a, soit 2/√3 = 1,1547 fois plus loin.

## 4. Ptolémée : les polygones dans le cercle

Théorème de Ptolémée (quadrilatère inscrit) : AC·BD = AB·CD + AD·BC.
- carré de côté 1 : d² = 1 + 1, d = √2 = 1,414214, la diagonale du carré, limite de la chèvre en dimension infinie ;
- pentagone régulier de côté 1 (quatre sommets consécutifs) : d² = 1 + d, d = φ = 1,618034.
Contrôle sur 1000 quadrilatères inscrits tirés au hasard : écart maximal 1.3e-15.

La corde de la chèvre est la corde de l'arc 70,8117° = 180° − β (β = 109,1883°). Dans la table de Ptolémée (rayon 60), elle vaut 69;31,25, entre les cordes de 70°30′ (69,2574) et de 71° (69,6844), calculées ici avec les valeurs modernes.

## 5. Le plan hyperbolique, jumeau de l'œil de poisson

Indice n = 2/(1 − r²) dans le disque unité : c'est le disque de Poincaré, le plan hyperbolique.
24 rayons partis de P = (0,3 ; 0,2) : tous atteignent le bord (|x| > 0,997) ; angle avec le rayon du disque à l'arrivée ≤ 0,2° (perpendiculaires au bord, à la discrétisation près) ; deux rayons ne se recroisent jamais (distance minimale hors du départ : 0,047).
Avec l'indice 2/(1 + r²) (partie VIII), tous se recroisent en −P/|P|². Sphère : les rayons se refocalisent ; plan : droites ; plan hyperbolique : ils s'écartent sans retour.

Récurrence du pentagone x_(n+1) = (1 + x_n)/x_(n−1), départ (1 ; 2) : 1,0000, 2,0000, 3,0000, 2,0000, 1,0000, 1,0000, 2,0000, 3,0000, 2,0000, 1,0000, 1,0000 … période 5.
Contrôle sur 200 départs au hasard : retour au départ après 5 pas, écart relatif maximal 3.1e-16. Point fixe : x² = 1 + x, soit φ = 1,618034 (la relation de Ptolémée du pentagone).
