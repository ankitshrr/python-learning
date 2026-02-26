#  Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
mark1=int(input("enter the marks 1"))
marks2=int(input("enter the marks 2"))
marks3=(int(input("eter the mrks3")))

total_percentaage= (mark1+marks2+marks3)*100 / 300
if total_percentaage >=40 and mark1>=33 and marks2 >=33 and marks3 >= 33:
    print("you are pass",total_percentaage)
elif total_percentaage>=100:
    print("you exceed the limit",total_percentaage)
    

     