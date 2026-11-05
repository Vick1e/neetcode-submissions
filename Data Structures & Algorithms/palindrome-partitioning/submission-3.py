class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(start):
            if start ==len(s):
                res.append(path[:])
                return res

            for end in range(start,len(s)):
                sub = s[start:end+1]
                if sub!=sub[::-1]:
                    continue
                path.append(sub)
                dfs(end+1)
                path.pop()

        dfs(0)
        return res

