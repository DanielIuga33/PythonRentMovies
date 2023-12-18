from service.ServiceClient import ServiceClient
from service.ServiceMovie import ServiceMovie
from utils.Functions import show_all
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
                case "a":
                    show_all(self.srv_mv.get_all())
                case "x":
                    return
                case _:
                    print("Invalid choice")

    def add(self):
        title = input("Enter the movie title: ")
        dc = input("Enter the movie description: ")

        self.srv_mv.add()

    def remove(self):
        return