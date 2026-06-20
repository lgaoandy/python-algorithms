from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # combine lists
        nums = nums1 + nums2
        n = len(nums)
        
        snums = merge(nums1)
            
        
        # merge  
        def merge(nums1: List[int], nums2: List[int]):
            

        pass


if __name__ == "__main__":
    s = Solution()
    