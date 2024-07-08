def rle(s):
    bef = s[0]
    cnt = 1
    arr = []
    for i in range(1, len(s)):
        if s[i] == bef:
            cnt += 1
        else:
            arr.append([bef, cnt])
            bef = s[i]
            cnt = 1
    arr.append([bef, cnt])
    return arr
