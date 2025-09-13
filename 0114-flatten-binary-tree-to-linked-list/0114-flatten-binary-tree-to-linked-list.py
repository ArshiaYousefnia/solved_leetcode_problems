# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        self.traverse(stack, root)
        n = len(stack)

        for i in range(n-1):
            stack[i].left = None
            stack[i].right = stack[i + 1]

    def traverse(self, stack, node):
        if node is None:
            return

        stack.append(node)

        self.traverse(stack, node.left)
        self.traverse(stack, node.right)
        

