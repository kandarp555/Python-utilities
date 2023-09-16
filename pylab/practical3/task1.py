#Append tool using while loop 
#Use 0.0 to stop the loop
lst = []
i = 0
while 1>i:
  elem = input("Enter anything to append:\n")
  if elem in lst:
      continue
  elif elem == '0.0':
      i = i + 1
  lst.append(elem)
lst.pop()    
print(lst)
