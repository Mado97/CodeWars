def open_or_senior(data):
    x = []
    for (i,j) in data:
        if i >= 55 and j > 7:
            x.append('Senior')
        else: 
            x.append('Open')    
    return x

"""
VERSION 1
def open_or_senior(data):
    x = []
    for i in range(0,len(data)):
        if data[i][0] >= 55 and data[i][1] > 7:
            x.append('Senior')
        else: 
            x.append('Open')
    return x
"""
