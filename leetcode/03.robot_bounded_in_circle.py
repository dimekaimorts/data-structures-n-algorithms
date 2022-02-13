
"""
URL problem:     https://leetcode.com/problems/robot-bounded-in-circle/
Related topics:  | Math | String | Simulation |
Idea: 
-------------------------------------------------------------------
- Encontrar aquellas caracteristicas cuando ocurre un ciclo/loop.
1. Cuando despues de recorrer la cadena, vuelve al inicio (0,0), va a haber un ciclo
2. Si cambia de direccion, puede haber un ciclo.
3. Si el punto 1 y 2 se cumple, va a haber un ciclo
Todo nace de girar en el propio eje, hacia la izquierda o derecha, 90 grados
    <-^ 
    | |
    v->

"""

from typing import List
from unittest import TestCase

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        x:int = 0
        y:int = 0
        direction:int = 0   # 0:Norte | 1:West | 2:South | 3:East |
        
        directions:List[int] = [
            (0, 1),  # North
            (-1, 0),  # West
            (0, -1),  # South
            (1, 0)   # East
        ]
        
        for instruction in instructions:
            if instruction == "G":
                x = x + directions[direction][0]
                y = y + directions[direction][1]
            
            elif instruction == "L":
                direction = (direction + 1) % len(directions)
            
            elif instruction == "R":
                direction = 3 if direction == 0 else direction - 1
            
        
        return (direction != 0) or (x == 0 and y == 0)

class TryTesting(TestCase):
    
    def setUp(self):
        solution = Solution()

    def test_always_passes(self):
        self.assertTrue(solution.isRobotBounded("GGLLGG"))
        self.assertTrue(solution.isRobotBounded("GL"))
        self.assertTrue(solution.isRobotBounded("GRGLGRGRGGRGG"))
        self.assertTrue(solution.isRobotBounded("GR"))

    def test_always_fails(self):
        self.assertTrue("GG")
        self.assertTrue("GGLR")
        self.assertTrue("GGLRG")


if __name__ == "__main__":
    solution = Solution()
    is_cycle = solution.isRobotBounded("GGLLGG")
    