class Board_game():
    def init (self):
    #self.grille = [[' ' for  in range(10)] for _ in range(10)] ( alternative au i)
        self.plateau = []
        for x in range(10):
            line = []
        for y in range(10):
            line.append(' ')
        self.plateau.append(line)
        

class Navire():
    def __init__(self, shipe_name, shipe_size ):
        self.shipe_name = shipe_name
        self.shipe_size = shipe_size
        
        # début de méthode pour la gestion des points de vie des navires
        # def shipe_life():
        #     shipe_life = shipe_size 
        
        
class Player():
    def __init(self, name, #bateau, #grille ?):
               