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
    def __init__(self, ship_name, ship_size, player):
        self.ship_name = ship_name
        self.ship_size = ship_size
        self.player = player        
        self.ship_life_played = self.ship_size 
        self.positions = [] # [[2,0],[1,0],[0,0]]
        self.positions_touched = [] # [[1,0],[0,0]]
        
        
        def is_touched(x,y):
            self.ship_life_played -= 1
            self.positions_touched.append([x,y])
            
            #print(ship_life_played)
        
        
class Player():
    
    player_ship_info = {"2" : "Torpilleur", "3" : "Croisseur", "4" : "Porte-Avion"}
    player_ship = [4,3,3,2,2,2] #le joueur doit avoir 3 bateaux de 2cases, 2 bateaux de 3 cases et un de 4 cases
    def __init__(self, name):
        self.ship_list = []
        for i in self.player_ship:
            self.ship_list.append(Ship(self.player_ship_info[str(i)],i, self))
                
            
player1 = Player("Lucie")