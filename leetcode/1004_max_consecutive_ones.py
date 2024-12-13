class Solution:
    '''
        pseudo-code
        - variable sliding window
        - start with two pointers, left & right of the window, defaulting to 0
        - loop nums: increment right and record max until amount of 0s exceeds k, then increment left until equals to k
        - end of loop: when right reaches end of nums, return max
    '''
    def longest_ones(self, nums: list[int], k: int) -> int:
        left, right = 0, 0
        max_length = 0
        zeroes = nums[right] == 0

        while right < len(nums):
            if zeroes <= k:
                max_length = max(max_length, right - left + 1)
                right += 1
                if right in range(len(nums)) and nums[right] == 0:
                    zeroes += 1
            else: 
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
        return max_length

    '''
        improvements from PHIND:
        - use k instead of zeros
        - single-pass approach: instead of maintaining two pointers throughout the loop, move right pointer forward and adjust left only when necessary
    '''
    def longest_ones_optimized(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = 0
        max_length = 0
        
        for right in range(n):
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

if __name__ == "__main__":
    test = Solution()
    print(test.longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2))
    print(test.longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))