class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        while node:
            node.next, next = prev, node.next
            prev, node = node, next
        return prev