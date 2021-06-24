from database import DBSingleton


class Player:
    player_table = DBSingleton.get_db().table('player')

    def __init__(self, p_id, first_name, last_name, birth_date, gender, rank):
        self.id = p_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank

    @property
    def serialized(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'rank': self.rank,
        }

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'({self.id}, {self.first_name}, {self.last_name}, {self.rank})')

    @classmethod
    def insert_one(cls, text):
        cls.player_table.insert(text)

    @classmethod
    def load_all(cls):
        return cls.player_table.all()

    @classmethod
    def save_all(cls, list_player):
        cls.player_table.truncate()
        cls.player_table.insert_multiple(list_player)
