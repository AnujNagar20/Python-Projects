# Student Library
class Library:
      def __init__(self,listbooks):
            self.books=listbooks

      def Showbooks(self):
            print("The available books are :")
            for book in self.books:
                  print(f"* {book}")
      def Borrowbook(self,bookname):
            if bookname in self.books:
                  print(f"You have issued book :{bookname}\nPlease return in 30 days")          
                  self.books.remove(bookname)
            else:
                  print(f"SORRY, This book is not available")   
      def returnbook(self,bookname):
            self.books.append(bookname)    
            print("Thanks for return the Book")  

class Student:
      def requestbook(self):
            bookname=input("Enter the book name :")
            return bookname
      def returnbook(self):
            bookname=input("Enter the book name :")
            return bookname



 
CentralLibrary=Library(["mathematics" ,"python", "java", "english"])  
Student=Student()
while True:
      command='''Please select the following commands:
      1 : Show the list of available books
      2 : For Borrow the book
      3 : For return the book
      4 : For Exit the Library'''
      print(command)
      n=int(input("Enter your choice :"))
      if n in (1 , 2, 3, 4):
            if n==1:
                  CentralLibrary.Showbooks()
            elif n==2:      
                  CentralLibrary.Borrowbook(Student.requestbook())   
            elif n==3:      
                  CentralLibrary.returnbook(Student.returnbook())   
            elif n==4:
                  print("Thank you")      
                  exit()
      else:
            print("You enter invalid command")