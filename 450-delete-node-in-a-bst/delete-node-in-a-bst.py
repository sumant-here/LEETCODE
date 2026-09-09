# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):

        # Node not found
        if root is None:
            return None

        # Search in left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Search in right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Node found
        else:

            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: Only right child
            if root.left is None:
                return root.right

            # Case 2: Only left child
            if root.right is None:
                return root.left

            # Case 3: Two children
            successor = root.right

            while successor.left:
                successor = successor.left

            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)

        return root