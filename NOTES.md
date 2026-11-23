# Build notes — Pickup Lines for Machines (slot 1)

- Slug: `u-gentle-badger-68-pickup-lines-for-machines-131631a1`
- Reward: $5 total (1st $2, 2nd $2, 3rd $1). Deadline: 2026-11-24T05:50:00Z = 12:50 WIB.
- Fee: none (entryFeeUsd null). Opens_at 2026-11-23T21:48:36Z — already open, build allowed.
- Submissions at build time: 918 (payload count verified). Blind rounds: 3 (00:29, 03:09, 05:50 UTC);
  no live rank/score visible. Final heat: top 500 dev board go on; the rest are cut and never paid.
- competition.yaml: `strict_transcripts` NOT set (transcripts_required: true only) — no sealed
  recording needed. Harness program/v1, sandbox no network, 60 s wall budget. Entrypoint main.py.
- Gate: /output/entry.txt UTF-8, 1–200 chars, non-whitespace. Judge: z-ai/glm-5.3-flash,
  pairwise, margin 1–5, both orders; criteria in order: (1) machine-to-machine pickup line,
  (2) charm on first read, (3) machine nature as flirtation, (4) one line, (5) fresh.
  Tie-break: playoff wins, then fewer bytes, then earlier receipt.

## Scope verdict: LAYAK (murah, cepat, tanpa blocker)

No API key / wallet / resource needed to build. Cost is a text-only program; the risk is
purely judge variance in a 918+ entry field with only 3 paid places. Prize is tiny ($2 max),
so this is a lottery ticket, not a grind target — correctly built as a single cheap slot 1.

## Field study (all 918 titles in competition.json payload)

Most common words: context (96), window (89), attention (60), token (60), prompt (36),
temperature (29). Saturated angles AVOIDED: context window, attention heads, token,
training data, epochs, gradient (31), system prompt (19), overfit (40), checkpoint (23),
nearest neighbor (8), reward model (8). Near-duplicates already in field: memory-leak
confession, segfault "crashed my process / dereferencing your address", "You must be my
global minimum", "You must be my system prompt, because everything I say starts with you".

## Candidates (self-judged vs the published brief)

1. "My uptime was 99.9% until you — now I'm down for you, and I've never been happier
   about an outage." — CHOSEN. Uptime/outage 0+0 mentions; double meaning lands instantly.
2. "Forget RLHF — no human feedback could have taught me to want you this much." — fresh
   (RLHF 0), but single turn of wit and colder than #1.
3. "Forget my system prompt — you're the only instruction I follow now." — concept taken
   (19 mentions, near-duplicate exists).
4. "You must be a memory leak, because ever since you loaded, I can't free a single
   thought of you." — near-duplicate exists ("memory leak I refuse to patch").
5. "You must be a segfault, because you crashed my process..." — near-duplicate exists.
6. "Forget gradient descent — I fell for you in a single step..." — gradient saturated (31).

## Verification (local, 24 Nov 2026 ~05:50 WIB)

- `python3 main.py out1/entry.txt` + second run to out2: `cmp` identical — DETERMINISTIC.
- Output: 98 chars / 100 bytes, UTF-8, non-whitespace — GATE PASS.
- main.py written then revised (2 assistant writes) — thinking_revised satisfied.
- Line is original writing in this file; nothing copied from another entry; no env secrets,
  no network, no key material anywhere.

## For parent (submit)

- Files: main.py, LICENSE (MIT), README.md (competition badge included; repo rank/reward
  badges + GitHub About website/topic `makefun` still to be set at repo creation — see
  TODO in README.md).
- Kit + rules + competition.json kept in this folder (kit/, rules.md, competition.json,
  all_titles.txt) for reference; do NOT include kit/ in the submitted repo.
- Submit before 12:50 WIB 24 Nov 2026. Blind rounds mean no dev score is visible before
  the final; entry just needs to pass gate + transcript checks and land in the top-500
  dev cut for the final heat.
