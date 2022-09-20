import random
randomnum=random.randint(1,100)

guess=0
f=0
while True:
      guess+=1
      num=int(input("Enter a number "))
      if(randomnum==num):
            print("You guess right")
            f=1
            break
      else:
            if (num<randomnum):
                  print("You not guess wrong : please select greater number")
            else:
                  print("You not guess wrong : please select smaller number")       

print(f"you gress in {guess} attempt")                             