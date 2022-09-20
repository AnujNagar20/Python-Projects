from ast import Pass
from pickle import TRUE
import numpy as np
i=1
def Board():
      a=([1,2,3,''],[4,5,6,''],[7,8,9,''])
      board=np.array(a)
      return board
b=Board()

def Play():
      i=1
      while i<6:          
            print(b)
            print("X's Turn ")
            value=int(input("Enter your value : "))
            if (value==1):
                  b[0,0]="X"
            elif (value==2):
                  b[0,1]="X"
            elif (value==3):
                  b[0,2]="X"
            elif (value==4):
                  b[1,0]="X" 
            elif (value==5):
                  b[1,1]="X"
            elif (value==6):
                  b[1,2]="X"                      
            elif (value==7):
                  b[2,0]="X"  
            elif (value==8):
                  b[2,1]="X"          
            elif (value==9):
                  b[2,2]="X" 
            else:
                  print("You enter invalid number")  
            print(b) 
            
            if((b[0,0]=="X" and b[0,1]=="X" and b[0,2]=="X") or (b[1,0]=="X" and b[1,1]=="X" and b[1,2]=="X") or (b[2,0]=="X" and b[2,1]=="X" and b[2,2]=="X") or (b[0,0]=="X" and b[1,0]=="X" and b[2,0]=="X") or (b[0,1]=="X" and b[1,1]=="X" and b[2,1]=="X") or (b[0,2]=="X" and b[1,2]=="X" and b[2,2]=="X") or (b[0,0]=="X" and b[1,1]=="X" and b[2,2]=="X") or (b[0,2]=="X" and b[1,1]=="X" and b[2,0]=="X")):
                  print("X's WIN")
                  print("Thanks for playing the game")
                  exit()

            if(i==5):
                  print("Match is Tie") 
                  break     

                  

      #f=0      
      #i=1
      #while(i<6):
      #      if (i==5):
      #            f=1
      #            break
      
            print("0's Turn ")
            val=int(input("Enter your value : "))
            if (val==1):
                  b[0,0]="O"
            elif (val==2):
                  b[0,1]="O"
            elif (val==3):
                  b[0,2]="O"
            elif (val==4):
                  b[1,0]="O" 
            elif (val==5):
                  b[1,1]="O" 
            elif (val==6):
                  b[1,2]="O"                      
            elif (val==7):
                  b[2,0]="O"  
            elif (val==8):
                  b[2,1]="O"          
            elif (val==9):
                  b[2,2]="O" 
            else:
                  print("You enter invalid number") 
            print(b)
            if((b[0,0]=="O" and b[0,1]=="O" and b[0,2]=="O") or (b[1,0]=="O" and b[1,1]=="O" and b[1,2]=="O") or (b[2,0]=="O" and b[2,1]=="O" and b[2,2]=="O") or (b[0,0]=="O" and b[1,0]=="O" and b[2,0]=="O") or (b[0,1]=="O" and b[1,1]=="O" and b[2,1]=="O") or (b[0,2]=="O" and b[1,2]=="O" and b[2,2]=="O") or (b[0,0]=="O" and b[1,1]=="O" and b[2,2]=="O") or (b[0,2]=="O" and b[1,1]=="O" and b[2,0]=="O")):     
                  print("O's WIN") 
                  print("Thanks for playing the game")
                  exit()
            i+=1
                


print("Your welcome in Tic Tac Toe GAME")

#while True:
Play()
   
