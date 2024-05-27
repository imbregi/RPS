# Checks for an integer ,more than 0 (allows <enter>)
def int_checker(question):
    while True:

        error = "Please enter an integer that is 1 or higher"

        to_check = input(question)

        # Check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # Checks if integer is greater than or equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine

# Initialise game variables
mode = "regular"
rounds_played = 0

print("Rock Paper Scissors Game")
print()
# Instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_checker("How many rounds would you like? Push enter for infinite mode ")

if num_rounds == "infinite":
    mode = "infinite"
    print("You chose infinite ")
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:
    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("Rounds played: ", rounds_played)

    # Increase num_rounds for infinite mode
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game history / stats
