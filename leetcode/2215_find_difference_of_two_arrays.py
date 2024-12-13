class Solution:
    '''
        pseudo-code based on PHIND approach hints
        - convert input arrays into sets for efficient lookup & comparison
        - use set operations to find the difference between 2 sets
    '''
    def find_difference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        for num in set1.copy():
            if num in set2:
                set1.remove(num)
                set2.remove(num)
        return [list(set1), list(set2)]

    '''
        python has in-built set methods
        - set1.difference(set2) returns the difference 
        - set1 - set2 is the same as set1.difference(set2)
        - .difference_update() is also available, updating the parent set instead of returning a new set
    '''
    def find_difference_optimized(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]

if __name__ == "__main__":
    test = Solution()
    # print(test.find_difference([1,2,3],[2,4,6]))
    # print(test.find_difference([1,2,3,3],[1,1,2,2]))
    print(test.find_difference_optimized([1,2,3],[2,4,6]))
    print(test.find_difference_optimized([1,2,3,3],[1,1,2,2]))