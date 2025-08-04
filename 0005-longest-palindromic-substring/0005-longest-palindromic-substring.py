class Solution:
    def longestPalindrome(self, s: str) -> str:
        data = {}

        max_index = None
        max_del = -1

        n = len(s)

        for delta in range(n):
            for i in range(n - delta):
                j = i + delta

                if s[i] == s[j]:
                    if delta < 2:
                        data[(i,j)] = 1
                    else:
                        data[(i,j)] = data[(i + 1, j - 1)]
                    
                    if data[(i,j)] == 1 and (j-i) > max_del:
                        max_index = (i,j)
                else:
                    data[(i,j)] = 0 
        
        if max_index is None:
            return ""
        
        i, j = max_index
        return s[i: j + 1]

        