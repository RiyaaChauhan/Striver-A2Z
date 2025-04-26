class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findKthFromLast(head, k):
    if not head or k <= 0:  # Edge case: empty list or invalid k
        return None

    i = head  # Initialize `i` pointer at head
    j = head  # Initialize `j` pointer at head

    # Move `j` pointer k steps ahead
    for _ in range(k):
        if not j:  # If `j` reaches the end before `k` steps, return None
            return None
        j = j.next
    
    # Now move both `i` and `j` pointers in parallel
    while j:
        i = i.next  # Move `i` one step
        j = j.next  # Move `j` one step
    
    return i  # `i` is now at the k-th node from the end


# or

def findKthFromLast(head,k):

        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length of the list
        length = 1
        current = head
        while current.next:
            length += 1
            current = current.next
        
        # Step 2: Find the effective k (in case k is larger than length)
        k = k % length
        
        # Step 3: If k is 0, no rotation is needed
        if k == 0:
            return head
        
        # Step 4: Find the (length - k)-th node
        current = head
        for _ in range(length - k - 1):
            current = current.next
        
        # Step 5: Make the necessary connections
        new_head = current.next
        current.next = None
        current = new_head
        
        while current.next:
            current = current.next
        current.next = head
        
        return new_head