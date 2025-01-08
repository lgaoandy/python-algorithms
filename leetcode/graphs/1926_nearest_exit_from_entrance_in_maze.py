from collections import deque

class Solution:
    '''
        constriants:
        - 1 <= rows, columns <= 100
        - "." and "+" are the only possible values in a maze coordinate
        - entrance coordinates always inside the maze and will always be on an empty cell

        comments/questions for interviewer
        - N/A

        pseudo-code
        - 1) identify the size of the maze
        - 2) loop maze, creating an adjacency list for spaces and track exits, if there are no exits, return -1
        - 3) use a bfs search algorithm to find the closest distance to exit the maze 

        analysis
        - time complexity: O(spaces in maze)
        - space complexity: O(spaces in maze)
    '''
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        m = rows - 1
        n = cols - 1
        spaces = { i:[] for i in range(rows) }
        exits = []

        # check borders for exits
        for i in range(rows):
            for j in range(cols):
                if maze[i][j] == "." and [i, j] != entrance:
                    spaces[i].append(j)
                    if i == 0 or j == 0 or i == m or j == n:
                        exits.append([i, j])

        # if there are no exits
        if len(exits) == 0:
            return -1
        
        # find closest exit if applicable
        steps = 1
        tiles = exits.copy()
        next_tiles = []

        while True:
            while len(tiles) > 0:
                [i, j] = tiles.pop()

                # make adjacent tiles
                adjacent = []
                adjacent.append([i-1, j]) # move left
                adjacent.append([i, j-1]) # move top
                adjacent.append([i+1, j]) # move right
                adjacent.append([i, j+1]) # move bottom

                for x, y in adjacent:
                    if [x, y] == entrance: # if tile is entrance, return steps
                        return steps
                    if x not in spaces.keys(): # if tile is out of bound, skip
                        continue
                    if y not in spaces[x]: # if tile is not an unexplored space, skip
                        continue

                    # otherwise, it is an valid space, add to queue then remove from spaces
                    next_tiles.append([x, y])
                    spaces[x].remove(y)
            
            # when tiles is empty, set next tiles to tiles, if also empty returns -1
            if len(next_tiles) == 0:
                return -1
            tiles = next_tiles.copy()
            next_tiles = []
            steps += 1


    '''
        improvements
        - in previous implementation, every cell in the maze was checked, this may be unnecessary
        - instead of iterating through the entire maze, we only need to iterate through the borders first
        - then using BFS to find the solution, checking only necessary tiles on the way
        - instead of using a spaces dictionary, we can store tuples inside of a set to quickly check if a tile has been visited
    '''
    def nearestExitOptimized(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        m = rows - 1
        n = cols - 1
        exits = set()

        # search through borders for exits
        for i in range(rows):
            if maze[i][0] == ".":
                exits.add((i, 0))
            if maze[i][n] == ".":
                exits.add((i, n))

        for j in range(1, n):
            if maze[0][j] == ".":
                exits.add((0, j))
            if maze[m][j] == ".":
                exits.add((m, j))
        
        # if entrance is on border, remove it
        if (entrance[0], entrance[1]) in exits:
            exits.remove((entrance[0], entrance[1]))

        # find nearest exit
        steps = 1
        visited = set()
        tiles = exits.copy()
        next_tiles = set()

        while True:
            while len(tiles) > 0:
                (i, j) = tiles.pop()

                adjacent = []
                if i > 0: 
                    adjacent.append((i-1,j))
                if i < m:
                    adjacent.append((i+1,j))
                if j > 0:
                    adjacent.append((i,j-1))
                if j < n:
                    adjacent.append((i,j+1))
                for (x, y) in adjacent:
                    if [x, y] == entrance:
                        return steps
                    elif maze[x][y] == "." and (x, y) not in visited:
                        next_tiles.add((x, y))
                        visited.add((x, y))
        
            if len(next_tiles) == 0:
                return -1
            tiles = next_tiles.copy()
            next_tiles = set()
            steps += 1
    
    
    '''
        improvements:
        - uses a single loop to queue, storing the distance in each item
        - starts from entrance so there's no need for checking exits
        - maze to graph conversion seems redundant
    '''
    def nearestExitFromEntrance(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        i, j = entrance
        
        # Convert maze to a graph
        graph = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if maze[r][c] == '.':
                    graph[r][c] = 1
        print(graph)
        
        # BFS
        queue = deque([(i, j, 0)])
        visited = {(i, j)}
        
        while queue:
            r, c, dist = queue.popleft()
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                
                if (0 <= nr < rows and 0 <= nc < cols and 
                    graph[nr][nc] == 1 and (nr, nc) not in visited):
                    if (nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1):
                        return dist + 1
                    
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
                    
                    # Remove the cell from the graph
                    graph[nr][nc] = 0
        
        return -1

if __name__ == "__main__":
    s = Solution()
    
    # expected 1
    print(s.nearestExitOptimized(
        [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],
        [1,2]
    ))
    
    # expected 2
    print(s.nearestExitOptimized(
        [["+","+","+"],[".",".","."],["+","+","+"]],
        [1,0]
    ))

    # expected -1
    print(s.nearestExitOptimized(
        [[".","+"]],
        [0,0]
    ))

    # expected 1
    print(s.nearestExitOptimized(
        [[".","."]],
        [0,1]
    ))