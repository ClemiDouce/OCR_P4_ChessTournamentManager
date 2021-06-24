from database import DBSingleton


class Tournament:
    tournament_table = DBSingleton.get_db().table('tournament')

    def __init__(self, _id, name, date, location, player_list, play_style="blitz", max_turn=4):
        self.id = _id
        self.name = name
        self.date = date
        self.location = location
        self.players = player_list
        self.max_turn = max_turn
        self.turn_list = []
        self.actual_turn = 0
        self.play_style = play_style

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'date': self.date,
            'players': [{'id_player': participant.player_id, 'score': participant.score} for participant in
                        self.players],
            'max_turn': self.max_turn,
            'turn_list': [turn.serialized() for turn in self.turn_list],
            'actual_turn': self.actual_turn,
            'time_control': self.play_style
        }

    # def check_player(self, player):
    #     checklist = set(self.players)
    #     return player in checklist

    def check_by_id(self, search_id):
        checklist = {participant.player_id for participant in self.players}
        return search_id in checklist

    @classmethod
    def load_all(cls):
        return cls.tournament_table.all()

    @classmethod
    def save_all(cls, tournament_list):
        cls.tournament_table.truncate()
        cls.tournament_table.insert_multiple(tournament_list)
