#Print Even Numbers In Range
a = int(input("Enter a number:\n"))
print("Even numbers are:")

if(a>0):
    start=0
    end = a
else:
    start=a
    end = 0
for i in range(start+1,end):
    if(i%2 == 0):
        print(i)
