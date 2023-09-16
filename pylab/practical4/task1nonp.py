#Difference between number without using numpy
lst = []
lst2 = []
num = int(input("How many numbers do you want to add into array:\n"))
for i in range(0,num):
    x = int(input("Enter the number:\n"))
    lst.append(x)
    if i >= 1:
        diff = lst[i] - lst[i-1]
        lst2.append(diff)
print("Difference between numbers:")
print(lst2)       
        
        