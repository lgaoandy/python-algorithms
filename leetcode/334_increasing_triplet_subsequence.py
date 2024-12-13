class Solution:
    '''
        Pseudo-code
        - setup 3 variables, min, mid, start
        - loop through nums, until min and mid is set
            - if min is not set, set to min
            - if min is set and num is smaller than min, update min
            - if min is set and num is greater than min, set mid
            - when min and mid are set, save index as start
        - loop through nums from start
            - if num is less than min, update min
            - if num is greater than min but less than mid, update mid
            - if num is greater than min and mid, return true
        - return false end of loop
    '''
    def increasing_triplet(self, nums: list[int]) -> bool:
        min, mid, start = None, None, None
        for i in range(len(nums)):
            if min == None or nums[i] < min:
                min = nums[i]
            elif nums[i] > min:
                mid = nums[i]
                start = i + 1
                break

        if mid == None:
            return False
        
        for i in range(start, len(nums), 1):
            print(i, nums[i])
            if nums[i] < min:
                min = nums[i]
            elif nums[i] > min and nums[i] < mid:
                mid = nums[i]
            elif nums[i] > mid:
                return True
        return False

    '''
        Optimizations:
        - use infinity instead of nonetype to skip the filling loop
        - avoid using min as a variable
    '''
    def increasing_triplet_optimized(self, nums: list[int]) -> bool:
        first = second = float("inf")
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.increasing_triplet_([1,2,3,4,5]))
    print(solution.increasing_triplet([5,4,3,2,1]))
    print(solution.increasing_triplet([2,1,5,0,4,6]))
    print(solution.increasing_triplet([1,1,-2,6]))
    print(solution.increasing_triplet_optimized([1,2,3,4,5]))
    print(solution.increasing_triplet_optimized([5,4,3,2,1]))
    print(solution.increasing_triplet_optimized([2,1,5,0,4,6]))
    print(solution.increasing_triplet_optimized([1,1,-2,6]))