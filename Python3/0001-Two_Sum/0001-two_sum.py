from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashi = {}
        for i in range(len(nums)):
            required = target - nums[i]
            if required in hashi.keys():
                return [i,hashi[required]]
            hashi[nums[i]] = i