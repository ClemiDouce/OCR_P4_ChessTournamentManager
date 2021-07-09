from form.base_form import BasicForm


class TournamentForm(BasicForm):
    def __init__(self, name, location, start_date, end_date, max_turn, player_count, play_style):
        super().__init__()
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.max_turn = max_turn
        self.player_count = player_count
        self.play_style = play_style

    def is_valid(self):
        tests = [
            self.is_string_between("Nom de tournoi", self.name, 2, 20),
            self.is_string_between("Lieu", self.location, 2, 20),
            self.is_digit_between("Nombre de tour", self.max_turn, 0, int(self.player_count),
                                  borne_error="Le nombre de tour doit etre inferieur au nombre de joueur"),
            self.is_digit_between("Nombre de joueur", self.player_count, 1, 9),
            self.valid_play_style(),
            self.check_date("Date de début", self.start_date),
            self.check_date("Date de fin", self.end_date)
        ]

        if all(tests):
            return True
        else:
            self.display_error()
            return False

    def valid_play_style(self):
        if self.play_style.lower() in ['blitz', 'bullet', 'rapide']:
            return True
        else:
            self.errors.append('Style de jeu incorrect. (blitz, bullet ou rapide)')
            return False
