def array_diff(a, b):
    if b == [] :
        return a
    else:   
        for i in b:
            a = list(filter(lambda x: x != i, a)) 
        return a
