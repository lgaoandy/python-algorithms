'''
    Naive Recursive Approach
    - Generate all possible permutations of [1,2,3,...,n] using backtracking
    - For each permutation, check if any two queens are places on the same diagonal
    - If a permutation is valid during diagonal check, add it to our result

    Time complexity: O(n! x n)
    Space complexity: O(n!)
'''
def generate_permutations(n: int):
    def backtrack(current: list[int], remaining: list[int]):
        # base case: if we've used all numbers, add current permutations to result
        if len(current) == n:
            result.append(current[:])

        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()
    
    result = []
    backtrack([], list(range(1, n+1)))
    return result


def valid_queen(permutation: list[int]) -> bool:
    n = len(permutation)
    descending = []
    ascending = []
    for i in range(n):
        des = i + 1 - permutation[i]
        asc = n - i - permutation[i]
        if des in descending or asc in ascending:
            return False
        descending.append(des)
        ascending.append(asc)
    return True


def n_queens_recursion(n: int) -> list[list[int]]:
    permutations = generate_permutations(n)

    results = []
    for permutation in permutations:
        if valid_queen(permutation):
            results.append(permutation)
    return results


'''
    Backtracking with Pruning Approach
    - Instead of generating all possible permutation, build solution incrementally
    - If a conflict is detected then we'll backtrack immediately, which avoids unnecessary computations

    Time complexity: O(n!)
    Space complexity: O(n)
'''
def n_queen_pruning(n: int) -> list[list[int]]:
    result = []

    def backtrack(current: list[int], remaining: list[int], descending: list[int], ascending: list[int]):
        m = len(current)

        # base case
        if m == n:
            result.append(current.copy())
        
        for i in range(len(remaining)):
            # compute current diagonal
            des = m + 1 - remaining[i]
            asc = n - m - remaining[i]

            # if diagonal is occupied by a previous queen, backtrack
            if des not in descending and asc not in ascending:
                # add queen and diagonal occupied
                descending.append(des)
                ascending.append(asc)
                current.append(remaining[i])

                # get the next column of permutations
                backtrack(current, remaining[:i] + remaining[i+1:], descending, ascending)

                # remove current and diagonal
                current.pop()
                descending.pop()
                ascending.pop()

    backtrack([], list(range(1, n+1)), [], [])
    return result


if __name__ == "__main__":
    print(n_queens_recursion(1))
    print(n_queens_recursion(2))
    print(n_queens_recursion(3))
    print(n_queens_recursion(4))
    print(n_queens_recursion(5))
    # print(n_queens_recursion(8))

    print(n_queen_pruning(1))
    print(n_queen_pruning(2))
    print(n_queen_pruning(3))
    print(n_queen_pruning(4))
    print(n_queen_pruning(5))
    # print(n_queen_pruning(8))