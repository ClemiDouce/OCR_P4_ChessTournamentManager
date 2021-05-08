from random import shuffle
from modeles import Joueur, Tournoi, Tour


def add_points(tournoi, match_list):
    '''
    Rajoute les points de chaque matchs aux joueurs du tournoi
    '''
    for match in match_list:
        for i, p in enumerate((p for p in tournoi.players if p[0] in [match[0][0], match[1][0]])):
            p[1] += match[i][1]


def enter_player():
    '''
    A rajouter au vues
    Demande d'ajout de joueur
    '''
    name_player = input('Entrer le nom de votre joueur : ')
    if get_player_by_name(name_player) is not None:
        return [get_player_by_name(name_player).id, 0]
    else:
        print("Ce joueur n'existe pas, je le rentre dans la base")
        new_player = Joueur(len(players), name_player, 100 + len(players))
        players.append(new_player)
        return [new_player.id, 0]


def print_tournoi_state(tournoi):
    '''
    A rajouter dans vue
    Affiche tout les joueurs ainsi que leur score de tournoi
    '''
    for player in tournoi.players:
        print(f'{get_player_by_id(player[0]).name} Score actuel : {player[1]}')


def print_match(match):
    '''
    A rajouter dans Vue
    Affiche un match
    '''
    print(f"A ma gauche, {get_player_by_id(match[0][0]).name} avec {match[0][1]}")
    print(f"A ma droite, {get_player_by_id(match[1][0]).name} avec {match[1][1]}")


def gen_match_list(player_list):
    '''
    A rajouter dans Tournoi
    Genere une liste de match
    '''
    return_list = []
    for index in range(0, len(player_list)-1, 2):
        return_list.append(
            (
                [player_list[index][0], 0],
                [player_list[index+1][0], 0]
            )
        )
    print(return_list)
    return return_list


def ask_score(match):
    '''
    A rajouter dans vue
    Demande le score de chaque participant d'un match
    '''
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


print('Lancement du tournoi')
players = [
    Joueur(0, "Mathieu", 100),
    Joueur(1, "Florence", 102),
    Joueur(2, "Sophie", 101),
    Joueur(3, "Juliette", 103),
    Joueur(4, "Clement", 104),
    Joueur(5, "Jordan", 105),
    Joueur(6, "Josselin", 106),
    Joueur(7, "William", 108)
]

tournament_player = []
while len(tournament_player) < 8:
    tournament_player.append(enter_player())

for p in players:
    print(f'{p.name} Score : {p.rank}')

tournoi = Tournoi(
    0,
    "Tournoi des trois sorciers",
    tournament_player
)

print(tournoi.players)


# Debut du tournoi
while tournoi.actual_turn < tournoi.max_turn:
    print_tournoi_state(tournoi)
    shuffle(tournoi.players)
    tournoi.actual_turn += 1
    tour = Tour(
        1,
        "Tour numero " + str(tournoi.actual_turn),
        gen_match_list(tournoi.players)
    )
    tournoi.turn_list.append(tour)
    for match in tour.match_list:
        match[0][1], match[0][1] = ask_score(match)
        print_match(match)
        # add score to player
    add_points(tournoi, tour.match_list)

print_tournoi_state(tournoi)
classement = sorted(tournoi.players, key=lambda item: item[1])
winners = list(filter(lambda player: player[1] == classement[-1][1], classement))
winners = sorted(winners, key=lambda item: get_player_by_id(item[0]).score)
for winner in winners:
    print(f"{get_player_by_id(winner[0]).name} Score : {get_player_by_id(winner[0]).rank}")
winner = get_player_by_id(classement[-1][0])
true_winner = get_player_by_id(winners[-1][0])
print(f"Le grand gagnant est {winner.name} avec {classement[-1][1]} points")
print(f"Le VRAI gagnant est {true_winner.name} avec {winners[-1][1]} points")

print(tournoi)
