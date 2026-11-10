"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(cur):
            if cur in visited:
                return visited[cur]

            copy = Node(cur.val)
            visited[cur] = copy

            for neighbor in cur.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)


