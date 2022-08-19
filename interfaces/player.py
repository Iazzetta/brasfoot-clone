from abc import ABC
from domains.player import Player
from domains.team import Team


class IPlayerController(ABC):

    def pass_the_ball(self, me: Player, adversary: Player, friend: Player) -> Player:
        raise NotImplementedError

    def dribble_defender(self, me: Player, defensor: Player) -> bool:
        raise NotImplementedError

    def shoot_the_ball(self, me: Player, goalkeeper: Player) -> bool:
        raise NotImplementedError

    def get_player_to_pass(self, me: Player) -> str:
        raise NotImplementedError

    def get_player_to_intercept(self, me: Player) -> str:
        raise NotImplementedError

    def get_player_team(self, player: Player, t1: Team, t2: Team) -> Team:
        raise NotImplementedError

    def get_random_player_by_position(self, type_position: str, team: Team, except_me: Player = None) -> Player:
        raise NotImplementedError

    def reset_game_after_gol(self, winner: Team, t1: Team, t2: Team):
        raise NotImplementedError

    def show_score(self, t1: Team, t2: Team):
        raise NotImplementedError

    def who_starts_the_game(self):
        raise NotImplementedError