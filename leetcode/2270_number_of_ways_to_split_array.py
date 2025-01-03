class Solution:
    '''
        constriants:
        - 2 <= nums.length <= e5, given this we can always assume nums is never empty
        - -e5 <= nums[i] <= e5

        potential questions to ask interviewer
        - N/A

        pseudo-code
        - 2 passthroughs, populate a list of left sums then a list of right sums, using dynamic programming
        - passthrough once last time, checking if every split is valid, incrementing a count if valid

        analysis
        - time complexity: O(3n)
        - space complexity: O(2n)
    '''
    def waysToSplitArray(self, nums: list[int]) -> int:
        n = len(nums)
        l_sum = [0] * n
        r_sum = [0] * n
        count = 0

        l_sum[0] = nums[0]
        for i in range(1, n-1):
            l_sum[i] = l_sum[i-1] + nums[i]

        r_sum[n-1] = nums[n-1]
        for i in range(n-2, 0, -1):
            r_sum[i] = r_sum[i+1] + nums[i]
        
        for i in range(n-1):
            if l_sum[i] >= r_sum[i+1]:
                count += 1
        return count


    def waysToSplitArray_Optimized(self, nums: list[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        count = 0

        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            
            if left_sum >= right_sum:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.waysToSplitArray_Optimized([10,4,-8,7]))
    print(s.waysToSplitArray_Optimized([2,3,1,0]))