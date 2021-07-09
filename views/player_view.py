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
            if _first_name == "" and _last_name == "":
                first_name = input("Prénom : ").strip()
                last_name = input("Nom : ").strip()
            else:
                first_name = _first_name.strip()
                last_name = _last_name.strip()
            birth_date = input("Date de naissance (jj/mm/aaaa) : ").strip()
            gender = input("Gender (H/F) : ").strip()
            rank = input("Rang du joueur : ")
            return first_name, last_name, birth_date, gender, rank

    def ask_player_index(self, players_list):
        print("Index | Player Full Name | ")
        for index, player in enumerate(players_list):
            print(f"[{index}] | {player.last_name} {player.first_name} | {player.rank}")
        new_elo = -1
        while True:
            try:
                new_elo = int(input("Entrez le nouveau classement : "))
            except ValueError:
                print("Vous n'avez pas rentré un chiffre")
                continue
            break
        return new_elo

    def ask_new_elo(self, player):
        print(f'Actual elo of {player.first_name} {player.last_name} : {player.rank}')
        new_elo = -1
        while True:
            try:
                new_elo = int(input("Entrez le nouveau classement : "))
            except ValueError:
                print("Vous n'avez pas rentré un chiffre")
                continue
            break
        return new_elo

    def ask_continue_create(self):
        while True:
            print("Voulez vous continuer a créer des joueurs / joueuses ?\n",
                  "[0] Oui\n [1] Non\n",
                  "Entrez votre choix : ", end=" ")
            choice = input()
            if choice in ['0', '1']:
                return choice
            else:
                continue

    def show_player_list(self, player_list):
        print(
            "Name".center(10) + "|",
            "Last Name".center(25) + "|",
            "Birthdate".center(15) + "|",
            "Gender".center(10) + "|",
            "Rank".center(10)
        )
        print("-" * 80)
        for player in player_list:
            print(player)
