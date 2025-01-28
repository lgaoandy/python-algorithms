class Solution:
    def find_max_fish(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def find_fish(i, j):
            if (i, j) in visited:
                return 0
            
            visited.add((i, j))
            count = grid[i][j]
            adjacent = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            for ii, jj in adjacent:
                if 0 <= ii < rows and 0 <= jj < cols and grid[i][j] != 0:
                    count += find_fish(ii, jj)
            return count
                    
        max_fish = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited:
                    if grid[i][j] != 0:
                        max_fish = max(find_fish(i, j), max_fish)
                    visited.add((i, j))
        return max_fish


if __name__ == "__main__":
    s = Solution()
    print(s.find_max_fish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))
    print(s.find_max_fish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]))