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

        choice = input(PROMPT_SELECTION).strip()

        if choice == "1":
            say("\nYou press the left button.")
            say_color("SQUIRREL DOOMSDAY PROTOCOL ACTIVATED", RED)
            say("Mechanical squirrels swarm the room.")
            return game_over("Reality consumed by squirrels.")
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
            print(ERROR_CHOICE_5)

