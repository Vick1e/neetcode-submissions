import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        heap = [(0,0)]
        total_cost = 0


        while len(visited)<n:
            cost, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            total_cost += cost

            x1, y1 = points[node]

            for nb in range(n):
                if nb not in visited:
                    x2, y2 = points[nb]

                    dis = abs(x1-x2) + abs(y1-y2)

                    heapq.heappush(heap, (dis,nb))

        return total_cost

