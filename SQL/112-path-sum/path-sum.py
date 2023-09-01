# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        target=targetSum-(root.val)
        if not root.right and not root.left and target==0:
            return True
        if self.hasPathSum(root.left,target):
            return True
        if self.hasPathSum(root.right,target):
            return True
        return False   