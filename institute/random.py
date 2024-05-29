import random as std_random

# Generate a random number between 1 and 100
secret_number = std_random.randint(1, 100)


# Set the number of chances
num_chances = 6

# Use a for loop to allow the user 6 guesses
for index in range(1, num_chances + 1):
    # Prompt the user to guess the number
    guess = int(input(f"Guess the number (attempt {index} of {num_chances}): "))

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {index} attempts.")
        break
    elif guess < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

# If the user didn't guess the number within the maximum number of guesses
if index == num_chances:
    print(f"Sorry, you didn't guess the number. The secret number was {secret_number}.")