# Student ID : 1201200309
# Student Name : Alvin Chen

# get input for marks
# show grade based on the marks 
# A --> 80 and above, B --> 70 and above, C --> is 50 and above, below 50 is fail
# invalid marks is more than 100 or below 0
# using elif (meaning else if)

Marks = float(input("Please enter your marks : "))

if Marks>=80 and Marks<=100:
    print("Your Grade is A")

elif Marks>=70 and Marks<79:
    print("Your Grade is B")

elif Marks>=50 and Marks<69:
    print("Your Grade is C")

elif Marks>=0 and Marks<=49:
    print("Your Grade is Fail")

else:
    print("Invalid Input")