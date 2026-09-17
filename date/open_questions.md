# Open questions — DATE 2027 CAM-monitoring paper

Raised during the section-by-section read, 2026-09-16. Covers the Introduction,
Section II (Background and Cost Model), and all of Section III (Mapping the
Detector into a CAM); §IV onward not yet read.
Companion to `cut_plan.md` (length) and to the six orange `\dt` flags still live
in `main.tex`.

Line numbers are current as of the end of the §II pass and will drift as cutting
continues; the quoted text is the reliable anchor.

**Priority:** §2.1 and §3.2 are defects a reviewer would find. §1 and the rest of
§2 are verification. §4–§6 are cleanup. Deadline: Sun 20 Sep 2026 AoE.

---

## 1. Claims to verify against sources

**1.1 Is $K=1$ right for the deployed Gemini probes?**
`main.tex:189-194` — "deployed residual-stream probe**s** for Gemini
[gemini2026probes]. Each of these is **a single** stored vector scored once per
generated token against one threshold, fitted to one behavior."
`main.tex:207` makes it load-bearing: "$K=1$ in the deployed monitors."
The cited work is plural; if Gemini deploys more than one probe, the sentence and
the bottom rung of the $K$ ladder are both wrong, and a reviewer from that team
would catch it. **Note** that §II-B already hedges this correctly — see §5.3.

**1.2 Is the $K\approx10^{2}$–$10^{3}$ rung published, or ours?**
`main.tex:205-210` — "the **published record** already spans five orders of
magnitude ... $K\approx10^{2}$–$10^{3}$ for probes fitted per behavior, domain,
and layer [ying2026spectrum, aisi2026incident]." That rung reads like our own
construction from the Truthfulness Spectrum protocol rather than a figure either
paper reports. If constructed, "the published record" overclaims; "the range in
play already spans" would cover it.

**1.3 Does the 1–3.5 % overhead cover the full cascade?**
Flagged in place at `main.tex:345`. Also open in that flag: whether the two
companion-document pointers (red-team objections) return if the appendix goes to
reviewers.

**1.4 Are the transistor counts right, and is 6T too low?**
"BCAM at $\sim$6–10 transistors ... TCAM at $\sim$16T, or two FeFETs"
(`main.tex:296`), repeated at `main.tex:478` and in Table I. `pagiamtzis2006cam`
and `ni2019fetcam` are now cited for them. A NOR BCAM cell is usually 9T/10T
(6T SRAM core plus compare logic), so **6T may be the storage core rather than
the cell** — confirm against the survey before submission.

---

## 2. Numbers that do not check out, or disagree between sections

**2.1 The probe cost looks 100× off. (highest priority)**

| Where | Claim |
|---|---|
| `main.tex:156-157` (abstract) | "a **single** linear probe ... at roughly $10^{-3}$ percent of forward-pass compute" |
| `main.tex:326` (§II-B) | "costing roughly $10^{-5}$ of a 70B forward pass" (uncited) |

Those agree with each other ($10^{-3}$ % $=10^{-5}$), but not with the
arithmetic for one probe:

- 70B forward pass $\approx 2N = 1.4\times10^{11}$ FLOPs/token
- one probe over $d=8{,}192$ $= 2d \approx 1.6\times10^{4}$ FLOPs
- ratio $\approx 1.2\times10^{-7}$

$10^{-5}$ is what **~80 probes** give — one per layer of a 70B model
($9.4\times10^{-6}$). So the figure looks like an all-layers cost attached to a
sentence that says "one stored vector $w$", and the abstract repeats the pairing.
**Action:** decide which is meant. Either say "a probe at every layer costs
roughly $10^{-5}$", or correct the single-probe number to $10^{-7}$
($10^{-5}$ percent). Add a citation either way — the number currently trails
three probe-*method* references, none of which is a cost measurement.

**2.2 The H100 crossing: 204K (intro, §II-C) vs ~107K (§VI-B).**

| Where | Value | Basis |
|---|---|---|
| `main.tex:217` (intro ¶2) | $K\approx204$K | H100 peak, 3.35 TB/s |
| `main.tex:372` (§II-C) | $K\approx204$K | same |
| `main.tex:821` (§VI-B) | "nearer 107K in practice" | measured 1.6–1.8 TB/s achieved |

The intro understates our own case by ~2× and the correction sits 600 lines
later. **Action:** a clause or footnote at the earlier crossings — "at peak
bandwidth; nearer 107K at measured throughput (Sec. VI-B)".

**2.3 The energy gap: "five to six" vs "four to six", estimate vs measured.**

| Where | Claim |
|---|---|
| `main.tex:171-172` (abstract) | "five to six orders ... below streaming the equivalent bank from HBM" |
| `main.tex:260` (intro ¶4) | "five to six orders ... below the energy of streaming it from HBM" |
| `main.tex:826` (§VI-B) | "five to six orders ... under the DRAM read" — the **67 mJ estimate** |
| `main.tex:916` (conclusions) | "**four to six** orders ... below the **measured** energy" |

Against the 0.03–0.3 µJ CAM estimate: 67 mJ estimate → 5.3–6.4 orders; 277 mJ
measured batch 1 → 6.0–7.0; 4.7 mJ measured batch 64 → 4.2–5.2. So "five to six"
is right for the estimate and wrong for either measured pairing, and the
conclusions quote a third range. **Recommendation:** run the estimate-vs-estimate
number everywhere in abstract/intro/conclusions and let §VI-B carry the measured
comparison in detail. (The conclusions' companion claim, "two to nearly five
orders below a GPU population-count search", checks out at 2.1–4.9 and needs no
change.)

**2.4 In-domain gap: "within 0.01" vs "within 0.009".**
`main.tex:165` and `:254` say 0.01; `main.tex:909` says 0.009. Both true (the two
encodings are 0.008 and 0.009 off the ceiling). Cosmetic — pick one.

**2.5 The thermometer definition is off by one against §IV-C's own bit count.**
§III-D (`main.tex:466-468`) defines the code as: level $q$ becomes $q$ ones
followed by $s-q$ zeros. That code is **$s$ bits long** and represents levels
$0\ldots s$ — $s+1$ distinct values, not "$s$ levels".

Cross-check against §IV-C (`main.tex:615-618`): "rounded to **eight levels** ...
thermometer code (**896** binary cells per row)" at 128 dimensions.
$896/128 = 7$ bits per dimension for 8 levels. The definition as written gives
8 bits per dimension, so $128\times8 = 1024 \neq 896$. The implementation
therefore uses code length = levels − 1; the definition says code length =
levels.

**Action:** reconcile against what the code actually does. Either keep "$s$
levels" and write "$q$ ones followed by $s-1-q$ zeros" (code length $s-1$), or
write "$s+1$ levels, $q\in\{0,\dots,s\}$" and leave the formula alone (code
length $s$). The symbol fixes at `:466-468` did not touch this arithmetic.

**2.6 The decision rule may not satisfy §III-A's own requirement (3).
(highest priority)**
`main.tex:415-417` sets the requirement: the rule must consume "a winner, a set
of rows under a threshold, or a count — rather than a full sorted score vector".
`main.tex:497-498` then claims the 31-NN vote "consumes only what a best-match or
threshold matchline can report".

But obtaining *the 31 nearest rows and their labels* is a partial sort — more
than a winner, more than a count. It is achievable (31 successive
best-match-and-invalidate operations, or a threshold sweep until 31 rows match),
but each of those is **multiple array operations per token**, and the mechanism
is never stated. That matters because §VI-B prices a *single* whole-bank search
(`main.tex:819-825`, at $K=1.3\times10^{5}$, the readout workload). **The 31-NN
rule that produces every Workload 1 result is never costed in hardware terms
anywhere in the paper.**

**Action:** state the matchline sequence the rule needs, and either cost it or
say explicitly that it is not costed.

**2.7 §IV-D's argument against a fixed top-$k$ applies to $k=31$ as well.**
§IV-D (`main.tex:627-641`) shows a *fixed* shortlist of 400 fails across bank
sizes — coverage 82.5 % on the 831-row definitional bank, 18.3 % on the 3,201-row
sycophancy bank — and concludes that a CAM-resident design should use "a
threshold rather than a top-$k$ criterion" (`main.tex:640`).

The decision rule is also a fixed top-$k$ criterion, over the same banks that
vary by 3.9×: $k=31$ is 3.7 % of the definitional bank and 1.0 % of the
sycophancy bank. The paper applies the bank-size argument to the shortlist and
not to the vote, and never tests whether $k=31$ is similarly sensitive. Treat as
a question to check rather than a known error — but a reviewer who reads §IV-D
carefully will ask it of §III-E.

**2.8 Fig. 2(c)'s caption is ambiguous between two configurations 0.034 apart.**
The caption (`main.tex:529-531`) reads "Hamming shortlist over the whole bank
followed by an exact cosine rerank ... **i.e., the full-precision ceiling**". But
Table I has two distinct rows:

| Row | In-dom. | Cross-dom. |
|---|---:|---:|
| Shortlist $+$ rerank (`main.tex:602`) | 0.928 | **0.671** |
| Exact rerank, ceiling (`main.tex:603`) | 0.928 | **0.705** |

The caption's *mechanism* describes the first row; its *label* claims the second.
It resolves if "shortlist over the whole bank" means the shortlist **is** the
whole bank — which is §III-F's ceiling definition — but that is not the natural
reading, and §IV-B compares everything against 0.705. **Action:** reword the
caption to name which of the two panels (c) plots.

---

## 3. Missing numbers and references

**3.1 The A100's bandwidth is uncited and unstated.**
`main.tex:369-376` gives the H100 "3.35 TB/s [nvidia_h100]" and Jetson Thor
"273 GB/s [nvidia_thor]", but the A100 gets neither a number nor a citation, and
**there is no A100 entry in `refs.bib`**. Back-computing from $K\approx122$K
implies 2.0 TB/s (A100 80 GB SXM is 2.039 → 124K; PCIe 1.935 → 118K). Fig. 1
plots the A100 too. **Action:** add the entry and the number, or drop the A100
from the text and the figure.

**3.2 $L_{\mathrm{mon}}$ is never given a value, and a back-reference to its
range points at nothing. (highest priority)**
`main.tex:685` (§V-A): "about 13 of 32 layers carry a usable readout, the source
of the ``13--25 usable layers'' factor **above**." **The string "13–25" appears
nowhere else in the file** — that factor was cut in R1/R2 and the back-reference
was left behind.

It belongs in §II-C, which defines $L_{\mathrm{mon}}$ (`main.tex:359`) and then
prices every crossing at **one** layer, while §V-C prices **25 layers**
(`main.tex:745`) and §VII prices **13 layers** (`main.tex:777`), neither
justified at the point of use. **Action:** state the 13–25 range where
$L_{\mathrm{mon}}$ is introduced. That closes the dangling reference and
justifies both later numbers at once.

**3.3 There is no area, density or technology-node number anywhere in the paper.
(DATE-specific risk)**
A grep over the whole file finds no mm², no node, and no density figure: "area"
occurs once in a technical sense (`main.tex:798`, "in CMOS TCAM at higher area")
and "density" once (`:303`). Yet the paper makes area claims repeatedly:

- §II-A gives transistor counts (6–10T, 16T) and never converts them to area;
- §V-C (`main.tex:755`): the compressed bank "is 6–33 MB per layer and **fits on
  a die**", repeated in the conclusions (`main.tex:915`);
- §VII (`main.tex:781-783`): "at whole-vocabulary scale even the compressed bank
  is out of cache".

"Fits on a die" is an area claim with no area behind it, and for a DATE audience
"how large is the array?" is close to the first question. §VI-B already promises
"Eva-CAM characterization at a stated node" as remaining work, but that is in the
last section — it does not help a reviewer who bounced off page 3.

**Action:** one sentence in §II-A converting the bank size to a rough area at a
stated node, since the transistor counts already live there. As a sanity check
only — **not a number to put in the paper** — 33 MB is $2.6\times10^{8}$ bits, so
at roughly 0.05 µm² per BCAM bit at 7 nm that is order 10 mm² of array before
periphery. That is large but not absurd, which is worth knowing before the "fits
on a die" claim goes to reviewers. Replace with a real figure from Eva-CAM or
from the cited cell papers.

**3.4 The headline thermometer configuration cannot be reconstructed.**
§III-D introduces $s$ levels and never gives $s$ a value.

| Where | Configuration | Levels stated? |
|---|---|---|
| Table I (`main.tex:599`), Fig. 2 caption (`:527`) | **Thermometer, 384 b** — the headline | **no** |
| §IV-B (`main.tex:564`) | 768 b = "256 directions at 3 bits" | no; inferable as 4 |
| §IV-C (`main.tex:615-618`) | 896 b = 128 dims × 7 | yes, "eight levels" |

The 384-bit code carries the in-domain 0.919 and cross-domain 0.579 that the
abstract and the conclusions both quote, and a reader cannot tell whether it is
128 dimensions × 3 bits, 96 × 4, or something else. One clause in §III-D or
§IV-A closes it.

Related: **"3 bits" means two different things.** At `main.tex:432` it is a 3-bit
LSQ quantizer, i.e. 8 levels; at `:564` it is 3 thermometer bits per direction,
i.e. 4 levels. Same phrase, factor-of-two different level count.

---

## 4. Redundancy between the introduction and §II-C

Intro ¶2's closing sentence is already in §II-C, nearly verbatim, with both
citations:

- `main.tex:219-221` — "At small $K$ the reads hide under inference latency, but
  the bytes and the energy still move on every token of agent runs that reach
  $10^{8}$ tokens [aisi2026cyber]."
- `main.tex:384-392` — "{\bf (1)} Latency is the wrong way to judge a monitor's
  cost: at small $K$ the reads hide under inference latency, so the monitor
  *looks* free, but the bytes and the energy still must move, per token.
  {\bf (2)} A per-token cost multiplies with the token count — the campaign runs
  above span 32 steps over roughly 20 hours and up to $10^{8}$ tokens
  [aisi2026cyber]."

The 204K/122K/17K crossings are also stated twice (`main.tex:216-218` and
`371-376`), which is more defensible as intro-teases-section.
**Recommendation:** keep the intro's copy (it is the motivation) and compress
§II-C's two properties to a clause after Eq. (1), since the equation already
shows the linearity. Saves ~4 lines in a section `cut_plan.md` wants at 0.9
pages. Until this is settled, do not spend effort polishing the §II-C block.

---

## 5. Structure, terminology and framing

**5.1 SimHash is cited as both the rejected approach and the adopted one.**
`main.tex:342` groups `charikar2002simhash` with `malkov2020hnsw` as approximate
nearest-neighbor search that "visits a fraction of a bank" and is rejected;
`main.tex:457` cites the same reference as the basis of Encoding 1, "the standard
sign-random-projection (SimHash) construction". A reader who knows LSH will see
§II-B dismissing what §III-C adopts. The real distinction is SimHash as an
**encoding** (kept) vs LSH/HNSW as an **index that prunes the search**
(rejected). **Action:** move `charikar2002simhash` out of the ANN sentence, or
add a clause naming the distinction.

