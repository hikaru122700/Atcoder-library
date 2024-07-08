import sys
import pypyjit

sys.setrecursionlimit(10 ** 7)
pypyjit.set_param('max_unroll_recursion=-1')
