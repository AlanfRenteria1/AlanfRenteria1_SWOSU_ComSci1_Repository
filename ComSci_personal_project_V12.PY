import datetime
import random
import time
import os


CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def say(text, delay=0.75):
    print(text)
    time.sleep(delay)


def beep():
    print("BEEP...")
    time.sleep(0.6)


def fast_beep():
    print("BEEP-BEEP-BEEP!")
    time.sleep(0.2)


def sound_alarm():
    print(RED + "WEEEOOO WEEEOOO WEEEOOO" + RESET)
    time.sleep(0.5)


def random_event():
    if random.random() > 0.25:
        return

    events = [
        "A temporal ripple passes through the room. Your hair grows 3 inches.",
        "A mechanical squirrel drops from the ceiling, salutes you, then leaves.",
        "Gravity flickers. You float for a moment before settling back down.",
        "A future version of you appears, whispers 'Don't trust the chicken,' then vanishes.",
        "A maintenance drone sprays you with lemon-scented coolant.",
        "Time loops for 3 seconds. You watch yourself blink twice.",
        "A coffee cup materializes in your hand. It is slightly ominous.",
        "A tiny wormhole opens and spits out a rubber duck.",
        "You hear distant chanting: 'ALL HAIL THE ENGINE.'",
        "A squirrel hands you a tiny wrench."
    ]

    event = random.choice(events)

    say(
        MAGENTA
        + f"\n✨ TEMPORAL ANOMALY: {event}"
        + RESET
    )


def show_time_and_date():
    now = datetime.datetime.now()

    print(CYAN + "\n╔════════════════════════════════════════════╗")
    print("║       TEMPORAL CALCULATION READOUT         ║")
    print("╠════════════════════════════════════════════╣" + RESET)
    print(f"  Date: {now.strftime('%A, %B %d, %Y')}")
    print(f"  Time: {now.strftime('%I:%M:%S %p')}")
    print(CYAN + "╚════════════════════════════════════════════╝" + RESET)


def show_cycle_number():
    cycle = random.randint(1, 999999)

    print(MAGENTA + "\n╔════════════════════════════════════════════╗")
    print("║          SQUIRREL ARCHIVE RECORD           ║")
    print("╠════════════════════════════════════════════╣" + RESET)
    print(f"  The Number of the Cycle: {cycle:,}")
    print(MAGENTA + "╚════════════════════════════════════════════╝" + RESET)


def find_cycle_number():
    say(
        "\n🐿 You ask a nearby squirrel about "
        "the Number of the Cycle."
    )

    say("The squirrel freezes.")
    say("It slowly points toward a locked filing cabinet.")

    beep()

    say("\nThe cabinet unlocks.")
    say("Inside is another filing cabinet.")
    say("You open that filing cabinet.")
    say("Inside is a much smaller filing cabinet.")
    say("You begin to question several design decisions.")

    fast_beep()

    say("\nThe final drawer opens dramatically.")

    say(
        YELLOW
        + "A single piece of paper rests inside."
        + RESET
    )

    show_cycle_number()


def use_beam():
    say(
        MAGENTA
        + "\n✨ The Nondescript Teleporting Beam™ activates."
        + RESET
    )

    say("A column of shimmering light surrounds you.")
    say("Your atoms file the correct paperwork.")
    say("Space folds like a poorly designed lawn chair.")
    say("Everything becomes extremely purple.")

    fast_beep()

    say("Your atoms politely rearrange themselves.")

    say(
        GREEN
        + "\n✨ TELEPORT COMPLETE"
        + RESET
    )

    say("You appear at the beginning of the facility.")


def inspect_beam():
    say("\nYou carefully inspect the machine.")

    print(MAGENTA + r"""
        ╔══════════════════════════════════╗
        ║                                  ║
        ║    NONDESCRIPT TELEPORTING       ║
        ║            BEAM™                 ║
        ║                                  ║
        ║          ┌─────────┐             ║
        ║          │   ???   │             ║
        ║          │   ⚡    │             ║
        ║          └────┬────┘             ║
        ║               │                  ║
        ║             \ │ /                ║
        ║              \│/                 ║
        ║               ▼                  ║
        ║             [ YOU ]              ║
        ║                                  ║
        ╚══════════════════════════════════╝
""" + RESET)

    say("A metal plate is bolted to the machine.")

    say(
        CYAN
        + "'Definitely Not Evil Industries INC.'"
        + RESET
    )

    say("'Model: NDB-9000'")
    say("'Safety Rating: Probably.'")
    say("'Do not use while existing.'")


