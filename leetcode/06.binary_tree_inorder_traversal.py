
"""
URL problem:     https://leetcode.com/problems/binary-tree-inorder-traversal/
Related topics:  | Tree | DFS | Binary Tree | Stack |
Idea: 
-------------------------------------------------------------------
Idea: La idea es considerar cada subarbol como un arbol unico, y usar una
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder:List[int] = list()
        stack_nodes:List[Optional[TreeNode]] = list()

        current:Optional[TreeNode] = root

        while stack_nodes or current:
            while current:
                stack_nodes.append(current)
                current = current.left

            # Hemos llegado a una hoja, y la pila no esta vacia
            current = stack_nodes.pop()
            inorder.append(current.val)
            current = current.right

        return inorder


