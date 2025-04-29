# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        def reverse(start, end):
            prev = None
            curr = start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Find the kth node
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # If fewer than k nodes left, done

            group_next = kth.next
            # Reverse the group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Rearranging connections
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp