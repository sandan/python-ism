class ListNode(object):
  
  def __init__(self, x):
    self.val = x
    self.next = None
  
    
def show(l):
  # just a helper method for printing out nodes
  if l is not None:
    print(l.val)
    show(l.next)


def append_to_list(l, l3):
  
  if l is None:
    return

  carry = 0
  if (l3.val >= 10):
    carry = carry_over(l3)

  l3.next = ListNode(carry + l.val)
  append_to_list(l.next, l3.next)


def carry_over(l3):
  
  carry = l3.val / 10 # 0 <= l3.val <=18
  new_val = l3.val % 10
  l3.val = new_val
  return carry
  
  
def create_list(l1, l2, l3):

  # l1 and l2 have single digit values
  # so we carry over a 1 at most
  if l1 is None or l2 is None:
    append_to_list(l1 or l2, l3)
    return

  carry = 0
  if (l3.val >= 10):
    # carry_over
    carry = carry_over(l3)
    
  l3.next = ListNode(carry + l1.val + l2.val)
  create_list(l1.next, l2.next, l3.next)


def solution(l1, l2):
  
  # (1) make new list from l1 and l2
  #     whilst:
  #
  #     (2) eagerly split list nodes if l_i.val >= 10
  #       as follows:
  #         if sum = l1_i.val + l2_i.val > 10, 
  #          carry = sum / 10
  #          l3_i.val = sum % 10
  
  # pass sentinel node to be head of list
  head = ListNode(None) 
  create_list(l1 , l2, head)
  head = head.next
  
  # take care of edge case when last node is >=10
  print('created list:')
  show (head)

def main():
  
  # l1:          ( 9 )  ->  ( 9 ) -> ( 1 ) -> (8) -> None
  # l2:          ( 9 )  ->  ( 1 ) -> ( 0 ) -> None
  # l3:  None -> ( 8 ) -> ( 1 ) -> ( 2 ) -> None 

  l1 = ListNode(9)
  l1.next = ListNode(9)
  l1.next.next = ListNode(9)
  l1.next.next.next = ListNode(9)
  
  l2 = ListNode(9)
  l2.next = ListNode(9)
  l2.next.next = ListNode(9)
  
  solution(l1, l2)
main()
