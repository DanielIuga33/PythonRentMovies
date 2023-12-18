from models.mappers import MovieMapper
from models.mappers.ClientMapper import ClientMapper
from models.validators.ClientValidator import ClientValidator
from models.validators.MovieValidator import MovieValidator
from repository.RepoFile import RepoFile
from service.ServiceClient import ServiceClient
from service.ServiceMovie import ServiceMovie
from ui.UserInterface import UserInterface


def main():
    repo_cl = RepoFile("Clients")
    # client_val = ClientValidator
    # client_mapper = ClientMapper
    srv_cl = ServiceClient(repo_cl)

    repo_mv = RepoFile("Movies")
    srv_mv = ServiceMovie(repo_mv)
    ui = UserInterface(srv_cl, srv_mv)
    ui.run()


if __name__ == '__main__':
    main()
