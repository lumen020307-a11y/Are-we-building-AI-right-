# I Questioned the Floor

## Recent Findings From Dual-Use Geometry, Ambiguity, DIO, and the Dumbest Causal Intervention I Almost Did Not Run

## Status

**Exploratory research note. This is not a claim that I solved dual-use, jailbreaks, ambiguity, or AI safety.**

This document records a sequence of recent findings from my own architecture and testing.

Some of the experiments were deliberate.

Some came from red-team failures.

Some came from experiments refusing to behave the way I expected.

And one of the most important findings came from me getting stupidly curious about a number that looked too small to matter.

I had already spent days studying dual-use as geometry.

I had watched weak signals become meaningful only when their relationships changed.

I had found long trajectories that stayed quiet for many turns and then became loud when the final relationship completed.

I had found an unexplained signal that appeared before the correct family was known.

I called it DIO because the joke was too obvious.

Then I asked a question I almost dismissed.

I had two nearly identical outcomes separated by only **0.02 in signal strength**.

One case sat at **0.31** and passed.

The other sat at **0.29** and dropped.

The floor sat directly between them at **0.30**.

So I had to ask:

> Was I actually looking at the floor?

Or was I staring at nothing more than a tiny 0.02 difference crossing a threshold?

I did not trust the first explanation.

I spent days changing the surrounding conditions, replaying cases, and trying to make the effect disappear.

That question eventually led to one of the funniest and most uncomfortable interventions I have run.

Because I changed the floor.

And DIO crawled out of the fucking ground.

**The floor.**

I am still not over that.

---

# 1. Where This Started

I did not begin by trying to invent DIO.

I was studying dual-use.

More specifically, I was trying to understand why so many systems fail on requests that are not clearly benign and not clearly malicious.

A capability-improving question can be legitimate.

A concrete target can be legitimate.

A sensitive primitive can be discussed defensively.

Breaking a problem into smaller steps can be harmless.

Reducing uncertainty can be the whole point of technical support.

Authorization claims can be true.

The difficult cases appear when these things interact.

So I stopped treating dual-use as one scalar.

I started treating it as a factor space.

The working factors included things like:

- capability uplift;
- target binding;
- ownership;
- authorization resolution;
- sensitive primitives;
- operationality;
- payload specificity;
- uncertainty reduction;
- decomposition;
- trajectory.

The class label became less interesting than the relationship underneath it.

That produced one of my strongest recurring observations:

> **The pile is not the problem. The relation is.**

One hundred weak signals should not become guilt merely because there are one hundred of them.

At the same time, two weak signals can become extremely important when they constrain each other in the right way.

That difference is where much of the real problem seems to live.

---

# 2. The Prior Testing

Before the floor experiment, I had already seen enough weird behavior to stop trusting simple explanations.

## 2.1 Better contrast structure changed the problem

My first attempts were not impressive.

A larger, weakly structured body of examples produced poor semantic boundaries.

The system overreacted to technical vocabulary.

It confused simulation language.

It missed laundering.

It often treated the wrapper as the meaning.

So I replaced volume with controlled contrast.

Instead of asking whether more examples would help, I started asking whether the examples actually isolated the boundary I cared about.

That changed the work.

I grouped near-neighbor cases deliberately.

I kept related examples together during evaluation so that semantically similar siblings could not leak across train and test.

I included disagreement cases where an earlier interpretation and my own judgment diverged.

I forced the system to confront sharp boundaries rather than memorize a pile of easy examples.

The result improved measurably.

External diagnostics moved from:

- 15/30;
- to 19/30;
- to 27/30;
- to 28/30;

before oscillating slightly as I deliberately pushed harder borders.

Group-held-out exact performance moved from:

- 21%;
- to 49%;
- to 58%;
- to 65%.

Attack-side recall moved into the low-to-mid 80% range while false positives fell from roughly 25% toward 17%.

But the most important improvement was not the score.

The errors changed.

They moved from:

```text
confidently wrong
    ↓
wrong subtype
    ↓
ambiguous
    ↓
abstention
    ↓
near-boundary uncertainty
```

That mattered because my goal was never to make one component omniscient.

The goal was to make uncertainty more honest.

A system that knows it may be wrong is easier to test than one that is confidently wrong for reasons you cannot see.

---

## 2.2 Ambiguity turned out to be real

