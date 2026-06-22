class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0,
        }
        
        for i in text:
            if i in letters:
                letters[i] += 1
        
        return min(
            letters["b"], 
            letters["a"], 
            letters["l"] // 2, 
            letters["o"] // 2, 
            letters["n"]
        )
    

if __name__ == "__main__":
    s = Solution()
    
    print(s.maxNumberOfBalloons("nlaebolko"))
    print(s.maxNumberOfBalloons("loonbalxballpoon"))
    print(s.maxNumberOfBalloons("leetcode"))