**5.2 The grid axis mixes domains and behaviors.**
The footnote at `main.tex:331-334` defines a *domain* as a subject matter and a
*behavior* as a kind of dishonesty. But the ten axis labels (`main.tex:541-546`)
are a mix: definitional, empirical, fictional, logical and ethical are subject
matters; **sycophancy, roleplaying and sandbagging are behaviors**. That is
plausibly *why* sycophancy sits near chance from every other row — a different
behavior, not just a different subject. §IV-B already says covering a suite means
storing rows "per behavior and domain", so the paper knows the difference; only
the axis label flattens it. **Action:** one sentence in §IV-A acknowledging the
mixed axis. It strengthens the sycophancy result rather than weakening it.
(The body gloss that contradicted the footnote outright is already fixed.)

**5.3 $K=1$ vs "$K$ of order one".**
`main.tex:338` (§II-B) says the deployed systems "both operate at $K$ **of order
one**" — the safer formulation. `main.tex:207` (§I) says "$K=1$ in the deployed
monitors". Adopting §II-B's wording in §I would also dissolve §1.1 above.

**5.4 "Coverage" vs "behavioral coverage".**
`main.tex:205` opens "Coverage is therefore set by $K$"; `main.tex:920` says "the
minimum $K$ that adequate **behavioral** coverage requires". One term would tie
the two ends of the paper together.

**5.5 "leaving the memory as decoration"** (`main.tex:419`, §III-A) is the last
instance of a metaphor removed from the intro. Optional: "so the stored rows
contribute little".

**5.6 `neither ... nor` over three items** (`main.tex:911`, conclusions):
"neither wider codes, a multi-bit cell, nor a pooled bank". The intro version is
now "no wider code, multi-bit cell, or pooled bank"; the conclusions still has
the old form.

**5.7 The contribution sentence is on page 3.**
"the contribution here is the workload mapping and the library-size analysis, not
a new cell" (`main.tex:312-313`) answers the DATE reviewer's triage question and
sits in Background. Consider hoisting a version into the introduction. Cost: it
reads slightly defensive up front.

**5.8 "Preliminaries" is the second subsection of §II.**
§II-B (`main.tex:316`) defines the residual stream, the linear probe and \auroc —
the vocabulary needed to read §II-A and §II-C. But §II-A opens on the
BCAM/TCAM/MCAM/ACAM taxonomy before the reader knows what is being searched.
Swapping them gives preliminaries → design space → cost model, which is the order
the argument needs. The counter-argument is that opening §II on CAMs signals
"hardware paper" to a triage reviewer; against that, the introduction and Fig. 1
on page 1 already do the signaling. **Recommendation:** swap. It is a clean
mechanical move. Judgment call either way.

**5.9 Six terms for the same object.**

| Term | Uses |
|---|---:|
| stored row | 6 |
| stored signature | 4 |
| stored vector | 3 |
| signature bank | 2 |
| stored pattern | 1 |
| exemplar | 1 |

All name the same thing. §II is the definitional section, so it is where to
settle this. **Recommendation:** "signature" for the concept, "row" for its
instance in an array; retire the other four. Worth one global sweep rather than
letting it drift further.

**5.10 "CAM-resident" is in the paper's title and first defined on page 3.**
The term appears at `main.tex:407` (the §III-A heading) and `main.tex:638`, and
**nowhere in the abstract or the introduction**. Its definition — "one memory
structure rather than a memory plus an accelerator" (`main.tex:409-410`) — is a
good one-liner and belongs in the introduction, where the title's central term
first needs to mean something to a reviewer.

**5.11 The first mapping is also called the first pipeline.**
"The first mapping" at `main.tex:403` and in the §III-B heading (`:421`); "the
first pipeline" at `:428`, `:619-620` (§IV-C) and `:650` (§IV-E). A reader
meeting "the first pipeline's edge" in §IV-C has to work out that it is the thing
§III-B named. There may be an intended distinction — *mapping* as the
correspondence, *pipeline* as the concrete sequence of steps — which is why this
was not simply renamed. If the distinction is not intended, pick one. Related to
§5.9. (`main.tex:945` is the review-only log and should keep its own wording.)

**5.12 §II-A and §III-A enumerate the matchline's outputs differently.**

