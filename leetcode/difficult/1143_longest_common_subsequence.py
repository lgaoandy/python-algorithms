def print_grid(grid):
    # Check if the grid is empty
    if not grid or not grid[0]:
        print("Grid is empty")
        return

    # Get the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])

    # Print the header row
    print('    ', end='')  # Space for column numbers
    for col in range(cols):
        print(f'{col:2}', end=' ')  # Print column numbers aligned
    print()  # Move to the next line

    # Print separator line
    print('-' * (cols * 8 + 1))  # Adjust width as needed

    # Print each row
    for row_idx, row in enumerate(grid, start=1):  # Start counting from 1
        print(f'{row_idx:2}:', end=' ')  # Print row number aligned
        for cell in row:
            print(f'{cell:2}', end=' ')  # Print cell value aligned
        print()  # Move to the next line


class Solution:
    '''
        Dynamic Programming Approach
        - Loop through text1, listing the index of occurrence of each letter in a list 
        - Loop through text2, 
    '''
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # Create a 2D table to store intermediate results
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill up the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        print_grid(dp)
        # The length of LCS is stored in the bottom-right corner
        return dp[m][n]


if __name__ == "__main__":
    s = Solution()
    print(s.longest_common_subsequence("abcde", "ace"))
    print(s.longest_common_subsequence("abc", "ace"))
    print(s.longest_common_subsequence("abc", "def"))