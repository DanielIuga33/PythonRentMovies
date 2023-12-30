import uuid
from datetime import datetime

from service.ServiceClient import ServiceClient
from service.ServiceMovie import ServiceMovie
from service.ServiceRent import ServiceRent
from ui.UserInterfaceClient import UserInterfaceClient
from ui.UserInterfaceMovie import UserInterfaceMovie
from utils.Functions import show_all
from utils.Prints import print_rent_menu, print_main_menu, show_all_menu


class UserInterface:
    def __init__(self, srv_cl: ServiceClient, srv_mv: ServiceMovie, srv_rent: ServiceRent):
        self.srv_cl = srv_cl
        self.srv_mv = srv_mv
        self.srv_rent = srv_rent
        self.ui_cl = UserInterfaceClient(srv_cl, srv_mv)
        self.ui_mv = UserInterfaceMovie(srv_cl, srv_mv)

    def run(self):
        while True:
            print_main_menu()
            choice = input("Give your choice here: ")
            match choice:
                case "1":
                    self.ui_cl.run()
                case "2":
                    self.ui_mv.run()
                case "3":
                    self.rent_handler()
                case "x":
                    return
                case _:
                    print("Invalid choice !")

    def rent_handler(self):
        while True:
            print_rent_menu()
            choice = input("Give your choice here: ")
            match choice:
                case "1":
                    self.add_rent()
                case "2":
                    self.delete_rent()
                case "a":
                    self.show_all_handler()
                case "x":
                    return
                case _:
                    print("Invalid choice !")

    def add_rent(self):
        show_all(self.srv_cl.get_all_dto())
        name = input("Give the renter name: ")
        try:
            id_cl = self.srv_cl.find(name, "name").get_id_entity()
        except ValueError as e:
            print(f" Error: {e}")
            return
        show_all(self.srv_mv.get_all_dto())
        title = input("Give the movie title: ")
        try:
            id_m = self.srv_mv.find(title, "title").get_id_entity()
        except ValueError as e:
            print(f" Error: {e}")
        id_rent = uuid.uuid4()
        date = datetime.now()
        try:
            self.srv_rent.add(id_rent, id_cl, id_m, date)
        except ValueError as e:
            print(f" Error: {e}")

    def delete_rent(self):
        return

    def show_all_handler(self):
        show_all_menu()
        choice = input("Give your choice here: ")
        match choice:
            case "1":
                self.show_all_rents(1)
            case "2":
                self.show_all_rents(2)
            case "3":
                show_all(self.srv_rent.get_all())
            case "x":
                return
            case _:
                print("Invalid choice !")

    def show_all_rents(self, nr):
        if nr == 1:
            show_all(self.srv_cl.get_all_dto())
            name = input("Give the client name: ")
            try:
                id_cl = self.srv_cl.find(name, "name").get_id_entity()
                if len(self.srv_rent.get_all_movies_for_a_client(id_cl)) == 0:
                    print(f" {name}  did not rent anything yet !")
                    return
                print(f"The movies rented by client {name} are: ")
                for rent in self.srv_rent.get_all_movies_for_a_client(id_cl):
                    print(self.srv_mv.find(rent, "id"))
            except AttributeError:
                print(f" Error: You wrote the name wrong or a Client with this "
                      f"name you wrote does not exist !")
        elif nr == 2:
            show_all(self.srv_mv.get_all_dto())
            title = input("Give the movie title: ")
            try:
                id_mv = self.srv_mv.find(title, "title").get_id_entity()
                if len(self.srv_rent.get_all_clients_for_a_movie(id_mv)) == 0:
                    print(f" The movie {title} is not rented by anyone !")
                    return
                print(f"The clients for the film {title} are: ")
                for rent in self.srv_rent.get_all_clients_for_a_movie(id_mv):
                    print(self.srv_cl.find(rent, "id"))
            except AttributeError:
                print(f" Error: You wrote the title wrong or a Movie with this"
                      f" title you wrote does not exist !")
