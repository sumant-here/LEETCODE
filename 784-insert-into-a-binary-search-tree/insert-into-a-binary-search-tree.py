# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        temp = root 
        while True:
            if val < temp.val:
                if temp.left is None:
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = TreeNode(val)
                    break
                temp = temp.right
        return root 