class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        hashi = {}
        nums.sort()
        n = len(nums)
        for i in range(n):
            if hashi.get(nums[i],0):
                hashi[nums[i]] += 1
            else:
                if nums[i]%2 == 0:
                    hashi[nums[i]] = 1
        val = 0
        key = -1
        for (k,v) in hashi.items():
            if v > val:
                key, val = k,v
        return key