#Conditional statements
#if   if_else    elif

#Example-1  print a person is eligible for vote or not
#age>=18
age=15
if(age>=18):
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")
#output
#You are not old enough to vote


age=20
if(age>=18):
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")
#output
#You are old enough to vote
#Example-2
if True:
    print("true condition")
else:
    print("false condition")
#output
#true condition
if False:
    print("true condition")
else:
    print("false condition")
#output
#false condition

#Example-3
if 1:
    print("one")    #one
else:
    print("none")

if 0:
    print("one")    #none
else:
    print("none")
#Example-4 find number is even or odd
num=10
if(num%2==0):
    print("even")      #even
else:
    print("odd")

num=15
if(num%2==0):
    print("even")
else:
    print("odd")    #odd
#Example-5 if else in single line
num=10
print("even num") if num%2==0 else print("odd")   #even num
num=15
print("even num") if num%2==0 else print("odd num") #odd num

#Example-6  if-else multiple statements in single line
a=20
{print("hello"),print("world")} if a>=10 else {print("hi"),print("java")}   #hello world

#Example-7  Multiple conditions using elif
weekno=8
if(weekno==1):     #sunday
    print("sunday")
elif(weekno==2):
    print("Monday")
elif(weekno==3):
    print("Tuesday")
elif(weekno==4):
    print("Wednesday")
elif(weekno==5):
    print("Thursday")
elif(weekno==6):
    print("Friday")
elif(weekno==7):
    print("Saturday")
else:
    print("invalid week number")     #weekno=8 invalid week number

weekName=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
if(weekName[0]=="sunday"):
    print("sunday")



