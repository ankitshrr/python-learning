# List of football clubs (strings)
club = ['barca', 'realmadrid', 'ankit']

# append() → adds element at the end of list
club.append(23)   # adding number into string list (mixed list allowed in Python)
print(club)


# List of words with different uppercase/lowercase
li = ["wAnzy", "wanzY", "Wanzy", "wanzy", 'a']

# sort() → sorts strings using ASCII (uppercase first, then lowercase)
li.sort()
# li.reverse()  # reverse() → would reverse the sorted list
print(li)


# Numeric list
num = [1, 2, 4]

# insert(index, element) → inserts element at given index
num.insert(2, "ankit")   # insert string at index 2
# num becomes [1, 2, 'ankit', 4]

# pop(index) → removes and returns element from given index
re = num.pop(3)   # removes 4
print(num)


# remove(value) → removes element by value (not index)
num.remove("ankit")   # removes 'ankit' from list

# extend(iterable) → adds all elements of another list into this list
num.extend(li)   # adding sorted li elements into num
print(num)


revClub =["barcelona","Real Madrid","Juventus"]
revClub.reverse()#reverse change the original list and doesnt return new listg
print(revClub)