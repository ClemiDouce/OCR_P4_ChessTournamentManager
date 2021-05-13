from modeles import Joueur

option_list = [
    "Listes des joueurs",
    "Liste joueur d'un tournoi",
    "Liste de tout les tournois",
    "Liste de tout les tours d'un tournoi",
    "Liste de tout les match d'un tournoi"
]

under_option_list = [
    "Par ordre Alphabetique",
    "Par classement"
]


class View:
    @staticmethod
    def show_tournament_score(self, tournament):
        for player in tournament.players:
            id_player = player[0]
            real_player = Joueur.get_by_id(id_player)
            print(f"{real_player}'s score : {player[1]}")

    @staticmethod
    def show_menu_options():
        pass

    @staticmethod
    def show_rapport_options():
        choice = 0
        sub_choice = 0
        while True:
            try:
                for index, option in enumerate(option_list):
                    print(f"[{index}] - {option}")

                choice = int(input("Entrez l'index de l'option voulu : "))
            except ValueError:
                print("Vous n'avez pas rentré un chiffre")
                continue
            if choice not in list(range(len(option_list))):
                print("Le chiffre entré n'existe pas")
                continue

            if choice in [0, 1]:
                try:
                    for index, sub_option in enumerate(under_option_list):
                        print(f"[{index} - {sub_option}")
                    sub_choice = int(input("Entrez l'index de l'option voulu : "))
                except ValueError:
                    print("Vous n'avez pas entré un chiffre")
                if choice not in list(range(len(under_option_list))):
                    print("Le chiffre entré n'existe pas")
                    continue
                break
            else:
                break
        return choice, sub_choice

    @staticmethod
    def display_player_list(player_list):
        for player in player_list:
            player.display_stat()

    @staticmethod
    def display_tournaments(tournament_list):
        print(f"---- Liste des tournois ----")
        for tournament in tournament_list:
            tournament.display()

    @staticmethod
    def display_tournament_turn(tournament):
        print(f"---- Liste des tours du tournoi {tournament.name} ----")
        for turn in tournament.turn_list:
            print(turn)

    @staticmethod
    def display_tournament_matchs(match_list):
        for match in match_list:
            player1 = match[0][0]
            player2 = match[1][0]
            print(f"{player1} / Score : {match[0][1]}\n"
                  f"{player2} / Score : {match[1][1]}")

    @staticmethod
    def ask_tournoi_index(tournoi_list):
        while True:
            for index, tournament in enumerate(tournoi_list):
                print(f"[{index}] - {tournament.name}")
            try:
                choice = int(input("Entrez le numero du tournoi de votre choix : "))
            except ValueError:
                print("Vous n'avez pas rentré de chiffre")
                continue
            if choice not in range(len(tournoi_list)):
                print("Aucun tournoi a cette index")
                continue
            else:
                return choice

    @staticmethod
    def ask_tournament_infos():
        tournament_name = input("Entrez le nom du tournoi")
        tournament_date = input("Entrez la date du tournoi(JJ/MM/AAAA)")
        tournament_location = input("Entrez le lieu du tournoi")
        return tournament_name, tournament_date, tournament_location

    @staticmethod
    def enter_new_player(player_name):
        first_name, last_name = player_name.split(" ")
        while True:
            try:
                birth_date = input("Date de naissance (jj/mm/aaaa) : ")
                gender = input("Gender (M/F) : ")
                rank = int(input("Rang du joueur : "))
            except ValueError:
                print('Le score doit etre une valeur numérique')
                continue
            return first_name, last_name, birth_date, gender, rank

    @staticmethod
    def enter_player_name():
        player_name = input("Entrez le prenom et nom du joueur (Prenom Nom)")
        return player_name.lower()

    @staticmethod
    def ask_score(match):
        """
        A rajouter dans vue
        Demande le score de chaque participant d'un match
        """
        while True:
            try:
                p1_score = float(input(f"Score de {get_player_by_id(match[0][0]).name} : "))
                p2_score = float(input(f"Score de {get_player_by_id(match[1][0]).name} : "))
                if p1_score not in [0, 0.5, 1] or p2_score not in [0, 0.5, 1]:
                    print('Not a valid number (0, 0.5 or 1)')
                    continue
                else:
                    return p1_score, p2_score
            except ValueError as error:
                print('Sorry, not a number')
