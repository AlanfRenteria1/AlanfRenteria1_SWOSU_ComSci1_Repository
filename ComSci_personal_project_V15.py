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
        "A squirrel hands you a tiny wrench.",
        "You feel eyes on the back of your head for just a moment."
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
    say(CYAN + "'Definitely Not Evil Industries INC.'" + RESET)
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

    say(
        YELLOW
        + f"You find: '{found_file}'"
        + RESET
    )

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
        say(
            "Someone has crossed out 'DEATH RAY' "
            "and written 'FLASHLIGHT.'"
        )

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

    say(
        YELLOW
        + "\nSomething large hums behind a pile of boxes."
        + RESET
    )

    if random.random() < 0.20:
        say(MAGENTA + "\n✨ ARCHIVE ANOMALY DETECTED" + RESET)
        say("A filing cabinet opens on its own.")
        say("Inside is a mirror.")
        say("Your reflection whispers: 'Wrong timeline.'")

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
            print(RED + "❌ Choose 1, 2, 3, 4, or 5." + RESET)


def inspect_tool_wall():
    say("\n🔧 You approach a wall covered in maintenance tools.")
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
    say("\nYou wipe several years of dust off the warning label.")

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
    say("For a brief moment, you regret several recent decisions.")

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
            return "maintenance"

        else:
            print(RED + "❌ Choose 1, 2, 3, or 4." + RESET)


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

    say("You decide not to touch the Reality switch.")


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

    say("A loud metallic CLANK echoes somewhere above you.")

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
            print(RED + "❌ Choose 1, 2, 3, 4, or 5." + RESET)


def search_cubicles():
    say("\n🖥 You wander through the rows of cubicles.")
    say("Every desk looks almost exactly the same.")

    items = [
        "a mug labeled 'WORLD'S OKAYEST TEMPORAL ENGINEER'",
        "a calculator displaying the number 7",
        "a sticky note that says 'DO NOT RESET REALITY AGAIN'",
        "a tiny framed photograph of a mechanical squirrel",
        "an unopened box labeled 'EMERGENCY PAPERCLIPS'",
        "a keyboard missing the Escape key",
        "a completely ordinary stapler",
        "a memo titled 'PLEASE STOP FEEDING THE VENTS'",
        "a desk phone with no buttons",
        "a rubber duck wearing an employee badge",
        "a sticky note that says 'THE DUCK KNOWS'",
        "a tiny portal labeled 'DO NOT TAP'",
        "a USB drive labeled 'ABSOLUTELY NOT EVIL'",
        "a keyboard with only the Q key remaining",
        "a binder titled 'REALITY PATCH NOTES'",
        "a glowing acorn sitting on a velvet pillow"
    ]

    item = random.choice(items)

    say(
        YELLOW
        + f"\nYou find {item}."
        + RESET
    )

    if item == "a sticky note that says 'THE DUCK KNOWS'":
        say("You look around. No ducks. Probably.")

    elif item == "a tiny portal labeled 'DO NOT TAP'":
        say("You tap it. A small hand taps back.")

    elif item == "a USB drive labeled 'ABSOLUTELY NOT EVIL'":
        say("You decide not to plug it in. Wise.")

    elif item == "a keyboard with only the Q key remaining":
        say("You press Q. Somewhere, something screams.")

    elif item == "a binder titled 'REALITY PATCH NOTES'":
        say("'Version 3.1: Fixed bug where gravity forgot to happen.'")

    elif item == "a glowing acorn sitting on a velvet pillow":
        say("It hums softly. You feel judged.")


def visit_meeting_area():
    say("\n📋 You enter the meeting area.")
    say("A long table is surrounded by twelve identical chairs.")
    say("A whiteboard covers one wall.")
    say("Someone has drawn a complicated flowchart.")

    print(CYAN + r"""
        TEMPORAL ENGINE MEETING NOTES

                  Problem
                     |
                     v
              Schedule Meeting
                     |
                     v
               Discuss Problem
                     |
                     v
           Schedule Another Meeting
                     |
                     v
            Forget Original Problem
                     |
                     v
                  SUCCESS?
""" + RESET)

    while True:
        print("\nMeeting Area")
        print("────────────")
        print("1 - Sit in the important chair")
        print("2 - Inspect the whiteboard")
        print("3 - Return to the offices")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            say("\nYou sit at the head of the table.")
            say("You immediately feel qualified to schedule meetings.")
            say("No actual knowledge has been gained.")

        elif choice == "2":
            say("\nYou inspect the whiteboard.")
            say(
                YELLOW
                + "'ACTION ITEM: Determine what an action item is.'"
                + RESET
            )

        elif choice == "3":
            return

        else:
            print(RED + "❌ Choose 1, 2, or 3." + RESET)


