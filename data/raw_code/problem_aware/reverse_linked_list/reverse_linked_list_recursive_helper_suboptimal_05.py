class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def helper(prev, curr):
    if not curr:
        return prev
    nxt = curr.next
    curr.next = prev
    return helper(curr, nxt)

def reverse_list(head):
    return helper(None, head)

"""has_recursion = 1
num_functions = 2
"""