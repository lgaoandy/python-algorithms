from collections import Counter

class Solution():
    '''
        pseudo-code:
        - loop through array, make a hash map for different values
        - loop through copy of array, check if a number exists to sum to k in hash map
            - if exist, add remove both nums
    '''
    def max_operations(self, nums: list[int], k: int) -> int:
        hashmap = {}
        count = 0

        for i in range(len(nums)):
            num = nums[i]
            if num not in hashmap:
                hashmap[num] = []
            hashmap[num].append(i)
    
        i = 0
        while i < len(nums):
            num = nums[i]
            if isinstance(num, int):
                addend = k - num
                if addend in hashmap.keys():
                    j = -1
                    for x in range(len(hashmap[addend])):
                        if hashmap[addend][x] != i and nums[hashmap[addend][x]] != None:
                            j = hashmap[addend].pop(x)
                            break
                    
                    if j != -1:
                        nums[i], nums[j] = None, None
                        count += 1
                        if len(hashmap[num]) == 0:
                            del hashmap[num]
            i += 1

        nums = [x for x in nums if x != None]
        print(nums)
        return count
    
    '''
        Optimal solution by PHIND
        - use a hashmap to count the number of occurrence for each num
        - for every unique num, find the complement num, if complement exists, add to total_pairs
        - result is total_pairs divided by 2 
            (because 2 and 5, 5 and 2 are the same pairs)
    '''
    def max_operations_optimized(self, nums: list[int], k: int) -> int:
        count = Counter(nums)
        total_pairs = 0
        for num in set(nums):
            complement = k - num
            if complement in count:
                total_pairs += min(count[num], count[complement])
        return total_pairs // 2
                            

if __name__ == "__main__":
    test = Solution()
    # print(test.max_operations([1,2,3,4], 5))
    # print(test.max_operations([3,1,3,4,3], 6))
    print(test.max_operations_optimized([1,2,3,4], 5))
    print(test.max_operations_optimized([3,1,3,4,3], 6))