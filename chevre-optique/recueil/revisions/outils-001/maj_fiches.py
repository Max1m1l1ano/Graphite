"""Marque les fiches 001 à 015 « révisé : 001 », ajoute les dimensions confirmées par les dossiers et les verdicts.

    python3 maj_fiches.py resultats_1.json [resultats_2.json …]

Idempotent : la section « ## Révision 001 » est remplacée si elle existe.
"""
import glob
import json
import os
import re
import sys

REPO = "/home/user/Graphite/chevre-optique"
CANON = {"D1": "D1 la chèvre et les cordes", "D2": "D2 bases, chiffres et congruences",
         "D3": "D3 grain, pixels et précision", "D4": "D4 optique et diffraction",
         "D5": "D5 Kakeya, Perron et aiguilles", "D6": "D6 sphères, cubes, Venn et symétries",
         "D7": "D7 hasard et méthode", "D8": "D8 physique"}
LABS = {"corde": "corde", "moities": "moitiés", "bases": "bases", "grain": "grain", "lumiere": "lumière",
        "aiguilles": "aiguilles", "ombres": "ombres", "methode": "méthode"}
DOSS = {"corde": "corde-et-dimensions", "moities": "moities-et-crans", "bases": "bases-congruences-premiers",
        "grain": "grain-pixels-centres", "lumiere": "lumiere-et-physique", "aiguilles": "aiguilles-kakeya-perron",
        "ombres": "ombres-cube-venn", "methode": "hasard-et-methode"}
TESTS = {
    "002": "Le diésis reste un hasard testé ; le dossier corde en fait le comparant de K1 (la lumière du polygone inscrit).",
    "003": "Test 4.4 (K10) : n·tan(π/n) est la constante isopérimétrique du n-gone régulier ; le seuil du centre du Venn en dépend (fiche 020).",
    "004": "La part des triangles dérive avec n : 35,95 ; 35,76 ; 35,12 % à 17, 19 et 23 courbes (dossier ombres ; à 23, les cinq comptes publiés par Dzoba). Elle passe par les 35,10 % de l'octaèdre vers 23 courbes : une dérive qui croise une constante, comme la fiche 021. Les droites tirées au hasard en donnent 2 − π²/6 = 35,51 % (Miles, 1964, à vérifier) : un étalon possible (dossiers ombres et méthode).",
    "005": "Le dossier moitiés trouve « miroir + complément » en tête dans les 18 certificats, à 1,5 à 2,3 fois le hasard (calcul de l'agent, à refaire) ; la cause reste inconnue. Le dossier ombres montre que le complément n'est une symétrie d'aucun des 18 certificats (N_l ≠ N_(n−l)), et qu'au sens fort il ne peut pas l'être à 17 courbes (une obstruction de parité) : rien ne force la moitié exacte.",
    "006": "Tests 4.8 et 4.9 (T4) : la seconde cause est le seuil, pas l'ordre de dessin ; la moitié ne bouge pas avec le seuil (fiche 018). La cause « dipôle des couleurs » est établie par une intervention sur un système modèle : sur un Venn à 13 courbes de palette connue, G·H₁ prédit l'écart sans paramètre libre (2,08 px prédits, 2,05 à 2,20 observés), et l'ordre de dessin ne compte pas (dossier méthode ; refait par revision_001.py, § 4.12). Sur l'image à 17 courbes, la palette reste ajustée : le code de rendu n'est pas publié (dossiers grain et lumière).",
    "007": "Une autre erreur de chaîne de mesure est trouvée par la révision : le seuil (fiche 018).",
    "010": "Correction : 39,34 % est la part exacte du cercle du bord (la limite du niveau 1) ; la part monte quand on rentre vers le centre (dossiers corde et moitiés). Le titre est corrigé.",
    "011": "Test 4.4 (K10) : le seuil des 13 courbes est la constante isopérimétrique 4π (fiche 020). Il vaut 4π·(s/a)² et dépend du choix a = s = 2 px (dossier grain). De même, les 18,99 courbes à 2 000 px dépendent des 2 px d'arc par croisement : 19,76 courbes à 1,5 px, 17,90 à 3 px (revision_001.py, § 4.10 ; dossier méthode). « Pile à la limite » ne tient qu'avec ce critère : le titre est précisé.",
    "012": "Test 4.7 (T5) : la même inégalité de Bonferroni, tronquée à l'ordre 2, donne la moitié de Kakeya fini (fiche 019). Le banc relu (dossier méthode, vérifié dans le code) : quatre cas sont des identités, trois verdicts de la variation sont écrits à la main, et la précision ne dit jamais « hasard ». « Ne se trompent jamais » est trop fort ; CLAUDE.md, § 10, le précise.",
    "013": "Tests 4.1, 4.3 et 4.10 : le lien est propre à la base 10, expliqué par la famille q² + 1 et le lemme des chiffres ; Φ₆(10) = 7 × 13 explique la fausse piste de 1/13.",
    "014": "Le dossier bases sépare 2^(3/2) (≡ −i dans F₉) et (−2)^(3/2) (= ±1 dans F₉) : la phrase de l'auteur est à préciser avec lui.",
    "015": "Test 4.2 : en faisant varier N, le rapport par motif dérive et croise π puis 2√2 (fiche 021) ; les paires larges restent à 2 (Hardy et Littlewood).",
}

