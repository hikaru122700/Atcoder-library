import math
#  LCAのコード

class LowestCommmonAncestor:
    def __init__(self, n):
        self._n = n
        self._logn = int(math.log2(self._n)+2)
        self._depth = [0 for _ in range(self._n)]
        self._distance = [0 for _ in range(self._n)]
        self._ancestor = [
            [-1 for _ in range(self._n)]
            for k in range(self._logn)
        ]
        self._edges = [[] for _ in range(self._n)]
        self._parent_edge_id = [
            -1 for _ in range(self._n)
        ]
        #  親と接続している辺の番号

    #  u, v間に重みｗ＝１の辺を追加
    def add_edge(self, u, v, edge_id, w=1):
        #  辺の番号が関係ない問題ではedge_idはどんな数でもいい

        # self._edges[u].append((v, w))
        # self._edges[v].append((u, w))
        self._edges[u].append((v, w, edge_id))
        self._edges[v].append((u, w, edge_id))

    #  根をrootにした木に対して計算
    def build(self, root=0):
        stack = [root]
        while len(stack):
            cur = stack.pop()
            for nxt, w, edge_id in self._edges[cur]:
                if (
                    self._ancestor[0][nxt] != cur and
                    self._ancestor[0][cur] != nxt
                ):
                    self._ancestor[0][nxt] = cur
                    self._parent_edge_id[nxt] = edge_id
                    self._depth[nxt] = self._depth[cur]+1
                    self._distance[nxt] = self._distance[cur]+w
                    stack.append(nxt)

        for k in range(1, self._logn):
            for i in range(self._n):
                if self._ancestor[k-1][i] == -1:
                    self._ancestor[k][i] = -1
                else:
                    self._ancestor[k][i] = \
                        self._ancestor[k-1][self._ancestor[k-1][i]]

    #  vの親と接続する辺の番号を返す
    def get_parent_id(self, v):
        return self._parent_edge_id[v]

    #  頂点ｖの親を返す
    def get_parent(self, v):
        return self._ancestor[0][v]

    #  頂点ｖの深さを返す
    def get_depth(self, v):
        return self._depth[v]

    #  u, v のＬＣＡ(最小共通祖先)を求める
    def lca(self, u, v):
        if self._depth[u] > self._depth[v]:
            u, v = v, u

        for k in range(self._logn-1, -1, -1):
            if ((self._depth[v]-self._depth[u]) >> k) & 1:
                v = self._ancestor[k][v]
        if u == v:
            return u

        for k in range(self._logn-1, -1, -1):
            if self._ancestor[k][u] != self._ancestor[k][v]:
                u = self._ancestor[k][u]
                v = self._ancestor[k][v]

        return self._ancestor[0][u]

    def distance(self, u, v):
        return (
                self._depth[u] + self._depth[v]
                - 2 * self._depth[self.lca(u, v)]
        )

'''
辺を追加するときにはtree.edge(a, b, i, 1)
末尾２文字は辺の重みが関係する問題以外は関係ないので
上のように引数を渡す
'''
N, M = map(int, input().split())

#  頂点の数Nを受け取った後のおまじない
tree = LowestCommmonAncestor(3*M+10)
for i in range(M):
    a, b = map(int, input().split())
    tree.add_edge(a, b, 1, 1)




'''
辺を張りきった後には
root(親) = 0などとして
以下を書く
'''
tree.build(root=0)
ans = tree.lca(s, t)
print(ans)
'''
4 3
1 2
1 3
2 4
2 4

-2
'''
