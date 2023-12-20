from models.Client import Client


class ClientValidator:
    def validate(self, client: Client):
        errors = []
        if not self.validate_name(client.get_name()):
            errors.append("Name cannot be null !")
        if not self.validate_surname(client.get_surname()):
            errors.append("Surname cannot be null !")
        if self.validate_email(client.get_email()):
            errors.append(self.validate_email(client.get_email()))
        if not self.validate_cnp(client.get_cnp()):
            errors.append("Invalid CNP !")
        if not self.validate_age(client.get_age()):
            errors.append("Invalid age !")
        if errors:
            raise ValueError(errors)

    def validate_cnp(self, client):
        try:
            if len(client) != 13 or int(client) < 0:
                return False
            return True
        except ValueError as e:
            return False

    def validate_age(self, client):
        try:
            if int(client) < 1 or int(client) > 100:
                return False
            return True
        except ValueError as e:
            return False

    def validate_name(self, client: str):
        if client == "":
            return False
        return True

    def validate_surname(self, client: str):
        if client == "":
            return False
        return True

    def validate_email(self, client):
        errors = []
        if client == "":
            errors.append("Email cannot be null !")
        if "@" not in client:
            errors.append("Email must contain @")
        if client[-4:] != ".com":
            errors.append("Email must end with .com !")
        return errors
