 #Add a static method in problem 2, to greet the user with hello. 
# Create a class “Programmer” for storing information of few programmers working at Microsoft. 
class Calculator :
    def __init__(self,num):
         self.num = num

    def square(self):
         print("square:",self.num ** 2)
    def cube(self):
         print("Cube",self.num ** 3)
    def square_root(self):
         print("square root:",self.num ** 0.5)
    @staticmethod
    def greet():
         print("hello")
         

c =Calculator(2)
c.square()
Calculator.greet()