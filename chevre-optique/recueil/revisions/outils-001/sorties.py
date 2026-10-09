"""Réunit les sorties structurées des agents de dossier en un seul fichier de données brutes de la révision.

    python3 sorties.py resultats_1.json [resultats_2.json …]

Écrit recueil/revisions/sorties-agents-001.json : une entrée par dossier, avec ses corrections du recouvrement,
ses verdicts sur les fiches, ses congruences, ses obstructions, ses erreurs trouvées et ses fiches proposées.
La prochaine révision (son agent Opus) peut partir de ce fichier au lieu de relire les huit dossiers en entier.
"""
import json
import sys

SORTIE = "/home/user/Graphite/chevre-optique/recueil/revisions/sorties-agents-001.json"
NOM = {"corde": "corde-et-dimensions", "moities": "moities-et-crans", "bases": "bases-congruences-premiers",
       "grain": "grain-pixels-centres", "lumiere": "lumiere-et-physique", "aiguilles": "aiguilles-kakeya-perron",
       "ombres": "ombres-cube-venn", "methode": "hasard-et-methode"}
NOTE = {"lumiere": "sortie structurée perdue (limite d'usage après l'écriture du dossier) : corrections, verdicts et fiches "
                   "proposées relevés à la main dans les § 4, 6.1 et 8 du dossier"}

res = {}
for f in sys.argv[1:]:
    res.update(json.load(open(f, encoding="utf-8")))
out = {"revision": "001", "format": "une entrée par dossier ; les champs suivent le schéma de sortie des agents du workflow (les consignes sont au § 7 de plan-001.md)",
       "dossiers": {}}
for lab in NOM:
    if lab not in res:
        continue
    r = dict(res[lab])
    r.pop("code_test", None)          # le code est dans le § 7 de chaque dossier
    r["fichier_ecrit"] = f"recueil/dossiers/{NOM[lab]}.md"
    if lab in NOTE:
        r["note"] = NOTE[lab]
    out["dossiers"][NOM[lab]] = r
json.dump(out, open(SORTIE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("écrit", SORTIE, len(out["dossiers"]), "dossiers")
