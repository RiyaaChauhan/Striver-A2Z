class Solution:
    def getFloorAndCeil(self, arr, x):
        floor, ceil = -1, -1  # Default values if no floor/ceil is found
        
        for num in arr:
            if num <= x:  # Check for floor condition
                floor = max(floor, num)
            if num >= x:  # Check for ceil condition
                ceil = min(ceil, num) if ceil != -1 else num
        
        return [floor, ceil]