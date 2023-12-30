from models.Entity import Entity


class Rent(Entity):
    def __init__(self, id_entity, id_client, id_movie, date):
        super().__init__(id_entity)
        self.__id_cl = id_client
        self.__id_mv = id_movie
        self.__date = date

    def get_id_client(self):
        return self.__id_cl

    def get_id_movie(self):
        return self.__id_mv

    def get_date(self):
        return self.__date

    def set_id_client(self, id_client):
        self.__id_cl = id_client

    def set_id_movie(self, id_movie):
        self.__id_mv = id_movie

    def set_date(self, date):
        self.__date = date

    def __eq__(self, other):
        return (self.get_id_entity() == other.get_id_entity()
                and self.get_id_client() == other.get_id_client()
                and self.get_id_movie() == other.get_id_movie()
                and self.get_date() == other)

    def __str__(self):
        return f"{self.get_id_entity()}~{self.get_id_client()}~{self.get_id_movie()}~{self.get_date()}"
