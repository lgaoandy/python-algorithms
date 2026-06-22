from typing import List
import heapq

class Solution:
    ''''
        Thoughts:
        - Estimate: best time complexity for this problem is O(n) - you need to go through n to ensure the restrictions are valid
        - Seems like a backtracking problem, as the solution can be summaried in the following
            - Outside of restrictions, we prioritize tall buildings as much as possible
            - The growth step is always 1

        Strategy:
        - Convert restrictions to dictionary
        - for loop range(n), always try increment by 1 until a 
    '''
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1
        
        heightr = {}
        for a, b in restrictions:
            heightr[a-1] = b
        
        height = [0] * n
        for i in range(1, n-1):
            print(i)
            if i in heightr:
                print(f"{i} in heightr")
                j = i - 1
                while height[j] > height[j+1]:
                    height[j] = height[j+1] - 1
                    j -= 1
                else:
                    height[i] = height[i-1]
            else:
                height[i] = height[i-1] + 1
        return height
        

if __name__ == "__main__":
    s = Solution()
    
    r1 = [[2,1], [4,1]]
    print(s.maxBuilding(5, r1)) # ans: 2
    
    r2 = []
    print(s.maxBuilding(6, r2)) # ans: 5
    
    r3 = [[5,3], [2,5], [7,4], [10,3]]
    print(s.maxBuilding(10, r3)) # ans: 5