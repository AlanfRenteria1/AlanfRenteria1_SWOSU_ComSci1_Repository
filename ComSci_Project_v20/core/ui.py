def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def say(text, delay=0.75):
    print(text)
    time.sleep(delay)


def say_color(text, color, delay=0.75):
    say(color + text + RESET, delay)


def beep():
    print("BEEP...")
    time.sleep(0.6)


def fast_beep():
    print("BEEP-BEEP-BEEP!")
    time.sleep(0.2)


def sound_alarm():
    print(RED + "WEEEOOO WEEEOOO WEEEOOO" + RESET)
    time.sleep(0.5)
