def capitalize(string):
    result = string[0].upper()

    for index, letter in enumerate(string[1:]):
        if string[index] == ' ':
            result += letter.upper()
        else:
            result += letter
    
    return result
