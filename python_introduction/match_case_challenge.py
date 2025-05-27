import random

def play_game():
  while True:
    secret_number = random.randint(1, 10)
    guessed_correctly = False

    while not guessed_correctly:
      guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? "))
      print(f"You guessed: {guess}")

      match guess:
        case _ if guess == secret_number:
          print("🎉 Congratulations, you guessed it!")
          guessed_correctly = True
        case _ if guess > secret_number:
          print("Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
          print("Nope, your guess is a bit low. Give it another shot!")

    # Ask if they want to play again AFTER correct guess
    play_again = input("Would you like to play again? Enter Yes or No: ").strip().lower()
    if play_again != "yes":
      print("Thank you for playing. See you next time!")
      break

play_game()
