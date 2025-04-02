class Solution:
        
    def countFreq(self, arr, target):
        first=self.firstoccurance(arr,target)
        last=self.lastoccurance(arr,target)
        if first==-1:
            return 0
        return last-first+1
    
    def firstoccurance(self,arr,target):
        low,high=0,len(arr)-1
        first=-1
        while low<=high:
            mid= low+(high-low)//2
            if arr[mid]==target:
                first=mid
                high=mid-1
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return first
                
    def lastoccurance(self,arr,target):
        low,high=0,len(arr)-1
        last=-1
        while low<=high:
            mid= low+(high-low)//2
            if arr[mid]==target:
                last=mid
                low=mid+1
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return last