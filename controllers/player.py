from dataclasses import dataclass
from domains.player import Player
from interfaces.player import IPlayerController
from random import randint

@dataclass
class PlayerController(IPlayerController):

    def pass_the_ball(self, me: Player, adversary: Player, team_target_player: Player) -> str:

        # calcular % de acerto em passe/chute com o adicional de pontos
        percent_me = randint(0, 100) + me.pass_points
        percent_adversary = randint(0, 100) + adversary.intercept_pass_points

        

        return 'ok'

    def shoot_the_ball(self, me: Player, defensor: Player, goalkeeper: Player) -> str:
        return 'ok'