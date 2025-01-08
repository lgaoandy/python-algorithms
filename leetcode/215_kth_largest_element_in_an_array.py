class Solution:
    '''
        constriants:
        - 1 <= k <= nums.length <= e5

        comments/questions for interviewer
        - N/A

        pseudo-code
        - sort nums then return the k ranked value

        analysis
        - time complexity: O(nlogn)
    '''
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        return nums[len(nums) - k]


    '''
        average time complexity - O(n)
        worst time complexity - O(n^2)
    '''
    def findKthLargestQuickSelect(self, nums: list[int], k: int) -> int:
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, p =  nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargestQuickSelect([3,2,1,5,6,4], 2))
    print(s.findKthLargestQuickSelect([3,2,3,1,2,4,5,5,6], 4))