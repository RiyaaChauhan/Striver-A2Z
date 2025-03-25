class Solution:
    def findFloor(self, arr, x):
        left, right=0, len(arr)-1
        ans=-1
        while left<=right:
            mid=left+(right-left)//2
            if arr[mid]<=x:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans