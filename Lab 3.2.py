# Student ID : 1201200309
# Student Name : Alvin Chen

# get input from user to withdraw money
# if balance is less RM10, alert the user that there is no sufficient fund.
# and display the current balance
# use the keyboard else: to of the current balance is sufficient and
# display the new current balance.

cur_balance = 30.12

withdraw = float(input("Please enter the withdraw amount : "))

if (cur_balance - withdraw) < 10.00 :
    print("Insufficient fund")
    print("Your current balance is : {:.2f} " .format(cur_balance))

else :
    print("Sufficient balance")
    new_balance = cur_balance - withdraw
    print("New current balance is : {:.2f}" .format(new_balance))



