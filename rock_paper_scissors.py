import random

user_win = 0
computer_win = 0

options = ["r", "p", "s"]


while True:
    user_input = input("Type (r)Rock/(p)Paper/(s)Scissors or Quit(Q): ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
      # rock: 0, paper:1, scissors:2
    
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

    if user_input == "r" and computer_pick == "S":
        print("You won!")
        user_win += 1

    elif user_input == "p" and computer_pick == "r":
        print("You won!")
        user_win += 1
        
    elif user_input == "S" and computer_pick == "p":

        print("You won!")
        user_win += 1


    else:
        print("You lost!")
        computer_win += 1
       
    
print("you won", user_win, "times.")
print("the computer won", computer_win, "times.") 
print("goodbye!")   