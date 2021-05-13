menus = [
    "Lancer un tournoi",
    "Modification",
    "Rapport",
    "Quitter"
]

modifications = [
    "Joueur",
    "Tournoi"
]

modif_tournoi = [
    "Nom",
    "Date",
    "Lieu"
]

modif_joueur = [
    "Nom",
    "Prenom",
    "Date de naissance",
    "Sexe",
    "Classement"
]

rapport_list = [
    "Listes des joueurs",
    "Liste joueur d'un tournoi",
    "Liste de tout les tournois",
    "Liste de tout les tours d'un tournoi",
    "Liste de tout les match d'un tournoi",
    "Retour"
]

under_rapport_list = [
    "Par ordre Alphabetique",
    "Par classement"
]


class View:
    @staticmethod
    def show_tournament_score(tournament):
        pass

    @staticmethod
    def show_menu_options():
        choice = 0
        while True:
            try:
                for index, option in enumerate(menus):
                    print(f"[{index}] - {option}")
                choice = int(input("Entrez l'index de l'option voulu : "))
            except ValueError:
                print("Vous n'avez pas rentré un chiffre")
                continue
            if choice not in list(range(len(rapport_list))):
                print("Le chiffre entré n'existe pas")
                continue
            else:
                break
        return choice

    @staticmethod
    def show_rapport_options():
        choice = 0
        sub_choice = 0
        while True:
            try:
                for index, option in enumerate(rapport_list):
                    print(f"[{index}] - {option}")

                choice = int(input("Entrez l'index de l'option voulu : "))
            except ValueError:
                print("Vous n'avez pas rentré un chiffre")
                continue
            if choice not in list(range(len(rapport_list))):
                print("Le chiffre entré n'existe pas")
                continue

            if choice in [0, 1]:
                try:
                    for index, sub_option in enumerate(under_rapport_list):
                        print(f"[{index}] - {sub_option}")
                    sub_choice = int(input("Entrez l'index de l'option voulu : "))
                except ValueError:
                    print("Vous n'avez pas entré un chiffre")
                if choice not in list(range(len(under_rapport_list))):
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
        print("---- Liste des tournois ----")
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
        tournament_turn_number = input("Entrez le nombre de tour")
        tournament_play_style = input("Entrer le style de partie (bullet / blitz / ...)")
        tournament_player_number = input("Entrez le nombre de participant")
        return (tournament_name, tournament_date, tournament_location,
                tournament_turn_number, tournament_player_number, tournament_play_style)

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
    def ask_score(p1_name, p2_name):
        print(f"Match opposant {p1_name} contre {p2_name}")
        while True:
            try:
                p1_score = float(input(f"Score de  {p1_name} : "))
                p2_score = float(input(f"Score de {p2_name} : "))
                if p1_score not in [0, 0.5, 1] or p2_score not in [0, 0.5, 1]:
                    print('Not a valid number (0, 0.5 or 1)')
                    continue
                else:
                    return p1_score, p2_score
            except ValueError as error:
                print("Vous n'avez pas entré de nombre", error)

    @staticmethod
    def display_tournament_board(players):
        pass
