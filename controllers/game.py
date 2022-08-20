from datetime import datetime
import time
from controllers.player import PlayerController
from domains.game import Game
from domains.hoster import Hoster
from domains.player import Player
from domains.team import Team
from interfaces.game import IGameController



class GameController(IGameController):
    __player_controller: PlayerController = PlayerController()
    __time_between_each_play: int = 2
    __game_running: bool = True
    __minutes_per_rounds: int = 24 * 60 * 60
    __round: int = 0
    __time_between_rounds: int = 5

    def load(self):
        team_a:Team = Team(name = "Palmeiras")
        team_b:Team = Team(name = "São Paulo")
        
        team_a.players = [
            Player(name = "Bruno", type_position = "goalkeeper"),
            Player(name = "Caio", type_position = "defensor"),
            Player(name = "Carlinhos", type_position = "defensor"),
            Player(name = "Jorge", type_position = "midfield"),
            Player(name = "Jairo", type_position = "midfield"),
            Player(name = "Fagundes", type_position = "midfield"),
            Player(name = "Neymar", type_position = "attacker"),
            Player(name = "Madara", type_position = "attacker"),
        ]

        team_b.players = [
            Player(name = "Rogerio", type_position = "goalkeeper"),
            Player(name = "Zidani", type_position = "defensor"),
            Player(name = "Chidori", type_position = "defensor"),
            Player(name = "Jeferson", type_position = "midfield"),
            Player(name = "Guilherme", type_position = "midfield"),
            Player(name = "Kenio", type_position = "midfield"),
            Player(name = "Messi", type_position = "attacker"),
            Player(name = "Pelé", type_position = "attacker"),
        ]
        hoster = Hoster(
            username = "pablo",
            name = "Campeonato Legal",
            email = "asdasjd@gmail.com",
        )
        self.game = Game(
            code = "123",
            status = "started",
            hoster = hoster,
            team_a = team_a,
            team_b = team_b,
        )
    
    def organize_players(self):
        self.__player_controller.team_with_ball = self.game.team_a
        self.__player_controller.ball_owner = self.__player_controller.get_random_player_by_position(
            type_position = 'midfield',
            team = self.__player_controller.team_with_ball,
        )
        self.__player_controller.show_score(t1 = self.game.team_a, t2 = self.game.team_b)
        time.sleep(self.__time_between_each_play)
        self.__player_controller.who_starts_the_game()

    def start_game(self):
        started_at = datetime.now()
        while self.__game_running:
            time.sleep(self.__time_between_each_play)
            actual_time = datetime.now()
            difference = actual_time - started_at
            check_minute = divmod(difference.days * self.__minutes_per_rounds + difference.seconds, 60) [0]
            if check_minute == 1 and self.__round < 1:
                print("\n@ Round 1 finalizado\n")
                self.__round = 1
                time.sleep(self.__time_between_rounds)
                self.organize_players()
            elif check_minute == 2:
                print("fim de jogo!")
                self.__game_running = False            

            if self.__player_controller.ball_owner.type_position in ['goalkeeper', 'defensor', 'midfield' ]:
                adversary = self.__player_controller.get_random_player_by_position(
                    type_position= self.__player_controller.get_player_to_intercept(me = self.__player_controller.ball_owner),
                    team = self.game.team_b if self.__player_controller.team_with_ball == self.game.team_a else self.game.team_a
                )
                friend = self.__player_controller.get_random_player_by_position(
                    type_position= self.__player_controller.get_player_to_pass(me = self.__player_controller.ball_owner),
                    team = self.__player_controller.team_with_ball,
                    except_me = self.__player_controller.ball_owner
                )
                self.__player_controller.ball_owner = self.__player_controller.pass_the_ball( self.__player_controller.ball_owner, adversary, friend )
                self.__player_controller.team_with_ball = self.__player_controller.get_player_team(
                    player = self.__player_controller.ball_owner, 
                    t1 = self.game.team_a, 
                    t2 = self.game.team_b
                )
            elif self.__player_controller.ball_owner.type_position == 'attacker':
                adversary_defensor = self.__player_controller.get_random_player_by_position(
                    type_position = self.__player_controller.get_player_to_intercept(me = self.__player_controller.ball_owner),
                    team = self.game.team_b if self.__player_controller.team_with_ball == self.game.team_a else self.game.team_a
                )
                adversary_goalkeeper = self.__player_controller.get_random_player_by_position(
                    type_position = 'goalkeeper',
                    team = self.game.team_b if self.__player_controller.team_with_ball == self.game.team_a else self.game.team_a
                )

                if self.__player_controller.dribble_defender(me = self.__player_controller.ball_owner, defensor = adversary_defensor):
                    time.sleep(self.__time_between_each_play)
                    if self.__player_controller.shoot_the_ball(me = self.__player_controller.ball_owner, goalkeeper = adversary_goalkeeper):
                        # update winner team score
                        winner = self.__player_controller.get_player_team(
                            player = self.__player_controller.ball_owner, 
                            t1 = self.game.team_a, 
                            t2 = self.game.team_b
                        )
                        if winner == self.game.team_a:
                            self.game.team_a.score += 1
                        else:
                            self.game.team_b.score += 1

                        # reset game after gol
                        self.__player_controller.reset_game_after_gol(winner = winner, t1 = self.game.team_a, t2 = self.game.team_b)
                        time.sleep(self.__time_between_each_play)
                        self.__player_controller.who_starts_the_game()
                    else:
                        self.__player_controller.ball_owner = adversary_goalkeeper
                        self.__player_controller.team_with_ball = self.__player_controller.get_player_team(
                            player = self.__player_controller.ball_owner, 
                            t1 = self.game.team_a, 
                            t2 = self.game.team_b
                        )
                    time.sleep(self.__time_between_each_play)
                else:
                    self.__player_controller.ball_owner = adversary_defensor
                    self.__player_controller.team_with_ball = self.__player_controller.get_player_team(
                        player = self.__player_controller.ball_owner, 
                        t1 = self.game.team_a, 
                        t2 = self.game.team_b
                    )
