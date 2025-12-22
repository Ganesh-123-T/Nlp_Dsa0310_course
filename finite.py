def fsa_ends_with_ab(string):
    state = 0

    for char in string:
        if state == 0:
            if char == 'a':
                state = 1
        elif state == 1:
            if char == 'b':
                state = 2
            else:
                state = 0

    if state == 2:
        print("Accepted: String ends with 'ab'")
    else:
        print("Rejected: String does not end with 'ab'")

# Test cases
fsa_ends_with_ab("cab")
fsa_ends_with_ab("abab")
fsa_ends_with_ab("abc")
