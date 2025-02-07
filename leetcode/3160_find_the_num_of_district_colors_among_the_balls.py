class Solution:
    '''
        Intuition
        - Uncolor balls are ignores
        - Queries can repaint an already colored ball

        Approach
        - Use an array to represent balls
        - Use a dictionary to count the number of occurrences in each color
        - Use a count to determine the number of distinct colors
        - Iterate through queries to determine the following
    '''
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        n = len(queries)
        balls = [-1] * (limit + 1)
        colors = {}
        ans = [1] * n

        # populate first color
        balls[queries[0][0]] = queries[0][1]
        colors[queries[0][1]] = 1

        for i in range(1, n):
            x, y = queries[i] # extract no and color
            ans[i] = ans[i-1]

            if balls[x] == y: # if repainting the same color, skip
                continue

            if balls[x] != -1: # if overriding a different color
                colors[balls[x]] -= 1
                if colors[balls[x]] == 0:
                    ans[i] -= 1

            if y not in colors.keys(): # if color appears the first time, add color
                colors[y] = 0
            if colors[y] == 0:
                ans[i] += 1
            balls[x] = y
            colors[y] += 1
        return ans
    

if __name__ == "__main__":
    s = Solution()
    # print(s.queryResults(4, [[1,4],[2,5],[1,3],[3,4]]))
    # print(s.queryResults(4, [[0,1],[1,2],[2,2],[3,4],[4,5]]))
    print(s.queryResults(1, [[0,1],[0,4],[1,2],[1,5],[1,4]]))