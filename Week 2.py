print("Please think of a number between 0 and 100!")
guess = 50
interval = 50
while True:
    print("Is your secret number " + str(int(guess)) + "?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.", end=" ")
    user_input = input()
    if user_input == "h":
        interval /= 2
        guess = guess - interval
    elif user_input == "l":
        interval /= 2
        guess = guess + interval
    elif user_input == "c":
        print("Game over. Your secret number was:", int(guess))
        break
    else:
        print("Sorry, I did not understand your input.")