def search_archives():
    files = [
        "ACORNS: Acceptable Sizes and Shapes",
        "Emergency Nut Storage Procedures",
        "Incident Report #482: The Ceiling Fan",
        "Why Humans Cannot Be Trusted With Levers",
        "Temporal Engine Warranty: VOID",
        "Classified Squirrel Business",
        "Rubber Chicken Calibration Manual",
        "Coffee Machine Repair Records",
        "List of People Banned From Touching The Red Button",
        "Blueprints For Something Labeled 'ABSOLUTELY NOT A DEATH RAY'"
    ]

    say("\n🐿 You pull open a tiny filing cabinet.")

    found_file = random.choice(files)

    say(
        YELLOW
        + f"You find: '{found_file}'"
        + RESET
    )

    if found_file == "Temporal Engine Warranty: VOID":
        say("Someone has written 'WHOOPS' across the document.")

    elif found_file == "Classified Squirrel Business":
        say(
            "Every page just says 'NUTS' "
            "in increasingly large letters."
        )

    elif found_file == "Rubber Chicken Calibration Manual":
        say("The manual contains 847 pages.")
        say("All of them are diagrams of the same rubber chicken.")

    elif found_file == "Coffee Machine Repair Records":
        say(
            "The coffee machine has apparently caused "
            "seven temporal incidents."
        )

    elif found_file == (
        "List of People Banned From Touching The Red Button"
    ):
        say("Your name has been added recently.")

    elif "DEATH RAY" in found_file:
        say(
            "Someone has crossed out 'DEATH RAY' "
            "and written 'FLASHLIGHT.'"
        )

    else:
        say("You decide this information is probably useless.")


def visit_archives():
    say("\n📚 You enter the Squirrel Archives.")
    say("Thousands of tiny filing cabinets cover the walls.")
    say("The labels appear to have been written by squirrels.")
    say("Most of the documents concern acorn inventory.")

    say(
        YELLOW
        + "\nSomething large hums behind a pile of boxes."
        + RESET
    )

    while True:
        print("\nSquirrel Archives")
        print("─────────────────")
        print("1 - Search the archives")
        print("2 - Inspect the humming machine")
        print("3 - Use the humming machine")
        print("4 - Find the Number of the Cycle")
        print("5 - Leave the archives")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            search_archives()

        elif choice == "2":
            inspect_beam()

        elif choice == "3":
            use_beam()
            return "start"

        elif choice == "4":
            find_cycle_number()

        elif choice == "5":
            say("\nYou leave the Squirrel Archives.")
            return "explore"

        else:
            print(
                RED
                + "❌ Choose 1, 2, 3, 4, or 5."
                + RESET
            )


def inspect_tool_wall():
    say(
        "\n🔧 You approach a wall covered in maintenance tools."
    )

    say("Every tool has a label.")
    say("None of the labels are helpful.")

    tools = [
        "Emergency Temporal Hammer",
        "Left-Handed Screwdriver",
        "Squirrel-Sized Wrench",
        "Quantum Plunger",
        "Backup Backup Hammer",
        "Pipe Encouragement Stick",
        "Absolutely Normal Crowbar"
    ]

    tool = random.choice(tools)

    say(
        YELLOW
        + f"\nYou pick up the '{tool}'."
        + RESET
    )

    say("You have no idea what you would use it for.")


def read_vapuration_warning():
    say(
        "\nYou wipe several years of dust off the warning label."
    )

    print(RED + r"""
╔════════════════════════════════════════════╗
║                  WARNING                   ║
╠════════════════════════════════════════════╣
║                                            ║
║   VAPURATION SYSTEM                        ║
║                                            ║
║   DO NOT PRESS WHILE STANDING HERE.        ║
║                                            ║
║   Seriously.                               ║
║                                            ║
║   We put the button somewhere else         ║
║   originally, but nobody could reach it.   ║
║                                            ║
╚════════════════════════════════════════════╝
""" + RESET)

    say("Someone has written underneath:")

    say(
        YELLOW
        + "'Surely they don't mean ME.'"
        + RESET
    )


