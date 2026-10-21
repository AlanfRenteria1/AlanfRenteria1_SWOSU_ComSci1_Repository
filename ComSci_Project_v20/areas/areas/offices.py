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
    say_color(f"\nYou find {item}.", YELLOW)

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
    print(MEETING_NOTES_ART)

    while True:
        print(HEADER_MEETING)
        print("1 - Sit in the important chair")
        print("2 - Inspect the whiteboard")
        print("3 - Return to the offices")

        choice = input(PROMPT_SELECTION).strip()

        if choice == "1":
            say("\nYou sit at the head of the table.")
            say("You immediately feel qualified to schedule meetings.")
            say("No actual knowledge has been gained.")
        elif choice == "2":
            say("\nYou inspect the whiteboard.")
            say_color("'ACTION ITEM: Determine what an action item is.'", YELLOW)
        elif choice == "3":
            return
        else:
            print(ERROR_CHOICE_3)


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
    say_color("You decide this counts as coffee.", GREEN)


def use_microwave():
    say("\nYou inspect the microwave.")
    say("Someone has left 00:01 on the timer.")
    say("Nobody knows how long it has been there.")

    while True:
        print("\nWhat do you do?")
        print("1 - Clear the timer")
        print("2 - Leave it alone")

        choice = input(PROMPT_SELECTION).strip()

        if choice == "1":
            beep()
            say("\nYou press CLEAR.")
            say_color("The office is finally at peace.", GREEN)
            return
        elif choice == "2":
            say("\nYou leave the 00:01 untouched.")
            say("Somewhere, an employee becomes irrationally annoyed.")
            return
        else:
            print(ERROR_CHOICE_2)


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
    say_color(f"\nInside you find {item}.", YELLOW)
    say("You quietly close the refrigerator.")


def visit_break_area():
    say("\n☕ You enter the office break area.")
    say("There are two coffee machines, a microwave, and a refrigerator.")
    say("A small table occupies the center of the room.")

    while True:
        print(HEADER_BREAK_AREA)
        print("1 - Use the coffee machine")
        print("2 - Inspect the microwave")
        print("3 - Open the refrigerator")
        print("4 - Return to the offices")

        choice = input(PROMPT_SELECTION).strip()

        if choice == "1":
            use_coffee_machine()
        elif choice == "2":
            use_microwave()
        elif choice == "3":
            inspect_fridge()
        elif choice == "4":
            return
        else:
            print(ERROR_CHOICE_4)


def interact_printer():
    say("\n🖨 You approach the office printer.")
    say("It vibrates slightly, as if preparing to be difficult.")

    while True:
        print(HEADER_PRINTER)
        print("1 - Try to print a document")
        print("2 - Check the paper tray")
        print("3 - Check the toner")
        print("4 - Politely ask it to cooperate")
        print("5 - Back away")

        choice = input(PROMPT_SELECTION).strip()

        if choice == "1":
            say("\nYou press PRINT.")
            fast_beep()
            say_color("The printer prints a blank page.", RED)
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
            say_color("'NO.'", YELLOW)
        elif choice == "5":
            say("\nYou back away from the printer.")
            say("It prints a page that says 'COWARD.'")
            return
        else:
            print(ERROR_CHOICE_5)

def inspect_office_wall():
    say("\nYou inspect the wall beside Cubicle 47.")
    say("Something about it looks wrong.")
    say("The paint does not quite meet the floor.")
    say("From the correct angle, you can see a thin line of absolute nothing.")
    return clip_through_wall()


def clip_through_wall():
    say("\nYou press your hand against the suspicious wall.")
    say("Your hand passes straight through it.")
    time.sleep(1)
    say("That is probably not supposed to happen.")

    while True:
        print("\nWhat do you do?")
        print("1 - Step through the wall")
        print("2 - Back away")

        choice = input(PROMPT_SELECTION).strip()

        if choice == "1":
            say("\nYou carefully step forward.")
            say("For half a second, everything looks normal.")
            fast_beep()
            say_color("\n⚠ REALITY COLLISION ERROR ⚠", MAGENTA)
            say("The office vanishes.")
            say("The floor also vanishes.")
            destination = random.choice(["backrooms", "wrong_place"])
            if destination == "backrooms":
                return "backrooms"
            else:
                return "wrong_place"
        elif choice == "2":
            say("\nYou pull your hand out of the wall.")
            say("You decide that solid objects should remain solid.")
            return "offices"
        else:
            print(ERROR_CHOICE_2)

def visit_offices():
    say("\nYou enter the Offices.")
    say("The sudden normality is unsettling.")
    say("Rows of gray cubicles stretch across the room.")
    say("Computer monitors glow quietly on empty desks.")
    say("There is a meeting area near the windows.")
    say("A break area sits beneath a sign reading 'EMPLOYEE WELLNESS ZONE.'")
    say("Nobody appears to be working.")

    random_event()

    if random.random() < 0.15:
        say_color("\n✨ OFFICE ANOMALY DETECTED", MAGENTA)
        say("A printer turns on by itself.")
        say("It prints a single sheet of paper.")
        say_color("STOP LOOKING AT ME.", YELLOW)

    while True:
        print("\nOffices")
        print("────────")
        print("1 - Explore the cubicles")
        print("2 - Visit the meeting area")
        print("3 - Visit the break area")
        print("4 - Inspect a strange part of the wall")
        print("5 - Interact with the printer")
        print("6 - Return to the Exploration Wing")

        choice = input(PROMPT_SELECTION).strip()

        if choice == "1":
            search_cubicles()
        elif choice == "2":
            visit_meeting_area()
        elif choice == "3":
            visit_break_area()
        elif choice == "4":
            result = inspect_office_wall()
            if result == "backrooms":
                return "backrooms"
            elif result == "wrong_place":
                return "wrong_place"
        elif choice == "5":
            interact_printer()
        elif choice == "6":
            say("\nYou leave the Offices.")
            return "explore"
        else:
            print(ERROR_CHOICE_5)
