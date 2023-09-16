#Character Frequencies
dict = {}
word = input("Enter any word:\n")
print("characters with their frequencies:")
for i in word:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1
print(dict)
