def steps(n):
    for i in range(1, n+1):
        print(''.join(['#' for j in range(0, i)]) + ''.join([' ' for j in range(i, n)]))
