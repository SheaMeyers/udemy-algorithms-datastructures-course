def is_palindrome(string):

    string_length = len(string)

    for i in range(0, string_length/2):
        if string[i] != string[string_length-i-1]:
            return False

    return True
