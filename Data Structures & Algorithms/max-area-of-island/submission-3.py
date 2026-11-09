class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxA = 0

        def dfs(r,c):
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == 0):
                return 0

            grid[r][c] = 0
            area = 1

            area += dfs(r + 1, c)  # 下
            area += dfs(r - 1, c)  # 上
            area += dfs(r, c + 1)  # 右
            area += dfs(r, c - 1)  # 左

            return area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)

                    maxA = max(area, maxA)

        return maxA