from models.Client import Client
from models.mappers.ClientMapper import ClientMapper
from models.validators.ClientValidator import ClientValidator
from repository.RepoFile import RepoFile


class ServiceClient:
    def __init__(self, repo: RepoFile):
        self.__repo = repo
        self.__validator = ClientValidator()
        self.__mapper = ClientMapper()

    def add(self, id_client, name, surname, email, cnp, age):
        if self.exists(email, "email"):
            raise ValueError("Email already exists")
        if self.exists(cnp, "cnp"):
            raise ValueError("CNP already exists")
        client = Client(id_client, name, surname, email, cnp, age)
        print(client)
        self.__validator.validate(client)
        self.__repo.add(client)

    def remove(self, item, case):
        if case == "name":
            if self.exists(item, "name"):
                self.__repo.delete(self.find(item, "name"))
        elif case == "surname":
            if self.exists(item, "surname"):
                self.__repo.delete(self.find(item, "surname"))
        elif case == "email":
            if self.exists(item, "email"):
                self.__repo.delete(self.find(item, "email"))
        elif case == "cnp":
            if self.exists(item, "cnp"):
                self.__repo.delete(self.find(item, "cnp"))

    def find(self, item, by_what):
        match by_what:
            case "name":
                if self.__validator.validate_name(item):
                    for entity in self.get_all():
                        if entity.get_name() == item:
                            return entity
                    return None
                else:
                    raise ValueError("Name cannot be null !")
            case "surname":
                if self.__validator.validate_surname(item):
                    for entity in self.get_all():
                        if entity.get_surname() == item:
                            return entity
                    return None
                else:
                    raise ValueError("Surname cannot be null !")
            case "cnp":
                if self.__validator.validate_cnp(item):
                    for entity in self.get_all():
                        if entity.get_cnp() == item:
                            return entity
                    return None
                else:
                    raise ValueError("Invalid CNP !")
            case "email":
                if not self.__validator.validate_email(item):
                    for entity in self.get_all():
                        if entity.get_email() == item:
                            return entity
                    return None
                else:
                    raise ValueError("Invalid email !")
            case _:
                return

    def exists(self, item, by_what):
        match by_what:
            case "name":
                if self.find(item, "name") is None:
                    return False
                return True
            case "surname":
                if self.find(item, "surname") is None:
                    return False
                return True
            case "cnp":
                if self.find(item, "cnp") is None:
                    return False
                return True
            case "email":
                if self.find(item, "email") is None:
                    return False
                return True
            case _:
                return

    def get_all(self):
        result = []
        for lines in self.__repo.get_all():
            line = lines.split("~")
            client = Client(line[0], line[1], line[2], line[3], line[4], line[5])
            result.append(client)
        return result

    def get_all_dto(self):
        return self.__mapper.fromListsEntityToDtoList(self.get_all())

    def size(self):
        return len(self.__repo.get_all())

