from itertools import combinations, product

suits = ['heart', 'spade', 'club', 'diamond']
denominations =  [str(i) for i in range(2, 11)] + ['j', 'q', 'k', 'a']
rank = denominations
hands = combinations(product(suits, denominations), 5)
values = dict({ (k, v) for k, v in zip(rank, range(2, len(rank) + 2)) }) # keep ace high
print(values)

# common getters for (suit, denom) in hands
def denom(x):
  return x[1]

def suit(x):
  return x[0]

def value(k):
  return values[k]

# basic filters
def is_consecutive(x):
  """
  filter applied to hands
  Takes a 5-tuple of (suits, rank)
  Returns True if cards are consecutive else False
  TODO: there must be a better way
  """
  nums = list(map(value, map(denom, x)))
  list.sort(nums)

  # check for ace low
  if nums[-1] == 14 and nums[0] == 2:
    for i in range(1, len(nums) - 1):
      if nums[i] - nums[i-1] != 1:
        return False
  else:
    for i in range(1, len(nums)):
      if nums[i] - nums[i-1] != 1:
        return False

  return True

def same_suit(x):
  """
  filter applied to hands
  """
  return len(set(map(suit, x))) == 1

def is_pair(x, y):
  """
  x, y ~ (suit, denom)
  """
  return denom(x) == denom(y)

# counters
def num_pairs(x):
  """
  appplied to hands
  """
  pairs = 0

  for x, y in combinations(x, 2):
    if is_pair(x, y):
     pairs += 1

  return pairs

# poker hand filters

def straight(x):
  """
  applied to hands
  """
  return is_consecutive(x) and not same_suit(x)

def royal_flush(x):
  den = list(map(denom, x))
  return straight_flush(x) and '10' in den and 'a' in den

def straight_flush(x):
  return is_consecutive(x) and flush(x)

def flush(x):
  """
  applied to hands
  Note: this includes royal and straight flushes
  """
  return same_suit(x)

if __name__ == '__main__':

  _hands = list(hands)

  straights = list(filter(straight, _hands))
  royals = list(filter(royal_flush, _hands))
  straight_flushes = list(filter(straight_flush, _hands))
  flushes = list(filter(flush, _hands))

  print('number of royal flushes: {}'.format(len(royals)))
  print('number of straight_flushes: {}'.format(len(straight_flushes)))
  print('number of flushes: {}'.format(len(flushes) - len(straight_flushes) - len(royals)))
  print('number of straights: {}'.format(len(straights)))
