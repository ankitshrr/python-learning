class Employee :
    language= "js"
    salary= 1000
    def getInfo(self):
     print(f"the language is {self.language}. THE salary is {self.salary}")
    
    def __init__(self,name,salary,lanhague):#dunder method whic is autmocally call the clsss 
       self.name=name
       self.salary=salary
       self.lanhague=lanhague 
       
ankit =Employee("harry",10000,"javascript")
print(ankit.name)
ankit.language= "as"
ankit.getInfo() 