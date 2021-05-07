class Joueur:
    def __init__(self, id, name, rank):
        self.id = id
        self.name = name
        self.rank = rank


class Tournoi:
    def __init__(self, id, name, player_list, max_turn=4):
        self.id = id
        self.name = name
        self.players = player_list
        self.max_turn = max_turn
        self.turn_list = []
        self.actual_turn = 0


class Tour:
    def __init__(self, id, name, match_list):
        self.id = id
        self.name = name
        self.match_list = match_list


class MethodeTri:
    def premier_tri(player_list):
        pass

    def second_tri(player_list):
        pass

class TriSuisse(MethodeTri):
    def premier_tri(player_list):
        pass

    def second_tri(player_list):
        pass
