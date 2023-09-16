#Dictionary merging
dict = {1:'a',2:'b',3:'c',4:'g'}
dict1 = {1:'d',4:'e',5:'f',6:'h'}
print("Dictionary1:\n",dict)
print("Dictionary2:\n",dict1)
dict.update({key:dict.get(key,'') + dict1[key] for key in dict1.keys()})
print("\nDictionary after merging:",dict)
