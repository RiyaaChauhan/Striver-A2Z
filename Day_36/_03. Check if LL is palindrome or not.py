# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list (slow and fast pointers)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Step 3: Compare the first half and the reversed second half
        left = head
        right = prev
        while right:  # Only need to check the second half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True