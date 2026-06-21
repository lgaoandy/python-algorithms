from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        self.mergeSort(costs)
        print(costs)
        
        ice_cream = 0
        for cost in costs:
            if cost <= coins:
                ice_cream += 1
                coins -= cost
            else:
                break
        return ice_cream
    
    
    def mergeSort(self, arr: List[int]) -> None:
        n = len(arr)
        
        if n > 1:
            left_arr = arr[:n // 2]
            right_arr = arr[n // 2:]
            
            self.mergeSort(left_arr)
            self.mergeSort(right_arr)
            
            i = j = k = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1
                
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
                
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1
                    


if __name__ == "__main__":
    s = Solution()
    
    print(s.maxIceCream([1,3,2,4,1], 7))
    print(s.maxIceCream([10,6,8,7,7,8], 5))
    print(s.maxIceCream([1,6,3,1,2,5], 20))
    print(s.maxIceCream([7,3,3,6,6,6,10,5,9,2], 56))