from collections import deque

class Solution:
    '''
        Intuition
        - Every land tile adjacent to a water tile is always a 1
        - We want to maximize peak - so every land tile adjacent to another land tile will seek to maximize peak

        BFS Approach
        - Define a grid the same size as isWater, then iterate isWater, adding all water tiles to a queue
        - Using a queue, find adjacent unvisited tiles and add to queue
    '''
    def highest_peak(self, isWater: list[list[int]]) -> list[list[int]]:
        ROWS = len(isWater)
        COLS = len(isWater[0])
        grid = [[-1] * COLS for _ in range(ROWS)]
        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if isWater[i][j]:
                    queue.append((i, j))
                    grid[i][j] = 0

        while queue:
            i, j = queue.popleft()
            
            for ii, jj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= ii < ROWS and 0 <= jj < COLS and grid[ii][jj] == -1:
                    queue.append((ii, jj))
                    grid[ii][jj] = grid[i][j] + 1
        return grid


if __name__ == "__main__":
    s = Solution()
    print(s.highest_peak([[0,1],[0,0]]))
    print(s.highest_peak([[0,0,1],[1,0,0],[0,0,0]]))
    print(s.highest_peak(
        [[0,0,0,0,0,0,1,0],
         [0,1,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,1,0],
         [0,0,1,0,0,0,0,0]]
    ))