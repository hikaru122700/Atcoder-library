from collections import Counter
P: Counter[int] = Counter()
P[1] += 2
P[3] = 1
print(sum(P.values()))  # Pの要素の合計を出力
print('P', P)
print(P.values())
print(P.most_common()[0][0])
max_key = max(P, key=P.get)
print(max_key)
#  出現回数が一番多い要素の表示
# counter型は要素の出現回数の記録に向いている。
# 計算量はすべてO（１）
# most_commonはO（NlogN）
#出現回数のカウント
# Pの並び順は要素の大きい順で並ぶ
print('#########')
V = list(P.values())
# でPの要素が大きい順にlist内包表記になる。
c = Counter(P[i][:K])
'''
範囲の要素のstr要素をCounterに入れる

'''
counter_obj = P
keys = counter_obj.keys()
# キーを改行して出力する
for key in counter_obj.keys():
    a, b = key
    print(a+1, b+1)
from collections import Counter

# 与えられた Counter オブジェクト
counter_obj = Counter({1: 2, 3: 1})

# 削除したいキー
key_to_delete = 1

# キーを削除
del counter_obj[key_to_delete]

print(counter_obj)  # 残った Counter オブジェクトを表示
