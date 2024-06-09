import random
import sys


# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Make sure input is lowercase

        user_response = random.choice(rps_list[:-1])
        for item in valid_ans:
            # check if input is on the list
            if item == user_response:
                return item

            # Check if input is the same as first letter of an item on list
            elif user_response == item[0]:
                return item

        # print error if input is invalid
        print(error)
        print()


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


# Compares user choice and computer choice
def rps_compare(user, comp):
    # If the user choice is the same as comp choice then the result is a tie
    if user == comp:
        round_result = "tie"
    # If it's a win its a win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    # If it's not a win, not a tie, it's a lose
    else:
        round_result = "lose"
    return round_result


# Main Routine

# Initialise game variables
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0
rounds_won = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("Rock Paper Scissors Game")
print()

# Ask user for number of rounds / infinite mode
num_rounds = int_checker("How many rounds would you like? Push enter for infinite mode ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds heading
    if mode == "infinite":
        rounds_heading = f"\n000 Round {rounds_played + 1} (Infinite Mode) 000"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()
    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("You chose ", user_choice)

    if user_choice == "xxx":
        break

    # computer chooses randomly from rps_list
    comp_choice = random.choice(rps_list[:-1])

    result = rps_compare(user_choice, comp_choice)

    # Adjust game lost/tied counters and add results to game history.
    if result == "tie":
        rounds_tied += 1
    elif result == "lose":
        rounds_lost += 1
    elif result == "win":
        rounds_won += 1


    def check_sum(rounds_lost, rounds_won, rounds_tied, rounds_played):
        # Add the three values
        total = rounds_lost + rounds_won + rounds_tied
        # Check if the sum equals the target value
        if total == rounds_played:
            return "pass"
        else:
            return 'fail'


    if check_sum == "fail":
        print("!!!!FAIL!!!!")

    print(f"{user_choice} vs {comp_choice}, {result}")

    print(f"Wins: {rounds_won} Ties: {rounds_tied} Losses: {rounds_lost}")

    rounds_played += 1

    # Increase num_rounds for infinite mode
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here


# Game history / stats
