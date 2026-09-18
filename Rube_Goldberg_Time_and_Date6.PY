# ============================================================
#        THE RUBE GOLDBERG TEMPORAL CALCULATION ENGINE
# ============================================================

import datetime
import random
import time
import os

# ANSI Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def dramatic_pause(message, delay=0.75):
    print(message)
    time.sleep(delay)


def machine_run():

    clear_screen()

    print(CYAN + r"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║      THE RUBE GOLDBERG TEMPORAL CALCULATION ENGINE           ║
║                                                              ║
║            Powered By Gears, Squirrels & Luck               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""" + RESET)

    dramatic_pause(YELLOW + "⚙ Pulling the Primary Lever..." + RESET)

    countdown = 3

    while countdown > 0:
        print(f"🟡 Marble releases in {countdown}...")
        time.sleep(1)
        countdown -= 1

    dramatic_pause("\n🎱 Marble rolling down ramp!")

    for domino in range(1, 8):
        print(f"🧱 Domino #{domino} falls!")
        time.sleep(0.25)

    dramatic_pause("\n🚗 Toy car launched!")

    lap = 1

    while lap <= 3:
        print(f"🏁 Toy car completes lap {lap}")
        time.sleep(0.5)
        lap += 1

    dramatic_pause("\n🔴 Giant Red Button Pressed!")

    gadgets = [
        "Spring",
        "Gear",
        "Rubber Chicken",
        "Catapult",
        "Tiny Piano",
        "Mechanical Squirrel"
    ]

    for gadget in gadgets:
        print(f"⚡ {gadget} activated!")
        time.sleep(0.4)

    dramatic_pause("\n🎹 Tiny piano plays dramatic chord!")
    dramatic_pause("🐿 Mechanical squirrel pulls FINAL LEVER!")

    # Generate Number of the Cycle
    cycle_number = random.randint(1, 999999)

    # Get current date and time
    current = datetime.datetime.now()

    print(
        GREEN +
        "\n╔══════════════════════════════════════════════╗\n"
        "║              MISSION COMPLETE               ║\n"
        "╚══════════════════════════════════════════════╝\n"
        + RESET
    )

    print(BLUE + "📅 Current Date" + RESET)
    print("   " + current.strftime("%A, %B %d, %Y"))

    print()

    print(BLUE + "🕒 Current Time" + RESET)
    print("   " + current.strftime("%I:%M:%S %p"))

    print()

    print(MAGENTA + "🔮 The Number of the Cycle" + RESET)
    print(f"   {cycle_number:,}")

    print("\n" + "═" * 54)


# ==========================
# Main Program Loop
# ==========================

running = True

while running:

    machine_run()

    while True:

        print("\nMENU")
        print("────")
        print("U - Run another cycle")
        print("B - Reveal Top Secret Information")
        print("E - Exit machine")

        choice = input("\nSelection: ").strip().upper()

        if choice == "U":

            print(
                CYAN +
                "\n🔧 Resetting machine..."
                "\n🧱 Standing up dominoes..."
                "\n🎱 Returning marble..."
                "\n🐿 Winding squirrel..."
                + RESET
            )

            time.sleep(2)
            break

        elif choice == "B":

            print(
                YELLOW +
                "\n╔══════════════════════════════════════════════╗"
                "\n║          TOP SECRET INFORMATION             ║"
                "\n╚══════════════════════════════════════════════╝"
                + RESET
            )

            time.sleep(1)

            print("\n🔓 ACCESSING CLASSIFIED DATABASE...")
            time.sleep(1)

            print("🕵 Verifying clearance...")
            time.sleep(1)

            print("🐿 Contacting squirrel headquarters...")
            time.sleep(1)

            secret_day = datetime.datetime.now().strftime("%A")

            print("\nCLASSIFIED INFORMATION")
            print("──────────────────────")
            print("The current day of the week is:")
            print()
            print(f"⭐ {secret_day} ⭐")
            print()
            print("This information has been classified")
            print("because nobody asked the squirrel.")
            print()
            print("Thank you for accessing these completely useless secrets.")

            input("\nPress Enter to return to the menu...")

        elif choice == "E":

            print(
                RED +
                r"""

      /\_/\\
     ( o.o )
      > ^ <

The squirrel salutes you.

SHUTTING DOWN TEMPORAL CALCULATION ENGINE...

"""
                + RESET
            )

            time.sleep(3)

            print("🚗 Stopping toy car...")
            time.sleep(1)

            print("🧱 Collecting dominoes...")
            time.sleep(1)

            print("🎱 Returning marble to storage...")
            time.sleep(1)

            print("🐿 Powering down squirrel...")
            time.sleep(2)

            print("\n✅ Shutdown complete.")

            running = False
            break

        else:
            print("\n❌ Invalid selection. Please choose U, B, or E.")

print("\nGoodbye!")
input("\nPress Enter to close the program...")

