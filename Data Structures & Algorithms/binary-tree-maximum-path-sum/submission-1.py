class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def path(root):
            if not root:
                return 0    
            left = max(0,path(root.left))
            right = max(0,path(root.right))

            self.max_sum = max(self.max_sum, root.val+left+right)

            return root.val+max(left,right)
        self.max_sum = root.val
        path(root)
        return self.max_sum