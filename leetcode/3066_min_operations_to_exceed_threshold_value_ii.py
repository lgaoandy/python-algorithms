from heapq import heapify, heappush, heappop

class Solution:
    '''
        Intuition
        - We want to perform operations to the lowest nums in an array, and transform them, until all values are greater than k
        - Using a min heap would be a strong solution

        Min Heap Approach
        - Convert nums into min heap
        - Check the lowest value - if it is greater than or equal to k, return count
        - Else, we pop the first two values and heappush the transform value, then repeat
    '''
    def minOperations(self, nums: list[int], k: int) -> int:
        count = 0
        heapify(nums)
        
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, 2*x + y)
            count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([2,11,10,1,3], 10))
    print(s.minOperations([1,1,2,4,9], 20))