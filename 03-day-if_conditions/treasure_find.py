from turtle import right


print("welcome to Treasure island")
user_input=input("please enter left or right: ")
if user_input=='right':
    print("Game over")
else:
    sw=input("you want to wait or swim: ")
    if sw=='swim':
         print("Game over")
    else:
        door=input("which you door you want, red or Blue or yellow: ")
        if door==('Blue' or 'Red'):
            print("Game over")
        else:
            print("you won")