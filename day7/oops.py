#example-1
# class MyClass:
#     def myfunc(self):
#         pass
#     def display(self,name):
#         print("john")
# mc1=MyClass()
# mc1.myfunc()
# mc1.display("sccott")

#example-2
# class MyClass:
#     def m1(self):
#         print('this is instance method....')
# @staticmethod
# def m2(self,num):
#     print(num)
# mc=MyClass()
# mc.m1()
# mc.m2(100,200)
# MyClass.m2(10,20)

# #example-3
# class MyClass:
#     def __init__(self):
#         print("this is constructor")
#     def m1(self):
#         print("this is m1")
# mc=MyClass()
# mc.m1()
# res=mc.m2(10,20)
# print(res)

#example-8
# class MyClass:
#     name="john"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
# mc=MyClass("David")

#example-9
# class emp:
#     eid=""
#     ename=""
#     sal=""
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#     def display(self):
#         print(self.eid,self.ename,self.sal)
# e1=emp(101,"john",500000)
# e1.display()
# e2=emp(102,"david",500000)
# e2.display()

# #example-10
# class emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#     def __str__(self):
#         return (self.ename)
#         return(self.eid,self.sal)      #invalid becoz str__() returns only string data
# e1=emp(101,"john",500000)
# print(e1)
# e2=emp(102,"david",500000)
# print(e2)

