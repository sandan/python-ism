from collections import defaultdict
from random import seed, randint
from datetime import datetime
from itertools import combinations
from tree import Q

# node factory
node = lambda : defaultdict(node)


def count_in_degree(G):
  """
  counts the in degree of each vertex in G
  """
  count = dict()
  for v in G:
    # init in degree
    count.setdefault(v['value'], 0)

  for v in G:
    for neighbor in v['neighbors']:
      count[neighbor['value']] += 1

  return count

def count_out_degree(G):
  """
  counts the out degree of each vertex in G
  """
  count = dict()
  for v in G:
    count[v['value']] = len(v['neighbors'])

  return count

def make_random_directed_graph(N, **kw):
  """
  make a random graph on N nodes
  """
  graph = dict()

  # init vertices
  vertices = range(1, N + 1)

  for v in vertices:
    q = node()
    q['value'] = v
    q['neighbors'] = [] # formally init with list
    graph[v] = q

  # make edges
  # N choose 2 = N(N-1)/2 ~ O(N^2)
  seed(datetime.today())
  for edge in combinations(range(1, N + 1), 2):
    if randint(0, 1) == 1: # heads
      if randint(0, 1) == 1:
        to, frm = edge[0], edge[1]
      else:
        frm, to = edge[0], edge[1]

      graph[to]['neighbors'] += [graph[frm]]

  return list(graph.values())

def make_random_undirected_graph(N, **kw):
  """
  make a random graph on N nodes
  """
  graph = dict()

  # init vertices
  vertices = range(1, N + 1)

  for v in vertices:
    q = node()
    q['value'] = v
    q['neighbors'] = [] # formally init with list
    graph[v] = q

  # make edges
  # N choose 2 = N(N-1)/2 ~ O(N^2)
  seed(datetime.today())
  for edge in combinations(range(1, N + 1), 2):
    if randint(0, 1) == 1: # heads
      to, frm = edge[0], edge[1]
      graph[to]['neighbors'] += [graph[frm]]
      graph[frm]['neighbors'] += [graph[to]]

  return list(graph.values())

def print_graph(g):
  for v in g:
    print('[{}]: ->'.format(str(v['value'])))
    for neighbor in v['neighbors']:
      print('\t{}'.format(str(neighbor['value'])))

def bfs(g, src, target=None, **kw):
  """
  bfs will modify vertices
  with a distance attribute and parent attribute
  g: the graph
  src: the source vertex in g to run bfs on
  target: optional node.
  """

  # init the graph
  for v in g:
    v['distance'] = None
    v['parent'] = None
    v['visited'] = False

  src['distance'] = 0
  src['visited'] = 'True'
  q = Q()
  q.enqueue(src)

  while not q.isempty():

    v = q.dequeue()

    for u in v['neighbors']:
      if not u['visited']:

        u['visited'] = True # neighbor processed
        u['parent'] = v
        # least distance from src to u is thru v
        u['distance'] = v['distance'] + 1
        q.enqueue(u)


def print_bfs(src, target):
  """
  prints the path from src to target
  after bfs(g, src)
  """
  if target['value'] == src['value']:
    print(target['value'])
  elif target['parent'] is None:
    print('no such path')
  else:
    print_bfs(src, target['parent'])
    print(target['value'])

if __name__ == '__main__':

  # vertices
  G = node()
  G['value'] = 1

  a = node()
  a['value'] = 2

  b = node()
  b['value'] = 3

  c = node()
  c['value'] = 4

  # edges
  a['neighbors'] = [G]
  b['neighbors'] = [G]
  G['neighbors'] = [a]

  # list of adjacency lists
  graph = [G, a, b, c]

#  print('out degree counts: {}'.format(str(count_out_degree(graph))))
#  print('in degree counts: {}'.format(str(count_in_degree(graph))))

  graph = make_random_undirected_graph(5)
  print_graph(graph)

  V = graph[0]
  bfs(graph, V)
  for u in graph:
    if u['value'] != V['value']:
      print('shortest path from {} to {}'.format(V['value'], u['value']))
      print_bfs(V, u)

  # only get the shortest paths to V (in an undirected graph)

  min_dst = min(map(lambda u: u['distance'], filter(lambda v: v['value'] != V['value'] and v['distance'] is not None, graph)))
  for u in graph[1:]:
    if u['distance'] is not None and u['distance'] == min_dst:
      print('[path length {}] to {} <-> from {}'.format(min_dst, V['value'], u['value']))
