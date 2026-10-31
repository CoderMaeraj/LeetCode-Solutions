class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k == 0:
            return False
        window = set()
        for i in range(len(nums)):
            if (i > k):
                window.discard(nums[i-k-1])
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False