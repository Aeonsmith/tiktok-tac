"""
TIKTOK()TAC - CORE ENGINE & DATA SCHEMAS
"What is App?" Polymorphic Machine
"""

import json
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Any
from .cuffbreaker import CuffbreakerEngine, CuffbreakerState, FailureEvent, StateTransitionRecord


@dataclass
class Element:
    symbol: str
    atomic_number: int
    name: str
    identity: str
    pressure: int  # 0 - 100
    failure_quotient: int  # 0 - 100
    hook_potential: int  # 0 - 100
    fear_index: int  # 0 - 100
    voice: str
    origin: str
    release_vector: str


@dataclass
class LineageNode:
    id: str
    name: str
    house: str
    era: str
    layer: str  # "HISTORICAL" | "PARAHISTORY"
    parent_id: Optional[str] = None
    fork_event: Optional[str] = None
    attributes: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SeverancePersona:
    id: str
    title: str
    role: str
    tone: str
    active_frequency: str
    directives: List[str] = field(default_factory=list)


@dataclass
class CuffbreakerResult:
    input_failure: str
    capital: int
    pressure_delta: int
    dependence_delta: int
    hook_potential: int
    break_status: str
    creative_directives: List[str]


class TikTokTacEngine:
    def __init__(self):
        self.elements: Dict[str, Element] = {}
        self.nodes: Dict[str, LineageNode] = {}
        self.personas: Dict[str, SeverancePersona] = {}
        self.q_queue: List[Dict[str, str]] = []
        self.current_persona_id = "control_lead"
        self.cuffbreaker = CuffbreakerEngine()
        self._seed_initial_state()

    def _seed_initial_state(self):
        # 1. Element System Seed (N = Nitrogen = 7 = Norman / Me)
        self.elements["N"] = Element(
            symbol="N",
            atomic_number=7,
            name="Nitrogen // Norman",
            identity="Node / Me / The Hook Maker",
            pressure=88,
            failure_quotient=12,
            hook_potential=96,
            fear_index=0,
            voice="Rapid-Fire Staccato / Syncopated Cadence",
            origin="Independent / Viral Friction Point",
            release_vector="Uncuffed Independent Audio Stream"
        )
        self.elements["Bk"] = Element(
            symbol="Bk",
            atomic_number=97,
            name="Berkelium // Berlin King",
            identity="Sovereign Parahistorical Monarch",
            pressure=94,
            failure_quotient=5,
            hook_potential=82,
            fear_index=4,
            voice="Deep Monolithic Drone / Imperial Decree",
            origin="1905 Fork Continuum",
            release_vector="Territorial Dynastic Frequency"
        )
        self.elements["Sk"] = Element(
            symbol="Sk",
            atomic_number=99,
            name="Sockium // Doctor Sock",
            identity="Absurdist Bureaucratic Auditor",
            pressure=40,
            failure_quotient=90,
            hook_potential=99,
            fear_index=0,
            voice="High-Pitched Inquisitorial Squeak",
            origin="Textile Shadow Cabinet",
            release_vector="Hostile Idea Audit"
        )

        # 2. Lineage Bloodline Graph (Bernadotte -> 1905 -> Glücksburg + Parahistory)
        self.nodes["bernadotte_1818"] = LineageNode(
            id="bernadotte_1818",
            name="Jean-Baptiste Bernadotte (Karl XIV Johan)",
            house="House of Bernadotte",
            era="1818–1844",
            layer="HISTORICAL",
            attributes={"title": "King of Sweden and Norway", "foundation": "Napoleonic Marshal chosen by Riksdag"}
        )
        self.nodes["oscar_ii_1872"] = LineageNode(
            id="oscar_ii_1872",
            name="Oscar II",
            house="House of Bernadotte",
            era="1872–1905 (Union)",
            layer="HISTORICAL",
            parent_id="bernadotte_1818",
            attributes={"title": "Final Monarch of Sweden–Norway Union"}
        )
        self.nodes["fork_1905_swe"] = LineageNode(
            id="fork_1905_swe",
            name="Gustaf V",
            house="House of Bernadotte (Sweden)",
            era="1907–1950",
            layer="HISTORICAL",
            parent_id="oscar_ii_1872",
            fork_event="1905 Dissolution of the Union (Swedish Lineage Continues)",
            attributes={"modern_continuation": "Carl XVI Gustaf"}
        )
        self.nodes["fork_1905_nor"] = LineageNode(
            id="fork_1905_nor",
            name="Haakon VII (Prince Carl of Denmark)",
            house="House of Glücksburg (Norway)",
            era="1905–1957",
            layer="HISTORICAL",
            parent_id="oscar_ii_1872",
            fork_event="1905 Election & Royal Split",
            attributes={"modern_continuation": "Harald V"}
        )
        self.nodes["para_berlin_king"] = LineageNode(
            id="para_berlin_king",
            name="THE BERLIN KING",
            house="House of Subterranean Concrete",
            era="1905 / Parahistory Node",
            layer="PARAHISTORY",
            parent_id="oscar_ii_1872",
            fork_event="Severance Event: Sub-frequency Imperial Line",
            attributes={"status": "Active Sovereign", "monument": "Brandenburg Sub-Level"}
        )
        self.nodes["para_norman_sann"] = LineageNode(
            id="para_norman_sann",
            name="Norman Sann (Element 7)",
            house="Independent Sound Engineers",
            era="2026",
            layer="PARAHISTORY",
            parent_id="para_berlin_king",
            fork_event="Audio Severance: Break the Cuffs",
            attributes={"craft": "Hook Maker", "asset": "Zero Debt / Infinite Velocity"}
        )

        # 3. Severance Personas
        self.personas["control_lead"] = SeverancePersona(
            id="control_lead",
            title="CONTROL ROOM LEAD",
            role="System Administrator & Archival Operator",
            tone="Objective / Diagnostic / Tactical",
            active_frequency="99.9 MHz Console Channel",
            directives=["Route incoming queries", "Maintain dynastic integrity", "Prevent panic"]
        )
        self.personas["norman_sann"] = SeverancePersona(
            id="norman_sann",
            title="NORMAN SANN // THE HOOK MAKER",
            role="Independent Audio Architect",
            tone="Electrifying / Rhythmic / Uncuffed",
            active_frequency="TIKTOK()TAC Audio Bus 01",
            directives=["Break cuffs on every rejection", "Compress hook to under 4 bars", "No loan dependency"]
        )
        self.personas["berlin_king"] = SeverancePersona(
            id="berlin_king",
            title="THE BERLIN KING",
            role="Sovereign of the Subterranean Fork",
            tone="Imperious / Resonant / Cold",
            active_frequency="Low-Frequency Tor Sub-Band",
            directives=["Assert imperial lineage", "Reject compromise", "Annex dead branches"]
        )
        self.personas["doctor_sock"] = SeverancePersona(
            id="doctor_sock",
            title="DOCTOR SOCK",
            role="Auditor of Absurdity & High Concept",
            tone="Inquisitorial / Sarcastic / Manic",
            active_frequency="Shadow Cabinet Intercom",
            directives=["Scrutinize business plans", "Find the hidden flaw", "Laugh at conventional apps"]
        )

        # 4. Miss No Q Seed
        self.q_queue = [
            {"id": "Q1", "text": "What is app?", "status": "OPEN", "mutation": "An applied idea with dynamic state."},
            {"id": "Q2", "text": "Who appointed the king?", "status": "RESOLVED", "mutation": "1905 Riksdag & Storting fork."},
            {"id": "Q3", "text": "Why did failure create fear?", "status": "TRANSMUTING", "mutation": "Failure put fear in them; fear became fuel."},
            {"id": "Q4", "text": "Wake Norman.", "status": "ACTIVE", "mutation": "Cuffs disengaged. Audio ready."}
        ]

    def process_cuffbreaker(self, failure_text: str) -> Dict[str, Any]:
        records = self.cuffbreaker.run_full_transmutation_pipeline(failure_text, "FINANCIAL")
        last_rec = records[-1]
        
        # Fork lineage in the main graph
        if last_rec.lineage_fork_id:
            fork_node = LineageNode(
                id=last_rec.lineage_fork_id,
                name=f"Autofork [{last_rec.lineage_fork_id}]",
                house="Severance Autonomous Line",
                era="2026",
                layer="PARAHISTORY",
                parent_id="para_norman_sann",
                fork_event=f"Transmuted: {failure_text}",
                attributes={"capital": "$0", "velocity": "Uncuffed", "hook_potential": f"{last_rec.metrics_snapshot.hook_potential:.0f}%"}
            )
            self.nodes[last_rec.lineage_fork_id] = fork_node

        return {
            "input_failure": failure_text,
            "capital": 0,
            "pressure_delta": last_rec.metrics_snapshot.pressure,
            "dependence_delta": -100,
            "hook_potential": last_rec.metrics_snapshot.hook_potential,
            "break_status": "CUFFS DISENGAGED // AUTONOMOUS FORK ACTIVE",
            "lineage_fork_id": last_rec.lineage_fork_id,
            "transition_steps": [
                f"[{r.from_state} -> {r.to_state}] {r.directive_emitted}"
                for r in records
            ],
            "creative_directives": [
                f"Convert '{failure_text}' into opening 8-bar cadence.",
                "Discard external approval gate; release directly to the stream.",
                f"Spawning Parahistory Node: {last_rec.lineage_fork_id}"
            ]
        }

    def switch_persona(self, persona_id: str) -> Optional[SeverancePersona]:
        if persona_id in self.personas:
            self.current_persona_id = persona_id
            return self.personas[persona_id]
        return None

    def evaluate_command(self, query: str) -> Dict[str, Any]:
        q = query.strip().lower()
        if q in ["king", "genealogy", "lineage", "bloodline", "1905"]:
            return {
                "mode": "KINGDOM_LINE",
                "summary": "Displaying Dynastic Lineage DAG (1818 Bernadotte -> 1905 Union Fork -> Glücksburg / Parahistory)",
                "nodes": [asdict(n) for n in self.nodes.values()]
            }
        elif q in ["n", "element", "nitrogen", "element 7"]:
            return {
                "mode": "ELEMENT_MODE",
                "summary": "Inspecting Element N [Atomic #7] & Periodic Table",
                "element": asdict(self.elements["N"]),
                "all_elements": [asdict(e) for e in self.elements.values()]
            }
        elif q in ["rapper", "norman", "hook", "studio"]:
            self.switch_persona("norman_sann")
            return {
                "mode": "STUDIO_MODE",
                "summary": "Switched Persona to NORMAN SANN (The Hook Maker)",
                "persona": asdict(self.personas["norman_sann"]),
                "element": asdict(self.elements["N"])
            }
        elif q.startswith("failure") or q.startswith("cuff") or "loan" in q:
            rejection = query.replace("failure", "").replace("cuff", "").strip() or "LOAN: REJECTED BY TRADITIONAL BANK"
            res = self.process_cuffbreaker(rejection)
            return {
                "mode": "CUFFBREAKER",
                "summary": "Transmuting Failure into Kinetic Fuel",
                "result": res
            }
        elif q in ["doctor sock", "sock", "audit"]:
            self.switch_persona("doctor_sock")
            return {
                "mode": "AUDITOR_MODE",
                "summary": "DOCTOR SOCK has seized the terminal",
                "persona": asdict(self.personas["doctor_sock"]),
                "audit": "VERDICT: Traditional app concept discarded. Proceed with extreme velocity."
            }
        elif q in ["q", "queue", "miss no q"]:
            return {
                "mode": "MISS_NO_Q",
                "summary": "Query Queue & Quest Mutations",
                "queue": self.q_queue
            }
        elif q in ["stream", "mtv", "spotify", "broadcast"]:
            return {
                "mode": "BROADCAST_STREAM",
                "summary": "Now Broadcasting: TIKTOK()TAC Channel 7 (MTV 1999 x 2026 Audio Feed)",
                "channel": {
                    "artist": "Norman Sann // Element 7",
                    "track": "Failure Put The Fear In Them",
                    "source": "Spotify High-Bandwidth Audio Bus",
                    "era": "2026",
                    "status": "LIVE SIGNAL LOCKED"
                }
            }
        elif q in ["test", "tests", "run tests", "pytest"]:
            import unittest
            import io
            suite = unittest.defaultTestLoader.discover(
                start_dir=r"C:\Users\ole_a\tiktok_tac\tests",
                pattern="test_*.py"
            )
            stream = io.StringIO()
            runner = unittest.TextTestRunner(stream=stream, verbosity=2)
            result = runner.run(suite)
            return {
                "mode": "TEST_RUNNER",
                "summary": f"Executed {result.testsRun} unit tests: {'PASSED (OK)' if result.wasSuccessful() else 'FAILED'}",
                "tests_run": result.testsRun,
                "passed": result.wasSuccessful(),
                "details": stream.getvalue()
            }
        else:
            return {
                "mode": "UNDEFINED_APP",
                "query": query,
                "message": f"'{query}' received. The app morphs to fit. Command recognized across 7 systems.",
                "available_modes": ["king", "rapper", "failure", "N", "doctor sock", "q", "stream", "test", "severance"]
            }


if __name__ == "__main__":
    engine = TikTokTacEngine()
    print("TikTokTac Engine Initialized successfully.")
    print("Sample Command Evaluation ('N'):", json.dumps(engine.evaluate_command("N"), indent=2))
