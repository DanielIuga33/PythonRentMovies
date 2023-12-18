import uuid
from dataclasses import dataclass


@dataclass
class ClientDto:
    id_client: uuid
    name: str
    surname: str
    email: str
