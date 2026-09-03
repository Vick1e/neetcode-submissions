# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if not q and not p:
                return True

            if not p or not q:
                return False

            if q.val != p.val:
                return False

            left = sameTree(p.left, q.left)
            right = sameTree(p.right, q.right)

            return left and right

        if not root:
            return False

        # left = sameTree(root.left, subRoot)
        # right = sameTree(root.right, subRoot)
        Same = sameTree(root, subRoot)


        if Same:
            return True

        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
                
