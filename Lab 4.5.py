# Get input for a number from 1 until 12 using the for loop display the multiplication tables

gnum=int(input("Enter you number :"))

for num in range(1,13):
    ans = num * gnum
    print(ans)