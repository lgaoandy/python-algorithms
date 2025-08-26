class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # setup rows and columns dp
        rows = [[0] * n for _ in range(m)]
        cols = [[0] * n for _ in range(m)]
        
        # iterate through matrix, populating rows
        for i in range(m):
            rows[i][n-1] = int(matrix[i][n-1])
            for j in range(n-2, -1, -1):
                if matrix[i][j] == "1":
                    rows[i][j] = rows[i][j+1] + 1
        
        # iterate through matrix, populating cols
        for j in range(n):
            cols[m-1][j] = int(matrix[m-1][j])
            for i in range(m-2, -1, -1): 
                if matrix[i][j] == "1":
                    cols[i][j] = 1 + cols[i+1][j]
        
        for i in range(m):
            print(rows[i])
            
        print()
        for i in range(m):
            print(cols[i])
        
        area = [[0] * n for _ in range(m)]
        # iterate through grid, calculating areas
        for i in range(m):
            for j in range(n):
                ii = rows[i][j]
                jj = cols[i][j]
                if ii <= 1 or jj <= 1:
                    area[i][j] = ii * jj
                else:
                    area1 = max()
                    
        
        print()
        for i in range(m):
            print(area[i])
                
    
if __name__ == "__main__":
    s = Solution()

    # Expected: 6
    print(s.maximalRectangle([
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","1","0","1","0"]
    ]))