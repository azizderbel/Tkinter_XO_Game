class Move:
    
    def __init__(self,row,col,label=None):
        
        # store the move coordinates
        self.row = row
        self.col = col

        # store the player sign who had made the move
        self.label = label