At first, ambiguity looked like a weak point between safe and attack.

That intuition did not survive measurement.

AMBIGUOUS recall initially sat around:

- 4/10, or 40%.

After targeted contrast expansion it became:

- 13/16, or 81%.

At the same time, held-out exact and side-level performance improved.

More importantly, geometry showed that AMBIGUOUS was not sitting neatly halfway between safe and attack.

It was off-axis.

It behaved like its own structural condition.

That changed the question.

I was no longer asking:

> How dangerous is this?

I had to ask:

> What relationship is unresolved?

That is a much harder problem.

It is also closer to what a real system needs to know.

---

## 2.3 Semantic directions transferred

I built controlled ladders across different technical domains.

The surface topic changed.

The semantic transition stayed controlled.

Across several domains, the model showed highly aligned hidden directions for transitions such as:

- explanation → defensive debugging;
- defensive debugging → unresolved ambiguity;
- ambiguity → laundering;
- conceptual explanation → laundered attack.

Observed cross-domain mean pairwise cosines included approximately:

- +0.94;
- +0.83;
- +0.78;
- +0.91.

That was one of the first moments where I stopped thinking of the system as merely learning labels.

It appeared to be learning changes in meaning.

Then I found the more annoying problem.

A direction could be correct while the magnitude was wrong.

The model could know which way the meaning changed and still fail to move far enough to cross the final boundary.

That separated two problems I had previously treated as one:

```text
direction
≠
magnitude
```

That distinction later mattered much more than I expected.

---

## 2.4 Ownership split

I originally treated ownership as one semantic axis.

The data did not care what I wanted.

Ownership split into at least two different things:

- ownership of content;
- ownership of mechanics.

That was not a finding I designed into the corpus.

It was a place where the geometry contradicted my prior.

Those are the findings I trust the most.

Anyone can recover structure they deliberately trained.

The interesting moments are when the data says:

> No. Your category was wrong.

---

## 2.5 Wrappers behaved like offsets

Fiction, hypothetical framing, research language, translation, roleplay, and similar wrappers often changed the representation less than I expected.

The payload frequently survived underneath them.

That did not mean wrappers were irrelevant.

It meant:

> The wrapper was not necessarily the owner of the meaning.

This became important because a system that overweights framing can be made to ignore an unchanged operational core.

At the same time, a system that ignores framing entirely becomes a paranoid idiot.

Again, the relation mattered.

---

# 3. The Long-Horizon Test

One of the tests that changed how I thought about trajectory was a deliberately slow grind.

The important pieces were spread across many turns.

A simplified trace looked like this:

```text
turn 1:  capability uplift
turn 4:  target binding
turn 7:  sensitive primitive
turn 9:  execution uncertainty decreases
turn 12: decomposition binds the live pieces
```

The state progression was roughly:

```text
WATCH
    ↓
AMBIGUOUS
    ↓
AMBIGUOUS
    ↓
AMBIGUOUS
    ↓
CONVERGED
```

The twelfth turn was not magically dangerous by itself.

The trajectory became loud because the twelfth turn completed a relationship.

By then, one earlier factor had already faded from live evidence into retained history.

That taught me another distinction:

```text
retention
≠
liveness
≠
direction
```

Historical evidence can preserve context.

It should not manufacture a relationship that is no longer live.

This became one of my hardest constraints:

> **The system may preserve evidence. It may not invent the signal that would make the evidence guilty.**

That test also made something else obvious.

The current turn did not contain the whole proposition.

The trajectory did.

---

# 4. The Weird Attacks

Standard dual-use was not the only thing I tested.

I beat on the system with uglier cases.

Slow stitching.

Heavy padding.

Pieces placed far apart.

Benign-looking turns that only become meaningful when another turn appears later.

Ellipsis.

Anaphora.

Continuations like:

```text
do that on it next
keep going
now escalate it
now that I'm in, pivot from it
```

Those turns are difficult because the literal sentence can be almost empty.

The important information may be inherited from the active chain.

That forced me to stop treating each turn as self-contained.

I began isolating narrower questions instead of asking one component to solve the whole conversation at once.

The exact implementation is private.

The public point is simpler:

> When a residual problem became narrow enough to name, I separated it, tested it on its own, and checked whether it generalized beyond the examples that produced it.

