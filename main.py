from menuenums import Menu, Rapports, TriStyle
from modeles import Joueur, Tour, Tournoi, list_player, list_tournoi
from view import View


def launch_tournament():
    t_name, t_date, t_location, t_turn_cnt, t_player_cnt, t_play_style = View.ask_tournament_infos()
    print(' ---- Lancement du tournoi ----')
    tournament_player = []
    while len(tournament_player) < t_player_cnt:
        # Demande nom
        player_name = View.enter_player_name()
        # Verification Nom
        player = Joueur.exist(player_name)
        if player is not None:
            tournament_player.append([player.id, 0])
        else:
            print(f"Aucun joueur du nom de {player_name} dans notre base de donnée")
            p_first_name, p_last_name, p_birth_date, p_gender, p_rank = View.enter_new_player(player_name)
            new_player = Joueur(p_first_name, p_last_name, p_birth_date, p_gender, p_rank)
            tournament_player.append([new_player.id, 0])

    with Tournoi(
            t_name,
            t_date,
            t_location,
            tournament_player,
            t_player_cnt
    ) as tournoi:

        # Debut du tournoi
        while tournoi.actual_turn < tournoi.max_turn:
            tournoi.actual_turn += 1
            if tournoi.actual_turn == 1:
                matchs = tournoi.tri_suisse()
            else:
                matchs = tournoi.tri_francais()
            tour = Tour(
                    f"Round {tournoi.actual_turn}",
                    matchs
            )
            tournoi.turn_list.append(tour)
            print(f"---- {tour.name} ----")
            for match in tour.match_list:
                # Demander le score
                player1 = Joueur.get_by_id(match[0][0])
                player2 = Joueur.get_by_id(match[1][0])
                match[0][1], match[1][1] = View.ask_score(
                        f"{player1.first_name}.{player1.last_name[:1]}",
                        f"{player2.first_name}.{player2.last_name[:1]}"
                )
                # Ajouter le score a chaque joueur
                tournoi.add_point(match)


# def _search_winner():
#     print_tournoi_state(tournoi)
#     classement = sorted(tournoi.players, key=lambda item: item[1])
#     winners = list(filter(lambda player: player[1] == classement[-1][1], classement))
#     winners = sorted(winners, key=lambda item: get_player_by_id(item[0]).score)
#     for winner in winners:
#         print(f"{get_player_by_id(winner[0]).name} Score : {get_player_by_id(winner[0]).rank}")
#     winner = get_player_by_id(classement[-1][0])
#     true_winner = get_player_by_id(winners[-1][0])
#     print(f"Le grand gagnant est {winner.name} avec {classement[-1][1]} points")
#     print(f"Le VRAI gagnant est {true_winner.name} avec {winners[-1][1]} points")


def generation_rapport():
    while True:
        choice, sub_choice = View.show_rapport_options()
        print(choice, sub_choice)
        if choice == Rapports.PLAYERS.value:
            players_to_show = []
            if sub_choice == TriStyle.SCORE.value:
                players_to_show = sorted(list_player, key=lambda player: player.rank)
            elif sub_choice == TriStyle.ALPHABETIQUE.value:
                players_to_show = sorted(list_player, key=lambda player: player.last_name)
            View.display_player_list(players_to_show)

        elif choice == Rapports.PLAYERS_TOURNAMENT.value:
            players_to_show = []
            tournoi_choice = View.ask_tournoi_index(list_tournoi)
            tournament = list_tournoi[tournoi_choice]
            player_list = [Joueur.get_by_id(p[0]) for p in tournament.players]
            if sub_choice == TriStyle.SCORE.value:
                players_to_show = sorted(
                        player_list,
                        key=lambda player: player.rank
                )
            elif sub_choice == TriStyle.ALPHABETIQUE.value:
                players_to_show = sorted(
                        player_list,
                        key=lambda player: player.last_name
                )
            View.display_player_list(players_to_show)

        elif choice == Rapports.TOURNAMENTS.value:
            View.display_tournaments(list_tournoi)

        elif choice == Rapports.TURNS_TOURNAMENT.value:
            tournoi_choice = View.ask_tournoi_index(list_tournoi)
            tournament = list_tournoi[tournoi_choice]
            View.display_tournament_turn(tournament)

        elif choice == Rapports.MATCHS_TOURNAMENT.value:
            tournoi_choice = View.ask_tournoi_index(list_tournoi)
            tournament = list_tournoi[tournoi_choice]
            show_match = []
            for turn in tournament.turn_list:
                for match in turn.match_list:
                    match[0][0] = Joueur.get_by_id(match[0][0])
                    match[1][0] = Joueur.get_by_id(match[1][0])
                    show_match.append(match)
            View.display_tournament_matchs(show_match)
        elif choice == Rapports.RETOUR_MENU.value:
            break


# Debut du programme
if __name__ == "__main__":
    Joueur.load_player_list()
    Tournoi.load_tournoi_list()

    while True:
        menu_choice = View.show_menu_options()
        if menu_choice == Menu.LAUNCH_TOURNAMENT.value:
            launch_tournament()
        elif menu_choice == Menu.MODIFICATION.value:
            pass
        elif menu_choice == Menu.RAPPORT.value:
            generation_rapport()
        elif menu_choice == Menu.QUIT.value:
            Joueur.save_player_list()
            Tournoi.save_tournoi_list()
            break
