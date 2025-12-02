from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid -1
                else:
                    low = mid+1
        return -1


sol = Solution()
print(sol.search([11,15,20,1,4,5,6,8,9,10],20))