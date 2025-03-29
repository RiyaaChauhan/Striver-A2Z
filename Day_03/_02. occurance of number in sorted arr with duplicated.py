class Solution:
    def first_occurrence(self, arr, target):
        low, high = 0, len(arr) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                first = mid
                high = mid - 1  # Move left to find first occurrence
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first
    
    def last_occurrence(self, arr, target):
        low, high = 0, len(arr) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                last = mid
                low = mid + 1  # Move right to find last occurrence
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last
    def countFreq(self, arr, target):
        first = self.first_occurrence( arr, target)
        if first == -1:
            return 0  # Target not found
        last = self.last_occurrence(arr, target)
        return last - first + 1