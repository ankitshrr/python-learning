f = open("Readline.txt")

line = f.readline()

# lines =f.readlines()
while (line != ""):
   print(line)
   line =  f.readline()