def press_vapuration():
    say("\nYou press the VAPURATION button.")

    beep()

    say("Nothing happens.")

    time.sleep(1)

    say("Still nothing.")

    time.sleep(1)

    say("You begin to suspect the button is broken.")

    fast_beep()

    say(
        RED
        + "\n⚠ VAPURATION SEQUENCE STARTED ⚠"
        + RESET
    )

    say("Every valve in the room opens at once.")
    say("A completely unreasonable cloud of steam fills the room.")

    say(
        "For a brief moment, you regret several recent decisions."
    )

    say(
        RED
        + "\n♨ FWHOOSSSHHH! ♨"
        + RESET
    )

    say(
        RED
        + "\n💥 GAME OVER — You have been thoroughly Vapurationed."
        + RESET
    )

    return "game_over"


def inspect_steam_pipes():
    say("\n♨ You approach the Steam Pipe Control Area.")
    say("A maze of pipes covers the wall.")
    say("Gauges shake for reasons nobody bothered to document.")
    say("In the center is a large yellow button.")

    print(YELLOW + r"""
        ╔══════════════════════════════╗
        ║     STEAM PIPE CONTROL       ║
        ╠══════════════════════════════╣
        ║                              ║
        ║        ┌──────────┐          ║
        ║        │   !!!    │          ║
        ║        │ PRESS ME │          ║
        ║        └──────────┘          ║
        ║                              ║
        ║        VAPURATION            ║
        ║                              ║
        ╚══════════════════════════════╝
""" + RESET)

    while True:
        print("\nWhat do you do?")
        print("1 - Press VAPURATION")
        print("2 - Inspect the pipes")
        print("3 - Read the warning label")
        print("4 - Back away")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            return press_vapuration()

        elif choice == "2":
            say("\nYou inspect the pipes.")
            say("One pipe is marked 'STEAM.'")
            say("Another is marked 'MORE STEAM.'")
            say("The largest pipe is marked 'TOO MUCH STEAM.'")

        elif choice == "3":
            read_vapuration_warning()

        elif choice == "4":
            say(
                "\nYou make the unusual decision "
                "not to press the suspicious button."
            )

            return "maintenance"

        else:
            print(
                RED
                + "❌ Choose 1, 2, 3, or 4."
                + RESET
            )


def inspect_power_box():
    say("\n⚡ You approach the Maintenance Power Box.")
    say("It contains dozens of switches.")
    say("Most have sensible labels.")
    say("One does not.")

    print(BLUE + r"""
╔════════════════════════════════╗
║         POWER CONTROL          ║
╠════════════════════════════════╣
║                                ║
║ [ON]  Hallway Lights           ║
║ [ON]  Temporal Engine          ║
║ [ON]  Squirrel Archives        ║
║ [ON]  Coffee Machine           ║
║ [ON]  Teleporting Beam         ║
║ [???] Reality                  ║
║                                ║
╚════════════════════════════════╝
""" + RESET)

    say(
        "You decide the Reality switch is probably "
        "best left exactly where it is."
    )


def inspect_vent():
    say("\nYou crouch beside a maintenance vent.")
    say("Something moves inside.")

    time.sleep(1)

    say("Two tiny glowing eyes appear.")
    say("A mechanical squirrel crawls out.")
    say("It is wearing a miniature maintenance helmet.")
    say("It hands you a work order.")

    say(
        YELLOW
        + "\nWORK ORDER: Stop touching things."
        + RESET
    )

    say("The squirrel crawls back into the vent.")


def visit_maintenance():
    say("\n🔧 You enter the Maintenance Hall.")

    say(
        "Pipes, wires, gauges, and questionable machinery "
        "cover every wall."
    )

    say(
        "A loud metallic CLANK echoes somewhere above you."
    )

    random_event()

    while True:
        print("\nMaintenance Hall")
        print("────────────────")
        print("1 - Inspect the Steam Pipes")
        print("2 - Inspect the Tool Wall")
        print("3 - Inspect the Power Box")
        print("4 - Inspect the Maintenance Vent")
        print("5 - Return to the Exploration Wing")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            result = inspect_steam_pipes()

            if result == "game_over":
                return "game_over"

        elif choice == "2":
            inspect_tool_wall()

        elif choice == "3":
            inspect_power_box()

        elif choice == "4":
            inspect_vent()

        elif choice == "5":
            say("\nYou leave the Maintenance Hall.")
            return "explore"

        else:
            print(
                RED
                + "❌ Choose 1, 2, 3, 4, or 5."
                + RESET
            )


