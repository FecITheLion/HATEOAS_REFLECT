```[BASE] Initial state={"largest_prime": 47, "candidate": 53, "schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}, "document": {"count": 3}, "last_mode": "step-prime", "last_actor": "client", "saved_at": "inspect_state.json"}
[INIT] Querying http://127.0.0.1:8002/options?prop=candidate ...
[INIT] Current=53 | Options=[53, 54, 53]
[INIT] Peer (inspect) options=[53, 54, 53]
[SET ] http://127.0.0.1:8002/set -> {'property': 'candidate', 'value': 54} | DIFF: ~$.candidate: 53 -> 54 | ~$.last_mode: "step-prime" -> "set:candidate" | ~$.saved_at: "inspect_state.json" -> "mutate_state.json"
[SAVE] http://127.0.0.1:8002/save -> file=mutate_state.json saved=True
[LOOP] Starting infinite loop from http://127.0.0.1:8001/?reader=mutate (timeout=10.0s, max_hops=infinite)
[HOP 001 | + 0.06s | rem= 9.94s] Following [peer_save_state] POST http://127.0.0.1:8002/save?reader=inspect
[HOP 001 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=55 (used=2)
[HOP 001 | DIFF] saved=True | ~$.candidate: 54 -> 56 | ~$.last_actor: "client" -> "mutate" | ~$.last_mode: "set:candidate" -> "step-prime"
[HOP 001 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 54, "to": 56}, "$.last_actor": {"from": "client", "to": "mutate"}, "$.last_mode": {"from": "set:candidate", "to": "step-prime"}}}
[HOP 002 | + 0.18s | rem= 9.82s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 002 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=56 (used=1)
[HOP 002 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 002 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 003 | + 0.29s | rem= 9.71s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 003 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=57 (used=3)
[HOP 003 | DIFF] saved=True | ~$.candidate: 56 -> 58 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 003 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 56, "to": 58}}}
[HOP 004 | + 0.41s | rem= 9.59s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 004 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=58 (used=2)
[HOP 004 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 004 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 005 | + 0.53s | rem= 9.47s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 005 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=59 (used=4)
[HOP 005 | DIFF] saved=True | ~$.candidate: 58 -> 60 | ~$.largest_prime: 47 -> 59 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 005 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 58, "to": 60}, "$.largest_prime": {"from": 47, "to": 59}}}
[HOP 006 | + 0.65s | rem= 9.35s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 006 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=60 (used=3)
[HOP 006 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 006 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 007 | + 0.77s | rem= 9.23s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 007 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=61 (used=5)
[HOP 007 | DIFF] saved=True | ~$.candidate: 60 -> 62 | ~$.largest_prime: 59 -> 61 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 007 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 60, "to": 62}, "$.largest_prime": {"from": 59, "to": 61}}}
[HOP 008 | + 0.96s | rem= 9.04s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 008 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=62 (used=4)
[HOP 008 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 008 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 009 | + 1.08s | rem= 8.92s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 009 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=63 (used=6)
[HOP 009 | DIFF] saved=True | ~$.candidate: 62 -> 64 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 009 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 62, "to": 64}}}
[HOP 010 | + 1.21s | rem= 8.79s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 010 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=64 (used=5)
[HOP 010 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 010 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 011 | + 1.34s | rem= 8.66s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 011 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=65 (used=7)
[HOP 011 | DIFF] saved=True | ~$.candidate: 64 -> 66 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 011 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 64, "to": 66}}}
[HOP 012 | + 1.47s | rem= 8.53s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 012 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=66 (used=6)
[HOP 012 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 012 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 013 | + 1.61s | rem= 8.39s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 013 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=67 (used=8)
[HOP 013 | DIFF] saved=True | ~$.candidate: 66 -> 68 | ~$.largest_prime: 61 -> 67 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 013 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 66, "to": 68}, "$.largest_prime": {"from": 61, "to": 67}}}
[HOP 014 | + 1.75s | rem= 8.25s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 014 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=68 (used=7)
[HOP 014 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 014 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 015 | + 1.88s | rem= 8.12s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 015 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=69 (used=9)
[HOP 015 | DIFF] saved=True | ~$.candidate: 68 -> 70 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 015 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 68, "to": 70}}}
[HOP 016 | + 2.00s | rem= 8.00s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 016 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=70 (used=8)
[HOP 016 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 016 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 017 | + 2.11s | rem= 7.89s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 017 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=71 (used=10)
[HOP 017 | DIFF] saved=True | ~$.candidate: 70 -> 72 | ~$.largest_prime: 67 -> 71 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 017 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 70, "to": 72}, "$.largest_prime": {"from": 67, "to": 71}}}
[HOP 018 | + 2.24s | rem= 7.76s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 018 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=72 (used=9)
[HOP 018 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 018 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 019 | + 2.36s | rem= 7.64s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 019 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=73 (used=11)
[HOP 019 | DIFF] saved=True | ~$.candidate: 72 -> 74 | ~$.largest_prime: 71 -> 73 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 019 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 72, "to": 74}, "$.largest_prime": {"from": 71, "to": 73}}}
[HOP 020 | + 2.59s | rem= 7.41s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 020 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=74 (used=10)
[HOP 020 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 020 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 021 | + 2.73s | rem= 7.27s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 021 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=75 (used=12)
[HOP 021 | DIFF] saved=True | ~$.candidate: 74 -> 76 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 021 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 74, "to": 76}}}
[HOP 022 | + 2.84s | rem= 7.16s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 022 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=76 (used=11)
[HOP 022 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 022 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 023 | + 2.96s | rem= 7.04s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 023 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=77 (used=13)
[HOP 023 | DIFF] saved=True | ~$.candidate: 76 -> 78 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 023 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 76, "to": 78}}}
[HOP 024 | + 3.08s | rem= 6.92s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 024 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=78 (used=12)
[HOP 024 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 024 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 025 | + 3.20s | rem= 6.80s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 025 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=79 (used=14)
[HOP 025 | DIFF] saved=True | ~$.candidate: 78 -> 80 | ~$.largest_prime: 73 -> 79 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 025 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 78, "to": 80}, "$.largest_prime": {"from": 73, "to": 79}}}
[HOP 026 | + 3.32s | rem= 6.68s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 026 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=80 (used=13)
[HOP 026 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 026 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 027 | + 3.46s | rem= 6.54s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 027 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=81 (used=15)
[HOP 027 | DIFF] saved=True | ~$.candidate: 80 -> 82 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 027 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 80, "to": 82}}}
[HOP 028 | + 3.63s | rem= 6.37s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 028 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=82 (used=14)
[HOP 028 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 028 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 029 | + 3.77s | rem= 6.23s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 029 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=83 (used=16)
[HOP 029 | DIFF] saved=True | ~$.candidate: 82 -> 84 | ~$.largest_prime: 79 -> 83 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 029 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 82, "to": 84}, "$.largest_prime": {"from": 79, "to": 83}}}
[HOP 030 | + 3.89s | rem= 6.11s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 030 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=84 (used=15)
[HOP 030 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 030 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 031 | + 4.02s | rem= 5.98s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 031 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=85 (used=17)
[HOP 031 | DIFF] saved=True | ~$.candidate: 84 -> 86 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 031 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 84, "to": 86}}}
[HOP 032 | + 4.19s | rem= 5.81s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 032 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=86 (used=16)
[HOP 032 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 032 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 033 | + 4.32s | rem= 5.68s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 033 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=87 (used=18)
[HOP 033 | DIFF] saved=True | ~$.candidate: 86 -> 88 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 033 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 86, "to": 88}}}
[HOP 034 | + 4.43s | rem= 5.57s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 034 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=88 (used=17)
[HOP 034 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 034 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 035 | + 4.56s | rem= 5.44s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 035 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=89 (used=19)
[HOP 035 | DIFF] saved=True | ~$.candidate: 88 -> 90 | ~$.largest_prime: 83 -> 89 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 035 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 88, "to": 90}, "$.largest_prime": {"from": 83, "to": 89}}}
[HOP 036 | + 4.68s | rem= 5.32s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 036 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=90 (used=18)
[HOP 036 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 036 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 037 | + 4.80s | rem= 5.20s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 037 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=91 (used=20)
[HOP 037 | DIFF] saved=True | ~$.candidate: 90 -> 92 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 037 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 90, "to": 92}}}
[HOP 038 | + 4.92s | rem= 5.08s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 038 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=92 (used=19)
[HOP 038 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 038 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 039 | + 5.05s | rem= 4.95s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 039 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=93 (used=21)
[HOP 039 | DIFF] saved=True | ~$.candidate: 92 -> 94 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 039 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 92, "to": 94}}}
[HOP 040 | + 5.17s | rem= 4.83s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 040 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=94 (used=20)
[HOP 040 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 040 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 041 | + 5.38s | rem= 4.62s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 041 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=95 (used=22)
[HOP 041 | DIFF] saved=True | ~$.candidate: 94 -> 96 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 041 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 94, "to": 96}}}
[HOP 042 | + 5.51s | rem= 4.49s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 042 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=96 (used=21)
[HOP 042 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 042 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 043 | + 5.62s | rem= 4.38s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 043 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=97 (used=23)
[HOP 043 | DIFF] saved=True | ~$.candidate: 96 -> 98 | ~$.largest_prime: 89 -> 97 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 043 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 96, "to": 98}, "$.largest_prime": {"from": 89, "to": 97}}}
[HOP 044 | + 5.75s | rem= 4.25s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 044 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=98 (used=22)
[HOP 044 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 044 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 045 | + 5.87s | rem= 4.13s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 045 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=99 (used=24)
[HOP 045 | DIFF] saved=True | ~$.candidate: 98 -> 100 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 045 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 98, "to": 100}}}
[HOP 046 | + 6.00s | rem= 4.00s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 046 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=100 (used=23)
[HOP 046 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 046 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 047 | + 6.11s | rem= 3.89s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 047 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=101 (used=25)
[HOP 047 | DIFF] saved=True | ~$.candidate: 100 -> 102 | ~$.largest_prime: 97 -> 101 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 047 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 100, "to": 102}, "$.largest_prime": {"from": 97, "to": 101}}}
[HOP 048 | + 6.25s | rem= 3.75s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 048 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=102 (used=24)
[HOP 048 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 048 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 049 | + 6.37s | rem= 3.63s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 049 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=103 (used=26)
[HOP 049 | DIFF] saved=True | ~$.candidate: 102 -> 104 | ~$.largest_prime: 101 -> 103 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 049 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 102, "to": 104}, "$.largest_prime": {"from": 101, "to": 103}}}
[HOP 050 | + 6.49s | rem= 3.51s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 050 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=104 (used=25)
[HOP 050 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 050 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 051 | + 6.62s | rem= 3.38s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 051 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=105 (used=27)
[HOP 051 | DIFF] saved=True | ~$.candidate: 104 -> 106 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 051 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 104, "to": 106}}}
[HOP 052 | + 6.82s | rem= 3.18s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 052 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=106 (used=26)
[HOP 052 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 052 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 053 | + 6.93s | rem= 3.07s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 053 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=107 (used=28)
[HOP 053 | DIFF] saved=True | ~$.candidate: 106 -> 108 | ~$.largest_prime: 103 -> 107 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 053 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 106, "to": 108}, "$.largest_prime": {"from": 103, "to": 107}}}
[HOP 054 | + 7.07s | rem= 2.93s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 054 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=108 (used=27)
[HOP 054 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 054 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 055 | + 7.21s | rem= 2.79s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 055 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=109 (used=29)
[HOP 055 | DIFF] saved=True | ~$.candidate: 108 -> 110 | ~$.largest_prime: 107 -> 109 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 055 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 108, "to": 110}, "$.largest_prime": {"from": 107, "to": 109}}}
[HOP 056 | + 7.35s | rem= 2.65s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 056 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=110 (used=28)
[HOP 056 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 056 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 057 | + 7.47s | rem= 2.53s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 057 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=111 (used=30)
[HOP 057 | DIFF] saved=True | ~$.candidate: 110 -> 112 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 057 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 110, "to": 112}}}
[HOP 058 | + 7.59s | rem= 2.41s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 058 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=112 (used=29)
[HOP 058 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 058 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 059 | + 7.71s | rem= 2.29s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 059 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=113 (used=31)
[HOP 059 | DIFF] saved=True | ~$.candidate: 112 -> 114 | ~$.largest_prime: 109 -> 113 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 059 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 112, "to": 114}, "$.largest_prime": {"from": 109, "to": 113}}}
[HOP 060 | + 7.84s | rem= 2.16s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 060 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=114 (used=30)
[HOP 060 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 060 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 061 | + 7.95s | rem= 2.05s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 061 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=115 (used=32)
[HOP 061 | DIFF] saved=True | ~$.candidate: 114 -> 116 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 061 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 114, "to": 116}}}
[HOP 062 | + 8.08s | rem= 1.92s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 062 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=116 (used=31)
[HOP 062 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 062 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 063 | + 8.40s | rem= 1.60s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 063 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=117 (used=33)
[HOP 063 | DIFF] saved=True | ~$.candidate: 116 -> 118 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 063 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 116, "to": 118}}}
[HOP 064 | + 8.52s | rem= 1.48s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 064 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=118 (used=32)
[HOP 064 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 064 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 065 | + 8.64s | rem= 1.36s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 065 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=119 (used=34)
[HOP 065 | DIFF] saved=True | ~$.candidate: 118 -> 120 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 065 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 118, "to": 120}}}
[HOP 066 | + 8.77s | rem= 1.23s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 066 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=120 (used=33)
[HOP 066 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 066 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 067 | + 8.89s | rem= 1.11s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 067 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=121 (used=35)
[HOP 067 | DIFF] saved=True | ~$.candidate: 120 -> 122 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 067 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 120, "to": 122}}}
[HOP 068 | + 9.01s | rem= 0.99s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 068 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=122 (used=34)
[HOP 068 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 068 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 069 | + 9.13s | rem= 0.87s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 069 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=123 (used=36)
[HOP 069 | DIFF] saved=True | ~$.candidate: 122 -> 124 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 069 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 122, "to": 124}}}
[HOP 070 | + 9.27s | rem= 0.73s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 070 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=124 (used=35)
[HOP 070 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 070 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 071 | + 9.39s | rem= 0.61s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 071 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=125 (used=37)
[HOP 071 | DIFF] saved=True | ~$.candidate: 124 -> 126 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 071 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 124, "to": 126}}}
[HOP 072 | + 9.51s | rem= 0.49s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 072 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=126 (used=36)
[HOP 072 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 072 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 073 | + 9.66s | rem= 0.34s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 073 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=127 (used=38)
[HOP 073 | DIFF] saved=True | ~$.candidate: 126 -> 128 | ~$.largest_prime: 113 -> 127 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 073 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 126, "to": 128}, "$.largest_prime": {"from": 113, "to": 127}}}
[HOP 074 | + 9.82s | rem= 0.18s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 074 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=128 (used=37)
[HOP 074 | DIFF] saved=True | -$.document: {"count": 3} | -$.last_actor: "mutate" | -$.last_mode: "step-prime" | -$.saved_at: "mutate_state.json" | -$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 074 | JSON] {"added": {}, "removed": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "changed": {}}
[HOP 075 | + 9.94s | rem= 0.06s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 075 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=129 (used=39)
[HOP 075 | DIFF] saved=True | ~$.candidate: 128 -> 130 | +$.document: {"count": 3} | +$.last_actor: "mutate" | +$.last_mode: "step-prime" | +$.saved_at: "mutate_state.json" | +$.schema: {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}
[HOP 075 | JSON] {"added": {"$.document": {"count": 3}, "$.last_actor": "mutate", "$.last_mode": "step-prime", "$.saved_at": "mutate_state.json", "$.schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}}, "removed": {}, "changed": {"$.candidate": {"from": 128, "to": 130}}}
[LOOP] Timeout reached (timeout after 10.00s); stopping loop.

[SUMMARY] Hops=75 | DiffEvents=76 | Elapsed=10.00s | Stop=timeout after 10.00s
[RESET] http://127.0.0.1:8002/reset -> True | http://127.0.0.1:8001/reset -> True```
