# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [SOL1 - BFS]
# from collections import deque
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         max_depth =1
        
#         if root is None:
#             return 0

#         q = deque()
#         q.append((root,max_depth))

#         while q:
#             next_v,next_depth = q.popleft()
#             max_depth = next_depth

#             if next_v.left:
#                 q.append((next_v.left,max_depth+1))
#             if next_v.right:
#                 q.append((next_v.right,max_depth+1))
#         return max_depth

# [SOL2 - DFS]
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
            
        return max(left_depth, right_depth) +1