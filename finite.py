def fsa_ends_with_ab(string):
    # Initial state (start state)
    state = 0

    # Process each character in the input string
    for char in string:
        
        # State 0: Start state
        if state == 0:
            if char == 'a':
                state = 1
            else:
                state = 0

        # State 1: Found 'a'
        elif state == 1:
            if char == 'b':
                state = 2
            elif char == 'a':
                state = 1
            else:
                state = 0

        # State 2: Found 'ab'
        elif state == 2:
            if char == 'a':
                state = 1
            else:
                state = 0

    # Final state check
    if state == 2:
        print("Accepted: String ends with 'ab'")
    else:
        print("Rejected: String does not end with 'ab'")


# Test cases
fsa_ends_with_ab("cab")
fsa_ends_with_ab("abab")
fsa_ends_with_ab("abc")
