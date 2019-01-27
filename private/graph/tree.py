from collections import defaultdict
from functools import wraps

node = lambda : defaultdict(node)

def inorder(T):
  """
  generator yields tree T in order
  """
  if not T:
    return

  yield from inorder(T['left'])
  yield T['value']
  yield from inorder(T['right'])

def preorder(T):
  """
  generator yields tree T in preorder
  """
  if not T:
    return

  yield T['value']
  yield from inorder(T['left'])
  yield from inorder(T['right'])

def postorder(T):
  """
  generator yields tree T in postorder
  """
  if not T:
    return

  yield from inorder(T['left'])
  yield from inorder(T['right'])
  yield T['value']


def print_tree(T, order='inorder'):
  """
  prints a tree in various orders
  """

  if order == 'inorder':
    x = ' '.join([str(n) for n in inorder(T)])
  elif order == 'preorder':
    x = ' '.join([str(n) for n in preorder(T)])
  else:
    x = ' '.join([str(n) for n in postorder(T)])

  print( x )

def check_state(fn):
  def inner(n, q, N, **kw):
    print('n: {}'.format(n))
    print('queue: {}'.format(list(map(lambda x: str(x['value']), q))))
    return fn(n, q, N, **kw)
  return inner

class Q(list):
  """
  Queue implemented as a list
  """
  def __init__(self, elmts = [], **kw):
    super().__init__(elmts)

  def enqueue(self, x):
    self.append(x)

  def dequeue(self):
    if len(self) > 0:
      return self.pop(0)
    else:
      return None

  def isempty(self):
    return len(self) == 0

@check_state
def make_binary_tree_helper(n, q, N, **kw):

  if n <= 0 :
    # q will have all the leaves at this point
    return

  v = q.dequeue()

  # we only enqueue nodes if n >= 1
  if n >= 1:
    v['left'] = node()
    v['left']['value'] = N - n
    q.enqueue(v['left'])

  if n >= 2:
    v['right'] = node()
    v['right']['value'] = N - (n - 1)
    q.enqueue(v['right'])

  make_binary_tree_helper(n - 2 if n >= 2 else n - 1, q, N, **kw)


def make_binary_tree(n, **kw):
  """
  Make a binary tree on n nodes
  """
  if n <= 0:
    return None

  v = node()
  v['value'] = 0
  if n == 1:
    return v

  q = Q()
  q.enqueue(v)
  make_binary_tree_helper(n - 1, q, n, **kw)
  return v

if __name__ == '__main__':

  G = node()
  G['value'] = 1
  G['left']['value'] = 2
  G['right']['value'] = 3

  print_tree(G)

  v = make_binary_tree(7)
  print_tree(v, 'inorder')

  v = make_binary_tree(16)
  print_tree(v, 'inorder')
