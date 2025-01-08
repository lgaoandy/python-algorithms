from collections import deque

class Solution:
    '''
        constriants:
        - 1 <= m, n <= 10
        - grid[i][j] is 0, 1, or 2

        comments/questions for interviewer
        - N/A

        pseudo-code
        - loop through grids, identifying oranges and rotting oranges
        - run bfs using a queue starting from rotting oranges, until there are no items in queue left
        - eliminate oranges in the process
        - check if oranges is empty in the end, return minutes

        analysis
        - time complexity: O(nm)
        - space complexity: O()
    '''
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        oranges = set()
        rotten = []

        # view every cell once, tracking oranges and rotten oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    oranges.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j, 0))

        # in a queue, rot adjacent oranges if possible
        minutes = 0
        queue = deque(rotten)
        while queue:
            i, j, time = queue.pop()
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]: # check adjacent squares
                ii, jj = i + x, j + y # calculate adjacent positions
                if 0 <= ii < rows and 0 <= jj < cols and (ii, jj) in oranges:
                    queue.appendleft((ii, jj, time + 1))
                    oranges.remove((ii, jj))
                    minutes = max(minutes, time + 1)

        # if there are oranges left, those are not adjacent to oranges that can be rotten
        return minutes if len(oranges) == 0 else -1
    

if __name__ == "__main__":
    s = Solution()

    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(s.orangesRotting([[0,2]]))
    print(s.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))

