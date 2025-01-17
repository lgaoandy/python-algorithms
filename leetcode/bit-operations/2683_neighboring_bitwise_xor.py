class Solution:
    '''
        Neetcode:
        Brute Force Approach
        - Time complexity: O(n), Space: O(1)
    '''
    def neighboring_bitwise_xor(self, derived: list[int]) -> bool:
        last = 0
        for num in derived:
            if num == 1:
                last ^= 1
        return 0 == last
        

if __name__ == "__main__":
    s = Solution()
    print(s.neighboring_bitwise_xor([1,1,0]))
    print(s.neighboring_bitwise_xor([1,1]))
    print(s.neighboring_bitwise_xor([1,0]))