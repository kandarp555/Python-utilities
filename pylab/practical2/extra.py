#Vowel frequencies
dict = {}
word = input("Enter any word:\n")
print("Vowels with their frequencies:")
i = 0
while i != len(word)-1:
    if word[i] in dict:
        dict[word[i]] = dict[word[i]] + 1
    elif(
        word[i] == "a"
        or word[i] == "e"
        or word[i] == "i"
        or word[i] == "o"
        or word[i] == "u"
    ):
        dict[word[i]] = 1
    i = i + 1
print(dict)
