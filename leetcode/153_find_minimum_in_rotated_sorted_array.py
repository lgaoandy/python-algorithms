from math import floor, ceil

class Solution:
    '''
        Constriants:
        - all integers are unique, no repeated integers
        - values of nums: [-5000, 5000]

        Comments/questions for interviewer
        - N/a

        Pseudo-code
        - conceptually, the list is always sorted, to solve this problem in O(log n) time, we must find the start and end of the sorted array using binary search
        - start by getting the value of the first element and the value of the middle element in the list
        - evaluate until the start and end is found
        - then return the min value

        Analysis
        - time complexity must be O(logn)
    '''
    def findMin(self, nums: list[int]) -> int:
        min_p = 0
        max_p = len(nums) - 1
        
        # if array is perfectly sorted or is the same value (only containing one element)
        if nums[min_p] <= nums[max_p]: 
            return nums[min_p]
        else: # swap min and max pointer
            min_p, max_p = max_p, min_p

        # find the two indexes going from max to min value
        while max_p + 1 != min_p:
            i = (min_p + max_p) // 2 # get middle index (binary search)
            if nums[i] > nums[max_p]:
                max_p = i
            else: 
                min_p = i
        return nums[min_p]
        


if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3,4,5,1,2]))
    print(s.findMin([4,5,6,7,0,1,2]))
    print(s.findMin([11,13,15,17]))
    print(s.findMin([2,1]))
    print(s.findMin([3,1,2]))
    print(s.findMin([1]))