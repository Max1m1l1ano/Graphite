# Résultats de la partie XIII (générés par scripts/perron_dephasage.py)

## 1. Les branchages entourés en rouge

Zone A (en haut) : 1405 cases du spectre ; zone B (en bas) : 2046 cases.

Ressemblance (corrélation) entre le spectre mesuré et celui de la rangée reconstruite avec K composantes :

| K | composantes ajoutées | zone A | zone B | tout le spectre |
|---:|---|---|---|---|
| 2 | 21, 34 | 0,638 | 0,704 | 0,709 |
| 3 | 13 | 0,765 | 0,825 | 0,767 |
| 5 | 76, 89 | 0,720 | 0,899 | 0,826 |
| 8 | 26, 29, 8 | 0,846 | 0,965 | 0,885 |
| 12 | 16, 131, 144, 18 | 0,928 | 0,964 | 0,928 |
| 16 | 42, 186, 24, 199 | 0,943 | 0,968 | 0,940 |
| 24 | … | 0,937 | 0,985 | 0,950 |
| 40 | … | 0,970 | 0,980 | 0,971 |
| 200 | … | 0,994 | 0,999 | 0,997 |

264 nœuds (croisements) entre les aiguilles repliées des 12 premières composantes, pour 0 ≤ x/a ≤ 1.
Nœud miroir : une des deux aiguilles est vue dans le miroir du repliement (au-delà de 0,5 cycle par pixel) ; il bat à la fréquence u + v. Nœud direct : les deux du même côté ; il bat à |u − v|.
Chaque nœud est sur un centre fantôme de la fréquence de battement (u + v ou |u − v|) : 2(u ± v)·x/R y est un entier (écart max 8.9e-16).
Le premier nœud miroir de u et v est en x/a = R/(2(u+v)), à la fréquence f = u/(u+v) cycle par pixel.

| paire | x/a du nœud | f = u/(u+v) | en degrés par pixel (360·f) |
|---|---|---|---|
| 13 et 21 | 0,8824 | 13/34 = 0,38235 | 137,647° |
| 21 et 34 | 0,5455 | 21/55 = 0,38182 | 137,455° |
| 34 et 89 | 0,2439 | 34/123 = 0,27642 | 99,512° |
| 21 et 89 | 0,2727 | 21/110 = 0,19091 | 68,727° |

21/55 de tour = 137,45° et 34/55 = 222,55° : au nœud de 21 et 34, la composante 21 avance d'une approximation de Fibonacci de l'angle d'or par pixel, et la 34 de son complément (parties XI et XII).

- zone A : 21 nœuds (13 miroirs, 8 directs) ; les plus forts : 21 × 76 (miroir, battement 97) ; 21 × 89 (direct, battement 68) ; 21 × 131 (miroir, battement 152) ; 21 × 144 (miroir, battement 165) ; 13 × 76 (direct, battement 63) ; 34 × 131 (direct, battement 97)
- zone B : 41 nœuds (30 miroirs, 11 directs) ; les plus forts : 21 × 89 (miroir, battement 110) ; 21 × 131 (miroir, battement 152) ; 21 × 131 (direct, battement 110) ; 21 × 144 (miroir, battement 165) ; 21 × 144 (direct, battement 123) ; 13 × 76 (miroir, battement 89)

## 2. Le déphasage de 90° (cos → sin) sur la lame de zones

Chaque composante choisie passe de cos à sin ; écart relatif du spectre local (K = 40 composantes) :

| composantes décalées de 90° | tout le spectre | zone A | zone B |
|---|---|---|---|
| 21 et 34 | 0,372 | 0,325 | 0,435 |
| 13 et 8 | 0,182 | 0,121 | 0,317 |
| 26 et 29 | 0,166 | 0,225 | 0,147 |
| répliques 76, 89, 131, 144 | 0,287 | 0,155 | 0,233 |
| toutes sauf 21 et 34 | 0,481 | 0,446 | 0,429 |
| toutes (déphasage commun) | 0,393 | 0,232 | 0,342 |

Déphasage commun de 180° (tout change de signe) : écart 0,042.

