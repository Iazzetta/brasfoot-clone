from abc import ABC
from domains.player import Player


class IPlayerController(ABC):

    def pass_the_ball(self, me: Player, adversary: Player, team_target_player: Player) -> str:
        raise NotImplementedError

    def shoot_the_ball(self, me: Player, defensor: Player, goalkeeper: Player) -> str:
        raise NotImplementedError