def use_coffee_machine():
    say("\n☕ You approach the office coffee machine.")
    say("Its control panel contains far too many buttons.")

    drinks = [
        "Coffee",
        "Decaf Coffee",
        "Slightly More Coffee",
        "Employee Motivation",
        "Brown Liquid",
        "Mystery",
        "Tuesday"
    ]

    drink = random.choice(drinks)

    beep()

    say(f"The machine selects: {drink}.")
    say("A paper cup drops into place.")
    say("The machine makes several expensive-sounding noises.")
    say("The cup fills with something technically drinkable.")

    say(
        GREEN
        + "You decide this counts as coffee."
        + RESET
    )


def use_microwave():
    say("\nYou inspect the microwave.")
    say("Someone has left 00:01 on the timer.")
    say("Nobody knows how long it has been there.")

    while True:
        print("\nWhat do you do?")
        print("1 - Clear the timer")
        print("2 - Leave it alone")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            beep()
            say("\nYou press CLEAR.")
            say(GREEN + "The office is finally at peace." + RESET)
            return

        elif choice == "2":
            say("\nYou leave the 00:01 untouched.")
            say("Somewhere, an employee becomes irrationally annoyed.")
            return

        else:
            print(RED + "❌ Choose 1 or 2." + RESET)


def inspect_fridge():
    say("\n🧊 You open the office refrigerator.")
    say("Cold air rolls dramatically across the floor.")

    items = [
        "a sandwich labeled 'DO NOT EAT - STEVE'",
        "seventeen identical yogurt cups",
        "a lunchbox secured with a tiny padlock",
        "a bottle labeled 'TEMPORAL MILK - EXPIRES YESTERDAY'",
        "half of a birthday cake",
        "a single pickle on a paper plate",
        "an unreasonably large wheel of cheese",
        "a takeout container labeled 'DO NOT OPEN IN THIS TIMELINE'"
    ]

    item = random.choice(items)

    say(
        YELLOW
        + f"\nInside you find {item}."
        + RESET
    )

    say("You quietly close the refrigerator.")


def visit_break_area():
    say("\n☕ You enter the office break area.")
    say("There are two coffee machines, a microwave, and a refrigerator.")
    say("A small table occupies the center of the room.")

    while True:
        print("\nBreak Area")
        print("──────────")
        print("1 - Use the coffee machine")
        print("2 - Inspect the microwave")
        print("3 - Open the refrigerator")
        print("4 - Return to the offices")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            use_coffee_machine()

        elif choice == "2":
            use_microwave()

        elif choice == "3":
            inspect_fridge()

        elif choice == "4":
            return

        else:
            print(RED + "❌ Choose 1, 2, 3, or 4." + RESET)


def interact_printer():
    say("\n🖨 You approach the office printer.")
    say("It vibrates slightly, as if preparing to be difficult.")

    while True:
        print("\nPrinter Menu")
        print("────────────")
        print("1 - Try to print a document")
        print("2 - Check the paper tray")
        print("3 - Check the toner")
        print("4 - Politely ask it to cooperate")
        print("5 - Back away")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            say("\nYou press PRINT.")
            fast_beep()
            say(RED + "The printer prints a blank page." + RESET)
            say("It prints another blank page.")
            say("It prints a third blank page labeled 'HAHAHA'.")
            say("The printer is clearly mocking you.")

        elif choice == "2":
            say("\nYou open the paper tray.")
            say("It is full of paper.")
            say("The printer begins flashing 'OUT OF PAPER.'")

        elif choice == "3":
            say("\nYou check the toner.")
            say("It is completely full.")
            say("The printer begins flashing 'TONER EMPTY.'")

        elif choice == "4":
            say("\nYou politely ask the printer to cooperate.")
            beep()
            say("The printer prints a single sheet of paper.")
            say(YELLOW + "'NO.'" + RESET)

        elif choice == "5":
            say("\nYou back away from the printer.")
            say("It prints a page that says 'COWARD.'")
            return

        else:
            print(RED + "❌ Choose 1, 2, 3, 4, or 5." + RESET)


