from modeles import Joueur


class View:
    @staticmethod
    def show_tournament_score(tournament):
        for player in tournament.players:
            id_player = player[0]
            real_player = Joueur.get_by_id(id_player)
            print(f"{real_player}'s score : {player[1]}")
