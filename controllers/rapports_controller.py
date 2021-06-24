class RapportsController:
    def generation_rapport(self):
        while True:
            choice, sub_choice = self.view.show_rapport_options()
            print(choice, sub_choice)
            if choice == Rapports.PLAYERS.value:
                players_to_show = []
                if sub_choice == TriStyle.SCORE.value:
                    players_to_show = sorted(Player.list_player, key=lambda player: player.rank)
                elif sub_choice == TriStyle.ALPHABETIQUE.value:
                    players_to_show = sorted(Player.list_player, key=lambda player: player.last_name)
                self.view.display_player_list(players_to_show)

            elif choice == Rapports.PLAYERS_TOURNAMENT.value:
                players_to_show = []
                tournoi_choice = self.view.ask_tournoi_index(Tournament.list_tournoi)
                tournament = Tournament.list_tournoi[tournoi_choice]
                player_list = [Player.get_by_id(p[0]) for p in tournament.players]
                if sub_choice == TriStyle.SCORE.value:
                    players_to_show = sorted(
                            player_list,
                            key=lambda player: player.rank
                    )
                elif sub_choice == TriStyle.ALPHABETIQUE.value:
                    players_to_show = sorted(
                            player_list,
                            key=lambda player: player.last_name
                    )
                self.view.display_player_list(players_to_show)

            elif choice == Rapports.TOURNAMENTS.value:
                self.view.display_tournaments(Tournament.list_tournoi)

            elif choice == Rapports.TURNS_TOURNAMENT.value:
                tournoi_choice = self.view.ask_tournoi_index(Tournament.list_tournoi)
                tournament = Tournament.list_tournoi[tournoi_choice]
                self.view.display_tournament_turn(tournament)

            elif choice == Rapports.MATCHS_TOURNAMENT.value:
                tournoi_choice = self.view.ask_tournoi_index(Tournament.list_tournoi)
                tournament = Tournament.list_tournoi[tournoi_choice]
                show_match = []
                for turn in tournament.turn_list:
                    for match in turn.match_list:
                        show_match.append(match)
                self.view.display_tournament_matchs(show_match)
            elif choice == Rapports.RETOUR_MENU.value:
                break
