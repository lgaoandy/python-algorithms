class Solution:
    '''
        Intuition & Dynamic Programming Approach
        - We will create a grid, each tile represents a value of the number of possible paths it takes to reach the current position
        - Given the robot can only move down and right, the first row and column will always be 1
        - We can loop through the rest from 2nd row to last row, left to right, adding the nums from the top and left tile
        - Time complexity: O(nm)
        - Space complexity: O(nm)

        Optimizations:
        - Space complexity: O(n) if you alternative two rows to calculate paths (you only look at 2 rows at a time)
    '''
    def unique_paths(self, m: int, n: int) -> int:
        paths = [[1] * n for _ in range(m)] # initialize with values of 1

        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        print(paths)
        return paths[m-1][n-1]


if __name__ == "__main__":
    s = Solution()
    print(s.unique_paths(3,7))
    print(s.unique_paths(5,5))
    print(s.unique_paths(3,2))