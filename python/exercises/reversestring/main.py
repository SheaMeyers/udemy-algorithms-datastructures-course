def reverse_string(string):

    string_length = len(string)
    reversed_string = ''

    for i in range(1, string_length+1):
        reversed_string += string[string_length-i]

    return reversed_string

# def reverse_string(string):
#     return string[::-1]