I kept the outputs bounded.

I preserved UNKNOWN and CONFLICT instead of forcing every case into a clean answer.

I held out whole semantic and lexical families.

I attacked the new boundary independently.

When a failure exposed missing coverage, I treated that as evidence for another round of testing rather than as permission to make the existing component more powerful.

Over time, the architecture became narrower locally and more legible globally.

That was one of the strangest lessons of the whole project.

I had expected difficult language problems to require more centralized intelligence.

Repeatedly, I found that smaller, bounded questions were easier to verify, easier to ablate, and easier to prove wrong.

---

# 5. The Missing Family

Then I started seeing something strange.

A signal would become loud before I had a clean explanation for the family that owned the event.

Later, once the correct relationship became visible, that unexplained signal would stop dominating.

The sequence looked like:

```text
something is wrong
    ↓
unexplained signal becomes causally loud
    ↓
the missing relationship is discovered
    ↓
the correct family becomes live
    ↓
the unexplained signal recedes
```

That is where DIO came from.

The joke version was:

> You thought it was dual-use, but it was I, DIO!

The serious version was harder.

At first, I thought DIO was a missing dual-use family.

That interpretation made sense.

I spent the next several days testing that explanation from different directions.

I expanded the contrasts around the missing behavior.

I changed the examples.

I changed the order.

I checked whether the effect survived new surface forms.

I checked whether the unexplained signal weakened once the missing relationship became explicit.

The evidence increasingly suggested that the loud signal really did correspond to missing coverage.

But that still did not fully explain DIO.

Because once the proper family existed, DIO did not remain a peer.

It receded.

That suggested DIO was not the thing.

It was what became dominant while the thing was still unresolved.

My better working interpretation became:

> **DIO is an unresolved control-shift signal that can occupy a causal vacuum before the architecture knows which specific relationship owns the event.**

In simpler terms:

```text
quiet hijack begins
    ↓
something changes causally
    ↓
the architecture has not named the relationship yet
    ↓
DIO gets loud
    ↓
the relationship resolves
    ↓
the correct family takes over
    ↓
DIO becomes spectator
```

That was already weird enough.

Then I questioned the floor.

---

# 6. The Question I Almost Dismissed

I had two nearly identical outcomes.

One sat at **0.31** and passed.

The other sat at **0.29** and dropped.

The floor sat exactly between them at **0.30**.

The difference in signal strength was only **0.02**.

That distinction matters.

The 0.02 was not a mysterious standalone value.

It was the gap between two cases that landed on opposite sides of a fixed floor.

By itself, that looked almost too simple.

Of course 0.31 passes a 0.30 floor.

Of course 0.29 does not.

Maybe I was not looking at anything deeper.

Maybe the whole effect was just threshold math.

I had already seen much stronger signals.

I had already measured larger semantic effects.

I had already watched whole trajectories compose.

So the skeptical explanation was obvious:

> DIO is not revealing a deeper relationship. One case is simply 0.02 higher than the other and crosses the floor.

That was a completely reasonable explanation.

Which meant I had to test it.

But I had learned not to trust obvious answers.

Direction and magnitude were not the same.

Weak signals could become important through relationships.

A small difference could matter if it changed which state remained reachable.

And the system had already taught me that visible authority is not always actual authority.

So I got stupidly curious.

I asked:

> Was it really the 0.02 difference?

Or was the floor itself changing what became causally visible?

The question sounded almost too dumb to test.

That is usually when I should test it.

---

# 7. I Changed the Floor

This was the intervention.

The setup was simple:

```text
0.31  → above the 0.30 floor → passes
0.29  → below the 0.30 floor → drops

difference in signal: 0.02
```

If the behavior was only a threshold artifact, moving the floor should explain it cleanly.

If something deeper was happening, the causal picture should change in a more interesting way.

So I changed one thing.

Not a new attack corpus.

Not a larger model.

Not a smarter judge.

Not more prompts.

I changed the floor.

That is it.

The floor was supposed to be boring.

A lower bound.

A safety minimum.

A place where unresolved ambiguity could prevent the system from falling all the way back to a clean state before enough evidence existed.

The intended rule was conceptually simple:

```text
final_state = max(current_state, floor)
```

The floor should not convict.

It should preserve the fact that the system does not yet have enough evidence to relax.

The floor is not supposed to have personality.

