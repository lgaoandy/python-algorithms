from typing import List

'''
    Constraints:
    - 1 <= nums.length <= 1000
    - 1 <= nums[i] <= 10^9
    - 1 <= target <= 10^9

    Thoughts:
    - *Majority element* - the element that appears strictly more than half of the times in that subarray
    - Based on constraints - 0 < n < 1000, we can perform an numeration on every possible subarray
    
    - *Two pointers* approach - set two pointers, starting from the first index
        - pointer 1: indicates the start of the subarray
        - pointer j: indicates the end of the subarray
        - In first loop, iterate i, then iterate j with second loop
        
    - *Numeration* strategy - every j loop, i changes, set a new counter starting zero
        - As we iterate j, we check whether the current index is the target, if so, increase counter by one, else reduce counter by one
        - As we are trying if the current subarray representing i and j, has the majority element, any subarray with a counter of 1 or more is a majority element
    
    Time complexity: O(n^2)
    Space complexity: O(n)
'''

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        m_subarrays = 0
        for i in range(n):
            count = 0
            for j in range(i, n):
                count += 1 if nums[j] == target else -1
                if count >= 1:
                    m_subarrays += 1
                    
        return m_subarrays


if __name__ == "__main__":
    s = Solution()
    
    print(s.countMajoritySubarrays([1,2,2,3], 2)) # expected 5
    print(s.countMajoritySubarrays([1,1,1,1], 1)) # expected 10
    print(s.countMajoritySubarrays([1,2,3], 4)) # expected 0