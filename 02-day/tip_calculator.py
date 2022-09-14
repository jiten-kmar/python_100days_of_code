import sys
print("welcome to tip calculator:")
users=int(input("Enter how many people we had: "))
bill=float(input("Enter the bill:"))
tip=int(input("Please enter the tip, 15, 20 or 25:"))
if tip!=15 and tip!=20 and tip!=25:
        print("Tip entered is", tip)
        print("Tip can be 10, 20 and 25 only, exiting: ")
        sys.exit()
else:
    total_split=print((bill + (bill*tip/100)/users))
print(total_split)
print(type(users))
print(type(bill))
print(type(tip))
print(type(total_split))




