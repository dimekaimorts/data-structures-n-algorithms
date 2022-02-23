
"""
URL problem:     https://www.hackerrank.com/challenges/swap-nodes-algo/problem?isFullScreen=true
Related topics:  | Tree | DFS | Binary Tree |
Idea: 
-------------------------------------------------------------------
Idea de solucion:
1. Crear el arbol binario a partir de los indices, inicializando el
   nodo raiz con el valor de 1.
2. Meter ese nodo raiz a una cola, para iterar y crear el arbol
3. Recorrer el arbol y realizar swap por cada multiplo del nivel dado (k)
   dentro de la lista queries.
   a. Verificar si no es un nodo hoja
    -> Si no, entonces vemos si el nivel es multiplo de k: level%k==0
        -> Si si, intercambiamos los valores de los nodos:
           node.left, node.right = node.right, node.left
   b. Realizamos el recorrido inorder (LoR) y repetimos.
"""


from typing import List
from collections import deque
import sys
sys.setrecursionlimit(10_000)

class Node:
    def __init__(self, value) -> None:
        self.left  = None
        self.right = None
        self.value = value

def swapNodes(indexes:List[List[int]], queries:List[int]) -> List[List]:
    
    def create_binary_tree(root:Node, indexes:List[List[int]]) -> Node:
        queue = deque([root])

        for left, right in indexes:
            current_node = queue.popleft()

            if left != -1:
                current_node.left = Node(left)
                queue.append(current_node.left)
            
            if right != -1:
                current_node.right = Node(right)
                queue.append(current_node.right)

        return root


    def swap(root:Node, level:int, k:int, inorder_traversal:List[int]) -> None:
        if root:
            if level % k == 0:
                root.left, root.right = root.right, root.left

            swap(root.left, level + 1, k, inorder_traversal)
            inorder_traversal.append(root.value)
            swap(root.right, level + 1, k, inorder_traversal)


    root = Node(1)
    root = create_binary_tree(root, indexes)

    result = []
    for k in queries:
        inorder_traversal = []
        swap(root, 1, k, inorder_traversal)
        result.append(inorder_traversal)
    
    return result


