#Sentence Analyze tool
text = input("Enter the text:\n")
count1,count2,count3,count4,count5 = 0,0,0,1,0
for i in range(len(text)):
    if text[i]>= 'a' and text[i]<= 'z':
        count1 = count1 + 1
    elif text[i]>= 'A' and text[i]<= 'Z':
        count2 = count2 + 1
    elif text[i]>= '0' and text[i]<= '9':
        count3 = count3 + 1
    elif text[i]==" ":
        count4 = count4 + 1
    else:
        count5 = count5 + 1
print("Number of lowercase letters in text:\n%d"%count1)
print("Number of uppercase letters in text:\n%d"%count2)
print("Number of digits in text:\n%d"%count3)
print("Number of alphabets in text:\n%d"%(count1 + count2))
print("Number of special characters in text:\n%d"%count5)
print("Number of words in text:\n%d"%count4)




