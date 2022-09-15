# first way= dirty way 
print("Welcome to love calculator: ")
name1=input("what's your name: ")
name1=name1.lower()
name2=input("what's their name: ")
name2=name2.lower()

t1=name1.count('t')
t2=name2.count('t')
r1=name1.count('r')
r2=name2.count('r')
u1=name1.count('u')
u2=name2.count('u')
e1=name1.count('e')
e2=name2.count('e')
l1=name1.count('l')
l2=name2.count('l')
o1=name1.count('o')
o2=name2.count('o')
v1=name1.count('v')
v2=name2.count('v')
e3=name1.count('e')
e4=name2.count('e')

total_t=str(t1+t2+r1+r2+u1+u2+e1+e2)
total_l=str(l1+l2+o1+o2+v1+v2+e3+e4)
print(total_t)
print(total_l)

total_score=str(total_t+total_l)
ts=int(total_score)
print(f"Total score is {ts}")

##second way, better way

print("Welcome to love calculator: ")
name1=input("what's your name: ")
name2=input("what's their name: ")
combined_name=(name1+name2).lower()
print(combined_name)
t=combined_name.count('t')
r=combined_name.count('r')
u=combined_name.count('u')
e=combined_name.count('e')

l=combined_name.count('l')
o=combined_name.count('o')
v=combined_name.count('v')

true=t+r+u+e
love=l+o+v+e
ls=str(true)+str(love)
print(ls)
totals=int(ls)
print(type(totals))
print(totals)