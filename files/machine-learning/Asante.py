from AsanteClass import *
from random import randint, choice
""" Jallah Kollie. This is a Asante game that allows a human to play
against a human"""

#chooses the color tile
def Play():
    game = Asante()
    ans = input('Do I go first? y or n ')
    if ans == 'y':
        print('I choose Red :)')
        comp_col = 'r'
        user_col = 'b'
    
    else:
        if ans=='n':
#         make sure to make this case sensitive
            user_col = input('what color do you want r or b?')
        
            if user_col == 'r':
                comp_col = 'b'
            
            else:
                comp_col = 'r'
    q = Placing(game,comp_col,user_col,ans)
    if q == 'Moving':
        Make_moves(game,comp_col,user_col,ans)            
    
#print(comp_col, user_col)           

#placing

    

def Placing(game:Asante,comp_col: str,user_col: str,ans:str):
     
     def switchColor(turn):
        if turn == comp_col:
            return user_col
        else:
            return comp_col
 
 #evaluates if the computer is going first 
     if ans =='y':
         #starts by placing the first piece at position 4
        turn = comp_col
        game.place(turn,4)
        game.show_board()
        #adds 4 to the excluded list
        
        exclude = [4]
        for i in range(7):
            turn = switchColor(turn)
            if  turn == user_col:
                spot = int(input("Place '{0}': ".format(turn)))
                game.place(turn,spot)
                game.show_board()
                exclude.append(spot)
            else:
                for i in range(9):
                    if game.board[i] == '0':
                        game.board[i]= user_col
                        if game.win(user_col):
                            game.board[i] = comp_col
                            k = i
                            exclude.append(i)
                            game.show_board()
                            break
                        else:
                           game.board[i] ='0'
                           k = i
                           
                if game.board[k]=='0':
                    
                    choice = randint(0,8)
                    if choice not in exclude:
                        comp_spot = choice
                        game.place(turn,comp_spot)
                        game.show_board()
                        exclude.append(comp_spot)
                    else:
                        choice = randint(0,8)
                        comp_spot = choice
                        while choice in exclude:
                            choice = randint(0,8)
                            comp_spot = choice
                        exclude.append(comp_spot)
                        game.place(turn,comp_spot)
                        game.show_board()
                        
                
                
            if game.win(turn):
                print('Game over! {0} wins!'.format(turn))
                return 'done'
            
        
        return 'Moving'
        
        
     #evaluates if the user goes first   
     else:
         exclude = []
         turn = user_col
         for i in range(8):
            
            if  turn == user_col:
                spot = int(input("Place '{0}': ".format(turn)))
                game.place(turn,spot)
                game.show_board()
                exclude.append(spot)
            else:
                for i in range(9):
                    if game.board[i] == '0':
                        game.board[i]= user_col
                        if game.win(user_col):
                            game.board[i] = comp_col
                            k = i
                            exclude.append(i)
                            game.show_board()
                            break
                        else:
                           game.board[i] ='0'
                           k = i
                           
                if game.board[k]=='0':
                    
                    choice = randint(0,8)
                    if choice not in exclude:
                        comp_spot = choice
                        game.place(turn,comp_spot)
                        game.show_board()
                        exclude.append(comp_spot)
                       
                    else:
                        choice = randint(0,8)
                        comp_spot = choice
                        while choice in exclude:
                            choice = randint(0,8)
                            comp_spot = choice
                        exclude.append(choice)  
                        game.place(turn,comp_spot)
                        game.show_board()
                   
                
                
                
            if game.win(turn):
                print('Game over! {0} wins!'.format(turn))
                return 'done'
            turn = switchColor(turn)
        
         return 'Moving'
        

#movement phase
def Make_moves(game:Asante,comp_col: str,user_col: str, ans:str):
     def switchColor(turn):
        if turn == comp_col:
            return user_col
        else:
            return comp_col
        
    
    
     if ans == 'n':
        turn = user_col
        
        if not blocked(game,turn):
            winner = False
        else:
            winner = True
            print("{0} can't move. {1} wins!".format(turn, switchColor(turn)))
        
        while not winner:
               
            if turn == user_col:
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
                        
            
            else:
                 for i in range(9):
                       if game.board[i] == '0':
                           hit = i # Find empty spaces
                 for x in Asante.adj[hit]:  # Check adjacent positions
                     if game.board[x] == comp_col:  # Ensure x actually contains comp_col
                         game.move(comp_col, x, hit)
                         game.show_board()
                         if game.win(comp_col):
                            winner = True
                            print(f"'{comp_col}' wins!")
                         turn = switchColor(turn)
                         break
                        
                        
                        
                    
                                              
        
     else:
        turn = comp_col
        
        if not blocked(game,turn):
            winner = False
        else:
            winner = True
            print("{0} can't move. {1} wins!".format(turn, switchColor(turn)))
        
        while not winner:
            if turn == comp_col:
                for i in range(9):
                       if game.board[i] == '0':
                           hit = i # Find empty spaces
                for x in Asante.adj[hit]:  # Check adjacent positions
                     if game.board[x] == comp_col:  # Ensure x actually contains comp_col
                         game.move(comp_col, x, hit)
                         game.show_board()
                         if game.win(comp_col):
                            winner = True
                            print(f"'{comp_col}' wins!")
                         turn = switchColor(turn)
                         break
                        
                        
            else:
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
                
          
         
         
                        
                        
                   
                                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                
            
            
        
        
        
      
      
    
 











def blocked(game:Asante,color:str):
    for i in range(9):
        if game.board[i] == color:
            for pos in Asante.adj[i]:
                if game.board[pos] == '0':
                    return False
    return True
        
#Placing(game,comp_col,user_col,ans)       

Play()
