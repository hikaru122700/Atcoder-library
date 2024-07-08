def mul(A, B):
    N = len(A)
    C = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]

    return C

'''
A, Bにそれぞれ行列を引数として渡す。
このとき、A, Bの行列の大きさに注意すること。同じ大きさでないとエラーが出る。

'''
