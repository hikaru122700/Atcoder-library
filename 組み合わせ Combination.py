#coding:utf-8
import itertools
def comb(lst):
    c = list(itertools.combinations(lst, 3))
    return len(c)


#並べる対象
s = ['a','b','c','d','e']

#list化
c = list(itertools.combinations(s,3));

#パターン表示
#print c

#パターン数表示
print(len(c))
'''
#######
'''
mod = 998244353
from scipy.special import comb
base = comb(5, 3, mod)
print(base) # 10
'''
もしかしたら、下のやつのほうが早いかも
'''
F = [1]
Inv = [1]
for i in range(1, 5*10**3+10):
    F.append((F[-1] * i) % mod)
    Inv.append(pow(F[-1], -1, mod))

def comb(j, k, mod):
    res = F[j]
    res *= Inv[k]
    res %= mod
    res *= Inv[j - k]
    res %= mod
    return res
