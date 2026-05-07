'''Jallah Kollie, program 3 shraan game, March 4, 2025'''
from random import *
import numpy as np


#check2 = [6,5]
#check3 = [5,4]




#one turn of shraan

def shRaanTurn():
    #simulates the three rolls
    C1 = []
    C2 = []
    check1 = [6,5,4]
    n = 5
    turn = 0
    for i in range(3):
        #dice roll
        roll = sample(range(1,7),n)
        #print(roll)
        
       
        #checks for 6,5,4 in the roll
        for num in check1:
            #checks if we get 6,5,4 on first roll
            legit = sum(C2)
            # if we do, then break out of the loop            
            if legit == 15:
                break
            
            if n>2:
                
                 
                if num not in C1:
                    if num in roll:
                        turn+=1
                        #remove dice from the roll if we see a 6,5,or 4
                        roll.remove(num)
                        n = len(roll)
                        C1.append(num)
                        
                        #adds 6,5,4 to C2 list if we get it on the first roll
                        if turn == 1:
                            C2.append(num)
                            
                        
                 #makes sure we have a 6 in the list before adding a 5 and 4       
                if 6 not in C1:
                    C1.clear()
                    n=5
                    
                    #makes sure if a 6 in the list, a 5 is also in the list before adding a 4
                if 5 not in C1 and 6 in C1:
                    if sum(C1) == 10:
                        C1.remove(4)
                        n = 4
                
                        
    check2 = sum(C1)                  
   
     #make sure that we have 6,5,4 in the C1 list    
    if check2!=15:

        return 0
    
    else:
        score = sum(roll)
       
        
        return score
        
                        
            
                        
                    
def shRaan():
    #print('Player 1 rolls')
    player1 = shRaanTurn()
    
    #print('Player 2 rolls')
    
    player2 = shRaanTurn()
    
    # Compares the players score and return the winner 
    if player1 > player2:
        return f'Player 1 wins with a score of {player1}'
        
    elif player1 < player2:
        return f'Player 2 wins with a score of {player2}'
    
    else:
        return f'Its a tie with a score of {player2}'
    
    
    
def simShRaan(games:int):
    #initialize my trackers
    
    wins_1 = 0
    wins_2 = 0
    
    sco1 = 0
    sco2 =0
    
    score_1 = []
    score_2 = []
    
    tie = 0
     
     #starts simulating throuh the game
    for i in range(games):
        result = shRaan()
        #tracks player 1 wins and scores
        if 'Player 1 wins' in result:
            wins_1 += 1
            sco1 += int(result.split()[-1])
            score_1.append(sco1)
        
        #tracks player 2 wins and scores
        elif 'Player 2 wins' in result:
            wins_2 +=1
            sco2 += int(result.split()[-1])
            score_2.append(sco2)
            
        else:
            tie+=1
            
     #checks who had the most wins and calculates their mean and standard deviation       
    if wins_1 > wins_2:
        mean = round(sum(score_1)/len(score_1),3)
        stdev = round(np.std(score_1),3)
        
        return f'Player 1 wins with a mean score of {mean} and the standard deviation is {stdev}'
        
    elif wins_2 > wins_1:
        mean = round(sum(score_2)/len(score_2),3)
        stdev = round(np.std(score_2),3)
        return f'Player 2 wins with a mean score of {mean} and the standard deviation is {stdev}'
    
    else:
        return 'it was a tie with both having {tie} wins'
    
    
    
    
    
    
    
def money(n):
    p1_money = 5*n
    p2_money = 5*n
    p3_money = 5*n
    
    #simulates the games and money transaction
    for i in range(n):
        
        player1 = shRaanTurn()
    
        player2 = shRaanTurn()
    
        player3 = shRaanTurn()
        
        #checks for the winner and distribute money accordingly 
        if player1 > player2 and player3:
            p1_money+=10
            p2_money -= 5
            p2_money -= 5
            
        elif player2 > player1 and player3:
            p2_money+=10
            p1_money -= 5
            p3_money -= 5
            
        elif player3 > player1 and player2:
            p2_money+=10
            p1_money -= 5
            p3_money -= 5
            
        else:
            pass
        
      
      #returns the players total money at  the end of the game 
    return "\n".join([
    f'Player 1 has a total of ${p1_money:,}',
    f'Player 2 has a total of ${p2_money:,}',
    f'Player 3 has a total of ${p3_money:,}'])
   
   
            
    
    
        
        
        
            
            
    
            
        
    
    
def testProg3():
    print(shRaanTurn())
    print(shRaan())
    print(simShRaan(1000))
    print(money(10))
    
    
testProg3()

            
#the highest score a player can get is 12, so if I score a 10 I will be very confident.             
#We can assume that the player with the most amount of money had more wins than the other players.                
     
            