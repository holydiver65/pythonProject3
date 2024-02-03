# program to calculate car mileage per week per month and per year till oil change
x = int(input("insert the mileage job 1:"))
#x = 4 home to bus = job 1
#x = 112 bellmore mileage
print(x, "weekly mileage job 1")
s = int(input("insert the mileage round trip to stew leonard:"))
bk = int(input("insert the mileage round trip to burger king:"))
# bk = 9 miles round trip times 4 for TM and 8 miles for AM
#y = 96 garden city mileage
#y = 22 bus to karp to home = job 2
y = int(input("insert mileage job 2:"))
print(y, "weekly mileage job 2")
z = (x+y+bk+s)
print(z, "weekly total mileage")
Month = (z*4)
print(Month, "monthly total mileage")
year = (z*52)
print(year,"yearly total mileage")
#to calculate actual time till next oil change
am = int(input("insert mileage from odometer:"))
# actual mileage
oc = (am + z*3 + Month)# how many miles till oil change
print(oc, " oil change due in one month and 3 weeks ")
