
"""
URL problem:     https://leetcode.com/problems/maximum-depth-of-binary-tree/
Related topics:  | Tree | DFS | BFS | Binary Tree | Recursion |
Idea: 
-------------------------------------------------------------------
La idea es considerar cada subarbol como un arbol unico, y usar la 
misma funcion de forma recursiva para ir sumando 1 cada vez que uno
de los hijos no sea nulo. De igual forma, por cada subarbol se divide
la busqueda. Se guarda la profundidad por cada arbol
Finalmente, se guarda la profundidad de cada subarbol y se obtiene el maximo
"""
from typing import Optional

class Solution:

    class TreeNode:
        def __init__(self) -> None:
            pass

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
   
        subtree_left:int  = self.maxDepth(root.left)
        subtree_right:int = self.maxDepth(root.right)

        return max(subtree_left, subtree_right) + 1

    def maxDepth_v2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth:int = 0
   
        subtree_left:int  = self.maxDepth(root.left)
        subtree_right:int = self.maxDepth(root.right)
        
        if subtree_left > subtree_right:
            depth = 1 + subtree_left
        else:
            depth = 1 + subtree_right
            
        return depth
        
