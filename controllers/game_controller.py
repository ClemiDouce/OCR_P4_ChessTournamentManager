from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from views.game_view import GameView


class GameController:
    def __init__(self):
        self.view = GameView()
        self.player_controller = PlayerController.get_instance()
        self.tournament_controller = TournamentController.get_instance()

    def launch(self):
        self.player_controller.load_player_list()
        self.tournament_controller.load_tournament_list()
        while True:
            menu_choice = self.view.show_menu_options()
            if menu_choice == 1:
                self.launch_tournament()
            elif menu_choice == 2:
                while True:
                    self.player_controller.create_new_player()
                    choice = self.view.ask_validation('Créer un autre joueur ?')
                    self.player_controller.save_player_list()
                    if choice == "0":
                        continue
                    elif choice == "1":
                        break
            elif menu_choice == 3:
                self.player_controller.modify_player_elo()
            elif menu_choice == 4:
                self.generate_rapports()
            elif menu_choice == 5:
                self.exit()
                break

    def launch_tournament(self):
        tournament = self.tournament_controller.get_tournament()
        if tournament is not None:
            self.tournament_controller.save_tournament_list()
            while True:
                choice = self.view.ask_validation('Voulez vous lancer ce tournoi tout de suite ?')
                if choice == "0":
                    self.tournament_controller.run_tournament(tournament)
                    break
                elif choice == "1":
                    break
                else:
                    continue

    def generate_rapports(self):
        while True:
            choice, subchoice = self.view.display_rapport_menu()
            if choice == 0:
                self.player_controller.display_players(subchoice)
            elif choice == 1:
                self.tournament_controller.display_tournament_player(subchoice)
            elif choice == 2:
                self.tournament_controller.display_tournaments()
            elif choice == 3:
                self.tournament_controller.display_round_tournament()
            elif choice == 4:
                self.tournament_controller.display_match_tournament()
            elif choice == 5:
                break
            choice = self.view.ask_validation('Générer un autre rapport ?')
            if choice == "0":
                continue
            elif choice == "1":
                break

    def exit(self):
        self.player_controller.save_player_list()
        self.tournament_controller.save_tournament_list()
