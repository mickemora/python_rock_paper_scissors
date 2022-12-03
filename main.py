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

#Write your code below this line 👇
game_images = [rock, paper, scissors]
user_input  = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ")

if int(user_input) <= 2:
  print(game_images[int(user_input)])
  computer_response = str(random.randint(0,2))
  
  if computer_response == "0":
    print(rock)
    if user_input == "0":
      print("Tie")
    elif user_input == "1":
      print("You win!")
    elif user_input == "2":
      print("You lose!")
  elif computer_response == "1":
    print(paper)
    if user_input == "0":
      print("You lose!")
    elif user_input == "1":
      print("Tie")
    elif user_input == "2":
      print("You win!")
  elif computer_response == "2":
    print(scissors)
    if user_input == "0":
      print("You win!")
    elif user_input == "1":
      print("You lose!")
    elif user_input == "2":
      print("Tie")
else:
  print("You typed an invalid option. You lose!")