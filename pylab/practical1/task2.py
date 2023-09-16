#Multiplication Table using while loop
a = int(input("Enter the number for multiplication table:\n"))
print("Table using while loop:")
i = 1
while i <= 10:
    print(a,"*",i,"=",a*i)
    i = i + 1