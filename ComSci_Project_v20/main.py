from core.constants import *

def main():
    clear_screen()
    say_color("Welcome to the Temporal Calculation Facility!", YELLOW)

    state = "start"

    while True:
        if state == "start":
            print("\nWhere do you begin?")
            print("1 - Inspect the Primary Lever")
            print("2 - Talk to the Mechanical Squirrel")
            print("3 - Explore the Facility")
            print("4 - Push the Giant Red Button")
            print("E - Exit the facility")

            choice = input(PROMPT_SELECTION).strip().upper()

            if choice == "1":
                state = pull_lever()
            elif choice == "2":
                state = talk_to_squirrel()
            elif choice == "3":
                state = explore()
            elif choice == "4":
                state = game_over("You pushed the Giant Red Button.")
            elif choice == "E":
                say("\nYou leave the facility. Reality remains… mostly intact.")
                break
            else:
                print(ERROR_CHOICE_5)

        elif state == "explore":
            state = explore()

        elif state == "archives":
            state = visit_archives()

        elif state == "maintenance":
            state = visit_maintenance()

        elif state == "offices":
            state = visit_offices()

        elif state == "secret_room":
            state = enter_secret_room()

        elif state == "nuke_room":
            state = enter_nuke_room()

        elif state == "squirrel":
            state = talk_to_squirrel()

        elif state == "squirrel_help":
            say("\nThe squirrels take over the lever.")
            say("They do a much better job than you.")
            state = "start"

        elif state == "training":
            say("\nYou are sent to Temporal Safety Training.")
            say("There are many slides.")
            say("None of them explain anything.")
            state = "start"

        elif state == "coffee":
            say("\nYou drink the perfect cup of coffee.")
            say("Time stabilizes. Probably.")
            state = "start"

        elif state == "disco":
            say("\nA disco ball descends.")
            say("Squirrels begin synchronized dancing.")
            state = "start"

        elif state == "nuke_safe":
            say("\nThe failsafe shuts down.")
            say("Reality continues.")
            state = "start"

        elif state == "wrong_place":
            state = visit_wrong_place()

        elif state == "backrooms":
            state = enter_backrooms()

        else:
            print(RED + "❌ Unknown state. Returning to start." + RESET)
            state = "start"


if __name__ == "__main__":
    main()
