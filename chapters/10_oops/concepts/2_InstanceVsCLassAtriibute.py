class employee:
    language = "nepali" # this is a class attribute
    salary= 10000 
    name = "ankit"

ankit= employee()
ankit.language = "javascript"# this is an istant attribute
print(ankit.name,ankit.language,ankit.salary)