class Solution:
    '''
        Intuition
        - Dictionary, as we iterate through nums, we can calculate the digit sum
        - Then we added the digit sum as a key in the dictionary
        - When the same digit sum is encounter, we can add them up and compare with an answer
        - Replace the whichever is the higher number to the value of the digit sum key
    '''
    def maximumSum(self, nums: list[int]) -> int:
        ''' O(n) time, O(n) space'''
        sums = {}
        ans = -1
        
        for num in nums:
            i = sum(int(d) for d in str(num))
            
            if i in sums:
                ans = max(sums[i] + num, ans)
                sums[i] = max(num, sums[i])
            else:
                sums[i] = num
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maximumSum([18,43,36,13,7]))
    print(s.maximumSum([10,12,19,14]))