class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v,w))
        
        dist = [float('inf')] * (n+1)

        dist[k] = 0

        heap=[(0,k)]
        
        while heap:
            time, node = heapq.heappop(heap)

            if time > dist[node]:
                continue

            for nb ,we in graph[node]:

                new_time = time + we


                if new_time< dist[nb]:
                    dist[nb] = new_time
                    heapq.heappush(heap,(new_time,nb))

        ans = max(dist[1:])

        return ans if ans != float('inf') else -1




