# Check that users have entered a valid
# option based on a list
def int_checker():
    while True:

        error = "Please enter an integer that is 13 or higher"

        try:
            response = int(input("Enter an integer  "))
            # Checks if integer is greater than or equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main

rps_list = "rock", "paper", "scissors", "xxx"

want_instructions = int_checker("Do you want to see the instructions?")

print("You chose", want_instructions)

rps = int_checker("Please choose r, p or s",
                     rps_list)

print("You chose", rps)
