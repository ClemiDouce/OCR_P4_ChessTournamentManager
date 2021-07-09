class Match:
    def __init__(self, p1, p1_score, p2, p2_score):
        self.p1 = p1
        self.p1_score = p1_score
        self.p2 = p2
        self.p2_score = p2_score

    def __str__(self):
        result = ""
        if self.p1_score == 0 and self.p2_score == 0:
            result = "Non joué"
        elif self.p1_score == self.p2_score:
            result = "Egalité"
        elif self.p1_score == 1:
            result = f"Victoire de {self.p1.shorted}"
        elif self.p2_score == 1:
            result = f"Victoire de {self.p2.shorted}"
        return (f"{self.p1.shorted} vs {self.p2.shorted}\n"
                f"Resultat : {result}")
