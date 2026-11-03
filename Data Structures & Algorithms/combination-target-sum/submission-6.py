class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(start, path, total):

            if total == target:
                res.append(path[:])
                return
            if total>target:
                return 

            for i in range(start, len(nums)):
                path.append(nums[i])
                
                dfs(i, path, total+nums[i])

                path.pop()

        dfs(0,[],0)

        return res

            

