from typing import List

class Solution:
    '''
        Constriants:
        - m == grid.length, n == grid[i].length
        - 1 <= m, n <= 50
        - 2 <= m * n                    (m and n cannot be zero)
        - 1 <= health <= m + n          (don't need to check obvious answers)
        - grid[i][j] is either 0 or 1   (cannot loss 1 heath per grid)

        Thoughts
        - 2D dp solution: c
            - Create a m x n grid named safest_path
            - Start with the top row, iterate columns then rows
        - During iteration:
            - Check the immediate top and left grid if applicable and take the highest number as max_health
            - Check if current cell is a hazard (1) OR safe (0). If a hazard, reduce the health count by 1
            - Print the max_health into our grid
        - The cells the safest_path represents the most health you can have reaching that particular grid
        - Complete the iteration and check if the lower-right corner is >= 1, if so, true, else false

        Analysis
        - time complexity: O(n)
        - space complexity: O(1)
    '''
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        max_hp = [[health] * n] * m
        
        # Iterate first row
        for j in range(1, n):
            max_hp[0][j] = max_hp[0][j-1] # health carries over from the left
            if grid[0][j] == 1: 
                max_hp[0][j] -= 1
        
        # Iterate first column
        for i in range(1, m):
            max_hp[i][0] = max_hp[i-1][0] # health carries over from the top
            if grid[i][0] == 1:
                max_hp[i][0] -= 1
        
        # Iterate rest of grid
        for i in range(1, m):
            for j in range(1, n):
                max_hp[i][j] = max(max_hp[i-1][j], max_hp[i][j-1])
                if grid[i][j] == 1:
                    max_hp[i][j] -= 1
        
        return max_hp[m-1][n-1] >= 1


if __name__ == "__main__":
    s = Solution()
    
    grid1 = [
        [0,1,0,0,0],
        [0,1,0,1,0],
        [0,0,0,1,0]
    ]
    print(s.findSafeWalk(grid1, 1))
    
    grid2 = [
        [0,1,1,0,0,0],
        [1,0,1,0,0,0],
        [0,1,1,1,0,1],
        [0,0,1,0,1,0]
    ]
    print(s.findSafeWalk(grid2, 3))
    
    grid3 = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    print(s.findSafeWalk(grid3, 5))