#https://qiita.com/Kept1994/items/051594a52dee5f8a4d3f

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        #要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        #要素xが属するグループと要素yが属するグループとを併合する
        x = self.find(x)
        y = self.find(y)

        if x == y:
            #根が同じなら何もしない
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        #要素xが属するグループのサイズ（要素数）を返す
        return -self.parents[self.find(x)]

    def same(self, x, y):
        #要素x, yが同じグループに属するかどうかを返す
        return self.find(x) == self.find(y)

    def members(self, x):
        #要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        #すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        #グループの数を返す
        return len(self.roots())

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


# 1.全ての辺を重みの小さいものから順に選びとる。
# 2.その過程で閉路を作ってしまうものは捨てる。全ての辺に対してこれを行う。

#入力読み込み
V, E = map(int, input().split())    #V:頂点数,E:辺数

edges = list()

for _ in range(E):
    s, t, w = map(int, input().split())     #s,t:点 , w:コスト
    edges.append((w, s-1, t-1))             #union findが0開始なので下駄を抜く。重みの小さいものから順に選びとるために、(重み,点,点)で全辺リストに追加

edges.sort(reverse=False)    #重みの小さい順で並び替え

uf = UnionFind(V)
cost = 0

#全ての辺を重みの小さいものから順に選びとる。
for edge in edges:
    w, s, t = edge

    if not uf.same(s, t):
        #点が既に同グループに属していない = 閉路を作らない ならOK
        cost += w
        uf.union(s,t)

print(cost)
