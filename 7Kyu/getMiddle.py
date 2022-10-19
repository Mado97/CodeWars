def get_middle(s):
    if len(s) % 2 != 0:
        return s[len(s) // 2]
    else: 
        return [s[i-1] + s[i] for i in range(len(s)//2, len(s)//2 + 1)][0]
