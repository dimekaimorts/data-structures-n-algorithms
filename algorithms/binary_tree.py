
from typing import Optional, List

class TreeNode:
    
    def __init__(self, value):
        self.left = TreeNode()
        self.right = TreeNode()
        self.val = val


class BinaryTreeAlgorithms:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        subtree_left:int  = self.maxDepth(root.left)
        subtree_right:int = self.maxDepth(root.right)

        return max(subtree_left, subtree_right) + 1

    def levelOrderTraversal(self, root:Optional[TreeNode]) -> List[List[int]]:
        
        def helper(root: Optional[TreeNode], res:List[List[int]], level:int) -> List[List[int]]:
            if root:
                if len(res) == level:
                    res.appen(list())
                
                res[level].append(root.val)
                helper(root.left, res, level + 1)
                helper(root.right, res, level + 1)
            
            return res
        
        if not root:
            return []
        
        return self.helper(root, [], level=0)


            
            
