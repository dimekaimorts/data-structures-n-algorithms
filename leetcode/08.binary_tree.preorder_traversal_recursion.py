
"""
URL problem:     https://leetcode.com/problems/binary-tree-preorder-traversal/
Related topics:  | Tree | DFS | Binary Tree | Stack | Iterative |
Idea: 
-------------------------------------------------------------------
Idea: 
1. Verificamos si la raiz actual es nula
2. Si no es nula, agregamos el valor del nodo raiz a la lista
3. Verificamos si el subárbol izquierdo es nulo
    a. Si no, hacemos la llamada recursiva para recorrer el subárbol izquierdo, considerando como raíz a ese nodo.
4. Verificamos si el subárbol derecho es nulo
    a. Si no, hacemos la llamada recursiva para recorrer el subárbol derecho, considerando como raíz a ese nodo.
5. Repetimos.
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder:List[int] = list()

        def dfs(root: Optional[TreeNode], preorder:List[int]) -> List[int]:
            if root:
                preorder.append(root.val)

                if root.left:
                    dfs(root.left, preorder)
                
                if root.right:
                    dfs(root.right, preorder)

            return preorder

        return dfs(root, preorder)

