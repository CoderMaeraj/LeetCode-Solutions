class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        req = nums[n//2]
        step = 0
        for num in nums:
            step = step + abs(req-num)
        return step