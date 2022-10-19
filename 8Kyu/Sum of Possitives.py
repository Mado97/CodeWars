def positive_sum(arr):
    x = []
    for i in arr:
        if i > 0:
            x.append(i)
        
    return sum(x)
