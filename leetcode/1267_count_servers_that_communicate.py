class Solution:
    '''
        Approach
        - Time complexity: O(mn)
        - Space complexity: O(m+n)
    '''
    def count_servers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = { i:0 for i in range(m) }
        cols = { i:0 for i in range(n) }
        count = 0

        # count number of servers in each row and col
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                    count += 1
        
        # iterate again, now check isolated servers
        for i in range(m):
            for j in range(n):
                # find unconnected servers and decrement count
                if rows[i] == 1 and cols[j] == 1 and grid[i][j] == 1:
                    count -= 1

        return count


if __name__ == "__main__":
    s = Solution()

    print(s.count_servers([[1,0],[0,1]]))
    print(s.count_servers([[1,0],[1,1]]))
    print(s.count_servers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))