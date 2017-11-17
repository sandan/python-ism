from itertools import product
M = [3, 2, 4]
def mr_prod(m):
  return product(*(range(x) for x in m))
  
c = mr_prod(M)
print([i for i in c])

# recursive
def mr_rec(m, n, a ,i):
  if i < 0:
    yield a
  else:
    for _ in mr_rec(m, n, a, i - 1):
      for x in range(m[i]):
        a[i] = x
        yield a

def mr_recursive(m):
  n = len(m)
  a = [0] * n
  return mr_rec(m, n, a, n - 1)

print()
c = mr_recursive(M)
for i in c:
  print(i)
# print([i for i in c]) doesnt work...

# iter
def mr_iter(M):
  """
  keep incrementing from the right till we have to 'carry'
  then find where to increment and set to 0 along the way, right to left
  """
    n = len(M)
    a = [0] * n
    while True:
        yield a
        # Find right-most index k such that a[k] < M[k] - 1 by scanning from
        # right to left, and setting everything to zero on the way.
        k = n - 1
        while a[k] == M[k] - 1:
            a[k] = 0
            k -= 1
            if k < 0:
                # Last lexicographic item
                return
        a[k] += 1

c = mr_iter(M)
print()
for i in c:
  print(i)
  
# coroutine
