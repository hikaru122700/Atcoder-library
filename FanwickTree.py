class FenwickTree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x):
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def _sum(self, r):
        s = 0
        while 0 < r:
            s += self.data[r - 1]
            r -= r & -r
        return s

    def sum(self, l, r):
        r += 1
        return self._sum(r) - self._sum(l)

    def select(self, p):
        return self.sum(p, p)


# 初期化【O(N)】：変数名=Fenwick_Tree(要素数)
FT = FenwickTree(10)

# 加算【O(logN)】：add(インデックス番号,加算する数)
FT.add(2, 4)
FT.add(5, -1)
FT.add(8, 3)

# 区間和の計算【O(logN)】：sum(左インデックス番号,右インデックス番号)
print(FT.sum(2, 8))

# 値の参照【O(logN)】：select(インデックス番号)
print(FT.select(5))
