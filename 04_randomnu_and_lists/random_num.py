##### this is randomisation code
import random
random_number = random.randint(10,20)
random_float_number=random.random()
print(random_number)
print(random_float_number) ## prints number between 0 and 1 but both 0 and 1 will not print
random_floatnumber = float(random.randint(10,20))
print(random_floatnumber)
# Another way to find out float  is 
random_floatnumber1 = (random.random())*5
print(random_floatnumber1)