### La loi du nœud

Deux composantes seules ; on ajoute la phase θ à la seconde (relatif), ou aux deux (commun), et on lit le spectre au nœud. a et b : le spectre au nœud avec chaque composante seule.

| nœud | type | a | b | relatif : min → max | \|a − b\| et a + b | période | commun : min → max | période |
|---|---|---|---|---|---|---|---|---|
| 21 × 34 en x/a = 0,545, f = 0,382 | miroir (battement 55) | 1,66 | 0,97 | 0,75 → 2,57 | 0,69 et 2,63 | 360° | 0,75 → 2,58 | 180° |
| 13 × 76 en x/a = 0,476, f = 0,206 | direct (battement 63) | 0,72 | 0,31 | 0,41 → 1,03 | 0,41 et 1,03 | 360° | 0,43 → 0,44 | aucune (constant) |
- 21 × 34 avec les phases de la lame : passer les deux en sin fait passer le nœud de 1,97 à 1,83 seulement, car il part presque en quadrature (à mi-chemin entre fort et faible).
- 21 × 34 (miroir) : en partant de la phase commune 140° (nœud au plus clair), ajouter 90° à tout fait passer le nœud de 2,58 à 0,75.
- 13 × 76 (direct) : en partant de la phase commune 290° (nœud au plus clair), ajouter 90° à tout fait passer le nœud de 0,44 à 0,43.

Le nœud suit la loi des interférences : il va de |a − b| (opposition) à a + b (en phase) quand le déphasage relatif fait un tour. Un cos réel est la somme de deux rotations de sens contraires, cos θ = (e^{iθ} + e^{−iθ})/2, et l'aiguille vue dans le miroir est la moitié e^{−iθ}. Un déphasage commun de 90° tourne donc les deux aiguilles d'un nœud miroir de +90° et de −90° : leur déphasage relatif change de 180°, et le nœud passe à l'état opposé (clair ↔ sombre ; un nœud à mi-chemin, en quadrature, reste à mi-chemin). Sur un nœud direct, le même déphasage commun ne change rien.

### D'une rangée de pixels à l'autre

À la hauteur y0, la composante u prend la phase 2πu·y0²/R² : un nœud de u et v se décale de 2π(u ± v)·y0²/R².

| y0 (pixels) | décalage du nœud miroir 21 × 34 (battement 55) | écart du spectre (tout) | zone A | zone B |
|---:|---|---|---|---|
| 0 | 0,0° | 0,000 | 0,000 | 0,000 |
| 2 | 22,0° | 0,247 | 0,213 | 0,278 |
| 4 | 88,0° | 0,467 | 0,503 | 0,326 |
| 6 | 198,0° | 0,353 | 0,142 | 0,352 |
| 8 | 352,0° | 0,469 | 0,277 | 0,373 |
| 12 | 72,0° | 0,441 | 0,350 | 0,459 |

Le nœud 21 × 34 tourne de 90° dès y0 = R/(2√55) = 4,05 pixels : dans l'image elle-même, le passage de cos à sin se fait tout seul d'une rangée à l'autre.

## 3. L'arbre de Perron tourné de 90°

Arbre à 8 branches de la partie X (α = 4/5, 3/4, 2/3). Chaque branche donne 3 aiguilles (ses deux bords et sa médiane). Tourné de 90°, la base devient l'axe des fréquences et la hauteur l'axe des positions : chaque aiguille devient une fréquence qui glisse de la base (x = 0) au sommet (x = 1). 241 points, fenêtre de 48 points.

| arbre tourné | branches alternées cos / sin | déphasage commun de 90° | déphasage commun de 180° |
|---|---|---|---|
| sous 0,5 (de 0,02 à 0,48) | 0,413 | 0,010 | 0,000 |
| centré sur 0,5 (de 0,27 à 0,73) : une moitié dans le miroir | 0,567 | 0,200 | 0,000 |

