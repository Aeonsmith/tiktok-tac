# TIKTOK()TAC — THE UNDEFINED APP

> **"WHAT IS APP?"**  
> *No permanent definition. The user defines what the machine becomes.*  
> **Core Principle:** *Failure doesn't close a branch. Failure forks it.*

---

## Overview

**TIKTOK()TAC** is a polymorphic concept engine, state machine, and audio-lineage workstation. Built upon the historical 1905 union dissolution between Sweden (House of Bernadotte) and Norway (House of Glücksburg), the application treats historical splits as the root metaphor: **rejections and failures fork lineages rather than terminating them**.

---

## System Architecture

The application comprises 7 interconnected subsystems:

```
                  ┌─────────────────────────────────────┐
                  │    WHAT IS APP? (Command Router)    │
                  └──────────────────┬──────────────────┘
                                     │
    ┌────────────────┬───────────────┼───────────────┬────────────────┐
    │                │               │               │                │
┌───▼──────────┐ ┌───▼─────────┐ ┌───▼─────────┐ ┌───▼─────────┐ ┌───▼─────────┐
│ 01. KINGDOM  │ │ 02. ELEMENT │ │ 03. SEVER   │ │ 05. CUFF-   │ │ 07. BROAD-  │
│     LINE DAG │ │     N (ME)  │ │     SWITCH  │ │     BREAKER │ │     CAST    │
└──────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘
```

1. **01 // KINGDOM LINE (Bloodline Graph):**
   * Real historical lineage: 1818 Jean-Baptiste Bernadotte (Karl XIV Johan) &rarr; Oscar II &rarr; 1905 Union Fork (Sweden: Gustaf V &rarr; Carl XVI Gustaf | Norway: Haakon VII &rarr; Harald V).
   * Parahistory layer: Spawns sovereign branches such as **THE BERLIN KING** and **Norman Sann (Element 7)**.
2. **02 // ELEMENT N (Periodic Identity Inspector):**
   * $\text{N} = \text{Nitrogen} = 7 = \text{Norman} = \text{Node} = \text{Me}$.
   * Metrics: Pressure Index, Hook Potential, Fear Index, Voice Cadence, and Release Vector.
3. **03 // SEVERANCE SWITCH:**
   * Isolates active personas (`Control Lead`, `Norman Sann // The Hook Maker`, `The Berlin King`, `Doctor Sock`).
4. **04 // TIKTOK()TAC TEMPORAL WHEEL:**
   * Temporal cycle: $\text{TIK (Present)} \rightarrow \text{TAC (History)}$.
5. **05 // CUFFBREAKER (Failure-to-Fuel Transmutation Engine):**
   * State Machine: $\text{BOUND} \rightarrow \text{CALCULATING} \rightarrow \text{SEVERED} \rightarrow \text{TRANSMUTED} \rightarrow \text{FORKED}$.
   * Automatically nullifies dependence, computes kinetic pressure, and generates Parahistory DAG nodes.
6. **06 // MISS NO Q:**
   * Dynamic question / quest mutation queue (`Q1` to `Q4`).
7. **07 // BROADCAST STREAM (MTV 1999 &times; 2026 Spotify):**
   * Live visualizer and audio bus monitor.

---

## Project Structure

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
└── README.md                # Project architecture & documentation
```

---

## Getting Started

### 1. Terminal / TUI Console (Option A)
Run the interactive CRT console:
```powershell
python C:\Users\ole_a\tiktok_tac\tui\console.py
```
* Commands: `king`, `n`, `rapper`, `failure [text]`, `doctor sock`, `q`, `stream`, `test`, `exit`.

### 2. Graphical Web Dashboard (Option B)
Open the standalone control room in your default browser:
```powershell
Start-Process "C:\Users\ole_a\tiktok_tac\web\index.html"
```

### 3. Running Unit Tests
Execute the test suite directly:
```powershell
python -m unittest discover -s C:\Users\ole_a\tiktok_tac\tests -p "test_*.py" -v
```
Or execute inside the TUI console by typing `test`.
