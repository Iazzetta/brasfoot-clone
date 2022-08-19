import unittest
from domains.manager import Manager
from domains.player import Player
from domains.team import Team

class TestPlayerController(unittest.TestCase):

    def setUp(self) -> None:

        self.team1 = Team(name = "Palmeiras")
        self.team2 = Team(name = "São Paulo")
        
        self.team1.players.append(Player(
            name = "Zangueiro",
            type_position = "defensor"
        ))

    def test_check_team_names(self):
        self.assertEqual(self.team1.name, "Palmeiras")
        self.assertEqual(self.team2.name, "São Paulo")

if __name__ == '__main__':
    unittest.main()