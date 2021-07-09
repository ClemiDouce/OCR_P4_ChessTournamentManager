from utils import get_now_time


class Round:
    def __init__(self, name, match_list, start_time="", end_time=""):
        self.name = name
        self.match_list = match_list
        self.start_time = get_now_time() if start_time == "" else start_time
        self.end_time = end_time

    def __str__(self):
        return "|".join([
            self.name.center(20),
            str(len(self.match_list)).center(20),
            self.start_time.center(20),
            self.end_time.center(20)
        ])

    def serialized(self):
        return {
            'name': self.name,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'match_list': [
                {
                    'p1': {'id': match.p1.id, 'score': match.p1_score},
                    'p2': {'id': match.p2.id, 'score': match.p2_score},
                }
                for match in self.match_list]
        }
