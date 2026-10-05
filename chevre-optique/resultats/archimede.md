# Résultats numériques de la partie II (générés par scripts/calculs_archimede.py)

## 1. Archimède : tranches, croisements, demi-volumes

Rayon R = 1. Hémisphère z ∈ [0, 1] ; cylindre de hauteur 1 ; cône pointe en bas (rayon de tranche = z) ;
paraboloïde-bol z = ρ² (rayon de tranche √z).

| hauteur z | hémisphère π(1−z²) | cône πz² | cylindre − cône π(1−z²) | bol π z |
|---:|---:|---:|---:|---:|
| 0,0000 | 3,1416 | 0,0000 | 3,1416 | 0,0000 |
| 0,2500 | 2,9452 | 0,1963 | 2,9452 | 0,7854 |
| 0,5000 | 2,3562 | 0,7854 | 2,3562 | 1,5708 |
| 0,7071 | 1,5708 | 1,5708 | 1,5708 | 2,2214 |
| 0,6180 | 1,9416 | 1,2000 | 1,9416 | 1,9416 |
| 0,7500 | 1,3744 | 1,7671 | 1,3744 | 2,3562 |
| 1,0000 | 0,0000 | 3,1416 | 0,0000 | 3,1416 |

- Sphère ∩ cône : z = 1/√2 = 0,707107 ; les deux tranches valent π/2, la moitié de la tranche du cylindre.
- Sphère ∩ paraboloïde : z² + z − 1 = 0, z = 1/φ = 0,618034 (nombre d'or), rayon de tranche 1/√φ = 0,786151.
- Cône ∩ paraboloïde : z = 0 et z = 1 seulement.
- Volumes : hémisphère 2π/3, cône π/3, cylindre π, bol π/2 (le paraboloïde est la moitié du cylindre).

Plan horizontal qui coupe chaque solide en deux volumes égaux (volume compté depuis z = 0) :
- hémisphère (et cylindre − cône, par Archimède) : z³ − 3z + 1 = 0 → z = 2 cos 80° = 0,347296 (contrôle 0,347296) — cas irréductible : 3 racines réelles, radicaux complexes obligatoires
- cône pointe en bas : z = 2^(−1/3) = 0,793701 ; bol paraboloïde : z = 1/√2 = 0,707107 ; cylindre : 1/2

## 2. Le cube et ses trois sphères ; le cube en dimension n

Cube d'arête 2 : sphère inscrite R = 1 (6 contacts : centres des faces), sphère médiane √2 (12 contacts : milieux
des arêtes), sphère circonscrite √3 (8 contacts : sommets).
- Volumes rapportés au cube : π/6 = 0,5236 ; π√2/3 = 1,4810 ; π√3/2 = 2,7207

| n | boule inscrite / cube = V_n/2^n | demi-diagonale √n | centres de facettes à distance √2 d'un centre donné |
|---:|---:|---:|---:|
| 1 | 1,00000 | 1,0000 | 0 sur 1 (0 %) |
| 2 | 0,78540 | 1,4142 | 2 sur 3 (67 %) |
| 3 | 0,52360 | 1,7321 | 4 sur 5 (80 %) |
| 4 | 0,30843 | 2,0000 | 6 sur 7 (86 %) |
| 5 | 0,16449 | 2,2361 | 8 sur 9 (89 %) |
| 6 | 0,08075 | 2,4495 | 10 sur 11 (91 %) |
| 8 | 0,01585 | 2,8284 | 14 sur 15 (93 %) |
| 10 | 0,00249 | 3,1623 | 18 sur 19 (95 %) |
| 20 | 0,00000 | 4,4721 | 38 sur 39 (97 %) |

n³ − n = (n−1)n(n+1) et n² − n = (n−1)n : des factorielles seulement si (n−2)! = 1, donc n = 2 ou 3.
- n = 2 : n² − n = 2, n³ − n = 6 = 3! ; n² − n = 2!
- n = 3 : n² − n = 6, n³ − n = 24 = 4! ; n² − n = 3!
- n = 4 : n² − n = 12, n³ − n = 60
- n = 5 : n² − n = 20, n³ − n = 120
- Le cube a 2n = 6 faces en dimension 3, et 2n = n! seulement pour n = 3. Son groupe de symétries a 2ⁿ·n! = 48 éléments.

