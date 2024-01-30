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

#random hand


import random

hands = [rock, paper, scissors]

user_choice = int(input("choice your option.\n 1 = rock\n 2= paper\n 3 =scissors.\n=> "))
if user_choice == 1:
    print(rock)
elif user_choice == 2:
    print(paper)
elif user_choice == 3:
    print(scissors)

print("AI chose :")
ai_choice = random.choice(hands)
print(ai_choice)

x = hands.index(ai_choice)
index = x + 1


# Winner

if user_choice == index:
    print("its draw")
elif user_choice == 1 and index == 3:
    print("you win.")
elif user_choice == 2 and index == 1:
    print("you win.")
elif user_choice == 3 and index == 2:
    print("you win.")
else:
    print("you lose")
