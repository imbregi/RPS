# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Make sure input is lowercase
        user_response = input(question).lower()

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


# Main

rps_list = "rock", "paper", "scissors", "xxx"

want_instructions = string_checker("Do you want to see the instructions?")

print("You chose", want_instructions)

rps = string_checker("Please choose r, p or s",
                     rps_list)

print("You chose", rps)
