class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    new_head = None
    curr = head

    while curr:
        new_node = ListNode(curr.val)
        new_node.next = new_head
        new_head = new_node
        curr = curr.next

    return new_head
"""num_loops = 1
uses_list = 0

    """