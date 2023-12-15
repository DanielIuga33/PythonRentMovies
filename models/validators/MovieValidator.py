from models.Movie import Movie


class MovieValidator:
    def validate(self, movie: Movie):
        errors = []
        if movie.get_title() == "":
            errors.append("Title cannot be null !")
        if errors:
            raise KeyError(errors)
