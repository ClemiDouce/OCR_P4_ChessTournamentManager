from models.player import Player
from views.player_view import PlayerView


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
        print(f"Existence du joueur {first_name} {last_name} : {player}")
        if player is not None:
            return player
        else:
            return self.add_player(first_name, last_name)

    def add_player(self, first_name, last_name):
        player_info = self.view.new_player(first_name, last_name)
        new_player = Player(
                len(self.player_list),
                *player_info
        )
        self.player_list.append(new_player)
        return new_player

    def get_by_id(self, player_id):
        return next((player for player in self.player_list if player.id == player_id), None)

    def get_by_name(self, first_name, last_name):
        return next((player for player in self.player_list if player.first_name == first_name and player.last_name
                     == last_name), None)

    def modify_player_elo(self):
        self.view.show_all_players()


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
