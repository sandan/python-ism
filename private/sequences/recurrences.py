

def fibonacci(stop = None, **kw):
  """
  The Fibonacci recurrence is defined by
  a0 = 0, a1 = 1, a_n = a_{n-1} + a_{n-2} for n >= 2
  """
  a_2 = 0
  yield a_2

  a_1 = 1
  yield a_1

  while True:
    a_n = a_1 + a_2

    yield a_n

    a_2 = a_1
    a_1 = a_n

if __name__ == '__main__':

  # fib generator
  f = fibonacci()
  for times in range(16):
    print(next(f))
