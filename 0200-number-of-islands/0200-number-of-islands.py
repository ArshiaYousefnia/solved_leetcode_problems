class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    self._dfsIsland(grid=grid, root=(i, j))
        
        return count


    def _dfsIsland(self, grid:List[List[str]], root:Tuple[int, int]) -> None:
        n = len(grid)
        m = len(grid[0])
        
        i, j = root

        if grid[i][j] == "0":
            return
        
        grid[i][j] = "0"
        
        neighbours_x = [1, 0, -1, 0]
        neighbours_y = [0, 1, 0, -1]

        for k in range(len(neighbours_x)):
            new_i = i + neighbours_x[k]
            new_j = j + neighbours_y[k]

            if new_i < 0 or new_i >= n:
                continue
            if new_j < 0 or new_j >= m:
                continue

            if grid[new_i][new_j] != "0":
                self._dfsIsland(grid=grid, root=(new_i, new_j))
        
