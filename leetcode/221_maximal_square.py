class Solution:
    '''
        Solution:
        -   3D dynamic programming: make a grid of the same size as the matrix
        -   Going bottom up, each grid must check the grid to the right, under and bottom-right diagonal of itself
            - If the grid is an edge, simply assign as its matrix value (1 as 1, 0 as 0)
        - Conceptually, this solution grid represents the largest square size that can exist given the current grid as the topmost leftmost corner of the area
    '''
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        # get length & width of matrix
        m, n = len(matrix), len(matrix[0])
        
        # generate dp grid
        dp = [[0] * n for _ in range(m)]
        
        # iterate bottom up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "0": # check if matrix is zero:
                    continue
                if i >= m - 1 or j >= n - 1: # check if grid is an non-zero edge:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
                    
        # get largest square
        max_square = 0
        for i in range(m):
            for j in range(n):
                max_square = max(max_square, dp[i][j])
        
        # calculate power
        return pow(max_square, 2)
        
        
        


if __name__ == "__main__":
    s = Solution()
    
    # expected: 4
    print(s.maximalSquare([
        ["0","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]))
    
    # expected: 1
    print(s.maximalSquare([
        ["0","1"],
        ["1","0"]
    ]))
    
    # expected: 0
    print(s.maximalSquare([
        ["0"]
    ]))