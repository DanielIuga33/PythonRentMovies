from service.ServiceClient import ServiceClient
from service.ServiceMovie import ServiceMovie
from ui.UserInterfaceClient import UserInterfaceClient
from ui.UserInterfaceMovie import UserInterfaceMovie
from utils.Prints import print_main_menu


class UserInterface:
    def __init__(self, srv_cl: ServiceClient, srv_mv: ServiceMovie):
        self.srv_cl = srv_cl
        self.srv_mv = srv_mv
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
                case "x":
                    return
                case _:
                    print("Invalid choice !")
