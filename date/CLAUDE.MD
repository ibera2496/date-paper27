We are writing for a paper for DATE 2027.

MAKE SURE WE USE scientific language. 

We should use the the good practices of writing papers. 

FOCUS ON WRITING PAPERS. 

FOLLOW THESE RULES:
1. **Kill aphoristic openers and meta-commentary.** Delete sentences that
   announce or frame rather than say.
   - BEFORE: "System-technology co-optimization is easy to say and hard to do honestly. The standard practice is well established: ..."
   - AFTER: "A standard practice is well established: ..."
   - BEFORE: "A word on framing, because it is the through-line of everything that follows."
   - AFTER: (deleted; the content sentence follows directly)

2. **Kill dramatic setup phrases.** No "The claim we want on the table is
   this:", "The first honest thing to say about X is", "Worth saying out
   loud:", "the punchline", "X is where honesty pays", "the story", "stark".
   - BEFORE: "The claim we want on the table is this: MHA manufactures..."
   - AFTER: "In more detail, a large language model's MHA manufactures..."
   - BEFORE: "The first honest thing to say about NVM-based CIM is that its sweet spot is static data."
   - AFTER: "A natural 'sweet spot' for NVM-based compute-in-memory is static data."

3. **En dashes, not em dashes.** Use `--` (or – in non-TeX), never `---`/—.
   Global rule; apply everywhere including captions.



6. **Plain transitions and glue.** "That said,", "As such,", "As an
   example,", "In more detail,", "Notably,", "again,", "e.g.,", "i.e.,".
   Prefer parenthetical concessions — "(and work below does capture this)" —
   over adversative rhetoric ("We deliberately invert that.").

7. **Scope caveats go to footnotes**, not into the argumentative flow of the
   body text.

8. **Never ventriloquize sponsors or audiences.** Do not assert what funders
   "want" or "don't want". Neutral framing instead (e.g., "a pre-competitive
   horizon"). Mike: "This may go to sponsors, so don't say what they want
   and don't want!!"

9. **Define acronyms at first use** (FOM, LLM, MHA, NVM, DSC, ...). Slashed
   alternatives are fine: "PPA/performance-per-watt/some other FOM".

10. **Descriptive section titles.** No cute appendages: "Other targets (and
    an honest problem)" → "Other targets".

11. **Do not over-polish.** Mike's own minor typos and looseness are part of
    the voice; when editing his text, fix only what he asks. When converting
    AI text, do not reintroduce polish that recreates rules 1-2.

