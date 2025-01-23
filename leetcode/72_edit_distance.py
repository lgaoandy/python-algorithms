class Solution:
    '''
        Intuition
        -

        Approach
        - 
    '''
    def min_distance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Create a 2D table to store intermediate results
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill up the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The length of LCS is stored in the bottom-right corner
        return max(m, n) - dp[m][n]
    

if __name__ == "__main__":
    s = Solution()
    
    print(s.min_distance("horse", "ros"))
    print(s.min_distance("intention", "execution"))