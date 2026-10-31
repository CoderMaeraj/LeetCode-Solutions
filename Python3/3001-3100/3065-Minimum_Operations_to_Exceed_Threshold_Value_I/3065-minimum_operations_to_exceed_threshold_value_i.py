from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans=0
        for i in range(n):
            if nums[i] < k:
                ans+=1
        return ans