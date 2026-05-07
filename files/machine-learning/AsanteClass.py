#Asante Game Base
#Uses the Asante class to represent the game board

class Asante():
    """An Asante object represents an Asante game.
        The board is conceptualized as a list. """
    
    #Adjacency dictionary:
    """The key is board position and its value is a list of adjacent board positions"""
    
    adj ={0:[1,3,4],1:[0,2,4],2:[1,4,5],3:[0,4,6],4:[0,1,2,3,5,6,7,8],
              5:[2,4,8],6:[3,4,7],7:[4,6,8],8:[4,5,7]}
    
    #List of winning lines
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    def __init__(self):
               
        self.board = list('000000000')         #Board positions:   0   1   2
                                               #                   3   4   5
                                               #                   6   7   8
    def place(self, color:str, p:int):
        """Places a color at position p."""
        if self.board[p] == '0':
            self.board[p]=color
        else:
            raise ValueError('Position {0} not open'.format(p)) 
    
    
    def move(self,color:str,p:int,newp:int):
        """Moves a color from position p to position newp.
           ValueError is raised if the move is not possible."""
        if self.board[p] == color:
            if self.board[newp] == '0':
                if newp in Asante.adj[p]:
                    self.board[newp]= color
                    self.board[p] = '0'
                else:
                    raise ValueError('{0} not adjacent to {1}'.format(newp,p))
            else:
                raise ValueError('Position {0} not open'.format(newp))
        else:
            raise ValueError("'{0}' is not in position {1}.".format(color,p))
            
    
    def win(self,color):
        """Determines whether or not color wins the game."""
        for winline in Asante.wins:
            isWin = True
            for p in winline:
                if self.board[p] != color:
                    isWin = False
            if isWin:
                return True
        return False

    def show_board(self):
        """Displays the current game board."""
        qq = ''.join(self.board)
        print('\n{0}\n{1}\n{2}\n'.format(qq[:3],qq[3:6],qq[6:])) 

#This section is human vs human to illustrate the use of Asante object.
#You will write human versus computer.
        
def placingPhase(game:Asante,color1:str,color2:str):
    """color1 places first"""
    def switchColor(turn):
        if turn == color1:
            return color2
        else:
            return color1
    turn =color1
    
    for i in range(8):
        spot = int(input("Place '{0}': ".format(turn)))
        game.place(turn,spot)
        game.show_board()
        if game.win(turn):
            print('Game over! {0} wins!'.format(turn))
            return 'done'
        turn = switchColor(turn)
    return 'placed'

def movingPhase(game:Asante,color1:str,color2:str):
    """color1 moves first"""
    def switchColor(turn):
        if turn == color1:
            return color2
        else:
            return color1
    turn = color1
    #Check for block before moving 
    if not blocked(game,turn):
        winner = False
    else:
        winner = True
        print("{0} can't move. {1} wins!".format(turn, switchColor(turn)))
    
    while not winner:
        s,d = eval(input("Move '{0}' from, to  ".format(turn)))
        game.move(turn,s,d)
        game.show_board()
        if game.win(turn):
            winner = True
            print( "'{0}' wins!".format(turn))
        turn = switchColor(turn)
        #check for block after moving
        if not winner:
            if not blocked(game,turn):
                winner = False
            else:
                winner = True
                print("{0} can't move. {1} wins!".format(turn, switchColor(turn)))

#Is color blocked from moving?
def blocked(game:Asante,color:str):
    for i in range(9):
        if game.board[i] == color:
            for pos in Asante.adj[i]:
                if game.board[pos] == '0':
                    return False
    return True
    

#Plays the game
def playAsante():
    game = Asante()
    first = input('Who goes first (r or b)? ')
    if first == 'r':
        second = 'b'
    else:
        second = 'r'
        
    q = placingPhase(game,first,second)
    if q == 'placed':
        movingPhase(game,first,second)


#playAsante()

