class PlayerView:
    def ask_player_name(self):
        first_name = input("Entrez le prenom du joueur : ").capitalize()
        last_name = input("Entrez le nom du joueur : ").capitalize()
        return first_name, last_name

    def display_stat(self, player):
        print(f"{player.first_name.center(10)} | {player.last_name.center(25)} | "
              f"Birthdate : {player.birth_date.center(15)} / Genre : {player.gender.center} | "
              f"Rank : {player.rank}")

    def new_player(self, _first_name="", _last_name=""):
        while True:
            try:
                if _first_name == "" and _last_name == "":
                    first_name = input("Prénom : ").strip()
                    last_name = input("Nom : ").strip()
                else:
                    first_name = _first_name.strip()
                    last_name = _last_name.strip()
                birth_date = input("Date de naissance (jj/mm/aaaa) : ").strip()
                gender = input("Gender (M/F) : ").strip()
                rank = int(input("Rang du joueur : "))
            except ValueError:
                print('Le score doit etre une valeur numérique')
                continue
            return first_name, last_name, birth_date, gender, rank
