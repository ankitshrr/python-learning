# Count even numbers
nums= [1,2,3,2,4,5,7,8]
 
evenNum = 0 # 2 ,4,5
for  num in nums: 
 if num % 2 == 0: #2 ,2,4,8
   evenNum +=  nums.count(num) #2 ,2,1,1
   nums.remove(num) #only remove  first 2 if there is multiple element
print(evenNum)

       

