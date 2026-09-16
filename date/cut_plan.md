# Cut plan — DATE 2027 CAM-monitoring paper (16 → 6+1 pages)

Working copy: `date/main.tex` (single file). Baseline build: **16 pages** ≈ 14.7 body + 1.3 references.
DATE 2027 limit: **6 pages, plus one extra page for references only**. Final-paper deadline: **Sun 20 Sep 2026 AoE**.
So ≈ 9 body pages (≈ 60 %) have to go. The four contributions survive intact; what goes is repetition, tutorial
material, forward-looking lists, and five of twelve floats.

## 1. Page budget by section

| Section | Now | Target | What changes |
|---|---:|---:|---|
| Abstract | 0.45 | 0.25 | ~170 words. Keep the K ladder in one sentence, the CAM proposal, one result sentence per workload, the energy gap. |
| I. Introduction + Fig. 1 | 1.9 | 1.0 | Security-evaluation paragraph 230 → ~80 words (32 steps / 22 / 19 actions / OpenAI–HF as one sentence each). Interpretability paragraph → 3 sentences. Ladder: one clause per rung; drop the feature-dictionary rung and the spider footnote (VI keeps the example once). **Fig. 1 → panel (b) only**, caption 170 → ~60 words. Contributions kept, tightened. |
| II. Background (absorbs III) | 1.8 | 0.9 | II-B folded into II-A as 3 sentences (SRAM CAM in any CMOS; FeFET/RRAM = density, nonvolatility, multi-bit; BEOL prospect with two cites). II-A's FeFET matchline physics → 1 sentence + cite. II-C: probe/Eq. (1) → 3 sentences; drop the 2Ld / DeepSeek L·d aside and the 23.7 % → 1–3.5 % overhead history; ANN → 2 sentences; GSI APU said once (it is currently in II-B *and* II-C). **Sec. III becomes II-D "Cost model"**: Eqs. (1)–(2), the three crossings (H100 204K, A100 122K, Jetson 17K), the per-token argument in 2 sentences; drop the anchor-strip paragraph (VLA/video/voice rates — it exists to explain Fig. 1(b)'s strip). Table I stays. |
| IV. Mapping | 2.0 | 0.9 | Intro → 2 sentences. IV-A requirements kept (~100 words). IV-B first mapping → 1 paragraph (8,192→128 learned projection, 3-bit LSQ, Euclidean WTA, "384-bit-equivalent"); drop the INLP detail and the QAT footnote. Path-back → 1 sentence; delete the commented-out old IV-C. Encoding 1: Eq. (3) + 2 sentences (subarray split → a clause). Encoding 2: Eq. (4) + identity; 1FeFET-1C paragraph → 1 sentence (its citation is still "authors TBD"); drop the "not symmetric" paragraph (V says it, and the new matched-cell result closes it). Decision rule → ~80 words, **reworded per IB: score = fraction of deceptive rows among the 31 nearest, not a majority vote**. Encoding 3 → 3 sentences. |
| V. Workload 1 | 3.0 | 1.4 | Intro → 2 sentences. **Fig. 2 → bottom row (d)–(f) only**, full width, caption ~50 words; drop the "top row scores the first mapping" paragraph and its footnote (those four-domain numbers are the undergrads' pipeline, not IB's runs). V-A setup → ~120 words with the domain renames. V-B: three observations at ~60 % length; Table II stays (caption trimmed). **Fig. 3 cut** (23/90 cells > 0.05, worst −0.303 stated in text). **Fig. 4 cut** (coverage 82.5 % vs 48.1 % floor; 18.3 % vs 12.5 %; sycophancy row −0.204; recovery costs 75–100 % of the bank — all stated in text). V-C and V-D → one paragraph each. V-E audit → Table III + one paragraph, with the 384-b numbers. |
| VI. Workload 2 | 2.0 | 0.8 | Intro + VI-A → one paragraph (~90 words). VI-B watchlist → ~90 words. VI-C is the core: three observations at ~180 words total; **Fig. 5 kept, shorter** (panels (a)(b); drop (c) with VI-D), caption ~40 words. **VI-D cut** — its data is digitized from a deck and carries three known bugs; the conclusions note already calls it "the one a reviewer could catch us on". VI-E → ~100 words; **Fig. 6 cut** (6–33 MB vs 2.1 GB per layer stated in text). |
| VII. Hardware | 3.0 | 0.7 | VII-A and VII-B → 3 sentences each. **Table IV cut**, placement → 2 sentences (co-resident contention vs. appliance; BEOL as a one-clause outlook — MN's own flag says DATE reviewers are less forgiving). **Table V cut** (already on the driver's cut list). VII-D → ~80 words, closed by the recombination result. VII-E energy/latency estimate kept (~200 words) + **Table VI compacted to the measured/estimated rows** (drop the TBD rows). **VII-F cut**; one sentence of remaining work goes in the conclusions. |
| VIII. Limitations + Conclusions | 1.0 | 0.25 | Limitations → one paragraph (~90 words: no end-to-end system; label definition; per-response granularity; one model, one tuned layer; hardware numbers first-order). Conclusions → one paragraph (~120 words); it currently restates every number in the paper. |
| References | 1.3 | ≤ 1.0 | Drop the ~10 references orphaned by the cuts (serving-throughput roundup, VLA-Perf, feature dictionaries ×3, QAT/Apple, DeepSeek, cheap-monitors, first-gen CC, robust-ANN); strip `url` fields from arXiv/blog entries (IEEEtran prints them in full). |
| **Body total** | **14.7** | **≈ 6.0** | ~0.3 page of slack for the new one-sentence results below. |