Tant que l'arbre reste sous 0,5 cycle par pixel, aucune aiguille n'est vue dans le miroir : le spectre ne voit que les déphasages relatifs, et le déphasage commun ne change presque rien. Centré sur 0,5, la moitié de l'arbre passe dans le miroir, des nœuds miroirs apparaissent, et le déphasage commun change le spectre, comme dans la lame.
Lame de zones, pour comparer : déphasage relatif 0,481, commun 0,393.

La loi du nœud dans l'arbre centré sur 0,5 (deux aiguilles seules de deux branches différentes) :

| nœud | type | relatif : min → max | période | commun : min → max | période |
|---|---|---|---|---|---|
| branches 1 × 6 en x = 0,520, f = 0,431 | miroir | 0,76 → 22,68 | 360° | 1,00 → 22,63 | 180° |
| branches 3 × 4 en x = 0,600, f = 0,423 | direct | 0,46 → 23,43 | 360° | 15,40 → 15,42 | aucune (constant) |

Même loi que dans la lame : un tour pour le déphasage relatif ; un demi-tour pour le déphasage commun sur un nœud miroir ; rien sur un nœud direct.

## 4. Tourner de 90° le plan position–fréquence, c'est la transformée de Fourier

Fenêtre gaussienne de variance L/(2π) (L = 256), qui est sa propre transformée de Fourier (écart 1.1e-16).
Spectre local de la transformée de Fourier de l'arbre tourné, comparé au spectre local tourné de 90° : écart max 4.6e-16 (relatif). Deux transformées de suite (180°) : s(n) → s(−n), l'image retournée (écart 2.3e-15).

## 5. La bande 2,44–2,56

Corde calculée par la fonction bêta incomplète (contrôle à 30 chiffres en n = 2 ; 2,5 ; 3 : écart 2e-16).

| grandeur | n = 2,44 | n = 2,50 | n = 2,56 |
|---|---|---|---|
| corde r | 1,195111 | 1,199270 | 1,203272 |
| r² | 1,428291 | 1,438249 | 1,447862 |
| rⁿ (boule de la corde, en boules unité) | 1,544814 | 1,575044 | 1,605946 |
| corde du simplexe s | 1,191052 | 1,195229 | 1,199251 |
| écart r − s | 0,004059 | 0,004042 | 0,004021 |
| volume de la boule V(n) | 3,627788 | 3,691529 | 3,754506 |
| aire de la sphère n·V(n) | 8,851802 | 9,228822 | 9,611535 |
| hémisphère / cylindre h(n) | 0,725998 | 0,718884 | 0,711973 |
| angle au piquet α (°) | 53,304972 | 53,156228 | 53,012860 |
| arc de la corde γ (°) | 73,390057 | 73,687544 | 73,974280 |

Croisements exacts dans la bande (la grandeur passe par la valeur exacte) :

