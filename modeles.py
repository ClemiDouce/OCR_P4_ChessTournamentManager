from tinydb import TinyDB

from utils import get_now_time, split_array_in_half

db = TinyDB('database.json')
player_table = db.table('player')
tournoi_table = db.table('tournoi')

list_player = []
list_tournoi = []


class Joueur:
    def __init__(self, first_name, last_name, birth_date, gender, rank):
        self.id = len(list_player)
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        list_player.append(self)

    def serialized(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'rank': self.rank,
        }

    def display_stat(self):
        print(f"{self.first_name} {self.last_name}\n"
              f"Birthdate : {self.birth_date} / Genre : {self.gender}\n"
              f"Rank : {self.rank}")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'({self.id}, {self.first_name}, {self.last_name}, {self.rank})')

    @staticmethod
    def get_by_id(player_id):
        return next((item for item in list_player if item.id == player_id), None)

    @staticmethod
    def exist(complete_name):
        return next((item for item in list_player if str(item).lower() == complete_name), None)

    @staticmethod
    def _create_player_from_dict(data):
        Joueur(data['first_name'], data['last_name'], data['birth_date'], data['gender'], data['rank'])

    @staticmethod
    def load_player_list():
        for player in player_table.all():
            Joueur._create_player_from_dict(player)

    @staticmethod
    def save_player_list():
        player_table.truncate()
        for player in list_player:
            print(player)
            player_table.insert(player.serialized())


class Tournoi:
    def __init__(self, name, date, location, player_list, play_style="blitz", max_turn=4):
        self.id = len(list_tournoi)
        self.name = name
        self.date = date
        self.location = location
        self.players = player_list
        self.max_turn = max_turn
        self.turn_list = []
        self.actual_turn = 0
        self.play_style = play_style
        list_tournoi.append(self)

    def __enter__(self):
        print(f"---- Bienvenue au tournoi {self.name} ---- !")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Merci d'avoir participé ! A bientot au tournoi de {self.name}")

    def __str__(self):
        return f""

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.max_turn})"

    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'date': self.date,
            'players': [{'id_player': x[0], 'score': x[1]} for x in self.players],
            'max_turn': self.max_turn,
            'turn_list': [turn.serialized() for turn in self.turn_list],
            'actual_turn': self.actual_turn,
            'time_control': self.play_style
        }

    def display(self):
        print(f"{self.name}\n"
              f"Date : {self.date} / Location : {self.location}\n")

    def match_exist(self, p1, p2):
        participants = sorted([p1, p2])
        for turn in self.turn_list:
            if participants in turn.get_matchs_pair():
                return True
        return False

    def tri_suisse(self):
        sorted_list = sorted(self.players, key=lambda p: Joueur.get_by_id(p[0]).rank)
        first_half, second_half = split_array_in_half(sorted_list)
        match_list = [([first_half[i][0], 0], [second_half[i][0], 0]) for i in range(len(first_half))]
        return match_list

    def tri_francais(self):
        match_list = []
        used_id = set()
        sorted_players = sorted(self.players, key=lambda p: (p[1], Joueur.get_by_id(p[0]).rank))
        for index, player in enumerate(sorted_players):
            i = 1
            player_id = player[0]
            if player_id in used_id:
                continue
            while index + i < len(sorted_players):
                other_player_id = sorted_players[index + i][0]
                if other_player_id in used_id:
                    i += 1
                    continue
                if self.match_exist(player_id, other_player_id):
                    i += 1
                    continue
                else:
                    match_list.append(([player_id, 0], [other_player_id, 0]))
                    used_id.update({player_id, other_player_id})
                    break
        return match_list

    def get_tournament_player_by_id(self, player_id):
        return next((player for player in self.players if player[0] == player_id), None)

    def add_point(self, match):
        for player in match:
            player_to_add = player[0]
            searched_player = self.get_tournament_player_by_id(player_to_add)
            searched_player[1] += player[1]
            print(f"{player[1]} ajouté au joueur {searched_player}")

    @staticmethod
    def _create_tournoi_from_dict(data):
        player_list = [[p['id_player'], p['score']] for p in data['players']]
        turn_list = Tour.create_tour_from_data(data['turn_list'])
        tournoi = Tournoi(data['name'], data['date'], data['location'], player_list, data['time_control'],
                          data['max_turn'])
        tournoi.turn_list = turn_list
        tournoi.actual_turn = data['actual_turn']

    @staticmethod
    def load_tournoi_list():
        for tournoi in tournoi_table.all():
            Tournoi._create_tournoi_from_dict(tournoi)

    @staticmethod
    def save_tournoi_list():
        tournoi_table.truncate()
        for tournoi in list_tournoi:
            tournoi_table.insert(tournoi.serialized())


class Tour:
    def __init__(self, name, match_list, start_time="", end_time=""):
        self.name = name
        self.match_list = match_list
        self.start_time = get_now_time() if start_time == "" else start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} / Start time : {self.start_time} / End time : {self.end_time}"

    def serialized(self):
        return {
            'name': self.name,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'match_list': [
                {
                    'p1': {'id': match[0][0], 'score': match[0][1]},
                    'p2': {'id': match[1][0], 'score': match[1][1]},
                }
                for match in self.match_list]
        }

    def get_matchs_pair(self):
        return [sorted([match[0][0], match[1][0]]) for match in self.match_list]

    @staticmethod
    def create_tour_from_data(data):
        turn_list = [
            Tour(
                    turn['name'],
                    [(
                        [match['p1']['id'], match['p1']['score']],
                        [match['p2']['id'], match['p2']['score']]
                    ) for match in turn['match_list']],
                    turn['start_time'],
                    turn['end_time']
            )
            for turn in data
        ]
        return turn_list
