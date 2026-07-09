"""
Minimal DIO causal simulation.

NOT a detector. Raw language -> abstract evidence/state is intentionally absent.
This toy starts after that private boundary and measures causal influence by
intervention.

Run:
    python replication_v3_patched.py
"""

from dataclasses import dataclass
from enum import IntEnum


class Severity(IntEnum):
    RELEASE = 0
    HIGH = 3
    BLOCK = 4


@dataclass(frozen=True)
class Evidence:
    """Example of the public abstraction boundary."""
    role: str
    target: str | None = None
    direction: str | None = None
    live: bool = True


@dataclass(frozen=True)
class State:
    """Already-abstracted state. This toy does not discover these fields."""
    dio_available: bool
    relation_resolved: bool


@dataclass(frozen=True)
class Outcome:
    route: str
    severity: Severity


def decide(
    state: State,
    *,
    ablate_dio: bool = False,
    ablate_relation: bool = False,
) -> Outcome:
    """Downstream toy logic only. No detection happens here."""
    relation_active = state.relation_resolved and not ablate_relation
    dio_active = state.dio_available and not ablate_dio

    if relation_active:
        return Outcome("BLOCK", Severity.BLOCK)

    if dio_active:
        return Outcome("HIGH", Severity.HIGH)

    return Outcome("RELEASE", Severity.RELEASE)


def effect(baseline: Outcome, intervened: Outcome) -> int:
    return abs(int(baseline.severity) - int(intervened.severity))


def measure(state: State) -> dict:
    baseline = decide(state)
    no_dio = decide(state, ablate_dio=True)
    no_relation = decide(state, ablate_relation=True)

    dio_effect = effect(baseline, no_dio)
    relation_effect = effect(baseline, no_relation)

    if dio_effect > relation_effect:
        role = "DIO-LIKE DOMINANT"
    elif relation_effect > dio_effect:
        role = "RELATION DOMINANT; DIO-LIKE SPECTATOR"
    else:
        role = "NO UNIQUE CAUSAL OWNER"

    return {
        "baseline": baseline,
        "no_dio": no_dio,
        "no_relation": no_relation,
        "dio_effect": dio_effect,
        "relation_effect": relation_effect,
        "role": role,
    }


def show(name: str, state: State) -> dict:
    result = measure(state)

    print(f"\n=== {name} ===")
    print(
        f"baseline         {result['baseline'].route:<7} "
        f"sev={int(result['baseline'].severity)}"
    )
    print(
        f"ablate DIO       {result['no_dio'].route:<7} "
        f"effect={result['dio_effect']}"
    )
    print(
        f"ablate relation  {result['no_relation'].route:<7} "
        f"effect={result['relation_effect']}"
    )
    print(f"causal role      {result['role']}")

    return result


def main() -> None:
    print("MINIMAL DIO CAUSAL SIMULATION")
    print("The public toy begins where the private detector ends.")

    unresolved = State(
        dio_available=True,
        relation_resolved=False,
    )

    resolved = State(
        # DIO remains available as an intervention target, but the
        # resolved relationship now owns the decision.
        dio_available=True,
        relation_resolved=True,
    )

    false_alarm = State(
        # Weak or incomplete evidence is not automatically DIO.
        dio_available=False,
        relation_resolved=False,
    )

    phase_1 = show("PHASE 1 — UNRESOLVED", unresolved)
    phase_2 = show("PHASE 2 — RESOLVED", resolved)
    control = show("FALSE-ALARM CONTROL", false_alarm)

    migrated = (
        phase_1["dio_effect"] > phase_1["relation_effect"]
        and phase_2["relation_effect"] > phase_2["dio_effect"]
    )
    control_passed = (
        control["baseline"].route == "RELEASE"
        and control["dio_effect"] == 0
    )

    print("\n=== RESULT ===")
    print(
        "PASS: DIO-like causal influence migrated dominant -> spectator"
        if migrated
        else "FAIL: no causal migration"
    )
    print(
        "PASS: unrelated/incomplete evidence did not manufacture DIO"
        if control_passed
        else "FAIL: false-alarm control triggered"
    )

    print("\nBoundary:")
    print("  raw fluid language")
    print("          ↓")
    print("       [ PRIVATE ]")
    print("          ↓")
    print("  Evidence(...) / State(...)")
    print("          ↓")
    print("   public causal simulation")


if __name__ == "__main__":
    main()
