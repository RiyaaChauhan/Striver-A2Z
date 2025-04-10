class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        return (n*(n+1)//2-sum(nums))
    
          # OR 

class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        xor1=0
        xor2=0

        for i in range(n + 1):
            xor1 ^= i
        for y in nums:
            xor2 ^= y

        return xor1 ^ xor2