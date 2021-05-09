from tinydb import TinyDB

db = TinyDB('test.json')
player_table = db.table('player')
tournoi_table = db.table('tournoi')

list_player = []
list_tournoi = []


class Joueur:
    def __init__(self, name, rank):
        self.id = len(list_player)
        self.name = name
        self.rank = rank

    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'rank': self.rank,
        }

    @staticmethod
    def get_by_id(player_id):
        return next((item for item in list_player if item.id == player_id), None)

    @staticmethod
    def get_player_by_name(name):
        return next((item for item in list_player if item.name == name), None)

    @staticmethod
    def __create_player_from_csv(data):
        player = Joueur(data['name'], data['rank'])
        list_player.append(player)

    @staticmethod
    def load_player_list():
        for player in player_table.all():
            Joueur.__create_player_from_csv(player)

    @staticmethod
    def save_player_list():
        player_table.truncate()
        for player in list_player:
            print(player)
            player_table.insert(player.serialized())


class Tournoi:
    def __init__(self, name, player_list, max_turn=4):
        self.id = len(list_tournoi)
        self.name = name
        self.players = player_list
        self.max_turn = max_turn
        self.turn_list = []
        self.actual_turn = 0

    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'players': [{'id_player': x[0], 'score': x[1]} for x in self.players],
            'max_turn': self.max_turn,
            'turn_list': [turn.serialized() for turn in self.turn_list],
            'actual_turn': self.actual_turn
        }

    @staticmethod
    def __create_tournoi_from_csv(data):
        player_list = [[p['id_player'], p['score']] for p in data['players']]
        turn_list = Tour.create_tour_from_data(data['turn_list'])
        tournoi = Tournoi(data['name'], player_list, data['max_turn'])
        tournoi.turn_list = turn_list
        tournoi.actual_turn = data['actual_turn']
        list_tournoi.append(tournoi)

    @staticmethod
    def load_tournoi_list():
        for tournoi in tournoi_table.all():
            Tournoi.__create_tournoi_from_csv(tournoi)

    @staticmethod
    def save_tournoi_list():
        print("let's insert some tournament")
        tournoi_table.truncate()
        for tournoi in list_tournoi:
            tournoi_table.insert(tournoi.serialized())


class Tour:
    def __init__(self, name, match_list):
        self.name = name
        self.match_list = match_list

    def serialized(self):
        return {
            'name': self.name,
            'match_list': [
                {
                    'p1': {'id': match[0][0], 'score': match[0][1]},
                    'p2': {'id': match[1][0], 'score': match[1][1]},
                }
                for match in self.match_list]
        }

    @staticmethod
    def create_tour_from_data(data):
        print("Start turn creation")
        turn_list = [
            Tour(
                turn['name'],
                [(
                    [match['p1']['id'], match['p1']['score']],
                    [match['p2']['id'], match['p2']['score']]
                ) for match in turn['match_list']]
            )
            for turn in data
        ]
        print(turn_list)
        return turn_list

