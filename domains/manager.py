from dataclasses import dataclass
from domains.team import Team

@dataclass
class Manager:
    name: str
    team: Team