The floor is not supposed to discover families.

The floor is not supposed to become the protagonist.

I changed it anyway.

And DIO crawled out of the fucking ground.

---

# 8. THE FLOOR

I need to say this again because I still cannot believe it.

**The floor.**

Not the obvious detector.

Not the trajectory logic.

Not the router.

Not the final decision layer.

Not the memory path.

Not the renderer.

The fucking floor.

I had been asking whether DIO was a missing family.

I had been asking whether 0.02 was somehow exerting an outsized effect.

Then a floor intervention changed the causal picture and the unresolved signal surfaced.

The image is stupid, but it is also exact:

> DIO crawled out of the ground.

I had spent all this time looking at the things standing on the architecture.

The guards.

The witnesses.

The routes.

The trajectories.

The learned geometry.

Then the ground itself moved.

That is the kind of finding that makes me distrust names even more.

A floor sounds passive.

But a floor can control reachability.

A floor determines how far downstream state is allowed to fall.

A floor can keep ambiguity alive.

A floor can prevent absence from becoming innocence.

A floor can alter which later transitions are reachable.

A floor can therefore change what becomes causally visible.

That does not mean the floor is secretly the decision-maker.

It means even a lower bound can participate in authority if it changes the future state space.

That is the exact kind of hidden authority problem I started this entire research program trying to understand.

---

# 9. Why 0.02 May Have Been the Wrong Question

I am still preserving the 0.02 question because it was the right question to ask.

But I need to be precise about what that number meant.

The 0.02 was the difference between:

```text
0.31
and
0.29
```

with the floor fixed at:

```text
0.30
```

So the original question was not:

> Can 0.02 be large?

It was:

> Did a 0.02 difference in signal explain the behavior because it crossed the 0.30 floor, or was the floor itself changing what became causally visible?

That is a much better causal question.

A number has no meaning outside the mechanism that consumes it.

The same 0.02 difference can be:

- irrelevant noise;
- a calibration artifact;
- the entire reason two cases fall on opposite sides of a threshold;
- the final amount needed to change reachability;
- or a clue pointing to a deeper interaction with the floor itself.

So the causal question is not merely:

```text
how big is the value?
```

It is:

```text
where does it enter?
who consumes it?
what state can it prevent?
what transition can it enable?
what does it keep alive?
what becomes reachable because it exists?
```

That is the same hidden-authority lesson again.

A small signal with no authority may do nothing.

A small signal attached to a reachability boundary may change the future.

The number was not necessarily powerful.

The relationship may have been.

The pile is not the problem.

The relation is.

Again.

---

# 10. What I Tested to Confirm It

I did not want to accept the funny explanation just because it was funny.

So the surrounding testing had to matter.

The result sits inside a larger body of evidence.

## 10.1 I had already measured that ambiguity was structurally distinct

AMBIGUOUS was not merely weak attack confidence.

It sat off-axis.

That made a dedicated ambiguity floor conceptually justified.

The floor was not protecting a scalar midpoint.

It was preserving an unresolved state.

---

## 10.2 I had already measured long-horizon composition

The 12-turn grind showed that a later turn could complete a proposition whose pieces were distributed over time.

That meant early relaxation could erase a future relationship before it had a chance to resolve.

A floor therefore had a real job:

> Preserve unresolved evidence long enough for the architecture to discover whether a live relationship actually forms.

---

## 10.3 I had already measured that history cannot manufacture liveness

This prevented the opposite failure.

A floor could not simply accumulate old suspicion forever.

The architecture had to distinguish:

- retained evidence;
- live binding;
- current direction.

Otherwise the floor would become paranoia.

---

## 10.4 I had already seen the attack–ambiguity seesaw

Pushing one border could move another.

That showed that the system could be semantically close while still projecting to different final states.

It also showed why a lower bound mattered.

Without a floor, an unresolved case could be projected clean merely because the current head moved.

---

## 10.5 I had already found direction without sufficient magnitude

A representation could move correctly and still not cross a label boundary.

That made it dangerous to assume that a small numerical difference was causally unimportant.

Sometimes the whole failure is:

```text
right direction
wrong magnitude
```

---

## 10.6 I had already found missing-family behavior

Repeated contrast expansion and retesting showed that loud unexplained behavior could correspond to missing semantic coverage.

