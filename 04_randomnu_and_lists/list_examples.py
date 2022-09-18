states_america=["delaware","new jersey","california"]
print(states_america[0])
print(states_america[1])
print(states_america[-1])
## replacing a value
states_america[1]="georgia"
print(states_america)

## append list 
states_america.append("colrado")
print(states_america)

## extend the list with another list
states_america.extend(["new york","Albama","oregon"])
print(states_america)

##pop up an item from the list
states_america.pop(1)
print(states_america)
