class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:
    def reverseDLL(self, head):
        if head is None or head.next is None:
            return head
        prevNode = None
        currNode = head
        while currNode is not None:
            prevNode = currNode.prev
            currNode.prev = currNode.next
            currNode.next = prevNode
            currNode = currNode.prev
        return prevNode.prev
    def printList(node):
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()