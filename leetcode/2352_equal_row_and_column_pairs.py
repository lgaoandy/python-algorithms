from collections import Counter

class Solution:
    '''
        pseudo-code
        - brute force method 
        - for every row, check every column, checking cell no 1 to n
    '''
    def equal_pairs_brute_force(self, grid: list[list[int]]) -> int:
        size = len(grid)
        pairs = 0

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    if grid[i][k] != grid[k][j]:
                        break
                    elif k == size - 1:   
                        pairs += 1
        return pairs
    
    '''
        analysis
        - time complexity: O(n^3) is too high!
        - space complexity: O(1)
    '''
    def equal_pairs_optimized(self, grid: list[list[int]]) -> int:
        count1 = Counter(tuple(row) for row in grid)
        count2 = Counter(tuple(col) for col in zip(*grid))
        return sum(count1[i] * count2[i] for i in count1.keys() if i in count2)
    
if __name__ == "__main__":
    test = Solution()
    # print(test.equal_pairs_brute_force([[3,2,1],[1,7,6],[2,7,7]]))
    # print(test.equal_pairs_brute_force([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
    print(test.equal_pairs_optimized([[3,2,1],[1,7,6],[2,7,7]]))
    print(test.equal_pairs_optimized([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))

    # What I learned
    # - given a problem, utilizing native data structures of the language is important
    # - tuples is ordered and unchangeable
    # - tuples can be used in dictionary