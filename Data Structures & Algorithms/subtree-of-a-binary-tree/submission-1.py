# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            def dfs(p, q):
                if not p and not q:
                    return True
                
                if (p and not q) or (q and not p):
                    return False
                
                if p.val != q.val:
                    return False
                
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            
            return dfs(p, q)
        
        def dfs(root, subRoot):
            if not root:
                return False
            
            if root.val == subRoot.val and isSameTree(root, subRoot):
                return True

            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)