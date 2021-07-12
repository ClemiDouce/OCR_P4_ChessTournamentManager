from tinydb import TinyDB

db = TinyDB('db/data.json')
player_table = db.table('player')
tournament_table = db.table('tournament')

player_table.insert_multiple([
    {
        "id": 1,
        "first_name": "Mathieu",
        "last_name": "Ducournau",
        "birth_date": "14/03/1994",
        "gender": "H",
        "rank": "3000"
    },
    {
        "id": 2,
        "first_name": "Clement",
        "last_name": "Marcel",
        "birth_date": "20/08/1996",
        "gender": "H",
        "rank": 3000
    },
    {
        "id": 3,
        "first_name": "Glenn",
        "last_name": "Oberle",
        "birth_date": "20/01/2000",
        "gender": "H",
        "rank": 5000
    },
    {
        "id": 4,
        "first_name": "Gabriel",
        "last_name": "Dessere",
        "birth_date": "12/09/1990",
        "gender": "H",
        "rank": 300
    }
])

tournament_table.insert_multiple([
    {
      "id": 1,
      "name": "TournoiTest",
      "location": "Bordeaux",
      "start_date": "22/07/2020",
      "end_date": "23/07/2020",
      "players": [
        {
          "id": 1,
          "score": 0,
          "old_matchs": []
        },
        {
          "id": 2,
          "score": 0,
          "old_matchs": []
        },
        {
          "id": 3,
          "score": 0,
          "old_matchs": []
        },
        {
          "id": 4,
          "score": 0,
          "old_matchs": []
        }
      ],
      "max_turn": 3,
      "round_list": [],
      "actual_turn": 0,
      "time_control": "bullet"
    }
])
