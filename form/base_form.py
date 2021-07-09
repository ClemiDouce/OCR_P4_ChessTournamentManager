from datetime import datetime


class BasicForm:
    def __init__(self):
        self.errors = []

    def check_date(self, field_name, date):
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True
        except ValueError:
            self.errors.append(f"{field_name} n'est pas au format DD/MM/AAAA")
            return False

    def is_digit_between(self, field_name, number, min_length, max_length, digit_error=None, borne_error=None):
        if not number.isdigit():
            if digit_error:
                self.errors.append(digit_error)
            else:
                self.errors.append(f"{field_name} doit etre un nombre")
            return False
        elif not min_length <= int(number) <= max_length:
            if borne_error:
                self.errors.append(borne_error)
            else:
                self.errors.append(f"{field_name} doit ètre compris entre {min_length} et {max_length}")
            return False
        else:
            return True

    def is_string_between(self, field_name, string, min_length, max_length, err_msg=None):
        if min_length <= len(string) <= max_length:
            return True
        else:
            if err_msg:
                self.errors.append(err_msg)
            else:
                self.errors.append(f"La longueur de {field_name} doit etre entre {min_length} et {max_length} lettres")
            return False

    def display_error(self):
        print("Error List : \n" + "-" * 20)
        for error in self.errors:
            print(error)
