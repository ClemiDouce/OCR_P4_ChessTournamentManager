from views.round_view import RoundView
from models.round import Round

class RoundController:
    def __init__(self):
        self.view = RoundView()

    def load_round(self, data):
        round_list = [
            Round(
                    round['name'],
                    [(
                        [match['p1']['id'], match['p1']['score']],
                        [match['p2']['id'], match['p2']['score']]
                    ) for match in round['match_list']],
                    round['start_time'],
                    round['end_time']
            )
            for round in data
        ]
        return round_list
