# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        longest = 0
        for i in range(0, len(nums)):
            my_set.add(nums[i])
        
        for num in my_set:
            if num-1 not in my_set:
                count = 1
                x=num
                while x+1 in my_set:
                    count += 1
                    x+=1
                longest = max(longest, count)
        return longest

        
        