from models.Movie import Movie
from models.mappers.MovieMapper import MovieMapper
from models.validators.MovieValidator import MovieValidator
from repository.RepoFile import RepoFile


class ServiceMovie:
    def __init__(self, repo: RepoFile):
        self.__repo = repo
        self.__validator = MovieValidator()
        self.__mapper = MovieMapper()

    def add(self, id_mv, title, description, gen, duration, rating):
        self.__validator.validate(Movie(id_mv, title, description, gen, duration, rating))
        self.__repo.add(Movie(id_mv, title, description, gen, duration, rating))

    def remove_by_title(self, item):
        if self.exists(item, "title"):
            self.__repo.delete(self.find(item, "title"))
        else:
            raise ValueError("There is no movie with this title !")

    def find(self, item, by_what):
        match by_what:
            case "id":
                for entity in self.get_all():
                    if entity.get_id_entity() == item:
                        return entity
                return None
            case "title":
                for entity in self.get_all():
                    if entity.get_title() == item:
                        return entity
                return None
            case "description":
                for entity in self.get_all():
                    if entity.get_description() == item:
                        return entity
                return None

    def exists(self, item, by_what):
        match by_what:
            case "id":
                if self.find(item, "id") is None:
                    return False
                return True
            case "title":
                if self.find(item, "title") is None:
                    return False
                return True
            case "description":
                if self.find(item, "description") is None:
                    return False
                return True
            case _:
                return

    def get_all(self):
        result = []
        for lines in self.__repo.get_all():
            line = lines.split("~")
            client = Movie(line[0], line[1], line[2], line[3], line[4], line[5])
            result.append(client)
        return result

    def get_all_dto(self):
        return self.__mapper.fromListsEntityToDto(self.get_all())

    def size(self):
        return len(self.__repo.get_all())
