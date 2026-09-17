# Hand-markup log, round 2 — DATE CAM Monitoring (No Comments 4.pdf)

Source PDF: `DATE CAM Monitoring — No Comments 4.pdf` (17 pages) — Mike's markup
on the **v05** output. Read with the `hand-markup` skill's band-crop
procedure. **Nothing has been applied to the .tex yet.** This log is for
hand-off to a different model to execute; the v05 `.tex` tree (split by
section: `01 - Introduction.tex` … `10 - Candidate Experiments.tex`) is in
the same folder, and each item below names the file and an anchor line so
the exact passage can be found by `grep`, not by page.

Legend:

- **[EDIT]** = Mike's own wording (blue ink). Apply verbatim,
  exact-string-replace with a uniqueness check.
- **[ASK]** = a request for content that doesn't exist yet (pink). Write the
  thing being asked for, in Mike's voice (run new prose through
  `fix-ai-writing` before it lands).
- **[CUT]** = remove text, usually while preserving the idea elsewhere.
- **[RESTRUCTURE]** = reorganize a section.
- **[FLAG]** = genuinely ambiguous, or Mike flagged himself as unsure. Needs
  his answer, a collaborator's answer, or an `\aians{}` note — not a guess.
- **[DATA-CHECK]** = not a writing task; verify something first.
- **[RESOLVED]** = Mike's note describes something that's already true in the
  v05 source; no action needed, included for context only.

Only pages 3, 4, 5, 6, and 7 of the PDF carry hand markup. Pages 1, 2, and
8–17 are clean.

---

## Page 3 — Table I / II. Background / II-B CAM technologies / II-C intro

**File: `02 - Background.tex`**

**1. [ASK]** Target: the "II. Background" section heading and Table I
(`02 - Background.tex`, lines 1–20 for the table, `\section{Background}` at
line 2). Oval note, arrow from Table I to the heading:
> "Somehow capture Measured FeFET CAM Behavior? cb Scholarly Reports.pdf or
> other?"

→ Work in a brief mention of *measured* FeFET CAM behavior (as opposed to
the modeled/literature figures Table I currently gives), sourced from a
document Mike calls "Scholarly Reports.pdf" or a similar source.
**[FLAG]: that source file isn't in hand — ask Mike to attach it, same as
`IV.pdf`/`Truthfulness.pdf` last round, before writing this.**

**2. [RESOLVED — no action]** Target (pink-highlighted, `02 -
Background.tex` line 206, "Associative-search silicon:" paragraph, and its
predecessor at line 53 "...an emerging-technology \cam can or cannot buy").
Margin note, keyed **(A)**:
> "I wanted text in Sec. II-C — labeled (A) — to be moved here/integrated
> here, and Sec II-C eliminated."

This describes exactly the state the source is already in: the
Associative-search-silicon paragraph lives at the end of subsection B (CAM
technologies), and the current Sec. II-C ("Preliminaries and related work,"
line 115) has no duplicate of it — confirmed by grep. **No action needed**;
included so the next pass doesn't second-guess it.

---

## Page 4 — II-B tail (Interpretability/ANN/Associative-search) / III / IV intro

**Files: `02 - Background.tex`, `04 - Detector Mapping.tex`**

**3. [CUT]** Target (`02 - Background.tex`, starts line 182): the entire
paragraph, already struck through in blue —
> "**Interpretability work that sets $K$:** The cross-domain grid in [12]
> anchors the deployed, per-behavior end of the $K$ axis; it is the result
> our measurements reproduce at CAM precision and extend (Sec. V). SAE
> dictionaries [16]–[18] and whole-vocabulary readout [15] are the sources
> of the large-$K$ estimates."

→ Delete this paragraph in full.

**4. (Same target as item 2 above — the "(A)" circled paragraph, no new note
on this page.)**

**5. [RESTRUCTURE] [ASK]** Target (`04 - Detector Mapping.tex`, line 14, the
"IV. Mapping the Detector into a CAM" intro). Circled **(B)**, struck
through in the source itself: "We started with a technology-enabled \cam
and then studied CMOS as a nearer-term solution – in part to better
quantify the impact of technology, i.e., what an emerging-technology cell
can or cannot buy (Sec. II-A)."

Note: *"Cut this; start off more generically — capture ways to map
activation signatures to CAM arrays."*

