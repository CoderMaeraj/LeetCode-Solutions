class Solution:
    def maxArea(self, height: list[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        area = 0
        while p1<p2:
            y = min(height[p1], height[p2])
            x = p2 - p1
            area = max(area,x*y)
            if y == height[p1]:
                p1 +=1
            else:
                p2-=1
        return area