- **Fibonacci, Lucas et φ** (1) : rⁿ (boule de la corde, en boules unité) = 8/5 en n = 2,5486
- **bases 2, 10, 12 et 60** (72) : aire de la sphère n·V(n) = 71/8 en n = 2,4437 ; aire de la sphère n·V(n) = 89/10 en n = 2,4477 ; aire de la sphère n·V(n) = 107/12 en n = 2,4504 ; arc de la corde γ (°) = 73,5° en n = 2,4619 ; volume de la boule V(n) = 11/3 en n = 2,4765 ; aire de la sphère n·V(n) = 109/12 en n = 2,4770 ; aire de la sphère n·V(n) = 91/10 en n = 2,4796 ; aire de la sphère n·V(n) = 73/8 en n = 2,4836 ; aire de la sphère n·V(n) = 55/6 en n = 2,4902 ; aire de la sphère n·V(n) = 46/5 en n = 2,4954 ; aire de la sphère n·V(n) = 37/4 en n = 2,5033 ; volume de la boule V(n) = 37/10 en n = 2,5080 ; corde r = 6/5 en n = 2,5108 ; aire de la sphère n·V(n) = 93/10 en n = 2,5112 ; rⁿ (boule de la corde, en boules unité) = 19/12 en n = 2,5162 ; aire de la sphère n·V(n) = 28/3 en n = 2,5165 ; aire de la sphère n·V(n) = 75/8 en n = 2,5230 ; aire de la sphère n·V(n) = 47/5 en n = 2,5269 ; aire de la sphère n·V(n) = 113/12 en n = 2,5296 ; aire de la sphère n·V(n) = 19/2 en n = 2,5426 ; rⁿ (boule de la corde, en boules unité) = 8/5 en n = 2,5486 ; aire de la sphère n·V(n) = 115/12 en n = 2,5556 ; volume de la boule V(n) = 15/4 en n = 2,5557 ; aire de la sphère n·V(n) = 48/5 en n = 2,5582 ; et 48 fractions de dénominateur 15, 16, 20, 30 ou 60 (surtout l'aire n·V(n), qui varie vite)
- **constantes déjà rencontrées** (1) : rⁿ (boule de la corde, en boules unité) = π/2 en n = 2,4916

La corde vaut 6/5 en n = 2,51077 : alors cos α = r/2 = 3/5 et sin α = 4/5, le triangle piquet–centre–bord se coupe en deux triangles 3-4-5 (α = 53,13°).

Contrôle : le même compte pour toutes les bandes de largeur 0,12 entre 1,2 et 4,4 :

| famille | dans 2,44–2,56 | moyenne des bandes | écart-type | bandes plus pauvres | à égalité | plus riches |
|---|---|---|---|---|---|---|
| Fibonacci, Lucas et φ | 1 | 3,5 | 3,6 | 10 % | 24 % | 67 % |
| bases 2, 10, 12 et 60 | 72 | 72,2 | 6,0 | 35 % | 3 % | 61 % |
| constantes déjà rencontrées | 1 | 0,9 | 1,3 | 44 % | 38 % | 18 % |

### La ligne de Fibonacci de rⁿ

| rⁿ = | dimension n |
|---|---|
| 3/2 = 1,500000 | 2,348538 |
| 5/3 = 1,666667 | 2,674209 |
| 8/5 = 1,600000 | 2,548557 |
| 13/8 = 1,625000 | 2,596352 |
| 21/13 = 1,615385 | 2,578068 |
| 34/21 = 1,619048 | 2,585047 |
| 55/34 = 1,617647 | 2,582381 |
| 89/55 = 1,618182 | 2,583399 |
| 144/89 = 1,617978 | 2,583010 |
| 233/144 = 1,618056 | 2,583159 |
| 377/233 = 1,618026 | 2,583102 |
| φ = 1,618034 | 2,583118 |

Les dimensions convergent vers n* = 2,58312 en alternant, comme les fractions vers φ. Seule 8/5 (n = 2,5486) tombe dans la bande ; la limite est 0,023 au-dessus.
rⁿ vaut r² = 1,3427 en 2D et r³ = 1,8543 en 3D, et croît avec n : comme φ = 1,6180 est entre les deux, la limite tombe forcément entre 2D et 3D.

Toutes les limites de ce genre (une grandeur égale à une puissance de φ) entre 1,2 et 4,4 : 18, dont 0 dans la bande (on en attendrait 0,68 si elles étaient réparties au hasard) :
1,544 (volume de la boule V(n) = φ²); 1,587 (aire de la sphère n·V(n) = φ³); 1,592 (r² = 2/φ); 1,716 (r² = √φ); 1,734 (rⁿ (boule de la corde, en boules unité) = 2/φ); 1,827 (rⁿ (boule de la corde, en boules unité) = √φ); 1,851 (hémisphère / cylindre h(n) = φ/2); 1,995 (hémisphère / cylindre h(n) = 1/√φ); 2,583 (rⁿ (boule de la corde, en boules unité) = φ); 2,783 (angle au piquet α (°) = 360°/φ^4); 3,052 (volume de la boule V(n) = φ³); 3,156 (corde r = 2/φ); 3,236 (corde du simplexe s = 2/φ); 3,583 (hémisphère / cylindre h(n) = 1/φ); 4,037 (rⁿ (boule de la corde, en boules unité) = φ²); 4,131 (r² = φ); 4,131 (corde r = √φ); 4,236 (corde du simplexe s = √φ)
