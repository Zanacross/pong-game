from statemanager.game import Game
from statemanager.game_over import Game_Over

class State_Manager():
    def __init__(self, screen, clock):
        self.states = {
            'menu': None,
            'game': Game(screen, clock),
            'game_over': Game_Over(screen, clock)
        }

        self.current = self.states['game']