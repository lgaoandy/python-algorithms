class Solution:
    '''
        Dynamic Programming Approach
        - populate an array in the same size of nums, each index represents the minimum jumps to reach the current index in nums
    '''
    def jumpDP(self, nums: list[int]) -> int:
        ''' O(n) time, O(n) space '''
        n = len(nums)
        min_jumps = [0] * n
        
        cur_jump = 0
        cur_range = nums[0]
        next_range = 0
        for i in range(1, n):
            min_jumps[i] = cur_jump + 1
            next_range = max(nums[i], next_range - 1)
            cur_range -= 1

            if cur_range == 0:
                cur_jump += 1
                cur_range = next_range
                next_range = 0
        return min_jumps[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.jumpDP([2,3,1,1,4]))
    print(s.jumpDP([2,3,0,1,4]))
    print(s.jumpDP([2,1]))
    print(s.jumpDP([0]))
    print(s.jumpDP([2,1,1,1,1]))