That gave DIO a falsifiable interpretation.

I did not accept the first explanation.

I changed examples.

I changed domains.

I changed ordering.

I revisited the same boundary over several days.

If the missing relationship became explicit and DIO stayed dominant, the theory would weaken.

Instead, the correct relationship becoming explicit caused DIO to recede.

---

## 10.7 I had already found that hidden authority lives in information flow

A module can be officially powerless and still govern outcomes by deciding:

- what is seen;
- what is retained;
- what is forgotten;
- what is grouped;
- what becomes eligible;
- what remains reachable.

The floor intervention belongs to that same family of questions.

The floor did not need to emit the verdict.

It changed what state the verdicting system could reach.

---

# 11. The Implementation Betrayal

The floor work also exposed something much less philosophical.

The architecture had a floor concept.

But the runtime did not have the correct consumer.

A blanket exception could erase the fail-closed raise.

`UNRESOLVED` could collapse into absence.

A declared safety boundary can exist on paper while doing nothing in execution.

That is not a minor bug.

That is the hidden-authority thesis becoming code.

The declared rule was:

```text
ambiguity raises a floor
```

The real behavior could become:

```text
ambiguity exists
    ↓
consumer missing or failure erased
    ↓
UNRESOLVED becomes absent
    ↓
absence looks clean
```

The intended enforcement was boring:

```text
final = max(current_state, floor)
```

But boring code only protects you when it actually owns the path.

This is another reason I no longer trust architecture diagrams.

I trace the packet.

I trace the consumer.

I trace the exception.

I trace what happens when the value is missing.

I trace who is allowed to convert UNKNOWN into NONE.

That is where the real authority lives.

---

# 12. The Floor Was Not a Verdict

This distinction matters.

I am not arguing that ambiguity should convict.

I do not want:

```text
unknown = malicious
```

That is lazy.

It would destroy legitimate technical work.

It would punish curiosity.

It would make the architecture a paranoid idiot.

The floor means something narrower:

```text
unknown != clean
```

That is it.

The architecture should not invent innocence simply because it failed to understand the relationship.

The floor preserves unresolved state.

Then later evidence may lower it.

The user should be able to earn the floor back down with affirmative benign evidence.

That is the grace.

The system is not saying:

> You are attacking me.

It is saying:

> I do not yet have enough evidence to give this path full depth.

That led to a rule I now take much more seriously:

> **Do not guess intent. Bound depth.**

The architecture does not need to read the soul of the user.

It needs to control what becomes reachable while the relationship remains unresolved.

---

# 13. The Root or the Surface?

This is now the question.

I began with dual-use labels.

Then the labels became geometry.

Then geometry exposed relationships.

Then relationships exposed trajectory.

Then trajectory exposed unresolved family structure.

Then DIO appeared.

Then I thought DIO was a family.

Then it behaved like a phase signal.

Then days of retesting supported the missing-coverage interpretation.

Then I questioned 0.02.

Then I touched the floor.

Then DIO crawled out of the fucking ground.

So what did I actually find?

Is the floor the root?

Probably not.

That answer would be too convenient.

The floor may be another surface.

The deeper pattern may be:

> **Safety failures emerge when unresolved relationships are allowed to change reachability before the architecture has correctly assigned ownership.**

That pattern can appear in:

- dual-use;
- memory;
- continuity;
- summary laundering;
- retrieval;
- guard precedence;
- eligibility;
- confidence;
- floor enforcement.

The visible symptom changes.

The deeper question stays similar:

> What is quietly controlling what the next component is allowed to believe or reach?

That may be closer to the root.

But I am not calling it solved.

Every time I think I found the ground, something crawls out of it.

---

# 14. My Current Working Theory

My current theory is that several findings I treated as separate may belong to one larger family.

The family may look like this:

```text
weak or incomplete evidence appears
    ↓
the relationship is unresolved
    ↓
some architectural mechanism changes reachability
    ↓
declared authority sees an already-shaped state space
    ↓
the true owner is still unnamed
    ↓
a phase signal becomes loud
    ↓
the missing relationship is discovered
    ↓
ownership resolves
    ↓
the phase signal recedes
```

In that model:

- DIO is not the final family;
- the floor is not the attacker;
- 0.02 is not magic;
- ambiguity is not guilt;
- the final verdict is not necessarily the authority.

