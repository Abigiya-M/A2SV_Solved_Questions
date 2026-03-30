# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        lookup = defaultdict(int)
        for i,el in enumerate(postorder):
            lookup[el] = i
        self.Idx = 0
        def build(left, right):
            if self.Idx>len(preorder) or left>right:
                return None
            
            # Create root from preorder
            value = preorder[self.Idx]
            node = TreeNode(value)
            self.Idx+=1

            # If this subtree has only one node, return it
            if left == right:
                return node

            # Next preorder value is left subtree root
            valLeft = preorder[self.Idx]
            i = lookup[valLeft]

            # Recursively build left and right subtrees
            node.left = build(left, i)
            node.right = build(i+1, right-1)
            return node
        
        return build(0, len(postorder)-1)
            