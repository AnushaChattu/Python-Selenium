#example-1
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
# class B(A):
#     def m2(self):
#         print("this is m2 method from class B")
# bobj=B()
# bobj.m1()    #this is m1 method from class A
# bobj.m2()    #this is m1 method from class B

# #example2:single inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# bobj=B()
# bobj.m1()   #30
# bobj.m2()   #100

#example-3  multilevel inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# class C(B):
#     i,j=10,20
#     def m3(self):
#         print(self.i*self.j)
# cobj=C()
# cobj.m1()   #30
# cobj.m2()   #100
# cobj.m3()   #200

# #example-4   heirarchy inheritance.
#
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# class C(A):
#     i,j=10,20
#     def m3(self):
#         print(self.i*self.j)
#
# bobj=B()
# bobj.m1()     #30
# bobj.m2()     #100
#
# cobj=C()
# cobj.m1()   #30
# cobj.m3()   #200


#example-5   multiple inheritance.
#
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# class C(A):
#     i,j=10,20
#     def m3(self):
#         print(self.i*self.j)
#
# bobj=B()
# bobj.m1()     #30
# bobj.m2()     #100
#
# cobj=C()
# cobj.m1()   #30
# cobj.m3()   #200

#example-6 overriding method
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
# class B(A):
#     def m1(self):
#         print("this is m1 method from class B")
#         super().m1() #invoking parent class method through child class method
# bobj=B()
# bobj.m1()

# #example-7
# class A:
#     a,b=10,20
# class B(A):
#     i,j=00,200
#     def m(self,x,y):
#         print(x+y)    #local variables
#         print(self.a+self.b) #class variables
#         print(self.i+self.j) #class variables
#
# bobj=B()
# bobj.m(1000,2000)

#example-8 overriding variables
# class parent:
#     name="scott"
# class child(parent):
#     name="john"     #overriding the variable value
# cobj = child()
# print(cobj.name)

#example-9    overriding methods
# class Bank:
#     def rateOfInterest(self):
#         return 0
# class XBank(Bank):
#     def rateOfInterest(self):
#         return 10
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 20
# objx = XBank()
# print(objx.rateOfInterest())
# objy=YBank()
# print(objy.rateOfInterest())

#example-10 overloading polymorphism
class Human:
    def sayHi(self,name=None):
        if name is not None:
            print("hello"+name)
        else:
            print("hello")
h=Human()
h.sayHi("scott")
h.sayHi()


