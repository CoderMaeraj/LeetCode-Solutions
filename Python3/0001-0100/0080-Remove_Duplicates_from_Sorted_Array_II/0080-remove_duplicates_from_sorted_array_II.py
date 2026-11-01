class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        crsi = 0
        rem = 0
        i = 1
        while(i < (n-rem)):
            if nums[i] != nums[crsi]:
                crsi = i
                i += 1
            elif (nums[i] == nums[crsi]) and ((i-crsi)>=2):
                nums.append(nums.pop(i))
                rem += 1
            else:
                i += 1
        return (n-rem)