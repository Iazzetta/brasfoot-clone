from dataclasses import dataclass, field
from datetime import datetime

from domains.player import Player

@dataclass
class Team:
    name: str
    players: list[Player] = field(default_factory=list)
    score: int = 0
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()