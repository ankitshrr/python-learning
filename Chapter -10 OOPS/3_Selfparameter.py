class Employee :
    language= "js"
    salary= 1000
    def getInfo(self):
     print(f"the language is {self.language}. THE salary is {self.salary}")
    
    
ankit =Employee()
ankit.language= "as" #this is an object or instance attribute
ankit.getInfo() #-> change it to this and get error if not call in self para #Employee.getInfo(ankit)