from enum import Enum


class Menu(Enum):
    LAUNCH_TOURNAMENT = 0
    MODIFICATION = 1
    RAPPORT = 2
    QUIT = 3


class Rapports(Enum):
    PLAYERS = 0
    PLAYERS_TOURNAMENT = 1
    TOURNAMENTS = 2
    TURNS_TOURNAMENT = 3
    MATCHS_TOURNAMENT = 4
    RETOUR_MENU = 5


class TriStyle(Enum):
    SCORE = 1
    ALPHABETIQUE = 0


class PlayerModif(Enum):
    F_NAME = 0
    L_NAME = 1
    BIRTHDATE = 2
    GENDER = 3
    RANK = 4


class TournamentModif(Enum):
    NAME = 0
    DATE = 1
    LOCATION = 2
