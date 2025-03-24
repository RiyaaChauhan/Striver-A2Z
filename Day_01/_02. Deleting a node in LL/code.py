class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        if node is None or node.next is None:
                return
        # Copy the value of the next node into the current node
        node.val = node.next.val
        # Bypass the next node     
        node.next = node.next.next