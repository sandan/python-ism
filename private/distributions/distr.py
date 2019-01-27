from itertools import product, combinations, combinations_with_replacement as multichoose
from numpy import array

def is_mono_incr(x):
  for i in range(1, len(x)):
    if x[i - 1] > x[i]:
      return False
  return True

def mono_inc_list(n, k)
  x_i = (range(1, n + 1) for times in range(k))
  res = filter(is_mono_incr, product(*x_i))
  return list(res)

def multi(n, k):
  return combinations(range(k + n - 1), k)

def vector_subtract(x, y):
  if len(x) == len(y):
    return array(x) - array(y)

def multi_binary(n, k):
  B =  multi(n, k)
  v = range(k)
  res = (vector_subtract(sorted(s), v) for s in B)
  return res

# multisets
# k identical balls to n distinguishable bins with no restrictions
# counts the number of solutions to integer equations z1 + z2 + ... + zn = k s.t. zi > 0
# counts the number of k-lists [x1, x2, ..., xk] s.t. 1 <= x1 <= x2 <= ... <= xk <= n
