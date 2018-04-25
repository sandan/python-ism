from itertools import permutations

def n_k(n, k):
  return permutations(range(n), k)

def combine(x, y, z):
  return x + y + z

def swap(element, res):

  for x in permutations(element[0], len(element[0])):
    for y in permutations(element[1], len(element[1])):
      for z in permutations(element[2], len(element[2])):
        res.add(combine(x, y, z))

# breaks down a permutation into sizes of 3, 3, and 4
def generate_eq_class(element):

  res = set()

  a = element[:3]
  b = element[3:6]
  c = element[6:]

  print(len(a), len(b), len(c))
  print("number of block permutations is: %d" % len(list(permutations([a, b, c], 3))))

  for x in permutations([a, b, c], 3):
    swap(x, res)

  return res

if __name__ == '__main__':

  universe = list(n_k(10, 10))
  print(universe[0])
  eq_class = generate_eq_class(universe[0])
  print(len(eq_class))
  print(6 * 6 * 6 * 4 * 3 * 2)
