
"""
URL problem:     https://leetcode.com/problems/binary-tree-inorder-traversal/
Related topics:  | Tree | DFS | Binary Tree | Stack | Iterative |
Idea: 
-------------------------------------------------------------------
Idea: 
1. Creamos la pila
2. Inicializar el nodo raiz como el nodo actual (current).
3. Meter el nodo actual (current) a la pila (nodes)
4. Iterar mientras la pila tenga nodos
5. Iterar hasta llegar a un nodo hoja del subárbol izquierdo.
6. Obtenemos el tope de la pila
7. Lo agregamos al lista resultante (inorder)
8. Actualizamos el nodo actual, para recorrer el subárbol derecho
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


