# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minval(root):
            curr=root
            while curr and curr.left:
                curr=curr.left
            return curr
        
        
        if not root:
            return root
        elif key>root.val:
            root.right=(self.deleteNode(root.right,key))
        elif key<root.val:
            root.left=(self.deleteNode(root.left,key))
        else:
            if not root.left and not root.right:
                root=None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                mval=minval(root.right)
                root.val=mval.val
                root.right=self.deleteNode(root.right,mval.val)
        return root
