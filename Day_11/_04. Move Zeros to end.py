class Solution:
    def moveZeroes(self, nums):
        n=len(nums)
        left=0
        for right in range(n):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        
    

                     # OR

def move_zeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