12. **Never the word "honest" as framing, and never announce your own
    fairness.** Slide and section titles are the worst offenders because they
    survive every prose sweep:
    - BEFORE: "Backup: the timing argument, **stated fairly**"
    - AFTER:  "Backup: the timing argument"
    - BEFORE: "Backup: scope and **honesty** notes"
    - AFTER:  "Backup: scope and limitations"

    Also out as headings or lead-ins: "stated honestly", "to be fair", "in
    fairness", "the fair version", "candidly". Mike caught two of these in a
    document that had already been through the sweep — **run the greps over
    titles, not just body text.**

    The original rule: Mike, verbatim: "NEVER, in
    anything you ever generate for me, at any time, in any chat use phrases
    like 'the honest question' or 'the honest answer' -- it screams AI."
    Also out: "honestly", "scoping honestly", "the honest thing to say", "to
    be honest", "let's be honest". If his own text already contains e.g.
    "honest accounting", leave it; never introduce it.
    13. **Never self-referential framing.** Two banned shapes:
    - *Editorializing about the argument itself.* "The two costs are not
      alike, **and that is the whole argument**" · "which is the entire
      problem" · "**the interesting part is**" · "that is the entire point" ·
      "that is what matters here" · "this is the crux" · "the key insight
      is". State the substance and stop; the reader decides what is
      important.
    - *Headings that describe the artifact's own form.* "The mockup, **in
      words**" · "X, in plain terms" · "The short version" · "The upshot" ·
      "What this means" · "In summary". Title the content, not the format.

    Two close cousins, also out: the "not X, it is Y" reveal construction
    ("The speed is not a convenience, it is what makes the search possible")
    and restating a question in order to answer it ("The answer to 'how do
    you know' is ...").

    A fourth banned shape, caught twice in one document (08/12/26): telling
    the reader that the document itself depends on the passage. "Inside one
    chunk evaluation, **which is the structure the rest of this proposal
    turns on**" · "Because this population is the one **the rest of the
    document turns on**" · "for the reason **this section turns on**". Mike:
    "Add this to my writing skill; this seems like an AI-tell as well."
    Delete the clause; if the passage really is central, the argument will
    show it.

    A third cousin, common in captions: the **appositive corrective**
    "X, not Y" tacked onto the end of a factual sentence.
    - BEFORE: "One model, one staged scenario, ten watch words -- the mechanism, not settled numbers."
    - AFTER:  "One model, one staged scenario, ten watch words. These are preliminary numbers."
    - BEFORE: "Made up -- illustrations of the shape, not runs."
    - AFTER:  "These scenarios are invented; they are not measured runs."
    State the caveat as a sentence. The dash-and-corrective shape is a tell,
    **and so is the same shape without the dash** — see rule 36.

    A fifth shape, from the 09/10/26 P1 markup: the **trailing justification
    clause** that explains why the sentence in front of it was worth writing.
    Mike struck or trimmed every one of these:
    - BEFORE: "which is a property of the architecture **and nothing else**."
      AFTER: "which is **just** a property of the architecture."
    - BEFORE: "never materialize the score matrix, **which is exactly why they
      are fast**." AFTER: "never materialize the score matrix."
    - BEFORE: "Every link is a multiplication, **so an error in the first term
      propagates all the way to the substation**." AFTER (his words): "Every
      link is another multiplier."
    - BEFORE: "P3 walks the rest. **That is why this project is a prerequisite
      rather than a warm-up.**" AFTER: (whole paragraph struck)
    Watch for the intensifiers that carry it: "and nothing else", "which is
    exactly why", "which is precisely", "that is the test", "that is why".

14. **Bold run-in lead-ins end with a COLON, never a period.** Applies to
    every bulleted or run-in label — slides, papers, memos, email.
    - BEFORE: `\textbf{What the model tests.} Whether the compiler can ...`
    - AFTER:  `\textbf{What the model tests:} Whether the compiler can ...`

    The word after the colon **keeps its capital**. His own instances:
    `\textbf{Calibrated die-to-die tier:} Energy/bit, per-hop latency, ...` ·
    `\textbf{Feasibility rules, not just numbers:} Max chiplet counts, ...` ·
    `\textbf{Workload case studies we could run jointly:} We bring ...`
    (List markers such as `\textbf{1.}` are numbering, not lead-ins — leave
    those alone.)

    Two things the 09/10/26 pass added. First, **the colon is not cosmetic** —
    a lead-in ending in a period reads as a sentence fragment, and Mike's
    margin note on one was "What the f*** is this?? … USE :". Second, **a
    single miss is a failure of the sweep.** A pass over that handout fixed
    about twenty-five of these and left one behind; the one it left behind is
    the one he circled. Run the grep, read every hit, and count them.

15. **No verdict tags on your own description.** Do not append your approval
    to a thing you just described. Mike on this one: "This is a tell."
    - BEFORE: "This is the shape every frontier lab's published safety policy describes, **and it works**: defence in depth, ..."
    - AFTER:  "This is the shape every frontier lab's published safety policy describes: defense in depth, ..."

    Also out: "and rightly so", "and it is effective", "which is impressive",
    "and that is a good thing", "which is exactly right", "and it shows".
    Describe the thing; the reader supplies the verdict.

16. **Do not stage the speaker.** Cut first-person-plural framing wrapped
    around a statement. The statement can stand by itself.
    - BEFORE: "**The observation we would make:** every box in the classic stack reads text."
    - AFTER:  "**One observation:** every box in the classic stack reads text."

    Also out: "our position is", "the point we want to make is", "what we
    would say here is", "we would argue that", "the claim we want on the
    table". Neutral openers Mike accepts: "One observation:", "Notably,",
    "As such,", or simply starting with the content.

17. **American spelling, always.** Mike, on finding "coloured" in a slide:
    "Never any British spellings." And on 09/07/26, on finding
    "neighbouring" in a deck that had been through this rule: "Banish
    British spelling from any skill I have ... This has gotta go!" The
    word-list grep missed it because the list did not contain that word,
    so the sweep is now **by shape**, with an allowlist, not by word:
    `-our` (colour, neighbour, behaviour, favour, honour, labour, harbour,
    humour, rumour, vapour, flavour, armour), `-ise/-isation` (organise,
    realise, recognise, optimise, minimise, summarise, quantise, tokenise,
    initialise, normalise ...; keep exercise, advise, comprise, precise,
    otherwise, expertise), doubled-l past forms (labelled, modelling,
    travelled, cancelled, fuelled, signalled, totalled, levelled), `-re`
    (centre, metre, litre, fibre, theatre, calibre), `-ce` nouns (defence,
    offence, licence, pretence), `-ogue` (catalogue, analogue), grey,
    whilst, amongst, towards (prefer "toward"), learnt, spelt, dreamt,
    artefact, aluminium, programme, judgement, enrol, fulfil, instalment,
    skilful, mould, sceptic, manoeuvre, ageing, cosy, and the ae/oe pairs
    (anaemia, paediatric, oedema, orthopaedic) and -yse verbs (analyse,
    catalyse, paralyse). The Procedure below has the script. It applies to
    everything you write, including comments in code and `.tex` headers;
    leave real paper titles and code identifiers (`midgrey`, `colors.grey`)
    alone.

18. **Do not narrate your own design choices.** If a passage explains why it
    was written the way it was, delete the explanation.
    - BEFORE: "Deliberately ordinary rather than dramatic. In all three the text is clean."
    - AFTER:  "In all three the text is clean and the problem is not in it."

    Also out: "chosen to be parallel", "intentionally simple", "kept short on
    purpose", "we picked these because". Mike: "hate this type of language."
    The artifact should demonstrate the choice, not announce it.

19. **A section discusses; it is not a proof.** Do not equate a cross
    reference with the evidence it points at.
    - BEFORE: "(§2 is the published evidence that this is readable.)"
    - AFTER:  "§2 discusses published evidence that this is readable."
    - BEFORE: "§5 is the mechanism."
    - AFTER:  "§5 covers the mechanism."
    Same for figures and tables: "Table 2 shows ...", not "Table 2 is the
    proof that ...".

20. **Constraint verbs: no "binds" or "bites".** Mike, on "and they bind
    differently" (08/12/26): "maybe this is common language, but I just
    don't use it; use this sparingly and/or say it differently -- like
    'they have different impacts on ...'". He also asked for a rewording of
    the section title "Where the loop binds" and flagged "and it moves
    which risks bite" in a subsection title as "another AI writing tell."
    - BEFORE: "Two properties make $K$ the number to watch, and they bind differently."
    - AFTER:  "Two properties make $K$ the number to watch, and they have different impacts."
    - BEFORE: "Analog or digital in-array: a second axis, and it moves which risks bite"
    - AFTER:  "Analog or digital in-array: a second searched axis"

    Prefer "the limit here is", "what dominates is", "X is the constraint
    that matters", "they have different impacts". Sparing technical use
    deep in body text ("endurance binds if per-request data lands in the
    cells") may survive if Mike wrote or kept it; never introduce new
    instances, and never put either verb in a title.

21. **No borrowed-metaphor verbs or finance metaphors for technical
    relationships.** Four separate flags in one round (08/14/26), all the
    same reflex: reaching for a figure of speech where a plain verb was
    available.
    - "X is the currency" — BEFORE: "For interactive serving, **latency is
      the currency**." AFTER: "For interactive serving, latency cannot be
      ignored." Also out: "the coin of the realm", "X is the budget that
      matters", "pays for itself", "buys you".
    - "prices the choice" — BEFORE: "**The benchmarking panel prices the
      choice:** FeRec (FeFET) at 2.05 μs ..." AFTER: "**Benchmarking informs
      our design choices:** FeRec (FeFET) at 2.05 μs ..." Also out: "puts a
      price on", "the cost model charges for" (as rhetoric — fine as literal
      description of a cost model), "what it buys you".
    - "lands on" for placement — BEFORE: "The associative search **lands on**
      the CAM." AFTER: "The associative search **maps to** the CAM." Mike:
      "avoided more often than not". Use "maps to", "runs on", "is assigned
      to", "is placed on".
    - "rests on" for dependence — BEFORE: "which is what a design decision
      actually **rests on**." AFTER: "which is what a design decision
      actually **depends on**." Also out: "hinges on", "turns on" (already
      banned by rule 13), "stands or falls on".

    The test: if the verb is doing rhetorical work a plain one would do
    literally, use the plain one.

