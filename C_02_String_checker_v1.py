# Check that users have entered a valid
# option based on a list
def int_checker(to_test):
    while True:

        error = "Please enter an integer that is 13 or higher"

        # Check for infinite mode
        if to_test == "":
            return "infinite"

        try:
            response = int(input("Enter an integer  "))
            # Checks if integer is greater than or equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Automated testing is below in the form (test_case, expected_value)
to_test = {
    ('xlii', 'invalid'),
    ('0.5', 'invalid'),
    ('0', 'invalid'),
    ('1', '1'),
    ('2', '2'),
    ('', 'infinite'),
}

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = int_checker(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f" ❌❌❌Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
