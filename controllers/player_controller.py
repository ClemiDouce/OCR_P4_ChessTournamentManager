from models.player import Player
from views.player_view import PlayerView
from form.player_form import PlayerForm


class PlayerController:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = PlayerController()
        return cls._instance

    def __init__(self):
        self.player_list = []
        self.view = PlayerView()

    def get_player(self):
        first_name, last_name = self.view.ask_player_name()
        player = self.get_by_name(first_name, last_name)
        if player is not None:
            return player
        else:
            return self.create_new_player(first_name, last_name)

    def create_new_player(self, first_name=None, last_name=None):
        while True:
            if first_name is None and last_name is None:
                first_name, last_name = self.view.ask_player_name()
            if self.get_by_name(first_name, last_name) is None:
                while True:
                    player_info = self.view.new_player(first_name, last_name)
                    player_form = PlayerForm(*player_info)
                    if player_form.is_valid():
                        break
                new_player = Player(
                    len(self.player_list)+1,
                    *player_info
                )
                self.player_list.append(new_player)
                return new_player
            else:
                print('Joueur déja existant')
                first_name = last_name = None
                continue

    def get_by_id(self, player_id):
        return next((player for player in self.player_list if player.id == player_id), None)

    def get_by_name(self, first_name, last_name):
        return next((player for player in self.player_list
                     if player.first_name == first_name and player.last_name == last_name), None)

    def modify_player_elo(self):
        # self.view.show_all_players()
        pass

    def load_player_list(self):
        my_list = Player.load_all()
        for player in my_list:
            new_player = Player(
                player.doc_id,
                player['first_name'],
                player['last_name'],
                player['birth_date'],
                player['gender'],
                player['rank']
            )
            self.player_list.append(new_player)

    def save_player_list(self):
        serialized_players = [player.serialized for player in self.player_list]
        Player.save_all(serialized_players)

    def display_players(self, sort: int):
        player_list = []
        if sort == 0:
            player_list = sorted(self.player_list, key=lambda player: player.last_name)
        elif sort == 1:
            player_list = sorted(self.player_list, key=lambda player: player.rank)

        self.view.show_player_list(player_list)
