from models.mappers import MovieMapper
from models.mappers.ClientMapper import ClientMapper
from models.validators.ClientValidator import ClientValidator
from models.validators.MovieValidator import MovieValidator
from repository.RepoFile import RepoFile
from service.ServiceClient import ServiceClient
from service.ServiceMovie import ServiceMovie
from service.ServiceRent import ServiceRent
from ui.UserInterface import UserInterface


def main():
    repo_cl = RepoFile("Data/Clients")
    srv_cl = ServiceClient(repo_cl)

    repo_mv = RepoFile("Data/Movies")
    srv_mv = ServiceMovie(repo_mv)

    repo_rent = RepoFile("Data/Rents")
    srv_rent = ServiceRent(repo_rent)

    ui = UserInterface(srv_cl, srv_mv, srv_rent)
    ui.run()


if __name__ == '__main__':
    main()
