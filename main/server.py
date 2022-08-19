import sys, time

sys.path.append("/Users/iazzetta/workspace/aulas_python")

from controllers.player import PlayerController
from domains.player import Player
from domains.team import Team

GAME_RUNNING = True
RESET_GAME_AFTER_GOAL = True
TIME_BETWEEN_EACH_PLAY = 5

def create_teams():
    team1:Team = Team(name = "Palmeiras")
    team2:Team = Team(name = "São Paulo")

    team1.players = [
        Player(name = "Bruno", type_position = "goalkeeper"),
        Player(name = "Caio", type_position = "defensor"),
        Player(name = "Carlinhos", type_position = "defensor"),
        Player(name = "Jorge", type_position = "midfield"),
        Player(name = "Jairo", type_position = "midfield"),
        Player(name = "Fagundes", type_position = "midfield"),
        Player(name = "Neymar", type_position = "attacker"),
        Player(name = "Madara", type_position = "attacker"),
    ]

    team2.players = [
        Player(name = "Rogerio", type_position = "goalkeeper"),
        Player(name = "Zidani", type_position = "defensor"),
        Player(name = "Chidori", type_position = "defensor"),
        Player(name = "Jeferson", type_position = "midfield"),
        Player(name = "Guilherme", type_position = "midfield"),
        Player(name = "Kenio", type_position = "midfield"),
        Player(name = "Messi", type_position = "attacker"),
        Player(name = "Pelé", type_position = "attacker"),
    ]
    return (team1, team2)


if __name__ == '__main__':
    # initialize game
    team1, team2 = create_teams()

    # initialize player controller
    PC = PlayerController()

    # init ball owner / team to start the game
    PC.team_with_ball = team1
    PC.ball_owner = PC.get_random_player_by_position(
        type_position = 'midfield',
        team = team1
    )

    # initialize score
    PC.show_score(t1 = team1, t2 = team2)
    time.sleep(TIME_BETWEEN_EACH_PLAY)

    # who starts with the ball?
    PC.who_starts_the_game()

    # initialize game
    while GAME_RUNNING:
        time.sleep(TIME_BETWEEN_EACH_PLAY)
        if PC.ball_owner.type_position in ['goalkeeper', 'defensor', 'midfield' ]:
            adversary = PC.get_random_player_by_position(
                type_position= PC.get_player_to_intercept(me = PC.ball_owner),
                team = team2 if PC.team_with_ball == team1 else team1
            )
            friend = PC.get_random_player_by_position(
                type_position= PC.get_player_to_pass(me = PC.ball_owner),
                team = PC.team_with_ball,
                except_me = PC.ball_owner
            )
            PC.ball_owner = PC.pass_the_ball( PC.ball_owner, adversary, friend )
            PC.team_with_ball = PC.get_player_team(
                player = PC.ball_owner, 
                t1 = team1, 
                t2 = team2
            )
        elif PC.ball_owner.type_position == 'attacker':
            adversary_defensor = PC.get_random_player_by_position(
                type_position = PC.get_player_to_intercept(me = PC.ball_owner),
                team = team2 if PC.team_with_ball == team1 else team1
            )
            adversary_goalkeeper = PC.get_random_player_by_position(
                type_position = 'goalkeeper',
                team = team2 if PC.team_with_ball == team1 else team1
            )

            if PC.dribble_defender(me = PC.ball_owner, defensor = adversary_defensor):
                time.sleep(TIME_BETWEEN_EACH_PLAY)
                if PC.shoot_the_ball(me = PC.ball_owner, goalkeeper = adversary_goalkeeper):
                    # update winner team score
                    winner = PC.get_player_team(
                        player = PC.ball_owner, 
                        t1 = team1, 
                        t2 = team2
                    )
                    if winner == team1:
                        team1.score += 1
                    else:
                        team2.score += 1

                    # reset game after gol
                    PC.reset_game_after_gol(winner = winner, t1 = team1, t2 = team2)
                    time.sleep(TIME_BETWEEN_EACH_PLAY)
                    PC.who_starts_the_game()
                else:
                    PC.ball_owner = adversary_goalkeeper
                    PC.team_with_ball = PC.get_player_team(
                        player = PC.ball_owner, 
                        t1 = team1, 
                        t2 = team2
                    )
                time.sleep(TIME_BETWEEN_EACH_PLAY)
            else:
                PC.ball_owner = adversary_defensor
                PC.team_with_ball = PC.get_player_team(
                    player = PC.ball_owner, 
                    t1 = team1, 
                    t2 = team2
                )