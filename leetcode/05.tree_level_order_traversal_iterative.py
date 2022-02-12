
"""
URL problem:     https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
Related topics:  | Tree | DFS | BFS | Binary Tree | Recursion |
Idea: 
-------------------------------------------------------------------
La idea es considerar cada subarbol como un arbol unico, y usar una
cola para ir tomando cada nodo del arbol. Tener el control con una
variable para saber el nivel en el que estamos, y cada vez que cambiemos
de nivel, agregar el valor del nodo en el nivel actual en una lista.
Habra N listas con respecto al # de niveles, y cada lista va albergar
los M valores de los nodos asociados.
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
        
        queue= [root]
        result = []

        while queue:
            nodes_values = []
            nodes_by_level = queue.__len__()
            
            while nodes_by_level > 0:
                current_node = queue.pop(0)
                
                if current_node.left:
                    queue.append(current_node.left)
                
                if current_node.right:
                    queue.append(current_node.right)

                nodes_values.append(current_node.val)
                nodes_by_level -= 1
            
            result.append(nodes_values)
        
        return result
