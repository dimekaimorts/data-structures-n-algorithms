
"""
URL problem:     https://leetcode.com/problems/merge-intervals/
Related topics:  | Array | Sorting |
Idea: 
-------------------------------------------------------------------
Idea: 
1. Ordenar los intervalos
2. Agregar el primer intervalo al arreglo de solucion
3. Toma el último valor de la lista de soluciones, como el nuevo intervalo A.
4. Obtenemos Astar, Aend, Bstart y Bend
5. Verificar si Aend >= Bstart
    a. Si no, metemos ese intervalo a la solucion
    b. Si si, actualizamos el valor de fin de intervalo
6. Repetimos desde el paso 3
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if (len(intervals) <= 1):
            return intervals

        intervals.sort()
        solution:List[List[int]] = list()

        solution.append(intervals[0])

        for interval in intervals:
            Astart, Aend = solution[-1]
            Bstart, Bend = interval

            if (Aend >= Bstart):
                solution[-1][1] = max(Aend, Bend)
            else:
                solution.append(interval)

        return solution

