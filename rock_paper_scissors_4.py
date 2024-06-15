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

print("What do you choose?")
options = [rock, paper, scissors]
computer_choice = random.randint(0,2)
personal_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
print("")

if personal_choice >= 3 or personal_choice < 0:
  print("Invalid number. Start over and select a number between 0 and 2")  
else:
  print("You chose: \n")
  print(options[personal_choice])
  print()

  print("Computer chose:\n")
  print(options[computer_choice])
  print()
  if personal_choice == 0 and computer_choice == 2:
    print("You winnn!!")
  elif computer_choice == 0 and personal_choice == 2 or computer_choice > personal_choice:
    print("You lose :(")
  elif personal_choice > computer_choice:
    print("You win!!!")
  elif computer_choice == personal_choice:
    print("It's a draw ;)")


