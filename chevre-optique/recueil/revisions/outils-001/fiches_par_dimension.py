"""Classe les fiches proposées par les huit agents de dossier selon leur première dimension (D1 à D8).

    python3 fiches_par_dimension.py resultats_1.json [resultats_2.json …]

Écrit le tableau Markdown de la section 7 de la vérification croisée sur la sortie standard.
"""
import json
import re
import sys

NOMS = {"D1": "D1 la chèvre et les cordes", "D2": "D2 bases, chiffres et congruences",
        "D3": "D3 grain, pixels et précision", "D4": "D4 optique et diffraction",
        "D5": "D5 Kakeya, Perron et aiguilles", "D6": "D6 sphères, cubes, Venn et symétries",
        "D7": "D7 hasard et méthode", "D8": "D8 physique"}
LABS = {"corde": "corde", "moities": "moitiés", "bases": "bases", "grain": "grain", "lumiere": "lumière",
        "aiguilles": "aiguilles", "ombres": "ombres", "methode": "méthode"}
# une fiche proposée qui recouvre une fiche de la révision ou un test du script : on le dit, pour ne pas l'écrire deux fois
DEJA = [
    (r"Kakeya.*(corps fini|inclusion)", "fiche 019"),
    (r"43/108", "§ 4.10 (vérifié)"),
    (r"dérangements", "§ 4.10 (vérifié)"),
    (r"0,6668", "corrigé (partie XXIII)"),
    (r"q² \+ 1", "§ 4.3 (vérifié)"),
    (r"trois 4/3", "§ 4.5 (vérifié)"),
    (r"tour 2-adique", "§ 4.6 (vérifié)"),
    (r"Hardy et Littlewood", "fiche 021"),
    (r"isoluminante", "fiche 018"),
    (r"93 %", "§ 4.11 (vérifié)"),
    (r"(trois 34|éventails de Perron)", "K2 (deux dossiers)"),
]

res = {}
for f in sys.argv[1:]:
    res.update(json.load(open(f, encoding="utf-8")))
par_dim = {d: [] for d in NOMS}
for lab, r in res.items():
    for nf in r.get("nouvelles_fiches", []):
        d = (re.findall(r"D[1-8]", nf.get("dimension", "")) or ["D7"])[0]
        autres = [x for x in dict.fromkeys(re.findall(r"D[1-8]", nf.get("dimension", ""))) if x != d]
        deja = next((v for k, v in DEJA if re.search(k, nf["titre"])), "")
        statut = re.split(r"[(;]", nf.get("statut", ""))[0].strip()
        par_dim[d].append((lab, nf["titre"].strip().rstrip("."), statut, ", ".join(autres), deja))

total = sum(len(v) for v in par_dim.values())
print(f"{total} fiches proposées par {len(res)} dossiers.\n")
print("| dimension | fiches | dont déjà faites |")
print("|---|---:|---:|")
for d, v in par_dim.items():
    print(f"| {NOMS[d]} | {len(v)} | {sum(1 for x in v if x[4])} |")
for d, v in par_dim.items():
    if not v:
        continue
    print(f"\n**{NOMS[d]}** ({len(v)})\n")
    print("| dossier | titre | statut | puis | déjà fait |")
    print("|---|---|---|---|---|")
    for lab, titre, statut, autres, deja in sorted(v, key=lambda x: (bool(x[4]), list(LABS).index(x[0]))):
        print(f"| {LABS[lab]} | {titre} | {statut} | {autres or '—'} | {deja or '—'} |")
