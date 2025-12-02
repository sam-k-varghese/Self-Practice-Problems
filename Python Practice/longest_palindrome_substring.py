class Solution:
    @staticmethod
    def check_palindrome(str1):
        print("inside check")
        n = len(str1)
        if n == 1:
            return (True, str1)
        for i in range(0, n):
            if str1[i] != str1[n-i-1]:
                return (False, None)
        return (True, str1)

    def longestPalindrome(self, s: str) -> str:
        largest = ""
        if len(s) == 1:
            largest = s
        for i in range(0, len(s)-1):
            subs = ""
            for j in range(i+1, len(s)):
                subs += s[j]
                (res,str2) =  self.check_palindrome(subs)
                if res == True:
                    print(res)
                    if len(largest) < len(str2):
                        largest = str2
        return largest


sol = Solution()
print(sol.longestPalindrome("a"))