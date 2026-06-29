from typing import List

'''
    Constraints:
    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^9
    - 1 <= target <= 10^9
    
    Thoughts:
    - This problem is the same as #3737 except the constraints are no longer small - 10^5 which will make the previous O(n^2) solution too slow
    - We need a way to solve this same problem but only iterating nums ONCE: 2D prefix sum 
    
    Let's take a look at the first example:
        nums:               [ 1 ] [ 2 ] [ 2 ] [ 3 ] [ 2 ]    target = 2
       
        prefix [0:]:        [ -1] [ 0 ] [ 1 ] [ 0 ] [ 1 ]    for these presums, we need to start an prefix sum array for each 
        prefix [1:]:              [ 1 ] [ 2 ] [ 1 ] [ 2 ]    element of nums in order to check from each possible subarray. The rules:
        prefix [2:]:                    [ 1 ] [ 0 ] [ 1 ]        - If the current num is target, +1
        prefix [3:]:                          [ -1] [ 0 ]        - Else, -1
        prefix [4:]:                                [ 1 ]        - Else, -1
        
        sum of subarrays:   [ 0 ] [ 1 ] [ 3 ] [ 1 ] [ 4 ]    for every presum bracket with a value of one or greater, add one
        prefix sum:         [ 0 ] [ 1 ] [ 4 ] [ 5 ] [ 9 ]    
        -------------------------------------------------
        Translates into dp:
        prefix [0:]:        [ -1] [ 0 ] [ 1 ] [ 0 ] [ 1 ]
        
        prefix [0:]:        [ 0 ] [ 0 ] [ 1 ] [ 0 ] [ 1 ]    
        prefix [1:]:              [ 1 ] [ 3 ] [ 4 ] [ 3 ]    
        prefix [2:]:                    [ 4 ] [ 5 ] [ 3 ]    
        prefix [3:]:                          [ 5 ] [ 3 ]    
'''

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        dp = [[0] for _ in range(n) ] * n
        count = 0
        for i in range(n):
            count +=  1 if nums[i] == target else -1
            
        


if __name__ == "__main__":
    s = Solution()
    
    print(s.countMajoritySubarrays([1,2,2,3], 2)) # expected 5
    print(s.countMajoritySubarrays([1,1,1,1], 1)) # expected 10
    print(s.countMajoritySubarrays([1,2,3], 4)) # expected 0