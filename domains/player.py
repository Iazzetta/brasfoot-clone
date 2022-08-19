from dataclasses import dataclass

@dataclass
class Player:
    name: str
    type_position: str
    amount_goals: int = 0
    has_the_ball: bool = False

    # addictional points
    pass_points: int = 1
    shoot_points: int = 1
    defense_goal_points: int = 1
    intercept_pass_points: int = 1

    def fullname(self) -> str:
        nick_position = {
            "goalkeeper": "GL",
            "defensor": "D",
            "midfield": "M",
            "attacker": "A",
        }
        return f"[{nick_position[self.type_position]}] {self.name}"