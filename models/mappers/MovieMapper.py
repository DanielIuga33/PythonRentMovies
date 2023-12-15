from models.Movie import Movie
from models.dto.MovieDto import MovieDto


class ClientMapper:
    def fromEntityToDto(self, entity: Movie):
        return MovieDto(entity.get_id_movie(), entity.get_title())

    def fromListsEntityToDto(self, entityLists):
        result = []
        for entity in entityLists:
            result.append(self.fromEntityToDto(entity))
        return result
