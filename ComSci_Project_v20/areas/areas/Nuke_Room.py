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
║      [ RED ]   [ BLUE ]   [ GREEN ]        ║
║                                            ║
╚════════════════════════════════════════════╝
""" + RESET)

    say_color("\n⚠ COUNTDOWN INITIATED ⚠", YELLOW)

    for number in range(10, 0, -1):
        print(RED + f"Countdown: {number}" + RESET)
        time.sleep(0.4)

    while True:
        print("\nWhich wire do you cut?")
        print("1 - Red")
        print("2 - Blue")
        print("3 - Green")
        print("4 - Let fate decide")

        choice = input(PROMPT_SELECTION).strip()

        if choice == "1":
            say("\nYou cut the RED wire.")
            say_color("The countdown stops.", GREEN)
            return "nuke_safe"
        elif choice == "2":
            say("\nYou cut the BLUE wire.")
            return game_over("The failsafe detonated.")
        elif choice == "3":
            say("\nYou cut the GREEN wire.")
            return game_over("The failsafe detonated in a very dramatic way.")
        elif choice == "4":
            say("\nYou step back.")
            say("You let fate decide.")
            if random.random() < 0.5:
                say_color("Somehow, the failsafe shuts down on its own.", GREEN)
                return "nuke_safe"
            else:
                return game_over("The device explodes in a very bureaucratic way.")
        else:
            print(ERROR_CHOICE_4)
