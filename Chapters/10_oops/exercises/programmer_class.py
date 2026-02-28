# Create a class “Programmer” for storing information of few programmers working at Microsoft. 
class Programmer:
    Company = "ms" #class varible or class 
    def __init__(self,Name,EmployeeId,Department,language):
        self.Name =Name
        self.EmployeeId =EmployeeId
        self.Department =Department
        self.language =language
        
    def showDetail(self):
        print("Name:",self.Name)
        print("EmployeeId:",self.EmployeeId)
        print("Department:",self.Department)
        print("language:",self.language)
#creating object
p1  =Programmer("ankit",23123,"ai","js")

#displaying detail
p1.showDetail()


    