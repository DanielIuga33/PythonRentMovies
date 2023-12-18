from models.Client import Client
from models.mappers.ClientMapper import ClientMapper
from models.validators.ClientValidator import ClientValidator
from repository.RepoFile import RepoFile


class ServiceClient:
    def __init__(self, repo: RepoFile):
        self.__repo = repo
        self.__validator = ClientValidator
        self.__mapper = ClientMapper

    def add(self, name, surname, email, cnp, age):
        if self.exists(email, "email"):
            raise ValueError("Email already exists")
        if self.exists(cnp, "cnp"):
            raise ValueError("CNP already exists")
        self.__validator.validate(self, Client(name, surname, email, cnp, age))
        self.__repo.add(Client(name, surname, email, cnp, age))

    def remove(self, item):
        if self.exists(item, "name"):
            self.__repo.delete(self.find(item, "name"))
            return 1
        elif self.exists(item, "surname"):
            self.__repo.delete(self.find(item, "surname"))
            return 1
        elif self.exists(item, "email"):
            self.__repo.delete(self.find(item, "email"))
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
            case "email":
                for entity in self.__repo.get_all():
                    if entity.get_email() == item:
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
            case "email":
                if self.find(item, "email") == 0:
                    return False
                return True
            case _:
                return

    def get_all(self):
        result = []
        for lines in self.__repo.get_all():
            line = lines.split("~")
            client = Client(line[1], line[2], line[3], line[4], line[5])
            client.set_client_id(line[0])
            result.append(client)
        return result

    def get_all_dto(self):
        return self.__mapper.fromListsEntityToDtoList(self, self.get_all())

    def size(self):
        return len(self.__repo.get_all())
