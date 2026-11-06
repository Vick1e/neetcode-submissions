class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        root = {}

        # 第一步：把所有单词放进 Trie
        for word in words:
            node = root

            for char in word:
                if char not in node:
                    node[char]={}
                node = node[char]

            node["#"]=word

            row = len(board)
            col = len(board[0])

        # 第二步：定义 DFS
        def dfs(r,c,node):
            if r<0 or c<0 or r>=row or c>=col:
                return

            char = board[r][c]

            if char == "@" or char not in node:
                return 

            node = node[char]

            if "#" in node:
                res.append(node["#"])

                del node["#"]

                # 棋盘：标记当前格子已使用
            temp = board[r][c]
            board[r][c] = "@"

            dfs(r + 1, c, node)  # 下
            dfs(r - 1, c, node)  # 上
            dfs(r, c + 1, node)  # 右
            dfs(r, c - 1, node)  # 左

            board[r][c] = temp


        for r in range(row):
            for c in range(col):
                dfs(r,c,root)

        return res

        