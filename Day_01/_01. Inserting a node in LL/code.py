class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
 

class Solution:
    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        new_node = Node(x)  # Use x instead of 'data'
        
        # If the linked list is empty, return the new node as the head
        if head is None:
            return new_node
        
        curr = head
        while curr.next is not None:
            curr = curr.next
        
        curr.next = new_node  # Append new node at the end
        
        return head  # Return the updated head