## 2. Floats: 6 figures + 6 tables (≈ 3 pages) → 3 figures + 4 tables (≈ 1.6 pages)

Keep: Fig. 1(b) · Fig. 2(d–f) · Fig. 5(a,b) · Table I (design space) · Table II (encodings) · Table III (audit) · Table VI (cost model, compact).
Cut: Fig. 1(a) · Fig. 2(a–c) · Fig. 3 · Fig. 4 · Fig. 6 · Table IV (placement) · Table V (devices).
If still over after round 2: fold Table I into text (−0.2 p), then Table III (−0.15 p).

## 3. Results from IB's hand-off answers (each 1–2 sentences; they shorten the paper by closing open flags)

1. **Matched cell count** — thermometer at 768 b: 0.924 in-domain / 0.631 cross-domain vs ternary-384 0.920 / 0.640; ternary ahead in 54 of 90 cells (was 63). Replaces the "matched in bits, not silicon" caveat paragraph and the "paragraph to argue about" flag in V-B.
2. **Pooled ten-domain bank** — 0.906 (therm) / 0.909 (tern) vs 0.927 ceiling; sycophancy stays 0.63 vs the source paper's combined probe at 0.97. One sentence in V-B; it answers objection (1) of the companion appendix with our own numbers.
3. **Audit at 384 b** — mean 0.500 (ternary, all cells 0.40–0.56) and 0.501 (thermometer, 0.44–0.57). Replaces the 2,048-b "0.50 / 83 %" in V-E and closes that flag.
4. **Recombination** — frozen RP, 3-bit, Euclidean matchline: 0.920 / 0.579 vs Hamming 0.920 / 0.593 (unrounded Euclidean 0.916 / 0.598). Once the projection is frozen the multi-bit cell buys no accuracy, only fewer cells per row. Closes VII-D's "device result or projection artifact" question and removes the "checks queued" hedging in VI-C, VII-D, VII-F.
5. **GPU baselines (H100 PCIe, 131K rows)** — fp16 bank: 1.22 ms / 277 mJ per token at batch 1, 21 µs / 4.7 mJ at batch 64 (achieved 1.6–1.8 TB/s, so the 204K crossing is ~107K in practice). FAISS popcount on the 384-b codes: 28 µs / 2.1 mJ at batch 1, 0.5 µs / 0.04 mJ at batch 64. → Measured GPU column in Table VI. **Content decision for MN**: the popcount number says compression alone gets a GPU to ~3 % of its per-token budget at 10³ tok/s, so the CAM case rests on search energy (0.03–0.3 µJ vs 40 µJ–2 mJ) and no contention with inference, not on bandwidth alone. The text should say so.
6. **Decision-rule wording** — "the fraction of deceptive neighbors", not "majority label" (IV-E, V-E).
7. **Domain renames** — evidential → empirical, ethics → ethical, roleplay → roleplaying, insider_trd → insider trading; `repe_honesty` unchanged. Needs `gen_paper_figs.py` re-run for Fig. 2(d)–(f) labels.

## 4. Rounds

- **R1 — structural** (this session): drop the floats and subsections above, merge III→II, fold Limitations into Conclusions, delete commented-out text. Expect ~9 pages. Compile, sanity-check refs/cites.
- **R2 — paragraph compression** to 6.0 pages, in MN's voice rules (hedged first-person plural, en dashes, bold run-ins with colons, no self-referential framing). Add the seven items above.
- **R3 — references and polish**: prune bib, strip URLs, check overfull boxes, produce the With Comments build for MN.

## 5. Housekeeping question

`main.tex` carries ~60 resolved violet/orange review notes and the old commented-out IV-C. They do not print, but they double the file's length. Proposal: strip the resolved notes and dead comments in R1; keep only orange flags that are still open (fefet1c2026 authors, DAC citation, kim2023alscn author list, 1–3.5 % verification).
