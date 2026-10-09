"""Construit le recouvrement v2 : le v1 du plan, plus les corrections de chaque agent de dossier."""
import json, re, sys
REPO = "/home/user/Graphite/chevre-optique"
t = open(REPO + "/recueil/revisions/plan-001.md", encoding="utf-8").read()
m = re.search(r"```json\n(.*?)\n```", t[t.index("### 1.9"):], re.S)
v1 = json.loads(m.group(1))["dossiers"]
res = {}
for f in sys.argv[1:]:
    res.update(json.load(open(f)))
NOM = {"corde": "corde-et-dimensions", "moities": "moities-et-crans", "bases": "bases-congruences-premiers",
       "grain": "grain-pixels-centres", "lumiere": "lumiere-et-physique", "aiguilles": "aiguilles-kakeya-perron",
       "ombres": "ombres-cube-venn", "methode": "hasard-et-methode"}
ROM = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII","XIV","XV","XVI","XVII","XVIII","XIX","XX",
       "XXI","XXII","XXIII","XXIV","XXV","XXVI","XXVII","XXVIII","XXIX","XXX"]
v2 = {k: {"parties": list(v["parties"]), "fiches": list(v["fiches"])} for k, v in v1.items()}
lignes = []
for lab, r in res.items():
    d = NOM[lab]
    c = r["corrections_recouvrement"]
    norm = lambda xs: [x.strip().upper() for x in xs if x.strip()]
    ap = [x for x in norm(c["ajouter_parties"]) if x in ROM]
    rp = [x for x in norm(c["retirer_parties"]) if x in ROM]
    af = [re.sub(r"\D", "", x).zfill(3) for x in c["ajouter_fiches"] if re.sub(r"\D", "", x)]
    rf = [re.sub(r"\D", "", x).zfill(3) for x in c["retirer_fiches"] if re.sub(r"\D", "", x)]
    v2[d]["parties"] = sorted(set(v2[d]["parties"]) - set(rp) | set(ap), key=ROM.index)
    v2[d]["fiches"] = sorted(set(v2[d]["fiches"]) - set(rf) | set(af))
    lignes.append((lab, d, ap, rp, af, rf, c["raisons"]))
json.dump({"revision": "001", "version": "v2", "dossiers": v2}, open(sys.argv[0].replace("v2.py", "v2.json"), "w"), ensure_ascii=False, indent=1)
for l in lignes:
    print(l[0], "| + parties", l[2], "| − parties", l[3], "| + fiches", l[4], "| − fiches", l[5])
print({k: (len(v["parties"]), len(v["fiches"])) for k, v in v2.items()})

# le bloc compact, au format du § 1.9 du plan
L = ['{', '  "revision": "001",', '  "version": "v2",', '  "dossiers": {']
noms = list(v2)
for i, k in enumerate(noms):
    v = v2[k]
    L.append(f'    "{k}": {{')
    L.append('      "parties": [' + ", ".join(f'"{x}"' for x in v["parties"]) + '],')
    L.append('      "fiches": [' + ", ".join(f'"{x}"' for x in v["fiches"]) + ']')
    L.append('    }' + ("," if i < len(noms) - 1 else ""))
L += ['  }', '}']
open(sys.argv[0].replace("v2.py", "v2_compact.json"), "w").write("\n".join(L) + "\n")
json.loads("\n".join(L))
