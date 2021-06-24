from utils import get_now_time


class Round:
    def __init__(self, name, match_list, start_time="", end_time=""):
        self.name = name
        self.match_list = match_list
        self.start_time = get_now_time() if start_time == "" else start_time
        self.end_time = end_time

    def serialized(self):
        return {
            'name': self.name,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'match_list': [
                {
                    'p1': {'id': match[0][0], 'score': match[0][1]},
                    'p2': {'id': match[1][0], 'score': match[1][1]},
                }
                for match in self.match_list]
        }
