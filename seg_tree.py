
class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(N)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

    def dbg(self, l, r):
        return self.tree[self.num+l:self.num+r]

#####segfunc#####
def segfunc_min(x, y):
    return min(x, y)

def segfunc_max(x, y):
    return max(x, y)

def segfunc_xor(x, y):
    return x ^ y

def segfunc_add(x, y):
    return x+y
#################

#####ide_ele#####
ide_ele_max = float('-inf')
ide_ele_min = float('inf')
ide_ele_xor = int(0)
ide_ele_add = int(0)
#################


a = [14, 5, 9, 13, 7, 12, 11, 1, 7, 8]
N = len(a)
seg = SegTree(a, segfunc_max, ide_ele_max)

print(seg.query(0, 7))
seg.update(7, 4)
seg.update(0, 2)
seg.update(8, 100)
print(seg.query(0, 8))
print('######')
print(seg.dbg(0, N))
print(seg.query(0, 1))
'''
libralyは最小値を求めるようになっているので、問題に合わせて一番上のsegfancを追加すること
以下に例を挙げる
最大値　max(x, y)
区間和　x+y
区間積　x*y
最大公約数　math.gcd(x, y)
排他的論理和 x^y

queyの第二引数は右端を含まない
排他的論路和の時には、区間一転更新するたびに元の数列aを変更すること。
毎回更新のたびにdebag使って中身をみるとTLEする。
'''
