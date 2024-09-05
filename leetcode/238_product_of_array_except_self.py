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
    
    '''
        Weaknesses from phind
        - high space complexity O(n) due to creating temporary lists for each element
        - high time complexity O(n^2) because every element uses math.prod which has a time complexity of O(n)

        Pseudo code
        1) initiaize 2 arrays
        2) first pass, calculate running prefix product
        3) second pass, calculate running suffix product
        3) multiply corresponding elements from both arrays
    '''
    def product_except_self_optimized(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = []
        prefix_product, suffix_product = [1] * n, [1] * n

        for i in range(n - 1):
            prefix_product[i+1] = nums[i] * prefix_product[i]

        for i in range(n - 1, 0, -1):
            suffix_product[i-1] = nums[i] * suffix_product[i]

        for i in range(n):
            result.append(prefix_product[i] * suffix_product[i])

        return result
    
if __name__ == "__main__":
    solution = Solution()
    # print(solution.product_except_self([1,2,3,4]))
    # print(solution.product_except_self([-1,1,0,-3,3]))
    print(solution.product_except_self_optimized([1,2,3,4]))
    print(solution.product_except_self_optimized([-1,1,0,-3,3]))

# What I learned
# - when optimizing solutions from O(n^2) to O(n), consider having multiple O(n) passes
