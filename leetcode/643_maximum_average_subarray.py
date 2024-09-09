class Solution():
    '''
        pseudo-code:
        - sliding window technique over nums
        - each window of length k values is average and compared to the max_average
    '''
    def find_max_average(self, nums: list[int], k: int) -> float:
        max_average = float('-inf')
        for i in range(0, len(nums) - k + 1):
            average = 0
            for j in range(i, i + k):
                average += nums[j]
            max_average = max(max_average, average/k)
        return max_average
    
    '''
        - instead of calculating the average per window, change left and right values 
    '''
    def find_max_average_optimized(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_average = window_sum / k
        
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]
            max_average = max(max_average, window_sum / k)

        return max_average

if __name__ == "__main__":
    test = Solution()
    # print(test.find_max_average([1,12,-5,-6,50,3], 4))
    # print(test.find_max_average([5], 1))
    print(test.find_max_average_optimized([1,12,-5,-6,50,3], 4))
    print(test.find_max_average_optimized([5], 1))