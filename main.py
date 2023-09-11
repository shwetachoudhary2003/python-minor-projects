
import random
def play_game():
    user_choice = input(" enter your choice(stone,paper,scissor)").lower()
    computer_choice = random.choice(["stone", "paper", "scissor"])

    print(f"you chose:{user_choice}")
    print(f"computer chose:{computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "stone":
        if computer_choice == "scissor":
            print("stone smashes scissor!You win")
        else:
            print("paper cover stone !You lose")
    elif user_choice == "scissor":
        if computer_choice == "paper":
            print("scissor cuts paper! You win")
        else:
            print("stone smashes scissor!You lose")
    elif user_choice == "paper":
        if computer_choice == "stone":
            print("paper covers stone !You win")
        else:
            print(" scissor cuts paper ! you lose")
play_game()

