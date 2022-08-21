import sys, pathlib
sys.path.append(str(pathlib.Path().absolute()))

from domains.hoster import Hoster
from domains.player import Player
from domains.team import Team
from controllers.game import GameController

# init game controller
game_controller = GameController()

# TODO - get team/hoster/player informations by repository/database

# create teams
team_a:Team = Team(name = "Palmeiras")
team_b:Team = Team(name = "São Paulo")

# create team players
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
    username = "brasfoot",
    name = "Brasfoot Official",
    email = "company@company.com",
)

# load hoster and teams
game_controller.load(
    hoster = hoster, 
    team_a = team_a, 
    team_b = team_b
)

# organize players in midfield
game_controller.organize_players()

# run game
game_controller.start_game()