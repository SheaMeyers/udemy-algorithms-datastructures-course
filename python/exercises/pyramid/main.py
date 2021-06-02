def get_length_of_characters(n):
    return n + (n - 1)

def pyramid(n):
    total_length = get_length_of_characters(n)
    for i in range(1, n+1):
        hashtags_to_show = get_length_of_characters(i)
        spaces_to_show = (total_length - hashtags_to_show) / 2
        print(''.join([' ' for j in range(0, spaces_to_show)]) + 
              ''.join(['#' for j in range(0, hashtags_to_show)]) +
              ''.join([' ' for j in range(0, spaces_to_show)]))
