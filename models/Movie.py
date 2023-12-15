from models.Entity import Entity


class Movie(Entity):
    def __init__(self, title, description, gen):
        super().__init__()
        self.__title = title
        self.__description = description
        self.__gen = gen

    def get_id_movie(self):
        return self.get_id_entity()

    def get_title(self):
        return self.__title

    def set_title(self,title):
        self.__title = title

    def get_description(self):
        return self.__description

    def set_description(self,description):
        self.__description = description

    def get_gen(self):
        return self.__gen

    def set_gen(self, gen):
        self.__gen = gen

    def __eq__(self, other):
        return (self.__id_entity == other.__id_entity and self.__title == other
                and self.__description == other and self.__gen == other.__gen)

    def __str__(self):
        return str(self)