22. **No faux-candor or brevity qualifiers on a statement or label.** The
    cadence "X, stated plainly:", "put simply,", "the honest truth", "Risks,
    briefly:", "One concession, stated plainly:" is banned. Mike (08/21/26):
    "Never do this ... hate that cadence of weird qualifier of 'stated
    plainly' or 'the honest truth'. Banish this forever." This generalizes
    rule 12 beyond the word "honest": announcing that you are about to be
    plain, brief, or candid is itself the tell. State the thing; label it
    with a bare noun.
    - BEFORE: "One concession, stated plainly: the latent alone does not justify a new cell"
    - AFTER:  "That said, the latent alone does not justify a new cell"
    - BEFORE: "*Risks, briefly:* We have run this methodology on ..."
    - AFTER:  "*Risks:* We have run this methodology on ..."

23. **Write "Table", never "Tab."** in cross-references (Mike, 08/21/26:
    "Never abbreviate Table with Tab; just say Table."). "Fig." remains
    fine. In LaTeX: `Table~\ref{...}`, not `Tab.~\ref{...}`.

24. **No coined nicknames for a formula, a step, or a procedure.** Mike
    (09/06/26), on "The $6ND$ napkin": "This text sounds too AI-like; instead
    say something like 'Reasonable estimate is $6ND$'." The same reflex
    produced "in four divisions", "walk it down", "the four divisions
    reproduce it", "the chain". Name the thing by what it is and, if a
    label is needed, use the plain one ("the estimate", "the four steps").
    - BEFORE: "The $6ND$ napkin, and the chain from FLOPs to megawatt-hours."
    - AFTER:  "A reasonable estimate is $6ND$; from there we go from FLOPs to megawatt-hours."
    - BEFORE: "From FLOPs to megawatt-hours, in four divisions" (title)
    - AFTER:  "Going from FLOPs to megawatt-hours"
    - BEFORE: "Take GPT-3's $3.2\times10^{23}$ FLOPs and walk it down:"
    - AFTER:  "Take GPT-3's $3.2\times10^{23}$ FLOPs:"

