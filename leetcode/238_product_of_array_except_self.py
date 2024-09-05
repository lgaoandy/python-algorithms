import math

class Solution:
    '''
        Pseudo code
        1) Set up array
        2) loop through list, create a new list without the current element
        3) use math.prod() to get results
    '''
    def product_except_self(self, nums: list[int]) -> list[int]:
        array = []
        for i in range(len(nums)):
            temp_nums = nums[:i] + nums[i+1:]
            array.append(math.prod(temp_nums))
        return array
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.product_except_self([1,2,3,4]))
    print(solution.product_except_self([-1,1,0,-3,3]))