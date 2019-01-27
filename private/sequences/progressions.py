from functools import reduce

def arithmetic_progression(start, stop = None, step = 1):
  """
  An arithmetic progression is a sequence of numbers
  differing by a constant step
  """
  s_n = start
  while True:

    if s_n == stop:
      break

    yield s_n
    s_n += step


def geometric_progression(start, stop = None, step = 2):
  """
  A geometric progression is a sequence where the
  next number has the same ratio

  if s_{n-1}, s_n, s_{n+1} are in the sequence, then
  \frac{s_n}{s_{n-1}} = \frac{s_{n + 1}}{s_n} for all n
  """

  s_n = start
  while True:
    if s_n == stop:
      break

    yield s_n
    s_n *= step

if __name__ == '__main__':

  # arithmetic
  s = arithmetic_progression(2, step  = 2)
  seq = []
  for times in range(10):
    seq.append(next(s))

  n, a, b = len(seq), seq[0], seq[-1]

  # the sum of an arithmetic sequence has a closed form
  print(n * (a + b) / 2)
  print(reduce(lambda x, y: x + y, seq))

  # geometric
  g = geometric_progression(2, step = 3)
  seq = []
  for times in range(10):
    seq.append(next(g))

  n, a, b = len(seq), seq[0], seq[-1]
  # the sum of an arithmetic sequence has a closed form
  print((b*3 - a)/ (3 - 1))
  print(sum(seq))

  ## binary trees
  g = geometric_progression(1, step = 2)
  seq = []
  for times in range(10):
    seq.append(next(g))

  n, a, b = len(seq), seq[0], seq[-1]
  # the sum of an arithmetic sequence has a closed form
  print((b*2 - a)/ (2 - 1))
  print(2**(n) - 1)
  print(sum(seq))
