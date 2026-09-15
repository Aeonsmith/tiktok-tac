"""
TIKTOK()TAC - OPTION A: TERMINAL / TUI CONTROL ROOM
High-velocity Phosphor Console with CRT Framing and Polymorphic Commands
"""

import sys
import os
import time

# Ensure core is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.engine import TikTokTacEngine

# ANSI Color Codes
G_BRIGHT = "\033[92m"
G_DIM = "\033[32m"
AMBER = "\033[33m"
CYAN = "\033[96m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_banner():
    print(f"{G_BRIGHT}")
    print(" ╔══════════════════════════════════════════════════════════════════════════════╗")
    print(" ║  ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗  ████████╗ █████╗  ██████╗  ║")
    print(" ║  ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝  ╚══██╔══╝██╔══██╗██╔════╝  ║")
    print(" ║     ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝ ()   ██║   ███████║██║       ║")
    print(" ║     ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗      ██║   ██╔══██║██║       ║")
    print(" ║     ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗     ██║   ██║  ██║╚██████╗  ║")
    print(" ║     ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝     ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ║")
    print(" ╠══════════════════════════════════════════════════════════════════════════════╣")
    print(f" ║  {AMBER}TAGLINE: WHAT IS APP? // NO PERMANENT DEFINITION // 7 SUB-SYSTEMS ACTIVE{G_BRIGHT}  ║")
    print(" ╚══════════════════════════════════════════════════════════════════════════════╝" + RESET)


def render_kingdom_line(nodes):
    print(f"\n{AMBER}{BOLD}[ === SYSTEM 01: KINGDOM LINE & PARAHISTORY GRAPH === ]{RESET}")
    print(f"{CYAN}Historical Fork Point: 1905 Dissolution of the Union (Bernadotte -> Glücksburg){RESET}\n")
    for n in nodes:
        layer_color = G_BRIGHT if n['layer'] == 'HISTORICAL' else MAGENTA
        print(f"  {layer_color}● [{n['layer']}] {BOLD}{n['name']}{RESET}")
        print(f"    ├─ House: {n['house']} | Era: {n['era']}")
        if n.get('fork_event'):
            print(f"    ├─ {RED}⚡ FORK: {n['fork_event']}{RESET}")
        if n.get('attributes'):
            for k, v in n['attributes'].items():
                print(f"    └─ {k.upper()}: {v}")
        print()


def render_element_mode(element, all_elements):
    print(f"\n{G_BRIGHT}{BOLD}[ === SYSTEM 02: PERIODIC ELEMENT INSPECTOR === ]{RESET}")
    print(f"{AMBER}Inspecting Active Node: {element['name']} [{element['symbol']} - #{element['atomic_number']}]{RESET}\n")
    print(f"  ┌────────────────────────────────────────────────────────────┐")
    print(f"  │  SYMBOL:  {BOLD}{element['symbol']:<4}{RESET}             ATOMIC #: {element['atomic_number']:<4}           │")
    print(f"  │  NAME:    {element['name']:<47} │")
    print(f"  │  IDENTITY:{element['identity']:<47} │")
    print(f"  ├────────────────────────────────────────────────────────────┤")
    print(f"  │  PRESSURE INDEX:   [{'█' * (element['pressure'] // 10):<10}] {element['pressure']:>3}%                      │")
    print(f"  │  HOOK POTENTIAL:   [{'█' * (element['hook_potential'] // 10):<10}] {element['hook_potential']:>3}%                      │")
    print(f"  │  FAILURE QUOTIENT: [{'█' * (element['failure_quotient'] // 10):<10}] {element['failure_quotient']:>3}%                      │")
    print(f"  │  FEAR INDEX:       [{'█' * (element['fear_index'] // 10):<10}] {element['fear_index']:>3}%                      │")
    print(f"  ├────────────────────────────────────────────────────────────┤")
    print(f"  │  VOICE CADENCE:   {element['voice']:<40} │")
    print(f"  │  RELEASE VECTOR:  {element['release_vector']:<40} │")
    print(f"  └────────────────────────────────────────────────────────────┘")


