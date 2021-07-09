from database import DBSingleton


class Tournament:
    tournament_table = DBSingleton.get_db().table('tournament')

    def __init__(self, _id, name, start_date, end_date, location, player_list, play_style="blitz", max_turn=4):
        self.id = _id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.players = player_list
        self.max_turn = max_turn
        self.round_list = []
        self.actual_turn = 0
        self.play_style = play_style

    def __str__(self):
        ended = "Termine" if self.actual_turn == self.max_turn else "En cours"
        return "|".join([
            self.name.center(10),
            self.start_date.center(12),
            self.end_date.center(12),
            self.location.center(15),
            str(len(self.players)).center(5),
            str(self.max_turn).center(5),
            self.play_style.center(10),
            ended.center(10)
        ])

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'players': [participant.serialize() for participant in
                        self.players],
            'max_turn': self.max_turn,
            'round_list': [turn.serialized() for turn in self.round_list],
            'actual_turn': self.actual_turn,
            'time_control': self.play_style
        }

    # def check_player(self, player):
    #     checklist = set(self.players)
    #     return player in checklist

    def add_point(self, match):
        tournament_player_1 = self.get_participant_by_id(match.p1.id)
        tournament_player_1.score += match.p1_score

        tournament_player_2 = self.get_participant_by_id(match.p2.id)
        tournament_player_2.score += match.p2_score

    def get_participant_by_id(self, id):
        return next((participant for participant in self.players if participant.id == id), None)

    def check_by_id(self, search_id):
        checklist = {participant.id for participant in self.players}
        return search_id in checklist

    @classmethod
    def load_all(cls):
        return cls.tournament_table.all()

    @classmethod
    def save_all(cls, tournament_list):
        cls.tournament_table.truncate()
        cls.tournament_table.insert_multiple(tournament_list)
