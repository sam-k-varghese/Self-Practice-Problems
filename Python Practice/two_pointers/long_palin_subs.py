# 5. Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution(object):

    @staticmethod
    def is_palin(s:str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    @staticmethod
    def is_palindrome(s:str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return True
        for i in range(len(s) // 2):
            j = len(s)-1-i
            if s[i] != s[j]:
                return False
        return True

    @staticmethod
    def is_palindrome2(s:str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        n = len(s)
        if n == 0:
            return ""
        if n == 1:
            return s
        for i in range(n):
            for j in range(i+1, n+1):
                if self.is_palindrome(s[i:j]):
                    if len(s[i:j]) > len(longest):
                        longest = s[i:j]
        

        return longest


sol =  Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))


def is_palin(s:str) -> bool:
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True