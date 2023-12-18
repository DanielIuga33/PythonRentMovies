from models.Client import Client


class ClientValidator:
    def validate(self, client: Client):
        errors = []
        print(client.get_email())
        if client.get_name() == "":
            errors.append("Name cannot be null !")
        if client.get_surname() == "":
            errors.append("Surname cannot be null !")
        if client.get_email() == "":
            errors.append("Emmail cannot be null !")
        if "@" not in client.get_email():
            errors.append("Email must contain @")
        if client.get_email()[-4:] != ".com":
            errors.append("Email must end with .com !")
        try:
            if len(client.get_cnp()) != 13 or int(client.get_cnp()) < 0:
                errors.append("Invalid CNP !")
            if int(client.get_age()) < 1 or int(client.get_age()) > 100:
                errors.append("Invalid age !")
        except ValueError as e:
            errors.append(e)
        if errors:
            raise ValueError(errors)
