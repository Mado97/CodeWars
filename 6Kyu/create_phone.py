def create_phone_number(n):
    dig = 10
    a, b, c = '','',''
    for i in n:
        if dig > 7: 
            a += str(i)
            dig = dig - 1
        elif dig > 4:
            b += str(i)
            dig = dig - 1
        else: 
            c += str(i)
            dig = dig - 1
    return f"({a}) {b}-{c}"
