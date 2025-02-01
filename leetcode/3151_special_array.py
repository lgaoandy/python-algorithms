class Solution:
    '''
        Intuition
        - iterate through nums, if first num is even, next must be odd, so on so forth
    '''
    def isArraySpecial(self, nums: list[int]) -> bool:
        is_odd = nums[0] % 2
        for i in range(1, len(nums)):
            if (is_odd and nums[i] % 2 == 0) or (not is_odd and nums[i] % 2):
                is_odd = not is_odd
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isArraySpecial([1]))
    print(s.isArraySpecial([2,1,4]))
    print(s.isArraySpecial([4,3,1,6]))