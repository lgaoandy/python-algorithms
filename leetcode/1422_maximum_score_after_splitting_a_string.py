class Solution:
    '''
        constriants:
        - 2 <= s.length <= 500, we can assume str input is never empty

        potential questions to ask interviewer
        - N/A

        pseudo-code
        - calculate all instance of ones and initialize right score
        - loop through string, adding to left score and subtracting right and compare

        analysis
        - 
    '''
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0
        max_score = 0

        # compute inital right score
        for i in s:
            if i == "1":
                right += 1

        for i in range(len(s) - 1):
            if s[i] == "1":
                right -= 1
            else:
                left += 1
            max_score = max(max_score, left + right)
        return max_score
    

if __name__ == "__main__":
    s = Solution()
    print(s.maxScore("011101"))
    print(s.maxScore("00111"))
    print(s.maxScore("1111"))
    print(s.maxScore("00"))