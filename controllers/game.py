from controllers.player import PlayerController
from domains.team import Team
from interfaces import game
from interfaces.game import IGameController

class GameController(IGameController):
    __player_controller: PlayerController = PlayerController()

    def load(self, team_a: Team, team_b: Team) -> game:
        pass
    
    def organize_players(self):
        pass

    def start_game(self):
        pass
