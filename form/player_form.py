from form.base_form import BasicForm


class PlayerForm(BasicForm):
    def __init__(self, first_name, last_name, birth_date, gender, rank):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank

    def is_valid(self):
        tests = [
            self.is_string_between("Prenom", self.first_name, 2, 20),
            self.is_string_between("Nom", self.last_name, 2, 20),
            self.check_date("Date de naissance", self.birth_date),
            self.check_gender(),
            self.is_digit_between("Rank", self.rank, -1, 9999)
        ]
        if all(tests):
            return True
        else:
            self.display_error()
            return False

    def check_gender(self):
        if self.gender.lower() in {'h', 'f'}:
            return True
        else:
            self.errors.append("Le genre doit etre H (Homme) ou F (Femme)")
            return False
