
# HANDSHAKE CHALLENGE

# You will need to:
# - Write a function that takes an integer for the number of people and returns an integer with the number of handshakes
# - There is a 6 mark penalty for not making it recursive.
#    -> HINT: For those doing non-recursive, there is a formula online for this problem that generalises the equation
# - Validate if a handshake can occur given X as an input
# - Identify an error state and throw a custom exception
# - Create a test file for the function and create a comprehensive test suite


# Note - I checked the code on https://www.geeksforgeeks.org/number-of-handshakes-such-that-a-person-shakes-hands-only-once/
# as I couldn't get mine to work and I wanted to test the other parts of the question.

def no_of_handshakes(no_people):
    try: 
        if no_people <= 1:
            return 0
        else:
            return (no_people - 1) + no_of_handshakes(no_people - 1)
    except TypeError:
        print("The value passed to the function was not an integer")

# Validate if a handshake can occur givenn X as an input    
assert no_of_handshakes(20) != 0

    
