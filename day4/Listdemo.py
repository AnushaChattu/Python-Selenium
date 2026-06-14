#ex-1  how to create a list
# mylist1=[10,20,30,40]
# mylist2=["apple","banana","mango"]
# mylist3=["apple",10,"banans",20]
# mylist=list()
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)

# #ex-2 accessing items from the list
# mylist=["apple","banana","cherry"]
# print(mylist[0])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2])

# #ex-3 Range of indexes
# mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# print(mylist[2:5])
# print(mylist[-4:-1])
# print(len(mylist))

#ex-4 change item value
# mylist=["apple","banana","pear"]
# print(mylist)
# mylist[0]="orange"
# print(mylist)

#ex-5 read the list items using loop
# mylist=["apple","banana","cherry"]
# for item in mylist:
#     print(item)

#ex-6 check if the item is exist in list or not
# mylist=["apple","banana","cherry"]
# if "apple" in mylist:
#     print("apple is in my list")
# else:
#     print("apple is not in my list")

#ex-7 list length
# mylist=[1,2,3,4,5]
# print(len(mylist))

#ex-8 add items append(),insert()
# mylist=["apple","banana","cherry"]
# mylist.append("orange")
# print(mylist)
# mylist.insert(1,"kiwi")
# print(mylist)

# #ex-9 remove item from the list-pop()
# mylist=["apple","banana","cherry"]
# mylist.pop(0)
# print(mylist)

# #ex-10 del
# mylist=["apple","banana","cherry"]
# del mylist[0]
# print(mylist)

# #ex-11 clear()
# mylist=["apple","banana","cherry"]
# mylist.clear()
# print(mylist)

#ex-12 copy-list
# mylist1=["apple","banana","cherry"]
# mylist2=list(mylist1)
# print(mylist1)
# print(mylist2)

#ex-13 copy()
# mylist1=["apple","banana","cherry"]
# mylist2=mylist1.copy()
# print(mylist1)
# print(mylist2)

#ex-14 combine/join lists using +operator
# list1=["a","b","c"]
# list2=[1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1)

#ex-15 using loop statement
list1=["a","b","c"]
list2=[1,2,3]
list1.extend(list2)
print(list1)