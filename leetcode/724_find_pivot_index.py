class Solution:
    '''
        pseudo-code
        - first pass, calculate left_sum: 
            left_sum[i] = left_sum[i-1] + nums[i-1]
        - second pass, calculate right_sum: 
            right_sum[i] = right_sum[i+1] + nums[i+1]
        - third pass, compare left_sum and right_sum of each index
            if left_sum[i] = right_sum[i], return i
            else return -1
    '''
    def pivot_index(self, nums: list[int]) -> int:
        n = len(nums)

        left_sum = [0]
        for i in range(n-1):
            left_sum.append(left_sum[i] + nums[i])

        right_sum = [0]
        for i in range(n-1, 0, -1):
            right_sum.insert(0, right_sum[0] + nums[i])

        for i in range(n):
            if left_sum[i] == right_sum[i]:
                return i
        return -1
    
    '''
        above solution
        - O(3n) time complexity
        - O(2n) space complexity

        further optimization
        - you can calculate right_sum through the first pass by dividing it by the sum
        - if you have both left_sum and right_sum, you can compare them right away
        - if you can compare left_sum and right_sum first pass, you can use left_sum/right_sum as int

        pseudo-code:
        - pass through nums, calculate left_sum by adding the next 
    '''
    def pivot_index_optimized(self, nums: list[int]) -> int:
        n = len(nums)
        left_sum = 0
        right_sum = sum(nums)

        for i in range(n):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1

if __name__ == "__main__":
    test = Solution()
    # print(test.pivot_index([1,7,3,6,5,6]))
    # print(test.pivot_index([1,2,3]))
    # print(test.pivot_index([2,1,-1]))
    print(test.pivot_index_optimized([1,7,3,6,5,6]))
    print(test.pivot_index_optimized([1,2,3]))
    print(test.pivot_index_optimized([2,1,-1]))
