class Solution:
    '''
        Brutal Force Approach
        - Simply we will find the XOR for every num pair then XOR across the pairs

        Analysis
        - Time complexity: O(nm)
    '''
    def xor_nums_brutal_force(self, nums1: list[int], nums2: list[int]) -> int:
        pairs = []

        # get XOR of each pair
        for i in nums1:
            for j in nums2:
                pairs.append(i ^ j)
        print(pairs)

        # get XOR of all pairs
        result = 0
        for i in pairs:
            result = result ^ i
        return result


    '''
        Pruning Approach
        - The end result is asking a XOR of all of the pairs, and order of operations does not matter for a series of XOR operation
        - Given i xor i = 0, this means every even number of occurrence of a variable is cancelled out
        - Given a num in nums1, if the length of nums2 is even, we can completely cancel out this num
        - If the length of nums2 is odd, we only need to add a single num to result
        
        Analysis
        - Time complexity: O()
    '''
    def xor_nums_pruning(self, nums1: list[int], nums2: list[int]) -> int: 
        result = 0
        n = len(nums1)
        m = len(nums2)

        # prune list
        if m % 2 == 0:
            nums1 = []
        if n % 2 == 0:
            nums2 = []
        
        for num in nums1:
            result = result ^ num
        for num in nums2:
            result = result ^ num
        return result


    '''
        Improvements from Pruning Approach
        - Instead of empty the lists, check if the opposing list is odd, then apply xor immediately
        - Predefining n and m is unnecessary since they are only used once
        - result = result ^ num can be re-written as result ^= num
    '''
    def xor_nums_pruning_written_better(self, nums1: list[int], nums2: list[int]) -> int: 
        result = 0
        if len(nums2) % 2:
            for num in nums1:
                result ^= num
        if len(nums1) % 2:
            for num in nums2:
                result ^= num
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.xor_nums_pruning([2,1,3],[10,2,5,0]))
    print(s.xor_nums_pruning([1,2],[3,4]))