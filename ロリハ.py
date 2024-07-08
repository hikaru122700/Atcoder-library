class rollinghash:
    def __init__(self, mod, base, S):
        self.mod = mod
        self.S = S
        self.N = len(self.S)
        self.base = base

    def inv(self, x):
        return pow(x, self.mod - 2, self.mod)

    def build(self):
        self.accum = [0] * (N + 1)


        for i in range(N):
            self.accum[i + 1] = (self.accum[i] + self.base * (ord(self.S[i]) - ord('a') + 20)) % self.mod
            self.base = self.base * 113 % self.mod

    def get(self, l, r):
        return (self.accum[r] - self.accum[l - 1]) * self.inv(pow(113, l - 1, self.mod)) % self.mod

'''
baseは１でいい
Sは文字列
rh = rollinghash(mod, 1, S)
rh.build()
入力読み込んだ後、上２行を書く
判定はget(l, r)で受け取る。[l, r)

以下素数リスト
9007199254740881
'''

N, Q = map(int, input().split())
S = input()
mod = 998244353
rh = rollinghash(mod, 1, S)
rh.build()

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    if rh.get(a, b) == rh.get(c, d):
        print('Yes')
    else:
        print('No')
