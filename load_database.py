import pprint
from modeles import Tournoi, Joueur, Tour, list_player, list_tournoi

Joueur.load_player_list()

tournoi = Tournoi(
        "Winterfield",
        [[player.id, 0] for player in list_player])

turn_list = [
    Tour('Round1', [([turn, 0], [0, turn]) for turn in range(4)]),
    Tour('Round2', [([turn, 0], [0, turn]) for turn in range(4)]),
    Tour('Round3', [([turn, 0], [0, turn]) for turn in range(4)]),
]

tournoi.turn_list = turn_list

tournoi_2 = Tournoi(
        "Le tournoi des 15",
        [[player.id, 0] for player in list_player])

turn_list_2 = [
    Tour('Round1', [([turn, 2], [1, turn]) for turn in range(4)]),
    Tour('Round2', [([turn, 1], [2, turn]) for turn in range(4)]),
    Tour('Round3', [([turn, 3], [1, turn]) for turn in range(4)]),
]

tournoi_2.turn_list = turn_list_2

list_tournoi.append(tournoi)
list_tournoi.append(tournoi_2)


