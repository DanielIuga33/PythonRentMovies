import uuid

from models.Entity import Entity


class Client(Entity):
    def __init__(self, name, surname, cnp, age):
        super().__init__()
        self.__name = name
        self.__surname = surname
        self.__cnp = cnp
        self.__age = age

    def get_client_id(self):
        return self.__id_entity

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname

    def set_surname(self, name):
        self.__surname = name

    def get_cnp(self):
        return self.__cnp

    def set_cnp(self, cnp):
        self.__cnp = cnp

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def __eq__(self, other):
        return (self.__id_entity == other.__id_entity and self.__name == other.__name
                and self.__surname == other and self.__cnp == other.__cnp and self.__age == other.__age)

    def __str__(self):
        return str(self)

