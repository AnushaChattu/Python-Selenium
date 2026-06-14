# #Example-1 ways of creating string variables
# s=("welcome")
# s='welcome'
# s=str("welcome")
# s=str('welcome')
#
# #creating empty string variables
# name=" "
# name=' '
# name=str()
#
# #Example-2 ways of creating string variables
# #mutable-cannot change the value of variable
# #immutable-can change the value of variable
# #string is immutable
# #if the value is changed after updation then it is immutable
# str1="welcome"
# print(id(str1))    #2424657985088
# str1=str1+"to python"
# print(id(str1))     #2403021501104
#
# #Example-3 + and * with string
# str="welcome"
# print(str+"programming")
# print(str*3)
#
# #Example-4 slicing
# #starting index-0
# #ending index-1
# str="welcome"
# print(str[1:3])    #el
# print(str[:6])     #welcom
# print(str[2:])     #lcome
# print(str[1:-1])   #elcom
# print(str[1:-2])   #elco

# #Example-5 ord() and char()
# print(ord('A'))     #65
# print(chr(65))      #A
#
# #Example-6 max(),min(),len()
# print(max('abc'))  #c
# print(min('abc'))  #a
# print(len('welcome'))  #7
#
# #Example-7 in,not in operators
# s="welcome"
# print("come" in s)     #True
# print("lome" in s)     #False
# print("come" not in s)  #false
# print("lome" not in s)   #true
#
# #Example-8  string compartison
# print("tim"=="tie")    #False
# print("hello"!="hi")    #True
# print("Arrow" > "Arow") #True
# print("teeth" < "tee")  #False
# print("yellow" <="vellow") #False
# print("abc" > " ")   #True
#
# #Example-9 testing strings True/False
# s="welcome to python"
# print(s.isalnum())     #False
# print("Welcome".isalpha())  #True
# print("2012".isdigit())   #True
# print("firstNumber".isidentifier())  #True
# print(s.islower()) #True
# print("WELCOME".isupper()) #True
# print(" ".isspace())   #True

# #Example-10 searching for substrings
# s="welcome to python"
# print(s.endswith("thon"))     #True
# print(s.startswith("good"))   #False
# print(s.find("come"))        #3
# print(s.find("become"))      #-1    not found
# print(s.count("t"))       #2

#Example-11 converting string
s="String In Python"
s1=print(s.capitalize())    #String in python
s2=print(s.title())         #String In Python
s3=print(s.lower())         #string in python
s4=print(s.upper())         #STRING IN PYTHON
s5=print(s.swapcase())      #sTRING iN pYTHON
s6=print(s.replace('in','on'))    #Strong In Python

#Example-12 Reverse a string
s="welcome"
rev_str=" "
for i in s:
    rev_str=i+rev_str
print(" Revetrsed string is:",rev_str)    #emoclew