## 3. Le cube qui tourne autour de sa grande diagonale (arête 1)

- Profil : cônes r² = 2s² (demi-angle arctan √2 = 54,7356°, l'« angle magique », cos = 1/√3), hyperboloïde r² = 1/2 + 2(s − √3/2)² au milieu ; écart formule / calcul direct = 1.4e-15
- Volume balayé : 1,8137993642 (calcul direct) = 1,8137993642 (formule) = π/√3 = 1,8137993642
- Cylindre circonscrit (rayon √(2/3), longueur √3) : 3,627599 → rapport 0,5000000000 : la moitié, comme le paraboloïde
- Losange (bicône des cônes prolongés) : volume 2,72069905 = sphère circonscrite au cube 2,72069905 ; solide balayé = 0,66666667 du bicône (2/3)
- Losange : angles 109,4712° et 70,5288°, diagonales √3 et √6 (rapport √2), côté 3/2 : la face du dodécaèdre rhombique
- Asymptotes de l'hyperboloïde : r = ±√2 (s − √3/2), parallèles aux cônes des bouts
- Ménisque central (entre le cylindre des sommets et l'hyperboloïde, tiers du milieu) : 0,20153326 = π/(9√3) = 0,20153326, soit 0,111111 du solide (1/9)
  épaisseur max √(2/3) − √(1/2) = 0,109390, longueur 1/√3 = 0,577350
- Sphère médiane (rayon √2/2, centre au milieu) : tangente aux cônes en s = √3/6 = 0,288675 et s = 5√3/6, cercles de rayon 1/√6 = 0,408248, et au col (rayon √2/2) ; à l'intérieur du solide : True
  → 3 cercles de contact, 6 points dans la coupe ; volume de la sphère / solide = 0,816497 = √(2/3)
- Vide entre l'hyperboloïde et la sphère médiane (tiers du milieu) : 0,15114995 = π/(12√3)
- Ombre du cube vue le long de la diagonale : hexagone régulier de côté √(2/3) = 3 losanges de 60°/120°

## 4. Le ménisque réel dans un tube

Ménisque en calotte sphérique (valable si le rayon a du tube est petit devant la longueur capillaire).
Volume oublié en lisant au point extrême = π a³ (1 − S)(1 + 2S) / (3C(1 + S)), S = sin θ, C = |cos θ|.

| angle de contact θ | flèche / a | volume oublié / (π a³) | hauteur équivalente / a |
|---:|---:|---:|---:|
| 0° | 1,0000 | 0,3333 | 0,3333 |
| 10° | 0,8391 | 0,3211 | 0,3211 |
| 20° | 0,7002 | 0,2929 | 0,2929 |
| 30° | 0,5774 | 0,2566 | 0,2566 |
| 40° | 0,4663 | 0,2163 | 0,2163 |
| 60° | 0,2679 | 0,1308 | 0,1308 |
| 80° | 0,0875 | 0,0436 | 0,0436 |
| 100° | 0,0875 | 0,0436 | 0,0436 |
| 120° | 0,2679 | 0,1308 | 0,1308 |
| 140° | 0,4663 | 0,2163 | 0,2163 |
| 160° | 0,7002 | 0,2929 | 0,2929 |
| 180° | 1,0000 | 0,3333 | 0,3333 |

θ = 0 (eau sur verre propre) : ménisque hémisphérique, l'anneau oublié est cylindre − hémisphère = le cône : π a³/3.
- eau : longueur capillaire 2,73 mm ; Jurin : a = 0.25 mm → 59,5 mm ; a = 0.5 mm → 29,7 mm ; a = 1.0 mm → 14,9 mm
- mercure : longueur capillaire 1,91 mm ; Jurin : a = 0.25 mm → -22,4 mm ; a = 0.5 mm → -11,2 mm ; a = 1.0 mm → -5,6 mm
  (signe − : dépression ; Jurin et la calotte ne valent que pour a petit devant la longueur capillaire)

Liquide en rotation (seau de Newton) : surface z = ω²ρ²/(2g), le centre descend et le bord monte de ω²a²/(4g) ;
miroir liquide : focale f = g/(2ω²).
- f = 1 m → ω = 2,215 rad/s, une rotation en 2,8 s
- f = 4 m → ω = 1,107 rad/s, une rotation en 5,7 s
- f = 9 m → ω = 0,738 rad/s, une rotation en 8,5 s

## 5. Découper l'aire de la chèvre : bandes (Riemann), niveaux (coaire), contour

Erreur sur la corde r quand l'aire est calculée avec N subdivisions :

| N | bandes verticales | niveaux de distance (milieu) | niveaux (Gauss) | contour d'Ullisch |
|---:|---:|---:|---:|---:|
| 4 | 2.4e-02 | 4.1e-03 | 2.2e-07 | 3.0e-02 |
| 8 | 9.5e-03 | 1.0e-03 | 3.1e-13 | 1.7e-03 |
| 16 | 3.1e-03 | 2.6e-04 | 2.2e-16 | 3.0e-06 |
| 32 | 1.2e-03 | 6.6e-05 | < 1e-16 | 9.5e-12 |
| 64 | 3.8e-04 | 1.6e-05 | 2.2e-16 | < 1e-16 |
| 128 | 1.4e-04 | 4.1e-06 | — | < 1e-16 |
| 256 | 4.9e-05 | 1.0e-06 | — | < 1e-16 |
| 512 | 1.8e-05 | 2.6e-07 | — | < 1e-16 |
| 1024 | 6.2e-06 | 6.4e-08 | — | < 1e-16 |

## 6. Dimensions 5 et 7, et la place de la 3D

| rayon R | dimension du volume max | dimension de l'aire max | 2πR² − 1 |
|---:|---:|---:|---:|
| 0,5 | 1 | 3 | 0,6 |
| 1,0 | 5 | 7 | 5,3 |
| 1,5 | 13 | 15 | 13,1 |
| 2,0 | 24 | 26 | 24,1 |
| 3,0 | 56 | 58 | 55,5 |

Projection de l'aire de la sphère sur un axe : densité ∝ (1 − z²)^((n−3)/2) ; uniforme seulement pour n = 3.
- n = 2 : densité en z = 0 : 0,3183 ; en z = 0,9 : 0,7303
- n = 3 : densité en z = 0 : 0,5000 ; en z = 0,9 : 0,5000
- n = 4 : densité en z = 0 : 0,6366 ; en z = 0,9 : 0,2775
- n = 10 : densité en z = 0 : 1,1641 ; en z = 0,9 : 0,0035

- π − 3 = 0,14159265 ; √2/10 = 0,14142136 ; écart 0,00017130
- Encadrement d'Archimède (96-gones) : 10/71 = 0,140845 < π − 3 < 1/7 = 0,142857

## 7. Entre la 2D et la 3D : des chèvres dans les solides d'Archimède

Piquet T = (1, 0, 0) : contact de la sphère, du cylindre et du cube. Corde qui broute la moitié :

| forme | dimension | volume | corde de la moitié |
|---|---:|---:|---:|
| disque | 2 | π | 1,158728 |
| carré (piquet au milieu d'un côté) | 2 | 4 | 1,165644 |
| boule | 3 | 4,1888 | 1,228545 |
| cylindre − double cône | 3 | 4,1888 | 1,289987 |
| cylindre (hauteur 2) | 3 | 6,2832 | 1,299443 |
| cube | 3 | 8,0000 | 1,313563 |

Quart, moitié, trois quarts (piquet sur le bord) :
- 25 % : plan r = 0,774753 (sin β − β cos β = 0,75π) ; boule r = 0,912643 (3r⁴ − 8r³ + 4 = 0)
- 50 % : plan r = 1,158728 (sin β − β cos β = 0,50π) ; boule r = 1,228545 (3r⁴ − 8r³ + 8 = 0)
- 75 % : plan r = 1,512054 (sin β − β cos β = 0,25π) ; boule r = 1,513956 (3r⁴ − 8r³ + 12 = 0)

## 8. Glisser le disque de la moitié : constructions et événements

Champ : disque unité ; piquet P = (δ, 0) ; corde k(δ) des 50 %.

| δ | k | corde commune x₀ | demi-corde y₀ | angle QPQ' | secteur PQQ' | rectangle des tangentes y = ±k |
|---:|---:|---:|---:|---:|---:|---|
| 0,0000 | 0,7071 | — | — | — | — | 1,4142 × 1,4142 (carré) |
| 0,1500 | 0,7071 | — | — | — | — | 1,4142 × 1,4142 (carré) |
| 0,2929 | 0,7071 | — | — | — | — | 1,4142 × 1,4142 (carré) |
| 0,5000 | 0,7849 | 0,6340 | 0,7734 | 199,65° | 1,0733 | 1,2393 × 1,5698 |
| 0,5658 | 0,8245 | 0,5658 | 0,8245 | 180,00° | 1,0679 | 1,1316 × 1,6491 |
| 0,7000 | 0,9173 | 0,4633 | 0,8862 | 150,09° | 1,1020 | 0,7965 × 1,8346 |
| 0,8079 | 1,0000 | 0,4040 | 0,9148 | 132,35° | 1,1549 | aucun (k ≥ 1) |
| 1,0000 | 1,1587 | 0,3287 | 0,9444 | 109,19° | 1,2793 | aucun (k ≥ 1) |
| 1,5000 | 1,6086 | 0,2208 | 0,9753 | 74,65° | 1,6856 | aucun (k ≥ 1) |
| 2,0000 | 2,0822 | 0,1661 | 0,9861 | 56,53° | 2,1391 | aucun (k ≥ 1) |
| 3,0000 | 3,0552 | 0,1109 | 0,9938 | 37,97° | 3,0926 | aucun (k ≥ 1) |

Événements : plateau tant que δ ≤ 1 − 1/√2 = 0,2929 (tangence intérieure, Q = Q' naît en (1, 0)) ; k = 1 en δ = 0,80795 (cercles égaux : chaque disque couvre la moitié de l'autre, c'est la FTM50) ; δ = 1 : piquet sur la clôture ; au-delà, la corde commune tend vers un diamètre (x₀ ≈ 1/(3δ)).
Corde commune passant par le piquet en δ = 0,565802 (k = 0,824541) : ψ − sin ψ = (π/2)(1 + cos ψ) avec ψ = 2 arccos δ ; résidu 2.4e-15

## 9. L'erreur des polygones et des polyèdres

Polygone régulier inscrit (piquet sur un sommet) et circonscrit (piquet au milieu d'un côté) :

| n côtés | inscrit : corde | écart × n² | circonscrit : corde | écart × n² |
|---:|---:|---:|---:|---:|
| 3 | 1,11377287 | -0,405 | 1,28607414 | 1,146 |
| 4 | 1,12837917 | -0,486 | 1,16564432 | 0,111 |
| 6 | 1,12413821 | -1,245 | 1,18161211 | 0,824 |
| 8 | 1,14537544 | -0,855 | 1,16564432 | 0,443 |
| 12 | 1,15127567 | -1,073 | 1,16327773 | 0,655 |
| 24 | 1,15712368 | -0,924 | 1,15946948 | 0,427 |
| 48 | 1,15829125 | -1,007 | 1,15895411 | 0,520 |
| 96 | 1,15862188 | -0,982 | 1,15878146 | 0,488 |
| 192 | 1,15870166 | -0,989 | 1,15874177 | 0,490 |

Polyèdres inscrits dans la sphère (piquet sur un sommet), chèvre 3D exacte : 1,228545

| polyèdre | sommets | faces (triangles) | volume / volume de la boule | corde | écart | écart × faces |
|---|---:|---:|---:|---:|---:|---:|
| tetra | 4 | 4 | 0,1225 | 1,117722 | -0,11082 | -0,443 |
| octa | 6 | 8 | 0,3183 | 1,137365 | -0,09118 | -0,729 |
| cube | 8 | 12 | 0,3676 | 1,137086 | -0,09146 | -1,098 |
| icosa | 12 | 20 | 0,6055 | 1,161076 | -0,06747 | -1,349 |
| dodeca | 20 | 36 | 0,6649 | 1,173138 | -0,05541 | -1,995 |
| geo2 | 42 | 80 | 0,8735 | 1,209984 | -0,01856 | -1,485 |
| geo4 | 162 | 320 | 0,9662 | 1,223416 | -0,00513 | -1,641 |
| geo8 | 642 | 1280 | 0,9914 | 1,227253 | -0,00129 | -1,653 |
