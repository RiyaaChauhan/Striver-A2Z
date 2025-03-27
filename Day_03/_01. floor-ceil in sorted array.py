def getFloorAndCeil(a, n, x):
    left, right = 0, n - 1
    floor, ceil = -1, -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if a[mid] == x:
            return (a[mid], a[mid])  # If x is found, both floor and ceil are x
        
        if a[mid] < x:
            floor = a[mid]  # Update floor
            left = mid + 1
        else:
            ceil = a[mid]  # Update ceil
            right = mid - 1

    return (floor, ceil)