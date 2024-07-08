def chenge(N):
    R = ''
    while N >= 1:
        if N % 2 == 1:
            R = '1'+R
        else:
            R = '0'+R
        N //= 2
    return R

N = int(input())
print(chenge(N))
