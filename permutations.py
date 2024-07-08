from itertools import permutations

N = int(input())
for perm in permutations(range(N)):
    print(perm)
    # print(type(perm))

'''
(0, 1, 2)
(0, 2, 1)
(1, 0, 2)
(1, 2, 0)
(2, 0, 1)
(2, 1, 0)
itertools.permutations、順列全探索
'''
