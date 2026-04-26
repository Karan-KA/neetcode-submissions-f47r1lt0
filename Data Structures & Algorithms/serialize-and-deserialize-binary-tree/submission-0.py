# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return 'N'

        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return f"{root.val},{left},{right}"            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        self.idx = 0
        data = data.split(',')

        def helper():
            if data[self.idx] == 'N':
                self.idx += 1
                return None
            node =  TreeNode(data[self.idx])
            self.idx+=1
            node.left = helper()  
            node.right = helper()  

            return node
        return helper()




