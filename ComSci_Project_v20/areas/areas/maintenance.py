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
    say_color(f"\nYou pick up the '{tool}'.", YELLOW)
    say("You have no idea what you would use it for.")


def read_vapuration_warning():
    say("\nYou wipe several years of dust off the warning label.")
    print(VAPURATION_WARNING_ART)
    say("Someone has written underneath:")
    say_color("'Surely they don't mean ME.'", YELLOW)


def game_over(message):
    say_color("\n💥 GAME OVER — " + message, RED)
    input("\nPress ENTER to return to the facility...")
    return "start"


def press_vapuration():
    say("\nYou press the VAPURATION button.")
    beep()
    say("Nothing happens.")
    time.sleep(1)
    say("Still nothing.")
    time.sleep(1)
    say("You begin to suspect the button is broken.")

    fast_beep()
    say_color("\n⚠ VAPURATION SEQUENCE STARTED ⚠", RED)

    say("Every valve in the room opens at once.")
    say("A completely unreasonable cloud of steam fills the room.")
    say("For a brief moment, you regret several recent decisions.")

    say_color("\n♨ FWHOOSSSHHH! ♨", RED)
    return game_over("You have been thoroughly Vapurationed.")


def inspect_steam_pipes():
    say("\n♨ You approach the Steam Pipe Control Area.")
    say("A maze of pipes covers the wall.")
    say("Gauges shake for reasons nobody bothered to document.")
    say("In the center is a large yellow button.")

    print(STEAM_PIPE_ART)

    while True:
        print("\nWhat do you do?")
        print("1 - Press VAPURATION")
        print("2 - Inspect the pipes")
        print("3 - Read the warning label")
        print("4 - Back away")

        choice = input(PROMPT_SELECTION).strip()

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
            print(ERROR_CHOICE_4)


def inspect_power_box():
    say("\n⚡ You approach the Maintenance Power Box.")
    say("It contains dozens of switches.")
    say("Most have sensible labels.")
    say("One does not.")
    print(POWER_BOX_ART)
    say("You decide not to touch the Reality switch.")


def inspect_vent():
    say("\nYou crouch beside a maintenance vent.")
    say("Something moves inside.")
    time.sleep(1)
    say("Two tiny glowing eyes appear.")
    say("A mechanical squirrel crawls out.")
    say("It is wearing a miniature maintenance helmet.")
    say("It hands you a work order.")
    say_color("\nWORK ORDER: Stop touching things.", YELLOW)
    say("The squirrel crawls back into the vent.")


def visit_maintenance():
    say("\n🔧 You enter the Maintenance Hall.")
    say("Pipes, wires, gauges, and questionable machinery cover every wall.")
    say("A loud metallic CLANK echoes somewhere above you.")

    random_event()

    while True:
        print(HEADER_MAINTENANCE)
        print("1 - Inspect the Steam Pipes")
        print("2 - Inspect the Tool Wall")
        print("3 - Inspect the Power Box")
        print("4 - Inspect the Maintenance Vent")
        print("5 - Return to the Exploration Wing")

        choice = input(PROMPT_SELECTION).strip()

        if choice == "1":
            result = inspect_steam_pipes()
            if result == "game_over":
                return "start"
            else:
                return result
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
            print(ERROR_CHOICE_5)

