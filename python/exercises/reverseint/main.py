def reverse_int(num):

    is_negative = num < 0
    abs_num = abs(num)
    reversed_num_string = str(abs_num)[::-1]
    reversed_num = int(reversed_num_string)

    if is_negative:
        return -reversed_num
    else:
        return reversed_num

    return reversed_num

