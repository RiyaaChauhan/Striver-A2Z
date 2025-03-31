class Solution:
    def findMin(self, nums):
        low, high = 0, len(nums) - 1
        ans = float('inf')  # Initialize with a high value
        while low <= high:
            mid = (low + high) // 2  # Integer division
            if nums[low] <= nums[high]:
                ans = min(ans, nums[low])
                break

            # Update answer
            ans = min(ans, nums[mid])

            # Determine which half to explore
            if nums[mid] >= nums[low]:  # Left half is sorted, go right
                low = mid + 1
            else:  # Right half is sorted, go left
                high = mid - 1

        return ans