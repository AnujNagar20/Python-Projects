# BANK ACCOUNT APP

class account:
      
      def __init__(self,owner,balance):
            self.owner = owner
            self.balance = balance
      def details(self):
            print(f"The owner name is {self.owner}")  
            print(f"The Balance is {self.balance}")
      def deposit(self):
            p=int(input("Please enter the deposit Ammount : "))
            print("Deposit Accepted")
            self.balance=self.balance+p
            print(f"Your available balance is : {self.balance}")
      def withdrawals(self):
            w=int(input("Please enter the withdrawals Ammount : "))
            if(self.balance>w):
                  print("Withdrawals Accepted")
                  self.balance=self.balance-w
                  print(f"Your available balance is : {self.balance}")      
            else:
                  print("Funds unavailable")      
while True:                             
      x=account("ANUJ",500)
      print("Please select the options")
      print("For check details/balance  press : 1")
      print("For deposit  press : 2")
      print("For withdrawals  press : 3")
      r=int(input())
      if r in (1,2,3):
            if r==1:
                  x.details()
            elif r==2:
                  x.deposit()     
            elif r==3:
                  x.withdrawals()  

      else:
            print("You select invalid number")
      y=int(input("Press '0' for exit :")) 
      if y==0:
            
            break     






                

