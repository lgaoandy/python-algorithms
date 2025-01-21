class Solution:
    '''
        Intuition
        - Grid size being 2 x n greatly simplifies the problem
        - Because robots can only move right or down, there is only one instance where it travels down and this is a crucial tile
            - Given the exact index where it traverses down, the rest of its path is calculated (right)
            - The path of robot 1 would essentially be a line to divide the grid by 2 parts
            - The only remaining path would for robot 2 would one of those parts
        - Thus, what we ultimately are looking for is the find the minimum sum between the two parts created by robot 1's path

        Dynamic Programming Approach
        - Iterate from left to right, sum the values of the bottom leftmost area up to but not including the current index
        - Iterate from right to left, sum the vlaues of the upper rightmost area up to but not including the current index
            - This time, simultaneously evaluating the left and right sum, take its max and find the minimum of each index
    '''
    def grid_game(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        l_sum = [0] * n
        r_sum = [0] * n

        for i in range(1, n):
            l_sum[i] = l_sum[i-1] + grid[1][i-1]

        min_points = l_sum[-1] # initialize min_points as the last point in l_sum, where r_sum will always be zero
        for i in range(n-2, -1, -1):
            r_sum[i] = r_sum[i+1] + grid[0][i+1]
            max_sum = max(l_sum[i], r_sum[i]) # robot 2 will always choose the best path
            min_points = min(min_points, max_sum) # robot 1 wants to minimize the points robot 2 can get
        return min_points


if __name__ == "__main__":
    s = Solution()

    print(s.grid_game([[2,5,4],[1,5,1]]))
    print(s.grid_game([[3,3,1],[8,5,2]]))
    print(s.grid_game([[1,3,1,15],[1,3,3,1]]))