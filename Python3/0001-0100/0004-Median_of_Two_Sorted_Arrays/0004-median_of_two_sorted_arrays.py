from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        n = len(nums)
        if n%2 == 0:
            return float((nums[n//2] + nums[(n//2)-1])/2)
        else:
            return float(nums[n//2])