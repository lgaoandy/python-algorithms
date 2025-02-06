class Solution:
    '''
        Intuition
        - Given a tuple, every 4 valid numbers constructs 8 valid tuples due to permutations
        - Given there are 3 pairs of numbers or more, the answer would be the combination of the 3 pairs

        Approach
        - Iterate through nums, storing products of every pair on a hash table
        - Iterate through products, and return answer
    '''
    def tupleSameProductBruteForce(self, nums: list[int]) -> int:
        ''' O(n!) time, O(n) space '''
        n = len(nums)
        products = {}
        
        for i in range(n-1):
            for j in range(i+1, n):
                p = nums[i] * nums[j]
                products[p] = products.get(p, 0) + 1
        
        ans = 0
        for i in products.values():
            if i > 1:
                ans += int(i*(i-1)/2) * 8
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.tupleSameProductBruteForce([2,3,4,6]))
    print(s.tupleSameProductBruteForce([1,2,4,5,10]))
    print(s.tupleSameProductBruteForce([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]))