from typing import List

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
        
        rheight = {}
        for a, b in restrictions:
            rheight[a] = b
        
        pass


if __name__ == "__main__":
    s = Solution()
    
    r1 = [[2,1], [4,1]]
    print(s.maxBuilding(5, r1)) # ans: 2
    
    r2 = []
    print(s.maxBuilding(6, r2)) # ans: 5
    
    r3 = [[5,3], [2,5], [7,4], [10,3]]
    print(s.maxBuilding(10, r3)) # ans: 5