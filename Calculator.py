def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y
f=0
print("Select any command")
print("Addition : a\nsubtraction : b\nmultiply : c\ndivide : d") 
n=input()
while True:
    if n in ("a","b","c","d"):
        if (n=="a"):
            print(add(int(input("Enter 1 no.")),int(input("Enter 1 no."))))
        elif (n=="b"):
            print(sub(int(input("Enter 1 no.")),int(input("Enter 1 no."))))
        elif (n=="c"):
            print(mul(int(input("Enter 1 no.")),int(input("Enter 1 no."))))
        elif (n=="d"):
            print(div(int(input("Enter 1 no.")),int(input("Enter 1 no."))))


        x=input("you want to next calculation yes/no :")  
        if(x=="no"): 
            break
    else:
        f=1
        break
if(f==1):    
    print("invalid input")    
        


  

