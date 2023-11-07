import random
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

rps_list = [rock, paper, scissors]

player_1_selection = int(input("Select 0 for Rock, 1 for Paper and 2 for Scissors\n"))
print("You Chose")
print(rps_list[player_1_selection])

player_2_selection = random.randint(0, 2)
print("Computer Chose")
print(rps_list[player_2_selection])

if player_1_selection == 0 and player_2_selection == 2:
    print("You Win!")
elif player_1_selection == 2 and player_2_selection == 1:
    print("You Win!")
elif player_1_selection == 1 and player_2_selection == 0:
    print("You Win!")
elif player_1_selection == player_2_selection:
    print("It's a tie!")
else:
    print("You Lose")