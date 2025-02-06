class Solution:
    '''
        Approach
        - Assign a variable to store a max value and a current value
        - Iterate through nums, 
    '''
    def maxAscendingSum(self, nums: list[int]) -> int:
        res = 0
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                cur += nums[i]
            else:
                res = max(res, cur)
                cur = nums[i]
        return max(res, cur)


if __name__ == "__main__":
    s = Solution()
    print(s.maxAscendingSum([10,20,30,5,10,50]))
    print(s.maxAscendingSum([10,20,30,40,50]))
    print(s.maxAscendingSum([12,17,15,13,10,11,12]))