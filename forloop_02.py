'''
🎯 Tasks (DO ALL — structured & postable)
🔹 Core (must do)
Find sum of all elements
Find maximum number (without using max())
Find minimum number
Count total elements
🔹 Logic (important)
Count frequency of each element
👉 Output example:
23 → 3 times
45 → 3 times
Count even and odd numbers
🔹 Advanced (this is what makes it GitHub-worthy 🔥)
Find second largest number
Remove duplicates (create new list)
Find all elements greater than average
Find all pairs whose sum = 100'''


# Find sum of all elements 

# we have a data set 
print("Finding the sum of a list")
data = [23, 45, 12, 67, 45, 23, 89, 12, 67, 45, 100, 23]

summ = 0
for n in data:
    if n >=0  and n >=9:
        summ = summ + n
    else:
        print("Enter correct number")
print("sum",summ)


#Find maximum number (without using max())
print("Finding maximum number")
data = [23, 45, 12, 67, 45, 23, 89, 12, 67, 45, 100, 23]
res = data[0] # 23
for i in data:
    if i > res: #  23 <= 23, 
        res = i
print(res)


print("Finding minimum number")
data = [23, 45, 12, 67, 45, 23, 89, 12, 67, 45, 100, 23]
res = data[0] # 23
for i in data:
    if i < res: #  23  
        res = i
print(res)

# Count Total Elements
print("Counting total elements ")

data = [23, 45, 12, 67, 45, 23, 89, 12, 67, 45, 100, 23,12,22,33]
res = 0
for i in data:
    res = res + 1
print(res)

 
#Print("Counting frequency of each element ")

data = [23, 45, 12, 67, 45, 23, 89, 12, 67, 45, 100, 23]
res = []
for i in data:
    if res not in i:
        res = i + 1

print(res)        




for i in range(1,10):
    print("*")





   
   

      
        
    
    




