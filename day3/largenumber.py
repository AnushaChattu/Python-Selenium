# num1=100
# num2=120
# if num1>num2:
#     print("the larget number is:",num1)
# else:
#     print("the smallest number is:",num1)

# num1=180
# num2=100
# num3=150
# if num1>num2:
#     print("the larget number is:",num1)
# if num2>num3:
#     print("the smallest number is:",num2)
# else:
#     print("the smallest number is:",num3)

 #Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 18
num2 = 20
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

#check the given number is positive or negitive
num=float(input("Enter a number: "))
if num >= 0:
    print("the number is positive",num)
else:
    print("the number is negative",num)
#print weekno if you provide weekname as input
# #Example-7  Multiple conditions using elif
# weekno=8
# if(weekno==1):     #sunday
#     print("sunday")
# elif(weekno==2):
#     print("Monday")
# elif(weekno==3):
#     print("Tuesday")
# elif(weekno==4):
#     print("Wednesday")
# elif(weekno==5):
#     print("Thursday")
# elif(weekno==6):
#     print("Friday")
# elif(weekno==7):
#     print("Saturday")
# else:
# #     print("invalid week number")     #weekno=8 invalid week number
#
# weekName=str(input("Enter a week number: "))
# if (weekName==1):
#     print("monday")
# elif (weekName==2):
#     print("tuesday")
# elif (weekName==3):
#     print("wedensday")
# elif (weekName==4):
#     print("thursday")
# elif (weekName==5):
#     print("friday")
# elif (weekName==6):
#     print("saturday")
# elif (weekName==7):
#     print("sunday")
# else:
#     print("invalid weekname")
# Source - https://stackoverflow.com/a
# Posted by 404th, modified by community. See post 'Timeline' for change history
# # Retrieved 2025-12-11, License - CC BY-SA 4.0
#
# num =float(input("Enter a number: "))
# while num <= 7:
#     num += 1
#     if num == 1:
#         print('Monday')
#     elif num == 2:
#         print('Tuesday')
#     elif num == 3:
#         print('Wednesday')
#     elif num == 4:
#         print('Thursday')
#     elif num == 5:
#         print('Friday')
#     elif num == 6:
#         print('Saturday')
#     elif num == 7:
#         print('Sunday')

# Create a list of weekday names (Monday is at index 0)
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Take the week number input from the user
try:
    week_num = int(input("Enter a week number (1-7): "))

    # Check if the input is within the valid range (1 to 7)
    if 1 <= week_num <= 7:
        # Convert the 1-based input to a 0-based index (e.g., 1 becomes 0)
        day_index = week_num - 1
        # Print the corresponding weekday name
        print(f"The weekday for number {week_num} is {weekdays[day_index]}.")
    else:
        print("Error: Please enter a number between 1 and 7.")
except ValueError:
    # Handle cases where the input is not a valid integer
    print("Error: Invalid input. Please enter an integer.")






