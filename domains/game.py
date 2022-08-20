from dataclasses import dataclass
from datetime import datetime

from domains.hoster import Hoster
from domains.team import Team

@dataclass
class Game:
    code: str
    status: str
    hoster: Hoster
    team_a: Team
    team_b: Team
    score_a: int = 0
    score_b: int = 0
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()