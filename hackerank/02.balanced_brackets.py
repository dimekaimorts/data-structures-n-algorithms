
"""
URL problem:     https://www.hackerrank.com/challenges/balanced-brackets/problem
Related topics:  | Stack | Simulation |
Idea: 
-------------------------------------------------------------------
Voy a recorrer cada uno de los caracteres
- Si es un corchete de apertura, despues puede venir otro corchete de apertura o uno de cierre
    - Meto a la pila el caracter actual
- Si es un corchete de cierre
    - Verifico si la pila esta vacia
        - Si esta vacia, obtengo el valor del tope de la pila y hago un pop()
        - Verifico si el valor actual de cierre, corresponde con el analogo
          correspondiente al valor de apertura del tope de la pila, es decir

          Si viene un "}", el elemento hasta el tope de la pila debe ser "{"
          Si viene un "]", el elemento hasta el tope de la pila debe ser "["
          Si viene un ")", el elemento hasta el tope de la pila debe ser "("

        - Si no es asi, entonces regreso un NO
    - Si la pila esta vacia, quiere decir que hay corchetes de cierre que de apertutra
      entonces regreso NO
- Finalmente, si la pila esta vacia, regreso "YES", de otro modo, "NO"
"""

def isBalanced(s:str) -> bool:
    stack = []
    brackets = {
        "{" : "}",
        "[" : "]",
        "(" : ")"
    }
    opening = [bracket_open for bracket_open in brackets.keys()]
    closing = [bracket_close for bracket_close in brackets.values()]
    
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if stack:
                top = stack.pop()
                if brackets[top] != char:
                    return "NO"
            else:
                return "NO"
    
    return "YES" if not stack else "NO"


if __name__ == "__main__":
    tests = [
        "{[()]}",
        "{[(])}",
        "{{[[(())]]}}", 
        "((())",
        "{()[]}",
        "(())))))"
    ]

    for test in tests:
        print("{} is balanced? {}".format(test, isBalanced(test)))