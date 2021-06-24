from tinydb import TinyDB


class DBSingleton:
    _db_instance = None

    @classmethod
    def get_db(cls):
        if cls._db_instance is None:
            cls._db_instance = TinyDB('db/data.json')
        return cls._db_instance
