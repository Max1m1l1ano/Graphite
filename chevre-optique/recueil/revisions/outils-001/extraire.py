"""Extrait les sorties structurées d'un journal de workflow : python3 extraire.py journal.jsonl sortie.json"""
import json
import sys

labels, res = {}, {}
for line in open(sys.argv[1], encoding="utf-8"):
    d = json.loads(line)
    if d.get("type") == "started":
        labels[d["key"]] = d.get("label")
    elif d.get("type") == "result":
        r = d["result"]
        if isinstance(r, str):
            r = json.loads(r)
        res[labels.get(d["key"], d["key"])] = r
json.dump(res, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: list(v)[:4] for k, v in res.items()})
