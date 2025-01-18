class Solution:
    '''
        Brute Force Backtrack Approach
        - Store a rows, columns and quad - arrays representing unavailable nums for the cell
        - Try a number, backtrack if it is not possible
    '''
    def solve_sudoku(self, board: list[list[str]]) -> None:
        def quadrant(i, j):
            return ((i // 3) * 3) + (j // 3)

        def coordinates(tile):
            i = tile // 9
            j = tile % 9
            return (i, j)
        
        def next_tile(tile):
            while True:
                tile += 1
                if coordinates(tile) not in permanent:
                    return tile
            
        N = 9 
        END = N - 1
        rows = [set(str(i) for i in range(1, N+1)) for _ in range(N)]
        cols = [set(str(i) for i in range(1, N+1)) for _ in range(N)]
        quad = [set(str(i) for i in range(1, N+1)) for _ in range(N)]
        permanent = set()
        
        # populate rows, cols, quads
        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    permanent.add((i, j))
                    rows[i].remove(board[i][j])
                    cols[j].remove(board[i][j])
                    quad[quadrant(i,j)].remove(board[i][j])

        def backtrack(tile):
            # get coordinates of current tile
            i, j = coordinates(tile)

            # if at the end of suduko, solution is found
            if i > END or j > END:
                return True
            else:
                # find the numbers available matching from row, column and quadrant
                k = quadrant(i, j)
                remaining = list(rows[i].intersection(cols[j]).intersection(quad[k]))
                
                for num in remaining:
                    board[i][j] = num
                    rows[i].remove(num)
                    cols[j].remove(num)
                    quad[k].remove(num)
                    found = backtrack(next_tile(tile))

                    if found:
                        return True
                    
                    board[i][j] = "."
                    rows[i].add(num)
                    cols[j].add(num)
                    quad[k].add(num)
        backtrack(next_tile(-1))


def print_by_row(board):
    print()
    for i in range(9):
        print(board[i])


if __name__ == "__main__":
    s = Solution()

    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    s.solve_sudoku(board1)
    print_by_row(board1)

    board2 = [
        [".",".","9","7","4","8",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        [".","2",".","1",".","9",".",".","."],
        [".",".","7",".",".",".","2","4","."],
        [".","6","4",".","1",".","5","9","."],
        [".","9","8",".",".",".","3",".","."],
        [".",".",".","8",".","3",".","2","."],
        [".",".",".",".",".",".",".",".","6"],
        [".",".",".","2","7","5","9",".","."]
    ]

    s.solve_sudoku(board2)
    print_by_row(board2)

