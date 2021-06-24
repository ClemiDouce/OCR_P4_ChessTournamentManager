from .tournament_controller import TournamentController
from .player_controller import PlayerController
# from .rapports_controller import RapportsController
from views.game_view import GameView


class GameController:
    def __init__(self):
        self.view = GameView()
        self.player_controller = PlayerController.get_instance()
        self.tournament_controller = TournamentController()

    def launch(self):
        self.player_controller.load_player_list()
        self.tournament_controller.load_tournament_list()
        self.launch_tournament()
        self.exit()
        # while True:
        #     menu_choice = self.view.show_menu_options()
        #     if menu_choice == Menu.LAUNCH_TOURNAMENT.value:
        #         self.launch_tournament()
        #     elif menu_choice == Menu.MODIFICATION.value:
        #         self.modify_player()
        #     elif menu_choice == Menu.RAPPORT.value:
        #         self.generation_rapport()
        #     elif menu_choice == Menu.QUIT.value:
        #         self.exit_program()
        #         break

    def launch_tournament(self):
        new_tournament = self.tournament_controller.create_new_tournament()


    def exit(self):
        self.player_controller.save_player_list()
        self.tournament_controller.save_tournament_list()
