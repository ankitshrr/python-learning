a ="vr7 ankit"
# print(len(a))
# print(a.endswith("r7"))
print(a.startswith("V"))
print(a.upper())
print(a.capitalize())

print(a.title())#capitalize each word first letter except middlespace
text = "  QA Engineer  "

print(text.strip())
text = "QQQA EngineerQQQ"
print(text.strip("Q"))

data = "apple,banana,orange"
print(data.split(","))# SPLIT THE STRING INTO LIST


num="1232323"
print(num.isdigit()) #check numeric



text = "test test test"
print(text.count("test"))#Counts occurrences of substring.
