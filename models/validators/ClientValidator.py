from models.Client import Client


class ClientValidator:
    def validate(self, client: Client):
        errors = []
        if client.get_name() == "":
            errors.append("Name cannot be null !")
        if client.get_surname() == "":
            errors.append("Surname cannot be null !")
        if len(client.get_cnp()) != 13:
            errors.append("Invalid CNP !")
        if int(client.get_age()) < 1 or int(client.get_age()) > 100:
            errors.append("Invalid age !")
        if errors:
            raise KeyError(errors)
