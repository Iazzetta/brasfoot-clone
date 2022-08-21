from datetime import datetime
import time
from controllers.player import PlayerController
from domains.game import Game
from domains.hoster import Hoster
from domains.team import Team
from interfaces.game import IGameController



class GameController(IGameController):
    __pcontroller: PlayerController = PlayerController()
    __time_between_each_play: int = 2
    __game_running: bool = True
    __minutes_per_rounds: int = 24 * 60 * 60
    __round: int = 0
    __time_between_rounds: int = 5

    def load(self, hoster: Hoster, team_a: Team, team_b: Team):
        self.game = Game(
            code = "123",
            status = "started",
            hoster = hoster,
            team_a = team_a,
            team_b = team_b,
        )
    
    def organize_players(self):
        """ 
            Define who team will start with the ball and ball owner
            based on random midfield player.
            Show the score and initial informations
        """
        self.__pcontroller.team_with_ball = self.game.team_a
        self.__pcontroller.ball_owner = self.__pcontroller.get_random_player_by_position(
            type_position = 'midfield',
            team = self.__pcontroller.team_with_ball,
        )
        self.__pcontroller.show_score(t1 = self.game.team_a, t2 = self.game.team_b)
        time.sleep(self.__time_between_each_play)
        self.__pcontroller.who_starts_the_game()

    def start_game(self):
        started_at = datetime.now()
        while self.__game_running:

            """
                validation to check rounds (1 min each round)
            """
            time.sleep(self.__time_between_each_play)
            actual_time = datetime.now()
            difference = actual_time - started_at
            check_minute = divmod(difference.days * self.__minutes_per_rounds + difference.seconds, 60) [0]
            if check_minute == 1 and self.__round < 1:
                print("\n@ 1º Tempo finalizado\n")
                self.__round = 1
                time.sleep(self.__time_between_rounds)
                self.organize_players()
            elif check_minute == 2:
                print("\n@ 2º Tempo finalizado. FIM DE JOGO!\n")
                self.__game_running = False

            """ 
                control players who need to pass the ball to do a goal
                controll players who will intercept pass
            """
            if self.__pcontroller.ball_owner.type_position in ['goalkeeper', 'defensor', 'midfield' ]:
                # get adversary (interceptor)
                adversary = self.__pcontroller.get_random_player_by_position(
                    type_position= self.__pcontroller.get_player_to_intercept(
                        me = self.__pcontroller.ball_owner
                    ),
                    team = self.game.team_b if self.__pcontroller.team_with_ball == self.game.team_a else self.game.team_a
                )
                # get friend (ball owner want to pass)
                friend = self.__pcontroller.get_random_player_by_position(
                    type_position= self.__pcontroller.get_player_to_pass(
                        me = self.__pcontroller.ball_owner
                    ),
                    team = self.__pcontroller.team_with_ball,
                    except_me = self.__pcontroller.ball_owner
                )
                # try pass the ball and set the new owner (adversary or friend)
                self.__pcontroller.ball_owner = self.__pcontroller.pass_the_ball( 
                    self.__pcontroller.ball_owner, adversary, friend 
                )
                # define team who have the ball now
                self.__pcontroller.team_with_ball = self.__pcontroller.get_player_team(
                    player = self.__pcontroller.ball_owner, 
                    t1 = self.game.team_a, 
                    t2 = self.game.team_b
                )

            elif self.__pcontroller.ball_owner.type_position == 'attacker':
                """
                    if player is attacker, must to dribble defensor and try to do a goal
                """

                # get defensor adversary (interceptor to be dribbled)
                adversary_defensor = self.__pcontroller.get_random_player_by_position(
                    type_position = self.__pcontroller.get_player_to_intercept(me = self.__pcontroller.ball_owner),
                    team = self.game.team_b if self.__pcontroller.team_with_ball == self.game.team_a else self.game.team_a
                )
                # get goalkeeper
                adversary_goalkeeper = self.__pcontroller.get_random_player_by_position(
                    type_position = 'goalkeeper',
                    team = self.game.team_b if self.__pcontroller.team_with_ball == self.game.team_a else self.game.team_a
                )

                # try dribble defensor
                if self.__pcontroller.dribble_defender(me = self.__pcontroller.ball_owner, defensor = adversary_defensor):
                    time.sleep(self.__time_between_each_play)

                    # try shoot to goal
                    if self.__pcontroller.shoot_the_ball(me = self.__pcontroller.ball_owner, goalkeeper = adversary_goalkeeper):
                       
                        # update winner team score
                        winner = self.__pcontroller.get_player_team(
                            player = self.__pcontroller.ball_owner, 
                            t1 = self.game.team_a, 
                            t2 = self.game.team_b
                        )
                        if winner == self.game.team_a:
                            self.game.team_a.score += 1
                        else:
                            self.game.team_b.score += 1

                        # reset game after gol
                        self.__pcontroller.reset_game_after_gol(winner = winner, t1 = self.game.team_a, t2 = self.game.team_b)
                        time.sleep(self.__time_between_each_play)
                        self.__pcontroller.who_starts_the_game()
                    else:
                        # goalkeeper defends.
                        self.__pcontroller.ball_owner = adversary_goalkeeper
                        self.__pcontroller.team_with_ball = self.__pcontroller.get_player_team(
                            player = self.__pcontroller.ball_owner, 
                            t1 = self.game.team_a, 
                            t2 = self.game.team_b
                        )
                    time.sleep(self.__time_between_each_play)
                else:
                    # defensor intercept dribble
                    self.__pcontroller.ball_owner = adversary_defensor
                    self.__pcontroller.team_with_ball = self.__pcontroller.get_player_team(
                        player = self.__pcontroller.ball_owner, 
                        t1 = self.game.team_a, 
                        t2 = self.game.team_b
                    )
