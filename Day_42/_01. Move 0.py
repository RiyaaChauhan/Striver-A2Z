class Solution:
    def moveZeroes(self, nums):
        j = 0  # position to place the next non-zero element

        # First pass: move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # Second pass: fill the rest with zeroes
        while j < len(nums):
            nums[j] = 0
            j += 1