import uuid
from dataclasses import dataclass

from models.Entity import Entity


@dataclass
class ClientDto(Entity):
    id_client: str
    name: str
    surname: str
    email: str
