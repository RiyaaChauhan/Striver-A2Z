class Solution:
    def moveZeroes(self, nums):
        non_zero_index = 0
        n=len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0
        return nums
    

                     # OR

def move_zeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
