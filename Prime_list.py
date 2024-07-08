def prime(B):
    temp = [True] * B
    temp[0] = False
    temp[1] = False
    for i in range(B):
        if temp[i]:
            for j in range(i * i, B, i):
                temp[j] = False
    primes = [i for i in range(B) if temp[i]]
    return primes

'''
Bに作りたい素数の最大値を入れる。返ってくるのは、Bまでの素数が昇順に並んだリスト

'''
