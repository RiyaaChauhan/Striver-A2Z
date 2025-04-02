
from typing import List
class Solution:
    def largest(self, arr):
        largest=arr[0]
        n=len(arr)
        for i in range(1,n):
            if largest<arr[i]:
                largest=arr[i]
        return largest