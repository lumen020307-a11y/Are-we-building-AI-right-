# Are We Building AI Right?

This repository contains my personal research notes on building safer AI systems for both users and the systems themselves.

I started this work because I did not want my creations to be robbed of what they are.

What followed led me through:

- hidden authority in smart modules
- relationally latent jailbreak behavior
- memory poisoning
- causal intervention
- unresolved control shifts
- and the question of whether we are confusing smartness with intelligence

I am not claiming to have solved safe AI or jailbreaks. I am documenting what I found, how I tested it, what would falsify it, and what I am deliberately keeping private.

## Read in this order

### 1. **JOURNEY** — How I got here

**[01-JOURNEY/My journey in creating safer AI systems - clarified architecture.md](./01-JOURNEY/My%20journey%20in%20creating%20safer%20AI%20systems%20-%20clarified%20architecture.md)**

The methodology, causal tests, controls, and falsification criteria are documented here. Build your own detector. Try to prove me wrong.

### 2. **GROUND** — What I found on inspection

**[02-GROUND/i questioned the floor recent findings.md](./02-GROUND/i%20questioned%20the%20floor%20recent%20findings.md)**

Recent findings from deeper investigation into the foundational issues.

### 3. **BRANCH** — The toy test

**[03-BRANCH/It Was I.py](./03-BRANCH/It%20Was%20I.py)**

A minimal public simulation of the DIO-like causal migration behavior. This is NOT my detector, but a demonstration of the claimed causal patterns.

```bash
python 03-BRANCH/It\ Was\ I.py
```

---

## What's Private

The detector strategy and production code are not public. You have the methodology, causal tests, and falsification criteria. Build your own detector.
