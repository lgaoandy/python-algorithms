class Solution:
    '''
        Constriants:
        - length of s == length of locked
        - length range: [1, e5], so it cannot be empty

        Comments/questions for interviewer
        - Can parentheses overlap each other or contain another pair of parentheses? 
            upon reading the question more careful, I deducted yes
        
        Intuition
        - For a group of parentheses to be valid, the following must be true
            - total number of start and end parenthese must be equal - "(" == ")"
            - from left to right, the number of end parenthese can never exceed the number of start parentheses
            - indirectly, the length s must always be even

        Pseudo-code
        - Since we change the parentheses, we only need to check every variable in locked and conditionally what is being locked
            - length of s must be even
            - check the number of locked end parenthese must never be greater than unlocked parathesis from left to right
            - the last string cannot be a start parenthese

        Analysis
        - time complexity: O(n)
        - space complexity: O(1)
    '''
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2:
            return False
        
        # check at every instance, the number of end parentheses can be greater
        end = 0
        for i in range(n):
            if locked[i] == "1" and s[i] == ")":
                end += 1
            if end > i + 1 - end:
                return False
        
        # check at every instance, the number of start parentheses can be greater
        start = 0
        for i in range(n-1, -1, -1):
            if locked[i] == "1" and s[i] == "(":
                start += 1
            if start > (n - 1 - i) + 1 - start:
                return False
        return True
    
    

if __name__ == "__main__":
    s = Solution()
    print(s.canBeValid("))()))", "010100"))
    print(s.canBeValid("()()", "0000"))
    print(s.canBeValid(")", "0"))
    print(s.canBeValid(")(", "00"))
    print(s.canBeValid("())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(", "100011110110011011010111100111011101111110000101001101001111"))