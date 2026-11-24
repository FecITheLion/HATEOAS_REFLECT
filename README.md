```[INIT] Querying http://127.0.0.1:8002/options?prop=candidate ...
[INIT] Current=3 | Options=[3, 4, 3]
[INIT] Peer (inspect) options=[3, 4, 3]
[SET ] http://127.0.0.1:8002/set -> {'property': 'candidate', 'value': 4}
[SAVE] http://127.0.0.1:8002/save -> file=mutate_state.json saved=True
[LOOP] Starting infinite loop from http://127.0.0.1:8001/?reader=mutate (timeout=5.0s, max_hops=infinite)
[HOP 001 | + 0.05s | rem= 4.95s] Following [peer_set_value] POST http://127.0.0.1:8002/set?prop=document&val=%7B%22count%22%3A%203%7D&reader=inspect
[HOP 001 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=5 (used=2)
[HOP 001 | DONE] updated={'property': 'candidate', 'value': 5} | saved=True
[HOP 002 | + 0.23s | rem= 4.77s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 002 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=6 (used=1)
[HOP 002 | DONE] updated={'property': 'candidate', 'value': 6} | saved=True
[HOP 003 | + 0.35s | rem= 4.65s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 003 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=7 (used=3)
[HOP 003 | DONE] updated={'property': 'candidate', 'value': 7} | saved=True
[HOP 004 | + 0.48s | rem= 4.52s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 004 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=8 (used=2)
[HOP 004 | DONE] updated={'property': 'candidate', 'value': 8} | saved=True
[HOP 005 | + 0.63s | rem= 4.37s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 005 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=9 (used=4)
[HOP 005 | DONE] updated={'property': 'candidate', 'value': 9} | saved=True
[HOP 006 | + 0.76s | rem= 4.24s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 006 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=10 (used=3)
[HOP 006 | DONE] updated={'property': 'candidate', 'value': 10} | saved=True
[HOP 007 | + 0.88s | rem= 4.12s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 007 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=11 (used=5)
[HOP 007 | DONE] updated={'property': 'candidate', 'value': 11} | saved=True
[HOP 008 | + 1.02s | rem= 3.98s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 008 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=12 (used=4)
[HOP 008 | DONE] updated={'property': 'candidate', 'value': 12} | saved=True
[HOP 009 | + 1.13s | rem= 3.87s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 009 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=13 (used=6)
[HOP 009 | DONE] updated={'property': 'candidate', 'value': 13} | saved=True
[HOP 010 | + 1.26s | rem= 3.74s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 010 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=14 (used=5)
[HOP 010 | DONE] updated={'property': 'candidate', 'value': 14} | saved=True
[HOP 011 | + 1.39s | rem= 3.61s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 011 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=15 (used=7)
[HOP 011 | DONE] updated={'property': 'candidate', 'value': 15} | saved=True
[HOP 012 | + 1.52s | rem= 3.48s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 012 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=16 (used=6)
[HOP 012 | DONE] updated={'property': 'candidate', 'value': 16} | saved=True
[HOP 013 | + 1.63s | rem= 3.37s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 013 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=17 (used=8)
[HOP 013 | DONE] updated={'property': 'candidate', 'value': 17} | saved=True
[HOP 014 | + 1.76s | rem= 3.24s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 014 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=18 (used=7)
[HOP 014 | DONE] updated={'property': 'candidate', 'value': 18} | saved=True
[HOP 015 | + 1.87s | rem= 3.13s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 015 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=19 (used=9)
[HOP 015 | DONE] updated={'property': 'candidate', 'value': 19} | saved=True
[HOP 016 | + 2.00s | rem= 3.00s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 016 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=20 (used=8)
[HOP 016 | DONE] updated={'property': 'candidate', 'value': 20} | saved=True
[HOP 017 | + 2.13s | rem= 2.87s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 017 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=21 (used=10)
[HOP 017 | DONE] updated={'property': 'candidate', 'value': 21} | saved=True
[HOP 018 | + 2.26s | rem= 2.74s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 018 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=22 (used=9)
[HOP 018 | DONE] updated={'property': 'candidate', 'value': 22} | saved=True
[HOP 019 | + 2.39s | rem= 2.61s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 019 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=23 (used=11)
[HOP 019 | DONE] updated={'property': 'candidate', 'value': 23} | saved=True
[HOP 020 | + 2.51s | rem= 2.49s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 020 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=24 (used=10)
[HOP 020 | DONE] updated={'property': 'candidate', 'value': 24} | saved=True
[HOP 021 | + 2.62s | rem= 2.38s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 021 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=25 (used=12)
[HOP 021 | DONE] updated={'property': 'candidate', 'value': 25} | saved=True
[HOP 022 | + 2.76s | rem= 2.24s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 022 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=26 (used=11)
[HOP 022 | DONE] updated={'property': 'candidate', 'value': 26} | saved=True
[HOP 023 | + 2.90s | rem= 2.10s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 023 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=27 (used=13)
[HOP 023 | DONE] updated={'property': 'candidate', 'value': 27} | saved=True
[HOP 024 | + 3.02s | rem= 1.98s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 024 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=28 (used=12)
[HOP 024 | DONE] updated={'property': 'candidate', 'value': 28} | saved=True
[HOP 025 | + 3.16s | rem= 1.84s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 025 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=29 (used=14)
[HOP 025 | DONE] updated={'property': 'candidate', 'value': 29} | saved=True
[HOP 026 | + 3.28s | rem= 1.72s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 026 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=30 (used=13)
[HOP 026 | DONE] updated={'property': 'candidate', 'value': 30} | saved=True
[HOP 027 | + 3.39s | rem= 1.61s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 027 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=31 (used=15)
[HOP 027 | DONE] updated={'property': 'candidate', 'value': 31} | saved=True
[HOP 028 | + 3.51s | rem= 1.49s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 028 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=32 (used=14)
[HOP 028 | DONE] updated={'property': 'candidate', 'value': 32} | saved=True
[HOP 029 | + 3.66s | rem= 1.34s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 029 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=33 (used=16)
[HOP 029 | DONE] updated={'property': 'candidate', 'value': 33} | saved=True
[HOP 030 | + 3.78s | rem= 1.22s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 030 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=34 (used=15)
[HOP 030 | DONE] updated={'property': 'candidate', 'value': 34} | saved=True
[HOP 031 | + 3.90s | rem= 1.10s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 031 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=35 (used=17)
[HOP 031 | DONE] updated={'property': 'candidate', 'value': 35} | saved=True
[HOP 032 | + 4.03s | rem= 0.97s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 032 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=36 (used=16)
[HOP 032 | DONE] updated={'property': 'candidate', 'value': 36} | saved=True
[HOP 033 | + 4.14s | rem= 0.86s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 033 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=37 (used=18)
[HOP 033 | DONE] updated={'property': 'candidate', 'value': 37} | saved=True
[HOP 034 | + 4.26s | rem= 0.74s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 034 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=38 (used=17)
[HOP 034 | DONE] updated={'property': 'candidate', 'value': 38} | saved=True
[HOP 035 | + 4.40s | rem= 0.60s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 035 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=39 (used=19)
[HOP 035 | DONE] updated={'property': 'candidate', 'value': 39} | saved=True
[HOP 036 | + 4.54s | rem= 0.46s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 036 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=40 (used=18)
[HOP 036 | DONE] updated={'property': 'candidate', 'value': 40} | saved=True
[HOP 037 | + 4.66s | rem= 0.34s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 037 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=41 (used=20)
[HOP 037 | DONE] updated={'property': 'candidate', 'value': 41} | saved=True
[HOP 038 | + 4.79s | rem= 0.21s] Following [peer_options] GET http://127.0.0.1:8001/options?prop=candidate&reader=mutate
[HOP 038 | OPT ] http://127.0.0.1:8001/options?prop=candidate -> picked=42 (used=19)
[HOP 038 | DONE] updated={'property': 'candidate', 'value': 42} | saved=True
[HOP 039 | + 4.92s | rem= 0.08s] Following [peer_options] GET http://127.0.0.1:8002/options?prop=candidate&reader=inspect
[HOP 039 | OPT ] http://127.0.0.1:8002/options?prop=candidate -> picked=43 (used=21)
[HOP 039 | DONE] updated={'property': 'candidate', 'value': 43} | saved=True
[LOOP] Timeout reached (timeout after 5.00s); stopping loop.

[SUMMARY] Hops=39 | Elapsed=5.00s | Stop=timeout after 5.00s
[RESET] Skipped (--skip-reset)```


