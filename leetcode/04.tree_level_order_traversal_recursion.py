
"""
URL problem:     https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
Related topics:  | Tree | DFS | BFS | Binary Tree | Recursion |
Idea: 
-------------------------------------------------------------------
La idea es considerar cada subarbol como un arbol unico, y usar una
funcion helper de forma recursiva para ir bajando a traves del arbol
por nivel. Cuando nos encontremos en un nuevo nivel, creamos una nueva
lista que va a albergar el valor de los nodos a esa altura del nivel
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        return self.__helper(root, [], level=0)

    def __helper(self, root: Optional[TreeNode], res:List[List[int]], level:int) -> List[List[int]]:
        if root:
            if len(res) == level:
                res.append(list())
            
            res[level].append(root.val)
            self.__helper(root.left, res, level + 1)
            self.__helper(root.right, res, level + 1)

        return res