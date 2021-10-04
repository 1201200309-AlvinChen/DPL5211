# Student ID : 1201200309
# Student Name : Alvin Chen

# get input of how many hours worked for a week
# calculate staff salary for one week
# if staff work more than 40 hours, overtime pay is 10.50 per hour for the additional hours
# staff cannot work 60 hours per week, so only additional 20 hours is calculate for overtime pay
# display the salary

hourly_rate = 0.50
overtime_pay = 10.50
week = 7

hours = float(input("How many hours did you work this week ? "))
salary = hours * week

if (hours >= 60) :
    print("Too much work")
    extra = (hours - 60) * hourly_rate
    salary = (20 * overtime_pay) + (40 * hourly_rate) + extra

elif hours >= 40 and hours <= 59 :
    overtime_pay = (hours - 40) * overtime_pay
    result_p = 40 * hourly_rate
    salary = overtime_pay + result_p

elif (hours <= 40) :
    salary = hours * hourly_rate

print("Your salary will be RM{:.2f}".format(salary))
    
    

