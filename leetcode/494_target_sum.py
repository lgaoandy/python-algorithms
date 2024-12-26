class Solution:
    def target_sum(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        
        if total_sum < target or (total_sum - target) % 2 != 0:
            return 0
        
        subset_sum = (total_sum - target) // 2
        
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        print(dp)
        
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.target_sum([1,1,1,1,1], 3))
    print(s.target_sum([1,2,1,1,2,3,1,1,1], 3))
    print(s.target_sum([1], 1))