import uuid

from models.Entity import Entity


class Client(Entity):
    def __init__(self, id_entity, name, surname, email, cnp, age):
        super().__init__(id_entity)
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__cnp = cnp
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname

    def set_surname(self, name):
        self.__surname = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_cnp(self):
        return self.__cnp

    def set_cnp(self, cnp):
        self.__cnp = cnp

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def __eq__(self, other):
        return (self.get_name() == other.get_name() and self.get_surname() == other.get_surname()
                and self.get_email() == other.get_email() and self.get_cnp() == other.get_cnp()
                and self.get_age() == other.get_age())

    def __str__(self):
        return (f"{self.get_id_entity()}~{self.__name}~{self.__surname}"
                f"~{self.__email}~{self.__cnp}~{self.__age}")
