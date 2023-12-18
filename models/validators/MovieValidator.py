from models.Movie import Movie


class MovieValidator:
    def validate(self, movie: Movie):
        errors = []
        if movie.get_title() == "":
            errors.append("Title cannot be null !")
        if float(movie.get_rating()) < 0:
            errors.append("Rating cannot be negative !")
        if float(movie.get_duration()) < 0:
            errors.append("Duration cannot be negative !")
        if errors:
            raise ValueError(errors)
