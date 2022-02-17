
"""
URL problem:     https://www.hackerrank.com/challenges/find-the-running-median/problem?isFullScreen=true
Related topics:  | DFS | Tree | Trie | Prefix Tree |
Idea: 
===============================================================================
La idea es utilizar un Trie, o arbol de prefijos, para almacenar los contactos.
1. Cuando haya un operacion `add`, vamos a agregar un nodo por cada letra, 
   junto con un contador de sus nodos asociados
2. Cuando haya una operacion `find`, vamos a armar el recorrido usando una DFS.
   en el i-esimo arbol con el cual empieza la cadena parcial, y devolvemos el valor
   del ultimo nodo.
"""

import json
from typing import Dict, List, Optional

def contacts(queries:List[str]) -> Optional[List[int]]:
    result:List[int] = []
    contacts:Dict = dict()
    
    def add(name:str, contacts:Dict, idx:int) -> None:
        if len(name) == idx:
            return
        
        letter = name[idx]
        if letter in contacts:
            contacts[letter]["relations"] += 1
        else: 
            contacts[letter] = dict()
            contacts[letter]["relations"] = 1
        
        add(name, contacts[letter], idx+1)

    def find(partial:str, contacts:Dict, idx:int) -> int:
        num_contacts = 0
        if len(partial) == idx:
            return contacts["relations"]
        
        letter = partial[idx]
        if letter in contacts:
            num_contacts = find(partial, contacts[letter], idx+1)
        
        return num_contacts

    for query in queries:
        operation = query[0]

        if "add" == operation:
            name = query[1]
            add(name, contacts, 0)
        
        elif "find" == operation:
            partial = query[1]
            result.append(find(partial, contacts, 0))

    print(json.dumps(contacts, indent=4))
    print(result)

    return result


if __name__ == "__main__":
    queries = [['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']]
    contacts(queries)
