import random

from core.ui import say_color

from core.constants import (
    MAGENTA
)

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
    say_color("\n✨ TEMPORAL ANOMALY: " + event, MAGENTA)