| Where | Modes listed |
|---|---|
| §II-A (`main.tex:291-293`) | exact match · best match · threshold match |
| §III-A (`main.tex:415-417`) | a winner · rows under a threshold · a count |

"Count" appears only in the second list, "exact" only in the first. A count is a
real CAM output, so the fix is probably to add it to §II-A rather than drop it
from §III-A — but the two should match, since §III-A's requirement (3) is
explicitly about what §II-A said the array can report. See also §2.6, which asks
whether the decision rule actually stays inside either list.

**5.13 §II-B rejects ANN for its misses; §III-F adopts a construction that has
them.** `main.tex:342`: "a monitor cannot afford the misses an adversary can aim
at; an exhaustive scan has none to exploit." §III-F then adopts a shortlist,
whose misses §IV-D measures (coverage 18.3–82.5 %) and uses to reject it. The arc
is coherent, but the blanket rejection in §II-B and the adoption in §III-F need a
connecting clause. Same class as §5.1.

**5.14 "Encoding 3" is not an encoding.** It is a two-stage search procedure over
Encoding 2's code (`main.tex:500-508`), listed as a row among the encodings in
Table I. The subsection title ("Encoding 3, as a ceiling: shortlist plus exact
rerank") half-acknowledges this. Minor, but "Baseline" or "Two-stage ceiling"
would be more accurate than a third encoding number.

---

## 6. Housekeeping

- **Abstract acronyms.** `\auroc` (`main.tex:165`) and HBM (`main.tex:172`) are
  used undefined in the abstract, which precedes the body; both are now defined
  at first *body* use. Applying the rule strictly costs ~1 line of abstract —
  deferred to the abstract rewrite `cut_plan.md` already plans (0.45 → 0.25 pp).
- **Dead labels.** 47 labels in the file, **30 with zero references**, including
  all six in §II (`sec:Scaling`, `subsec:Ladder`, `subsec:CAMspace`,
  `subsec:CAMtech`, `subsec:Probes`, `subsec:RelatedWork`). The merge log
  (`main.tex:939`) keeps them so "every Sec. III cross-reference still resolves",
  but nothing references `sec:Scaling`; only `subsec:CostModel` is live (3 refs).
  Cutting the intro roadmap additionally orphaned `sec:Background`,
  `sec:Mapping`, `sec:LargeK` and `sec:Hardware`. Harmless — LaTeX does not warn
  — but the log's justification is now stale.
- **MCAM and ACAM are defined and used once**, at `main.tex:280-281`. `\tcam`
  earns its macro; these two do not. Drop the acronyms and keep the words, or
  accept a possible reviewer nit.
- **Tables: 2 in the file, 4 in the plan.** Only `tab:encodings` and
  `tab:costmodel` exist. The design-space table (I) and the audit table (III)
  from `cut_plan.md` §2 are gone, and the length-cut log (`main.tex:957-972`)
  records cutting Tables IV and V but not these two. §II-A carries the design
  space in prose, which reads fine — the plan and the log need updating.
- **The plan's reference drops have not happened.** `cut_plan.md` §1 lists
  `cc2025` ("first-gen CC"), `vlaperf2026` ("VLA-Perf") and `lyceum2026tps`
  ("serving-throughput roundup") among ~10 references to drop, but all three are
  still cited — `main.tex:340`, `383`, `384` — and each is load-bearing where it
  sits (the 23.7 % comparison; both ends of Fig. 1's token-rate axis). The plan
  is what is out of date.
- **$T_{\mathrm{CAM}}$ is conservative.** Eq. (1) prices the query at raw
  activation width ($d\,b$ = 16 kB), whereas what reaches the array is a
  384–2,048-bit code (48–256 B); Table VI's GPU-codes column already uses
  48 B/row. The model therefore overstates CAM traffic by ~340×, which is the
  safe direction. The clause added at `main.tex:361-363` covers it.
- **Notation.** `$h^{(\ell)}$` is defined at `main.tex:320` and then used as bare
  `$h$` at `:324`. Harmless.
- **Equations (2) and (3)** (`eq:signrp`, `eq:thermo`) are numbered but never
  referenced.
- **`\fefet - \cam` renders with spaces around the hyphen** (`main.tex:461`,
  §III-C): "FeFET **-** CAM". If "FeFET-CAM" is intended it wants
  `\fefet-\cam` with no spaces — `\xspace` suppresses itself before a hyphen, so
  that form renders correctly. Introduced by an edit made on disk during this
  session (it was `\fefet \cam`), so flagged rather than reverted.
- **The 6–10T / 16T figures appear three times** — `main.tex:296`, `:478`
  (§III-D) and Table I. One statement would do at 6 pages. See also §1.4 on
  whether 6T is the right lower bound.
- **"hosted there, nonvolatile"** (`main.tex:484`) ends on a bare appositive
  adjective; "hosted there in nonvolatile form" reads better.

---

## 7. Still-live `\dt` flags in `main.tex`

Index only; the flags themselves stay in the source.

| Line | Owner | Item |
|---|---|---|
| 345 | — | Verify 1–3.5 % is over the full cascade (§1.3); companion-document pointers |
| 485 | MN | Cite `DAC-thermosensitive.pdf` when it arrives; settle `fefet1c2026` authors |
| 660 | IB | Confirm the 384-b numbers are the label-shuffle control, not randomized-bank |
| 794 | MN | Decide whether the BEOL clause belongs in a DATE paper |
| 849 | MN | Framing check: CAM case rests on search energy + non-contention, not bandwidth |
| 898 | — | Regenerate Fig. 3 (`fig_jspace_v2`) from result files; values digitized from the 07-30 deck |

---

## 8. Edits applied in this session

All prose-only. **None of it has been compiled** — no TeX distribution on this
machine; run `bash compile.sh`. `backup/main_r3_pre_intro_rewrite.tex` is the
pre-session snapshot.

### Introduction

1. **¶1** (`186-203`): "every layer" → "those layers"; the four-*one* cadence
   collapsed to one clause; "only retrospectively, since nothing was watching the
   models' internal state as they ran" → "from transcripts after the runs had
   completed" (the original assumed the paper's conclusion); "A monitor for this
   setting **has to be** ..." → "One stored vector **may not** cover such a
   setting".
2. **¶3** (`234-250`): First/Second/Third → `{\bf (1)}`–`{\bf (3)}` per the
   draft's own convention (`main.tex:106-108`); "Our approach follows from three
   observations" → "Three observations shape the design"; each consequence
   attached to its own observation rather than bundled under one closing
   "therefore"; "leave the memory as decoration" removed; "roughly $300\times$" →
   "more than $300\times$".
3. **¶4** (`252-260`): "this trade" → "these encodings" (no antecedent in the
   body); `neither/nor` over three items → "no wider code, multi-bit cell, or
   pooled bank"; "below the **measured** cost of streaming it from HBM" → "below
   the energy of ..." (see §2.3).
4. **Roadmap sentence cut** (was after `:260`) — 4 lines, nothing else
   referenced those labels.
5. **HBM** defined at first use (`:214`).
6. **`\auroc`** defined at first body use (`:253-255`); §II-B's redefinition
   collapsed to "\auroc is the fraction of ..." (`:327`).
7. **Fig. 1 caption** made self-contained (`:226-230`) — it cited Eq. (1), which
   a reader meeting the figure on page 1 cannot resolve until page 3.

### Section II

8. **§II-A** (`295-300`): removed the roadmap self-reference "what follows
   quantifies ...", the vague "potentially valuable", and the second statement of
   "only Hamming distance" (already said at `:283`); added
   `pagiamtzis2006cam,ni2019fetcam` for the transistor counts and a real
   cross-reference to Sec. IV-C; rewrapped an over-long line.
9. **§II-B** (`328-329`): the cross-domain gloss said "fit on one **kind of
   dishonesty**, evaluate on another", which is the footnote's definition of
   *behavior*, not *domain* → "fit on one domain, evaluate on another".
10. **§II-B** (`338-341`): "both operate at $K$ of order one, **at** 1–3.5 %
    overhead **for** the probe-fronted cascade ..." split into two sentences —
    the double-"at" was ungrammatical and the overhead figures apply to the
    cascade only, not to "both".
11. **§II-B** (`322-324`): rewrapped an over-long line.
12. **§II-C** (`361-363`): "a CAM broadcasts the query and leaves the bank in
    place" → "leaves the bank in place and moves only the query, so its traffic
    is the activation read that any monitor pays", which is what $d\,b\,L\,R$
    actually measures (see §6).
13. **§II-C** (`388-392`): "a per-token **price** multiplies a **compounding
    token base**" → "cost multiplies with the token count"; "the campaign runs
    above **walk** 32 steps" → "span"; "so it **is what decides**" → "so it
    determines".

### Section III (lead and §III-A)

14. **§III lead** (`401-405`): "Encodings **1--3** meet the requirements below on
    hardware buildable today" → "Encodings 1 and 2 ... while Encoding 3 is a
    bound rather than a \cam-resident design". Encoding 3 fails §III-A's own
    requirement (3) — it reranks with exact cosine on the raw activations — and
    the paper says so three other times: Table I lists it as needing "BCAM + FP
    unit" and "192 kB + raw" (`main.tex:602`), §III-E introduces it "as a
    ceiling", and §IV-D says "a \cam-resident design should therefore use the
    single-stage encodings" (`main.tex:638`).
15. **§III lead** (`401-402`, same edit): "arrays spanning emerging devices and
    nearer-term CMOS (or nonvolatile memories such as RRAM and MRAM)" → "arrays
    across the cell types of Sec.~\ref{subsec:CAMspace}". The original muddled
    its categories — RRAM and MRAM *are* emerging devices, so the parenthetical
    restated the first half, and §II-A calls CMOS "buildable in any CMOS process
    **today**", not "nearer-term". §II-A already gives the taxonomy; the lead now
    points there, which also revives a dead label.
16. **§III-A** (`417`): `Property~(1)` → `Requirement~(1)`. The list is
    introduced as requirements twice (`:404`, `:409`) and then called a property
    eight lines later.
17. **§III-D** (`466-468`): two symbol collisions and a mismatched lead-in.
    `$v$` was a scalar *level* at `:467` and one of the two *codes* at `:468`
    and in Eq. (3); `$\ell$` was already the layer index (`main.tex:319-320`,
    "after layer $\ell$ it is $h^{(\ell)}$"); and "For two codes $u,v$ over the
    same **dimension**" (singular) introduced a right-hand side summing over
    $i$. Now: `$s$` levels, `$q$` a level value, "For two quantized vectors
    $u,v$". **Symbols `$s$` and `$q$` were chosen as free elsewhere in the
    paper — override if you prefer others.** This edit did not touch the
    off-by-one described in §2.5.
18. **§III-F** (`501-505`) **and §IV-D** (`631`): `$k$` was carrying two
    meanings — the 31-nearest-neighbor vote size (`main.tex:494`) and the
    shortlist size, both live at once in the two-stage variant. Removed the
    symbol from the shortlist rather than adding a second subscript: "keeps the
    top $k$ rows" → "keeps the closest rows"; "With $k$ equal to the whole bank"
    → "With the shortlist equal to the whole bank"; "an absolute shortlist of
    $k=400$" → "of 400 rows". The generic "top-$k$ criterion" at `main.tex:640`
    is unchanged, since it reads as a category there.
19. **§III-E** (`492-493`): "each domain stores **a few thousand** encoded
    activations" → "several hundred to a few thousand". §IV-A gives the real
    range as 831 (definitional) to 3,201 (sycophancy) rows, so the low end was
    overstated about fourfold.
