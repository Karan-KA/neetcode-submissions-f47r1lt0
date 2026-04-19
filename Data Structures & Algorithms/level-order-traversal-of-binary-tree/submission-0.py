# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        
        while queue:
            sub = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                sub.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sub)

        return res


        