Right-margin note (attached via arrow into the paragraph, near "the
deployment target tightened to cells a current CMOS process offers"):
> "CAM Arrays. Spans emerging devices to nearer-term CMOS solutions that
> leverage different encoding schemes. (Notably, traditional CAM solutions
> can also be realized w/ NVMs — RRAM, MRAM, etc. — which could approach
> density gains, benefit from non-volatility with static datasets, etc.)"

Bottom-margin note: *"Update rest of shaded text based on (B). Keep
reference point sentiment as well."*

→ Rewrite the opening of the Sec. IV intro to be more generic: lead with
mapping activation signatures onto CAM arrays broadly (not "we started with
a technology-enabled CAM..."), and work in that CAM arrays span emerging
devices through to nearer-term CMOS solutions using different encoding
schemes — including, parenthetically, that traditional CAM designs can
also be realized with NVMs (RRAM, MRAM) for density/non-volatility gains
on static datasets. Then revise the rest of the highlighted paragraph
(lines 14–29ish) to read consistently with this new opening, while keeping
the "technology-enabled mapping retained as the reference point" sentiment
that's already in the paragraph (line 29) — that idea should survive the
rewrite.

---

## Page 5 — IV-A / IV-B / IV-C / IV-D / IV-E (start)

**File: `04 - Detector Mapping.tex`**

**6. [FLAG]** Target: property (3) at the end of "What 'CAM-resident'
requires" (line ~49–51: "...rather than a full sorted score vector, since
returning all $K$ scores is the readout job a \cam is not for.").

Note: *"Make 1 #."* (with an insertion mark right after "for.")

→ Unclear exactly what's meant — read as "add a footnote here" (turn part
of this into a footnote) but could also mean "make this one number/point."
**Confirm with Mike before acting**; don't guess at footnote content.

**7. [none — positive feedback only]** "Good ↑" next to "A. What
'CAM-resident' requires" heading (line 41). No action.

**8. [ASK] [RESTRUCTURE]** Target: the first two sentences of "B. The first
mapping" (line ~68, struck through): *"The strategy: reduce each raw
activation from $d$ dimensions to a much smaller $d'$ with a front end
cheap enough to run on every token (requirement (1)), quantize query and
stored rows alike to a few bits per dimension, and let the array's
matchline carry the distance."*

Left-margin note: *"Reframe intro as to what CAN be done w/ FeFET CAMs, and
could allow for richer representation of data or fewer memory cells, etc.
However, do need to implement [the] down-projection mechanism [regardless]."*

→ Rewrite this section's opening to lead with what FeFET CAMs make
possible — richer representation of data, or fewer memory cells — rather
than starting with "the strategy: reduce dimensions." Keep in mind (and
say) that a down-projection mechanism still has to be implemented either
way; this reframe changes the motivation, not the mechanism.

**9. [CUT] [ASK]** Target: "C. The path back to a multi-bit cell" (line
105) and both of its paragraphs (fully pink-highlighted, through "...the
whole detector fits in a plain CMOS array today.").

Note: *"This makes no sense — we don't talk about abandoning it in Sec.
B! Also, I think we can cut [the] highlighted text."*

Right-margin note attached to the same section: *"Just transition. Also
say we also look @ Hamming-distance solutions, as those are near-term and
realizable by a host of NVMs."*

→ Two things: (a) the opening line "Moving to frozen projections and a
Hamming metric is not an abandonment of the Euclidean track..." doesn't
work because Sec. IV-B (the first mapping) never frames anything as being
abandoned — fix or cut that framing. (b) Mike thinks the section's
highlighted content can likely be cut down to a short transition; if kept
at all, it should say that Hamming-distance-based solutions are also
being looked at because they're near-term and realizable across a range of
NVMs (ties to item 5's NVM point — keep these consistent). **This reads as
"cut most of Sec. IV-C to one transition sentence," but confirm the scope
with Mike since he phrased it as "I think," not a flat instruction.**

**10. [CUT]** Target (line 135, start of "D. Encoding 1: sign random
projection, ternary"): *"...draw a random matrix $P \in \mathbb{R}^{m\times
d}$ once, fix it, and never touch it again."*

Note: *"too AI-like — simplify."*

→ Rewrite this sentence plainly; it reads as AI-drafted filler. Route
through `fix-ai-writing` when redrafting.

**11. [CUT]** Target: *"This is the standard sign-random-projection
(SimHash) construction [30]: the probability that two vectors fall on
opposite sides of a random hyperplane is the angle between them divided by
180°, so counting differing bits estimates the angle."* (pink oval)

Note (right margin): *"CAM simplify."*

→ Shorten/simplify this explanation.

**12. [CUT]** Target: *"The contribution here is not the construction but
running it on LLM activations and sizing the resulting array."* (struck
through in the source's own render — appears as strikethrough already)

→ Delete this sentence.

**13. [EDIT]** Target: *"Two properties matter for hardware: the projection
is never trained, and the comparison is an XOR plus a population count..."*

Blue strike over **"Two properties matter for hardware: the projection is
never trained, and"**, replaced above with **"From a hardware
perspective,"**.

→ "**From a hardware perspective,** the comparison is an XOR plus a
population count, which a plain CAM array computes natively."

**14. [ASK]** Target: *"A code wider than a practical array row is split
across subarrays and the mismatch counts summed, which is standard practice
and a real design parameter."*

Note (right margin, arrow in): *"Cite Scientific Reports .pdf paper."*

→ Add a citation to a paper Mike calls "Scientific Reports .pdf" near this
claim. **[FLAG]: need the actual reference/file from Mike — don't invent a
citation.**

**15. [CUT — low priority]** Right-margin note near the Encoding 1/Encoding
2 boundary: *"Probably not needed; can simplify."* Same general
simplify-this-section instruction as items 10–13 — no new distinct target,
just reinforcing the section should be trimmed.

**16. [RESTRUCTURE]** Target: "D. Encoding 1: sign random projection,
ternary" heading (line 135). Small insertion **"(or via other NVMs)"**
near the heading, with note: *"Then, pick up here, updating section titles
as needed."*

→ Once the Sec. IV-C rewrite (item 9) and the NVM framing (items 5, 9) are
in place, revisit the Encoding 1/2/3 section titles/openings so they read
consistently with "or via other NVMs" as an option, not just sign-RP/
thermometer specifically.

---

## Page 6 — IV-E (thermometer) / IV-F (decision rule) / IV-G (Encoding 3) / V intro / V-A

**Files: `04 - Detector Mapping.tex`, `05 - Results.tex`**

**17. [ASK]** Target (`04 - Detector Mapping.tex`, "E. Encoding 2:
thermometer coding," two arrows into the paragraph: one at "The identity is
exact, not approximate, which is what makes the encoding useful here," the
other at "a cell that can only report disagreement now supports a
magnitude-sensitive metric").

Note: *"Parse/cite DAC-thermosensitiv[e].pdf here and mention plausible
extensions. Also look at 1FeFET-1C.pdf and consider [a similar]
extension."*

→ Add citations to two documents Mike has — "DAC-thermosensitive.pdf" and
"1FeFET-1C.pdf" — near the thermometer-coding identity claim, and mention
plausible extensions each source suggests. **[FLAG]: need both files from
Mike before writing this — don't guess at their content.**

**18. [FLAG]** Target: "F. The decision rule" (whole boxed section, line
189).

Left-margin note: *"Flag this. Need to clarify with Ismail. Do we store
more vectors than just 1 with CAM? What is going on here? This is not
clear!"*

→ Genuine open question — same thread as prior round's "not sure I follow
this / few-shot analogy" flag (already partly addressed: the section now
reads "the bank operates $N$-way, many-shot..."). Mike wants this
confirmed with **Ismail** specifically before anything more is written
here. **Don't resolve this by writing more prose — it needs a person's
answer.**

**19. [EDIT] [FLAG on exact scope]** Target (`05 - Results.tex`, lines
10–11): *"This section evaluates the mappings of Sec.~IV on the first of
the paper's two workloads: deception detection, where the library is
set..."*

Marks: "This section" struck; "evaluates" has an X through it; "on the
first of the paper's two workloads:" struck; caret-insert **"a"** before
"deception detection"; caret-insert **"workload"** after "detection,".

→ Best reconstruction: *"...the mappings of Sec. IV on **a** deception
detection **workload**, where the library is set by..."* — but the strikes
over "This section" and "evaluates" leave the sentence without a clear
subject/verb if applied literally. **[FLAG]: apply the clear inserts ("a"
/ "workload") and the clear cut ("on the first of the paper's two
workloads:"), but double-check the "This section"/"evaluates" strikes
against the original scan before committing — if applying them literally
breaks the sentence, flag it back with `\aians{}` rather than
silently rewriting around it,** per the skill's rule on awkward blue edits.

*(Also on this page, just above the heading: "We 1st" in blue — this reads
as Mike orienting himself ["we're first," i.e. this is Workload 1], not an
editing instruction. No action.)*

**20. [CUT]** Target (`05 - Results.tex`, line 20 area): the full paragraph
—
> "...the library is set by the vocabulary. One may reasonably ask why we
> evaluate at small $K$ when the case for hardware sharpens at large $K$:
> the $K$ values on this rung of Fig. 1 are where established results exist
> to reproduce and where a GPU baseline can be compared against directly –
> and, per Sec. III, at $K\approx10^3$ an edge-class part is already
> approaching the practical limits of said baseline."

Struck through in blue in full.

→ Delete this paragraph. (Note: this is the paragraph added per the prior
round's item #29 "pre-emptive small-K" ask — Mike now wants it cut
entirely rather than kept.)

**21. [FLAG — needs a conversation, not a writing task]** Right-margin pink
box, attached near the same paragraph:
> "? Can we make [the] argument that Truthfulness is somehow connected to
> VLA? Brainstorm this with me. Or go back to [the] argument that this is
> just an established dataset? Maybe this is not that important?"

→ Open-ended question Mike is explicitly unsure about ("maybe this is not
that important?"). **Do not resolve this in the .tex — flag it back for a
conversation with Mike rather than picking one framing.**

**22. [FLAG — needs a conversation, not a writing task]** Target (`05 -
Results.tex`, line 104): *"Fig.~\ref{fig:grids}(d)--(f) shows the
ten-domain cross-domain grids for the two single-stage encodings and for
the exact-rerank ceiling; Table~II summarizes them..."*

Note: *"I'm to cut Fig. 2a–2c, but per [an earlier] chat, [we] looked at it
in more detail than Truthfulness repeated. Do we need to repeat/discuss
both? Let's game this out."*

→ Follow-up to last round's flagged item about Fig. 2(a)–(c) vs.
"Truthfulness.pdf." Mike is now weighing whether to actually cut the
top-row four-domain panels (a)–(c) or keep discussing both rows. **This is
a planning question for Mike, not something to decide unilaterally in the
.tex.**

**23. [ASK]**, keyed **(E)**. Right-margin note near the same paragraph:
> "We also need to explain how to read/interpret grid charts in Fig. 2 in
> the text — i.e., training on behavior X is tested on behavior Y."

→ Add a sentence in the main text (not just the figure caption) explaining
how to read Fig. 2's grids: rows = domain the bank was trained/stored on,
columns = domain the held-out test activations come from. (Page 7's note
#25 says the "Cross-domain fidelity..." paragraph already partly covers
this — see below — so check for redundancy before adding more.)

---

## Page 7 — Fig. 2 / "In-domain fidelity" / "Cross-domain fidelity"

**File: `05 - Results.tex`**

**24. [ASK]** Target (line 140, boxed): *"**In-domain fidelity is
essentially unaffected by the encoding:** The diagonal means are 0.920
(sign-RP ternary, 384 b), 0.919 (thermometer, 384 b) and 0.928 (exact
rerank)..."*

Note: *"Write in plain English! — use my voice skill."*

→ Rewrite this paragraph in plain English via the `fix-ai-writing` /
voice skill — same content, plainer delivery.

**25. [RESOLVED — mostly; cross-reference to item 23]** Target (line 149):
*"**Cross-domain fidelity is where compression shows, and it separates the
two encodings:** An off-diagonal cell scores a bank built from one domain
against test examples from another, so it measures how well a stored
library transfers to material it was not built from..."*

Left-margin note: *"Some of this covers the points that I made at (E)."*

→ Mike is noting this paragraph already explains the row/column reading
convention in prose (matches item 23's ask). When executing item 23, check
this paragraph first — the "explain how to read the grids" ask may already
be satisfied here, or need only a small addition rather than new text.

---

## Summary for the next pass

- **Clean [EDIT]s** (blue, apply verbatim, watch for the one flagged
  scope issue): #3 (delete paragraph), #13 (from a hardware perspective),
  #19 (flag exact scope before applying), #20 (delete paragraph).
- **[RESOLVED], no action**: #2 (the (A)/Sec. II-C note — already true in
  the source).
- **Needs a file from Mike before writing**: #1 ("Scholarly Reports.pdf"),
  #14 ("Scientific Reports .pdf"), #17 ("DAC-thermosensitive.pdf" and
  "1FeFET-1C.pdf"). Don't guess at citations or content from these.
- **Needs a person's answer, not a rewrite**: #6 ("Make 1 #."), #18 (ask
  Ismail about multi-vector storage), #21 (Truthfulness↔VLA — brainstorm
  with Mike), #22 (whether to cut Fig. 2a–2c).
- **One coherent restructuring thread**: #5, #8, #9, #16 all reframe Sec.
  IV around "what CAM arrays can do, spanning emerging devices to
  near-term CMOS/NVM solutions" — do these together, in order, so the
  section reads as one consistent argument rather than four patches.
- **Simplification thread** (items 10–15): Encoding 1's exposition reads
  as over-explained/AI-like across several consecutive marks — treat as
  one trim pass over that subsection rather than five separate edits.
- Items 23 and 25 are the same ask from two angles — resolve together, and
  check #25's paragraph before adding new text for #23.
