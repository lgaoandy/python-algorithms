class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        cur = 1
        res = 1
        increasing = 0
        
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                if increasing > 0:
                    cur += 1
                else:
                    cur = 2
                    increasing = 1
            elif nums[i-1] > nums[i]:
                if increasing < 0:
                    cur += 1
                else:
                    cur = 2
                    increasing = -1
            else:
                cur = 1
                increasing = 0
            res = max(res, cur)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestMonotonicSubarray([1,4,3,3,2]))
    print(s.longestMonotonicSubarray([3,3,3,3]))
    print(s.longestMonotonicSubarray([3,2,1]))