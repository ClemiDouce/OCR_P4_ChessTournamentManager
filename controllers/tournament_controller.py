from models.tournament import Tournament
from models.participant import Participant
from models.match import Match

from views.tournament_view import TournamentView
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController
from form.tournament_form import TournamentForm

from utils import split_array_in_half, get_now_time


class TournamentController:
    _instance = None

    def __init__(self):
        self.tournament_list = []
        self.view = TournamentView()
        self.round_controller = RoundController.get_instance()
        self.player_controller = PlayerController.get_instance()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = TournamentController()
        return cls._instance

    def get_tournament(self):
        while True:
            choice = self.view.ask_tournament_load()
            if choice == "0":
                return self.get_active_tournament()
            elif choice == "1":
                return self.create_new_tournament()
            elif choice == "2":
                return None

    def create_new_tournament(self):
        while True:
            (
                t_name,
                t_location,
                t_start_date,
                t_end_date,
                t_max_turn,
                t_player_cnt,
                t_play_style
            ) = self.view.new_tournament()
            tournament_validator = TournamentForm(
                t_name, t_location,
                t_start_date, t_end_date,
                t_max_turn, t_player_cnt, t_play_style
            )
            if tournament_validator.is_valid():
                break
        tournoi = Tournament(
            len(self.tournament_list),
            t_name,
            t_start_date,
            t_end_date,
            t_location,
            [],
            t_play_style,
            int(t_max_turn)
        )
        while len(tournoi.players) < int(t_player_cnt):
            player = self.player_controller.get_player()
            if not tournoi.check_by_id(player.id):
                tournoi.players.append(Participant(player.id))
            else:
                print('Ce joueur est déja présent dans le tournoi')
        self.tournament_list.append(tournoi)
        return tournoi

    def run_tournament(self, tournament):
        while tournament.actual_turn < tournament.max_turn:
            tournament.actual_turn += 1
            if tournament.actual_turn == 1:
                matchs = self.first_sorting(tournament)
            else:
                matchs = self.second_sorting(tournament)
            actual_round = self.round_controller.create_round(f"Round {tournament.actual_turn}", matchs)
            tournament.round_list.append(actual_round)
            self.view.display_turn()
            self.run_round(tournament, actual_round)
            if tournament.actual_turn < tournament.max_turn - 1:
                stop_tournament = self.view.ask_stop_tournament()
                if stop_tournament == "0":
                    continue
                elif stop_tournament == "1":
                    self.save_tournament_list()
                    return

        # annonce du gagnant
        self.search_winner(tournament)
        print(f"--- Fin du tournoi {tournament.name} ---")
        self.save_tournament_list()
        self.view.display_end_match()

    def run_round(self, tournament, round):
        for match in round.match_list:
            while True:
                result = self.view.ask_score(match)
                if result in {"1", "2", "3"}:
                    break
                else:
                    continue
            if result == "1":
                match.p1_score, match.p2_score = 1, 0
            elif result == "2":
                match.p1_score, match.p2_score = 0, 1
            else:
                match.p1_score, match.p2_score = 0.5, 0.5
            tournament.add_point(match)
        round.end_time = get_now_time()

    def sort_by_score_and_rank(self, participant):
        player_rank = self.player_controller.get_by_id(participant.id).rank
        return participant.score, player_rank

    def search_winner(self, tournoi):
        # sort by score and ranking
        classement = sorted(tournoi.players, key=self.sort_by_score_and_rank, reverse=True)

        # recuperation des joueurs ayant le score maximum
        best_score = list(
                (
                    self.player_controller.get_by_id(participant.id),
                    participant.score
                )
                for participant in classement
        )
        self.view.display_ranking(best_score)

    def get_active_tournament(self):
        list_tournament = [
            tournament for tournament in self.tournament_list
            if tournament.actual_turn < tournament.max_turn
        ]
        if len(list_tournament) == 0:
            self.view.display_no_tournament()
            return None
        choice = self.view.ask_tournament_index(list_tournament)
        return list_tournament[choice]

    def first_sorting(self, tournament):
        sorted_list = sorted(
                tournament.players,
                key=lambda p: self.player_controller.get_by_id(p.id).rank
        )
        first_half, second_half = split_array_in_half(sorted_list)
        match_list = [
            self.create_match(
                first_half[i],
                second_half[i]
            )
            for i in range(len(first_half))
        ]
        return match_list

    def second_sorting(self, tournament):
        match_list = []
        used_id = set()
        sorted_participants = sorted(
            tournament.players, key=lambda p: (
                    p.score,
                    self.player_controller.get_by_id(p.id).rank
            )
        )
        for index, participant in enumerate(sorted_participants):
            i = 1
            if participant.id in used_id:
                continue
            while index + i < len(sorted_participants):
                other_participant = sorted_participants[index + i]
                if other_participant.id in used_id or other_participant.id in participant.old_matchs:
                    i += 1
                    if i == len(sorted_participants):
                        match_list.append(
                            self.create_match(
                                    participant, other_participant
                            )
                        )
                        used_id.update({participant.id, other_participant})
                        break
                    continue
                else:
                    match_list.append(
                        self.create_match(
                                participant, other_participant
                        )
                    )
                    used_id.update({participant.id, other_participant.id})
                    break
        return match_list

    def create_match(self, participant_1, participant_2):
        participant_1.old_matchs.add(participant_2.id)
        participant_2.old_matchs.add(participant_1.id)
        return Match(
                self.player_controller.get_by_id(participant_1.id), 0,
                self.player_controller.get_by_id(participant_2.id), 0
        )

    # Rapport
    def display_tournament_player(self, sort: int):
        if len(self.tournament_list) == 0:
            self.view.display_no_tournament()
            return

        choice = self.view.ask_tournament_index(self.tournament_list)
        tournament = self.tournament_list[choice]
        player_list = [self.player_controller.get_by_id(player.id) for player in tournament.players]
        if sort == 0:
            player_list = sorted(player_list, key=lambda player: player.last_name)
        elif sort == 1:
            player_list = sorted(player_list, key=lambda player: player.rank)
        self.view.display_tournament_player(tournament, player_list)

    def display_tournaments(self):
        self.view.display_tournaments(self.tournament_list)

    def display_match_tournament(self):
        choice = self.view.ask_tournament_index(self.tournament_list)
        tournament = self.tournament_list[choice]
        match_list = {}
        for round in tournament.round_list:
            match_list[round.name] = round.match_list
        self.view.display_match_tournaments(match_list)

    def display_round_tournament(self):
        choice = self.view.ask_tournament_index(self.tournament_list)
        tournament = self.tournament_list[choice]
        self.view.display_round_tournaments(tournament.round_list)

    def load_tournament_list(self):
        my_list = Tournament.load_all()
        for tournament in my_list:
            player_list = [
                Participant(participant['id'], participant['score'], set(participant['old_matchs']))
                for participant in tournament['players']
            ]
            round_list = self.round_controller.load_round(tournament['round_list'])
            tournoi = Tournament(
                tournament.doc_id,
                tournament['name'],
                tournament['start_date'],
                tournament['end_date'],
                tournament['location'],
                player_list,
                tournament['time_control'],
                tournament['max_turn']
            )
            tournoi.round_list = round_list
            tournoi.actual_turn = tournament['actual_turn']
            self.tournament_list.append(tournoi)

    def save_tournament_list(self):
        serialized_tournament = [tournament.serialized for tournament in self.tournament_list]
        Tournament.save_all(serialized_tournament)
