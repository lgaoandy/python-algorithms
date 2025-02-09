class Solution:
    '''
        Intuition
        - Possible pairs = permutation of 2 of all indexes 
        - A good pair between two indexes is that the difference in their distance is the same in their value
    '''
    def countBadPairsBruteForce(self, nums: list[int]) -> int:
        ''' Brute Force - O(n^2) time '''
        n = len(nums)
        count = 0
        
        for i in range(n):
            for j in range(i, n):
                if j - i  != nums[j] - nums[i]:
                    count += 1
        return count


    '''
        Intuition:
        - Since a good pair is the the same value plus the distance between the two indexes, we can essentially calculate the value of each index if it is at zero
        - Therefore, every value that is equal to another value is a good pair
        - We can store the frequency of each value into a hash table
    '''
    def countBadPairs(self, nums: list[int]) -> int:
        frequency = {}
        good_pairs = 0
        n = len(nums)
        
        for i in range(n):
            base_value = nums[i] - i
            good_pairs += frequency.get(base_value, 0)
            frequency[base_value] = frequency.get(base_value, 0) + 1
        return (n * (n - 1)) // 2 - good_pairs


if __name__ == "__main__":
    s = Solution()
    print(s.countBadPairs([4,1,3,3]))
    print(s.countBadPairs([1,2,3,4,5]))