import random

options = ["stone", "paper", "scissors"]
win_map = {
    "stone": "scissors",
    "scissors": "paper",
    "paper": "stone"
}

user_score = 0
computer_score = 0
rounds = 0 
while True:
    user = input("\nEnter stone, paper, or scissors (or 'quit' to exit): ").lower()
    
    if user == "quit":
        print("Thanks for playing! 👋")
        break
    elif user not in options:
        print("Invalid input. Try again.")
        continue

    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif win_map[user] == computer:
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    rounds += 1
    print(f"Score => You: {user_score} | Computer: {computer_score} | Rounds: {rounds}\n")

print("\n🏁 Final Score:")
print(f"You: {user_score} | Computer: {computer_score} | Total Rounds: {rounds}")
if user_score > computer_score:
    print("🎉 You won the game!")
elif user_score < computer_score:
    print("😞 Computer won the game!")
else:
    print("🤝 It's a draw!")


    

    






