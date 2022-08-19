import unittest
from domains.manager import Manager
from domains.player import Player
from domains.team import Team

class TestPlayerController(unittest.TestCase):

    def setUp(self) -> None:

        self.team1 = Team(name = "Palmeiras")
        self.team2 = Team(name = "São Paulo")
        
        self.team1.players.append([
            Player(name = "Bruno", type_position = "goalkeeper"),
            Player(name = "Caio", type_position = "defensor"),
            Player(name = "Jorge", type_position = "midfield"),
            Player(name = "Neymar", type_position = "attacker"),
        ])

        self.team2.players.append([
            Player(name = "Rogerio", type_position = "goalkeeper"),
            Player(name = "Zidani", type_position = "defensor"),
            Player(name = "Jeferson", type_position = "midfield"),
            Player(name = "Messi", type_position = "attacker"),
        ])

    def test_check_team_names(self):
        self.assertEqual(self.team1.name, "Palmeiras")
        self.assertEqual(self.team2.name, "São Paulo")

        

if __name__ == '__main__':
    unittest.main()