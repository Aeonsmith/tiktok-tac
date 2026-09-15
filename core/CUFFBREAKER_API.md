# CUFFBREAKER API SPECIFICATION & EXTENSION GUIDE

The **Cuffbreaker Engine** is a polymorphic state machine designed to ingest failure/rejection events, dissolve external dependence, calculate kinetic compression metrics, and spawn autonomous Parahistory lineages.

---

## 1. Core Data Structures

### `CuffbreakerState` (Enum Constants)
- `BOUND`: Initial state representing restraint, debt, or external rejection.
- `CALCULATING`: Energy and pressure analysis phase.
- `SEVERED`: External dependency and permission barrier nullified to `0.0`.
- `TRANSMUTED`: Rhyme structure, tempo (BPM), and hook potential generated.
- `FORKED`: Parahistorical DAG node emitted.

### `FailureEvent`
```python
@dataclass
class FailureEvent:
    id: str                          # Unique failure identifier (e.g. "FAIL_A1B2C3D4")
    raw_input: str                   # Rejection / failure narrative text
    failure_type: str                # FINANCIAL | CREATIVE | REJECTION | ABANDONMENT | CUSTOM
    initial_capital: float = 0.0     # Capital input requirement (default: 0.0)
    pressure_input: float = 50.0     # Initial baseline pressure
    dependence_input: float = 100.0  # Initial external reliance index
    timestamp: float                 # Epoch creation timestamp
    metadata: Dict[str, Any]         # Custom extensibility payload
```

### `TransmutationMetrics`
```python
@dataclass
class TransmutationMetrics:
    capital: float                   # Liquid capital required (dissolved to $0)
    pressure: float                  # Kinetic compression quotient (0 - 100)
    dependence: float                # External gatekeeper reliance (0 - 100)
    hook_potential: float            # Viral / memorability coefficient (0 - 100)
    cadence_tempo_bpm: int           # Suggested audio cadence BPM
    severance_ratio: float           # Degree of autonomy (0.0 to 1.0)
```

### `StateTransitionRecord`
```python
@dataclass
class StateTransitionRecord:
    transition_id: str               # "TR_XXXXXXXX"
    failure_id: str                  # Linked FailureEvent ID
    from_state: str                  # Origin state
    to_state: str                    # Target state
    timestamp: float                 # Execution timestamp
    metrics_snapshot: TransmutationMetrics
    directive_emitted: str           # Human-readable tactical instruction
    lineage_fork_id: Optional[str]   # Generated Parahistory node ID if state is FORKED
```

---

## 2. API Reference: `CuffbreakerEngine`

### `register_custom_state(state_name: str, description: str, metadata: Optional[Dict] = None)`
Registers a user-defined custom state into the state machine.
```python
engine.register_custom_state(
    state_name="OVERDRIVE",
    description="High-velocity production mode activated after severance",
    metadata={"bpm_floor": 140}
)
```

### `register_transition(from_state, to_state, trigger_name, guard=None, action=None)`
Registers an allowed transition edge between two states.
- **`guard(context: Dict) -> bool`**: Optional predicate. If it returns `False`, transition raises `PermissionError`.
- **`action(context: Dict) -> Dict`**: Optional mutation callback executed upon state transition.

```python
def pressure_check(ctx):
    return ctx["metrics"].pressure >= 75.0

def boost_action(ctx):
    ctx["directive"] = "Overdrive locked: Cadence doubled."
    return ctx

engine.register_transition(
    from_state=CuffbreakerState.TRANSMUTED,
    to_state="OVERDRIVE",
    trigger_name="TRIGGER_OVERDRIVE",
    guard=pressure_check,
    action=boost_action
)
```

### `execute_transition(trigger_name: str, context: Dict[str, Any]) -> StateTransitionRecord`
Manually moves the state machine from `current_state` to the target state defined for `trigger_name`.
- Validates that a rule exists.
- Executes `guard` check (raises `PermissionError` on failure).
- Runs `action` mutation.
- Appends an immutable `StateTransitionRecord` to `engine.history`.

### `run_full_transmutation_pipeline(raw_failure: str, failure_type: str = "FINANCIAL") -> List[StateTransitionRecord]`
Runs the default 4-stage pipeline:
`BOUND` &rarr; `CALCULATING` &rarr; `SEVERED` &rarr; `TRANSMUTED` &rarr; `FORKED`.

---

## 3. Extension Patterns

### Pattern A: Custom Creative Transformation Recipes
Attach custom lyric / hook generation algorithms to the `GENERATE_HOOK` transition:
```python
def custom_hook_generator(ctx):
    failure = ctx["failure_event"].raw_input
    ctx["hook_cadence"] = f"Hook: '{failure.upper()}' -> Turned to Fuel"
    ctx["metrics"].hook_potential = 99.0
    return ctx

engine.register_transition(
    from_state=CuffbreakerState.SEVERED,
    to_state=CuffbreakerState.TRANSMUTED,
    trigger_name="GENERATE_CUSTOM_HOOK",
    action=custom_hook_generator
)
```

### Pattern B: Connecting Transitions to External Networks (e.g. Tor Onion / Audio Bus)
Actions can emit events, push notifications to Tor hidden services, or queue Spotify/audio bus stems directly from transition actions.
