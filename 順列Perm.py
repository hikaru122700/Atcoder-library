'''
https://qiita.com/ysys_Ba/items/cc897fa6ab2c9f4c5d1d
'''

#coding:utf-8
import itertools

#並べる対象
s = ['a','b','c','d','e']
s = [1, 2, 3, 4, 5]
#list化
p = list(itertools.permutations(s))

#パターン表示
#print p

#パターン数表示
print(p)
print(len(p))

from itertools import permutations

N = int(input())
for perm in permutations(range(N)):
    print(perm)
'''

(0, 1, 2)
(0, 2, 1)
(1, 0, 2)
(1, 2, 0)
(2, 0, 1)
(2, 1, 0)
itertools.permutations、順列全探索

'''
