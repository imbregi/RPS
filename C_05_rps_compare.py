# Check that users have entered a valid
# option based on a list
def rps_compare(user, comp):

    # If the user choice is the same as comp choice then the result is a tie
    if user == comp:
        result = "tie"
    # If its a win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    # If it's not a win, not a tie, it's a lose
    else:
        result = "lose"
    return result


# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ('rock', 'rock', 'tie'),
    ('paper', 'paper', 'tie'),
    ('scissors', 'scissors', 'tie'),
    ('rock', 'scissors', 'win'),
    ('paper', 'rock', 'win'),
    ('scissors', 'paper', 'win'),
    ('scissors', 'rock', 'lose'),
    ('rock', 'paper', 'lose'),
    ('paper', 'scissors', 'lose'),
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    user = item[0]
    comp = item[1]
    expected = item[2]

    # get actual value (ie: test ticket function)
    actual = rps_compare(user, comp)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {user} vs {comp}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f" ❌❌❌Failed! Case: {user} vs {comp}, expected: {expected}, received: {actual} ❌❌❌")
