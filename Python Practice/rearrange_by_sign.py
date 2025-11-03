# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        po = 0
        neg = 1
        n = len(nums)
        res = [0] * n
        for i in range(0, n):
            if nums[i] > 0:
                res[po] = nums[i]
                po+=2
            if nums[i] < 0:
                res[neg] = nums[i]
                neg+=2
        return res

sol = Solution()
print(sol.rearrangeArray([3,1,-2,-5,2,-4]))
        