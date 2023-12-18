from models.Client import Client
from models.mappers.ClientMapper import ClientMapper
from models.validators.ClientValidator import ClientValidator
from repository.RepoFile import RepoFile


class ServiceClient:
    def __init__(self, repo: RepoFile):
        self.__repo = repo
        self.__validator = ClientValidator
        self.__mapper = ClientMapper

    def add(self, name, surname, cnp, age):
        client = Client(name, surname, cnp, age)
        self.__validator.validate(self, client)
        self.__repo.add(Client(name, surname, cnp, age))

    def remove(self, item):
        if self.exists(item, "name"):
            self.__repo.delete(self.find(item, "name"))
            return 1
        elif self.exists(item, "surname"):
            self.__repo.delete(self.find(item, "surname"))
            return 1
        elif self.exists(item, "cnp"):
            self.__repo.delete(self.find(item, "cnp"))
            return 1

    def find(self, by_what, item):
        match by_what:
            case "name":
                for entity in self.__repo.get_all():
                    if entity.name == item:
                        return entity
                return 0
            case "surname":
                for entity in self.__repo.get_all():
                    if entity.surname == item:
                        return entity
                return 0
            case "cnp":
                for entity in self.__repo.get_all():
                    if entity.get_cnp() == item:
                        return entity
                return 0
            case _:
                return

    def exists(self, by_what, item):
        match by_what:
            case "name":
                if self.find(item, "name") == 0:
                    return False
                return True
            case "surname":
                if self.find(item, "surname") == 0:
                    return False
                return True
            case "cnp":
                if self.find(item, "cnp") == 0:
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
