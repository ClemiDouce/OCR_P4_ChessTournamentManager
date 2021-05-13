from random import shuffle

import modeles
from modeles import Joueur, Tournoi, Tour, list_player, list_tournoi
from view import View
from collections import namedtuple
from enum import Enum


class Rapports(Enum):
    PLAYERS = 0
    PLAYERS_TOURNAMENT = 1
    TOURNAMENTS = 2
    TURNS_TOURNAMENT = 3
    MATCHS_TOURNAMENT = 4


class TriStyle(Enum):
    SCORE = 1
    ALPHABETIQUE = 0


def tri_suisse(list_player):
    pass


def add_points(tournoi, match_list):
    """
    Rajoute les points de chaque matchs aux joueurs du tournoi
    """
    for match in match_list:
        for i, p in enumerate((p for p in tournoi.players if p[0] in [match[0][0], match[1][0]])):
            p[1] += match[i][1]


# def print_tournoi_state(tournoi):
#     """
#     A rajouter dans vue
#     Affiche tout les joueurs ainsi que leur score de tournoi
#     """
#     for player in tournoi.players:
#         print(f'{get_player_by_id(player[0]).name} Score actuel : {player[1]}')
#
#
# def print_match(match):
#     """
#     A rajouter dans Vue
#     Affiche un match
#     """
#     print(f"A ma gauche, {get_player_by_id(match[0][0]).name} avec {match[0][1]}")
#     print(f"A ma droite, {get_player_by_id(match[1][0]).name} avec {match[1][1]}")


def launch_tournament():
    t_name, t_date, t_location = View.ask_tournament_infos()
    print('Lancement du tournoi')
    tournament_player = []
    while len(tournament_player) < 3:
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

    tournoi = Tournoi(
            t_name,
            t_date,
            t_location,
            tournament_player
    )

    print(tournoi.players)

    # Debut du tournoi
    # while tournoi.actual_turn < tournoi.max_turn:
    #     print(tournoi)
    #     shuffle(tournoi.players)
    #     tournoi.actual_turn += 1
    #     tour = Tour(
    #             1,
    #             "Tour numero " + str(tournoi.actual_turn),
    #             gen_match_list(tournoi.players)
    #     )
    #     tournoi.turn_list.append(tour)
    #     for match in tour.match_list:
    #         match[0][1], match[0][1] = ask_score(match)
    #         print_match(match)
    #         # add score to player
    #     add_points(tournoi, tour.match_list)


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
                players_to_show = sorted(modeles.list_player, key=lambda player: player.rank)
            elif sub_choice == TriStyle.ALPHABETIQUE.value:
                players_to_show = sorted(modeles.list_player, key=lambda player: player.last_name)
            View.display_player_list(players_to_show)

        elif choice == Rapports.PLAYERS_TOURNAMENT.value:
            players_to_show = []
            tournoi_choice = View.ask_tournoi_index(list_tournoi)
            tournament = list_tournoi[tournoi_choice]
            player_list = [Joueur.get_by_id(p[0]) for p in tournament.players]
            if sub_choice == TriStyle.SCORE.value:
                players_to_show = sorted(player_list, key=lambda player: player.rank)
            elif sub_choice == TriStyle.ALPHABETIQUE.value:
                players_to_show = sorted(player_list, key=lambda player: player.last_name)
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

# Debut du programme
if __name__ == "__main__":
    Joueur.load_player_list()
    Tournoi.load_tournoi_list()
