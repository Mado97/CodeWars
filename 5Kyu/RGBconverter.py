def rgb(r, g, b):
    return range(r) + range(g) + range(b)    
    
def range(x):
    if 0 <= x <= 255:
        return str.upper(hex(x)[2:]).zfill(2)
    elif x < 0: 
        return '00'
    elif x > 255:
        return 'FF'
