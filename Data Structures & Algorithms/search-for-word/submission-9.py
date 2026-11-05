class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        # i 表示当前要匹配 word 中第几个字母
        def dfs(r,c,i):

            # 如果 i 等于 word 的长度
            # 说明整个单词已经匹配成功
            if i==len(word):
                return True
            
            # 检查是否越界、格子是否已经使用过
            # 或者当前字母是否与 word[i] 不相同
            if (r<0 or c<0 or
                r>=row or c>=col or
                board[r][c] != word[i]):

                return False


            # 保存当前位置原来的字母
            temp = board[r][c]

            # 标记当前格子已经使用
            # 避免同一条路径重复使用
            board[r][c]="#"

            found=(
                dfs(r+1,c,i+1)or
                dfs(r,c+1,i+1)or
                dfs(r-1,c,i+1)or
                dfs(r,c-1,i+1)
            )

            # 回溯：恢复原来的字母
            # 让其他搜索路径还能使用这个格子
            board[r][c]=temp

            return found


        # 遍历整个二维数组
        # 尝试从每一个格子开始搜索
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True

        # 所有起点都尝试过，仍然找不到
        return False



