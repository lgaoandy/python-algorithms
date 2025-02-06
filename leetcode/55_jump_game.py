from collections import deque

class Solution:
    '''
        Approach
        - Using a queue, we can check any possible jump locations to the next
        - Using a set to track visited indexes to avoid visiting repeated indexes
    '''
    def canJumpBFS(self, nums: list[int]) -> bool:
        ''' O(n) time, O(n) space '''
        n = len(nums)

        # check base case
        if n == 1:
            return True
        
        q = deque([0]) # initialize queue from start (index 0)
        visited = set()

        while q:
            i = q.popleft()

            visited.add(i)
            for j in range(i + nums[i], i, -1):
                if j in visited or j in q:
                    continue
                if j == n - 1:
                    return True
                q.append(j)
        return False


    def canJumpDFS(self, nums: list[int]) -> bool:
        ''' O(n) time, O(n) space '''
        n = len(nums)
        visited = set()

        def dfs(i):
            if i in visited:
                return
            if i == n - 1:
                return True
            
            visited.add(i)
            for j in range(i+1, i+nums[i]+1):
                if dfs(j):
                    return True
            return False
        return dfs(0)


    def canJump(self, nums: list[int]) -> bool:
        ''' O(n) time, O(1) space '''
        n = len(nums)
        goal = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
    print(s.canJump([1,1,1,0,0]))