from queue import Queue

# グラフGに対して、頂点Sを始点とした幅優先探索をおこなう
# 返り値：各頂点への頂点ｓからの最短経路を表す配列
def bfs(G, s):
    #  todoリストを表すキュー
    que = Queue()

    # dist[v]は始点ｓから頂点ｖへの最短経路長
    dist = [-1]*len(G)

    #  最初に始点ｓをtodoリストにセットする
    que.put(s)
    dist[s] = 0

# todoリストがになるまで探索をする
    while not que.empty():
        #  todoリストから頂点ｖを取り出す
        v = que.get()

# vに直接つながる頂点を探索
        for v2 in G[v]:
            #  ｖ２がすでに探索済みの場合はスキップする
            if dist[v2] != -1:
                continue

# v2を新たにtodoリストに追加
            que.put(v2)

# v2のdistの値を更新
            dist[v2] = dist[v] + 1

# 最短経路長を表す配列を返す
    return dist