def squirrel_recovery():
    say("\n🐿 You ask the squirrel for help.")
    say("The squirrel sighs.")
    say("It pulls a tiny radio from its tool belt.")
    say("'Another wall clip,' it says.")
    say("'Office sector.'")
    say("'Yes. Again.'")

    beep()

    say("\nA purple light appears above you.")

    say(
        MAGENTA
        + "The Nondescript Teleporting Beam™ locks onto your position."
        + RESET
    )

    say("Reality snaps back into place.")
    say(GREEN + "\nYou are returned to the Offices." + RESET)


def visit_wrong_place():
    say("\nEverything around you is an endless gray void.")
    say("Parts of the facility float in the distance.")
    say("You can see the back sides of walls.")
    say("A chair hangs upside down several hundred feet above you.")
    say("A mechanical squirrel walks past on an invisible floor.")
    say("It stops.")
    say("It looks at you.")
    say("You look at it.")
    say("Neither of you knows what to do about this.")

    while True:
        print("\nThe Wrong Place")
        print("───────────────")
        print("1 - Walk toward the floating door")
        print("2 - Touch the strange gray floor")
        print("3 - Ask the squirrel for help")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            say("\nYou walk toward the floating door.")
            say("The door moves away at exactly the same speed.")
            say("You stop.")
            say("The door stops.")
            say("The door is clearly doing this on purpose.")

        elif choice == "2":
            say("\nYou touch the gray floor.")
            say("For some reason, it makes an error sound.")
            print(BLUE + "\n*DUN*" + RESET)
            say("Reality appears mildly embarrassed.")

        elif choice == "3":
            squirrel_recovery()
            return "offices"

        else:
            print(RED + "❌ Choose 1, 2, or 3." + RESET)


def enter_backrooms():
    say("\nYou expect to fall into the gray void.")
    say("You don't.")

    time.sleep(1)

    say(YELLOW + "\nThe world suddenly becomes yellow." + RESET)
    say("Your feet land on an old carpet.")
    say("The office is gone.")
    say("The facility is gone.")
    say("Even the gray void is gone.")

    print(YELLOW + r"""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║       │              │              │                ║
║       │              │              │                ║
║───────┘              └──────────────┘                ║
║                                                      ║
║               ┌─────────────┐                        ║
║               │             │                        ║
║        ───────┘             └──────────              ║
║                                                      ║
║    │                      │                          ║
║    │                      │                          ║
║    └────────────          └───────────────           ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
""" + RESET)

    say("Endless empty rooms stretch in every direction.")
    say("The fluorescent lights make an endless hum.")
    say("Every hallway looks almost exactly like the last.")

    say("\nYou turn around.")

    time.sleep(1)

    say("The wall you came through is gone.")

    beep()

    say("\nYou try to contact the facility.")
    say("Nothing answers.")
    say("You try to contact the mechanical squirrels.")
    say("Nothing answers.")

    fast_beep()

    say(RED + "\n⚠ TELEPORTATION SIGNAL LOST ⚠" + RESET)
    say(RED + "⚠ FACILITY COORDINATES NOT FOUND ⚠" + RESET)
    say(RED + "⚠ CURRENT REALITY NOT RECOGNIZED ⚠" + RESET)

    time.sleep(1)

    say("\nYou start walking.")
    say("The rooms continue.")
    say("And continue.")
    say("And continue.")

    say(
        RED
        + "\n💥 GAME OVER — You clipped into the wrong reality."
        + RESET
    )

    return "game_over"


def leave_reality():
    destination = random.choice(["backrooms", "wrong_place"])

    if destination == "backrooms":
        return enter_backrooms()

    return visit_wrong_place()


