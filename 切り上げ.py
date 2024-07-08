def kiriage(a, b):
    inf = 1 << 60
    if b <= 0:
        return inf
    return (a+b-1)//b
