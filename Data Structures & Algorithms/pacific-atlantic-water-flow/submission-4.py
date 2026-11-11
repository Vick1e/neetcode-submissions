class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(q, visited):
            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc

                    if (0<=nr<rows and
                        0<=nc<cols and 
                        (nr,nc) not in visited and        
                         heights[nr][nc]>=heights[r][c]):

                         visited.add((nr,nc))
                         q.append((nr,nc))

        p_q = deque()
        a_q = deque()

        for r in range(rows):
            pacific.add((r,0))
            p_q.append((r,0))

            atlantic.add((r,cols-1))
            a_q.append((r,cols-1))

        for c in range (cols):
            pacific.add((0,c))
            p_q.append((0,c))

            atlantic.add((rows-1,c))
            a_q.append((rows-1,c))

        # 从太平洋边界开始 BFS
        bfs(p_q, pacific)

        # 从大西洋边界开始 BFS
        # queue 对应 atlantic_queue，visited 对应 atlantic
        bfs(a_q, atlantic)

        # & 表示集合交集，找出两个海洋都能到达的坐标
        return [[r, c] for r, c in pacific & atlantic]
