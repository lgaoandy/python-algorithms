class Solution:
    '''
        Approach
        - If numbers descend more than once, return false
    '''
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        ascended = nums[n-1] > nums[0]
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                if ascended:
                    return False
                ascended = True
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.check([3,4,5,1,2]))
    print(s.check([2,1,3,4]))
    print(s.check([1,2,3]))