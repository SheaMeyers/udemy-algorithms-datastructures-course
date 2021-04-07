def is_anagram(stringA, stringB):
    return ''.join(sorted(stringA)) == ''.join(sorted(stringB))
