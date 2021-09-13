# Student ID: 1201200309
# Student Name: Alvin Chen

import math

radius=float(input("Enter The Radius:"))
volume=4/3*math.pi*pow(radius,3)
surface=4*math.pi*pow(radius,2)
print("The volume is :{:.2f} cm^3".format(volume))
print("The surface area is :{:.2f} cm^2".format(surface))