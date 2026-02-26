#Write a program to create a dictionary of Nepali words with values as their English translation. 
nepali ={
  "khana":"food",  
    "bhoot":"ghost",
    "water":"paani"
}
nepalis=input("enter the word")
print(nepali[nepalis]) # accesing the dictionary  value

# if nepalis == nepali["bhoot"] or nepali["khana"] or nepali["water"]:
#  print(f"{nepalis}:{nepali[nepalis]}")
# else :
#    print("error")
if nepalis in nepali:
 print(f"{nepalis}:{nepali[nepalis]}")
else :
   print("not found")