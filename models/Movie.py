from models.Entity import Entity


class Movie(Entity):
    def __init__(self, id_entity, title, description, gen, duration, rating):
        super().__init__(id_entity)
        self.__title = title
        self.__description = description
        self.__gen = gen
        self.__duration = duration
        self.__rating = rating

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_description(self):
        return self.__description

    def set_description(self,description):
        self.__description = description

    def get_gen(self):
        return self.__gen

    def set_gen(self, gen):
        self.__gen = gen

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        self.__rating = rating

    def __eq__(self, other):
        return (self.get_id_entity() == other.get_id_entity() and self.__title == other
                and self.__description == other and self.__gen == other.__gen)

    def __str__(self):
        return (f"{self.get_id_entity()}~{self.get_title()}~{self.get_description()}~{self.get_gen()}~"
                f"{self.get_duration()}~{self.get_rating()}")
