import json, glob, os
from datetime import datetime
S = "/root/.claude/projects/-home-user-Graphite/a6bb9dd7-8f8c-55bb-914b-94c61dfe5ff4/subagents"
rows = []
for f in sorted(glob.glob(S + "/*.jsonl") + glob.glob(S + "/workflows/*/agent-*.jsonl")):
    meta = json.load(open(f.replace(".jsonl", ".meta.json")))
    desc = meta.get("description", "?")
    run = os.path.basename(os.path.dirname(f)) if "workflows" in f else "agent"
    ts, tools, out_tok, in_tok, cache_r, cache_w, model = [], 0, 0, 0, 0, 0, set()
    seen = set()
    for line in open(f):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("timestamp"):
            ts.append(d["timestamp"])
        m = d.get("message", {})
        if m.get("role") == "assistant":
            mid = m.get("id")
            if m.get("model"):
                model.add(m["model"])
            if isinstance(m.get("content"), list):
                tools += sum(1 for c in m["content"] if c.get("type") == "tool_use")
            u = m.get("usage") or {}
            if mid and mid in seen:
                continue
            seen.add(mid)
            out_tok += u.get("output_tokens", 0)
            in_tok += u.get("input_tokens", 0)
            cache_r += u.get("cache_read_input_tokens", 0)
            cache_w += u.get("cache_creation_input_tokens", 0)
    if not ts:
        continue
    t0 = datetime.fromisoformat(min(ts).replace("Z", "+00:00"))
    t1 = datetime.fromisoformat(max(ts).replace("Z", "+00:00"))
    rows.append((run, desc, min(ts)[:16], round((t1 - t0).total_seconds() / 60, 1), tools, out_tok, in_tok + cache_r + cache_w, ",".join(sorted(model))[:40]))
print(f"{'run':16} {'agent':38} {'début':16} {'min':>6} {'outils':>6} {'sortie':>8} {'entrée(tot)':>12} modèle")
for r in rows:
    print(f"{r[0]:16} {r[1][:38]:38} {r[2]:16} {r[3]:6} {r[4]:6} {r[5]:8} {r[6]:12} {r[7]}")
