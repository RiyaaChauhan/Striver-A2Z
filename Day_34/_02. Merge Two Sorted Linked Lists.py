# Definition for singly-linked list.
# ITERATIVE
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy_node=ListNode(0)
        curr=dummy_node
        while list1 and list2:
            if list1.val<list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        if list1:
            curr.next=list1
        if list2:
            curr.next=list2
        return dummy_node.next
    

    ## RECURSIVE:

    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy_node=ListNode(0)
        curr=dummy_node
        while list1 and list2:
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2

            curr=curr.next
        if list1:
            curr.next=list1
        if list2:
            curr.next=list2
        return dummy_node.next