class Solution:
    def majorityElement(self, nums):
        # Size of the given array
        n = len(nums)
        cnt = 0  # Count
        el = None  # Element

        # Applying the algorithm
        for i in range(n):
            if cnt == 0:
                cnt = 1
                el = nums[i]
            elif el == nums[i]:
                cnt += 1
            else:
                cnt -= 1

        # Checking if the stored element is the majority element
        cnt1 = 0
        for i in range(n):
            if nums[i] == el:
                cnt1 += 1

        if cnt1 > (n / 2):
            return el
        return -1