class Solution:
    '''
        Learning sample
    '''
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        telephone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(i, current):
            if len(current) == len(digits):
                res.append(current)
                return
            
            for c in telephone[digits[i]]:
                backtrack(i + 1, current + c)

        if digits:
            backtrack(0, "")
        return res
            

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))