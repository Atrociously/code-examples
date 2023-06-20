def is_palindrome1(input):
    for i, _ in enumerated(input):
        if input[i] != input[len(input) - 1 - i]:
            return False
    return True

def is_palindrome2(input):
    return input == input[::-1]
