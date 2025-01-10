class Solution:
    '''
        Constriants:
        - 1 <= nums.length <= 1000
        - nums[i] != nums[i+1] for all valid i, between each two node, it is always increasing or decreasing

        Comments/questions for interviewer
        - binary search

        Pseudo-code
        - check edges first
        - if not, the worse case scenario is that there is only one peak in the array
        - start edge and end edge represents an ascending number and descending number
        - a peak is in between an ascending number and a descending number
        - use binary search to find a peak then return it

        Analysis
        - time complexity: O(logn)
        - space complexity: O(1)
    '''
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        # handle when edges are a peak or when length of nums = 1,2
        if n == 1 or nums[l+1] < nums[l]:
            return l
        elif nums[r-1] < nums[r]:
            return r

        while True:
            i = (l + r) // 2

            # 4 different scenarios - peak, ascending, descending, or valley
            if nums[i-1] < nums[i] > nums[i+1]:
                return i
            elif nums[i-1] < nums[i] < nums[i+1]:
                l = i
            else: # if valley, either l or r can be replaced, so we combine descending with valleys
                r = i


if __name__ == "__main__":
    s = Solution()

    print(s.findPeakElement([1,2,3,1])) # 2
    print(s.findPeakElement([1,2,1,3,5,6,4])) # 5
    print(s.findPeakElement([1])) # 0