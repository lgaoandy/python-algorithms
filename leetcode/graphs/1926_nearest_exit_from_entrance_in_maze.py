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
            

if __name__ == "__main__":
    s = Solution()
    
    # expected 1
    print(s.nearestExit(
        [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],
        [1,2]
    ))
    
    # expected 2
    print(s.nearestExit(
        [["+","+","+"],[".",".","."],["+","+","+"]],
        [1,0]
    ))

    # expected -1
    print(s.nearestExit(
        [[".","+"]],
        [0,0]
    ))