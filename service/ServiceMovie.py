from models.Movie import Movie
from models.mappers import MovieMapper
from models.validators.MovieValidator import MovieValidator
from repository.RepoFile import RepoFile


class ServiceMovie:
    def __init__(self, repo: RepoFile):
        self.__repo = repo
        self.__validator = MovieValidator
        self.__mapper = MovieMapper

    def add(self, title, description, gen):
        self.__validator.validate(self, Movie(title, description, gen))
        self.__repo.add(Movie(title, description, gen))

    def remove_by_title(self, item):
        if self.exists(item, "title"):
            self.__repo.delete(self.find(item, "title"))
            return 1

    def find(self, by_what, item):
        match by_what:
            case "title":
                for entity in self.__repo.get_all():
                    if entity.name == item:
                        return entity
                return 0
            case "description":
                for entity in self.__repo.get_all():
                    if entity.surname == item:
                        return entity
                return 0
            case _:
                return -1

    def exists(self, by_what, item):
        match by_what:
            case "title":
                if self.find(item, "title") == 0:
                    return False
                return True
            case "description":
                if self.find(item, "description") == 0:
                    return False
                return True
            case _:
                return

    def get_all(self):
        return self.__repo.get_all()

    def get_all_dto(self):
        return self.__mapper.fromListsEntityToDtoList(self.get_all())

    def size(self):
        return len(self.__repo.get_all())