def clip_through_wall():
    say("\nYou press your hand against the suspicious wall.")
    say("Your hand passes straight through it.")

    time.sleep(1)

    say("That is probably not supposed to happen.")

    while True:
        print("\nWhat do you do?")
        print("1 - Step through the wall")
        print("2 - Back away")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            say("\nYou carefully step forward.")
            say("For half a second, everything looks normal.")

            fast_beep()

            say(
                MAGENTA
                + "\n⚠ REALITY COLLISION ERROR ⚠"
                + RESET
            )

            say("The office vanishes.")
            say("The floor also vanishes.")

            return leave_reality()

        elif choice == "2":
            say("\nYou pull your hand out of the wall.")
            say("You decide that solid objects should remain solid.")
            return "offices"

        else:
            print(RED + "❌ Choose 1 or 2." + RESET)


def inspect_office_wall():
    say("\nYou inspect the wall beside Cubicle 47.")
    say("Something about it looks wrong.")
    say("The paint does not quite meet the floor.")

    say(
        "From the correct angle, you can see "
        "a thin line of absolute nothing."
    )

    return clip_through_wall()


def visit_offices():
    say("\n🏢 You enter the Offices.")
    say("The sudden normality is unsettling.")
    say("Rows of gray cubicles stretch across the room.")
    say("Computer monitors glow quietly on empty desks.")
    say("There is a meeting area near the windows.")

    say(
        "A break area sits beneath a sign reading "
        "'EMPLOYEE WELLNESS ZONE.'"
    )

    say("Nobody appears to be working.")

    random_event()

    if random.random() < 0.15:
        say(MAGENTA + "\n✨ OFFICE ANOMALY DETECTED" + RESET)
        say("A printer turns on by itself.")
        say("It prints a single sheet of paper.")
        say(YELLOW + "'STOP LOOKING AT ME.'" + RESET)

    while True:
        print("\nOffices")
        print("───────")
        print("1 - Explore the cubicles")
        print("2 - Visit the meeting area")
        print("3 - Visit the break area")
        print("4 - Inspect a strange part of the wall")
        print("5 - Interact with the printer")
        print("6 - Return to the Exploration Wing")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            search_cubicles()

        elif choice == "2":
            visit_meeting_area()

        elif choice == "3":
            visit_break_area()

        elif choice == "4":
            result = inspect_office_wall()

            if result == "game_over":
                return "game_over"

        elif choice == "5":
            interact_printer()

        elif choice == "6":
            say("\nYou leave the Offices.")
            return "explore"

        else:
            print(RED + "❌ Choose 1, 2, 3, 4, 5, or 6." + RESET)


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

    say(YELLOW + "Welcome to the Temporal Calculation Facility." + RESET)
    say("A place where time is stabilized using absurd machinery.")
    say("Mechanical squirrels maintain the systems.")
    say("You are here to activate the Temporal Engine.")
    say("Or accidentally destroy the universe. No pressure.")


def get_start_choice():
    print("\nWhere do you begin?\n")
    print("1 - Inspect the Primary Lever")
    print("2 - Talk to the Mechanical Squirrel")
    print("3 - Explore the Facility")
    print("4 - Push the Giant Red Button")
    print("E - Exit the facility")

    while True:
        choice = input("\nSelection: ").strip().upper()
        if choice in ("1", "2", "3", "4", "E"):
            return choice
        print(RED + "❌ Choose 1, 2, 3, 4, or E." + RESET)


def pull_lever():
    say("\nYou approach the Primary Lever.")
    say("It hums with temporal energy.")

    say(
        "A plaque reads: "
        "'WARNING: Lever may cause time implosions.'"
    )

    random_event()

    while True:
        print("\nPrimary Lever")
        print("─────────────")
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
            say("\nA small display flickers to life.")
            show_time_and_date()

        elif choice == "5":
            say("\nYou wisely step away from the suspicious lever.")
            return "start"

        else:
            print(RED + "❌ Choose 1, 2, 3, 4, or 5." + RESET)


