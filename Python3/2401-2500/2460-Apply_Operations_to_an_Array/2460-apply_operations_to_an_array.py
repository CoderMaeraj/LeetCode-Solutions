class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)
        new_nums = []
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                (nums[i],nums[i+1]) = (nums[i]*2,0)
        
        for num in nums:
            if num !=0:
                new_nums.append(num)
        while(len(new_nums)<n):
            new_nums.append(0)
        return new_nums
