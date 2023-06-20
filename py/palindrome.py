def is_palindrome1(input):
    for i, _ in enumerated(input):
        if input[i] != input[len(input) - 1 - i]:
            return False
    return True

def is_palindrome2(input):
    return input == input[::-1]

if __name__ == "__main__":
    print(is_palindrome("abcba"));
    print(is_palindrome("abc"));
