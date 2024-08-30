class Board_game():
    def init (self):
    #self.grille = [[' ' for  in range(10)] for _ in range(10)] ( alternative au i)
        self.plateau = []
        for x in range(10):
            line = []
        for y in range(10):
            line.append(' ')
        self.plateau.append(line)
        
        
        # self.cases = []
        # for i in range(taille):
        #     self.cases.append([])
        # for j in range(taille):
        #     self.cases[i].append("-")
        

class Ship():
    def __init__(self, ship_name, ship_size ):
        self.ship_name = ship_name
        self.ship_size = ship_size
        
        # début de méthode pour la gestion des points de vie des navires
        # def ship_life():
        #     ship_life = ship_size 
        
        
class Player():
    
    player_ship_info = {"2" : "Porte-Avion ", "2" : "Torpilleur", "3" : "Croisseur", "3" : "Sous-Marin", "4" : "Porte-Avion"}
    player_ship = [4,3,3,2,2,2]
    def __init__(self, name):
        self.ship_list = []
        for i in self.player_ship:
            self.ship_list.append(Ship("jkjkjkj",i))
        
    
