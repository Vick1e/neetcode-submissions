class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[]for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node,parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbour in graph[node]:
                if neighbour == parent:
                    continue

                if not dfs(neighbour,node):
                    return False

            return True

        if not dfs(0,-1):
            return False

        return len(visited) == n
