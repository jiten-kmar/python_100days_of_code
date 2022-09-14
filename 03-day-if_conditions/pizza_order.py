print("welcome to Pizza center: ")
size=input("Please enter size, S,M or L:  ")
add_pep=input("Do you need more paparoni: Y or N:   ")
extra_cheese=input("Do you need more cheese: Y or N:   ")

# small pizza is $15
# Medium pizza is $20
# Large pizza is $25
## pep for small pizza is $2
## pep for medium or large pizza is $3
## extra cheeze is $1
cost=0
if size=="S":
    print("Base pizza cost for small is:  $15")
    cost=cost+15
elif size=="M":
    print("Base pizza cost for Medium is:  $20")
    cost=cost+20
else:
    cost=cost+25

if add_pep=="Y":
    if size=="S": 
        cost=cost+2
    else:
        cost=cost+3
if extra_cheese=="Y":
        cost=cost+1
print(f"Total cost is:  ${cost}")