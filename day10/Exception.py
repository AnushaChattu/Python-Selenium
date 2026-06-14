# #Example-1
# print("this is starting point of program")
# print("this is starting point of program")
# print("this is starting point of program")
# try:
#     print(x)
# except:
#     print("exception occured")
# print("this is ending point of program")
# print("this is ending point of program")
# print("this is ending point of program")

#Example-2

# print("this is starting point of program")
# print("program in progress")
# try:
#     print(10/5)   #2.0
# except ZeroDivisionError:
#     print("exception occurred.... handled")
# print("program completed")

# #example-3
#
# print("this is starting point of program")
# print("program in progress")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("exception occurred.... handled")
#     print("program completed")

#example-4
# try:
#     num1,num2=10,0
#     Result=num1/num2
#     print("result is:", Result)
# except ZeroDivisionError:
#     print("thrown zero division error exception")
# except SyntaxError:
#     print("thrown syntax error exception")
# except:
#     print("Exception handled")
# else:
#     print("no exception handled")
# finally:
#     print("always executed.....")

#example-5
def enterage(num):
    if(num<0):
        raise ValueError("only integer numbers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")
# enterage(10)
# enterage(9)
# enterage(-1)
print("checking num is even or odd by calling function")
num=-1
try:
    enterage(num)
except ValueError:
    print("value error exception occured and handled")
print("program completed")
