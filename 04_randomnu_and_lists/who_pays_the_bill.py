## this program is about few people and decides who pay the bill

import random
payees=str(input("Enter the names of the payees sitting in the hotel: "))
payees = payees.split(",")
# ## split() function to split an input string by space. The split() method splits a string into a list.
print(payees)
print("Bill will be paid by",random.choice(payees))
# #Python random choice() function to select a random item from a List and Set

## Another way is
total_payees=len(payees)
print(total_payees)
random_choice=random.randint(0,total_payees - 1)
bill_paid_by=payees[random_choice]
print("bill to be paid by", bill_paid_by)
