class GameView:
    def show_menu_options(self):
        choice = ""
        while True:
            try:
                print("[1] Lancer un tournoi",
                      "[2] Ajouter un joueur",
                      "[3] Modifier le classement d'un joueur",
                      "[4] Menu rapports",
                      "[5] Quitter")
                choice = int(input('Choississez quelque chose'))
                if choice not in range(1, 6, 1):
                    print('Choix non disponible')
                    continue
                else:
                    break
            except ValueError:
                print('Entrez un chiffre')
                continue

        return choice
