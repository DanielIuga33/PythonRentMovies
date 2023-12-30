from models.Rent import Rent
from repository.RepoFile import RepoFile


class ServiceRent:
    def __init__(self, repo: RepoFile):
        self.__repo = repo

    def add(self, id_entity, id_cl, id_mv, date):
        self.__repo.add(Rent(id_entity, id_cl, id_mv, date))

    def remove(self, id_entity, id_cl, id_mv, date):
        self.__repo.delete(Rent(id_entity, id_cl, id_mv, date))

    def get_all(self):
        result = []
        for lines in self.__repo.get_all():
            line = lines.split("~")
            rent = Rent(line[0], line[1], line[2], line[3])
            result.append(rent)
        return result

    def get_all_movies_for_a_client(self, id_cl):
        result = []
        for rent in self.get_all():
            if rent.get_id_client() == id_cl:
                result.append(rent.get_id_movie())
        return result

    def get_all_clients_for_a_movie(self, id_movie):
        result = []
        for rent in self.get_all():
            if rent.get_id_movie() == id_movie:
                result.append(rent.get_id_client())
        return result


