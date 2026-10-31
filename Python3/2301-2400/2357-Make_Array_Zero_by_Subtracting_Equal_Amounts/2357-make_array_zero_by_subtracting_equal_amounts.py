class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # Obsereve in each step of example 1, Exactly 1 unique element is subtracted to 0.
        # So we just need to count unique number of elements in nums except 0.
        return (len(set([x for x in nums if x>0])))