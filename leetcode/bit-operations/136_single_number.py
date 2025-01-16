from collections import Counter

class Solution:
    '''
        Hash Table Approach
        - Iterate through nums, record the occurrence of each number
        - Time complexity: O(n)
        - Space complexity: O(n)
    '''
    def single_number(self, nums: list[int]) -> int:
        occurrences = { i:0 for i in nums }
        for i in nums:
            occurrences[i] += 1

        for i in occurrences.keys():
            if occurrences[i] == 1:
                return i
        return 0


    '''
        Bitwise Operation Approach
        - Take the XOR of all nums in the list and return
    '''
    def single_number_bitwise(self, nums: list[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.single_number_bitwise([2,2,1]))
    print(s.single_number_bitwise([4,1,2,1,2]))