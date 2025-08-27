class Solution:
    '''
        Histogram Solution:
    '''
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        sums = [[0] * n for _ in range(m)]
        
        # Populate first row
        for j in range(m):
            sums[0][j] = int(matrix[0][j])
        
        for i in range(1, m):
            for j in range(n):
                if sums[i-1][j] > 0 or 
                sums[i][j] = int(matrix[i][j]) + sums[i-1][j]
                
            
        
        
                
    
if __name__ == "__main__":
    s = Solution()

    # Expected: 6
    print(s.maximalRectangle([
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","1","0","1","0"]
    ]))