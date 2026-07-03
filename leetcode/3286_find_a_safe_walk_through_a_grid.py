from collections import deque
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
        - Greedy approach: try to find the exit in the least resistance path possible
        - Track of grid spots that have been visited to avoid repeated
        - Track of grid spots priority

        Analysis
        - time complexity: 
        - space complexity: 
    '''
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        queue = deque([(0,0,health)]) # starting point
        low_priority = set()
        
        while queue:
            i, j, hp = queue.popleft()
            visited.add((i,j))
            
            if grid[i][j] == 1:
                hp -= 1
            
            if (i, j) == (m-1, n-1):
                return hp > 0
            
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in visited:
                    if grid[ii][jj] == 1:
                        low_priority.add((ii,jj,hp))
                    else:
                        queue.append((ii,jj,hp))
            
            if not queue:
                queue.extend(low_priority)


if __name__ == "__main__":
    s = Solution()
    
    grid1 = [
        [0,1,0,0,0],
        [0,1,0,1,0],
        [0,0,0,1,0]
    ]
    print(s.findSafeWalk(grid1, 1)) # ans: true
    
    grid2 = [
        [0,1,1,0,0,0],
        [1,0,1,0,0,0],
        [0,1,1,1,0,1],
        [0,0,1,0,1,0]
    ]
    print(s.findSafeWalk(grid2, 3)) # ans: false
    
    grid3 = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    print(s.findSafeWalk(grid3, 5)) # ans: true
    
    grid4 = [
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,0],
        [1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,1,1],
        [1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,0,1,0,1,1,1],
        [1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0],
        [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0],
        [1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
        [1,1,1,0,1,1,0,1,1,0,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1],
        [0,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1],
        [1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1],
        [1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1],
        [1,1,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,1],
        [1,0,0,1,1,1,1,0,0,1,0,1,0,0,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1],
        [1,1,0,1,0,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
        [1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1],
        [1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1],
        [1,1,0,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,0],
        [0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1]
    ]
    print(s.findSafeWalk(grid4, 33)) # ans: true
