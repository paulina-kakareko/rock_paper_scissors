import random

print("Welcome to my rock_paper_scissors-game!")
print("Do you want to play?")
want_to_play = input('yes/no ').lower()

if want_to_play != 'yes':
    print("Goodbay!")
    quit()
else:
    print(("OK! Let's play!"))

options = ['rock', 'paper', 'scissors']

user_score = 0
computer_score = 0

while True:
    user_choice = input("Type rock, paper, scissors or Q to quit: ").lower()
    computer_choice = options[random.randint(0,2)]
    if user_choice != computer_choice:
        print(f"Computer chose {computer_choice}.")
    if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':
        if user_choice == 'rock' and computer_choice == 'scissors':
            print('You win!')
            user_score += 1
        elif user_choice == 'paper' and computer_choice == 'rock':
            print('You win!')
            user_score += 1
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print('You win!')
            user_score += 1
        elif user_choice == computer_choice:
            print('You have chosen the same!')
        else:
            print('You lost!')
            computer_score += 1
    else:
        break

if user_score == 1:
    print('You won ' + str(user_score) + ' time.')
else:
    print('You won ' + str(user_score) + ' times.')

if computer_score == 1:
    print('Computer won ' + str(computer_score) + ' time.')
else:
    print('Computer won ' + str(computer_score) + ' times.')
print('Goodbay!')


