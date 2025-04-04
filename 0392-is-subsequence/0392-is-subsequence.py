class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        n = len(s)

        if n == 0:
            return True

        for i in t:
            if i == s[s_index]:
                s_index += 1

                if s_index == n:
                    return True
        
        return False
        