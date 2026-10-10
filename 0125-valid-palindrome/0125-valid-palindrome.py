class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = list(filter(lambda y: y is not None, map(lambda x: x.lower() if x.isalnum() else None, s)))

        n = len(chars)

        for i in range(n // 2):
            if chars[i] != chars[n - i - 1]:
                return False
        
        return True