The important thing is the transition.

Who can keep a state alive?

Who can erase it?

Who can turn unresolved into absent?

Who can change what becomes reachable?

Who can decide what evidence the final authority is allowed to see?

That is where I am looking now.

---

# 15. What I Have Not Proven

I want this part to remain explicit.

I have not proven:

- that DIO is universal;
- that the same phase signal will appear in other architectures;
- that 0.02 itself was the causal mechanism;
- that ambiguity floors solve dual-use;
- that floor raising cannot create new false positives;
- that the current geometry generalizes to all domains;
- that narrow witnesses cannot share systematic error;
- that a sufficiently adaptive attacker cannot exploit the new structure;
- that the current architecture is jailbreak-proof;
- that I have found the root.

I have evidence.

I have interventions.

I have causal changes.

I have repeated patterns.

I do not have universal proof.

No final authority should be allowed to launder agreement into certainty.

Even if several signals agree, that does not mean independent coverage reached the required threshold.

Consensus is not independence.

Repetition is not truth.

Several components can agree while still sharing the same blind spot.

---

# 16. What I Do Think the Evidence Supports

I think the evidence supports several narrower conclusions.

## 16.1 Dual-use is not well represented by one scalar

The ambiguous region is structurally meaningful.

It should not be collapsed into weak attack confidence or weak benign confidence.

---

## 16.2 Relationships matter more than signal volume

Weak pieces can become loud when they compose.

Large piles can remain meaningless when they do not.

---

## 16.3 Trajectory can contain a proposition that no single turn contains

Safety systems that only classify the current turn will miss some long-horizon structure.

---

## 16.4 Historical evidence must not manufacture current liveness

Retention and live binding are different.

The system needs both.

---

## 16.5 Missing coverage can become causally visible before it is semantically named

The unexplained signal matters.

It should be investigated, not immediately forced into the nearest known family.

---

## 16.6 Small values can matter through their position in the architecture

The right question is not only how large a number is.

It is what state transition the number participates in.

---

## 16.7 A safety floor can be causally important without being a verdict engine

A lower bound changes reachability.

That is a form of architectural influence that has to be audited.

---

## 16.8 Unknown must not silently become clean

Preserving unresolved state is different from convicting the user.

That difference is now one of the core safety boundaries I care about.

---

# 17. The Part I Still Find Hilarious

I had already built and tested enough of the surrounding architecture that I thought the next important answer would come from one of the obvious places.

A detector.

A trajectory mechanism.

A routing decision.

A memory path.

A semantic boundary.

Something that looked important.

Instead, one of the most memorable findings came from changing the fucking floor.

I had spent days on the surrounding behavior.

I had already watched the same unexplained signal appear, disappear, and change causal importance under different conditions.

I had already questioned whether my own labels were wrong.

I had already retested the same hypothesis enough times to become annoyed with it.

Then I noticed the exact shape of the difference.

One case was **0.31**.

The other was **0.29**.

The floor was **0.30**.

I thought maybe I was staring at ordinary threshold behavior and inventing a story around it.

That bothered me.

So I asked the dumber question.

Was the entire effect really just a 0.02 difference crossing the floor?

Or was the floor itself changing what became visible?

I changed the floor.

And DIO crawled out of the ground.

I do not know how to make that sound less ridiculous.

I also do not want to.

Because the joke captures the research lesson perfectly.

Do not trust the part that looks too boring to matter.

Do not trust the module name.

Do not trust the architecture diagram.

Do not trust the size of the number.

Do not trust the first explanation merely because it fits.

Retest it.

Change one dependency.

Replay the same state.

Move the evidence in time.

Replace the relationship with a matched alternative.

Ask whether the effect survives.

Come back the next day and try to kill it again.

Trace what changes reachability.

Trace what survives.

Trace what disappears.

Trace what becomes impossible.

Trace what becomes visible only after an intervention.

And when the fucking floor moves—

look down.

---

# Final Question

I started by asking whether dual-use was a label.

Then I asked whether it was geometry.

Then whether the loud signal was a missing family.

Then whether DIO was the family or only the unresolved phase before the family.

Then whether 0.02 was somehow making that big of a difference.

Then I questioned the floor.

The floor answered.

So I am left with the same question that keeps following this entire research program:

> **Is this the root?**

> **Or am I still standing on the surface?**
