
from heapq import heappush, heappop
from typing import List

"""
URL problem:     https://www.hackerrank.com/challenges/find-the-running-median/problem?isFullScreen=true
Related topics:  | MaxHeap | MinHeap | Heap |
Idea: 
===============================================================================
La idea es considerar dos heaps: maxHeap y un minHeap
- Regla 01 (R1) : Si es el primer elemento, va hacia el maxHeap
- Regla 02 (R2) : Si el i-esimo elemento es mayor a la raiz del maxHeap, va hacia el minHeap
- Regla 03 (R3) : Si la longitud de ambos heaps es igual, tomo el elemento de la raiz de cada heap y lo divido en 2
- Regla 04 (R4) : Si la longitud de maxHeap es mayor que la de minHeap, entonces tomo el elemento raiz de maxHeap
- Regla 05 (R5) : Si la longitud de minHeap es mayor que la de maxHeap
    a. Si la diferencia entre minHeap y maxHeap es mayor o igual a 2, agrego el elemento raiz del minHeap como elemento raiz del maxHeap
    b. Si no, entonces tomo el elemento raiz de minHeap

E.g.
    i=0 | n = 1 | maxHeap = [1] | minHeap = []  | medians = [1]          -> R1
    i=1 | n = 2 | maxHeap = [1] | minHeap = [2] | medians = [1, 1.5]     -> R2, R3
    i=2 | n = 3 | maxHeap = [1] | minHeap = [2, 3] | medians = [1, 1.5]  -> R2, R5b
    i=2 | n = 4 | maxHeap = [1] | minHeap = [2, 3, 4] | medians = [1, 1.5, 2]  -> R1, R5a
                | maxHeap = [2, 1] | minHeap = [3, 4] | medians = [1, 1.5, 2, 2.5]  -> R3
    
"""
def runningMedian(array:List[int]) -> List[float]:
    # Initialize variables
    min_heap:List[int] = []
    max_heap:List[int] = []
    medians:List[float] = [None]*len(array)

    def add_number(num:int, min_heap:List[int], max_heap:List[int]) -> None:
        # Signo `-` nos ayuda a convertir el minHeap a un maxHeap
        if not max_heap or num < -max_heap[0]:
            heappush(max_heap, -num)
        else:
            heappush(min_heap, num)


    def rebalance(min_heap:List[int], max_heap:List[int]) -> None:
        if len(min_heap) - len(max_heap) >= 2:
            root = heappop(min_heap)
            heappush(max_heap, -root)

        if len(max_heap) - len(min_heap) >= 2:
            root = heappop(max_heap)
            heappush(min_heap, -root)


    def get_median(min_heap:List[int], max_heap:List[int]) -> float:
        median = None
        if len(min_heap) == len(max_heap):
            median = (min_heap[0] - max_heap[0])/2
        elif len(min_heap) > len(max_heap):
            median = float(min_heap[0])
        else:
            median = float(-max_heap[0])
        
        return median

    for i, num in enumerate(array):
        # Insert the element according to the heap
        add_number(num, min_heap, max_heap)

        # Balancing heaps
        rebalance(min_heap, max_heap)

        # Find the median
        medians[i] = get_median(min_heap, max_heap)
    
    return medians


if __name__ == "__main__":
    array = [12, 4, 5, 3, 8, 7]
    medians = runningMedian(array)
    print(medians)