def show_title():
    clear_screen()

    print(CYAN + r"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║      THE RUBE GOLDBERG TEMPORAL CALCULATION ENGINE           ║
║                                                              ║
║         A Choose-Your-Own-Rube-Goldberg Adventure            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""" + RESET)

    say(
        YELLOW
        + "Welcome to the Temporal Calculation Facility."
        + RESET
    )

    say(
        "A place where time is stabilized using absurd machinery."
    )

    say("Mechanical squirrels maintain the systems.")
    say("You are here to activate the Temporal Engine.")

    say(
        "Or accidentally destroy the universe. No pressure."
    )


def get_start_choice():
    print("\nWhere do you begin?")
    print("────────────────────")
    print("1 - Inspect the Primary Lever")
    print("2 - Talk to the Mechanical Squirrel")
    print("3 - Explore the Facility")
    print("4 - Push the Giant Red Button")
    print("E - Exit the facility")

    while True:
        choice = input("\nSelection: ").strip().upper()

        if choice in ("1", "2", "3", "4", "E"):
            return choice

        print(
            RED
            + "❌ Choose 1, 2, 3, 4, or E."
            + RESET
        )


def pull_lever():
    say("\n⚙ You approach the Primary Lever.")
    say("It hums with temporal energy.")
    say("A small display flickers to life.")

    show_time_and_date()

    say(
        "\nA plaque reads: "
        "'WARNING: Lever may cause time implosions.'"
    )

    random_event()

    while True:
        print("\nWhat do you do?")
        print("1 - Pull the lever")
        print("2 - Tap the lever")
        print("3 - Ask the squirrel for help")
        print("4 - Inspect the Temporal Calculation Readout")
        print("5 - Step away from the lever")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            say("\nYou yank the lever.")
            say("The Temporal Engine roars to life!")

            return "win"

        elif choice == "2":
            say("\nYou tap the lever.")
            say("It barely moves.")
            say("A squirrel sighs loudly.")

            return "squirrel_help"

        elif choice == "3":
            return "squirrel"

        elif choice == "4":
            say(
                "\nYou inspect the Temporal Calculation Readout."
            )

            show_time_and_date()

        elif choice == "5":
            say(
                "\nYou wisely step away from the suspicious lever."
            )

            return "start"

        else:
            print(
                RED
                + "❌ Choose 1, 2, 3, 4, or 5."
                + RESET
            )


def talk_to_squirrel():
    say("\n🐿 The Mechanical Squirrel looks at you.")
    say("'Clearance code?' it chitters.")

    random_event()

    print("\nWhat do you say?")
    print("1 - Say today's weekday")
    print("2 - Admit you have no clearance")
    print("3 - Offer a rubber chicken")
    print("4 - Ask about secret rooms")
    print("5 - Ask about the Squirrel Archives")

    while True:
        choice = input("\nSelection: ").strip()

        if choice == "1":
            day = datetime.datetime.now().strftime("%A")

            say(
                f"\nYou whisper: '{day}'."
            )

            say(
                "'Correct. Temporal clearance granted.'"
            )

            return "win"

        elif choice == "2":
            say(
                "\nYou admit that you have no clearance."
            )

            say(
                "'Honesty protocol accepted.'"
            )

            return "training"

        elif choice == "3":
            say(
                "\nYou present the rubber chicken."
            )

            say(
                "'THE SACRED CHICKEN OF CALIBRATION!'"
            )

            return "squirrel_help"

        elif choice == "4":
            say("\nThe squirrel leans closer.")
            say("'There is a secret room.'")
            say("'One button makes coffee.'")
            say("'The other ends everything.'")

            return "secret_room"

        elif choice == "5":
            say(
                "\nThe squirrel points down the hall."
            )

            say(
                "'Archives. Third door. Watch out for the beam.'"
            )

            return "archives"

        else:
            print(
                RED
                + "❌ Choose 1, 2, 3, 4, or 5."
                + RESET
            )


def explore():
    say(
        "\n🏢 You enter the Facility Exploration Wing."
    )

    random_event()

    while True:
        print("\nWhere do you go?")
        print("1 - Squirrel Archives")
        print("2 - Maintenance Hall")
        print("3 - Secret Room")
        print("4 - Nuclear Failsafe Chamber")
        print("5 - Return to the lobby")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            return "archives"

        elif choice == "2":
            return "maintenance"

        elif choice == "3":
            return "secret_room"

        elif choice == "4":
            return "nuke_room"

        elif choice == "5":
            return "start"

        else:
            print(
                RED
                + "❌ Choose 1, 2, 3, 4, or 5."
                + RESET
            )


def enter_secret_room():
    say("\n🔴 You enter the Secret Room.")
    say("Two enormous red buttons sit on a pedestal.")
    say("'Choose wisely. Time depends on it.'")

    random_event()

    while True:
        print("\nWhat do you do?")
        print("1 - Press the left button")
        print("2 - Press the right button")
        print("3 - Ask the squirrel for help")
        print("4 - Leave")
        print("5 - (Hidden option)")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            say("\nYou press the left button.")

            say(
                RED
                + "⚠ SQUIRREL DOOMSDAY PROTOCOL ACTIVATED ⚠"
                + RESET
            )

            say(
                "Mechanical squirrels swarm the room."
            )

            say(
                RED
                + "\n💥 GAME OVER — Reality consumed by squirrels."
                + RESET
            )

            return "game_over"

        elif choice == "2":
            say("\nYou press the right button.")
            say("A hatch opens.")
            say("☕ A perfect cup of coffee rises.")

            return "coffee"

        elif choice == "3":
            say("\n🐿 The squirrel appears.")
            say("'One ends time. One makes coffee.'")
            say("'Good luck.'")

        elif choice == "4":
            return "explore"

        elif choice == "5":
            say("\n✨ A disco ball descends.")
            say("Squirrels begin synchronized dancing.")

            return "disco"

        else:
            print(
                RED
                + "❌ Choose 1, 2, 3, 4, or 5."
                + RESET
            )


def enter_nuke_room():
    clear_screen()
    sound_alarm()

    say(
        "\n🚪 You enter the Nuclear Failsafe Chamber."
    )

    say(
        "A dangerous device sits in the center of the room."
    )

    print(RED + r"""
        ╔══════════════════════════════╗
        ║      ☢  FAILSAFE DEVICE  ☢  ║
        ╠══════════════════════════════╣
        ║   [RED]   [BLUE]   [GREEN]  ║
        ║    ───     ───      ───     ║
        ╚══════════════════════════════╝
    """ + RESET)

    say(
        YELLOW
        + "⚠ 'COUNTDOWN INITIATED.'"
        + RESET
    )

    for number in range(10, 0, -1):
        print(
            RED
            + f"⏳ Countdown: {number}"
            + RESET
        )

        time.sleep(0.4)

    print("\nWhich wire do you cut?")
    print("1 - Red")
    print("2 - Blue")
    print("3 - Green")
    print("4 - Let fate decide")

    while True:
        choice = input("\nSelection: ").strip()

        if choice == "1":
            say("\n✂ You cut the RED wire.")

            say(
                GREEN
                + "The countdown stops."
                + RESET
            )

            return "nuke_safe"

        elif choice == "2":
            say("\n✂ You cut the BLUE wire.")

            say(
                RED
                + "💥 GAME OVER"
                + RESET
            )

            return "game_over"

        elif choice == "3":
            say("\n✂ You cut the GREEN wire.")

            say(
                RED
                + "💥 GAME OVER"
                + RESET
            )

            return "game_over"

        elif choice == "4":
            say("\nYou step back.")
            say("The machine considers your decision.")

            if random.choice([True, False]):
                say(
                    GREEN
                    + "It shuts itself down."
                    + RESET
                )

                return "nuke_safe"

            say(
                RED
                + "💥 Fate has made its decision."
                + RESET
            )

            return "game_over"

        else:
            print(
                RED
                + "❌ Choose 1, 2, 3, or 4."
                + RESET
            )


def show_ending(result):
    if result == "win":
        say(
            GREEN
            + "\n🎉 SUCCESS!"
            + RESET
        )

        say(
            "The Temporal Engine stabilizes time."
        )

    elif result == "training":
        say(
            "\nYou complete the training simulation."
        )

        say(
            "The squirrel gives you a tiny thumbs-up."
        )

    elif result == "squirrel_help":
        say(
            "\n🐿 The squirrel takes control."
        )

        say(
            GREEN
            + "The Temporal Engine activates flawlessly!"
            + RESET
        )

    elif result == "coffee":
        say(
            GREEN
            + "\n☕ You drink the Coffee of Temporal Enlightenment."
            + RESET
        )

        say(
            "You now understand quantum tax law."
        )

    elif result == "disco":
        say("\n💃🐿 The squirrels dance.")
        say("You dance.")
        say("Time itself appears to dance.")

        say(
            GREEN
            + "This is the best possible ending."
            + RESET
        )

    elif result == "nuke_safe":
        say(
            GREEN
            + "\n🎉 The failsafe is shut down!"
            + RESET
        )

        say(
            "Temporal stability is restored."
        )


def get_end_choice():
    print(
        CYAN
        + "\n══════════════════════════════════════════"
        + RESET
    )

    print(
        YELLOW
        + "       TEMPORAL ENGINE CONTROL PANEL"
        + RESET
    )

    print(
        CYAN
        + "══════════════════════════════════════════"
        + RESET
    )

    print("R - Restart")
    print("E - Exit")

    while True:
        choice = input("\nSelection: ").strip().upper()

        if choice in ("R", "E"):
            return choice

        print(
            RED
            + "❌ Choose R or E."
            + RESET
        )


def shut_down():
    print()

    say(
        YELLOW
        + "⚠ TEMPORAL ENGINE SHUTDOWN REQUESTED"
        + RESET
    )

    say("Saving current timeline...")
    say("Returning mechanical squirrels to storage...")
    say("Closing miniature wormholes...")

    beep()

    say("Accounting for all rubber ducks...")

    fast_beep()

    say("Turning off Giant Red Buttons...")
    say("Deactivating Nondescript Teleporting Beam™...")
    say("Checking universe integrity...")

    say(
        GREEN
        + "\n✓ UNIVERSE STILL EXISTS"
        + RESET
    )

    say(
        GREEN
        + "✓ TEMPORAL ENGINE OFFLINE"
        + RESET
    )

    say(
        GREEN
        + "✓ SQUIRRELS ACCOUNTED FOR"
        + RESET
    )

    print()

    say(
        CYAN
        + "Thank you for visiting the "
        "Temporal Calculation Facility."
        + RESET
    )

    say(
        MAGENTA
        + "Definitely Not Evil Industries INC."
        + RESET
    )

    input(
        "\nPress ENTER to close the program..."
    )


def play_game():
    while True:
        choice = get_start_choice()

        if choice == "1":
            result = pull_lever()

        elif choice == "2":
            result = talk_to_squirrel()

        elif choice == "3":
            result = explore()

        elif choice == "4":
            say(
                "\n🔴 You slam the Giant Red Button."
            )

            say(
                "Temporal reality collapses instantly."
            )

            say(
                RED
                + "\n💥 GAME OVER — Catastrophic impatience."
                + RESET
            )

            return "game_over"

        elif choice == "E":
            return "exit"

        while True:
            if result == "start":
                break

            elif result == "squirrel":
                result = talk_to_squirrel()

            elif result == "archives":
                result = visit_archives()

            elif result == "maintenance":
                result = visit_maintenance()

            elif result == "explore":
                result = explore()

            elif result == "secret_room":
                result = enter_secret_room()

            elif result == "nuke_room":
                result = enter_nuke_room()

            elif result in (
                "win",
                "training",
                "squirrel_help",
                "coffee",
                "disco",
                "nuke_safe",
                "game_over"
            ):
                show_ending(result)
                return result

            else:
                break


def reset_game():
    clear_screen()

    say(
        MAGENTA
        + "♻ Rewinding timeline..."
        + RESET
    )

    say("Resetting squirrels...")
    say("Putting all the furniture back...")
    say("Removing evidence of prior squirrel incidents...")

    say(
        GREEN
        + "✓ TEMPORAL RESET COMPLETE"
        + RESET
    )

    time.sleep(1)


def main():
    while True:
        show_title()

        result = play_game()

        if result == "exit":
            shut_down()
            return

        choice = get_end_choice()

        if choice == "E":
            shut_down()
            return

        reset_game()


if __name__ == "__main__":
    main()