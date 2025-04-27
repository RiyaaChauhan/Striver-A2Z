def lengthOfLoop(head):

    if not head:
        return 0

    slow = head
    fast = head

    # Detect cycle using Floyd?s Tortoise and Hare Algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:  # Cycle detected
            # Count the length of the cycle
            length = 1
            current = slow.next
            while current != slow:
                current = current.next
                length += 1
            return length
    return 0  # No cycle