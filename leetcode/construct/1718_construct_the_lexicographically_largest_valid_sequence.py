class Solution:
    '''
        Intuition
        - Finding the lexicographically largest sequence - always want to start with the largest value n
        - Pattern-wise adjacent numbers (1,2) cannot be beside each other, therefore we always decrement by 2
        - Some dry runs:
            - n = 1: [1], len = 1
            - n = 2: [2,1,2], len = 3
            - n = 3: [3,1,2,3,2], len = 5
            - n = 4: [4,2,3,2,4,3,1], len = 7
            - n = 5: [5,3,1,4,3,5,2,4,2] len = 9

        Greedy Backtracking Approach
        - Initialize an array of expected length (length = 2n - 1)
        - Define a backtracking function where the highest numbers are prioritized 
    '''
    def constructDistancedSequence(self, n: int) -> list[int]:
        m = 2*n - 1
        res = [-1] * m
        
        nums = set(i for i in range(1, n+1))
        def sequence(i):
            while i < m and res[i] != -1:
                i += 1
            
            if i >= m and len(nums) == 0:
                return True
            
            for num in range(n, 1, -1): # from largest to smallest 2 to n
                if num not in nums or i+num >= m or res[i+num] != -1:
                    continue 
                
                res[i] = num
                res[i+num] = num
                nums.remove(num)
                
                if sequence(i+1):
                    return True
                
                res[i] = -1
                res[i+num] = -1
                nums.add(num)
            
            if 1 in nums:
                res[i] = 1
                nums.remove(1)
                if sequence(i+1):
                    return True
                res[i] = -1
                nums.add(1)
                
        sequence(0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.constructDistancedSequence(3))
    print(s.constructDistancedSequence(4))
    print(s.constructDistancedSequence(5))
    print(s.constructDistancedSequence(6))
    print(s.constructDistancedSequence(12))