from collections import deque


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [dict() for _ in range(n)]
        self.level_list = [-1] * n

    def add_edge(self, fr, to, cap, is_directed=True):
        if to in self.graph[fr]:
            self.graph[fr][to] += cap
            if not is_directed:
                self.graph[to][fr] += cap
        else:
            self.graph[fr][to] = cap
            if is_directed:
                self.graph[to][fr] = 0
            else:
                self.graph[to][fr] = cap

    def flow(self, fr, to, rate):
        rate = min(rate, self.graph[fr][to])
        self.graph[fr][to] -= rate
        self.graph[to][fr] += rate
        return rate

    def bfs(self, start, end):
        graph = self.graph
        self.level_list = [-1] * self.n
        self.level_list[start] = 0
        todo = deque([start])
        while todo:
            t = todo.popleft()
            lv = self.level_list[t] + 1
            for node, cap in graph[t].items():
                if cap > 0 and self.level_list[node] == -1:
                    self.level_list[node] = lv
                    if node == end: return True
                    todo.append(node)
        return False

    def dfs(self, start, end):
        level_list = self.level_list
        todo = [start]
        path = [(-1, -1, float('inf'))]
        while todo:
            t = todo[-1]
            u, v, d = path[-1]
            if v == t:
                todo.pop()
                path.pop()
            else:
                if v != -1: d = min(d, self.graph[v][t])
                path.append((v, t, d))
                if t == end:
                    for u, v, _ in path:
                        if u == -1: continue
                        self.flow(u, v, d)
                    return d
                for node, cap in self.graph[t].items():
                    if cap > 0 and level_list[node] > level_list[t]:
                        todo.append(node)
        return 0

    def max_flow(self, start, end):
        flow = 0
        while self.bfs(start, end):
            f = float('inf')
            while f:
                f = self.dfs(start, end)
                flow += f
        return flow



'''
頂点数Vを読み込んだ後以下のおまじないをする
'''
D = Dinic(V)
