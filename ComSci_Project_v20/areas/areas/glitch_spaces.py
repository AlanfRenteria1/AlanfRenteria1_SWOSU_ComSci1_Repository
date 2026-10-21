def squirrel_recovery():
    say("\n🐿 You ask the squirrel for help.")
    say("The squirrel sighs.")
    say("It pulls a tiny radio from its tool belt.")
    say("'Another wall clip,' it says.")
    say("'Office sector.'")
    say("'Yes. Again.'")

    beep()

    say("\nA purple light appears above you.")
    say_color("The Nondescript Teleporting Beam™ locks onto your position.", MAGENTA)
    say("Reality snaps back into place.")
    say_color("\nYou are returned to the Offices.", GREEN)


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
        print(HEADER_WRONG_PLACE)
        print("1 - Walk toward the floating door")
        print("2 - Touch the strange gray floor")
        print("3 - Ask the squirrel for help")

        choice = input(PROMPT_SELECTION).strip()

        if choice == "1":
            say("\nYou walk toward the floating door.")
            say("The door moves away at exactly the same speed.")
            say("You stop.")
            say("The door stops.")
            say("The door is clearly doing this on purpose.")
        elif choice == "2":
            say("\nYou touch the strange gray floor.")
            say("For some reason, it makes an error sound.")
            print(BLUE + "\n*DUN*" + RESET)
            say("Reality appears mildly embarrassed.")
        elif choice == "3":
            squirrel_recovery()
            return "offices"
        else:
            print(ERROR_CHOICE_3)


def enter_backrooms():
    say("\nYou expect to fall into the gray void.")
    say("You don't.")
    time.sleep(1)

    say_color("\nThe world suddenly becomes yellow.", YELLOW)
    say("Your feet land on an old carpet.")
    say("The office is gone.")
    say("The facility is gone.")
    say("Even the gray void is gone.")

    print(BACKROOMS_ART)

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
    say_color("\n⚠ TELEPORTATION SIGNAL LOST ⚠", RED)
    say_color("⚠ FACILITY COORDINATES NOT FOUND ⚠", RED)
    say_color("⚠ CURRENT REALITY NOT RECOGNIZED ⚠", RED)

    time.sleep(1)

    say("\nYou start walking.")
    say("The rooms stretch on endlessly.")
    say("Your footsteps echo strangely, as if the floor is reconsidering its existence.")
    time.sleep(1)

    say_color("\n💥 GAME OVER — You clipped into the wrong reality.", RED)
    input("\nPress ENTER to return to the facility...")
    return "start"
