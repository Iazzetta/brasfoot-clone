from dataclasses import dataclass
from datetime import datetime

@dataclass
class Hoster:
    username: str
    name: str
    email: str
    document: str = None # CNPJ/CPF
    verified: bool = False
    contact: str = None # company@company.com
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

