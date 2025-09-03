class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        matrix = [list(map(int, matrix[i])) for i in range(m)]

        maximum = 1 if (1 in matrix[m-1] + [matrix[i][n-1] for i in range(m)]) else 0

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if matrix[i][j] == 0:
                    continue
                
                matrix[i][j] += min(
                    matrix[i+1][j],
                    matrix[i][j+1],
                    matrix[i+1][j+1]
                )

                maximum = max(maximum, matrix[i][j])

        return maximum * maximum

        