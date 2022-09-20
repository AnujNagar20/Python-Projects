import random
def gameWin(comp,you):
    if comp==you:
        return None
    
    elif comp=="g":
        if you=="w":
            return True
        elif you=="s":
            return False   

    elif comp=="w":
        if you=="s":
            return True
        elif you=="g":
            return False                    
    
    elif comp=="s":
        if you=="g":
            return True
        elif you=="w":
            return False 
print("Comp: snake(s),water(w),gun(g)? ")                  
x=random.randint(1, 3)

if x==1:
     comp="s"
elif x==2:
    comp="w" 
elif x==3:
    comp="g"  

print("you: snake(s),water(w),gun(g)? ") 
you=input()
print(f"comp choose {comp}")
print(f"you choose {you}")

a=gameWin(comp, you)
if a==None:
    print("Game is Tie")
elif a==True:
    print("You win")  
elif a==False:
    print("you lose") 
    
              

