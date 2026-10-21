import datetime

from assets.ascii_art import (
    TEMPORAL_READOUT_ART
)

from core.ui import say

def pull_lever():
    say("\nYou approach the Primary Lever.")
    say("It hums with temporal energy.")
    say("A plaque reads: WARNING: Lever may cause time implosions.")

    random_event()

    while True:
        print("\nPrimary Lever")
        print("─────────────")
        print("1 - Pull the lever")
        print("2 - Tap the lever")
        print("3 - Ask the squirrel for help")
        print("4 - Inspect the Temporal Calculation Readout")
        print("5 - Step away from the lever")

        choice = input(PROMPT_SELECTION).strip()

        if choice == "1":
            say("\nYou yank the lever.")
            say("The Temporal Engine roars to life!")
            say_color("Reality stabilizes. Probably.", GREEN)
            input("\nPress ENTER to return to the facility...")
            return "start"
        elif choice == "2":
            say("\nYou tap the lever.")
            say("It barely moves.")
            say("A squirrel sighs loudly.")
            return "squirrel_help"
        elif choice == "3":
            return "squirrel"
        elif choice == "4":
            say("\nA small display flickers to life.")
            show_time_and_date()
        elif choice == "5":
            say("\nYou wisely step away from the suspicious lever.")
            return "start"
        else:
            print(ERROR_CHOICE_5)

