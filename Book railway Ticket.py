from ast import Num
from sys import set_asyncgen_hooks
from unicodedata import name


class Train:
      def __init__(self, name, seats, price):
            self.name = name
            self.seats = seats
            self.price = price
      def getstatus(self):
            print(f"The name of train is {self.name}") 
            print(f"The Total number of seats are availables  is {self.seats}")     
            print(f"The Price of tickets is {self.price}")
      def bookticket(self):
            if (self.seats>0):
                  print("Congratulation your ticket is booked")      
                  self.seats = self.seats-1
            else:
                  print("Sorry, seats is not available")      

rest = Train("intercity", 2, 90)
rest.getstatus()

rest.bookticket()
rest.getstatus()

rest.bookticket()
rest.getstatus()

rest.bookticket()