def render_cuffbreaker(res):
    print(f"\n{RED}{BOLD}[ === SYSTEM 05: CUFFBREAKER // FAILURE TRANSMUTATION === ]{RESET}")
    print(f"{AMBER}INPUT FAILURE:{RESET} {res['input_failure']}")
    print(f"  ├─ {CYAN}CAPITAL REQUIRED:{RESET}   ${res['capital']} (INDEPENDENT DISCHARGE)")
    print(f"  ├─ {G_BRIGHT}PRESSURE ACCELERATION:{RESET} +{res['pressure_delta']}")
    print(f"  ├─ {G_BRIGHT}DEPENDENCE DELTA:{RESET}      {res['dependence_delta']} (EXTERNAL VALIDATION NULLIFIED)")
    print(f"  ├─ {AMBER}HOOK POTENTIAL:{RESET}        {res['hook_potential']:.0f}% (MAX VELOCITY)")
    print(f"  └─ {BOLD}{MAGENTA}STATUS: {res['break_status']}{RESET}\n")
    
    if res.get('transition_steps'):
        print(f"{CYAN}STATE TRANSITION PIPELINE:{RESET}")
        for step in res['transition_steps']:
            print(f"   ↳ {step}")
        print()

    print(f"{CYAN}TACTICAL DIRECTIVES:{RESET}")
    for d in res['creative_directives']:
        print(f"   » {d}")


def render_broadcast_stream(channel):
    print(f"\n{MAGENTA}{BOLD}[ === SYSTEM 07: STREAM // MTV 1999 × SPOTIFY AUDIO BUS === ]{RESET}")
    print(f"  ┌────────────────────────────────────────────────────────────┐")
    print(f"  │  NOW BROADCASTING:  {BOLD}{channel['artist']:<37}{RESET} │")
    print(f"  │  TRACK:             {channel['track']:<37} │")
    print(f"  │  SOURCE:            {channel['source']:<37} │")
    print(f"  │  ERA / FREQUENCY:   {channel['era']:<37} │")
    print(f"  │  STATUS:            {G_BRIGHT}{channel['status']:<37}{RESET} │")
    print(f"  └────────────────────────────────────────────────────────────┘")


def main():
    engine = TikTokTacEngine()
    print_banner()
    print(f"{G_DIM}Type commands: 'king', 'n', 'rapper', 'failure [text]', 'doctor sock', 'q', 'stream', or 'exit'{RESET}\n")

    while True:
        try:
            prompt_str = f"{G_BRIGHT}WHAT IS APP? {AMBER}[{engine.current_persona_id}]{G_BRIGHT}> {RESET}"
            user_input = input(prompt_str).strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q!"]:
                print(f"{AMBER}Severing terminal connection. Lineages preserved.{RESET}")
                break

            result = engine.evaluate_command(user_input)
            mode = result.get("mode")

            if mode == "KINGDOM_LINE":
                render_kingdom_line(result["nodes"])
            elif mode == "ELEMENT_MODE":
                render_element_mode(result["element"], result["all_elements"])
            elif mode == "STUDIO_MODE":
                print(f"\n{G_BRIGHT}⚡ STUDIO ACTIVE: {result['persona']['title']}{RESET}")
                print(f"Directives: {', '.join(result['persona']['directives'])}")
                render_element_mode(result["element"], [])
            elif mode == "CUFFBREAKER":
                render_cuffbreaker(result["result"])
            elif mode == "AUDITOR_MODE":
                print(f"\n{RED}🧦 DOCTOR SOCK AUDIT TRIGGERED:{RESET}")
                print(f"{result['persona']['tone']} -> {result['audit']}")
            elif mode == "MISS_NO_Q":
                print(f"\n{CYAN}{BOLD}[ === SYSTEM 06: MISS NO Q // ACTIVE QUEUE === ]{RESET}")
                for item in result["queue"]:
                    print(f"  {AMBER}{item['id']}{RESET}: {item['text']} [{item['status']}] -> {G_BRIGHT}{item['mutation']}{RESET}")
            elif mode == "TEST_RUNNER":
                print(f"\n{G_BRIGHT}{BOLD}[ === UNIT TEST EXECUTION SUITE === ]{RESET}")
                status_color = G_BRIGHT if result["passed"] else RED
                print(f"Status: {status_color}{result['summary']}{RESET}\n")
                print(result["details"])
            elif mode == "BROADCAST_STREAM":
                render_broadcast_stream(result["channel"])
            else:
                print(f"\n{G_BRIGHT}↳ {result['message']}{RESET}")
                print(f"{CYAN}Recognized vectors:{RESET} {', '.join(result['available_modes'])}\n")

        except (KeyboardInterrupt, EOFError):
            print(f"\n{AMBER}Interrupted. Exiting control console.{RESET}")
            break


if __name__ == "__main__":
    main()
