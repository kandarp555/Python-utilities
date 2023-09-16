#Product Price Min Max 
dict = {}
n = int(input("How many products do you want to add:\n"))
for i in range(n):
    product = input("Enter the name of the product %d:\n"%(i+1))
    price = input("Enter the price of the product %d(in rupees):\n"%(i+1))
    dict[product] = price
temp = 0
for prod,pri in dict.items():
    if int(pri)>temp:
        temp = int(pri)
temp1 = temp
for i,j in dict.items():
    if temp==int(j):
        print("Product with maximum price:\n",i,",",j,"rupees")
    elif int(j)<=int(temp1):
        temp1 = j
        p = i  
print("Product with minimum price:\n",p,",",temp1,"rupees")
 