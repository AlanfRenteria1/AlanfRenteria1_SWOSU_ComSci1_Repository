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


def talk_to_squirrel():
    say("\nThe Mechanical Squirrel looks at you.")
    say("Clearance code?' it chitters.")

    random_event()

    while True:
        print("\nWhat do you say?")
        print("1 - Say today's weekday")
        print("2 - Admit you have no clearance")
        print("3 - Offer a rubber chicken")
        print("4 - Ask about secret rooms")
        print("5 - Ask about the Squirrel Archives")
        print("6 - Leave the squirrel alone")

        choice = input(PROMPT_SELECTION).strip()

        if choice == "1":
            day = datetime.datetime.now().strftime("%A")
            say(f"\nYou whisper: '{day}'.")
            say("Correct. Temporal clearance granted.")
            say_color("The Temporal Engine stabilizes reality.", GREEN)
            input("\nPress ENTER to return to the facility...")
            return "start"
        elif choice == "2":
            say("\nYou admit that you have no clearance.")
            say("Honesty protocol accepted.")
            return "training"
        elif choice == "3":
            say("\nYou present the rubber chicken.")
            say("THE SACRED CHICKEN OF CALIBRATION!")
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
            print(ERROR_CHOICE_5)

