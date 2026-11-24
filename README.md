```python d.py --inspect-script a.py --mutate-script b.py --driver-script c.py --lock-file hateoas_io.lock --server mutate --prop largest_fib --timeout-seconds 10.0 --step-delay 0.1 --json-diff```


```[INSP_PROC] Callback-driven HATEOAS Inspect server on http://127.0.0.1:8001
[MUT_PROC] Callback-driven HATEOAS Mutate server on http://127.0.0.1:8002
[INSP_PROC] [INSPECT :8001] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /peer HTTP/1.1" 200 -
[DRV_PROC] [BASE] Initial state={"largest_prime": 2, "candidate": 3, "largest_fib": 1, "fib_candidate": 2, "schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}}, "document": {"count": "3"}, "script": ["candidate = 3", "largest_prime = 2", "fib_candidate = 2", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "script_version": 1, "last_mode": "init", "last_actor": "inspect", "saved_at": null}
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=list&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [AST ] Loaded AST functions count=4
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=2 HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=3&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [SET ] Body-free POST -> callback_next=mutate_step_prime | DIFF: ~$.fib_candidate: 2 -> 3 | ~$.largest_fib: 1 -> 2
[MUT_PROC] [MUTATE  :8002] "POST /save?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=3&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=save HTTP/1.1" 200 -
[DRV_PROC] [SAVE] Body-free POST saved=True
[DRV_PROC] [LOOP] Starting callback loop (timeout=10.0s, max_hops=infinite)
[DRV_PROC] [HOP 001 | + 0.57s | rem= 9.43s] Instruction [mutate_step_fib] POST http://127.0.0.1:8002/act?mode=step-fib&val=3&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-fib&val=3&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=3&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 001 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_prime
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B2%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 001 | PIPE] {"fn": "next_fib_after", "args": [2], "kwargs": {}, "result": 3, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 5, "to": 3}}, "returned_state_updates": {}, "state": {"largest_prime": 2, "candidate": 3, "largest_fib": 3, "fib_candidate": 3, "script_version": 4, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 001 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 4, 'largest_prime': 3, 'fib_candidate': 4, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=3&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=5&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 001 | DIFF] picked=3 | next=mutate_step_prime | ~$.candidate: 3 -> 5 | ~$.fib_candidate: 3 -> 2 | ~$.largest_fib: 2 -> 1 | ~$.largest_prime: 2 -> 3 | ~$.last_actor: "inspect" -> "mutate" | ~$.last_mode: "init" -> "script:exec" | ~$.script: ["candidate = 3", "largest_prime = 2", "fib_candidate = 2", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 3", "largest_prime = 2", "fib_candidate = 3", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 1 -> 4
[DRV_PROC] [HOP 001 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 3, "to": 5}, "$.fib_candidate": {"from": 3, "to": 2}, "$.largest_fib": {"from": 2, "to": 1}, "$.largest_prime": {"from": 2, "to": 3}, "$.last_actor": {"from": "inspect", "to": "mutate"}, "$.last_mode": {"from": "init", "to": "script:exec"}, "$.script": {"from": ["candidate = 3", "largest_prime = 2", "fib_candidate = 2", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 3", "largest_prime = 2", "fib_candidate = 3", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 1, "to": 4}}}
[DRV_PROC] [HOP 002 | + 0.79s | rem= 9.21s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=5&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=5&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=5&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 002 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 002 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 5, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 5, "candidate": 7, "largest_fib": 3, "fib_candidate": 2, "script_version": 7, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 002 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 6, 'largest_prime': 5, 'fib_candidate': 6, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=5&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=7&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 002 | DIFF] picked=5 | next=mutate_step_prime | ~$.candidate: 5 -> 7 | ~$.largest_prime: 3 -> 5 | ~$.script: ["candidate = 3", "largest_prime = 2", "fib_candidate = 3", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 5", "largest_prime = 2", "fib_candidate = 5", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 4 -> 7
[DRV_PROC] [HOP 002 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 5, "to": 7}, "$.largest_prime": {"from": 3, "to": 5}, "$.script": {"from": ["candidate = 3", "largest_prime = 2", "fib_candidate = 3", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 5", "largest_prime = 2", "fib_candidate = 5", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 4, "to": 7}}}
[DRV_PROC] [HOP 003 | + 1.00s | rem= 9.00s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=7&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=7&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=8&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 003 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 003 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 8, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 7, "candidate": 11, "largest_fib": 5, "fib_candidate": 2, "script_version": 10, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 003 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 8, 'largest_prime': 7, 'fib_candidate': 9, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=8&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=11&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 003 | DIFF] picked=8 | next=mutate_step_prime | ~$.candidate: 7 -> 11 | ~$.largest_prime: 5 -> 7 | ~$.script: ["candidate = 5", "largest_prime = 2", "fib_candidate = 5", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 7", "largest_prime = 2", "fib_candidate = 8", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 7 -> 10
[DRV_PROC] [HOP 003 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 7, "to": 11}, "$.largest_prime": {"from": 5, "to": 7}, "$.script": {"from": ["candidate = 5", "largest_prime = 2", "fib_candidate = 5", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 7", "largest_prime = 2", "fib_candidate = 8", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 7, "to": 10}}}
[DRV_PROC] [HOP 004 | + 1.24s | rem= 8.76s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=11&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=11&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=13&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 004 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 004 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 13, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 11, "candidate": 13, "largest_fib": 8, "fib_candidate": 2, "script_version": 13, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 004 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 12, 'largest_prime': 11, 'fib_candidate': 14, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=13&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=13&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 004 | DIFF] picked=13 | next=mutate_step_prime | ~$.candidate: 11 -> 13 | ~$.largest_prime: 7 -> 11 | ~$.script: ["candidate = 7", "largest_prime = 2", "fib_candidate = 8", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 11", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 10 -> 13
[DRV_PROC] [HOP 004 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 11, "to": 13}, "$.largest_prime": {"from": 7, "to": 11}, "$.script": {"from": ["candidate = 7", "largest_prime = 2", "fib_candidate = 8", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 11", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 10, "to": 13}}}
[DRV_PROC] [HOP 005 | + 1.43s | rem= 8.57s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=13&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=13&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=21&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 005 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 005 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 21, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 13, "candidate": 17, "largest_fib": 13, "fib_candidate": 2, "script_version": 16, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 005 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 14, 'largest_prime': 13, 'fib_candidate': 22, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=1&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=17&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 005 | DIFF] picked=1 | next=mutate_step_prime | ~$.candidate: 13 -> 17 | ~$.largest_prime: 11 -> 13 | ~$.script: ["candidate = 11", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 13", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 13 -> 16
[DRV_PROC] [HOP 005 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 13, "to": 17}, "$.largest_prime": {"from": 11, "to": 13}, "$.script": {"from": ["candidate = 11", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 13", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 13, "to": 16}}}
[DRV_PROC] [HOP 006 | + 1.64s | rem= 8.36s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=17&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=17&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 006 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 006 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {}, "returned_state_updates": {}, "state": {"largest_prime": 17, "candidate": 19, "largest_fib": 1, "fib_candidate": 2, "script_version": 19, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 006 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 18, 'largest_prime': 17, 'fib_candidate': 3, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=7&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=19&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 006 | DIFF] picked=7 | next=mutate_step_prime | ~$.candidate: 17 -> 19 | ~$.largest_prime: 13 -> 17 | ~$.script: ["candidate = 13", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 17", "largest_prime = 2", "fib_candidate = 2", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 16 -> 19
[DRV_PROC] [HOP 006 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 17, "to": 19}, "$.largest_prime": {"from": 13, "to": 17}, "$.script": {"from": ["candidate = 13", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 17", "largest_prime = 2", "fib_candidate = 2", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 16, "to": 19}}}
[DRV_PROC] [HOP 007 | + 1.82s | rem= 8.18s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=19&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=19&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=8&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 007 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 007 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 8, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 19, "candidate": 23, "largest_fib": 7, "fib_candidate": 2, "script_version": 22, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 007 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 20, 'largest_prime': 19, 'fib_candidate': 9, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=9&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=23&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 007 | DIFF] picked=9 | next=mutate_step_prime | ~$.candidate: 19 -> 23 | ~$.largest_prime: 17 -> 19 | ~$.script: ["candidate = 17", "largest_prime = 2", "fib_candidate = 2", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 19", "largest_prime = 2", "fib_candidate = 8", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 19 -> 22
[DRV_PROC] [HOP 007 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 19, "to": 23}, "$.largest_prime": {"from": 17, "to": 19}, "$.script": {"from": ["candidate = 17", "largest_prime = 2", "fib_candidate = 2", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 19", "largest_prime = 2", "fib_candidate = 8", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 19, "to": 22}}}
[DRV_PROC] [HOP 008 | + 2.01s | rem= 7.99s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=23&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=23&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=13&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 008 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 008 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 13, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 23, "candidate": 29, "largest_fib": 9, "fib_candidate": 2, "script_version": 25, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 008 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 24, 'largest_prime': 23, 'fib_candidate': 14, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=10&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=29&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 008 | DIFF] picked=10 | next=mutate_step_prime | ~$.candidate: 23 -> 29 | ~$.largest_prime: 19 -> 23 | ~$.script: ["candidate = 19", "largest_prime = 2", "fib_candidate = 8", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 23", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 22 -> 25
[DRV_PROC] [HOP 008 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 23, "to": 29}, "$.largest_prime": {"from": 19, "to": 23}, "$.script": {"from": ["candidate = 19", "largest_prime = 2", "fib_candidate = 8", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 23", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 22, "to": 25}}}
[DRV_PROC] [HOP 009 | + 2.18s | rem= 7.82s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=29&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=29&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=13&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 009 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 009 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 13, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 29, "candidate": 31, "largest_fib": 10, "fib_candidate": 2, "script_version": 28, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 009 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 30, 'largest_prime': 29, 'fib_candidate': 14, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=11&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=31&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 009 | DIFF] picked=11 | next=mutate_step_prime | ~$.candidate: 29 -> 31 | ~$.largest_prime: 23 -> 29 | ~$.script: ["candidate = 23", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 29", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 25 -> 28
[DRV_PROC] [HOP 009 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 29, "to": 31}, "$.largest_prime": {"from": 23, "to": 29}, "$.script": {"from": ["candidate = 23", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 29", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 25, "to": 28}}}
[DRV_PROC] [HOP 010 | + 2.37s | rem= 7.63s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=31&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=31&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=13&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 010 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 010 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 13, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 31, "candidate": 37, "largest_fib": 11, "fib_candidate": 2, "script_version": 31, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 010 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 32, 'largest_prime': 31, 'fib_candidate': 14, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=12&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=37&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 010 | DIFF] picked=12 | next=mutate_step_prime | ~$.candidate: 31 -> 37 | ~$.largest_prime: 29 -> 31 | ~$.script: ["candidate = 29", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 31", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 28 -> 31
[DRV_PROC] [HOP 010 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 31, "to": 37}, "$.largest_prime": {"from": 29, "to": 31}, "$.script": {"from": ["candidate = 29", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 31", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 28, "to": 31}}}
[DRV_PROC] [HOP 011 | + 2.56s | rem= 7.44s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=37&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=37&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=13&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 011 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 011 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 13, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 37, "candidate": 41, "largest_fib": 12, "fib_candidate": 2, "script_version": 34, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 011 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 38, 'largest_prime': 37, 'fib_candidate': 14, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=14&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=41&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 011 | DIFF] picked=14 | next=mutate_step_prime | ~$.candidate: 37 -> 41 | ~$.largest_prime: 31 -> 37 | ~$.script: ["candidate = 31", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 37", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 31 -> 34
[DRV_PROC] [HOP 011 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 37, "to": 41}, "$.largest_prime": {"from": 31, "to": 37}, "$.script": {"from": ["candidate = 31", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 37", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 31, "to": 34}}}
[DRV_PROC] [HOP 012 | + 2.81s | rem= 7.19s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=41&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=41&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=21&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 012 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 012 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 21, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 41, "candidate": 43, "largest_fib": 14, "fib_candidate": 2, "script_version": 37, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 012 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 42, 'largest_prime': 41, 'fib_candidate': 22, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=15&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=43&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 012 | DIFF] picked=15 | next=mutate_step_prime | ~$.candidate: 41 -> 43 | ~$.largest_prime: 37 -> 41 | ~$.script: ["candidate = 37", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 41", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 34 -> 37
[DRV_PROC] [HOP 012 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 41, "to": 43}, "$.largest_prime": {"from": 37, "to": 41}, "$.script": {"from": ["candidate = 37", "largest_prime = 2", "fib_candidate = 13", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 41", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 34, "to": 37}}}
[DRV_PROC] [HOP 013 | + 3.02s | rem= 6.98s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=43&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=43&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=21&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 013 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 013 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 21, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 43, "candidate": 47, "largest_fib": 15, "fib_candidate": 2, "script_version": 40, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 013 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 44, 'largest_prime': 43, 'fib_candidate': 22, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=16&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=47&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 013 | DIFF] picked=16 | next=mutate_step_prime | ~$.candidate: 43 -> 47 | ~$.largest_prime: 41 -> 43 | ~$.script: ["candidate = 41", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 43", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 37 -> 40
[DRV_PROC] [HOP 013 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 43, "to": 47}, "$.largest_prime": {"from": 41, "to": 43}, "$.script": {"from": ["candidate = 41", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 43", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 37, "to": 40}}}
[DRV_PROC] [HOP 014 | + 3.23s | rem= 6.77s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=47&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=47&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=21&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 014 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 014 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 21, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 47, "candidate": 53, "largest_fib": 16, "fib_candidate": 2, "script_version": 43, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 014 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 48, 'largest_prime': 47, 'fib_candidate': 22, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=17&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=53&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 014 | DIFF] picked=17 | next=mutate_step_prime | ~$.candidate: 47 -> 53 | ~$.largest_prime: 43 -> 47 | ~$.script: ["candidate = 43", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 47", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 40 -> 43
[DRV_PROC] [HOP 014 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 47, "to": 53}, "$.largest_prime": {"from": 43, "to": 47}, "$.script": {"from": ["candidate = 43", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 47", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 40, "to": 43}}}
[DRV_PROC] [HOP 015 | + 3.40s | rem= 6.60s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=53&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=53&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=21&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 015 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 015 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 21, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 53, "candidate": 59, "largest_fib": 17, "fib_candidate": 2, "script_version": 46, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 015 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 54, 'largest_prime': 53, 'fib_candidate': 22, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=18&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=59&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 015 | DIFF] picked=18 | next=mutate_step_prime | ~$.candidate: 53 -> 59 | ~$.largest_prime: 47 -> 53 | ~$.script: ["candidate = 47", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 53", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 43 -> 46
[DRV_PROC] [HOP 015 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 53, "to": 59}, "$.largest_prime": {"from": 47, "to": 53}, "$.script": {"from": ["candidate = 47", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 53", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 43, "to": 46}}}
[DRV_PROC] [HOP 016 | + 3.60s | rem= 6.40s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=59&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=59&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=21&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 016 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 016 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 21, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 59, "candidate": 61, "largest_fib": 18, "fib_candidate": 2, "script_version": 49, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 016 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 60, 'largest_prime': 59, 'fib_candidate': 22, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=19&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=61&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 016 | DIFF] picked=19 | next=mutate_step_prime | ~$.candidate: 59 -> 61 | ~$.largest_prime: 53 -> 59 | ~$.script: ["candidate = 53", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 59", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 46 -> 49
[DRV_PROC] [HOP 016 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 59, "to": 61}, "$.largest_prime": {"from": 53, "to": 59}, "$.script": {"from": ["candidate = 53", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 59", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 46, "to": 49}}}
[DRV_PROC] [HOP 017 | + 3.77s | rem= 6.23s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=61&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=61&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=21&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 017 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 017 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 21, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 61, "candidate": 67, "largest_fib": 19, "fib_candidate": 2, "script_version": 52, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 017 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 62, 'largest_prime': 61, 'fib_candidate': 22, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=20&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=67&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 017 | DIFF] picked=20 | next=mutate_step_prime | ~$.candidate: 61 -> 67 | ~$.largest_prime: 59 -> 61 | ~$.script: ["candidate = 59", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 61", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 49 -> 52
[DRV_PROC] [HOP 017 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 61, "to": 67}, "$.largest_prime": {"from": 59, "to": 61}, "$.script": {"from": ["candidate = 59", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 61", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 49, "to": 52}}}
[DRV_PROC] [HOP 018 | + 3.97s | rem= 6.03s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=67&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=67&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=21&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 018 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 018 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 21, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 67, "candidate": 71, "largest_fib": 20, "fib_candidate": 2, "script_version": 55, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 018 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 68, 'largest_prime': 67, 'fib_candidate': 22, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=21&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=71&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 018 | DIFF] picked=21 | next=mutate_step_prime | ~$.candidate: 67 -> 71 | ~$.largest_prime: 61 -> 67 | ~$.script: ["candidate = 61", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 67", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 52 -> 55
[DRV_PROC] [HOP 018 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 67, "to": 71}, "$.largest_prime": {"from": 61, "to": 67}, "$.script": {"from": ["candidate = 61", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 67", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 52, "to": 55}}}
[DRV_PROC] [HOP 019 | + 4.14s | rem= 5.86s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=71&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=71&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 019 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 019 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 71, "candidate": 73, "largest_fib": 21, "fib_candidate": 2, "script_version": 58, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 019 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 72, 'largest_prime': 71, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=22&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=73&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 019 | DIFF] picked=22 | next=mutate_step_prime | ~$.candidate: 71 -> 73 | ~$.largest_prime: 67 -> 71 | ~$.script: ["candidate = 67", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 71", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 55 -> 58
[DRV_PROC] [HOP 019 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 71, "to": 73}, "$.largest_prime": {"from": 67, "to": 71}, "$.script": {"from": ["candidate = 67", "largest_prime = 2", "fib_candidate = 21", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 71", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 55, "to": 58}}}
[DRV_PROC] [HOP 020 | + 4.32s | rem= 5.68s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=73&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=73&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 020 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 020 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 73, "candidate": 79, "largest_fib": 22, "fib_candidate": 2, "script_version": 61, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 020 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 74, 'largest_prime': 73, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=23&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=79&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 020 | DIFF] picked=23 | next=mutate_step_prime | ~$.candidate: 73 -> 79 | ~$.largest_prime: 71 -> 73 | ~$.script: ["candidate = 71", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 73", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 58 -> 61
[DRV_PROC] [HOP 020 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 73, "to": 79}, "$.largest_prime": {"from": 71, "to": 73}, "$.script": {"from": ["candidate = 71", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 73", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 58, "to": 61}}}
[DRV_PROC] [HOP 021 | + 4.53s | rem= 5.47s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=79&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=79&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 021 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 021 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 79, "candidate": 83, "largest_fib": 23, "fib_candidate": 2, "script_version": 64, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 021 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 80, 'largest_prime': 79, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=24&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=83&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 021 | DIFF] picked=24 | next=mutate_step_prime | ~$.candidate: 79 -> 83 | ~$.largest_prime: 73 -> 79 | ~$.script: ["candidate = 73", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 79", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 61 -> 64
[DRV_PROC] [HOP 021 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 79, "to": 83}, "$.largest_prime": {"from": 73, "to": 79}, "$.script": {"from": ["candidate = 73", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 79", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 61, "to": 64}}}
[DRV_PROC] [HOP 022 | + 4.74s | rem= 5.26s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=83&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=83&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 022 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 022 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 83, "candidate": 89, "largest_fib": 24, "fib_candidate": 2, "script_version": 67, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 022 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 84, 'largest_prime': 83, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=25&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=89&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 022 | DIFF] picked=25 | next=mutate_step_prime | ~$.candidate: 83 -> 89 | ~$.largest_prime: 79 -> 83 | ~$.script: ["candidate = 79", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 83", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 64 -> 67
[DRV_PROC] [HOP 022 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 83, "to": 89}, "$.largest_prime": {"from": 79, "to": 83}, "$.script": {"from": ["candidate = 79", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 83", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 64, "to": 67}}}
[DRV_PROC] [HOP 023 | + 4.93s | rem= 5.07s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=89&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=89&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 023 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 023 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 89, "candidate": 97, "largest_fib": 25, "fib_candidate": 2, "script_version": 70, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 023 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 90, 'largest_prime': 89, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=26&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=97&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 023 | DIFF] picked=26 | next=mutate_step_prime | ~$.candidate: 89 -> 97 | ~$.largest_prime: 83 -> 89 | ~$.script: ["candidate = 83", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 89", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 67 -> 70
[DRV_PROC] [HOP 023 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 89, "to": 97}, "$.largest_prime": {"from": 83, "to": 89}, "$.script": {"from": ["candidate = 83", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 89", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 67, "to": 70}}}
[DRV_PROC] [HOP 024 | + 5.13s | rem= 4.87s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=97&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=97&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 024 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 024 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 97, "candidate": 101, "largest_fib": 26, "fib_candidate": 2, "script_version": 73, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 024 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 98, 'largest_prime': 97, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=27&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=101&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 024 | DIFF] picked=27 | next=mutate_step_prime | ~$.candidate: 97 -> 101 | ~$.largest_prime: 89 -> 97 | ~$.script: ["candidate = 89", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 97", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 70 -> 73
[DRV_PROC] [HOP 024 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 97, "to": 101}, "$.largest_prime": {"from": 89, "to": 97}, "$.script": {"from": ["candidate = 89", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 97", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 70, "to": 73}}}
[DRV_PROC] [HOP 025 | + 5.36s | rem= 4.64s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=101&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=101&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 025 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 025 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 101, "candidate": 103, "largest_fib": 27, "fib_candidate": 2, "script_version": 76, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 025 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 102, 'largest_prime': 101, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=28&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=103&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 025 | DIFF] picked=28 | next=mutate_step_prime | ~$.candidate: 101 -> 103 | ~$.largest_prime: 97 -> 101 | ~$.script: ["candidate = 97", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 101", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 73 -> 76
[DRV_PROC] [HOP 025 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 101, "to": 103}, "$.largest_prime": {"from": 97, "to": 101}, "$.script": {"from": ["candidate = 97", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 101", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 73, "to": 76}}}
[DRV_PROC] [HOP 026 | + 5.55s | rem= 4.45s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=103&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=103&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 026 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 026 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 103, "candidate": 107, "largest_fib": 28, "fib_candidate": 2, "script_version": 79, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 026 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 104, 'largest_prime': 103, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=29&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=107&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 026 | DIFF] picked=29 | next=mutate_step_prime | ~$.candidate: 103 -> 107 | ~$.largest_prime: 101 -> 103 | ~$.script: ["candidate = 101", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 103", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 76 -> 79
[DRV_PROC] [HOP 026 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 103, "to": 107}, "$.largest_prime": {"from": 101, "to": 103}, "$.script": {"from": ["candidate = 101", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 103", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 76, "to": 79}}}
[DRV_PROC] [HOP 027 | + 5.75s | rem= 4.25s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=107&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=107&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 027 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 027 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 107, "candidate": 109, "largest_fib": 29, "fib_candidate": 2, "script_version": 82, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 027 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 108, 'largest_prime': 107, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=30&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=109&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 027 | DIFF] picked=30 | next=mutate_step_prime | ~$.candidate: 107 -> 109 | ~$.largest_prime: 103 -> 107 | ~$.script: ["candidate = 103", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 107", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 79 -> 82
[DRV_PROC] [HOP 027 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 107, "to": 109}, "$.largest_prime": {"from": 103, "to": 107}, "$.script": {"from": ["candidate = 103", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 107", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 79, "to": 82}}}
[DRV_PROC] [HOP 028 | + 5.94s | rem= 4.06s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=109&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=109&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 028 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 028 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 109, "candidate": 113, "largest_fib": 30, "fib_candidate": 2, "script_version": 85, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 028 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 110, 'largest_prime': 109, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=31&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=113&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 028 | DIFF] picked=31 | next=mutate_step_prime | ~$.candidate: 109 -> 113 | ~$.largest_prime: 107 -> 109 | ~$.script: ["candidate = 107", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 109", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 82 -> 85
[DRV_PROC] [HOP 028 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 109, "to": 113}, "$.largest_prime": {"from": 107, "to": 109}, "$.script": {"from": ["candidate = 107", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 109", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 82, "to": 85}}}
[DRV_PROC] [HOP 029 | + 6.18s | rem= 3.82s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=113&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=113&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 029 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 029 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 113, "candidate": 127, "largest_fib": 31, "fib_candidate": 2, "script_version": 88, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 029 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 114, 'largest_prime': 113, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=32&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=127&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 029 | DIFF] picked=32 | next=mutate_step_prime | ~$.candidate: 113 -> 127 | ~$.largest_prime: 109 -> 113 | ~$.script: ["candidate = 109", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 113", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 85 -> 88
[DRV_PROC] [HOP 029 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 113, "to": 127}, "$.largest_prime": {"from": 109, "to": 113}, "$.script": {"from": ["candidate = 109", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 113", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 85, "to": 88}}}
[DRV_PROC] [HOP 030 | + 6.36s | rem= 3.64s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=127&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=127&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 030 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 030 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 127, "candidate": 131, "largest_fib": 32, "fib_candidate": 2, "script_version": 91, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 030 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 128, 'largest_prime': 127, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=33&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=131&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 030 | DIFF] picked=33 | next=mutate_step_prime | ~$.candidate: 127 -> 131 | ~$.largest_prime: 113 -> 127 | ~$.script: ["candidate = 113", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 127", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 88 -> 91
[DRV_PROC] [HOP 030 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 127, "to": 131}, "$.largest_prime": {"from": 113, "to": 127}, "$.script": {"from": ["candidate = 113", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 127", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 88, "to": 91}}}
[DRV_PROC] [HOP 031 | + 6.55s | rem= 3.45s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=131&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=131&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=34&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 031 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 031 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 34, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 131, "candidate": 137, "largest_fib": 33, "fib_candidate": 2, "script_version": 94, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 031 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 132, 'largest_prime': 131, 'fib_candidate': 35, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=34&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=137&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 031 | DIFF] picked=34 | next=mutate_step_prime | ~$.candidate: 131 -> 137 | ~$.largest_prime: 127 -> 131 | ~$.script: ["candidate = 127", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 131", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 91 -> 94
[DRV_PROC] [HOP 031 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 131, "to": 137}, "$.largest_prime": {"from": 127, "to": 131}, "$.script": {"from": ["candidate = 127", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 131", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 91, "to": 94}}}
[DRV_PROC] [HOP 032 | + 6.72s | rem= 3.28s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=137&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=137&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 032 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 032 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 137, "candidate": 139, "largest_fib": 34, "fib_candidate": 2, "script_version": 97, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 032 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 138, 'largest_prime': 137, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=35&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=139&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 032 | DIFF] picked=35 | next=mutate_step_prime | ~$.candidate: 137 -> 139 | ~$.largest_prime: 131 -> 137 | ~$.script: ["candidate = 131", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 137", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 94 -> 97
[DRV_PROC] [HOP 032 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 137, "to": 139}, "$.largest_prime": {"from": 131, "to": 137}, "$.script": {"from": ["candidate = 131", "largest_prime = 2", "fib_candidate = 34", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 137", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 94, "to": 97}}}
[DRV_PROC] [HOP 033 | + 6.92s | rem= 3.08s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=139&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=139&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 033 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 033 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 139, "candidate": 149, "largest_fib": 35, "fib_candidate": 2, "script_version": 100, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 033 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 140, 'largest_prime': 139, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=36&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=149&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 033 | DIFF] picked=36 | next=mutate_step_prime | ~$.candidate: 139 -> 149 | ~$.largest_prime: 137 -> 139 | ~$.script: ["candidate = 137", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 139", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 97 -> 100
[DRV_PROC] [HOP 033 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 139, "to": 149}, "$.largest_prime": {"from": 137, "to": 139}, "$.script": {"from": ["candidate = 137", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 139", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 97, "to": 100}}}
[DRV_PROC] [HOP 034 | + 7.11s | rem= 2.89s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=149&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=149&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 034 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 034 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 149, "candidate": 151, "largest_fib": 36, "fib_candidate": 2, "script_version": 103, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 034 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 150, 'largest_prime': 149, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=37&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=151&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 034 | DIFF] picked=37 | next=mutate_step_prime | ~$.candidate: 149 -> 151 | ~$.largest_prime: 139 -> 149 | ~$.script: ["candidate = 139", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 149", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 100 -> 103
[DRV_PROC] [HOP 034 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 149, "to": 151}, "$.largest_prime": {"from": 139, "to": 149}, "$.script": {"from": ["candidate = 139", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 149", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 100, "to": 103}}}
[DRV_PROC] [HOP 035 | + 7.28s | rem= 2.72s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=151&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=151&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 035 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 035 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 151, "candidate": 157, "largest_fib": 37, "fib_candidate": 2, "script_version": 106, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 035 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 152, 'largest_prime': 151, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=38&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=157&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 035 | DIFF] picked=38 | next=mutate_step_prime | ~$.candidate: 151 -> 157 | ~$.largest_prime: 149 -> 151 | ~$.script: ["candidate = 149", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 151", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 103 -> 106
[DRV_PROC] [HOP 035 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 151, "to": 157}, "$.largest_prime": {"from": 149, "to": 151}, "$.script": {"from": ["candidate = 149", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 151", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 103, "to": 106}}}
[DRV_PROC] [HOP 036 | + 7.47s | rem= 2.53s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=157&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=157&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 036 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 036 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 157, "candidate": 163, "largest_fib": 38, "fib_candidate": 2, "script_version": 109, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 036 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 158, 'largest_prime': 157, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=39&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=163&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 036 | DIFF] picked=39 | next=mutate_step_prime | ~$.candidate: 157 -> 163 | ~$.largest_prime: 151 -> 157 | ~$.script: ["candidate = 151", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 157", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 106 -> 109
[DRV_PROC] [HOP 036 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 157, "to": 163}, "$.largest_prime": {"from": 151, "to": 157}, "$.script": {"from": ["candidate = 151", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 157", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 106, "to": 109}}}
[DRV_PROC] [HOP 037 | + 7.66s | rem= 2.34s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=163&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=163&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 037 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 037 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 163, "candidate": 167, "largest_fib": 39, "fib_candidate": 2, "script_version": 112, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 037 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 164, 'largest_prime': 163, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=40&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=167&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 037 | DIFF] picked=40 | next=mutate_step_prime | ~$.candidate: 163 -> 167 | ~$.largest_prime: 157 -> 163 | ~$.script: ["candidate = 157", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 163", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 109 -> 112
[DRV_PROC] [HOP 037 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 163, "to": 167}, "$.largest_prime": {"from": 157, "to": 163}, "$.script": {"from": ["candidate = 157", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 163", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 109, "to": 112}}}
[DRV_PROC] [HOP 038 | + 7.84s | rem= 2.16s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=167&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=167&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 038 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 038 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 167, "candidate": 173, "largest_fib": 40, "fib_candidate": 2, "script_version": 115, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 038 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 168, 'largest_prime': 167, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=41&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=173&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 038 | DIFF] picked=41 | next=mutate_step_prime | ~$.candidate: 167 -> 173 | ~$.largest_prime: 163 -> 167 | ~$.script: ["candidate = 163", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 167", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 112 -> 115
[DRV_PROC] [HOP 038 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 167, "to": 173}, "$.largest_prime": {"from": 163, "to": 167}, "$.script": {"from": ["candidate = 163", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 167", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 112, "to": 115}}}
[DRV_PROC] [HOP 039 | + 8.05s | rem= 1.95s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=173&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=173&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 039 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 039 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 173, "candidate": 179, "largest_fib": 41, "fib_candidate": 2, "script_version": 118, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 039 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 174, 'largest_prime': 173, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=42&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=179&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 039 | DIFF] picked=42 | next=mutate_step_prime | ~$.candidate: 173 -> 179 | ~$.largest_prime: 167 -> 173 | ~$.script: ["candidate = 167", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 173", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 115 -> 118
[DRV_PROC] [HOP 039 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 173, "to": 179}, "$.largest_prime": {"from": 167, "to": 173}, "$.script": {"from": ["candidate = 167", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 173", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 115, "to": 118}}}
[DRV_PROC] [HOP 040 | + 8.22s | rem= 1.78s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=179&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=179&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 040 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 040 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 179, "candidate": 181, "largest_fib": 42, "fib_candidate": 2, "script_version": 121, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 040 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 180, 'largest_prime': 179, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=43&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=181&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 040 | DIFF] picked=43 | next=mutate_step_prime | ~$.candidate: 179 -> 181 | ~$.largest_prime: 173 -> 179 | ~$.script: ["candidate = 173", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 179", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 118 -> 121
[DRV_PROC] [HOP 040 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 179, "to": 181}, "$.largest_prime": {"from": 173, "to": 179}, "$.script": {"from": ["candidate = 173", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 179", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 118, "to": 121}}}
[DRV_PROC] [HOP 041 | + 8.43s | rem= 1.57s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=181&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=181&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 041 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 041 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 181, "candidate": 191, "largest_fib": 43, "fib_candidate": 2, "script_version": 124, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 041 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 182, 'largest_prime': 181, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=44&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=191&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 041 | DIFF] picked=44 | next=mutate_step_prime | ~$.candidate: 181 -> 191 | ~$.largest_prime: 179 -> 181 | ~$.script: ["candidate = 179", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 181", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 121 -> 124
[DRV_PROC] [HOP 041 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 181, "to": 191}, "$.largest_prime": {"from": 179, "to": 181}, "$.script": {"from": ["candidate = 179", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 181", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 121, "to": 124}}}
[DRV_PROC] [HOP 042 | + 8.62s | rem= 1.38s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=191&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=191&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 042 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 042 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 191, "candidate": 193, "largest_fib": 44, "fib_candidate": 2, "script_version": 127, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 042 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 192, 'largest_prime': 191, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=45&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=193&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 042 | DIFF] picked=45 | next=mutate_step_prime | ~$.candidate: 191 -> 193 | ~$.largest_prime: 181 -> 191 | ~$.script: ["candidate = 181", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 191", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 124 -> 127
[DRV_PROC] [HOP 042 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 191, "to": 193}, "$.largest_prime": {"from": 181, "to": 191}, "$.script": {"from": ["candidate = 181", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 191", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 124, "to": 127}}}
[DRV_PROC] [HOP 043 | + 8.81s | rem= 1.19s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=193&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=193&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 043 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 043 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 193, "candidate": 197, "largest_fib": 45, "fib_candidate": 2, "script_version": 130, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 043 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 194, 'largest_prime': 193, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=46&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=197&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 043 | DIFF] picked=46 | next=mutate_step_prime | ~$.candidate: 193 -> 197 | ~$.largest_prime: 191 -> 193 | ~$.script: ["candidate = 191", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 193", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 127 -> 130
[DRV_PROC] [HOP 043 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 193, "to": 197}, "$.largest_prime": {"from": 191, "to": 193}, "$.script": {"from": ["candidate = 191", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 193", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 127, "to": 130}}}
[DRV_PROC] [HOP 044 | + 9.10s | rem= 0.90s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=197&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=197&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 044 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 044 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 197, "candidate": 199, "largest_fib": 46, "fib_candidate": 2, "script_version": 133, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 044 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 198, 'largest_prime': 197, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=47&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=199&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 044 | DIFF] picked=47 | next=mutate_step_prime | ~$.candidate: 197 -> 199 | ~$.largest_prime: 193 -> 197 | ~$.script: ["candidate = 193", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 197", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 130 -> 133
[DRV_PROC] [HOP 044 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 197, "to": 199}, "$.largest_prime": {"from": 193, "to": 197}, "$.script": {"from": ["candidate = 193", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 197", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 130, "to": 133}}}
[DRV_PROC] [HOP 045 | + 9.29s | rem= 0.71s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=199&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=199&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 045 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 045 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 199, "candidate": 211, "largest_fib": 47, "fib_candidate": 2, "script_version": 136, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 045 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 200, 'largest_prime': 199, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=48&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=211&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 045 | DIFF] picked=48 | next=mutate_step_prime | ~$.candidate: 199 -> 211 | ~$.largest_prime: 197 -> 199 | ~$.script: ["candidate = 197", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 199", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 133 -> 136
[DRV_PROC] [HOP 045 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 199, "to": 211}, "$.largest_prime": {"from": 197, "to": 199}, "$.script": {"from": ["candidate = 197", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 199", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 133, "to": 136}}}
[DRV_PROC] [HOP 046 | + 9.48s | rem= 0.52s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=211&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=211&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 046 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 046 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 211, "candidate": 223, "largest_fib": 48, "fib_candidate": 2, "script_version": 139, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 046 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 212, 'largest_prime': 211, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=49&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=223&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 046 | DIFF] picked=49 | next=mutate_step_prime | ~$.candidate: 211 -> 223 | ~$.largest_prime: 199 -> 211 | ~$.script: ["candidate = 199", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 211", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 136 -> 139
[DRV_PROC] [HOP 046 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 211, "to": 223}, "$.largest_prime": {"from": 199, "to": 211}, "$.script": {"from": ["candidate = 199", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 211", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 136, "to": 139}}}
[DRV_PROC] [HOP 047 | + 9.70s | rem= 0.30s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=223&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=223&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 047 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 047 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 223, "candidate": 227, "largest_fib": 49, "fib_candidate": 2, "script_version": 142, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 047 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 224, 'largest_prime': 223, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=50&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=227&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 047 | DIFF] picked=50 | next=mutate_step_prime | ~$.candidate: 223 -> 227 | ~$.largest_prime: 211 -> 223 | ~$.script: ["candidate = 211", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 223", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 139 -> 142
[DRV_PROC] [HOP 047 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 223, "to": 227}, "$.largest_prime": {"from": 211, "to": 223}, "$.script": {"from": ["candidate = 211", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 223", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 139, "to": 142}}}
[DRV_PROC] [HOP 048 | + 9.90s | rem= 0.10s] Instruction [mutate_step_prime] POST http://127.0.0.1:8002/act?mode=step-prime&val=227&reader=inspect
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /act?mode=step-prime&val=227&reader=inspect HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=step-prime HTTP/1.1" 200 -
[DRV_PROC] [HOP 048 | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> end_next=mutate_step_fib
[MUT_PROC] [MUTATE  :8002] "GET /ast?action=pipe&name=next_fib_after&args=%5B1%5D&pipe_mode=json_stream&reader=mutate HTTP/1.1" 200 -
[DRV_PROC] [HOP 048 | PIPE] {"fn": "next_fib_after", "args": [1], "kwargs": {}, "result": 2, "compiled_from_ast": true, "mutated_fields": {"fib_candidate": {"from": 55, "to": 2}}, "returned_state_updates": {}, "state": {"largest_prime": 227, "candidate": 229, "largest_fib": 50, "fib_candidate": 2, "script_version": 145, "last_mode": "fn:next_fib_after", "last_actor": "mutate"}}
[MUT_PROC] [MUTATE  :8002] "POST /script/exec?reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:exec HTTP/1.1" 200 -
[DRV_PROC] [HOP 048 | EXEC] http://127.0.0.1:8002/script/exec -> exec_ok=True updated_vars={'candidate': 228, 'largest_prime': 227, 'fib_candidate': 56, 'largest_fib': 1}
[MUT_PROC] [MUTATE  :8002] "GET /options?prop=largest_fib HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /set?prop=largest_fib&val=51&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=229&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=set:largest_fib HTTP/1.1" 200 -
[DRV_PROC] [HOP 048 | DIFF] picked=51 | next=mutate_step_prime | ~$.candidate: 227 -> 229 | ~$.largest_prime: 223 -> 227 | ~$.script: ["candidate = 223", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] -> ["candidate = 227", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"] | ~$.script_version: 142 -> 145
[DRV_PROC] [HOP 048 | JSON] {"added": {}, "removed": {}, "changed": {"$.candidate": {"from": 227, "to": 229}, "$.largest_prime": {"from": 223, "to": 227}, "$.script": {"from": ["candidate = 223", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"], "to": ["candidate = 227", "largest_prime = 2", "fib_candidate = 55", "largest_fib = 1", "if candidate % 2 != 0:", "    largest_prime = candidate", "candidate = candidate + 1", "fib_candidate = fib_candidate + 1"]}, "$.script_version": {"from": 142, "to": 145}}}
[DRV_PROC] [LOOP] Timeout reached (timeout after 10.00s); stopping loop.
[DRV_PROC]
[DRV_PROC] [SUMMARY] Hops=48 | DiffEvents=49 | Elapsed=10.00s | Stop=timeout after 10.00s
[MUT_PROC] [MUTATE  :8002] "POST /script/reset HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=55&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=script:reset HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /script/reset HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=229&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /callback?from=inspect&trigger=script:reset HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /reset HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=fib_candidate&val=2&reader=inspect HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /callback?from=mutate&trigger=reset HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "POST /reset HTTP/1.1" 200 -
[INSP_PROC] [INSPECT :8001] "GET /peer HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /script/mutate?op=set_var&var=candidate&val=3&reader=mutate HTTP/1.1" 200 -
[MUT_PROC] [MUTATE  :8002] "POST /callback?from=inspect&trigger=reset HTTP/1.1" 200 -
[DRV_PROC] [RESET] http://127.0.0.1:8002/reset -> True | http://127.0.0.1:8001/reset -> True
[RUNNER] Stopped mutate_server (pid=23472)
[RUNNER] Stopped inspect_server (pid=18628)```
