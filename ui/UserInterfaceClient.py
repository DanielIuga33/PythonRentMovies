from service.ServiceClient import ServiceClient
from service.ServiceMovie import ServiceMovie
from utils.Functions import show_all
from utils.Prints import print_movie_menu, print_client_menu


class UserInterfaceClient:
    def __init__(self, srv_cl: ServiceClient, srv_mv: ServiceMovie):
        self.srv_cl = srv_cl
        self.srv_mv = srv_mv

    def run(self):
        while True:
            print_client_menu()
            choice = input("Give your choice here: ")
            match choice:
                case "1":
                    self.add()
                case "2":
                    self.remove()
                case "a":
                    show_all(self.srv_cl.get_all_dto())
                case "x":
                    return
                case _:
                    print("Invalid choice !")

    def add(self):
        name = input("Enter Client name: ")
        surname = input("Enter Client surname: ")
        email = input("Enter Client email: ")
        cnp = input("Enter Client cnp: ")
        age = input("Enter Client age: ")
        try:
            self.srv_cl.add(name, surname, email, cnp, age)
        except ValueError as e:
            print(f"Errors: {e}")

    def remove(self):
        choice = input(" {a} Name\n {b} Surname\n {c} CNP\nDo you want to remove by: ")
        by_what = ""
        match choice:
            case "a":
                by_what = "name"
            case "b":
                by_what = "surname"
            case "c":
                by_what = "CNP"
            case "x":
                return
            case _:
                print("Invalid choice !")
        item = input(f"Enter the {by_what} of the Client to remove: ")
        self.srv_cl.remove(item)
