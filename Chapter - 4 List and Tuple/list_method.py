club=['barca','realmadrid','ankit']

club.append(23)
print(club)
li = ["wanzy","wanzY","Wanzy","wanzy"]# sort the list word letter by letter  using asci value 
li.sort() #sort the number and string in squeneely by lower to higher
li.reverse()
print(li)



num =[1,2,4]
# insert(,index,element)
num.insert(2,"ankit")
re = num.pop(3)
#print(num.pop(3))

num.remove("ankit")
num.extend(li)
print(num)



counts= ["wanzy","wanzy",1]
#print(counts.index(1))
counts.count(1)
print(counts)
