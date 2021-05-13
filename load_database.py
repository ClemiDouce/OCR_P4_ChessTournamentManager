from pprint import pprint
from modeles import Tournoi, Joueur, Tour, list_player, list_tournoi
from random import randrange, shuffle

Joueur.load_player_list()
Tournoi.load_tournoi_list()

def gen_player_list():
    shuffle(list_player)
    return [[player.id, 0] for player in list_player[:4]]

def gen_match_list(player_list):
    return [([randrange(len(player_list)), 0], [randrange(len(player_list)), 0]) for x in range(4)]

def gen_turn_list(player_list):
    return [
        Tour('Round' + str(x), gen_match_list(player_list))
        for x in range(3)
    ]

def gen_turnament(name, date, location):
    player_list = gen_player_list()
    tournoi = Tournoi(name, date, location, player_list)
    tournoi.turn_list = gen_turn_list(player_list)

def gen_player(first, last, gender):
    Joueur(first, last, f"{randrange(31)+1}/{randrange(12)+1}/{randrange(90,99)}", gender, randrange(50, 400))

def save_all():
    Joueur.save_player_list()
    Tournoi.save_tournoi_list()
