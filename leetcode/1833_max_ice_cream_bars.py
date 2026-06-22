from typing import List
from template.sorters import Sorters
import heapq

class Solution:
    # Using merge sort
    def maxIceCream_mergeSort(self, costs: List[int], coins: int) -> int:
        Sorters.mergeSort(costs)
        print(costs)
        
        ice_cream = 0
        for cost in costs:
            if cost <= coins:
                ice_cream += 1
                coins -= cost
            else:
                break
        return ice_cream

    # Using min heap
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        
        ice_creams = 0
        while costs and costs[0] <= coins:
            coins -= heapq.heappop(costs)
            ice_creams += 1
        return ice_creams
        
    

if __name__ == "__main__":
    s = Solution()
    
    print(s.maxIceCream([1,3,2,4,1], 7))
    print(s.maxIceCream([10,6,8,7,7,8], 5))
    print(s.maxIceCream([1,6,3,1,2,5], 20))
    print(s.maxIceCream([7,3,3,6,6,6,10,5,9,2], 56))