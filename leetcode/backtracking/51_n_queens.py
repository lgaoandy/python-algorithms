class Solution:
    '''
        Backtrack Approach
        - No queens can ever occupy the same row, column, descending diagonal and ascending diagonal
        - Use a 2D matrix board[i][j], each row is represented by board[i], and each grid is presented by board[i][j]
            - Use backtracking, to never have a single row with more than one queen
            - Use a set named columns to track which columns are available
            - Use 2 arrays, ascending and descending, to track ascending and descending diagonal occupied
    '''
    def n_queens(self, n: int) -> list[list[str]]:
        end = n - 1
        res = []

        board = [["."] * n for _ in range(n)]
        columns = set(range(n))
        ascending = []
        descending = []

        def backtrack(x):
            # base case 
            if x == n:
                res.append(["".join(row) for row in board.copy()])
                return

            for y in range(n):
                if y in columns:
                    # calculate diagonals
                    des = x - y
                    asc = end - x - y

                    if des not in descending and asc not in ascending:
                        board[x][y] = "Q"
                        descending.append(des)
                        ascending.append(asc)
                        columns.remove(y)

                        backtrack(x + 1)

                        columns.add(y)
                        ascending.pop()
                        descending.pop()
                        board[x][y] = "."

        backtrack(0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.n_queens(4))
    print(s.n_queens(1))