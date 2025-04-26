class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                break
        if not fast or not fast.next:
            return None
        slow = head  # Reset slow to head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow  # This is the node where the cycle starts