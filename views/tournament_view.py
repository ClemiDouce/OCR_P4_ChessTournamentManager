class TournamentView:
    def new_tournament(self):
        while True:
            try:
                tournament_name = input("Entrez le nom du tournoi")
                tournament_date = input("Entrez la date du tournoi(JJ/MM/AAAA)")
                tournament_location = input("Entrez le lieu du tournoi")
                tournament_turn_number = input("Entrez le nombre de tour")
                tournament_play_style = input("Entrer le style de partie (bullet / blitz / coup rapide)")
                tournament_player_number = int(input("Entrez le nombre de participant"))
                return (tournament_name, tournament_date, tournament_location,
                        tournament_turn_number, tournament_player_number, tournament_play_style)
            except ValueError:
                print('Le nombre de participant doit etre un chiffre')
                continue

    def enter_score(match):
        result = -1
        player1 = match[0][0]
        player2 = match[1][0]
        print(f"-- {player1.first_name}{player1.last_name[:1]} vs"
              f" {player2.first_name}{player2.last_name[:1]} -- ")
        while True:
            try:
                result = int(input(f"Entrez le chiffre correspondant au résultat\n"
                                   f"[1] Victoire de {player1.first_name}\n"
                                   f"[2] Victoire de {player2.first_name}\n"
                                   "[3] Egalité"))
            except ValueError:
                print("Vous n'avez pas entré un chiffre")
                continue
            if result not in [1, 2, 3]:
                print("Aucun resultat correspond a ce numero de choix")
                continue
            else:
                break
        if result == 1:
            return 1, 0
        elif result == 2:
            return 0, 1
        else:
            return 0.5, 0.5

    def display_tournament_rounds(self, tournament):
        print(f"---- Liste des tours du tournoi {tournament.name} ----")
        for turn in tournament.turn_list:
            print(turn)

    def display_tournament_matchs(self, match_list):
        for match in match_list:
            player1 = match[0][0]
            player2 = match[1][0]
            print(f"{player1} / Score : {match[0][1]}\n"
                  f"{player2} / Score : {match[1][1]}")

    def ask_tournoi_index(self, tournoi_list):
        while True:
            for index, tournament in enumerate(tournoi_list):
                print(f"[{index}] - {tournament.name}")
            try:
                choice = int(input("Entrez le numero du tournoi de votre choix : "))
            except ValueError:
                print("Vous n'avez pas rentré de chiffre")
                continue
            if choice not in range(len(tournoi_list)):
                print("Aucun tournoi correspond a cet index")
                continue
            else:
                return choice

    def display_ranking(self, players):
        print("---- CLASSEMENT ----")
        for index, p in enumerate(players):
            player, score = p
            print(f"[{index + 1}] - {player.first_name} {player.last_name} / Score : {score}")

    def enter_score(self, match):
        result = -1
        player1 = match[0][0]
        player2 = match[1][0]
        print(f"-- {player1.first_name}{player1.last_name[:1]} vs"
              f" {player2.first_name}{player2.last_name[:1]} -- ")
        while True:
            try:
                result = int(input(f"Entrez le chiffre correspondant au résultat\n"
                                   f"[1] Victoire de {player1.first_name}\n"
                                   f"[2] Victoire de {player2.first_name}\n"
                                   "[3] Egalité"))
            except ValueError:
                print("Vous n'avez pas entré un chiffre")
                continue
            if result not in [1, 2, 3]:
                print("Aucun resultat correspond a ce numero de choix")
                continue
            else:
                break
        if result == 1:
            return 1, 0
        elif result == 2:
            return 0, 1
        else:
            return 0.5, 0.5