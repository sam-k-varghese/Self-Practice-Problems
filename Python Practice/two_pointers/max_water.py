# 11. Container With Most Water
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height) - 1
        start = 0
        end = n
        final_area = 0
        while start < end:
            if height[start] <= height[end]:
                area = height[start] * (end)
                print(f"start: {height[start]}, end: {height[end]}, area = : {height[start]} * {n-1} = {area}")
                final_area = max(area, final_area)
                start +=1
            elif height[start] > height[end]:
                area = height[end] * (end-start)
                print(f"start: {height[start]}, end: {height[end]}, area = : {height[end]} * {end-start} = {area}")
                final_area = max(area, final_area)
                end-=1
        return final_area

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))