# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        # Base Case: Empty or single node
        if not head or not head.next:
            return head

        # Recurse till the end
        new_head = self.reverseList(head.next)

        # Reverse the link
        head.next.next = head
        head.next = None

        return new_head