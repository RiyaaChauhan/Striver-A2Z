class Solution:
    def check(self, nums):
        n = len(nums)
        count = 0  # Count the number of out-of-order pairs

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Compare with next element (circular)
                count += 1
            if count > 1:  # More than 1 disorder means not a rotated sorted array
                return False

        return True  # At most 1 disorder means it's a rotated sorted array