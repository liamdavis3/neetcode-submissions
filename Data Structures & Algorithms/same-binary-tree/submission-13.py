# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        print(self.solo_dfs(p))
        print(self.dfs(p,q))

        if not p and not q:
            return True
        if not p or not q:
            return False
        if self.solo_dfs(p) != self.solo_dfs(q):
            return False
        return self.solo_dfs(p) == self.dfs(p, q)

    def solo_dfs(self, root):
        if not root:
            return 0
        return 1 + self.solo_dfs(root.left) + self.solo_dfs(root.right)


    def dfs(self, p, q) -> int:
        #base case w no children returns 0
        if not p or not q:
            return 0
        if p.val != q.val:
            return 0
        return 1 + self.dfs(p.left,q.left) + self.dfs(p.right, q.right)  
        

        
            

