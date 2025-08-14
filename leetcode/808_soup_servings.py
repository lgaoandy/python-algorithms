from math import ceil

class Solution:
    # Brute Force Solution
    def soupServings1(self, n: int) -> float:
        operations = [(100, 0), (75, 25), (50, 50), (25, 75)]

        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1
            elif b <= 0:
                return 0
            else:
                return sum(dp(a - da, b - db) for da, db in operations) / len(operations)
        return dp(n, n)


    # Optimized - Solved by Editorial
    def soupServings(self, n: int) -> float:
        # deduce mL into servings of 25 mL
        m = ceil(n / 25)

        # setup dp as 2d array
        dp = {}

        # helper function for calculating new dp
        def calculate_dp(i, j):
            return (
                dp[max(0, i - 4)][j] +
                dp[max(0, i - 3)][j - 1] +
                dp[max(0, i - 2)][max(0, j - 2)] +
                dp[i - 1][max(0, j - 3)]
            ) / 4
        
        # if both a = 0, b = 0, probability = 0.5
        dp[0] = {0: 0.5}

        # iterate possible values of dp
        for k in range(1, m + 1):

            # setup base probability of a or b emptying first
            dp[0][k] = 1
            dp[k] = {0: 0}

            # calculate probability of in-between values
            for j in range(1, k + 1):
                dp[j][k] = calculate_dp(j, k)
                dp[k][j] = calculate_dp(k, j)
            
            # check if dp[k][k] has approached 1, if so, return 1
            if dp[k][k] > 1 - 1e-5:
                return 1

        # return actual probability
        return dp[m][m]


if __name__ == "__main__":
    s = Solution()
    print(s.soupServings(50))
    print(s.soupServings(100))
    print(s.soupServings(200))
    print(s.soupServings(300))