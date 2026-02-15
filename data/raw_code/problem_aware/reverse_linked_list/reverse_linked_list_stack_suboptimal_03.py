class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    stack = []
    curr = head

    while curr:
        stack.append(curr)
        curr = curr.next

    new_head = stack.pop()
    curr = new_head

    while stack:
        node = stack.pop()
        curr.next = node
        curr = node

    curr.next = None
    return new_head
"""num_loops = 2
uses_list = 1

    """