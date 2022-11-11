def nth_fib(n):
    a,b,c = 0, 1, 0
    if n == 0 and n == 1 : 
        n = 0
        return n
    elif n == 2:
        n = 1
        return n 
    else: 
        for i in range(1, n-1):
            c = a + b
            a = b 
            b = c
    return c
