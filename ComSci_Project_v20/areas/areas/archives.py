from core.ui import (
    say,
    beep
)

from core.constants import (
    YELLOW,
    RESET,
    HEADER_ARCHIVES
)

from assets.ascii_art import (
    TELEPORT_BEAM_ART
)
def show_cycle_number():
    cycle = random.randint(1, 999999)

    print(SQUIRREL_ARCHIVE_ART_TOP)
    print(f"  The Number of the Cycle: {cycle:,}")
    print(SQUIRREL_ARCHIVE_ART_BOTTOM)


def find_cycle_number():
    say("\n🐿 You ask a nearby squirrel about the Number of the Cycle.")
    say("The squirrel freezes.")
    say("It slowly points toward a locked filing cabinet.")

    beep()

    say("\nThe cabinet unlocks.")
    say("Inside is another filing cabinet.")
    say("Inside that is a smaller filing cabinet.")
    say("Inside that is an even smaller filing cabinet.")
    say("You begin to question several design decisions.")

    fast_beep()

    say("\nThe final drawer opens dramatically.")
    say_color("A single piece of paper rests inside.", YELLOW)

    show_cycle_number()


def use_beam():
    say_color("\n✨ The Nondescript Teleporting Beam™ activates.", MAGENTA)

    say("A column of shimmering light surrounds you.")
    say("Your atoms file the correct paperwork.")
    say("Space folds like a poorly designed lawn chair.")
    say("Everything becomes extremely purple.")

    fast_beep()

    say("Your atoms politely rearrange themselves.")
    say_color("\n✨ TELEPORT COMPLETE", GREEN)

    say("You appear at the beginning of the facility.")


def inspect_beam():
    say("\nYou carefully inspect the machine.")
    print(TELEPORT_BEAM_ART)

    say("A metal plate is bolted to the machine.")
    say_color("'Definitely Not Evil Industries INC.'", CYAN)
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
        "Blueprints For Something Labeled 'ABSOLUTELY NOT A DEATH RAY'",
        "Squirrel Union Contract — 2027 Edition",
        "Temporal Peanut Butter Incident Report",
        "List of Forbidden Dance Moves",
        "Emergency Reality Glue Instructions",
        "Acorn-Based Encryption Manual",
        "Squirrel Propaganda Pamphlet",
        "Rubber Duck Census — Incomplete"
    ]

    say("\n🐿 You pull open a tiny filing cabinet.")
    found_file = random.choice(files)
    say_color(f"You find: '{found_file}'", YELLOW)

    if found_file == "Temporal Engine Warranty: VOID":
        say("Someone has written 'WHOOPS' across the document.")
    elif found_file == "Classified Squirrel Business":
        say("Every page just says 'NUTS' in increasingly large letters.")
    elif found_file == "Rubber Chicken Calibration Manual":
        say("The manual contains 847 pages.")
        say("All of them are diagrams of the same rubber chicken.")
    elif found_file == "Coffee Machine Repair Records":
        say("The coffee machine has caused seven temporal incidents.")
    elif found_file == "List of People Banned From Touching The Red Button":
        say("Your name has been added recently.")
    elif "DEATH RAY" in found_file:
        say("Someone has crossed out 'DEATH RAY' and written 'FLASHLIGHT.'")
    elif found_file == "Squirrel Union Contract — 2027 Edition":
        say("The contract demands 'More breaks, fewer paradoxes.'")
    elif found_file == "Temporal Peanut Butter Incident Report":
        say("The report simply says: 'Never again.'")
    elif found_file == "List of Forbidden Dance Moves":
        say("Someone has circled 'The Chrono-Shuffle' with red ink.")
    elif found_file == "Emergency Reality Glue Instructions":
        say("Step 1: Apply glue. Step 2: Hope.")
    elif found_file == "Acorn-Based Encryption Manual":
        say("The encryption key appears to be 'CRUNCH.'")
    elif found_file == "Squirrel Propaganda Pamphlet":
        say("'JOIN THE GREAT NUT UPRISING' is printed on the cover.")
    elif found_file == "Rubber Duck Census — Incomplete":
        say("The final page reads: 'We lost count after 400.'")
    else:
        say("You decide this information is probably useless.")


def visit_archives():
    say("\n📚 You enter the Squirrel Archives.")
    say("Thousands of tiny filing cabinets cover the walls.")
    say("The labels appear to have been written by squirrels.")
    say("Most of the documents concern acorn inventory.")

    say_color("\nSomething large hums behind a pile of boxes.", YELLOW)

    if random.random() < 0.20:
        say_color("\n✨ ARCHIVE ANOMALY DETECTED", MAGENTA)
        say("A filing cabinet opens on its own.")
        say("Inside is a mirror.")
        say("Your reflection whispers: 'Wrong timeline.'")

    while True:
        print(HEADER_ARCHIVES)
        print("1 - Search the archives")
        print("2 - Inspect the humming machine")
        print("3 - Use the humming machine")
        print("4 - Find the Number of the Cycle")
        print("5 - Leave the archives")

        choice = input(PROMPT_SELECTION).strip()

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
            print(ERROR_CHOICE_5)
