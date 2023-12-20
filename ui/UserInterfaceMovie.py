import uuid

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
                    show_all(self.srv_mv.get_all_dto())
                case "x":
                    return
                case _:
                    print("Invalid choice")

    def add(self):
        id_mv = uuid.uuid4()
        title = input("Enter the movie title: ")
        dc = input("Enter the movie description: ")
        gen = input("Enter the movie genre: ")
        duration = input("Enter the movie duration(minutes): ")
        rating = input("Enter the movie rating(0-5): ")
        try:
            self.srv_mv.add(id_mv, title, dc, gen, duration, rating)
            print(" Movie added successfully")
        except ValueError as e:
            print(f"  Errors: {e}")

    def remove(self):
        show_all(self.srv_mv.get_all_dto())
        title = input("Enter the movie's title: ")
        try:
            self.srv_mv.remove_by_title(title)
            print(" Movie deleted successfully")
        except ValueError as e:
            print(f"  Error: {e}")
