from dataclasses import dataclass, field
from domains.player import Player

@dataclass
class Team:
    name: str
    players: list[Player] = field(default_factory=list)