def talk_to_squirrel():
    say("\nThe Mechanical Squirrel looks at you.")
    say("'Clearance code?' it chitters.")

    random_event()

    while True:
        print("\nWhat do you say?")
        print("1 - Say today's weekday")
        print("2 - Admit you have no clearance")
        print("3 - Offer a rubber chicken")
        print("4 - Ask about secret rooms")
        print("5 - Ask about the Squirrel Archives")
        print("6 - Leave the squirrel alone")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            day = datetime.datetime.now().strftime("%A")
            say(f"\nYou whisper: '{day}'.")
            say("Correct. Temporal clearance granted.")
            return "win"

        elif choice == "2":
            say("\nYou admit that you have no clearance.")
            say("'Honesty protocol accepted.'")
            return "training"

        elif choice == "3":
            say("\nYou present the rubber chicken.")
            say("'THE SACRED CHICKEN OF CALIBRATION!'")
            return "squirrel_help"

        elif choice == "4":
            say("\nThe squirrel leans closer.")
            say("There is a secret room.")
            say("One button makes coffee.")
            say("The other ends everything.")
            return "secret_room"

        elif choice == "5":
            say("\nThe squirrel points down the hall.")
            say("Archives. Third door. Watch out for the beam.")
            return "archives"

        elif choice == "6":
            return "start"

        else:
            print(RED + "❌ Choose 1, 2, 3, 4, 5, or 6." + RESET)


def explore():
    say("\nYou enter the Facility Exploration Wing.")
    random_event()

    while True:
        print("\nWhere do you go?")
        print("1 - Squirrel Archives")
        print("2 - Maintenance Hall")
        print("3 - Offices")
        print("4 - Secret Room")
        print("5 - Nuclear Failsafe Chamber")
        print("6 - Return to the lobby")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            return "archives"

        elif choice == "2":
            return "maintenance"

        elif choice == "3":
            return "offices"

        elif choice == "4":
            return "secret_room"

        elif choice == "5":
            return "nuke_room"

        elif choice == "6":
            return "start"

        else:
            print(RED + "❌ Choose 1, 2, 3, 4, 5, or 6." + RESET)


def enter_secret_room():
    say("\nYou enter the Secret Room.")
    say("Two enormous red buttons sit on a pedestal.")
    say("Choose wisely. Time depends on it.")

    random_event()

    while True:
        print("\nSecret Room")
        print("───────────")
        print("1 - Press the left button")
        print("2 - Press the right button")
        print("3 - Ask the squirrel for help")
        print("4 - Leave")
        print("5 - (Hidden option)")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            say("\nYou press the left button.")
            say(RED + "⚠ SQUIRREL DOOMSDAY PROTOCOL ACTIVATED ⚠" + RESET)
            say("Mechanical squirrels swarm the room.")
            say(
                RED
                + "\n💥 GAME OVER — Reality consumed by squirrels."
                + RESET
            )
            return "game_over"

        elif choice == "2":
            say("\nYou press the right button.")
            say("A hatch opens.")
            say("A perfect cup of coffee rises.")
            return "coffee"

        elif choice == "3":
            say("\nThe squirrel appears.")
            say("One ends time. One makes coffee.")
            say("Good luck.")

        elif choice == "4":
            return "explore"

        elif choice == "5":
            say("\nA disco ball descends.")
            say("Squirrels begin synchronized dancing.")
            return "disco"

        else:
            print(RED + "❌ Choose 1, 2, 3, 4, or 5." + RESET)


