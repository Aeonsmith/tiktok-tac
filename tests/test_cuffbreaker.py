"""
TIKTOK()TAC - UNIT TESTS FOR CUFFBREAKER MODULE
Tests for State Transitions, Custom User Transitions, Guards, and DAG Forking
"""

import unittest
import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.cuffbreaker import (
    CuffbreakerEngine,
    CuffbreakerState,
    FailureEvent,
    TransmutationMetrics,
    StateTransitionRecord
)
from core.engine import TikTokTacEngine


class TestCuffbreakerTransitions(unittest.TestCase):

    def setUp(self):
        self.engine = CuffbreakerEngine()

    def test_initial_state(self):
        self.assertEqual(self.engine.current_state, CuffbreakerState.BOUND)
        self.assertEqual(len(self.engine.history), 0)

    def test_full_automated_pipeline(self):
        input_failure = "LOAN DENIED BY BANK WITH STRICT COLLATERAL POLICY"
        records = self.engine.run_full_transmutation_pipeline(input_failure, "FINANCIAL")

        self.assertEqual(len(records), 4)
        self.assertEqual(records[0].from_state, CuffbreakerState.BOUND)
        self.assertEqual(records[0].to_state, CuffbreakerState.CALCULATING)

        self.assertEqual(records[1].from_state, CuffbreakerState.CALCULATING)
        self.assertEqual(records[1].to_state, CuffbreakerState.SEVERED)
        self.assertEqual(records[1].metrics_snapshot.dependence, 0.0)

        self.assertEqual(records[2].from_state, CuffbreakerState.SEVERED)
        self.assertEqual(records[2].to_state, CuffbreakerState.TRANSMUTED)
        self.assertGreater(records[2].metrics_snapshot.hook_potential, 50.0)

        self.assertEqual(records[3].from_state, CuffbreakerState.TRANSMUTED)
        self.assertEqual(records[3].to_state, CuffbreakerState.FORKED)
        self.assertIsNotNone(records[3].lineage_fork_id)
        self.assertTrue(records[3].lineage_fork_id.startswith("FORK_PARA_"))

    def test_step_by_step_transition_execution(self):
        event = self.engine.create_failure_event("PROJECT CANCELLED BY STUDIO", "CREATIVE")
        ctx = {"failure_event": event}

        # Step 1: BOUND -> CALCULATING
        rec1 = self.engine.execute_transition("ANALYZE_FAILURE", ctx)
        self.assertEqual(self.engine.current_state, CuffbreakerState.CALCULATING)
        self.assertIn("pressure", ctx["metrics"].__dict__)

        # Step 2: CALCULATING -> SEVERED
        rec2 = self.engine.execute_transition("CUT_DEPENDENCE", ctx)
        self.assertEqual(self.engine.current_state, CuffbreakerState.SEVERED)
        self.assertEqual(ctx["metrics"].dependence, 0.0)

    def test_invalid_trigger_raises_error(self):
        event = self.engine.create_failure_event("RANDOM FAIL", "CUSTOM")
        ctx = {"failure_event": event}

        # Triggering FORK_LINEAGE from BOUND should raise ValueError
        with self.assertRaises(ValueError):
            self.engine.execute_transition("FORK_LINEAGE", ctx)

    def test_custom_user_defined_state_and_guarded_transition(self):
        # 1. Register custom state
        self.engine.register_custom_state(
            state_name="HYPERDRIVE",
            description="Extreme audio production mode when pressure > 80"
        )
        self.assertIn("HYPERDRIVE", self.engine.custom_states)

        # 2. Register guarded transition from TRANSMUTED -> HYPERDRIVE
        def pressure_guard(ctx):
            return ctx.get("metrics") and ctx["metrics"].pressure > 50.0

        def hyperdrive_action(ctx):
            ctx["directive"] = "HYPERDRIVE ENGAGED: BPM OVERCLOCKED TO 160."
            return ctx

        self.engine.register_transition(
            from_state=CuffbreakerState.TRANSMUTED,
            to_state="HYPERDRIVE",
            trigger_name="ENGAGE_HYPERDRIVE",
            guard=pressure_guard,
            action=hyperdrive_action
        )

        # 3. Advance to TRANSMUTED
        event = self.engine.create_failure_event("RECORD DEAL TERMINATED ABRUPTLY", "CREATIVE")
        ctx = {"failure_event": event}
        self.engine.execute_transition("ANALYZE_FAILURE", ctx)
        self.engine.execute_transition("CUT_DEPENDENCE", ctx)
        self.engine.execute_transition("GENERATE_HOOK", ctx)
        self.assertEqual(self.engine.current_state, CuffbreakerState.TRANSMUTED)

        # 4. Trigger custom transition
        rec = self.engine.execute_transition("ENGAGE_HYPERDRIVE", ctx)
        self.assertEqual(self.engine.current_state, "HYPERDRIVE")
        self.assertIn("HYPERDRIVE ENGAGED", rec.directive_emitted)

    def test_guard_failure_blocks_transition(self):
        # Register a guarded transition that always fails
        self.engine.register_transition(
            from_state=CuffbreakerState.BOUND,
            to_state="BLOCKED_STATE",
            trigger_name="FAILING_TRIGGER",
            guard=lambda ctx: False
        )
        event = self.engine.create_failure_event("TEST REJECTION", "FINANCIAL")
        ctx = {"failure_event": event}

        with self.assertRaises(PermissionError):
            self.engine.execute_transition("FAILING_TRIGGER", ctx)

    def test_integration_with_tiktok_tac_engine_dag(self):
        tac_engine = TikTokTacEngine()
        initial_node_count = len(tac_engine.nodes)

        res = tac_engine.evaluate_command("failure LOAN APPLICATION TURNED DOWN")
        self.assertEqual(res["mode"], "CUFFBREAKER")
        self.assertEqual(res["result"]["capital"], 0)
        self.assertIsNotNone(res["result"]["lineage_fork_id"])

        # Check that the new lineage node was created in the main DAG
        fork_id = res["result"]["lineage_fork_id"]
        self.assertIn(fork_id, tac_engine.nodes)
        self.assertEqual(len(tac_engine.nodes), initial_node_count + 1)
        self.assertEqual(tac_engine.nodes[fork_id].parent_id, "para_norman_sann")


if __name__ == "__main__":
    unittest.main()
