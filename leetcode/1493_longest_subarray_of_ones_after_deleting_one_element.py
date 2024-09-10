class Solution():
    '''
        pseudo-code
        - variable sliding window
        - for loop nums, incrementing right side of the window until we hit 2 zeroes
        - in the case of no zeroes, we substract the max_length 
    '''
    def longest_subarray(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        max_length = 0
        zeroes = 0

        for right in range(n):
            if nums[right] == 0:
                zeroes += 1

            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            length = max(0, right - left)
            max_length = max(max_length, length)
        return max_length

if __name__ == "__main__":
    test = Solution()
    print(test.longest_subarray([1,1,0,1]))
    print(test.longest_subarray([0,1,1,1,0,1,1,0,1]))
    print(test.longest_subarray([1,1,1]))