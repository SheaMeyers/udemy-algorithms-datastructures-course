# --- Directions
# Given a string, return the character that is most
# commonly used in the string.
# --- Examples
# max_char("abcccccccd") === "c"
# max_char("apple 1231111") === "1"


def get_char_map(string):
    chars = dict()
    
    for char in string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    return chars

def max_char(string):
    char_map = get_char_map(string)

    max_char = ''
    max_value = 0

    for key, value in char_map.items():
        if value > max_value:
            max_char = key
            max_value = value
    
    return max_char