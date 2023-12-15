from service.ServiceClient import ServiceClient
from service.ServiceMovie import ServiceMovie
from utils.Prints import print_movie_menu


class UserInterfaceMovie:
    def __init__(self, srv_cl: ServiceClient, srv_mv: ServiceMovie):
        self.srv_cl = srv_cl
        self.srv_mv = srv_mv

    def run(self):
        while True:
            print_movie_menu()
            choice = input("Give your choice here: ")
            match choice:
                case "1":
                    self.add()
                case "2":
                    self.remove()
                case "x":
                    return
                case _:
                    print("Invalid choice")

    def add(self):
        return

    def remove(self):
        return