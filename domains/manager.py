from dataclasses import dataclass
from datetime import datetime

from domains.team import Team

@dataclass
class Manager:
    name: str
    team: Team
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
