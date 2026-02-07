class Employee :
    language= "js"
    salary= 1000
    def getInfo(self):
     print(f"the language is {self.language}. THE salary is {self.salary}")
    
    def __init__(self):
       print("i am lerning ")
ankit =Employee()
ankit.language= "as"
ankit.getInfo() 