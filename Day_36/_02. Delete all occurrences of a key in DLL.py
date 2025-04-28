def deleteAllOccurrences(head, k: int):
    # Initialize current node
    current = head
    # Traverse the list
    while current:
        if current.data == k:
            # If it's the head node
            if current.prev is None:
                head = current.next
                if head:
                    head.prev = None
            # If it's the tail node
            elif current.next is None:
                current.prev.next = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
        current = current.next
    
    return head