import random

class GameState:

    def __init__(self):

        self.state = "start"

        self.cycle_number = random.randint(
            1,
            999999
        )
