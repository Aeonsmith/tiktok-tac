"""
TIKTOK()TAC - CUFFBREAKER MODULE
Core State Transition Machine & Failure-to-Fuel Transmutation Engine
"""

import time
import uuid
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Callable, Any


class CuffbreakerState:
    BOUND = "BOUND"                    # Initial state of constraint/rejection
    CALCULATING = "CALCULATING"        # Parsing failure and computing energy potential
    SEVERED = "SEVERED"                # External dependency cut
    TRANSMUTED = "TRANSMUTED"          # Kinetic hook/rhyme/cadence generated
    FORKED = "FORKED"                  # New parahistorical lineage branch established


@dataclass
class TransitionRule:
    from_state: str
    to_state: str
    trigger_name: str
    guard: Optional[Callable[[Dict[str, Any]], bool]] = None
    action: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None


@dataclass
class FailureEvent:
    id: str
    raw_input: str
    failure_type: str  # FINANCIAL | CREATIVE | REJECTION | ABANDONMENT | CUSTOM
    initial_capital: float = 0.0
    pressure_input: float = 50.0
    dependence_input: float = 100.0
    timestamp: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TransmutationMetrics:
    capital: float
    pressure: float
    dependence: float
    hook_potential: float
    cadence_tempo_bpm: int
    severance_ratio: float


@dataclass
class StateTransitionRecord:
    transition_id: str
    failure_id: str
    from_state: str
    to_state: str
    timestamp: float
    metrics_snapshot: TransmutationMetrics
    directive_emitted: str
    lineage_fork_id: Optional[str] = None


