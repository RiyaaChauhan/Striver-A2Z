#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0
        
class Solution:
    def getCount(self, head):
        count=0
        curr=head
        while curr!=None:
            curr=curr.next
            count +=1
        return count