from sortedcontainers import SortedSet, SortedList, SortedDict

'''
SortedSetは重複が許されない
SortedListは重複が許される
SortedDictは
'''
'''
以下SortedSetの使い方
https://qiita.com/Shirotsume/items/706742162db68c481c3c
'''
S = SortedSet([3, 1, 2])
# SortedSet([1, 2, 3]), 初期化の計算量は O(N * logN)
S.add(4)
# SortedSet([1, 2, 3, 4]), add の計算量は O(logN)
S.add(3)
# SortedSet([1, 2, 3, 4]), 要素は重複しない
S.discard(4)
# SortedSet([1, 2, 3]), 値4を削除 計算量は O(logN) 存在しない要素をdiscardすると、何も起こらない
# S.remove(100) とやると、KeyErrorが出る
S.pop(2)
# S[2]を削除 S.pop()で最大要素の削除 S.pop(0) で最小要素の削除　全部 O(logN)
print('S:', S)
print(S[1])
# 2 getは O(logN)
print(S[:])
# 0 1 スライスなどもできる　これの計算量はよしなに
print('#######')
print(len(S[:2]))
# 2 現在の要素数 O(1)
print(S.bisect_left(1))
# 1
print(S.bisect_right(1))
# 2
# これらは二分探索。 S.bisect_left(x) で、Sにxを挿入する位置(index)を返す。
# S.bisect_right(x) との違いは、すでにxがSにあるときに左に入れるか右に入れるか
# Pythonのbisectと同じ使用感
# print(S.index(0))
# 1 Sに2が現れる最初の位置を返す。ないとValueError
print('###########')
print('S:', S)
print(S.irange(0, 2))
# [1, 2] S に含まれる 0以上2以下（両端含む）の要素を列挙

'''
############
'''
S = SortedList([3, 1, 2, 1])
# SortedList([1, 1, 2, 3]), 初期化の計算量は O(N * logN)
S.add(4)
# SortedList([1, 1, 2, 3, 4]), add の計算量は O(logN)
S.add(3)
# SortedList([1, 1, 2, 3, 3, 4]), 要素は重複する
S.discard(3)
# SortedList([1, 1, 2, 3, 4]), 値3を削除 計算量は O(logN) 要素は1個だけ消される
# S.remove(100) とやると、KeyErrorが出る
S.pop(2)
# S[2]を削除 S.pop()で最大要素の削除 S.pop(0) で最小要素の削除　全部 O(logN)
print(S[1])
# 2 getは O(logN)
# S[0:2]
print(S[0:2])
# スライスなどもできる　これの計算量はO(klogN)
len(S)
# 現在の要素数 O(1)
S.bisect_left(1)
S.bisect_right(1)
# これらは二分探索。 S.bisect_left(x) で、Sにxを挿入する位置(index)を返す。
# S.bisect_right(x) との違いは、すでにxがSにあるときに左に入れるか右に入れるか
# Pythonのbisectと同じ使用感
S.index(1)
# 1 Sに2が現れる最初の位置を返す。ないとValueError
S.count(1)
# 2 Sに含まれる要素の個数を返す SortedSetにもあるがそっちは使う意味ないので…
S.irange(0, 2)
# [1, 2] S に含まれる 0以上2以下（両端含む）の要素を列挙


'''
'''
S = SortedDict()
S['c'] = 2
S['b'] = 3
S['a'] = 1
# SortedDict({'a': 1, 'b': 3, 'c': 2}) keyの昇順に格納される O(logN)
print(S.items())
print(S.keys())
print(S.values())
# dictと同じ
print(S.peekitem(0))
# Sのうち、keyが最大のものを返す S.pop(i)でi番目 S.pop(0)で最小 全部 O(logN)
print('c' in S)
# True