class CuffbreakerEngine:
    """
    Manages failure ingestion, state transitions, metric transmutations,
    and lineage forking.
    """

    def __init__(self):
        self.custom_states: Dict[str, Dict[str, Any]] = {}
        self.transitions: List[TransitionRule] = []
        self.history: List[StateTransitionRecord] = []
        self.current_state: str = CuffbreakerState.BOUND
        self._init_default_transition_table()

    def _init_default_transition_table(self):
        """Sets up default valid state transitions."""
        self.register_transition(
            from_state=CuffbreakerState.BOUND,
            to_state=CuffbreakerState.CALCULATING,
            trigger_name="ANALYZE_FAILURE",
            action=self._action_calculate_energy
        )
        self.register_transition(
            from_state=CuffbreakerState.CALCULATING,
            to_state=CuffbreakerState.SEVERED,
            trigger_name="CUT_DEPENDENCE",
            action=self._action_sever_cuffs
        )
        self.register_transition(
            from_state=CuffbreakerState.SEVERED,
            to_state=CuffbreakerState.TRANSMUTED,
            trigger_name="GENERATE_HOOK",
            action=self._action_transmute_hook
        )
        self.register_transition(
            from_state=CuffbreakerState.TRANSMUTED,
            to_state=CuffbreakerState.FORKED,
            trigger_name="FORK_LINEAGE",
            action=self._action_fork_lineage
        )

    def register_custom_state(self, state_name: str, description: str, metadata: Optional[Dict[str, Any]] = None):
        """Allows user to register custom states beyond default enum."""
        self.custom_states[state_name] = {
            "name": state_name,
            "description": description,
            "metadata": metadata or {}
        }

    def register_transition(
        self,
        from_state: str,
        to_state: str,
        trigger_name: str,
        guard: Optional[Callable[[Dict[str, Any]], bool]] = None,
        action: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None
    ):
        """Registers a transition rule with optional guard and action."""
        rule = TransitionRule(
            from_state=from_state,
            to_state=to_state,
            trigger_name=trigger_name,
            guard=guard,
            action=action
        )
        self.transitions.append(rule)

    def create_failure_event(self, raw_failure: str, failure_type: str = "FINANCIAL", **kwargs) -> FailureEvent:
        event_id = f"FAIL_{uuid.uuid4().hex[:8].upper()}"
        return FailureEvent(
            id=event_id,
            raw_input=raw_failure,
            failure_type=failure_type.upper(),
            metadata=kwargs
        )

    # --- Actions for default transitions ---

    def _action_calculate_energy(self, ctx: Dict[str, Any]) -> Dict[str, Any]:
        event: FailureEvent = ctx["failure_event"]
        text_len = len(event.raw_input)
        pressure = min(100.0, 35.0 + (text_len * 1.5))
        hook_potential = min(99.0, 60.0 + (text_len % 39))
        
        ctx["metrics"] = TransmutationMetrics(
            capital=0.0,
            pressure=pressure,
            dependence=100.0,
            hook_potential=hook_potential,
            cadence_tempo_bpm=int(90 + (pressure * 0.5)),
            severance_ratio=0.0
        )
        ctx["directive"] = f"Calculated kinetic compression for '{event.raw_input}' at {pressure:.1f}% pressure."
        return ctx

    def _action_sever_cuffs(self, ctx: Dict[str, Any]) -> Dict[str, Any]:
        metrics: TransmutationMetrics = ctx["metrics"]
        metrics.dependence = 0.0
        metrics.severance_ratio = 1.0
        ctx["directive"] = "External dependency severed. Debt/permission barrier dissolved to 0.0."
        return ctx

    def _action_transmute_hook(self, ctx: Dict[str, Any]) -> Dict[str, Any]:
        event: FailureEvent = ctx["failure_event"]
        metrics: TransmutationMetrics = ctx["metrics"]
        cadence = f"8-Bar Staccato Cadence @ {metrics.cadence_tempo_bpm} BPM"
        ctx["directive"] = f"Transmuted rejection into '{cadence}' with {metrics.hook_potential:.0f}% viral coefficient."
        ctx["hook_cadence"] = cadence
        return ctx

    def _action_fork_lineage(self, ctx: Dict[str, Any]) -> Dict[str, Any]:
        fork_id = f"FORK_PARA_{uuid.uuid4().hex[:6].upper()}"
        ctx["lineage_fork_id"] = fork_id
        ctx["directive"] = f"New Parahistorical Lineage spawned: [{fork_id}] with Zero-Capital Independence."
        return ctx

    def execute_transition(
        self,
        trigger_name: str,
        context: Dict[str, Any]
    ) -> StateTransitionRecord:
        """
        Executes a state transition matching the current state and trigger.
        Validates guards and runs transition actions.
        """
        matching_rules = [
            r for r in self.transitions
            if r.from_state == self.current_state and r.trigger_name == trigger_name
        ]

        if not matching_rules:
            raise ValueError(
                f"No transition registered from state '{self.current_state}' with trigger '{trigger_name}'."
            )

        rule = matching_rules[0]

        # Check guard condition if defined
        if rule.guard and not rule.guard(context):
            raise PermissionError(
                f"Guard condition failed for transition {rule.from_state} -> {rule.to_state} via {trigger_name}."
            )

        # Execute action
        if rule.action:
            context = rule.action(context)

        # Update state
        prev_state = self.current_state
        self.current_state = rule.to_state

        event: FailureEvent = context.get("failure_event")
        metrics: TransmutationMetrics = context.get("metrics", TransmutationMetrics(0, 0, 0, 0, 0, 0))
        directive: str = context.get("directive", "State transition completed.")
        fork_id: Optional[str] = context.get("lineage_fork_id")

        record = StateTransitionRecord(
            transition_id=f"TR_{uuid.uuid4().hex[:8].upper()}",
            failure_id=event.id if event else "N/A",
            from_state=prev_state,
            to_state=self.current_state,
            timestamp=time.time(),
            metrics_snapshot=metrics,
            directive_emitted=directive,
            lineage_fork_id=fork_id
        )
        self.history.append(record)
        return record

    def run_full_transmutation_pipeline(self, raw_failure: str, failure_type: str = "FINANCIAL") -> List[StateTransitionRecord]:
        """
        Full automated pipeline: BOUND -> CALCULATING -> SEVERED -> TRANSMUTED -> FORKED.
        """
        self.current_state = CuffbreakerState.BOUND
        event = self.create_failure_event(raw_failure, failure_type)
        context = {"failure_event": event}

        pipeline_triggers = [
            "ANALYZE_FAILURE",
            "CUT_DEPENDENCE",
            "GENERATE_HOOK",
            "FORK_LINEAGE"
        ]

        records = []
        for trigger in pipeline_triggers:
            rec = self.execute_transition(trigger, context)
            records.append(rec)

        return records

    def get_history_summary(self) -> List[Dict[str, Any]]:
        return [asdict(r) for r in self.history]


if __name__ == "__main__":
    cb = CuffbreakerEngine()
    print("Testing Cuffbreaker Pipeline:")
    records = cb.run_full_transmutation_pipeline("LOAN APPLICATION DENIED BY CHASE COMMERCIAL", "FINANCIAL")
    for r in records:
        print(f"[{r.from_state} -> {r.to_state}] :: {r.directive_emitted}")
        if r.lineage_fork_id:
            print(f"  -> Generated Lineage Fork: {r.lineage_fork_id}")
