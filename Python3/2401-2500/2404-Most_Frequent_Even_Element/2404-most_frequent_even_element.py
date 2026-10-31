class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        hashi = {}
        for num in nums:
            if num%2 == 0:
                hashi[num] = hashi.get(num,0) + 1
        val = 0
        key = -1
        for (k,v) in hashi.items():
            if (v > val) or (v==val and k < key):
                key, val = k,v
        return key