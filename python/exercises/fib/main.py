def fib(n):
    first = 0
    second = 1
    result = 1

    for _ in range(1, n):
        result = second + first
        temp = second
        second += first
        first = temp
    
    return result
