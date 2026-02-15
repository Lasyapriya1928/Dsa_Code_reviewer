class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    if not head or not head.next:
        return head

    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None

    return new_head
#Pattern: Recursive
#Time: O(n)
#Space: O(n) (call stack)

