
"""
URL problem:     https://leetcode.com/problems/two-sum/
Related topics:  | Array | Hash Table |
Idea: 
-------------------------------------------------------------------
La idea es encontrar un complemento para que satisfaga la condicion
Es decir, si el valor `target` = 9, entonces debemos encontrar el 
`complemento` dado por target-Ni, donde Ni, es el i-esimo elemento 
de la list de elementos.

    E.g.    nums = [2,7,11,15]
            target = 9

        Iteracion: 0
            Ni = 2
            complemento = 9 - 2 = 7   | Esta `7` en indices? No
            indices = {2:0}           | Agregamos `2` a indices
        
        Iteracion: 1
            Ni = 7
            complemento = 9 - 7 = 2   | Esta `2` en indices? Si
            indices = {2:0, 7:1}      | Hemos encontrado la solucion
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        answer = []
        for i,n in enumerate(nums):
            complement = target - n
            if complement in indices:
                answer.append(indices[complement])
                answer.append(i)
                break            
            indices[n] = i

        return answer

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9

    sol = Solution()
    i,j = sol.twoSum(nums, target)
    print(f"{i},{j}")
