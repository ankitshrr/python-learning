#Write a class “Calculator” capable of finding square, cube and square root of a number.


# class Calculator :
#     def __init__(self,Square,Cube,Squareroot):
#            self.Square=Square **2
#            self.Cube = Cube **3
#            self.Squareroot =Squareroot  ** 0.2

#     def showResult(self):
#           print("square",self.Square)
#           print("squareroot",self.Squareroot)
#           print("Cube",self.Cube)

# p1 = Calculator(5,2,3)
# p1.showResult()

class Calculator :
    def __init__(self,num):
         self.num = num

    def square(self):
         print("square:",self.num ** 2)
    def cube(self):
         print("Cube",self.num ** 3)
    def square_root(self):
         print("square root:",self.num ** 0.5)


c =Calculator(2)
c.square()