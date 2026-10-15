class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        table = [[0 for _ in range(m)] for _ in range(n)]

        table[0][0] = 1 if text1[0] == text2[0] else 0

        for i in range(1, n):
            table[i][0] = max(table[i - 1][0], 1 if text1[i] == text2[0] else 0)
        
        for j in range(1, m):
            table[0][j] = max(table[0][j - 1], 1 if text1[0] == text2[j] else 0)
        
        for i in range(1, n):
            for j in range(1, m):
                equal = text1[i] == text2[j]

                table[i][j] = max(table[i][j - 1], table[i - 1][j])
                if equal:
                    table[i][j] = max(table[i][j], 1 + table[i - 1][j - 1])
        
        return table[n - 1][m - 1]
