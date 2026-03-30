# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.d=set()
        return self.dfs(root,k)


    def dfs(self, node: Optional[TreeNode], k:int) -> bool:
        if not node:
            return False
        if k-node.val in self.d:
            return True
        self.d.add(node.val)
        left=self.dfs(node.left,k)
        right=self.dfs(node.right,k)
        return left or right