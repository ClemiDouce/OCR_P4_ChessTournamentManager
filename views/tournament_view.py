class TournamentView:
    def new_tournament(self):
        tournament_name = input("Entrez le nom du tournoi : ")
        tournament_location = input("Entrez le lieu du tournoi : ")
        tournament_start_date = input("Entrez la date de debut du tournoi (JJ/MM/AAAA) : ")
        tournament_end_date = input("Entrez la date de fin du tournoi (JJ/MM/AAAA) : ")
        tournament_player_number = input("Entrez le nombre de participant : ")
        tournament_max_turn = input("Entrez le nombre de tour (doit etre inferieur au nombre de joueur : ")
        tournament_play_style = input("Entrer le style de partie (bullet / blitz / coup rapide) : ")
        return (tournament_name, tournament_location, tournament_start_date, tournament_end_date,
                tournament_max_turn, tournament_player_number, tournament_play_style)

    def ask_score(self, match):
        print(f"-- {match.p1.shorted} vs {match.p2.shorted} -- ")
        print(f"Entrez le chiffre correspondant au résultat\n"
              f"[1] Victoire de {match.p1.first_name}\n"
              f"[2] Victoire de {match.p2.first_name}\n"
              "[3] Egalité\n")
        return input("Votre réponse : ")

    def ask_tournament_index(self, tournoi_list):
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

    def ask_tournament_load(self):
        while True:
            print("Voulez vous \n[0] Charger un tournoi existant\n[1] Créer un nouveau tournoi\n[2] Quitter")
            choice = input("Réponse : ")
            if choice in ["0", "1", "2"]:
                return choice
            else:
                print("Votre choix n'existe pas")

    def display_tournament_rounds(self, tournament):
        print(f"---- Liste des tours du tournoi {tournament.name} ----")
        for round in tournament.round_list:
            print(round)

    def display_tournament_matchs(self, match_list):
        for match in match_list:
            player1 = match[0][0]
            player2 = match[1][0]
            print(f"{player1} / Score : {match[0][1]}\n"
                  f"{player2} / Score : {match[1][1]}")

    def display_ranking(self, players):
        print("---- CLASSEMENT ----")
        for index, p in enumerate(players):
            player, score = p
            print(f"[{index + 1}] - {player.first_name} {player.last_name} / Score : {score}")

    def display_no_tournament(self):
        print("Il n'y a aucun tournoi")

    def display_turn(self):
        print("C'est le début du tour")

    def display_end_match(self):
        print('Fin des matchs !')

    def display_tournament_player(self, tournament, player_list):
        print(f"---- {tournament.name} ----")
        for player in player_list:
            print(player)
            print("-" * 70)

    def display_tournaments(self, list_tournament):
        print("f---- Tournaments ----")
        for tournament in list_tournament:
            print(tournament)
            print('-' * 70)

    def display_match_tournaments(self, match_list):
        for key, matchs in match_list.items():
            print(f"---- {key} ----")
            for match in matchs:
                print(match)

    def display_round_tournaments(self, round_list):
        print('Liste de match')
        print('|'.join([
            "Name".center(20),
            "Match Count".center(20),
            "Start time".center(20),
            "End time".center(20)
        ]))
        for round in round_list:
            print(round)

    def ask_stop_tournament(self):
        print("Voulez vous continuer le tournoi ?")
        print('[0] - Oui\n[1] - Non\n')
        choice = input('Votre réponse : ')
        return choice
