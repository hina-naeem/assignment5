# Using conditional statements, check if the number is:
#  - Even or Odd.
#  - Positive, Negative, or Zero.
#  - Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and print statement for each case.
num:int=int(input("enter a number  :  "))
if(num%2 == 0):
    print("number is even")
else:
    print("number is odd")

if(num>0):
    print("Positive Number")
elif(num<0):
    print("Negative Number")
else:
    print("Zero Number")

if num%2 == 0 and num%3 == 0:
    print("number is divisible by both 2 and 3")
elif num%2 == 0:
    print("number is divisible by 2")
elif num%3 == 0:
    print("number is divisible by 3")
else:
    print("number is not divisible by both 2 and 3")


#  - Take the user age.
#   -- If the age is 18 or above:
#   -- Ask if they have a nationality of "Pakistani".
#     ---If yes, print "You are eligible to vote."
#     ---If no, print "Please obtain a valid ID to vote."
age:int=int(input("enter a age  :  "))
nationality:str=input("if ur pakistani enter yes otherwise no  : ")
if age >=18 and nationality == "yes":
    print("you are eligible to vote")
else:
    print("please obtain a valid ID to vote")

#  - Write a program that takes the age of a person as input and determines whether they are a child (0-12 years), teenager (13-19 years), 
# adult (20-59 years), or senior citizen (60 years and above)
age:int=int(input("enter a age  :  "))
if age <= 12:
    print("you are a chile")
elif age > 12 and age <= 19:
    print("you are teenager")
elif age > 19 and age < 60:
    print("you are an adult")
elif age >60 and age <130:
    print("you are senior citizen")
else:
    print("invalid age entry")

#  - Enter a month (as a number between 1 and 12). Print the number of days in that month. Assume a non-leap year.
month:int=int(input("enter the month's number :  "))
if month >=1 and month <=12:
    if month ==1 or month == 3 or month ==5 or month == 7 or month == 8 or month == 10 or month ==12:
        print("this month have 31 days")
    elif month == 2:
        print("this month have 28 days")
    else:
        print("this month have 30 days")
else:
    print("invalid month number")

#  - Check if a year is a leap year or not.
year:int=int(input("enter current year :  "))
if year%4 == 0:
    print("this is a leap year")
else:
    print("this is not a leap year")