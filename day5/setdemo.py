#ex:1
# myset={"apple", "banana", "cherry"}
# print(myset)      {'banana', 'apple', 'cherry'}

#ex-2 accessing items from set
# myset={"apple", "banana", "cherry"}
# for i in myset:
#     print(i)

#ex-3 value exists in set or not
# myset={"apple", "banana", "cherry"}
# print("banana" in myset)    True
# print("banana2" in myset)   False

#ex-4
# myset = {"apple", "banana", "cherry"}
# myset.add("orange")
# print(myset)
# myset.update(["kiwi","apple1"])
# print(myset)

#ex-5 find no of items in a set
# myset = {"apple", "banana", "cherry"}
# print(len(myset))

# #ex-6 remove item freom set-remove(),discard()
# myset = {"apple", "banana", "cherry"}
# #myset.remove("banana")
# #print(myset)
# #myset.remove("xyz")  #KeyError: 'xyz'
# myset.discard("banana")
# print(myset)
# myset.discard("xyz")  #will not through any error

# ex-7 clear all items from set
# myset={"apple", "banana", "cherry"}
# myset.clear()
# print(myset)
# del myset
# print(myset)        #NameError: name 'myset' is not defined

#ex-8 joining 2sets -union()
# set1={"a","b","c"}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3)

#ex-9 update()
set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1)





