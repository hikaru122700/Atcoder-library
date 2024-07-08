INF = 1 << 60
V, E, F = map(int, input().split())
'''
Vは頂点
Eは辺の数
Fは必要流量
計算量はO(FVE)
もし必要流用流れない構造だったらreturnでINFが返ってくる
'''
G = [[] for _ in range(V)]

def add_edge(u, v, capacity, cost):
    G[u].append([v, capacity, cost, len(G[v])])
    G[v].append([u, 0, -cost, len(G[u])-1])

def del_edge(u, v, capacity, cost):
    # G[u].remove([v, capacity, cost, len(G[v])])
    # G[v].remove([u, 0, -cost, len(G[u])-1])
    for i in range(len(G[v])):
        if G[v][i][0] == u:
            G[v].remove(G[v][i])
    for i in range(len(G[u])):
        if G[u][i][0] == v:
            G[u].remove(G[u][i])


def bellman_ford(s):
    #  点ｓから各頂点への最短経路を計算する
    dist = [INF]*V
    dist[s] = 0
    pv = [0]*V
    pe = [0]*V
    #  更新が起こらなくなるまで繰り返す
    while True:
        update = False
        for v in range(V):
            #  ｖに達してるかどうかを判定
            if dist[v] == INF:
                continue
            #  全ての頂点について見る
            for i in range(len(G[v])):
                next, capacity, cost, _ = G[v][i]
                #  更新できるなら更新する
                if capacity > 0 and dist[next] > dist[v]+cost:
                    dist[next] = dist[v]+cost
                    update = True
                    pv[next] = v
                    pe[next] = i
        if not update:
            break
    return dist, pv, pe


def calc_min_cost_flow(s, t, f):
    result = 0
    while f > 0:
        dist, pv, pe = bellman_ford(s)
        if dist[t] == INF:
            return INF
        flow = f
        v = t
        while v != s:
            flow = min(flow, G[pv[v]][pe[v]][1])
            v = pv[v]
        result += flow * dist[t]
        f -= flow
        v = t
        while v != s:
            dest, capacity, cost, r = G[pv[v]][pe[v]]
            capacity -= flow
            G[pv[v]][pe[v]] = (dest, capacity, cost, r)
            rev = G[pv[v]][pe[v]][3]
            dest, capacity, cost, r = G[v][rev]
            capacity += flow
            G[v][rev] = (dest, capacity, cost, r)
            v = pv[v]

    return result

'''
Eは辺の数
calc_min_cost_flow(始点、終点、必要流量)
を渡す
'''
for _ in range(E):
    u, v, capacity, cost = map(int, input().split())
    u -= 1
    v -= 1
    add_edge(u, v, capacity, cost)

ans = calc_min_cost_flow(0, V-1, F)

print(ans)
'''
4 4 1
1 2 1 2
1 3 1 1
2 4 1 4
3 4 1 7

-6
'''