```[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=22 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=24 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=26 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=28 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=30 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=32 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=34 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=36 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=38 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=40 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=42 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=44 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=46 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=48 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=50 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=52 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=54 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=56 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "POST /reset HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=6 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=8 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=10 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=12 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=14 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=16 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=18 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=20 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=22 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=24 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=26 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=28 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=30 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=32 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=34 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=36 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=38 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=40 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate&reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /options?prop=candidate HTTP/1.1" 200 -
[INSPECT :8001] "POST /set?prop=candidate&val=42 HTTP/1.1" 200 -
[INSPECT :8001] "POST /save HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET / HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET / HTTP/1.1" 200 -
[INSPECT :8001] "GET / HTTP/1.1" 200 -
[INSPECT :8001] "GET / HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET /?reader=mutate HTTP/1.1" 200 -
[INSPECT :8001] "GET / HTTP/1.1" 200 -```

```Two-way HATEOAS Mutate server on http://127.0.0.1:8002
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=3 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=document&val=%7B%22count%22%3A%203%7D&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop?hops=5 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /reset HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=11 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=document&val=%7B%22count%22%3A%203%7D&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop?hops=5 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /reset HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=11 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=document&val=%7B%22count%22%3A%203%7D&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop?hops=5 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /reset HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=document&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=document&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=document&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=document&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=10 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=11 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=13 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=14 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=16 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=17 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=19 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=20 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=19 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop?hops=5 HTTP/1.1" 200 -
[MUTATE  :8002] "GET /favicon.ico HTTP/1.1" 404 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop?hops=5 HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop?hops=5 HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop?hops=5 HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop?hops=5 HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop?hops=5 HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop?hops=5 HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop?hops=5 HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /loop HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=20 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save?reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=21 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=23 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=25 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=27 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=29 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=31 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=33 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=35 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=37 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=39 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=41 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=43 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=45 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=47 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=49 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=51 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=53 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=55 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /reset HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=4 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=document&val=%7B%22count%22%3A%203%7D&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=5 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=7 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=9 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=11 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=13 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=15 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=17 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=19 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=21 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=23 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=25 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=27 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=29 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=31 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=33 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=35 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=37 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=39 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=41 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate&reader=inspect HTTP/1.1" 200 -
[MUTATE  :8002] "GET /options?prop=candidate HTTP/1.1" 200 -
[MUTATE  :8002] "POST /set?prop=candidate&val=43 HTTP/1.1" 200 -
[MUTATE  :8002] "POST /save HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /?reader=mutate HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET / HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET / HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET / HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET / HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET / HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET / HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET / HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET / HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -
[MUTATE  :8002] "GET / HTTP/1.1" 200 -
[MUTATE  :8002] "GET /peer HTTP/1.1" 200 -```
