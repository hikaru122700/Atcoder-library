
'''
https://qiita.com/S_Kaji/items/c689ffe5d371373957c7
'''
class SCC_graph:  # グラフを構築し、SCC結果を返す
    def __init__(self, N):
        self._N = N
        self._G, self._rG = [[[] for _ in [0] * N] for _ in [0] * 2]
        self.id = [-1] * N
        self.team = []  # id: SCC番号  team: 同一SCCに含まれる頂点集合

    def add_edge(self, u, v):
        self._G[u].append(v); self._rG[v].append(u)

    def SCC(self):
        D = [0] * self._N + [1]
        Q = [(0, 0)]
        for i in range(self._N):
            Q = [(i, 0)] if D[i] == 0 else []
            while Q:  # DFS 帰りがけ順に採番
                now, cur = Q.pop()
                D[now] = -1 if cur == 0 else D[now]  # standby
                while cur < len(self._G[now]):
                    nxt = self._G[now][cur]
                    cur += 1
                    if D[nxt]: continue
                    Q.append((now, cur))
                    Q.append((nxt, 0))
                    break
                else:
                    D[now] = D[-1]; D[-1] += 1
        for _, i in sorted([(j, i) for i, j in enumerate(D[:-1])], reverse=1):
            if self.id[i] == -1:
                Q = [(i, 0)]
                self.team.append([])
                while Q:  # DFS2回目  逆辺をたどる
                    now, cur = Q.pop()
                    if cur == 0: self.team[-1].append(now)
                    while cur < len(self._rG[now]):
                        nxt = self._rG[now][cur]
                        cur += 1
                        if self.id[nxt] == -1 and nxt not in self.team[-1]:
                            Q.append((now, cur))
                            Q.append((nxt, 0))
                            break
                    else:
                        self.id[now] = len(self.team) - 1
        return self.team
'''
[{3}, {4}, {6, 5}]
このようなリスト型で帰ってくる
'''
