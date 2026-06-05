# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.dfs(root)

    def dfs(self, root) -> int:
        #base case w no children returns 0
        if not root:
            return 0

        #add 1 each time for longest
        return 1 + (max(self.dfs(root.right), self.dfs(root.left)))

        


