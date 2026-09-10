# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            
            map = {}
            for i,val in enumerate(inorder):
                map[val] =  i
            
            pre_index = 0

            def dfs(left,right):
                
                nonlocal pre_index
                if left>right:
                    return None

                root_val = preorder[pre_index]
                pre_index += 1
                root = TreeNode(root_val)
                mid = map[root_val]

                root.left = dfs(left, mid-1)
                root.right = dfs(mid+1, right)

                return root

            return dfs(0, len(inorder) - 1)

 