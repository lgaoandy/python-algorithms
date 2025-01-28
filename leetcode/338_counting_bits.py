class Solution:
    def count_bits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            # offset updates every power of 2 (1,2,4,8,16,...)
            if offset * 2 == i: 
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp


if __name__ == "__main__":
    s = Solution()

    print(s.count_bits(3))
    print(s.count_bits(64))