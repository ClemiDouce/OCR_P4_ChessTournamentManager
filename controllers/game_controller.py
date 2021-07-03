from .tournament_controller import TournamentController
from .player_controller import PlayerController
from .rapports_controller import RapportsController
from views.game_view import GameView


class GameController:
    def __init__(self):
        self.view = GameView()
        self.player_controller = PlayerController.get_instance()
        self.tournament_controller = TournamentController.get_instance()
        self.rapport_controller = RapportsController

    def launch(self):
        self.player_controller.load_player_list()
        self.tournament_controller.load_tournament_list()
        while True:
            menu_choice = self.view.show_menu_options()
            if menu_choice == 1:
                self.launch_tournament()
                break
            elif menu_choice == 2:
                self.player_controller.create_new_player()
                break
            elif menu_choice == 3:
                self.player_controller.modify_player_elo()
                break
            elif menu_choice == 4:
                self.exit()
                break
            elif menu_choice == 5:
                pass

    def launch_tournament(self):
        tournament = self.tournament_controller.get_tournament()


    def exit(self):
        self.player_controller.save_player_list()
        self.tournament_controller.save_tournament_list()