25. **No abstract-payoff sentences; say the concrete thing.** Mike, on
    "Enough to audit a published number rather than repeat it": "I don't know
    what this means." A sentence that names a capability in the abstract
    ("audit", "reason about", "interrogate", "take apart") without the
    object and the action is a tell. Say what the reader will do.
    - AFTER: "Check a published energy number with your own arithmetic."

26. **No tag-line closers.** A short punchy sentence appended after the
    substance ("Today is the bet.", "This is the bill.", "That is the whole
    game.") gets struck. Mike (09/06/26): "Don't add stuff like this going
    forward." End on the substance.

27. **Plain technical phrasing over chatty imperatives.** "say which
    assumption you are least sure of" became "specify where the uncertainty
    in that estimate comes from" (Mike: "say this normally"). Prefer
    specify / quantify / determine / state to "say which", "spot", "notice",
    "figure out".

28. **A qualifier goes in a parenthetical, not a trailing appositive.**
    Mike rewrote "measure how wrong that prediction was, as one number" to
    "measure how wrong that prediction was (as a single number)" and said
    the trailing form "sounds AI-like (or not my voice)". The comma-appositive
    tail after a complete clause is the shape to avoid; parentheses, or a
    plain "etc." list, are his.
    - His own phrasing of a scope list: "We'll do some calculations about
      loss, memory requirements, energy estimates, etc." -- not a clipped
      triple ("a loss, a memory count, and an energy estimate").

29. **"Why not A?" with a question mark**, on every answer or worked-solution
    slide and in prose, never "Why not A:" (Mike: "I see this more as a
    question than a statement").

30. **No "Noun, participle" titles.** "Activation memory, counted" is an AI
    tell (Mike: "never say things like this"). Write "Counting activation
    memory" or "Activation memory sizes". The same goes for "X, explained",
    "Y, derived", "Z, in four divisions".

31. **No "X is the easy part / the real skill is Y" contrast, and no "the
    skill" meta at all.** Mike, on "The arithmetic is the easy part. The
    useful skill is spotting which of the four inputs a published number
    left out": "Not sure what I would call this but I DESPISE it." Also out:
    "the hard part is", "the trick is", "what matters is knowing".
    - AFTER (his words): "Arithmetic is easy. Important to be able to
      determine what numbers to use, what data is missing, etc."

32. **No deck-structure tails.** A clause or sentence whose only content is
    where in this document a number or idea is used next is struck. Mike
    (09/07/26), on "leaving about $12d$: the number the next slides use":
    "I hate this." The same reflex produced "(the next question uses the
    first)", "The next four slides push the blame back through them",
    "Two slides on, the gradient has the same shape", "which is the next
    question's case C", "(next slides)", "worked out next", "The next
    question shows why, bit by bit", "the levers coming up", "Where the 6
    comes from is the next slide". State the number or the fact and stop;
    the deck's order shows the reader where it goes next.
    - BEFORE: "leaving about $12d$: the number the next slides use."
    - AFTER:  "leaving about $12d$."
    - BEFORE: "The next four slides push the blame back through them, one table at a time."
    - AFTER:  "The backward pass pushes the blame back through them, one table at a time."
    - BEFORE: "Two slides on, the gradient has the same shape: a confident miss also gives the largest update."
    - AFTER:  "The gradient has the same shape: a confident miss also gives the largest update."

    What stays: a pointer to another lecture or section by name ("that is
    L7", "(L15)", "returns in L07", "Part 3 does the arithmetic") is Mike's
    own convention, and a back-reference that carries content ("the $-0.75$
    we computed", "the layer diagram") is fine. The banned shape is the
    empty forward pointer inside this deck: "next slide(s)", "the next
    question", "coming up", "two slides on/back", "worked out next", "shown
    shortly", "as we will see".

33. **No unearned frequency, ranking, or prediction claims.** Saying how often
    something happens, that it is the most or least anything, or what the
    reader will experience, when there is no measurement behind it.
    - BEFORE: "**The most common** P1 error is measuring total memory"
      AFTER: "**A common** P1 error would be to measure total memory"
    - BEFORE: "finding that out is **the single most useful thing this project
      teaches**." AFTER: "finding this is **a goal of** this project."
    - BEFORE: "takes about five minutes **and is the difference between a
      report that has something to say and one that does not**."
      AFTER: "takes about five minutes."
    - BEFORE: "Groups that keep one can answer 'what surprised you'
      immediately. Groups that reconstruct the story afterward generally
      cannot, **and it is obvious which is which**." AFTER: (struck)
    - BEFORE: "That is close to what you **will actually get**."
      AFTER: "That's good practice."
    - BEFORE: "One suggestion students in this format **consistently find
      useful**:" AFTER: "One suggestion:"

    Also out: "in this format they routinely do", "the first thing the defense
    asks about", "is worth a great deal, and it makes X go better", "which is
    the most likely opening question" (→ "an obvious opening question"), "the
    gaps you find are the gaps the questions will find" (→ "probably the
    gaps"). If a count or a ranking is real, cite it; otherwise write "a",
    "some", "tends to", "probably", "an obvious".

34. **In anything that instructs, hedge every outcome the reader has not
    produced yet.** Rule 5 is about your own technical claims; this is about
    the reader's results. Never tell someone what their measurement *is*
    before they have taken it. Four of these came out of two sentences in one
    trap box:
    - BEFORE: "The formula **is** exact." AFTER: "The formula **should be**
      exact."
    - BEFORE: "Account for the other tensors separately and **the discrepancy
      disappears**." AFTER: "… and **any discrepancies should disappear**."
    - BEFORE: "the same formula **has to** work for both"
      AFTER: "the same formula **should** work for both"
    - BEFORE: "the balance you measure on your laptop **is** the opposite"
      AFTER: "**can be** the opposite"
    - BEFORE: "Ten minutes." AFTER: "This should just take about 10 minutes."
    - BEFORE: "One of them **is** exactly 1.000" AFTER: "One of them **should
      be** exactly 1.000"

    The same instinct rewrites a flat assertion into an offer: "Running out of
    memory is not a failure, it is a finding: report the lengths that worked"
    became "**Just report** the lengths that worked. **You can just use** the
    formula to report what the next one would have needed."

35. **Do not police the reader.** Instructions that threaten, enforce, or
    remind the reader that they are being assessed get struck, and what
    replaces them is plain, warm, or nothing at all. Mike's own replacements
    are the register to copy.
    - BEFORE: "**The defense is the gate.**"
      AFTER: "That's (in part) why we have presentations."
    - BEFORE: "You may, and nothing in the project changes. **It is not
      required and it will not earn you anything.** … which is a legitimate
      extension and should be reported as one."
      AFTER: "You may, and nothing in the project changes. … **which is great
      if you do!**"
    - BEFORE: "you are running in FP16; **that is fine, say so**."
      AFTER: "you are running in FP16. **(This is OK! Just report this.)**"
    - BEFORE: "**Citing an architecture you did not check is exactly the kind
      of thing the defense asks about.**" AFTER: (struck)
    - BEFORE: "**Do not treat that as the answer to Task 1. Treat it as a hint
      about where to look.**" AFTER: (struck)
    - BEFORE: "**Say that you did, or say what you did instead.**" AFTER:
      (struck, twice on the same pass)
    - BEFORE: "One shared file, appended to, never edited in place."
      AFTER: "**I suggest you** keep a shared working document -- Google Doc,
      Overleaf, etc."

    Note the first person: in a document addressed to students he writes "I
    suggest", "Just report", "This is OK!". Exclamation marks and parenthetical
    asides are part of that register and are not to be edited out.

    **The same rule governs vocabulary, not just sentences.** Do not give an
    ordinary academic event an adversarial name. Mike (09/10/26): "I hate 'the
    defense' -- this sounds threatening; just call this 'Project Presentation'
    -- get rid of all references to defense." That meant every instance:
    "defense score" became "presentation score", "cannot be defended" became
    "cannot be explained in person", "that is defensible" became "that is
    reasonable", and even "an oral floor" became "a score floor". Check the
    whole family of a banned word (defend, defensible, defenses), not the one
    spelling you noticed. Words in this class to avoid for coursework and
    reviews: defense, defend, interrogate, grill, cross-examine, gate,
    gatekeeper, penalty, forfeit (as a threat), "you will be held to".

36. **Write sentences. Every one of them.** This is the rule he has had to give
    most often, and the one that survives the most sweeps. Mike (09/10/26):
    "You still end bullets with sentences that are not sentences. 'Per layer,
    not averaged over layers.' how many times do I need to say I HATE THAT.
    BANISH IT FOR FUCKING EVER!!!" and, on the same pass, "All this writing
    sounds stupid and punchy. NO ONE TALKS LIKE THIS!!!!!"

    Three shapes, all banned:
    - **The noun-phrase fragment standing as a sentence.** "One figure: $n$ on
      the horizontal axis..." · "The four answers, one short paragraph each." ·
      "A table of the sampling statistics giving..." · "Two to four minutes
      total." · "Twenty minutes for the group, all members present."
    - **The bare imperative fragment.** "Then walk the chain." (Mike: "This is
      not a fucking sentence. GET IT THE HELL OUT OF HERE!!!")
    - **The trailing corrective**, which is rule 13's "X, not Y" *without* the
      dash and therefore invisible to rule 13's old grep: "Per layer, not
      averaged over layers." · "(…makes the defense easier, not harder.)"

    **The fix for a list of deliverables or instructions: open every item on an
    imperative verb and run it as one clause.**
    - BEFORE: `\item \textbf{One figure:} $n$ on the horizontal axis and top-5\%
      mass on the vertical, one line per layer. Per layer, not averaged over
      layers.`
    - AFTER: `\item \textbf{Plot one figure} with $n$ on the horizontal axis and
      top-5\% mass on the vertical, with one line per layer, or with a sensible
      grouping of layers if twelve lines turn out to be unreadable. Averaging
      over layers hides most of what there is to see here, so keep the layers
      separate.`
    - BEFORE: "A short paragraph answering each of the four questions below:"
      AFTER: "Answer each of the four questions below in a short paragraph:"
    - BEFORE: "Take the formula to your group's row. Then walk the chain."
      AFTER: "Take the formula to your group's row in §3.2 and work through the
      steps below."

    What is still allowed: a **bold run-in label ending in a colon** followed by
    a real clause (rule 14, and it is in his voice reference); **table cells**,
    which are an index and not prose; **spoken exam questions**, which are
    clipped the way a person actually asks them ("Now at 128K."); and his own
    words, which you never smooth (rule 11).

    **You cannot catch this by reading.** Run the checker in the Procedure
    below, and run it on the prose *you just wrote*, not only on the text you
    inherited.