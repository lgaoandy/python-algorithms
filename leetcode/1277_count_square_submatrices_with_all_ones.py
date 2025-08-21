class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        
        # DP: each grid represents the number of different squares it can obtain as the leftmost corner
        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if matrix[i][j] == 0:
                    continue
                elif i >= ROWS - 1 or j >= COLS - 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
        
        squares = 0
        # iterate through DP, counting all squares
        for i in range(ROWS):
            for j in range(COLS):
                squares += dp[i][j]
        return squares
        

if __name__ == "__main__":
    s = Solution()
    
    # Expected: 15
    print(s.countSquares([
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]))
    
    # Expected: 7
    print(s.countSquares([
        [1,0,1],
        [1,1,0],
        [1,1,0]
    ]))