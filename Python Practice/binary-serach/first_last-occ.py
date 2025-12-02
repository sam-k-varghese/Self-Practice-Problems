from typing import List

class Solution:
    def lowerBound(self, nums, target):
        n = len(nums)
        low = 0
        high = n-1
        lb = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                lb = mid
                high = mid -1

            elif nums[mid]>target:
                high = mid -1
            else:
                low = mid+1
        return lb
    
    def upperBound(self, nums, target):
        n = len(nums)
        low = 0
        high = n-1
        ub = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                ub=mid
                low=mid+1
            if nums[mid]> target:
                high = mid -1
            else:
                low = mid+1
        return ub
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.lowerBound(nums, target)
        if first == -1:
            return [-1,-1]
        else:
            last = self.upperBound(nums, target)
        return [first, last]



sol = Solution()
print(sol.searchRange([2,2],2))