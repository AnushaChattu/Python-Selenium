#ex-1
# def func(i,j):
#     print(i,j)
# func(10,20)
# func(j=20,i=10)

#ex-2 default values assigned to postional arguments
# def func(i,j=10):
#     print(i,j)
# func(100,200)
# func(100)

#ex-3 keyword arguments
# def greetings(name,greetmsg):
#     print(greetmsg+" "+name)
# greetings(name='john',greetmsg='Hello there')

#ex-4
# def myfunc(a,b,c):
#     print(a,b,c)
# myfunc(10,20,30)
# myfunc(a=10,b=20,c=30)
# #myfunc(10,b=20,30)
# #myfunc(10,30,b=20)

#ex-5 function can return multiple values
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(largest(2,3))
res=largest(200,300)
print(res)
print(type(res))