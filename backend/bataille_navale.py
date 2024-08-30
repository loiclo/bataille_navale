class Board_game():
    def init (self): #  alternative au i
    #self.grille = [[' ' for  in range(10)] for _ in range(10)]
        self.plateau = []
        for x in range(10):
            line = []
        for y in range(10):
            line.append(' ')
        self.plateau.append(line)