def enter_nuke_room():
    clear_screen()
    sound_alarm()

    say("\nYou enter the Nuclear Failsafe Chamber.")
    say("A very suspicious failsafe device sits in the center of the room.")

    print(RED + r"""
╔════════════════════════════════════════════╗
║              FAILSAFE DEVICE               ║
╠════════════════════════════════════════════╣
║                                            ║
║           [ RED ] [ BLUE ] [ GREEN ]       ║
║                                            ║
╚════════════════════════════════════════════╝
""" + RESET)

    say(YELLOW + "\n⚠ COUNTDOWN INITIATED ⚠" + RESET)

    for number in range(10, 0, -1):
        print(RED + f"Countdown: {number}" + RESET)
        time.sleep(0.4)

    while True:
        print("\nWhich wire do you cut?")
        print("1 - Red")
        print("2 - Blue")
        print("3 - Green")
        print("4 - Let fate decide")

        choice = input("\nSelection: ").strip()

        if choice == "1":
            say("\nYou cut the RED wire.")
            say(GREEN + "The countdown stops." + RESET)
            return "nuke_safe"

        elif choice == "2":
            say("\nYou cut the BLUE wire.")
            say(RED + "💥 GAME OVER" + RESET)
            return "game_over"

        elif choice == "3":
            say("\nYou cut the GREEN wire.")
            say(RED + "💥 GAME OVER" + RESET)
            return "game_over"

        elif choice == "4":
            say("\nYou step back.")
            say("You let fate decide.")
            if random.random() < 0.5:
                say(GREEN + "Somehow, the failsafe shuts down on its own." + RESET)
                return "nuke_safe"
            else:
                say(RED + "The device explodes in a very bureaucratic way." + RESET)
                return "game_over"

        else:
            print(RED + "❌ Choose 1, 2, 3, or 4." + RESET)


def show_ending(result):
    clear_screen()

    if result == "win":
        say(GREEN + "\n✨ The Temporal Engine stabilizes reality." + RESET)
        say("Mechanical squirrels applaud politely.")
        say("Time continues, mostly on schedule.")

    elif result == "training":
        say("\nYou are sent to Temporal Safety Training.")
        say("There are many slides.")
        say("None of them explain anything.")

    elif result == "squirrel_help":
        say("\nThe squirrels take over the lever.")
        say("They do a much better job than you.")
        say("You are reassigned to 'Button Observation.'")

    elif result == "coffee":
        say("\nYou drink the perfect cup of coffee.")
        say("Time itself appears to dance.")
        say(GREEN + "This is the best possible ending." + RESET)

    elif result == "disco":
        say("\nYou join the squirrels in synchronized disco.")
        say("Reality remains unstable, but stylish.")

    elif result == "nuke_safe":
        say(GREEN + "\nThe failsafe is shut down!" + RESET)
        say("Temporal stability is restored.")

    elif result == "game_over":
        say(RED + "\n💥 GAME OVER" + RESET)

    else:
        say("\nThe timeline shrugs. Nobody is sure what happened.")


def get_end_choice():
    print(CYAN + "\nTEMPORAL ENGINE CONTROL PANEL" + RESET)
    print(YELLOW + "R - Restart" + RESET)
    print(YELLOW + "E - Exit" + RESET)

    while True:
        choice = input("\nSelection: ").strip().upper()

        if choice in ("R", "E"):
            return choice

        print(RED + "❌ Choose R or E." + RESET)


def shut_down():
    print()

    say(YELLOW + "⚙ TEMPORAL ENGINE SHUTDOWN REQUESTED" + RESET)

    say("Saving current timeline...")
    say("Returning mechanical squirrels to storage...")
    say("Closing miniature wormholes...")

    beep()

    say("Accounting for all rubber ducks...")

    fast_beep()

    say("Turning off Giant Red Buttons...")
    say("Deactivating Nondescript Teleporting Beam™...")
    say("Checking universe integrity...")

    say(GREEN + "\n✔ UNIVERSE STILL EXISTS" + RESET)
    say(GREEN + "✔ TEMPORAL ENGINE OFFLINE" + RESET)
    say(GREEN + "✔ SQUIRRELS ACCOUNTED FOR" + RESET)

    print()

    say(
        CYAN
        + "Thank you for visiting the Temporal Calculation Facility."
        + RESET
    )

    say(
        MAGENTA
        + "Definitely Not Evil Industries INC."
        + RESET
    )

    input("\nPress ENTER to close the program...")


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
            say("\nYou slam the Giant Red Button.")
            say("Temporal reality collapses instantly.")
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

            elif result == "offices":
                result = visit_offices()

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

    say(MAGENTA + "\nRewinding timeline..." + RESET)
    say("Resetting squirrels...")
    say("Putting all the furniture back...")
    say("Returning office walls to Euclidean space...")
    say("Checking for missing employees...")
    say("Ignoring several missing employees...")
    say("Removing evidence of prior squirrel incidents...")

    say(
        GREEN
        + "\n✔ TEMPORAL RESET COMPLETE"
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
