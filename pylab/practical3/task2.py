#Password Validator
while True:
  Pass = input("Enter the password:\n")
  a,b,c,d,e,f,j = 0,0,0,0,0,0,0
  for i in Pass:
    if (i>='a' and i<'z') or (i>='A' and i<'Z'):
        if i>='a' and i<='z':
          a = a + 1
        elif i>='A' and i<='Z':
          b = b + 1
    elif i>='0' and i<='9':
      f = f + 1
    elif len(Pass)<6:
      d = d + 1
    elif len(Pass)>12:
      e = e + 1
    else:
      c = c + 1
  if a == 0:
    print("At least one lowercase require!!\n")
    j = j + 1
  elif d == 1:
    print("Minimun 6 characters require!!\n")
    j = j + 1
  elif b == 0:
    print("At least one uppercase require!!\n")
    j = j + 1
  elif f == 0:
    print("At least one digit require!!\n")
    j = j + 1
  elif c == 0:
    print("At least one special character is require!!\n")
    j = j + 1
  elif e == 1:
    print("Maximum length of pass is 12!!\n")
    j = j + 1
  if j > 0:
    print("Enter password again...\n")
  else:
    print("Password accepted")
    break
  
