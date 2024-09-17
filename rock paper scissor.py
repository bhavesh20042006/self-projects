import random
user_choice = int(input("what do you choose? type 0 for rock 1 for paper and 2 for scissor?  " ))
computer_choice = random.randint(0 ,2)
print(f"computer choose {computer_choice}")
if user_choice >= 3 or user_choice < 0:
    print("you choose an invalid number . you loose")

elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice > user_choice:
    print("you loose")
elif computer_choice == user_choice:
    print("Its a draw")
elif computer_choice == 0 and user_choice == 2:
    print("you loose")
elif user_choice > computer_choice:
    print("you win")

elif user_choice >= 3 or user_choice < 0:
    print("you choose an invalid number . you loose")
