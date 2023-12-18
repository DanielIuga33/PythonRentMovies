from models.Movie import Movie
from models.dto.MovieDto import MovieDto


class ClientMapper:
    def fromEntityToDto(self, entity: Movie):
        return MovieDto(entity.get_id_movie(), entity.get_title(), entity.get_rating(), entity.)

    def fromListsEntityToDto(self, entityLists):
        result = []
        for entity in entityLists:
            result.append(MovieDto(entity.get_id_movie(), entity.get_title()))
        return result
