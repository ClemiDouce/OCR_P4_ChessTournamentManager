menus = [
    "Lancer un tournoi",
    "Ajouter un joueur",
    "Modifier classement joueur"
    "Rapport"
    "Quitter"
]

rapport_list = [
    "Listes des joueurs",
    "Liste joueur d'un tournoi",
    "Liste de tout les tournois",
    "Liste de tout les match d'un tournoi",
    "Liste de tout les tours d'un tournoi",
    "Retour"
]

under_rapport_list = [
    "Par ordre Alphabetique",
    "Par classement"
]


class GameView:
    def show_menu_options(self):
        choice = ""
        while True:
            try:
                print("[1] Lancer un tournoi",
                      "[2] Ajouter un joueur",
                      "[3] Modifier le classement d'un joueur",
                      "[4] Menu rapports",
                      "[5] Quitter",
                      "Votre choix : ",
                      sep='\n', end='')
                choice = int(input())
                if choice not in range(1, 6, 1):
                    print('Choix non disponible')
                    continue
                else:
                    break
            except ValueError:
                print('Entrez un chiffre')
                continue

        return choice

    def display_rapport_menu(self):
        choice = 0
        sub_choice = 0
        while True:
            try:
                for index, option in enumerate(rapport_list):
                    print(f"[{index}] - {option}")

                choice = int(input("Entrez l'index de l'option voulu : "))
            except ValueError:
                print("Vous n'avez pas rentré un chiffre")
                continue
            if choice not in list(range(len(rapport_list))):
                print("Le chiffre entré n'existe pas")
                continue

            if choice in [0, 1]:
                try:
                    for index, sub_option in enumerate(under_rapport_list):
                        print(f"[{index}] - {sub_option}")
                    sub_choice = int(input("Entrez l'index de l'option voulu : "))
                except ValueError:
                    print("Vous n'avez pas entré un chiffre")
                if choice not in list(range(len(under_rapport_list))):
                    print("Le chiffre entré n'existe pas")
                    continue
                break
            else:
                break
        return choice, sub_choice

    def ask_validation(self, msg):
        print(msg)
        print('[0] - Oui\n[1] - Non\n')
        choice = input('Votre réponse : ')
        return choice
