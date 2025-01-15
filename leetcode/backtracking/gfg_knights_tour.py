import copy 

class Solution:
    '''
        Recursive Brute Force Appraoch
        - create a grid of size n
        - start at (0,0) as 1, then check all possible knight movements
        - recursively check all knight movement, backtracking when a movement is not possible
        - if a solution reaches the end, copy to results
    '''
    def knights_tour(self, n):
        # make board
        board = [[0 for _ in range(n)] for _ in range(n)]
        board[0][0] = 1
        max_steps = n * n

        def backtrack(board, current, steps):
            x, y = current
            if steps == max_steps:
                result.append(copy.deepcopy(board))

            for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    board[nx][ny] = steps + 1
                    backtrack(board, (nx, ny), steps + 1)
                    board[nx][ny] = 0

        result = []
        backtrack(board, (0, 0), 1)
        return result


if __name__ == "__main__":
    s = Solution()
    tours = s.knights_tour(5)

    for i in range(3):
        for row in range(5):
            for col in range(4):
                print(f"{tours[i][row][col]:2d}  ", end="")
            print(f"{tours[i][row][4]:2d}")
        print()