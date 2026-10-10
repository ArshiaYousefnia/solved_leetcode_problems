class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [x.lower() for x in s if x.isalnum()]

        n = len(chars)

        for i in range(n // 2):
            if chars[i] != chars[n - i - 1]:
                return False
        
        return True

