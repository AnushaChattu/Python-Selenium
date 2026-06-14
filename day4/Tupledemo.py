# #ex-1 creating tuple
# mytuple=("apple","banana","cherry")
# print(mytuple)

# # ex-2 access tuple items
# mytuple=("apple","banana","cherry")
# print(mytuple[1])
# print(mytuple[-1])

# ex-3 range of indexes
# mytuple=("apple","banana","cherry","kiwi","melon","mango")
# print(mytuple[2:5])

# ex-4 changing tuple items
#tuple-->list(modify)-->tuple
# mytuple=("apple","banana","cherry")
# mylist=list(mytuple)
# mylist[0]="orange"
# mytuple=tuple(mylist)
# print(mytuple)

#ex-5 reading tuple items using loop
# mytuple=("apple","banana","cherry")
# for i in mytuple:
#     print(i)

#ex-6 check if item exists(searching of item in tuple)
# mytuple=("apple","banana","cherry")
# if "banana" in mytuple:
#     print("yes,banana is present")
# else:
#     print("no,banana is not present")

#ex-7 tuple length counting items in a tuple
# mytuple=("apple","banana","cherry")
# print(len(mytuple))

#ex-8 add items to tuple -not possible becoz tuple is immutable,cannot change values/items
# mytuple=("apple","banana","cherry")
# mytuple[0]="orange"
# print(mytuple)

#ex-9 copy tuple
# mytuple1=("apple", "banana", "cherry")
# mytuple2=mytuple1   #('apple', 'banana', 'cherry')
# print(mytuple2)

#ex-10 removing items from tuple
# mytuple=("apple","banana","orange")
# mytuple.remove("banana")
# del mytuple
# print(mytuple)

#ex-11 join/combine tuple
# tuple1=("apple","banana","orange")
# tuple2=(10,20,30)
# tuple3=tuple1+tuple2
# print(tuple3)

#ex-12
# tuple1=(1,2,3)
# tuple2=('a','b','c')
# if tuple1==tuple2:
#     print("Tuples are equal")     #tuples are not equal
# else:
#     print("tuples are not equal")

