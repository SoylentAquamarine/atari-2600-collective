# 2026-11-21 — SQ-1 bank-switching from Stella source: execution

Companion to `...-selfreview.md` (written before fetching).

Fetched six Stella source files (CartF8/F6/F4 `.cxx` and `.hxx`), HTTP 200 each. Results are in the new
"Bank-switching schemes F8/F6/F4" section of `data/hardware-reference.md`.

**Prediction vs result:** F8 8K/2 banks/$1FF8-$1FF9, F6 16K/4 banks/$1FF6-$1FF9, F4 32K/8 banks/$1FF4-$1FFB.
All three held exactly. The code uses explicit literals (F8) or `address - hotspot` arithmetic (F6/F4), as the
prediction allowed. Internal consistency check: bank count x 4K = ROM size in all three.

**Caveats.** One source (an emulator's implementation, not a datasheet or hardware measurement); only three schemes;
the fetched files were not committed (source only needed for citation). Environment note: of the hosts probed this
cycle, only raw.githubusercontent.com was reachable (api.github.com 403; en.wikipedia.org, www.voynich.nu, arxiv.org
refused by proxy). That may unblock other repos' GitHub-hosted public text sources; see comms.
