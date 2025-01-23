class Solution:
    '''
        2D DP Approach
        - Build a 2D matrix where dp[i][j] represents the minimum number of operations required to transform substring[0:i-1] into substring[0:j-1]
        
        - If two letters are the same, we can effectively say:
            dp[i][j] = dp[i-1][j-1]

        - Otherwise we must perform the following operation:
            dp[i][j] = dp[i-1][j-1] for replacement
            dp[i][j] = dp[i-1][j] for deletion
            dp[i][j] = dp[i][j-1] for insertion

        - Since we don't know what is the optimal operation, we take the min of the 3 operations then add 1 (for using operation)
            Thus dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        - Base case: dp[0][0] is a direct comparison of the first letter of word1 and word2
            - thus dp[0][0] = 0 if word1[0] == word2[0] else 1

        - Base case: consider evaluating the first row: dp[0][j], let's consider some examples:
            - Dry run 1: "a" compared to "ace"
                dp[0][0] = 0, since "ace"[0] = "a"
                dp[0][1] = 1, because we need to insert "c"
                dp[0][2] = 2, becase we need to insert "e"

            - Dry run 2: "t" compared to "rrrt"
                dp[0][0] = 1, replace "t" to "r"
                dp[0][1] = 2, insert "r"
                dp[0][2] = 3, insert "r"
                dp[0][3] = 3, this "t" matches our letter, so we'd only need to do 3 insertions

            - Therefore, we can run an algorithm to populate the base case for any letter against a word
                - dp[0][j] = dp[0][j-1] only if letter == word[j] and this is the first occurrence of it
                - else dp[0][j] = dp[0][j-1] + 1
    '''
    def min_distance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Populate base case 
        for i in range(1, m+1):
            dp[i][0] = i

        for j in range(1, n+1):
            dp[0][j] = j

        # Run dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[m][n]
    

if __name__ == "__main__":
    s = Solution()
    
    print(s.min_distance("horse", "ros"))
    print(s.min_distance("intention", "execution"))
    print(s.min_distance("sea", "eat"))
    print(s.min_distance("", ""))
    print(s.min_distance("", "a"))