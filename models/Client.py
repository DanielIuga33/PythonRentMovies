class Client:
    def __init__(self, client_id, name, surname, cnp, age):
        self.__client_id = client_id
        self.__name = name
        self.__surname = surname
        self.__cnp = cnp
        self.__age = age

    def get_client_id(self):
        return self.__client_id

    def set_client_id(self, client_id):
        self.__client_id = client_id

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
        return (self.__client_id == other.__client_id and self.__name == other.__name
                and self.__surname == other and self.__cnp == other.__cnp and self.__age == other.__age)

    def __str__(self):
        return str(self)

