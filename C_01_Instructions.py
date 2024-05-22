# checks input yes (y) or no (n)
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


def instruction():
    print('''
**** Instructions ****

Do something
and then do something else
etc
    ''')


# loop for testing

want_instructions = string_checker("Do you want to read the instructions?")
if want_instructions == "yes":
    instruction()
print("program")
