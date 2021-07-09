from views.round_view import RoundView
from models.round import Round
from models.match import Match
from controllers.player_controller import PlayerController


class RoundController:
    _instance = None

    def __init__(self):
        self.view = RoundView()
        self.player_controller = PlayerController.get_instance()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = RoundController()
        return cls._instance

    def create_round(self, name, match_list):
        return Round(name, match_list)

    def load_round(self, data):
        round_list = [
            Round(
                round['name'],
                [Match(
                    self.player_controller.get_by_id(match["p1"]["id"]), match["p1"]["score"],
                    self.player_controller.get_by_id(match["p2"]["id"]), match["p2"]["score"]
                ) for match in round["match_list"]],
                round["start_time"],
                round["end_time"]
            )
            for round in data
        ]
        return round_list
