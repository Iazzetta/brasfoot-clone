import sys
sys.path.append("C:\\work\\brasfoot-clone")
from controllers.game import GameController

game_controller = GameController()
game_controller.load()
game_controller.organize_players()
game_controller.start_game()