class Solution:
    def deleteMiddle(self, head):
        # Edge case: if there is only one node
        if head is None or head.next is None:
            return None
        
        slow = head
        fast = head
        prev = None  # Initialize prev to None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is now at middle node
        # prev is just before slow
        prev.next = slow.next  # Skip the middle node

        return head
