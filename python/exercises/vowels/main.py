def vowels(string):
    vowels_constants = ['a','e','i','o','u','A','E','I','O','U']
    number_of_vowels = 0

    for char in string:
        if char in vowels_constants:
            number_of_vowels += 1
    
    return number_of_vowels
