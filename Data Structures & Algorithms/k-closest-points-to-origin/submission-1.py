class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []

        for x,y in points:
            dist = x*x + y*y

            heapq.heappush(minheap, (dist, x, y))

        res = []

        for i in range (k):
            dist, x, y = heapq.heappop(minheap)
            res.append([x,y])

        return res