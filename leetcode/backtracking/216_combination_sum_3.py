class Solution:
    '''
        Pseudo-code
        - loop through values of a set from 1 to 9, adding values to a list, until it is impossible then backtrack

        Analysis
        - 
    '''
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        nums = set([i for i in range(1, min(n + 2 - k, 9+1))])

        def backtrack(values, nums):
            m = len(values)

            if m == k and sum(values) == n and values not in result:
                result.append(values.copy())
                return
            
            for i in nums:
                values.add(i)
                nums.remove(i)
                backtrack(values, nums)
                values.remove(i)
                nums.add(i)

        backtrack(set(), nums)

        for i in range(len(result)):
            result[i] = list(result[i])
        return result
    

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(3,7))
    print(s.combinationSum3(3,9))
    print(s.combinationSum3(4,1))
    print(s.combinationSum3(9,45))
    print(s.combinationSum3(2,6))