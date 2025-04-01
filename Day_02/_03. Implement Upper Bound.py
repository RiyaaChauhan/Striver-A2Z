# class Solution:
#     def findFloor(self, arr, x):
#         left, right=0, len(arr)-1
#         ans=-1
#         while left<=right:
#             mid=left+(right-left)//2
#             if arr[mid]<=x:
#                 ans=mid
#                 left=mid+1
#             else:
#                 right=mid-1
#         return ans
    
class Solution:
    def getFloorAndCeil(self, arr, x):
        floor, ceil = -1, -1  # Default values if no floor/ceil is found
        
        for num in arr:
            if num <= x:  # Check for floor condition
                floor = max(floor, num)
            if num >= x:  # Check for ceil condition
                ceil = min(ceil, num) if ceil != -1 else num
        
        return [floor, ceil]