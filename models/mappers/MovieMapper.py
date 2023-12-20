from models.Movie import Movie
from models.dto.MovieDto import MovieDto


class MovieMapper:
    def fromEntityToDto(self, entity: Movie):
        return MovieDto(entity.get_id_entity(), entity.get_title(), entity.get_gen(), entity.get_rating())

    def fromListsEntityToDto(self, entityLists):
        result = []
        for entity in entityLists:
            result.append(MovieDto(entity.get_id_entity(), entity.get_title(), entity.get_gen(), entity.get_rating()))
        return result
