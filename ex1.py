# Fun with Linked Lists
# this one will make linked lists and do the following:
# 1) add each linked lists values
# 2) carry over the result of the addition if needed to a new node

class ListNode(object):
  
  def __init__(self, x):
    self.val = x
    self.next = None
  
    
def show(l):
  if l is not None:
    print(l.val)
    show(l.next)


def append_to_list(l1, l2):
  
  if l1 is None:
    return
  
  l2.next = ListNode(l1.val)
  append_to_list(l1.next, l2.next)


def create_list(l1, l2, l3):

  if l1 is None or l2 is None:
    append_to_list(l1 or l2, l3)
    return
  
  l3.next = ListNode(l1.val + l2.val)
  create_list(l1.next, l2.next, l3.next)

def lazily_split(l3):
  """
  l3_i.val = l1_i.val + l2_i.val at this point 
  (see create_list)
  """
  
  if l3 is None:
    return
  
  carry = l3.val % 10
  num = l3.val / 10
  
  l3.val = num
  
  if l3.next is not None:
    l3.next.val += carry
  else:
    # handle case where last node's 
    # value needs to be appended 
    if num >= 1:
      l3.next = ListNode(carry)

  lazily_split(l3.next)


def solution(l1, l2):

  # (1) make new list from l1 and l2
  
  l3 = ListNode(None) # pass sentinel node to start list
  create_list(l1 , l2, l3)
  print('created list:')
  show (l3)
  
  # (2) lazily split list nodes if l_i.val >= 10
  #     as follows:
  #       if sum = l1_i.val + l2_i.val > 10, 
  #         carry = sum % 10
  #         l3_i.val = sum /10
  
  lazily_split(l3.next)
  print('split list:')
  show(l3)
  
  
def main():
  
  # l1: ( 10 ) -> ( 11 ) -> None
  # l2: ( 2 ) -> ( 3 ) -> ( 4 ) -> None
  # l3: ( 12 ) -> ( 14 ) -> ( 4 ) -> None 
  #   solution: ( 1 ) -> ( 1 ) -> ( 1 )-> ( 0 ) -> None
  
  l1 = ListNode(9)
  l1.next = ListNode(9)
  l1.next = ListNode(1)
  
  l2 = ListNode(9)
  l2.next = ListNode(1)
  l2.next.next = ListNode(0)
  
  show(solution(l1, l2))

main()
