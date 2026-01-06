b = input("enter the name")
c = input("enter the date")
a = '''Dear <|Name|>,
You are selected!
<|Date|>
'''
print(a.replace("<|Name|>",b).replace("<|Date|>",b))
