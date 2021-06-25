from collections import namedtuple

from models.tournament import Tournament

from views.tournament_view import TournamentView

from .round_controller import RoundController
from .player_controller import PlayerController

Participant = namedtuple('Participant', 'player_id, score')


class TournamentController:
    _instance = None

    def __init__(self):
        self.tournament_list = []
        self.view = TournamentView()
        self.round_controller = RoundController()
        self.player_controller = PlayerController.get_instance()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = TournamentController()
        return cls._instance

    def create_new_tournament(self):
        t_name, t_date, t_location, t_max_turn, t_player_cnt, t_play_style = self.view.new_tournament()
        tournoi = Tournament(
                len(self.tournament_list),
                t_name,
                t_date,
                t_location,
                [],
                t_play_style,
                t_max_turn
        )
        while len(tournoi.players) < t_player_cnt:
            player = self.player_controller.get_player()
            if not tournoi.check_by_id(player.id):
                print("Player not in tournament")
                tournoi.players.append(Participant(player.id, 0))
            else:
                print('Player already in the tournament')
            print(player)
        self.tournament_list.append(tournoi)
        return tournoi

    def load_tournament_list(self):
        my_list = Tournament.load_all()
        for tournament in my_list:
            player_list = [[p['id_player'], p['score']] for p in tournament['players']]
            turn_list = self.round_controller.load_round(tournament['turn_list'])
            tournoi = Tournament(
                    tournament.doc_id,
                    tournament['name'],
                    tournament['date'],
                    tournament['location'],
                    player_list,
                    tournament['time_control'],
                    tournament['max_turn']
            )
            tournoi.turn_list = turn_list
            tournoi.actual_turn = tournament['actual_turn']
            self.tournament_list.append(tournoi)

    def save_tournament_list(self):
        serialized_tournament = [tournament.serialized for tournament in self.tournament_list]
        Tournament.save_all(serialized_tournament)
