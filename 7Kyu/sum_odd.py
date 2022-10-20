def row_sum_odd_numbers(n):
    return sum(i for i in range(n*(n-1)+1, n*n+n, 2))