res = {}
for f in sys.argv[1:]:
    res.update(json.load(open(f)))
dims, verd = {}, {}
for lab, r in res.items():
    for fi in r["fiches"]:
        n = re.sub(r"\D", "", fi["numero"]).zfill(3)
        if not n.isdigit() or not 1 <= int(n) <= 15:
            continue
        for d in fi["dimensions"]:
            d = d.strip()[:2]
            if d in CANON:
                dims.setdefault(n, {}).setdefault(d, 0)
                dims[n][d] += 1
        verd.setdefault(n, []).append((lab, fi["verdict"].strip()))

for p in sorted(glob.glob(os.path.join(REPO, "recueil", "observations", "[0-9][0-9][0-9]-*.md"))):
    n = os.path.basename(p)[:3]
    if not 1 <= int(n) <= 15:
        continue
    s = open(p, encoding="utf-8").read()
    prim = re.search(r"^\| dimension \| (D\d)", s, re.M).group(1)
    autres = sorted((d for d in dims.get(n, {}) if d != prim), key=lambda d: (-dims[n][d], d))
    champ = CANON[prim] + (" ; puis, à la révision 001 : " + ", ".join(CANON[d] for d in autres) if autres else "")
    s = re.sub(r"^\| dimension \| .* \|$", lambda m: f"| dimension | {champ} |", s, count=1, flags=re.M)
    s = re.sub(r"^\| révisé \| .* \|$", "| révisé | 001 (2026-10-09) |", s, count=1, flags=re.M)
    s = re.sub(r"\n\nDimensions voisines, à confirmer à la révision : [^\n]*\n", "\n", s)
    s = re.sub(r"\n## Révision 001\n.*\Z", "\n", s, flags=re.S)
    bloc = ["## Révision 001", ""]
    bloc.append("Synthèse : [revision-001.md](../revisions/revision-001.md).")
    if n in TESTS:
        bloc.append(f"- {TESTS[n]}")
    for lab, v in verd.get(n, []):
        # la voix de l'agent, rendue explicite dans la fiche
        v = re.sub(r"\b[Aa]joutée par moi", "ajoutée au dossier par son agent", v)
        v = v.replace("calculé ici", "calculé par l'agent").replace("ma lecture", "lecture de l'agent")
        if len(v) > 1 and v[0].isupper() and v[1].islower():
            v = v[0].lower() + v[1:]          # après un deux-points, pas de majuscule
        if not v.endswith("."):
            v += "."
        bloc.append(f"- Dossier [{LABS[lab]}](../dossiers/{DOSS[lab]}.md) : {v}")
    s = s.rstrip("\n") + "\n\n" + "\n".join(bloc) + "\n"
    if n == "010":
        s = s.replace("# 010 — La chèvre d'Ullisch broute 39,34 % de chaque anneau du bord",
                      "# 010 — La chèvre d'Ullisch broute 39,34 % du cercle du bord")
        s = s.replace("Ullisch prend la même part de chaque anneau du bord :",
                      "Ullisch prend 39,34 % du cercle du bord (la limite exacte du niveau 1 ; la part monte quand on rentre, révision 001) :")
    if n == "011":
        s = s.replace("# 011 — À 2 000 px, le centre du Venn à 19 courbes est pile à la limite",
                      "# 011 — À 2 000 px et 2 px par croisement, le centre du Venn à 19 courbes est à la limite")
    open(p, "w", encoding="utf-8").write(s)
    print(n, prim, "→", autres, "|", len(verd.get(n, [])), "verdicts")
