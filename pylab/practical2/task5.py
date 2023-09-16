#Perfect Number Checker
lst = []
num = int(input("Enter any number:\n"))
temp = num
for i in range(1,num):
    if num%i == 0:
        lst.append(i)
n = 0
temp2 = 0
while n <= len(lst)-1:
    temp2 = temp2 + lst[n]
    n = n + 1
if temp2 == temp:
    print("Number %d is a perfect number"%temp)
else:
    print("Number %d is not a perfect number"%temp)
   
