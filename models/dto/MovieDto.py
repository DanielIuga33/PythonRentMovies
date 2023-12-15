import uuid
from dataclasses import dataclass


@dataclass
class MovieDto:
    id_movie: uuid
    title: str

