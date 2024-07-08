class UnionFind:

    # インデックスは0-start
    # 初期化
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.group = n

    # private function
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            vertices = []
            while self.parents[x] >= 0:
                vertices.append(x)
                x = self.parents[x]
            for i in vertices:
                self.parents[i] = x
            return x

    # x,yが属するグループの結合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        '''
        以下消すかどうかその都度考える
        '''
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.group -= 1

    # x,yが同グループか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xと同じグループの要素数を取得
    def size(self, x):
        return -self.parents[self.find(x)]

    # xが親かを判定
    def isparent(self, x):
        return self.parents[x] < 0



'''
同じ群にいるかどうかの判定はsame(x, y)でおこなう
26, 27行目のunion-by-sizeは行ってはいけないときがある。
そのグループの中で親が変わってはいけないとき
'''
