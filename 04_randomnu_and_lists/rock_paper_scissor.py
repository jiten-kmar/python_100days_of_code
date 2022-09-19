import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
#rock wins against scissors
#scissors wins against paper
#paper wins against rock 

user_input=int(input("What do you choose, Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice=random.randint(0,2)
print(computer_choice)
if user_input==computer_choice:
    print("Seems both user and computer chose same, so its draw")
    if user_input==0:
        print(rock)
    elif user_input==1:
        print(paper)
    else:
        print(scissors)
    print("computer chose", computer_choice)
    if computer_choice==0:
        print(rock)
    elif computer_choice==1:
        print(paper)
    else:
        print(scissors)
elif (user_input==0 and computer_choice==2) or (user_input==2 and computer_choice==1) or (user_input==1 and computer_choice==0):
    print("user wins and here are the choices:")
    print("user chose,", user_input)
    if user_input==0:
        print(rock)
    elif user_input==1:
        print(paper)
    else:
        print(scissors)
    print("computer chose", computer_choice)
    if computer_choice==0:
        print(rock)
    elif computer_choice==1:
        print(paper)
    else:
        print(scissors)
else:
    print("Computer wins")
    print("here are the choice made by user", user_input)
    if user_input==0:
        print(rock)
    elif user_input==1:
        print(paper)
    else:
        print(scissors)
    print("here are the choice made by computer", computer_choice)
    print("computer chose", computer_choice)
    if computer_choice==0:
        print(rock)
    elif computer_choice==1:
        print(paper)
    else:
        print(scissors)