from abc import ABC
from domains.game import Game
from domains.team import Team
from controllers.player import PlayerController


class IGameController(ABC):

    __player_controller: PlayerController = PlayerController()

    def load(self, team_a: Team, team_b: Team) -> Game:
        raise NotImplementedError
    
    def organize_players(self):
        raise NotImplementedError

    def start_game(self):
        raise NotImplementedError