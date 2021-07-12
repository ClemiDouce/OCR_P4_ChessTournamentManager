class Participant:
    def __init__(self, p_id, score=0, old_matchs=None):
        self.id = p_id
        self.score = score
        self.old_matchs = old_matchs or set()

    def serialize(self):
        return {
            "id": self.id,
            "score": self.score,
            "old_matchs": list(self.old_matchs)
        }
