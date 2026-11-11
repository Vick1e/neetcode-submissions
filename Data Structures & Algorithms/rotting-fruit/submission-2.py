class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0

        minutes = 0

        for r in range(rows):
            for c in range (cols):
                if grid[r][c] == 2:
                    q.append((r,c))

                elif grid[r][c] == 1:
                    fresh +=1

        
        directions = [
            (1, 0),   # 下
            (-1, 0),  # 上
            (0, 1),   # 右
            (0, -1)   # 左
        ]

        while q and fresh > 0 :
            size = len(q)

            for i in range (size):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if grid[nr][nc]!=1:
                        continue

                    grid[nr][nc] = 2

                    fresh -=1

                    q.append((nr,nc))

            minutes += 1

            # 如果所有新鲜水果都腐烂了
        if fresh == 0:

            # 返回经过的分钟数
            return minutes

        # 如果还有新鲜水果，但已经无法继续传播
        # 说明有水果永远无法腐烂，返回-1
        return -1

