class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        graph  = [[] for _ in range (n+1)]

        def dfs(node,target,visited):

            if node == target:
                return True

            if node in visited:
                return False

            visited.add(node)

            for nb in graph[node]:

                if dfs(nb,target,visited):
                    return True

            return False

        for a,b in edges:
            visited = set()

            if dfs(a,b,visited):
                return [a,b]

            graph[a].append(b)
            graph[b].append(a)

        return []


            