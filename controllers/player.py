from dataclasses import dataclass
from domains.player import Player
from domains.team import Team
from interfaces.player import IPlayerController
from random import randint, choice

@dataclass
class PlayerController(IPlayerController):

    ball_owner: Player = None
    team_with_ball: Team = None

    def pass_the_ball(self, me: Player, adversary: Player, friend: Player) -> Player:

        # calcular % de acerto em passe/chute com o adicional de pontos
        percent_me = randint(0, 100) + me.pass_points
        percent_adversary = randint(0, 100) + adversary.intercept_pass_points

        # verificar vencedor da probabilidade
        if percent_me > percent_adversary:
            print(f"{me.fullname()} passa a bola para {friend.fullname()}")
            return friend

        # adversário rouba a bola
        print(f"{adversary.fullname()} rouba a bola de {me.fullname()}")
        return adversary


    def dribble_defender(self, me: Player, defensor: Player) -> bool:

        # calcular % do zagueiro x atacante
        percent_me = randint(0, 100) + me.pass_points
        percent_defensor = randint(0, 100) + defensor.intercept_pass_points

        # verificar se o atacante passa pelo zagueiro
        if percent_defensor > percent_me:
            print(f"{defensor.fullname()} rouba a bola de {me.fullname()}")
            return False
        
        # atacante dribla zagueiro
     
        print(f"\n{me.fullname()} driblou {defensor.fullname()} e vai chutar...\n")
        return True

    def shoot_the_ball(self, me: Player, goalkeeper: Player) -> bool:

        # calcular % do atacante x goleiro
        percent_me = randint(0, 100) + me.shoot_points
        percent_goalkeeper = randint(0, 100) + goalkeeper.defense_goal_points

        # verificar se o atacante passa pelo zagueiro
        if percent_goalkeeper > percent_me:
            
            print(f"\nDEFESA DO GOLEIRO {goalkeeper.fullname()}\n")
            return False

        print("""

            ###########    ###########   ###########   ##           @@@@@
            ###            ##       ##   ##       ##   ##          @@@@@@@@
            ###  ######    ##       ##   ##       ##   ##          @@@@@@@@
            ###     ###    ##       ##   ##       ##   ##            @@@@@
            ###########    ###########   ###########   #########

        """)
        print(f"@ GOL DO {me.fullname()} !!")
        return True

    def get_player_to_pass(self, me: Player) -> str:
        if me.type_position in ['goalkeeper', 'defensor']:
            return 'midfield'
        elif me.type_position == 'midfield':
            return 'attacker'

    def get_player_to_intercept(self, me: Player) -> str:
        if me.type_position == 'goalkeeper':
            return 'midfield'
        elif me.type_position == 'defensor':
            return 'attacker'
        elif me.type_position == 'midfield':
            return 'defensor'
        elif me.type_position == 'attacker':
            return 'defensor'

    def get_player_team(self, player: Player, t1: Team, t2: Team) -> Team:
        return t1 if player in t1.players else t2


    def get_random_player_by_position(self, type_position: str, team: Team, except_me: Player = None) -> Player:
        players = list(filter(lambda x: x.type_position == type_position and x != except_me, team.players))
        return choice(players)

    def reset_game_after_gol(self, winner: Team, t1: Team, t2: Team):
        self.team_with_ball = t1 if winner != t1 else t2
        self.ball_owner = self.get_random_player_by_position(
            type_position = 'midfield',
            team = self.team_with_ball
        )
        self.show_score(t1 = t1, t2 = t2)

    def show_score(self, t1: Team, t2: Team):
        print("\n--------------------------------\n")
        print(f"{t1.name} {t1.score} x {t2.score} {t2.name}")
        print("\n--------------------------------\n")
        print(f"@ Narração: Galvão Bueno")
        print(f"@ A Bola inicia com o {self.team_with_ball.name}!\n\n")

    def who_starts_the_game(self):
        print(f"{self.ball_owner.fullname()} recebe o passe e inicia a partida!")