from models.Movie import Movie


class MovieValidator:
    def validate(self, movie: Movie):
        errors = []
        if not self.validate_title(movie.get_title()):
            errors.append("Movie title cannot be null !")
        if not self.validate_rating(movie.get_rating()):
            errors.append("Invalid movie rating !")
        if not self.validate_duration(movie.get_duration()):
            errors.append("Invalid movie duration !")
        if errors:
            raise ValueError(errors)

    def validate_title(self, title):
        if title == "":
            return False
        return True

    def validate_rating(self, rating):
        try:
            if float(rating) < 0.0 or float(rating) > 5.0:
                return False
            return True
        except ValueError:
            return False

    def validate_duration(self, duration):
        try:
            if float(duration) < 0:
                return False
            return True
        except ValueError:
            return False
