from collections import deque
import math

class Solution:
    '''
        BFS Greedy Approach
        - Use an object (i, j, steps), where steps = number of changes to make to achieve current position
        - Use a double-sided queue, putting all of greedy approach to the left and the other possibilites to the right
    '''
    def min_cost(self, grid: list[list[int]]) -> int:
        w = len(grid)
        h = len(grid[0])
        
        costs = {}
        for i in range(w):
            for j in range(h):
                costs[(i, j)] = math.inf
                
        queue = deque([(0,0,0)])
        while queue:
            x, y, steps = queue.popleft()
            
            if steps < costs[(x,y)]:
                costs[(x, y)] = steps
                for dx, dy, direction in [(0,1,1), (0,-1,2), (1,0,3),(-1,0,4)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        if direction != grid[x][y] and costs[(nx, ny)] > steps + 1:
                            queue.append((nx,ny,steps+1))
                        elif costs[(nx, ny)] > steps:
                            queue.appendleft((nx,ny,steps))
        return costs[(w - 1, h - 1)]


if __name__ == "__main__":
    s = Solution()
    
    print(s.min_cost(
        [[1,1,1,1],
         [2,2,2,2],
         [1,1,1,1],
         [2,2,2,2]])
    )
    
    print(s.min_cost(
        [[1,1,3],
         [3,2,2],
         [1,1,4]]
    ))
    
    print(s.min_cost(
        [[1,2],
         [4,3]]
    ))