from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count
    

if __name__ == "__main__":
    s = Solution()
    print(s.numOfStrings(["a", "abc", "bc", "d"], "abc")) # ans: 3
    print(s.numOfStrings(["a", "b", "c", "d"], "aaaaabbbbb")) # ans: 2
    print(s.numOfStrings(["a", "a", "a"], "ab")) # ans: 3