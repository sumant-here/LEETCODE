# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0 
        answer = 0 
        def dfs(node):
            nonlocal count, answer 
            if node is None:
                return 
            #left 
            dfs(node.left)
            count += 1
            # root 
            if count == k :
                answer = node.val
                return 
            #right
            dfs(node.right)
        dfs(root)
        return answer 