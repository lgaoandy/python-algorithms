class Solution:
    '''
        Dynamic Programming Approach
        - Time complexity: O(n)
        - Space complexity: O(n)
            
    '''
    def tribonacci(self, n: int) -> int:
        # Define first 3 values of sequence
        sequence = [0, 1, 1]
        
        # Add to sequence up to n
        for i in range(3, n+1):
            sequence.append(sequence[i-1] + sequence[i-2] + sequence[i-3])
            
        # Return value of the nth sequence
        return sequence[n]
    
    
    '''
        - [Aftermath] To optimize space further, use 3 variables to replace the array
    '''
    def tribonacci(self, n: int) -> int:
        v0, v1, v2 = 0, 1, 1
        if n == 0:
            return v0
        elif n == 1:
            return v1
        
        for _ in range(2, n):
            v0, v1, v2 = v1, v2, v0 + v1 + v2
        return v2
    

if __name__ == "__main__":
    s = Solution()
    
    print(s.tribonacci(4))
    print(s.tribonacci(25))