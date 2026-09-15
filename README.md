# TIKTOK()TAC — THE UNDEFINED APP

> **"WHAT IS APP?"**  
> *No permanent definition. The user defines what the machine becomes.*  
> **Core Principle:** *Failure doesn't close a branch. Failure forks it.*

---

## 1. Overview & Conceptual Metaphor

**TIKTOK()TAC** is a polymorphic concept engine, state machine, and audio-lineage workstation.

The application uses the historical **1905 union dissolution between Sweden and Norway** as its foundational metaphor:
* **The Historical Lineage:** The Swedish House of Bernadotte (founded in 1818 by French Marshal Jean-Baptiste Bernadotte / Karl XIV Johan) held a personal union with Norway until 1905. Upon dissolution, King Oscar II stepped down from Norway, and Norway elected Prince Carl of Denmark as **King Haakon VII**, establishing the modern Norwegian House of Glücksburg.
* **The Source Code Split:** 1905 represents the architectural split. Rejections, debt constraints, and project failures do not terminate progress—they act as **Severance Events** that spawn autonomous, zero-capital branches (**Parahistory**).

---

## 2. System Architecture

TIKTOK()TAC comprises 7 interconnected subsystems routed through a central polymorphic command processor:

```
                  ┌─────────────────────────────────────────┐
                  │      WHAT IS APP? (Command Router)      │
                  └────────────────────┬────────────────────┘
                                       │
    ┌────────────────┬─────────────────┼─────────────────┬────────────────┐
    │                │                 │                 │                │
┌───▼──────────┐ ┌───▼───────────┐ ┌───▼───────────┐ ┌───▼──────────┐ ┌───▼──────────┐
│ 01. KINGDOM  │ │ 02. ELEMENT   │ │ 03. SEVERANCE │ │ 05. CUFF-    │ │ 07. BROAD-   │
│     LINE DAG │ │     N [7]     │ │     SWITCH    │ │     BREAKER  │ │     CAST     │
└──────────────┘ └─────────────-─┘ └───────────────┘ └──────────────┘ └──────────────┘
```

### The 7 Subsystems

1. **01 // KINGDOM LINE (Bloodline & Parahistory DAG):**
   * **Historical Layer:** Tracks the line from 1818 Bernadotte &rarr; Oscar II &rarr; 1905 Union Split (Sweden: Gustaf V &rarr; Carl XVI Gustaf | Norway: Haakon VII &rarr; Harald V).
   * **Parahistory Layer:** Spawns autonomous nodes such as **THE BERLIN KING** and **Norman Sann (Element 7)**.
2. **02 // ELEMENT N (Periodic Identity Inspector):**
   * $\text{N} = \text{Nitrogen} = \text{Atomic \#7} = \text{Norman} = \text{Node} = \text{Me}$.
   * Metrics: Pressure Index, Hook Potential, Fear Index, Voice Cadence, and Release Vector.
3. **03 // SEVERANCE SWITCH:**
   * Isolates workspace contexts into distinct personas:
     * `Control Lead` (System Operator)
     * `Norman Sann // The Hook Maker` (Audio Architect)
     * `The Berlin King` (Subterranean Sovereign)
     * `Doctor Sock` (Shadow Auditor)
4. **04 // TIKTOK()TAC (Temporal Wheel):**
   * Dual-phase temporal engine: $\text{TIK (Present Moment / Social Velocity)} \rightarrow \text{TAC (Historical Parahistory)}$.
5. **05 // CUFFBREAKER (Failure-to-Fuel Transmutation Engine):**
   * Finite State Machine: $\text{BOUND} \rightarrow \text{CALCULATING} \rightarrow \text{SEVERED} \rightarrow \text{TRANSMUTED} \rightarrow \text{FORKED}$.
   * Converts rejection/financial hurdles into cadence, tempo (BPM), hook potential, and auto-generated DAG nodes.
6. **06 // MISS NO Q (Quest Queue):**
   * Persistent query/quest queue that mutates unanswered questions (`Q1` to `Q4`) rather than discarding them.
7. **07 // BROADCAST STREAM (MTV 1999 &times; 2026 Spotify):**
   * Audio bus visualizer and live stream monitor.

---

## 3. Directory Layout

```
tiktok_tac/
├── core/
│   ├── engine.py            # Primary polymorphic engine & CLI router
│   ├── cuffbreaker.py       # Cuffbreaker finite state machine & transmutation engine
│   └── CUFFBREAKER_API.md   # API specification and custom extension patterns
├── tui/
│   └── console.py           # Option A: Phosphor green / CRT terminal console
├── web/
│   └── index.html           # Option B: Graphical CRT control room dashboard
├── tests/
│   └── test_cuffbreaker.py  # Unit test suite for state transitions & guards
├── .github/
│   └── workflows/ci.yml     # Automated CI workflow
└── README.md                # Project architecture & documentation
```

---

## 4. Usage Instructions

### A. Live Production Web Dashboard
The web control room is deployed and publicly accessible on GitHub Pages:
* **Live URL:** [https://aeonsmith.github.io/tiktok-tac/](https://aeonsmith.github.io/tiktok-tac/)

### B. Interactive Terminal / TUI Console (Option A)
Launch the CRT console:
```powershell
python C:\Users\ole_a\tiktok_tac\tui\console.py
```

#### Interactive Commands:
* `king` or `1905` &mdash; Displays the Dynastic Bloodline DAG and 1905 union fork.
* `n` &mdash; Inspects **Element 7 [Nitrogen // Norman]** and real-time metrics.
* `failure [rejection text]` &mdash; Ingests failure into the Cuffbreaker engine and breaks constraints.
* `rapper` &mdash; Switches active persona to Norman Sann Studio.
* `doctor sock` &mdash; Triggers the shadow auditor.
* `q` &mdash; Views and mutates the Miss No Q query queue.
* `stream` &mdash; Locks onto the MTV 1999 &times; Spotify broadcast signal.
* `test` &mdash; Runs the embedded unit test suite.
* `exit` &mdash; Disengages console session.

### C. Local Web Control Room (Option B)
Open the standalone dashboard locally in any browser:
```powershell
Start-Process "C:\Users\ole_a\tiktok_tac\web\index.html"
```

### D. Programmatic Python API
Use the engine programmatically in your own scripts:

```python
from core.engine import TikTokTacEngine

engine = TikTokTacEngine()

# Evaluate polymorphic commands
res = engine.evaluate_command("failure LOAN APPLICATION REJECTED")
print(res["summary"])
print("Hook Potential:", res["result"]["hook_potential"])
print("Generated DAG Fork:", res["result"]["lineage_fork_id"])
```

---

## 5. Verification & Testing

### Running Unit Tests
Execute the test suite with verbose output:
```powershell
python -m unittest discover -s C:\Users\ole_a\tiktok_tac\tests -p "test_*.py" -v
```

### Running Production Smoke Tests
Verify the live web endpoint:
```powershell
$resp = Invoke-WebRequest -Uri "https://aeonsmith.github.io/tiktok-tac/" -UseBasicParsing
Write-Output "Status: $($resp.StatusCode)" # Expect 200
```
